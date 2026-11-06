# Before It Was in the Minutes: the willow stack

**Sean Campbell** · Working stack · November 2026

How to rebuild the pile behind the [packet](../README.md) and rerun every
reading in it. It runs on the [willow](https://github.com/willow-memory/Willow)
kernel and its add-ons, local only. The pile is built by willow's own markets
demo, `demo/markets-2026-11-05`, which fetches each source once, pins its
SHA-256, and checks it offline after that.

| File | What |
|------|------|
| [stack.md](stack.md) | The readings, in pools: the draft's quotes and claims against the Fed's own text, the draft held to this packet, the vocabulary dated, the retirement sort |
| `retirement.txt` | The three retirement categories the sort reads |

---

## Build it

    git clone https://github.com/willow-memory/Willow WILLOW
    python WILLOW/demo/markets-2026-11-05/fetch.py --to PILE --contact YOUR-EMAIL
    python WILLOW/demo/markets-2026-11-05/mirror.py --from PILE --to MIRROR

`--contact` is needed only for SEC EDGAR, which refuses a client that names
no contact; the address goes to sec.gov in the request header and nowhere
else. Then make three boxes, each over its own folder, with every line broken
at its sentences first (the kernel reads only the first 500 characters of a
line; the money hour demo's `run.py` has the `fold` that does it):

| Box | Pile | Used for |
|-----|------|----------|
| `boxes/fed` | The FOMC's statements, minutes and press conference transcripts, 2023 to 2026, folded | Quotes, claims, the vocabulary chain, the timeline |
| `boxes/filings` | The 55 latest 10-Ks, folded | The retirement-language sort |
| `boxes/packet` | This packet's DRAFT.md and README.md, folded | pair-drift: the draft's figures against the packet's |

Each box needs `kernel.py init` and a key of its own. Nothing in this stack
seals; the key is only the box's.

---

## What the stack found on 6 November 2026

- **Quotes:** five of five Fed quotations in the draft are in the Fed's own files as written.
- **Packet drift:** none, after one fix. The first check found three figures only in the packet; each was the same number worded as a range on one side ("302 to 375") and a change on the other ("from 302 to 375"), and both texts now word it the same way.

---

## Limits

- First and last appearances are within the pile, which begins in 2023.
- The kernel reads "3-3/4" as 3, 3 and 4, so neighbouring rate ranges share every part; open the cited passage, do not trust the count.
- A word list from `dialect` over the press conference transcripts is mostly reporters' names, and curly apostrophes split contractions ("wouldn").
