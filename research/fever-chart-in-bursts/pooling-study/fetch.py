#!/usr/bin/env python3
"""Fetch the pinned CCC files from Harvard Dataverse and check them.

    python fetch.py --to DIR            download what's missing, then check
    python fetch.py --to DIR --check    check only, offline
    python fetch.py --to DIR --pin      write each file's SHA-256 into sources.json

Each file is fetched by its Dataverse file id in its original format, and
checked against the MD5 Dataverse publishes and, once pinned, the SHA-256 in
sources.json. A file that fails either check is refused, never scored.

--pin is run once, in the freeze commit, and refuses to overwrite a pin that is
already there: a changed file is a new freeze, made on purpose.

Downloading a file is not opening it. Nothing here reads a row.

Standard library only.
"""
from __future__ import annotations

import hashlib
import json
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = HERE / "sources.json"
URL = "https://dataverse.harvard.edu/api/access/datafile/{}?format=original"


def digests(p: Path) -> tuple[str, str]:
    md5, sha = hashlib.md5(), hashlib.sha256()
    with p.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            md5.update(block)
            sha.update(block)
    return md5.hexdigest(), sha.hexdigest()


def main(argv: list[str]) -> int:
    if "--to" not in argv:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    to = Path(argv[argv.index("--to") + 1])
    to.mkdir(parents=True, exist_ok=True)
    pins = json.loads(SOURCES.read_text(encoding="utf-8"))
    bad = 0
    for f in pins["files"]:
        p = to / f["filename"]
        if not p.exists() and "--check" not in argv:
            print(f"fetching {f['filename']} ({f['bytes']:,} bytes)", file=sys.stderr)
            req = urllib.request.Request(URL.format(f["file_id"]),
                                         headers={"User-Agent": "pooling-study-fetch/1"})
            part = p.with_suffix(p.suffix + ".part")
            with urllib.request.urlopen(req) as r, part.open("wb") as out:
                for block in iter(lambda: r.read(1 << 20), b""):
                    out.write(block)
            part.rename(p)
        if not p.exists():
            print(f"missing  {f['filename']}")
            bad += 1
            continue
        md5, sha = digests(p)
        ok = md5 == f["md5"] and (f["sha256"] is None or sha == f["sha256"])
        print(f"{'ok      ' if ok else 'MISMATCH'} {f['filename']}  md5 {md5}  sha256 {sha}")
        bad += not ok
        if ok and "--pin" in argv:
            if f["sha256"] not in (None, sha):
                print("refused: a different SHA-256 is already pinned", file=sys.stderr)
                return 2
            f["sha256"] = sha
    if "--pin" in argv and not bad:
        SOURCES.write_text(json.dumps(pins, indent=1) + "\n", encoding="utf-8")
        print("pinned: sources.json now holds each file's SHA-256")
    return 0 if not bad else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
