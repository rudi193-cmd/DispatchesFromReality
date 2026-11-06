# SOIL-PHYS-001: the willow stack

**Sean Campbell** · Working stack · November 2026

The [SOIL-PHYS-001 ledger](../README.md)'s sources, kept the way willow keeps
sources: by address, time and SHA-256, never their text. It runs on the
[willow](https://github.com/willow-memory/Willow) kernel and its stdlib
add-ons, local only, standard library only.

| File | What |
|------|------|
| `stack/catalog/catalog.json` | An Almanac catalog: each cited work with its venue, what it shows, the ledger lines that use it, its address, each probe's answer, and its open or provided copies |
| `stack/nuggets/soil-phys-001.json` | A Jeles seed: each work as a question and the answer it gives, with its address as evidence and the ledger line as the reason; unsigned, so Jeles sets the rung |
| `make_stack.py` | Writes both from one table; `--probe` asks each address once and appends the answer to `probes.jsonl` |
| `make_kept.py` | Writes [KEPT.md](../KEPT.md) from the catalog and the kept files |
| `probes.jsonl` | Every probe, never rewritten: a later 403 or 429 is a holder's block or rate limit, not the page gone |
| `keep/.snapshots.jsonl` | almanac-keep's log: each fetched copy's address, time, bytes and SHA-256 |
| `keep/.provided.jsonl` | Copies downloaded in a browser where a script is refused: where from, when, and SHA-256 |
| `checks.json` | The 35 lines checked, each with its file, verdict and deciding quote, as [CHECKS.md](../CHECKS.md) shows them |

The kept files themselves are not here: several are paywalled, and the repo
keeps sources by hash. To hold them again:

    python3 WILLOW/adapters/stdlib/almanac-keep/keep.py --catalog stack/catalog/catalog.json --id ID --to keep

for each entry, then compare each file's SHA-256 with the logs. A copy marked
as downloaded in a browser has to be downloaded by hand again; the log says
from where.

Read the catalog and the nuggets as passages:

    python3 WILLOW/adapters/stdlib/almanac/almanac.py mirror --from stack/catalog --to MIRROR/almanac
    python3 WILLOW/adapters/stdlib/jeles/jeles.py mirror --from stack/nuggets --to MIRROR/jeles

then point a box at MIRROR.
