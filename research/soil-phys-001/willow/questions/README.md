# SOIL-PHYS-001: asking the sources everything

**Sean Campbell** · A run of willow's `scan` over the ledger's sources · November 2026

Revision 3 checked the ledger's lines against their sources one at a time.
This run asks the sources everything at once and reads what comes back across
all of them: which passages many questions lead to, which papers answer each
other, which ideas meet in some passage and which meet nowhere.

Every answer is the kernel's own. Willow's `scan` indexes a folder once and asks
it a file of questions, each answered as the kernel's `rank` would answer it,
or by BM25 with `--rank bm25`. Nothing is written to a box's record.

| File | What |
|---|---|
| [run.sh](run.sh) | Indexes the built stack's `pile/sources`, writes the questions, asks them with both rankers, and reads the answers |
| [make_questions.py](make_questions.py) | The questions: the papers' own, the pairs of ideas, the ledger's lines |
| `questions.tsv` | The 7,637 questions this run asked (the ledger's part came from DRAFT.md as it stood that day, 60 lines; it has more now, and `run.sh` writes the current set over this file) |
| [analyze.py](analyze.py) | The passages served first most often, the sources served least, and the papers' questions another paper answers |
| [pairs.py](pairs.py) | Which pairs of ideas meet in a passage, in which sources and languages, and which meet nowhere |
| [look.py](look.py) | Prints where named pairs meet: `WILLOW=DIR python3 look.py "zero|nothing" "empty|set"` |
| `own_answered.json`, `pairs_out.json`, `lang_only.json` | The run's summaries. `kernel.jsonl` and `bm25.jsonl`, tens of MB, are made again by `run.sh` |

Run it from a folder `build.sh` made:

    WILLOW=WILLOW_DIR bash run.sh HOME_DIR

## The questions

- **332 the papers ask.** Every sentence in the sources of 4 to 40 words that ends in a question mark: Leibniz's "Whether Space is an absolute Being?", Ehrenfest's "For does space 'exist'?", Verlinde's "How does force arise?".
- **7,245 pairs of ideas.** 70 of the ledger's ideas (zero, nothing, empty, vacuum, void, ground state, boundary, origin, unit, container, distinction and the rest), every pair, each asked in English, German and French. Two ideas *meet* where one passage holds both. The kernel ranks a passage holding both words above any holding one, so a pair that meets nowhere in the answers meets nowhere in the pile, in those words.
- **60 of the ledger's lines**, SOURCE and READING, with quotes and parentheses taken out.

## The run, 2026-11-06

Over the pile `build.sh` makes, trimmed to the cited papers: 19,220 passages, 52 sources. The kernel's ranking took 5 minutes, BM25 2. 7,345 of the 7,637 questions found something.

**The passage most questions lead to is Dedekind's §2.** Served first for 99 questions: a system of "einem und nur einem" (one and only one) element admitted for uniformity, and "das leere System, welches gar kein Element enthält", the empty system, excluded, though "it may be appropriate to imagine such a system" (*erdichten*, to make up). In the ledger as line 0002a. The other most-served passages are a reference list on Springer's page for Feigenbaum (135), Mach on Maupertuis (113), and Dedekind's preface (92).

**The papers' questions, answered by another paper.** 13 of the 332 are answered by a passage from a different source holding all their words. Leibniz, 1716, "Whether Space is an absolute Being?": Mach, 1883, "the question whether a motion is in itself uniform, is senseless". Ehrenfest, 1917, "Is it three-dimensional?": Mach, on mathematical possibilities, which have "nothing to do with the question whether things really exist which correspond to these possibilities". Verlinde, 2011, "How does force arise?": Mach, on force known first from "our own volitional acts", "always sensible of a pressure". The rest are near misses on a word. Mostly the papers don't use each other's words.

**The pairs.** Of 2,415 pairs, 680 meet in no passage and 502 in one source only (Planck's book 78, Weyl's 74, Mach 59, Julia 38). 106 meet only outside English: 69 only in French, 33 only in German, 4 in both.

- **Container** meets 17 of the other 69 ideas, the fewest, and only ever as the French participle *contenant*: never with empty, element, ground state or distinction. The ledger's container is the ledger's own word. Its nearest: Julia's "une surface ... simplement connexe, contenant l'origine" (a simply connected surface containing the origin).
- **Zero** never meets **void**, and meets **ground state** only in Tegmark's "measure zero". **Empty** never meets quantum, temperature, symmetry or unit: in these sources emptiness belongs to the mathematics, and physics says vacuum.
- **Zero** and **nothing** meet in Frege's §75: "Null ist die Anzahl, welche einem Begriffe zukommt, unter den nichts fällt" (zero is the number belonging to a concept under which nothing falls). **Zero** and **one**, in his §89: "Die Null, die Eins sind Gegenstände, die uns nicht sinnlich gegeben werden können" (zero and one are objects that cannot be given to us through the senses). In the ledger as line 0001c.
- **Empty** and **vacuum** meet in Mach's *horror vacui* (line 0001a) and in Julia's "Pour ne pas raisonner dans le vide, il importe d'abord de prouver que E contient toujours des points" (so as not to reason in the void, first prove E always contains points). In the ledger in 05.02, beside Frege's "leeres Zeichen".

**The ledger's lines.** The kernel answers 24 of the 39 SOURCE lines and 4 of the 21 READING lines: no passage holds half the words of most readings. The readings are the ledger's own, and the box can measure it.

**The sources least asked for**, by times in any question's top three: van Raamsdonk (7), Leibniz's first paper (8), Nernst 1912 (22), von Neumann (34), Kaluza (35), Newton (38).

**Who the sources name** (`people`): Einstein and Newton, 254 mentions each; Galileo 179, all in Mach; Riemann 128. Leibniz isn't counted: `people` counts a name when the files show it doing a person's thing, and these sources argue with him without ever saying "Leibniz said".

## What it can't say

- **Meeting is sharing a passage**, not an argument. Two words in one passage can be about different things; every meeting the ledger uses was read.
- **The ideas and their translations are one person's list.** Other words for the same idea (Fichte's *Nichts*, Aristotle's *kenon*) were not asked.
- **OCR misses words.** A scan's noise ("Grümden", "rie pas") can hide a meeting; the scans' meetings were read on the page.
