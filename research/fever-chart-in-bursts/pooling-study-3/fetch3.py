#!/usr/bin/env python3
"""Find and fetch Study 3's data, by a rule frozen before the data existed.

    python fetch3.py --part valve|main --to DIR

History: Study 1's Phase 1 and Phase 2 files, by the same Dataverse ids, each
checked against the SHA-256 Study 1 pinned (../pooling-study/sources.json).

The Phase 3 file: the first version of doi:10.7910/DVN/RI9JFU, in release
order, released after the freeze (2026-11-04), whose ccc-phase3-public.csv
reaches the part's needed date: 2027-05-31 for `valve`, 2027-11-30 for `main`,
two months past each window's end, since CCC keeps adding events to recent
months. "Reaches" means its latest event date is on or after that date. Each
candidate is checked against the MD5 Dataverse publishes, and only its date
column is read.

Prints the chosen version and every file's SHA-256, and writes them to
DIR/chosen.json. Exit 0 when a version qualifies, 42 when none does yet
(not an error: the data aren't there), 2 on a refusal.

Standard library only.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
FROZEN_ON = "2026-11-04"
NEED = {"valve": "2027-05-31", "main": "2027-11-30"}
DOI = "doi:10.7910/DVN/RI9JFU"
NAME = "ccc-phase3-public.csv"
API = "https://dataverse.harvard.edu/api"
UA = {"User-Agent": "pooling-study-3-fetch/1"}

csv.field_size_limit(sys.maxsize)


def get(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA)) as r:
        return r.read()


def download(file_id: int, to: Path) -> None:
    req = urllib.request.Request(f"{API}/access/datafile/{file_id}?format=original", headers=UA)
    part = to.with_suffix(to.suffix + ".part")
    with urllib.request.urlopen(req) as r, part.open("wb") as out:
        for block in iter(lambda: r.read(1 << 20), b""):
            out.write(block)
    part.rename(to)


def digests(p: Path) -> tuple[str, str]:
    md5, sha = hashlib.md5(), hashlib.sha256()
    with p.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            md5.update(block)
            sha.update(block)
    return md5.hexdigest(), sha.hexdigest()


def latest_date(p: Path) -> str:
    with p.open(encoding="utf-8", errors="replace", newline="") as f:
        return max(((row.get("date") or "")[:10] for row in csv.DictReader(f)), default="")


def main(argv: list[str]) -> int:
    opts = dict(zip(argv[::2], argv[1::2]))
    if opts.get("--part") not in NEED or "--to" not in opts:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    need, to = NEED[opts["--part"]], Path(opts["--to"])
    to.mkdir(parents=True, exist_ok=True)
    chosen = {"part": opts["--part"], "needed_through": need, "files": {}}

    pins = json.loads((HERE.parent / "pooling-study" / "sources.json").read_text())
    for f in pins["files"][:2]:  # Phase 1 and Phase 2, as Study 1 pinned them
        p = to / f["filename"]
        if not p.exists():
            download(f["file_id"], p)
        _, sha = digests(p)
        if sha != f["sha256"]:
            print(f"refused: {f['filename']} is not the file Study 1 pinned", file=sys.stderr)
            return 2
        chosen["files"][f["filename"]] = sha

    versions = json.loads(get(f"{API}/datasets/:persistentId/versions?persistentId={DOI}"))["data"]
    versions = sorted((v for v in versions if (v.get("releaseTime") or "")[:10] > FROZEN_ON),
                      key=lambda v: v["releaseTime"])
    for v in versions:
        f = next((x["dataFile"] for x in v.get("files", [])
                  if (x["dataFile"].get("originalFileName") or x["dataFile"]["filename"]) == NAME), None)
        if not f:
            continue
        p = to / f"phase3-v{v['versionNumber']}.{v['versionMinorNumber']}.csv"
        if not p.exists():
            download(f["id"], p)
        md5, sha = digests(p)
        if md5 != (f.get("md5") or f.get("checksum", {}).get("value")):
            print(f"refused: version {v['versionNumber']} does not match its MD5", file=sys.stderr)
            return 2
        last = latest_date(p)
        print(f"version {v['versionNumber']}.{v['versionMinorNumber']} released "
              f"{v['releaseTime'][:10]}: latest event {last}")
        if last >= need:
            chosen.update(version=f"{v['versionNumber']}.{v['versionMinorNumber']}",
                          released=v["releaseTime"], file_id=f["id"], latest_event=last,
                          phase3=p.name)
            chosen["files"][p.name] = sha
            (to / "chosen.json").write_text(json.dumps(chosen, indent=1) + "\n")
            print(json.dumps(chosen, indent=1))
            return 0
    print(f"no version released after {FROZEN_ON} reaches {need} yet")
    return 42


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
