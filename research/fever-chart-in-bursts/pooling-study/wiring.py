#!/usr/bin/env python3
"""The dry run: does score.py's reader read the real files at all?

    python wiring.py --events FILE [FILE ...]

Run once, before the freeze, on the pinned files. For each file it prints only
how many rows were read, how many were kept, why the rest were dropped, and
how many kept rows carry each field the predictions use. Nothing about months,
counties, bursts or any prediction: a wrong column name would score zero
events, or no issues, without a word, and this is where that shows, before
any result can.

Standard library only.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import score  # noqa: E402


def why_dropped(row: dict) -> str:
    date = (row.get("date") or "").strip()[:10]
    if not score.FIRST_DAY <= date <= score.LAST_DAY:
        return "outside the two terms"
    if not (row.get("fips_code") or "").strip().split(".")[0].isdigit():
        return "no county"
    if (row.get("online") or "").strip() in ("1", "1.0"):
        return "online only"
    return "a labor strike"


def main(argv: list[str]) -> int:
    if argv[:1] != ["--events"] or len(argv) < 2:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    for p in map(Path, argv[1:]):
        read = kept = 0
        dropped: dict[str, int] = {}
        has = {"size": 0, "issues": 0, "orgs": 0}
        bad = p.read_bytes().decode("utf-8", errors="replace").count("\ufffd")
        with p.open(encoding="utf-8", errors="replace", newline="") as f:
            reader = csv.DictReader(f)
            used = [c for c in ("date", "fips_code", "online", "type", "event_type", "valence",
                                "issues", "issue_tags", "size_cat", "organizations")
                    if c in (reader.fieldnames or [])]
            for row in reader:
                read += 1
                e = score.normalize(row)
                if e is None:
                    k = why_dropped(row)
                    dropped[k] = dropped.get(k, 0) + 1
                    continue
                kept += 1
                has["size"] += e["size"] > 0
                has["issues"] += bool(e["issues"])
                has["orgs"] += bool(e["orgs"])
        print(f"{p.name}: {read} rows read, {kept} kept, {bad} bytes not UTF-8")
        print(f"  columns used: {', '.join(used)}")
        for k, n in sorted(dropped.items()):
            print(f"  dropped, {k}: {n}")
        for k, n in has.items():
            print(f"  kept rows with {k}: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
