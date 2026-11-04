#!/usr/bin/env python3
"""Score Study 3: pooling on months that did not exist when it was frozen.

    python score3.py --part valve|main --events FILE [FILE ...]
                     [--out RESULT.json] [--draws N] [--box BOX --willow WILLOW_DIR]

Frozen on 2026-11-04, when CCC's data reached May 2026. It scores months
collected after that:

- `--part valve` (P5): the November 2026 midterm, on the first Phase 3 version
  released on or after 1 June 2027; history through 31 March 2027.
- `--part main` (P1, P3, P4, and P2 reported): held-out months April 2026 to
  September 2027, on the first Phase 3 version released on or after
  1 December 2027.

Study 2's reader and burst rule (../pooling-study-2/score2.py, imported) and
the seasonal measure tried in ../pooling-exploratory. Everything before April
2026 is history only. --draws adds a county bootstrap, reported, deciding
nothing.

Standard library only. Exit 0 when every tested prediction is `pooling`.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "pooling-study-2"))
import score2  # noqa: E402

PARTS = {"valve": ("2027-03-31", (2027, 3)), "main": ("2027-09-30", (2027, 9))}
HELD = (2026, 4)
ELECTION = (2026, 11)
SIDE = 4  # usable quiet months on each side, for P1 and P5
TERM_STARTS = [(2021, 1), (2025, 1)]
SEED = 20261104
GATE_DRAWS = 200  # county resamples behind every P1 and P5 verdict

P1_SEASONAL = (1.05, 0.97)  # set from the exploratory synthetic worlds
P5_VALVE = (1.1, 0.9)  # pooling at or above; a drop at or below
P5_BEFORE, P5_AFTER = [(2026, m) for m in (7, 8, 9, 10)], [(2026, 12), (2027, 1), (2027, 2), (2027, 3)]
P5_MIN = 3  # usable months needed on each side of the election


def set_window(part: str) -> None:
    """Point Study 2's frozen functions at Study 3's window. They read these
    module globals when called, so nothing in score2.py changes."""
    last, end = PARTS[part]
    score2.LAST_DAY, score2.END, score2.HELD = last, end, HELD
    score2.N_MONTHS = score2.month_index(*end) + 1
    score2.H0 = score2.month_index(*HELD)


def term(i: int) -> int:
    return sum(i >= score2.month_index(*t) for t in TERM_STARTS)


def usable(b: list[bool], j: int) -> bool:
    out = {score2.month_index(*t) for t in TERM_STARTS} | score2._LOCK
    return (0 <= j - 12 and j < score2.N_MONTHS and not b[j] and j not in out
            and not b[j - 12] and j - 12 not in out)


def yoy(act, js) -> float | None:
    v = [len(act[j]) / len(act[j - 12]) for j in js if len(act[j - 12]) and len(act[j])]
    return math.exp(statistics.mean(map(math.log, v))) if v else None


def resample(events: list[dict], rng: random.Random) -> list[dict]:
    by_county: dict[str, list[dict]] = {}
    for e in events:
        by_county.setdefault(e["county"], []).append(e)
    counties = sorted(by_county)
    out = []
    for k, c in enumerate(rng.choice(counties) for _ in counties):
        out.extend({**e, "county": f"{c}#{k}"} for e in by_county[c])
    return out


def gated(point: list[float | None], draws: list[list[float | None]],
          rule: tuple[float, float], low_word: str) -> tuple[str, dict]:
    """A verdict that needs the resamples to agree. Pooling: every variant at
    the pooling line or above, and every variant's 2.5th percentile across
    resamples at 1.0 or above. The low verdict: every variant at the low line
    or below, and every variant's 97.5th percentile at 1.0 or below.
    Otherwise inconclusive. Study 3's power check found that on one or two
    bursts the point value alone gives false pooling in reset worlds."""
    bands = []
    for k in range(len(point)):
        ok = sorted(d[k] for d in draws if d[k] is not None)
        if len(ok) < len(draws) / 2:
            bands.append((None, None))
            continue
        bands.append((ok[int(0.025 * (len(ok) - 1))], ok[int(0.975 * (len(ok) - 1) + 0.5)]))
    info = {"bands": [[None if x is None else round(x, 4) for x in b] for b in bands]}
    if None in point or any(None in b for b in bands):
        return "inconclusive", info
    if min(point) >= rule[0] and min(b[0] for b in bands) >= 1.0:
        return "pooling", info
    if max(point) <= rule[1] and max(b[1] for b in bands) <= 1.0:
        return low_word, info
    return "inconclusive", info


def p1_seasonal(events: list[dict], gate: bool = True) -> dict:
    """Rising floor, seasonal: for each held-out burst, the 4 usable quiet
    months after it over their year-earlier months, divided by the same for
    the 4 before. Usable: not a burst, not January of a change of term, not
    the lockdown, and a year-earlier month that is none of those either. A
    burst is skipped when another burst falls inside its span, or the span
    crosses a change of term. Pooling needs the geometric mean over bursts at
    P1_SEASONAL[0] or more in both variants, and the resamples to agree (see
    `gated`)."""
    b = score2.bursts(score2.active(events))
    out = {}
    for name, keep in (("all", lambda e: True), ("100+", lambda e: e["size"] >= 2)):
        act = score2.active(events, keep)
        per, skipped = {}, []
        for m in score2.held_bursts(b):
            bef = [j for j in range(m - 1, -1, -1) if usable(b, j)][:SIDE]
            aft = [j for j in range(m + 1, score2.N_MONTHS) if usable(b, j)][:SIDE]
            ok = len(bef) == SIDE and len(aft) == SIDE
            if ok and (any(b[j] for j in range(bef[-1], aft[-1] + 1) if j != m)
                       or len({term(j) for j in bef + aft + [m]}) > 1):
                ok = False
            a, z = (yoy(act, aft), yoy(act, bef)) if ok else (None, None)
            if a and z:
                per[score2.label(m)] = round(a / z, 4)
            else:
                skipped.append(score2.label(m))
        g = score2.gmean(list(per.values()))
        out[name] = {"ratio": None if g is None else round(g, 4), "per_burst": per,
                     "skipped": skipped}
    ratios = [v["ratio"] for v in out.values()]
    if not gate:
        return {"variants": out}
    rng = random.Random(SEED)
    draws = [[v["ratio"] for v in p1_seasonal(resample(events, rng), False)["variants"].values()]
             for _ in range(GATE_DRAWS)]
    verdict, info = gated(ratios, draws, P1_SEASONAL, "against")
    return {"verdict": verdict, "variants": out, **info, "rule": P1_SEASONAL}


def p5_valve(events: list[dict], gate: bool = True) -> dict:
    """The midterm as a pressure valve, gated like P1: the usable months of December 2026 to
    March 2027 over their year-earlier months, divided by the same for July to
    October 2026. Pooling if both variants are at P5_VALVE[0] or more; `drop`
    if both are at P5_VALVE[1] or less. A drop is what a valve predicts, and
    also what exhaustion predicts: this cannot tell those two apart, only
    either of them from pooling."""
    b = score2.bursts(score2.active(events))
    bef = [j for j in map(lambda t: score2.month_index(*t), P5_BEFORE) if usable(b, j)]
    aft = [j for j in map(lambda t: score2.month_index(*t), P5_AFTER) if usable(b, j)]
    out = {}
    for name, keep in (("all", lambda e: True), ("100+", lambda e: e["size"] >= 2)):
        act = score2.active(events, keep)
        a, z = yoy(act, aft), yoy(act, bef)
        r = a / z if a and z and len(aft) >= P5_MIN and len(bef) >= P5_MIN else None
        out[name] = None if r is None else round(r, 4)
    rs = list(out.values())
    if not gate:
        return {"ratios": out}
    rng = random.Random(SEED)
    draws = [list(p5_valve(resample(events, rng), False)["ratios"].values())
             for _ in range(GATE_DRAWS)]
    v, info = gated(rs, draws, P5_VALVE, "drop")
    return {"verdict": v, "ratios": out, **info, "before": [score2.label(j) for j in bef],
            "after": [score2.label(j) for j in aft],
            "election_month_is_a_burst": b[score2.month_index(*ELECTION)], "rule": P5_VALVE}


def run(events: list[dict], part: str, gate: bool = True) -> dict:
    b = score2.bursts(score2.active(events))
    out = {"part": part, "events": len(events),
           "held_out_burst_months": [score2.label(m) for m in score2.held_bursts(b)]}
    if part == "valve":
        out["P5_pressure_valve"] = p5_valve(events, gate)
    else:
        out["P1_rising_floor"] = p1_seasonal(events, gate)
        out["P3_carryover_across_issues"] = score2.p3_carryover(events)
        out["P4_returning_organizations"] = score2.p4_organizations(events)
        out["reported_only_P2_spread_that_sticks"] = score2.p2_retention(events)
    return out


def measures(r: dict) -> dict:
    if r["part"] == "valve":
        v = r["P5_pressure_valve"]["ratios"]
        return {"P5 all": v["all"], "P5 100+": v["100+"]}
    return {"P1 all": r["P1_rising_floor"]["variants"]["all"]["ratio"],
            "P1 100+": r["P1_rising_floor"]["variants"]["100+"]["ratio"],
            "P3": r["P3_carryover_across_issues"]["ratio"],
            "P4": r["P4_returning_organizations"]["ratio"],
            "P2 (reported only)": r["reported_only_P2_spread_that_sticks"]["ratio"]}


def bootstrap(events: list[dict], part: str, draws: int) -> dict:
    rng = random.Random(SEED)
    by_county: dict[str, list[dict]] = {}
    for e in events:
        by_county.setdefault(e["county"], []).append(e)
    counties = sorted(by_county)
    got: dict[str, list] = {}
    for _ in range(draws):
        sample = []
        for k, c in enumerate(rng.choice(counties) for _ in counties):
            sample.extend({**e, "county": f"{c}#{k}"} for e in by_county[c])
        for name, x in measures(run(sample, part, gate=False)).items():
            got.setdefault(name, []).append(x)
    out = {}
    for name, vals in got.items():
        ok = sorted(v for v in vals if v is not None)
        q = lambda p: ok[min(len(ok) - 1, int(p * (len(ok) - 1) + 0.5))] if ok else None  # noqa: E731
        out[name] = {"low": q(0.025), "high": q(0.975), "computable": len(ok)}
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
    part = (after("--part") or [""])[0]
    paths = [Path(p) for p in after("--events", [])]
    if part not in PARTS or not paths:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    set_window(part)
    events = score2.read(paths)
    result = run(events, part)
    draws = int(after("--draws", ["0"])[0])
    if draws:
        result["bootstrap"] = bootstrap(events, part, draws)
    result["inputs"] = {p.name: sha(p) for p in paths}
    result["tool"] = {"score3.py": sha(Path(__file__)), "score2.py": sha(Path(score2.__file__))}
    text = json.dumps(result, indent=1)
    if "--out" in argv:
        Path(after("--out")[0]).write_text(text + "\n", encoding="utf-8")
    print(text)
    if "--box" in argv:
        sys.path.insert(0, after("--willow")[0])
        import datetime

        import kernel

        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
        for name, r in result.items():
            if name.startswith("P") and isinstance(r, dict):
                kernel.append(Path(after("--box")[0]), ts, "verdict", who="pooling-study-3",
                              gate=name, state=r["verdict"], inputs=result["inputs"],
                              tools=result["tool"])
    tested = [v for k, v in result.items() if k.startswith("P")]
    return 0 if all(p["verdict"] == "pooling" for p in tested) else 42


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
