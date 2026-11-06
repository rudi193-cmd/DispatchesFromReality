# SOIL-PHYS-001: the willow stack

**Sean Campbell** · Working stack · November 2026

The [SOIL-PHYS-001 ledger](../README.md)'s sources, kept the way willow keeps
sources: by address, time and SHA-256, never their text. It runs on the
[willow](https://github.com/willow-memory/Willow) kernel and its stdlib
add-ons, local only, standard library only.

| File | What |
|------|------|
| [build.sh](build.sh) | Makes the folder: clones this repo, fetches every open source with almanac-keep and holds it to its logged hash, turns them into text with willow's readers, starts three boxes |
| [stack.md](stack.md) | The steps, in pools: the ledger's quotes, the deciding quotes, short claims, packet drift and links, the sources asked directly, box health |
| `stack/catalog/catalog.json` | An Almanac catalog: each cited work with its venue, what it shows, the ledger lines that use it, its address, each probe's answer, and its open or provided copies |
| `stack/nuggets/soil-phys-001.json` | A Jeles seed: each work as a question and the answer it gives, with its address as evidence and the ledger line as the reason; unsigned, so Jeles sets the rung |
| `make_stack.py` | Writes both from one table; `--probe` asks each address once and appends the answer to `probes.jsonl` |
| `make_kept.py` | Writes [KEPT.md](../KEPT.md) from the catalog and the kept files |
| `probes.jsonl` | Every probe, never rewritten: a later 403 or 429 is a holder's block or rate limit, not the page gone |
| `keep/.snapshots.jsonl` | almanac-keep's log: each fetched copy's address, time, bytes and SHA-256 |
| `keep/.provided.jsonl` | Copies downloaded in a browser where a script is refused: where from, when, and SHA-256 |
| `keep/.text.jsonl` | Each kept web page's text hash: a page is rebuilt on every request, so its bytes never match twice, and its text is what's held |
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

---

## A run, 2026-11-06

`build.sh` from scratch, then the stack, on willow's main (93b2add):

- **Sources:** 27 held to their SHA-256 (every PDF and text file, the four browser downloads among them); 4 web pages whose bytes changed and whose text didn't; 5 live pages (Springer's and the reprint's) whose text changed too, an access counter or a notice, so the packet's copy is the record; Solomonoff's publisher page, a redirect stub, set aside. Weyl's page answered 429 the first time, a rate limit.
- **The ledger's quotes** (`quotes`): 33 in DRAFT.md, 10 as written, 19 almost, 4 not there. The four: Klein's words in English (his paper is German), Casimir's and Goldstone's (scans), and "deletion is an appended tombstone", revision 1's claim about willow, which nothing holds. Most of the "almost" are the pdf reader's: a word split at a line end ("univer se", "multi plets") or a ligature left as one character ("oﬀ"); the rest are the ledger quoting its own earlier wording in CHANGED lines, which no source holds.
- **The deciding quotes** (`misquote`): 6 of 6 as written, Leibniz's "would not at all differ" among them, which willow's study of these sources missed because its runner kept each of Leibniz's paragraphs on one line; `build.sh` breaks such lines with the text add-on.
- **Short claims** (`claim-check`): "gravity is an entropic force" has every part in Verlinde, "Rule 110 is capable of universal computation" in Cook; "the metric is proportional to entanglement" has every part nowhere.
- **Asked directly** (`fair-merge`): "is space absolute or relative" serves Leibniz's third paper first; "what happens to the ground state when a symmetry is broken" serves Nambu's lecture first.
- **The repo** (`xref`): 305 references, none broken. (`pair-drift`): this packet's README holds a "256" its draft doesn't, the 256 of SHA-256; across the repo it flags figures in three other packets' READMEs that their drafts don't hold.
- **pile-poetry**, seeded "the vault is sean's key":

      Un point c ζ à y any set
      So daß die berechnung des transcendantes
      La moitié droite de l itération des z
      Im and similarly we get a be treated
