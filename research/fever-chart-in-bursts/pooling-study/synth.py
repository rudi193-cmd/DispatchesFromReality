#!/usr/bin/env python3
"""Synthetic protest events from a world whose answer is known.

    python synth.py --world pooling|reset|exhaustion --to FILE.csv [--seed N]

Each world has the same counties, the same burst months and the same
coverage, which doubles over the window in every world, as the CCC codebooks
say its collection grew. They differ only in what a burst leaves behind:

- pooling: a county that turns out in a burst keeps a share of that capacity,
  its local organizations come back, and it protests on other issues after;
- reset: burst turnout is drawn fresh each time and leaves nothing behind;
- exhaustion: a county that turns out in a burst protests less afterwards.

score.py should call pooling `pooling`, and reset and exhaustion anything but.
That is the power check: rules that cannot tell these worlds apart cannot be
trusted on the real data. The columns are CCC's Phase 2 names.

Standard library only; the same seed gives the same bytes.
"""
from __future__ import annotations

import csv
import math
import random
import sys
from pathlib import Path

START, MONTHS = (2017, 1), 97  # January 2017 to January 2025
COUNTIES = 1500
TAGS = ["democracy", "racism", "women's rights", "immigration", "environment",
        "guns", "labor", "foreign affairs"]
BURSTS = {11: "women's rights", 38: "racism", 62: "women's rights",
          78: "democracy", 90: "democracy"}  # month index: the burst's issue


def poisson(rng: random.Random, lam: float) -> int:
    if lam <= 0:
        return 0
    k, p, threshold = 0, 1.0, math.exp(-lam)
    while True:
        p *= rng.random()
        if p <= threshold:
            return k
        k += 1


def make(world: str, seed: int) -> list[dict]:
    rng = random.Random(seed)
    base = [rng.lognormvariate(-3.2, 1.3) for _ in range(COUNTIES)]
    stock = [0.0] * COUNTIES
    orgs = [[f"group {c}-{k}" for k in range(rng.randint(0, 3))] for c in range(COUNTIES)]
    pull = [rng.random() for _ in range(COUNTIES)]  # how readily a county joins a wave
    rows = []
    for i in range(MONTHS):
        y, m = START[0] + (START[1] - 1 + i) // 12, (START[1] - 1 + i) % 12 + 1
        coverage = 1.0 + i / (MONTHS - 1)  # doubles over the window, in every world
        burst = BURSTS.get(i)
        joined = []
        for c in range(COUNTIES):
            rate = (base[c] + stock[c]) * coverage
            n = poisson(rng, rate)
            joins = bool(burst) and rng.random() < 0.15 + 0.5 * pull[c]
            if joins:
                n += 1 + poisson(rng, 1.0)
                joined.append(c)
            for _ in range(n):
                in_burst = joins and rng.random() < 0.8
                tag = burst if in_burst else rng.choice(TAGS)
                if world == "pooling" or not in_burst:
                    names = orgs[c][: rng.randint(0, len(orgs[c]))] if orgs[c] else []
                else:
                    names = [f"wave {i}-{c}-{rng.randint(0, 10**6)}"]
                rows.append({
                    "date": f"{y}-{m:02d}-{rng.randint(1, 28):02d}",
                    "fips_code": f"{1000 + c}", "online": "0", "type": "rally",
                    "valence": "1", "issue_tags": tag, "size_cat": str(rng.choice([1, 1, 2, 2, 3])),
                    "organizations": "; ".join(names),
                })
        for c in joined:
            if world == "pooling":
                stock[c] += 0.03 + 0.5 * base[c]
                if not orgs[c]:
                    orgs[c] = [f"group {c}-wave{i}"]
            elif world == "exhaustion":
                base[c] *= 0.5
                stock[c] *= 0.5
    return rows


def main(argv: list[str]) -> int:
    opts = dict(zip(argv[::2], argv[1::2]))
    if opts.get("--world") not in ("pooling", "reset", "exhaustion") or "--to" not in opts:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    rows = make(opts["--world"], int(opts.get("--seed", 1)))
    with Path(opts["--to"]).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{opts['--world']}: {len(rows)} events", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
