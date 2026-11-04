#!/usr/bin/env python3
"""Score the pooling study: four predictions over protest events, each a verdict.

    python score.py --events FILE [FILE ...] [--out RESULT.json]
                    [--box BOX --willow WILLOW_DIR]

FILE is a Crowd Counting Consortium compiled file (.tab or .csv, any of the
three phases) or a synthetic file from synth.py; every file is read into one
common shape first (see `normalize`). With --box, each verdict is appended to
that willow record as a `verdict` row, with the SHA-256 of every input file and
of this script, through the kernel's own `append`. Nothing here seals.

Every rule below is the one PLAN.md states. A change to a rule is a change to
this file, and so a new freeze.

Standard library only. Exit 0 when every prediction is `pooling`, 42 otherwise.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import statistics
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

# ---- the frozen window and rules (PLAN.md, "Rules") ------------------------

# Two full presidential terms, noon 20 January 2017 to noon 20 January 2025.
FIRST_DAY, LAST_DAY = "2017-01-20", "2025-01-19"
START, END = (2017, 1), (2025, 1)
WARMUP = 3  # January to March 2017: counted by Google search alone, and the
#             months in which a county's "first" month means nothing
BURST_X = 1.5  # a burst month: active counties >= 1.5 x its calendar year's median
FOLLOW = 12  # months followed after a recruit month or a burst

# Verdict thresholds, one pair per prediction: (pooling at or above, against at or below).
P1_STEP = (1.1, 1.0)  # quiet-level step after bursts / after placebo months, both variants
SIDE = 6  # quiet months on each side of a burst (or placebo) month
BREAKS = [(2021, 1)]  # coverage breaks a step window may not straddle (Phase 2 began)
LOCKDOWN = [(2020, 3), (2020, 4), (2020, 5)]  # never in a step window, nor a placebo month
P2_RATIO = (0.85, 0.65)  # burst-recruit retention / quiet-recruit retention
P3_RR = (0.95, 0.85)  # cross-issue carryover ratio after bursts / after placebo months
P4_RATIO = (0.8, 0.5)  # returning-organization share, burst / quiet months


# ---- reading ---------------------------------------------------------------


def month_index(y: int, m: int) -> int:
    return (y - START[0]) * 12 + (m - START[1])


N_MONTHS = month_index(*END) + 1


def year_of(i: int) -> int:
    return START[0] + (START[1] - 1 + i) // 12


EMPTY = {"na", "n/a", "none", "nan", "null"}  # placeholders the files use for a blank


def split(s: str) -> list[str]:
    return [t for t in (x.strip().lower() for x in s.replace(",", ";").split(";"))
            if t and t not in EMPTY]


def labor_strike(kind: str) -> bool:
    """A labor strike among an event's types. A hunger strike is a protest,
    not a work stoppage, and stays in."""
    return any("strike" in t and "hunger" not in t for t in split(kind))


def normalize(row: dict) -> dict | None:
    """One event in the common shape, or None when it is out of scope.

    Out of scope: no date in the window, no county, online only, or a labor
    strike (CCC stopped coding strikes in April 2023; its codebook's carve-out
    keeps the student climate "strikes" of the late 2010s, valence 1 with an
    environment tag, and a hunger strike is not a labor strike). A field that
    holds only a placeholder such as "NA" is empty."""
    date = (row.get("date") or "").strip()[:10]
    if not FIRST_DAY <= date <= LAST_DAY:
        return None
    try:
        y, m = int(date[:4]), int(date[5:7])
    except ValueError:
        return None
    i = month_index(y, m)
    if not 0 <= i < N_MONTHS:
        return None
    fips = (row.get("fips_code") or "").strip().split(".")[0]
    if not fips.isdigit():
        return None
    if (row.get("online") or "").strip() in ("1", "1.0"):
        return None
    issues = split(row.get("issue_tags") or row.get("issues") or "")
    kind = (row.get("event_type") or row.get("type") or "").lower()
    valence = (row.get("valence") or "").strip().split(".")[0]
    if labor_strike(kind) and not (valence == "1" and "environment" in issues):
        return None
    try:
        size = int(float(row.get("size_cat") or 0))
    except ValueError:
        size = 0
    return {
        "month": i,
        "county": fips.zfill(5),
        "size": size,
        "issues": issues,
        # Phase 1 has `actors` (organizations and kinds of people mixed); only
        # Phases 2 and 3 have `organizations`, so P4 reads only those.
        "orgs": split(row.get("organizations") or ""),
    }


def read(paths: list[Path]) -> list[dict]:
    events = []
    for p in paths:
        # The compiled Phase 1 and 2 files hold a few dozen bytes that are not
        # UTF-8; they are read as U+FFFD, in free-text fields only.
        with p.open(encoding="utf-8", errors="replace", newline="") as f:
            dialect = "excel-tab" if p.suffix in (".tab", ".tsv") else "excel"
            for row in csv.DictReader(f, dialect=dialect):
                e = normalize(row)
                if e:
                    events.append(e)
    return events


# ---- the series -------------------------------------------------------------


def active(events: list[dict], keep=lambda e: True) -> list[set[str]]:
    """The counties with at least one kept event, month by month."""
    out = [set() for _ in range(N_MONTHS)]
    for e in events:
        if keep(e):
            out[e["month"]].add(e["county"])
    return out


def bursts(act: list[set[str]]) -> list[bool]:
    """A burst month has at least BURST_X times its calendar year's median
    count of active counties. A year's median absorbs coverage that grows from
    year to year, so a burst is high for its own year."""
    by_year: dict[int, list[int]] = {}
    for i, s in enumerate(act):
        by_year.setdefault(year_of(i), []).append(len(s))
    med = {y: statistics.median(v) for y, v in by_year.items()}
    return [len(s) >= BURST_X * med[year_of(i)] and len(s) > 0 for i, s in enumerate(act)]


def spearman(xs: list[float], ys: list[float]) -> float:
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2
            i = j + 1
        return r

    rx, ry = ranks(xs), ranks(ys)
    mx, my = statistics.mean(rx), statistics.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else 0.0


def verdict(value: float | None, rule: tuple[float, float]) -> str:
    if value is None:
        return "inconclusive"
    if value >= rule[0]:
        return "pooling"
    if value <= rule[1]:
        return "against"
    return "inconclusive"


# ---- the four predictions ---------------------------------------------------


_LOCK = {month_index(*x) for x in LOCKDOWN}


def _sides(b: list[bool], m: int) -> tuple[list[int], list[int]]:
    """The SIDE quiet months before and after month m, skipping bursts and the
    spring 2020 lockdown, when protest fell for reasons that had nothing to do
    with capacity."""
    def quiet(j):
        return not b[j] and j not in _LOCK
    before = [j for j in range(m - 1, -1, -1) if quiet(j)][:SIDE]
    after = [j for j in range(m + 1, N_MONTHS) if quiet(j)][:SIDE]
    return before, after


def _windows(b: list[bool]) -> tuple[list[int], list[int]]:
    """Burst months and placebo months that have SIDE quiet months on each side
    inside the window, with no coverage break between the first and last of
    them. A placebo month is a quiet month at least SIDE months from any burst."""
    breaks = [month_index(*x) for x in BREAKS]
    def ok(m):
        before, after = _sides(b, m)
        if len(before) < SIDE or len(after) < SIDE:
            return None
        if any(before[-1] < k <= after[-1] for k in breaks):
            return None
        return before, after
    near = {j for m in range(N_MONTHS) if b[m] for j in range(m - SIDE, m + SIDE + 1)}
    bursts_ok = [m for m in range(N_MONTHS) if b[m] and ok(m)]
    placebo = [m for m in range(N_MONTHS)
               if not b[m] and m not in near and m not in _LOCK and ok(m)]
    return bursts_ok, placebo


def _gmean(v: list[float]) -> float | None:
    v = [x for x in v if x > 0]
    return math.exp(sum(map(math.log, v)) / len(v)) if v else None


def p1_floor(events: list[dict]) -> dict:
    """Rising floor, as a step: for each burst month, the median count of
    active counties over the SIDE quiet months after it, over the SIDE quiet
    months before it. Coverage that grows on its own moves every month alike,
    so the same step is taken around placebo months, and the burst step is
    divided by the placebo step. Pooling needs that ratio at P1_STEP[0] or more
    in both variants: all events, and events of 100 people or more."""
    out = {}
    variants = (("all", lambda e: True), ("100+", lambda e: e["size"] >= 2))
    for name, keep in variants:
        act = active(events, keep)
        b = bursts(act)
        bm, pm = _windows(bursts(active(events)))
        def step(m):
            bef, aft = _sides(b, m)
            lo = statistics.median(len(act[j]) for j in bef)
            return statistics.median(len(act[j]) for j in aft) / lo if lo else None
        sb = _gmean([x for x in map(step, bm) if x])
        sp = _gmean([x for x in map(step, pm) if x])
        out[name] = {"burst_step": None if sb is None else round(sb, 4),
                     "placebo_step": None if sp is None else round(sp, 4),
                     "ratio": round(sb / sp, 4) if sb and sp else None,
                     "bursts": len(bm), "placebos": len(pm)}
    ratios = [v["ratio"] for v in out.values()]
    if None in ratios:
        v = "inconclusive"
    elif min(ratios) >= P1_STEP[0]:
        v = "pooling"
    elif max(ratios) <= P1_STEP[1]:
        v = "against"
    else:
        v = "inconclusive"
    return {"verdict": v, "variants": out, "rule": P1_STEP}


def p2_retention(events: list[dict]) -> dict:
    """Spread that sticks: a county's first active month after the warm-up is
    its recruit month. Retained: active in at least one quiet month among the
    FOLLOW months after it. Pooling needs burst recruits to be retained at
    least P2_RATIO[0] times as often as quiet recruits."""
    act = active(events)
    b = bursts(act)
    first: dict[str, int] = {}
    for i, s in enumerate(act):
        for c in s:
            first.setdefault(c, i)
    groups = {"burst": [0, 0], "quiet": [0, 0]}
    for c, i in first.items():
        if i < WARMUP or i + FOLLOW >= N_MONTHS:
            continue
        g = "burst" if b[i] else "quiet"
        groups[g][0] += 1
        groups[g][1] += any(c in act[j] and not b[j] for j in range(i + 1, i + 1 + FOLLOW))
    rates = {g: (k / n if n else None) for g, (n, k) in groups.items()}
    ratio = (rates["burst"] / rates["quiet"]
             if rates["burst"] is not None and rates["quiet"] else None)
    return {"verdict": verdict(ratio, P2_RATIO), "ratio": None if ratio is None else round(ratio, 4),
            "recruits": {g: n for g, (n, _) in groups.items()},
            "retained": {g: k for g, (_, k) in groups.items()}, "rule": P2_RATIO}


def _carryover(events: list[dict], act, b, months: list[int]) -> tuple[float | None, dict]:
    by_month: dict[int, list[dict]] = {}
    for e in events:
        by_month.setdefault(e["month"], []).append(e)
    bins = {"1-2": [0, 0, 0, 0], "3-5": [0, 0, 0, 0], "6+": [0, 0, 0, 0]}  # nS, kS, nC, kC
    for m in months:
        if m < FOLLOW or m + FOLLOW >= N_MONTHS:
            continue
        counts: dict[str, int] = {}
        for e in by_month.get(m, []):
            for t in e["issues"]:
                counts[t] = counts.get(t, 0) + 1
        if not counts:
            continue
        top = max(sorted(counts), key=counts.get)
        s_set = {e["county"] for e in by_month.get(m, []) if top in e["issues"]}
        prior: dict[str, int] = {}
        for j in range(m - FOLLOW, m):
            for c in act[j]:
                prior[c] = prior.get(c, 0) + 1
        c_set = {c for c in prior if c not in act[m]}
        later: dict[str, int] = {}
        for j in range(m + 1, m + 1 + FOLLOW):
            if b[j]:
                continue
            for c in {e["county"] for e in by_month.get(j, []) if top not in e["issues"]}:
                later[c] = later.get(c, 0) + 1
        for group, members in (("S", s_set), ("C", c_set)):
            for c in members:
                k = prior.get(c, 0)
                if k == 0:
                    continue
                key = "1-2" if k <= 2 else "3-5" if k <= 5 else "6+"
                off = 0 if group == "S" else 2
                bins[key][off] += 1
                bins[key][off + 1] += later.get(c, 0)
    num = den = 0.0
    for nS, kS, nC, kC in bins.values():
        if nS and nC and kC:
            num += kS
            den += nS * (kC / nC)
    return (num / den if den else None), bins


def p3_carryover(events: list[dict]) -> dict:
    """Carryover across issues: after each burst month, counties that turned
    out on its top issue (S) against counties active in the FOLLOW months
    before it that stayed home (C), each stratified by how many of those prior
    months they were active. Outcome: how many of the quiet months that
    follow hold an event on any other issue. The ratio is S's months over what
    C's rates predict for S. Active counties stay active anyway, so the same ratio is
    taken around placebo months, and the burst ratio is divided by it."""
    act = active(events)
    b = bursts(act)
    bm = [m for m in range(N_MONTHS) if b[m]]
    _, pm = _windows(b)
    rb, bins = _carryover(events, act, b, bm)
    rp, _ = _carryover(events, act, b, pm)
    ratio = rb / rp if rb and rp else None
    return {"verdict": verdict(ratio, P3_RR), "ratio": None if ratio is None else round(ratio, 4),
            "burst_rr": None if rb is None else round(rb, 4),
            "placebo_rr": None if rp is None else round(rp, 4), "bins": bins, "rule": P3_RR}


def p4_organizations(events: list[dict]) -> dict:
    """Returning organizations, 2021 on only (Phase 1 has no organizations
    field). For each month from 2022 on, the share of events naming an
    organization whose names include one seen in an earlier month since
    January 2021. Pooling needs the burst-month share to be at least
    P4_RATIO[0] of the quiet-month share."""
    act = active(events)
    b = bursts(act)
    start = month_index(2021, 1)
    seen: set[str] = set()
    by_month: dict[int, list[dict]] = {}
    for e in events:
        if e["month"] >= start and e["orgs"]:
            by_month.setdefault(e["month"], []).append(e)
    tally = {"burst": [0, 0], "quiet": [0, 0]}
    for m in range(start, N_MONTHS):
        evs = by_month.get(m, [])
        if m >= month_index(2022, 1):
            g = "burst" if b[m] else "quiet"
            for e in evs:
                tally[g][0] += 1
                tally[g][1] += any(o in seen for o in e["orgs"])
        for e in evs:
            seen.update(e["orgs"])
    share = {g: (k / n if n else None) for g, (n, k) in tally.items()}
    ratio = (share["burst"] / share["quiet"]
             if share["burst"] is not None and share["quiet"] else None)
    return {"verdict": verdict(ratio, P4_RATIO), "ratio": None if ratio is None else round(ratio, 4),
            "share": {g: None if v is None else round(v, 4) for g, v in share.items()},
            "events": {g: n for g, (n, _) in tally.items()}, "rule": P4_RATIO}


def run(events: list[dict]) -> dict:
    act = active(events)
    b = bursts(act)
    return {
        "events": len(events),
        "counties": len({e["county"] for e in events}),
        "burst_months": [f"{year_of(i)}-{(START[1] - 1 + i) % 12 + 1:02d}" for i, x in enumerate(b) if x],
        "P1_rising_floor": p1_floor(events),
        "P2_spread_that_sticks": p2_retention(events),
        "P3_carryover_across_issues": p3_carryover(events),
        "P4_returning_organizations": p4_organizations(events),
    }


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv: list[str]) -> int:
    if "--events" not in argv:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    def after(flag):
        i = argv.index(flag) + 1
        out = []
        while i < len(argv) and not argv[i].startswith("--"):
            out.append(argv[i])
            i += 1
        return out
    paths = [Path(p) for p in after("--events")]
    result = run(read(paths))
    result["inputs"] = {p.name: sha(p) for p in paths}
    result["tool"] = {"score.py": sha(Path(__file__))}
    text = json.dumps(result, indent=1)
    if "--out" in argv:
        Path(after("--out")[0]).write_text(text + "\n", encoding="utf-8")
    print(text)
    if "--box" in argv:
        sys.path.insert(0, after("--willow")[0])
        import kernel  # the willow kernel: verdicts go on its record, unsealed

        box = Path(after("--box")[0])
        ts = __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat()
        for name, r in result.items():
            if name.startswith("P") and isinstance(r, dict):
                kernel.append(box, ts, "verdict", who="pooling-study", gate=name,
                              state=r["verdict"], inputs=result["inputs"], tools=result["tool"])
    preds = [v for k, v in result.items() if k.startswith("P")]
    return 0 if all(p["verdict"] == "pooling" for p in preds) else 42


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
