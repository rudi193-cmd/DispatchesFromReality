#!/usr/bin/env python3
"""Study 2's dry run: counts only, before the freeze.

    python wiring2.py --events FILE [FILE ...]

For each file: rows read, rows kept, kept rows in the held-out months
(February 2025 on), the latest date kept, and how many kept held-out rows name
an organization or an issue. Nothing about months, counties, bursts or any
prediction. It confirms the reader sees the held-out months at all, and how
far into 2026 the pinned file reaches.

Standard library only.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import score2  # noqa: E402


def main(argv: list[str]) -> int:
    if argv[:1] != ["--events"] or len(argv) < 2:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    for p in map(Path, argv[1:]):
        read = kept = held = orgs = issues = 0
        latest = ""
        with p.open(encoding="utf-8", errors="replace", newline="") as f:
            for row in csv.DictReader(f):
                read += 1
                e = score2.normalize(row)
                if e is None:
                    continue
                kept += 1
                latest = max(latest, (row.get("date") or "")[:10])
                if e["month"] >= score2.H0:
                    held += 1
                    orgs += bool(e["orgs"])
                    issues += bool(e["issues"])
        print(f"{p.name}: {read} read, {kept} kept, {held} held out, latest kept date {latest}")
        print(f"  held-out rows naming an organization: {orgs}; with an issue: {issues}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
