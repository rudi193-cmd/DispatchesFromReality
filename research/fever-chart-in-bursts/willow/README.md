# The Fever Chart in Bursts: the willow stack

**Sean Campbell** · Working stack · November 2026

A willow stack that keeps the [Fever Chart packet](../README.md) honest and
current: every Brinton quote held to the 1938 text, every packet's figures held
to its draft, the four post-election tests on a calendar, and each test as a
scored prediction once you write your odds down. It runs on the
[willow](https://github.com/willow-memory/Willow) kernel and its stdlib
add-ons, local only, standard library only.

| File | What |
|------|------|
| [build.sh](build.sh) | Makes the folder: clones this repo, fetches the Brinton text and checks its SHA-256, starts two boxes |
| [stack.md](stack.md) | The steps, in pools: quotes, claims, packet drift, dates, questions, wagers, box health |
| [watch-list.md](watch-list.md) | The four tests from the draft, each with a check-in date that `coming-up` reads |

---

## Three boxes, on purpose

| Box | Pile | Used for |
|-----|------|----------|
| `boxes/sources` | The Brinton text only | Quotes and claims from the draft. A box that also held the draft would find every quote "as written" in the draft itself, which proves nothing |
| `boxes/whole` | This repo as the `markdown` and `text` add-ons mirror it, the Brinton text, and your notes | Drift between every draft and its packet, dates coming up, questions asked across everything |
| `boxes/links` | The raw repo | `xref` only: the `markdown` add-on keeps a link's text and drops a link inside the folder, so the mirror has nothing for `xref` to check |

The repo writes each paragraph on one line, and the kernel keeps only the
first 500 characters of a line. So `build.sh` reads the repo through two
add-ons before the kernel sees it: `markdown` takes the markup off, line for
line, and `text` breaks every line over 500 characters at spaces, with a
hidden `.lines` map beside each file that gives the source line. That is why
`pair-drift` names `DRAFT.md.txt.txt`: the draft, mirrored twice.

-----|------|----------|
| `boxes/sources` | The Brinton text only | Quotes and claims from the draft. A box that also held the draft would find every quote "as written" in the draft itself, which proves nothing |
| `boxes/whole` | This repo (as a wrapped mirror, see Limits), the Brinton text, and your notes | Drift between every draft and its packet, broken links, dates coming up, questions asked across everything |

---

## Build and run

    git clone https://github.com/willow-memory/Willow ~/github/willow-memory/Willow
    bash build.sh ~/github/willow-memory/Willow ~/fever-chart ~/.willow-keys
    cd ~/fever-chart
    python3 ~/github/willow-memory/Willow/adapters/stdlib/stack/stack.py --box boxes/whole --stack stack.md

The keys go to `~/.willow-keys` by default, and the script refuses a key folder
inside the stack's folder, so no pile ever holds a key. Re-running `build.sh`
pulls this repo and leaves the boxes and keys alone. Notes of your own go in
`~/fever-chart/pile/notes`; `said` reads any line shaped `Name: "quote"` there
and dates it from the nearest date above it.

---

## What the rehearsal run found

A run on 2026-11-04 over this branch, with a throwaway box and key:

- **Brinton quotes:** 10 of the draft's 13 quotations are in the 1938 text as
  written. The other 3 read "almost": two are titles of other works (Davies
  and Chenoweth), which the Brinton-only box is not meant to hold, and one
  ("can and does use force with an effectiveness the old ruling class did not
  command") is exact in the text but crosses a passage boundary, so the kernel
  sees only part of it in one passage.
- **Claims:** all four claim checks hold every part in one Brinton passage.
  Phrasing matters: "the moderates failed because they were realists" splits
  across two passages in the text, so the check is written against the half
  that names realists.
- **Packet drift:** this packet's one drifted figure ("1795 to 1796" in the
  evidence table) was fixed. `pair-drift` also reads the other research pairs,
  and two of them carry a figure only in the summary:
  `childrens-software-interruption/README.md:131` (118) and
  `postwar-institutional-legacies/README.md:62` (117). Those are left for you.
- **Links:** 291 references checked, none broken.
- **Left out:** `contradictions` and `duplicates` read the whole repo, and
  every hit was a byline date or a lesson's timing set against another's, so
  they are not in the stack. Add them back if the pile narrows.
- **Box health:** `boxes/links` (the raw repo) cannot read one file,
  `knowledge-corpus/nestor.bundle.json`, which is over the kernel's 1 MB limit.

---

## The four tests, as wagers

`forecasts` keeps a prediction on the record before the outcome, settles it
only with your seal, and scores you over time. The odds are yours to write;
nothing here writes a wager for you. Keep each claim's exact words in
`pile/notes`, since the record keeps only its hash:

    F=~/github/willow-memory/Willow/adapters/stdlib/forecasts/forecasts.py
    python3 $F wager --box boxes/whole --p P "The 2026 results are accepted without a rival claim to their authority by 2026-11-18"
    python3 $F wager --box boxes/whole --p P "Republicans who distanced themselves before the election cast a coordinated vote against the administration by 2026-12-04"
    python3 $F wager --box boxes/whole --p P "The administration treats the new Congress's subpoenas and appropriations as binding by 2027-01-04"
    python3 $F wager --box boxes/whole --p P "The new majority passes a law that touches prices, wages or housing by 2027-03-01"

Settle each on its check-in date with `forecasts.py settle --box boxes/whole
ROW yes|no`, then seal the proposal with your key. The stack's wager pool shows
the Brier score from then on.

---

## Limits

- `text` breaks a long line at the last space before 500 characters, and that
  can fall between a number and its unit. In the rehearsal it split
  "2.9 million" and "34 percent" across two lines, so `pair-drift` reports
  both as figures only the packet says. Read the line it names before you
  call it drift; both are in the draft.
- `claim-check` and `quotes` work passage by passage, so a sentence that
  straddles two passages in the source reads as short. Read the line it names
  before you call a quote wrong.
- A claim that holds every part in one passage may still deny the claim.
  "Held" says where to read, never that the source agrees.
- The stack writes nothing, seals nothing and never reads a key. Every
  approval and every settled wager is yours.
