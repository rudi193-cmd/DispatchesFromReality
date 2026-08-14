#!/usr/bin/env python3
"""Repo integrity checks for Dispatches From Reality.

Two invariants, enforced in CI (.github/workflows/checks.yml) and runnable by
hand. Modelled on Nestor's docs gate: the front door reaches everything, and a
link that names a file means that file exists.

1. **Every relative Markdown link resolves.** A link to a path that is not there
   is a broken promise; external (http/mailto) links are not checked.
2. **Every Markdown file is reachable from README.md** by following relative
   links — nothing is stranded where a reader can never find it — except an
   explicit, reasoned allowlist. A new file must be linked from the index
   (directly or transitively) or added here on purpose; silence is not allowed.

Run: `python scripts/check_repo.py` (stdlib only; exits non-zero on any failure).
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

# Files deliberately NOT linked from the front door, each with a reason. This is
# the one place an exception may live, and it must say why — an unindexed file
# is either a bug or a documented choice, never an accident nobody noticed.
ALLOWLIST = {
    "drafts/applied-governance-of-autonomous-systems.md":
        "work-in-progress draft; drafts/ is staging, not the published index",
    "professional/HANDOFF-2026-06-10.md":
        "internal session handoff, not reader-facing portfolio content",
    "AGENTS.md":
        "agent cold-start map, not reader-facing portfolio content",
    "CLAUDE.md":
        "thin pointer to AGENTS.md for Claude Code; not reader-facing",
}


def rel_link_targets(md: pathlib.Path):
    """Yield the relative link targets in a Markdown file (external links skipped)."""
    for m in LINK.finditer(md.read_text(encoding="utf-8", errors="replace")):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            continue
        path = target.split("#", 1)[0].split("?", 1)[0]
        if path:
            yield path


def main() -> int:
    mds = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    failures: list[str] = []

    # 1. Broken relative links.
    for md in mds:
        for path in rel_link_targets(md):
            if not (md.parent / path).resolve().exists():
                failures.append(f"broken link: {md.relative_to(ROOT)} -> {path}")

    # 2. Reachability from README.md (transitive closure over relative .md links).
    readme = ROOT / "README.md"
    reached = {readme.resolve()}
    stack = [readme]
    while stack:
        cur = stack.pop()
        for path in rel_link_targets(cur):
            tgt = (cur.parent / path).resolve()
            if tgt.suffix == ".md" and tgt.exists() and tgt not in reached:
                reached.add(tgt)
                stack.append(tgt)
    allowed = {(ROOT / a).resolve() for a in ALLOWLIST}
    for md in mds:
        r = md.resolve()
        if r not in reached and r not in allowed:
            failures.append(f"orphan (unreachable from README.md): {md.relative_to(ROOT)}")

    if failures:
        print(f"FAIL — {len(failures)} issue(s):")
        for f in sorted(failures):
            print(f"  {f}")
        return 1
    print(f"OK — {len(mds)} markdown files: all relative links resolve, all reachable "
          f"from README.md ({len(ALLOWLIST)} allowlisted).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
