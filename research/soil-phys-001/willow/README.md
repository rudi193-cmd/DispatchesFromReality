# SOIL-PHYS-001: the willow stack

**Sean Campbell** · Working stack · November 2026

The [SOIL-PHYS-001 ledger](../README.md)'s sources, kept the way willow keeps
sources: by address, time and SHA-256, never their text. It runs on the
[willow](https://github.com/willow-memory/Willow) kernel and its stdlib
add-ons, local only, standard library only.

| File | What |
|------|------|
| [build.sh](build.sh) | Makes the folder: clones this repo, fetches every open source with almanac-keep and holds it to its logged hash, turns them into text with willow's readers, starts three boxes |
| [stack.md](stack.md) | 86 steps in 13 pools, 72 add-ons: the ledger against its sources, the catalog and nuggets, the sources asked directly and in their own languages, kept and sealed, the packet and the repo read across, privacy and code guards, the record, what it makes in `out/`, and play |
| `sections.txt` | The ledger's six sections as `sort` categories, in the ledger's own words |
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

## 81 add-ons

Willow has 337 add-ons. This stack uses every one that has something to say
about this packet, 81 with the ones `build.sh` runs and `snapshot` under
`almanac-keep`; each was run on the built boxes before it went in. The rest
don't fit, and why:

| Left out | Why |
|---|---|
| Readers of other kinds of file (93) | The pile is PDFs, web pages, TEI and Markdown; `build.sh` uses the readers for those |
| Life logs (garden, car, pets, budget, baby-log and the like) | They each said, correctly, that nothing here is a garden or a car |
| Editor and assistant setup (aider, cursor, vscode, vim and the like) | They print a config to paste, not a check |
| Anything that needs an approved answer (export's answers, static-search, annotations, rss-out, badge's count, pile-gold, pile-sweep, quantized, deep-links) | Approving is the key's, and the key is Sean's; nothing here is approved |
| `predict ask` | `stack` adds `--json` to a report add-on's step, and `ask` takes none; run it by hand |
| `browse`, `pipe` | One waits at a prompt, the other reads its standard input |
| Model, network and sealing add-ons | The stack runs local and offline, and never seals |

---

## A run, 2026-11-06

`build.sh` from scratch, then the stack, on willow's main (93b2add):

- **Sources:** 27 held to their SHA-256 (every PDF and text file, the four browser downloads among them); 4 web pages whose bytes changed and whose text didn't; 5 live pages (Springer's and the reprint's) whose text changed too, an access counter or a notice, so the packet's copy is the record; Solomonoff's publisher page, a redirect stub, set aside. Weyl's page answered 429 the first time, a rate limit.
- **The ledger's quotes** (`quotes`): 33 in DRAFT.md, 10 as written, 19 almost, 4 not there. The four: Klein's words in English (his paper is German), Casimir's and Goldstone's (scans), and "deletion is an appended tombstone", revision 1's claim about willow, which nothing holds. Most of the "almost" are the pdf reader's: a word split at a line end ("univer se", "multi plets") or a ligature left as one character ("oﬀ"); the rest are the ledger quoting its own earlier wording in CHANGED lines, which no source holds.
- **The deciding quotes** (`misquote`): 6 of 6 as written, Leibniz's "would not at all differ" among them, which willow's study of these sources missed because its runner kept each of Leibniz's paragraphs on one line; `build.sh` breaks such lines with the text add-on.
- **Short claims** (`claim-check`): "gravity is an entropic force" has every part in Verlinde, "Rule 110 is capable of universal computation" in Cook; "the metric is proportional to entanglement" has every part nowhere.
- **Asked directly** (`fair-merge`): "is space absolute or relative" serves Leibniz's third paper first; "what happens to the ground state when a symmetry is broken" serves Nambu's lecture first.
- **The repo** (`xref`): 305 references, none broken. (`pair-drift`): this packet's README holds a "256" its draft doesn't, the 256 of SHA-256; across the repo it flags figures in three other packets' READMEs that their drafts don't hold.
- **The full stack, again from scratch:** `build.sh` in 66 seconds (27 sources held to their hashes, 0 differ), the 86 steps in 180 seconds, none refused, 14 with something for you, 8 files in `out/` (a PROV record, an in-toto statement, a folder card, a timeline, a calendar of what's coming up, CloudEvents, a printable answer, a badge). Among them: `thesis` puts each of the draft's 167 sentences to the sources and finds 11 held whole in one passage; `sort` places 25 of the 35 source files in the ledger's sections; `stems` reads "Feldgleichung" as Einstein's "Feldgleichungen"; `launcher` finds Mach's "absolute space and absolute motion ... are pure things of thought"; `a11y-check` finds one heading that skips a level, in `creative/`; `fixity` and `changed` fingerprint the 35 source files so a later run says what moved.
- **pile-poetry**, seeded "the vault is sean's key":

      Un point c ζ à y any set
      So daß die berechnung des transcendantes
      La moitié droite de l itération des z
      Im and similarly we get a be treated
