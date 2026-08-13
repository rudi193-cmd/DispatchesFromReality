# AGENTS.md — Dispatches From Reality

Cold-start map for any agent (Claude Code, Cursor, Codex, cloud) working in this
repository. This is a **writing** repo — professional essays, research packets,
lessons, and creative dispatches by Sean Campbell — so the checks are about the
prose and its wiring, not a test suite.

## First move (every session)

```bash
git fetch origin
git status -sb
python scripts/check_repo.py        # links resolve + everything reachable from README
```

`scripts/check_repo.py` is the one gate, and it is stdlib-only (no install). CI
(`.github/workflows/checks.yml`) runs it on every push and pull request. Run it
before you push; a red check is a broken link or a stranded file, and both are
cheap to fix once you can see them.

## The two invariants the check enforces

1. **Every relative Markdown link resolves.** A link that names a file the reader
   cannot open is a broken promise. External (`http`/`mailto`) links are not
   checked — those live outside the repo. Files that belong to another repo (the
   `Emerging-Rule/community` lessons and showcases) are linked by full URL on
   purpose, not by a relative path that only resolves in that tree.
2. **Every Markdown file is reachable from `README.md`.** The front door reaches
   everything; nothing is stranded where no reader will find it. A new file must
   earn a link from the index (directly or transitively) — or an entry in the
   `ALLOWLIST` at the top of `scripts/check_repo.py`, **with a reason**. Silence
   is not a valid state: an unindexed file is either a bug or a documented choice.

## House conventions (not gate-enforced, but expected)

These are the habits the research work already keeps; hold them because a reader
trusts the prose only as far as it earns it.

- **Research packages come in pairs.** `research/<topic>/DRAFT.md` is the full
  prose; `research/<topic>/README.md` is the packet that summarises it. **Keep
  their figures identical** — a number that drifts between the draft and its
  packet is an internal contradiction a reader will catch.
- **Sources named inline, no URLs in the research drafts.** The drafts name their
  sources in the sentence; they do not carry a link section. (Lessons and indexes
  may link out; the no-URL rule is specific to the research prose.)
- **Provenance is a state, and it is honest.** Where a piece tags evidence, use
  the `assumed` / `fitted` / `measured` ordering from *Nobody Counts the Ad
  Breaks*: `measured` means read at first hand, `fitted` means corroborated by a
  stated rule, `assumed` means a single source or none. Do **not** call a
  secondary summary `measured` — that is the exact conflation that paper is about.
- **Do not overclaim.** No "peer-reviewed", "verified against", or "proven" unless
  it is true and traceable. Say what was checked and what was not.

## What is where

| Path | What |
|------|------|
| `README.md` | The index — the front door the check measures reachability from |
| `research/<topic>/` | A draft + packet pair per research thread |
| `essays/`, `education/`, `professional/`, `lessons/`, `creative/` | The writing, all indexed from `README.md` |
| `drafts/` | Work in progress — staging, allowlisted out of the reachability check |
| `scripts/check_repo.py` | The gate: links resolve, everything reachable |
| `.github/workflows/checks.yml` | Runs the gate in CI on push and pull request |
