#!/usr/bin/env python3
"""Score Study 2: the pooling predictions, on held-out months, with fixed rules.

    python score2.py --events FILE [FILE ...] [--out RESULT.json] [--draws N]
                     [--box BOX --willow WILLOW_DIR]

Study 1 (../pooling-study) ran once on January 2017 to January 2025. Study 2
asks the same questions of the months after it, February 2025 to March 2026, which no rule had been computed on when this was written. Everything
before February 2025 is read only as history: which counties had protested
before, which organizations had been seen, and the quiet months on the near
side of a burst.

What changed from Study 1, and why, is in PLAN.md: P1 measured against each
burst's own trend, P3 against matched placebo months, shorter windows to fit
a shorter period, looser organization names for P4, and P2 reported but not
tested. The thresholds are Study 1's. --draws adds a county bootstrap
to the output; it is reported, and decides nothing.

Standard library only. Exit 0 when P1, P3 and P4 are all `pooling`, 42 otherwise.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import re
import statistics
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

# ---- the frozen window and rules (PLAN.md, "Rules") ------------------------

# History from Study 1's start. The pinned Phase 3 file reaches 31 May 2026;
# its last two months are left out, because CCC keeps adding events to recent
# months as reports surface, so the newest months are the thinnest.
FIRST_DAY, LAST_DAY = "2017-01-20", "2026-03-31"
START, END = (2017, 1), (2026, 3)
HELD = (2025, 2)  # first held-out month: January 2025 straddles the term change
WARMUP = 3  # January to March 2017 can't be anyone's first month
BURST_X = 1.5  # a burst month: active counties >= 1.5 x its calendar year's median
SIDE = 4  # quiet months after a burst that P1 compares with the trend
TREND = 8  # quiet months before a burst that P1 fits its trend to
GAP = 24  # months without an event that make a county's return a new recruit
MATCH = (3, 12)  # P3: a burst's placebos are quiet months 3 to 12 months away from it
CLEAR = 2  # and at least this many months from every burst
FOLLOW = 6  # months followed after a recruit month (P2) or a burst (P3)
PRIOR = 12  # months of history that define P3's comparison counties
LOCKDOWN = [(2020, 3), (2020, 4), (2020, 5)]  # never in a step window
ORGS_FROM = (2021, 1)  # the first month with an organizations field
SEED = 20261104

P1_STEP = (1.1, 1.0)
P2_RATIO = (0.85, 0.65)
P3_RR = (0.95, 0.85)
P4_RATIO = (0.8, 0.5)


def month_index(y: int, m: int) -> int:
    return (y - START[0]) * 12 + (m - START[1])


N_MONTHS = month_index(*END) + 1
H0 = month_index(*HELD)
_LOCK = {month_index(*x) for x in LOCKDOWN}


def year_of(i: int) -> int:
    return START[0] + (START[1] - 1 + i) // 12


def label(i: int) -> str:
    return f"{year_of(i)}-{(START[1] - 1 + i) % 12 + 1:02d}"


# ---- reading (Study 1's reader, with the window and org names changed) -----

EMPTY = {"na", "n/a", "none", "nan", "null"}


def split(s: str) -> list[str]:
    return [t for t in (x.strip().lower() for x in s.replace(",", ";").split(";"))
            if t and t not in EMPTY]


def org_name(s: str) -> str:
    """An organization's name, loosened so small differences in how coders
    wrote it don't make one group two: case, punctuation, "&" against "and",
    and a leading "the"."""
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[4:] if s.startswith("the ") else s


def labor_strike(kind: str) -> bool:
    return any("strike" in t and "hunger" not in t for t in split(kind))


def normalize(row: dict) -> dict | None:
    date = (row.get("date") or "").strip()[:10]
    if not FIRST_DAY <= date <= LAST_DAY:
        return None
    try:
        y, m = int(date[:4]), int(date[5:7])
    except ValueError:
        return None
    fips = (row.get("fips_code") or "").strip().split(".")[0]
    if not fips.isdigit():
        return None
    if (row.get("online") or "").strip() in ("1", "1.0"):
        return None
    issues = split(row.get("issue_tags") or row.get("issues") or "")
    kind = row.get("event_type") or row.get("type") or ""
    valence = (row.get("valence") or "").strip().split(".")[0]
    if labor_strike(kind) and not (valence == "1" and "environment" in issues):
        return None
    try:
        size = int(float(row.get("size_cat") or 0))
    except ValueError:
        size = 0
    orgs = [o for o in (org_name(x) for x in split(row.get("organizations") or "")) if o]
    return {"month": month_index(y, m), "county": fips.zfill(5), "size": size,
            "issues": issues, "orgs": orgs}


def read(paths: list[Path]) -> list[dict]:
    events = []
    for p in paths:
        with p.open(encoding="utf-8", errors="replace", newline="") as f:
            dialect = "excel-tab" if p.suffix in (".tab", ".tsv") else "excel"
            for row in csv.DictReader(f, dialect=dialect):
                e = normalize(row)
                if e:
                    events.append(e)
    return events


# ---- the series -------------------------------------------------------------


def active(events: list[dict], keep=lambda e: True) -> list[set[str]]:
    out = [set() for _ in range(N_MONTHS)]
    for e in events:
        if keep(e):
            out[e["month"]].add(e["county"])
    return out


def bursts(act: list[set[str]]) -> list[bool]:
    by_year: dict[int, list[int]] = {}
    for i, s in enumerate(act):
        by_year.setdefault(year_of(i), []).append(len(s))
    med = {y: statistics.median(v) for y, v in by_year.items()}
    return [len(s) >= BURST_X * med[year_of(i)] and len(s) > 0 for i, s in enumerate(act)]


def gmean(v: list[float]) -> float | None:
    v = [x for x in v if x and x > 0]
    return math.exp(sum(map(math.log, v)) / len(v)) if v else None


def verdict(value: float | None, rule: tuple[float, float]) -> str:
    if value is None:
        return "inconclusive"
    if value >= rule[0]:
        return "pooling"
    if value <= rule[1]:
        return "against"
    return "inconclusive"


def matched(b: list[bool], burst: int, need_room) -> list[int]:
    """A burst's placebos: quiet months MATCH[0] to MATCH[1] months from it,
    at least CLEAR months from every burst, and with the room `need_room`
    asks for. Each burst gets its own, so a placebo is from the same stretch
    of time as the burst it controls for."""
    near = {j for x in range(N_MONTHS) if b[x] for j in range(x - CLEAR, x + CLEAR + 1)}
    return [m for d in range(MATCH[0], MATCH[1] + 1) for m in (burst - d, burst + d)
            if 0 <= m < N_MONTHS and not b[m] and m not in near and m not in _LOCK
            and need_room(m)]


def held_bursts(b: list[bool]) -> list[int]:
    return [m for m in range(H0, N_MONTHS) if b[m]]


# ---- the four predictions ---------------------------------------------------


def p1_floor(events: list[dict]) -> dict:
    """Rising floor, against the burst's own trend: for each held-out burst,
    a straight line is fitted to log active counties over the TREND quiet
    months before it, and the SIDE quiet months after it are compared with
    where that line says they would be. The geometric mean of actual over
    expected, across those months and then across bursts, is the measure.
    Coverage that was already growing is in the line; a step up after the
    burst is not. Pooling needs P1_STEP[0] or more in both variants."""
    base = active(events)
    b = bursts(base)
    quiet = [not x and j not in _LOCK for j, x in enumerate(b)]
    out = {}
    for name, keep in (("all", lambda e: True), ("100+", lambda e: e["size"] >= 2)):
        act = active(events, keep)
        per, skipped = {}, []
        for m in held_bursts(b):
            bef = [j for j in range(m - 1, -1, -1) if quiet[j]][:TREND]
            aft = [j for j in range(m + 1, N_MONTHS) if quiet[j]][:SIDE]
            if len(bef) < TREND or len(aft) < SIDE:
                skipped.append(label(m))
                continue
            ys = [math.log(max(len(act[j]), 1)) for j in bef]
            mx, my = statistics.mean(bef), statistics.mean(ys)
            slope = (sum((x - mx) * (y - my) for x, y in zip(bef, ys))
                     / sum((x - mx) ** 2 for x in bef))
            gap = [math.log(max(len(act[j]), 1)) - (my + slope * (j - mx)) for j in aft]
            per[label(m)] = round(math.exp(statistics.mean(gap)), 4)
        g = gmean(list(per.values()))
        out[name] = {"ratio": None if g is None else round(g, 4), "per_burst": per,
                     "skipped": skipped}
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
    """Spread that sticks: a recruit month is a held-out month in which a
    county is active after GAP months or more with no event (or none since
    the warm-up). Few counties are new in 2025 after eight years of data, so
    a county coming back after two quiet years counts as recruited again.
    Retained: active in a quiet month within FOLLOW."""
    act = active(events)
    b = bursts(act)
    recruits: list[tuple[str, int]] = []
    last: dict[str, int] = {}
    for i, s in enumerate(act):
        for c in s:
            if i >= H0 and i - last.get(c, -GAP - 1) > GAP:
                recruits.append((c, i))
            last[c] = i
    groups = {"burst": [0, 0], "quiet": [0, 0]}
    for c, i in recruits:
        if i + FOLLOW >= N_MONTHS:
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


def _carry(by_month, act, b, months: list[int]) -> float | None:
    bins = {"1-2": [0, 0, 0, 0], "3-5": [0, 0, 0, 0], "6+": [0, 0, 0, 0]}
    for m in months:
        counts: dict[str, int] = {}
        for e in by_month.get(m, []):
            for t in e["issues"]:
                counts[t] = counts.get(t, 0) + 1
        if not counts:
            continue
        top = max(sorted(counts), key=counts.get)
        s_set = {e["county"] for e in by_month.get(m, []) if top in e["issues"]}
        prior: dict[str, int] = {}
        for j in range(max(0, m - PRIOR), m):
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
    return num / den if den else None


def p3_carryover(events: list[dict]) -> dict:
    """Carryover across issues: Study 1's measure, with FOLLOW months after
    and each held-out burst's own matched placebos as the baseline. The
    burst ratio pools every held-out burst with FOLLOW months of room; the
    placebo ratio pools all of their placebos."""
    act = active(events)
    b = bursts(act)
    by_month: dict[int, list[dict]] = {}
    for e in events:
        by_month.setdefault(e["month"], []).append(e)
    room = lambda m: m + FOLLOW < N_MONTHS  # noqa: E731
    used = [m for m in held_bursts(b) if room(m)]
    pls = sorted({p for m in used for p in matched(b, m, room)})
    used = [m for m in used if matched(b, m, room)]
    rb = _carry(by_month, act, b, used)
    rp = _carry(by_month, act, b, pls)
    ratio = rb / rp if rb and rp else None
    return {"verdict": verdict(ratio, P3_RR), "ratio": None if ratio is None else round(ratio, 4),
            "burst_rr": None if rb is None else round(rb, 4),
            "placebo_rr": None if rp is None else round(rp, 4),
            "bursts": [label(m) for m in used], "placebos": [label(m) for m in pls],
            "rule": P3_RR}


def p4_organizations(events: list[dict]) -> dict:
    """Returning organizations, held-out months only: the share of events
    naming an organization whose loosened names include one seen in an
    earlier month since January 2021, burst months over quiet months."""
    act = active(events)
    b = bursts(act)
    start = month_index(*ORGS_FROM)
    by_month: dict[int, list[dict]] = {}
    for e in events:
        if e["month"] >= start and e["orgs"]:
            by_month.setdefault(e["month"], []).append(e)
    seen: set[str] = set()
    tally = {"burst": [0, 0], "quiet": [0, 0]}
    for m in range(start, N_MONTHS):
        evs = by_month.get(m, [])
        if m >= H0:
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
    b = bursts(active(events))
    return {
        "events": len(events),
        "held_out_events": sum(e["month"] >= H0 for e in events),
        "counties": len({e["county"] for e in events}),
        "held_out_burst_months": [label(m) for m in held_bursts(b)],
        "P1_rising_floor": p1_floor(events),
        # Not a prediction in Study 2: the power check showed that on 19
        # months, with a few dozen recruits, it calls reset worlds pooling.
        # Reported for the record; it waits for a full term.
        "reported_only_P2_spread_that_sticks": p2_retention(events),
        "P3_carryover_across_issues": p3_carryover(events),
        "P4_returning_organizations": p4_organizations(events),
    }


MEASURES = {
    "P1 all events": lambda r: r["P1_rising_floor"]["variants"]["all"]["ratio"],
    "P1 100 or more": lambda r: r["P1_rising_floor"]["variants"]["100+"]["ratio"],
    "P2 (reported only)": lambda r: r["reported_only_P2_spread_that_sticks"]["ratio"],
    "P3": lambda r: r["P3_carryover_across_issues"]["ratio"],
    "P4": lambda r: r["P4_returning_organizations"]["ratio"],
}
RULES = {"P1 all events": P1_STEP, "P1 100 or more": P1_STEP, "P2 (reported only)": P2_RATIO,
         "P3": P3_RR, "P4": P4_RATIO}


def bootstrap(events: list[dict], draws: int) -> dict:
    """Counties resampled with replacement, the whole run repeated. Reported,
    never a verdict."""
    rng = random.Random(SEED)
    by_county: dict[str, list[dict]] = {}
    for e in events:
        by_county.setdefault(e["county"], []).append(e)
    counties = sorted(by_county)
    got = {k: [] for k in MEASURES}
    for _ in range(draws):
        sample = []
        for k, c in enumerate(rng.choice(counties) for _ in counties):
            sample.extend({**e, "county": f"{c}#{k}"} for e in by_county[c])
        r = run(sample)
        for name, f in MEASURES.items():
            got[name].append(f(r))
    out = {}
    for name, vals in got.items():
        ok = sorted(v for v in vals if v is not None)
        q = lambda p: ok[min(len(ok) - 1, int(p * (len(ok) - 1) + 0.5))] if ok else None  # noqa: E731
        pool, against = RULES[name]
        out[name] = {"low": q(0.025), "high": q(0.975), "computable": len(ok),
                     "at_or_above_pooling_line": round(sum(v >= pool for v in ok) / draws, 4),
                     "at_or_below_against_line": round(sum(v <= against for v in ok) / draws, 4)}
    return {"draws": draws, "measures": out}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv: list[str]) -> int:
    def after(flag, default=None):
        if flag not in argv:
            return default
        i, out = argv.index(flag) + 1, []
        while i < len(argv) and not argv[i].startswith("--"):
            out.append(argv[i])
            i += 1
        return out
    paths = [Path(p) for p in after("--events", [])]
    if not paths:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    events = read(paths)
    result = run(events)
    draws = int(after("--draws", ["0"])[0])
    if draws:
        result["bootstrap"] = bootstrap(events, draws)
    result["inputs"] = {p.name: sha(p) for p in paths}
    result["tool"] = {"score2.py": sha(Path(__file__))}
    text = json.dumps(result, indent=1)
    if "--out" in argv:
        Path(after("--out")[0]).write_text(text + "\n", encoding="utf-8")
    print(text)
    if "--box" in argv:
        sys.path.insert(0, after("--willow")[0])
        import datetime

        import kernel  # verdicts go on the record, unsealed

        box = Path(after("--box")[0])
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
        for name, r in result.items():
            if name.startswith("P") and isinstance(r, dict):
                kernel.append(box, ts, "verdict", who="pooling-study-2", gate=name,
                              state=r["verdict"], inputs=result["inputs"], tools=result["tool"])
    preds = [v for k, v in result.items() if k.startswith("P")]
    return 0 if all(p["verdict"] == "pooling" for p in preds) else 42


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
