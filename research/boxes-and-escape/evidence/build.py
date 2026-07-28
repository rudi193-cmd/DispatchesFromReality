#!/usr/bin/env python3
"""Rebuild evidence.db from schema.sql + seed.sql.

The SQL files are the source of truth; the database is a derived artifact.
Edit the SQL, rerun this, commit both.

    python3 build.py            # rebuild and print a summary
    python3 build.py --check    # rebuild into a temp file and verify only
"""

import argparse
import pathlib
import sqlite3
import sys
import tempfile

HERE = pathlib.Path(__file__).parent
SCHEMA = HERE / "schema.sql"
SEED = HERE / "seed.sql"
DB = HERE / "evidence.db"


def build(target: pathlib.Path) -> sqlite3.Connection:
    if target.exists():
        target.unlink()
    conn = sqlite3.connect(target)
    conn.executescript(SCHEMA.read_text())
    conn.executescript(SEED.read_text())
    conn.commit()
    return conn


def summarize(conn: sqlite3.Connection) -> None:
    tables = [
        "sources",
        "events",
        "claims",
        "mechanisms",
        "experiments",
        "open_questions",
    ]
    print("rows")
    for t in tables:
        (n,) = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()
        print(f"  {t:<16} {n:>4}")

    (unver,) = conn.execute("SELECT COUNT(*) FROM v_needs_verification").fetchone()
    print(f"\nrows needing verification: {unver}")

    print("\nblocking open questions")
    rows = conn.execute(
        "SELECT question FROM open_questions WHERE blocking = 1 AND status = 'open'"
    ).fetchall()
    for (q,) in rows:
        print(f"  - {q}")

    print("\nsources not read at the source")
    rows = conn.execute(
        "SELECT slug, retrieval FROM sources "
        "WHERE retrieval != 'fetched_full' ORDER BY retrieval, slug"
    ).fetchall()
    for slug, retrieval in rows:
        print(f"  {retrieval:<22} {slug}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="build to a temp file only")
    args = ap.parse_args()

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            conn = build(pathlib.Path(tmp) / "check.db")
            summarize(conn)
            conn.close()
        print("\nOK (check only, evidence.db untouched)")
        return 0

    conn = build(DB)
    summarize(conn)
    conn.close()
    print(f"\nwrote {DB}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
