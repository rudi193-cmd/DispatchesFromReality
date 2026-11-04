#!/usr/bin/env python3
"""EXPLORATORY. A seasonal baseline for P1, tried on data already seen.

    python seasonal.py --events FILE [FILE ...]

Not a test and not frozen: written after both studies, run on months both
have already scored. It asks whether a different instrument for the rising
floor would have read those months differently, so that Study 3 can choose
its instrument knowing that.

The measure, for each burst month: over the 4 quiet months after it, active
counties against the same calendar months a year earlier; over the 4 quiet
months before it, the same; the first over the second. Season and steady
year-on-year growth in coverage appear on both sides and cancel. A ramp in
the months before a burst no longer sets the bar for the months after, which
is what broke Study 2's trend line. Months used must have a year-earlier month
that is neither a burst nor the spring 2020 lockdown, and a burst's before and
after months must fall within one presidential term, January of a change of
term excluded.

Reuses Study 2's reader and burst rule. Standard library only.
"""
from __future__ import annotations

import json
import math
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pooling-study-2"))
import score2  # noqa: E402

SIDE = 4
TERM_STARTS = [(2021, 1), (2025, 1)]


def term(i: int) -> int:
    return sum(i >= score2.month_index(*t) for t in TERM_STARTS)


EXCLUDED = {score2.month_index(*t) for t in TERM_STARTS} | score2._LOCK


def usable(b: list[bool], j: int) -> bool:
    return (0 <= j - 12 and not b[j] and j not in EXCLUDED
            and not b[j - 12] and j - 12 not in EXCLUDED)


def seasonal(events: list[dict], keep=lambda e: True, clean: bool = True) -> dict:
    """clean: a burst is skipped when another burst falls inside its span of
    before and after months, which would make it measure that burst too."""
    b = score2.bursts(score2.active(events))
    act = score2.active(events, keep)
    per, skipped = {}, []
    for m in range(score2.N_MONTHS):
        if not b[m]:
            continue
        bef = [j for j in range(m - 1, -1, -1) if usable(b, j)][:SIDE]
        aft = [j for j in range(m + 1, score2.N_MONTHS) if usable(b, j)][:SIDE]
        crossed = clean and len(bef) == SIDE and len(aft) == SIDE and any(
            b[j] for j in range(bef[-1], aft[-1] + 1) if j != m)
        if (len(bef) < SIDE or len(aft) < SIDE or crossed
                or len({term(j) for j in bef + aft + [m]}) > 1):
            skipped.append(score2.label(m))
            continue

        def yoy(js):
            v = [len(act[j]) / len(act[j - 12]) for j in js if len(act[j - 12])]
            return math.exp(statistics.mean(map(math.log, v))) if v and all(v) else None

        a, z = yoy(aft), yoy(bef)
        if a and z:
            per[score2.label(m)] = round(a / z, 4)
        else:
            skipped.append(score2.label(m))
    g = score2.gmean(list(per.values()))
    return {"ratio": None if g is None else round(g, 4), "per_burst": per, "skipped": skipped}


def main(argv: list[str]) -> int:
    if argv[:1] != ["--events"] or len(argv) < 2:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    events = score2.read([Path(p) for p in argv[1:]])
    big = lambda e: e["size"] >= 2  # noqa: E731
    out = {"clean, all": seasonal(events), "clean, 100+": seasonal(events, big),
           "any span, all": seasonal(events, clean=False),
           "any span, 100+": seasonal(events, big, clean=False)}
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
