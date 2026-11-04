#!/usr/bin/env python3
"""Error bars on the frozen run: resample counties, rerun the frozen rules.

    python bootstrap.py --events FILE [FILE ...] --out results/bootstrap.json
                        [--draws 400] [--seed 20261104]

Written after the one run, and not part of the freeze: it changes no rule and
no verdict. Each draw picks counties with replacement (a county drawn twice
counts as two counties), keeps all of their events, and runs score.py's
frozen `run` on the result, burst calendar and all, so the uncertainty in
which months are bursts is carried through. Reported for each measure: the
point value from the full data, the 2.5th and 97.5th percentiles of the
draws, and the share of draws on each side of the pooling and against lines.

Standard library only; the same seed gives the same numbers.
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import score  # noqa: E402

MEASURES = {
    "P1 all events": lambda r: r["P1_rising_floor"]["variants"]["all"]["ratio"],
    "P1 100 or more": lambda r: r["P1_rising_floor"]["variants"]["100+"]["ratio"],
    "P2": lambda r: r["P2_spread_that_sticks"]["ratio"],
    "P3": lambda r: r["P3_carryover_across_issues"]["ratio"],
    "P4": lambda r: r["P4_returning_organizations"]["ratio"],
}
RULES = {"P1 all events": score.P1_STEP, "P1 100 or more": score.P1_STEP,
         "P2": score.P2_RATIO, "P3": score.P3_RR, "P4": score.P4_RATIO}


def pct(v: list[float], q: float) -> float:
    v = sorted(v)
    k = (len(v) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (k - lo)


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
    if not paths or "--out" not in argv:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    draws = int(after("--draws", ["400"])[0])
    rng = random.Random(int(after("--seed", ["20261104"])[0]))
    events = score.read(paths)
    by_county: dict[str, list[dict]] = {}
    for e in events:
        by_county.setdefault(e["county"], []).append(e)
    counties = sorted(by_county)
    full = score.run(events)
    got = {k: [] for k in MEASURES}
    for d in range(draws):
        sample = []
        for k, c in enumerate(rng.choice(counties) for _ in counties):
            sample.extend({**e, "county": f"{c}#{k}"} for e in by_county[c])
        r = score.run(sample)
        for name, f in MEASURES.items():
            got[name].append(f(r))
        if (d + 1) % 50 == 0:
            print(f"{d + 1} of {draws} draws", file=sys.stderr)
    out = {"draws": draws, "counties": len(counties), "measures": {}}
    for name, vals in got.items():
        ok = [v for v in vals if v is not None]
        pool, against = RULES[name]
        out["measures"][name] = {
            "point": MEASURES[name](full),
            "low": round(pct(ok, 0.025), 4) if ok else None,
            "high": round(pct(ok, 0.975), 4) if ok else None,
            "computable": len(ok),
            "at_or_above_pooling_line": round(sum(v >= pool for v in ok) / draws, 4),
            "at_or_below_against_line": round(sum(v <= against for v in ok) / draws, 4),
            "rule": [pool, against],
        }
    out["tool"] = {"bootstrap.py": score.sha(Path(__file__)), "score.py": score.sha(Path(score.__file__))}
    out["inputs"] = {p.name: score.sha(p) for p in paths}
    Path(after("--out")[0]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out["measures"], indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
