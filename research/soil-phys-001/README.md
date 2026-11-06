# SOIL-PHYS-001: The Arbitrary Seed and the Bounded Void

**Sean Campbell** · A speculative ledger, held to its sources · November 2026

**Tags:** `foundations-of-physics`, `symmetry-breaking`, `von-neumann-ordinals`, `relationalism`, `holography`, `provenance`, `source-checking`, `willow`

*Nothing physical is ever an empty zero. The smallest thing that exists is a boundary around one: {0}, which von Neumann already called 1.*

For the broader research map, see [Research Portfolio](../README.md). For the provenance states used here, see [Nobody Counts the Ad Breaks](../childrens-software-interruption/README.md).

---

## Current versions

| Version | Form | Status | Purpose |
|---------|------|--------|---------|
| **Rev 3** | The ledger | [DRAFT.md](DRAFT.md) | Every entry marked SOURCE (what a cited work shows), READING (this ledger's interpretation) or CHANGED (what an earlier revision said and why it moved); SOURCE lines checked against their texts marked CHECKED |
| **Checks** | Claim table | [CHECKS.md](CHECKS.md) | 44 lines, each with its verdict and the source's own deciding words |
| **Kept** | Source table | [KEPT.md](KEPT.md) | The 49 cited works: which are held, as what, by SHA-256 |
| **Stack** | willow | [willow/README.md](willow/README.md) | The sources as an Almanac catalog, the SOURCE lines as Jeles nuggets, and the scripts that rebuild both |
| Packet | Public summary | This file | Scope, method, evidence, claim boundaries |

Revision 2, before the checks, is this file's history: the commit before revision 3.

---

## Core question

The ledger argues that true zero is never observed: every physical "zero" is a ground state with something in it, a horizon, or a breakdown, and the minimal existing thing is the container {0}. It leans on forty-odd works from Planck to the Platonic Representation Hypothesis. Which of its lines are what those works say, and which are the ledger's own reading of them?

---

## Method

1. **Revision 1** was written as a synthesis, its citations attached to its claims.
2. **Revision 2** separated the lines: SOURCE for what a work shows, READING for interpretation, and fixed the citations that were wrong (dates, venues, credits).
3. **The sources were kept, not just cited.** Each work became an entry in an Almanac catalog with its address; each address was probed and logged; each open copy was fetched with willow's `almanac-keep` and held by SHA-256. Where a publisher refused scripts but serves a reader, the copy was downloaded in a browser and logged as such. Paywalled papers are held by hash only, never committed.
4. **Revision 3** held every SOURCE line whose work is held in full to that work's own words. Readers quoted the deciding sentence; every quote was then searched for in its file, or read on the page where a scan has no text layer.

---

## What the checks found

| Verdict | Lines |
|---------|-------|
| Holds | 28 |
| Holds once reworded | 11 |
| Does not hold | 3 |
| Not in the text held | 2, both since settled by later texts |

**Revision 1's three strongest claims fail on their own sources.**

- "The metric g_μν is directly proportional to entanglement": the only proportionality in Ryu and Takayanagi, Van Raamsdonk, or Maldacena and Susskind is a surface's area to entanglement entropy.
- Sakharov's "conserved ground offset": his own words are "we assume that the baryon and muon conservation laws are not absolute".
- Large models converging on "the geometry of physics": Huh et al. hypothesize "a shared statistical model of reality"; the word physics appears only in their references.

**Revision 2 overstated its sources too, and revision 3 says less.** Sakharov never lists three conditions; that list is how later physics summarizes his mechanism. The 1964 papers give mass to some gauge bosons, "in certain cases", not to all. Klein's fifth dimension is periodic with a period tied to Planck's constant, not "compact and small". Tegmark finds 3 + 1 dimensions "not implausible", not singled out. Nernst's 1906 theorem is a hypothesis about work and energy, not yet about entropy. Solomonoff weights every description of the data, not only the shortest.

**The thesis has an ancestor, and it's already in the pile.** The stack, sorting the sources into the ledger's sections by the ledger's own words, put almost nothing in "zero": the section the ledger is built around is the one its readable sources say least about. What it found instead, in Mach's history of mechanics, was *horror vacui*: "Nature was thought to possess the power of preventing the formation of a vacuum ... it must be conceded, that to a certain extent it really represents the phenomenon. ... This principle, however, does not fit all cases." The ledger's line 0001 now carries it, as a source beside a reading: a precedent, and a warning that the cases decide.

**The zero section has its sources now, and they are German.** The stack's sort was right that the section's readable sources were thin, and half wrong about why: the ones that exist are in German, and the ledger's words for zero were English. Five public-domain works fill it, each kept by SHA-256 and checked:

- **Zermelo (1908)** builds the ledger's {0} fifteen years before von Neumann. His number series "enthält die Elemente 0, {0}, {{0}} usw." (contains the elements 0, {0}, {{0}} and so on), "weil ihre Elemente die Stelle der Zahlzeichen vertreten können" (because its elements can stand in for numerals). And the empty set enters his axioms as "uneigentliche", improper.
- **Frege (1884)** defines 0 as the number of the concept "sich selbst ungleich" (not identical with itself), "weil unter den Begriff ... nichts fällt" (because nothing falls under it), and 1 as the number of the concept "identical with 0". **Dedekind (1888)** starts the numbers at 1, and his preface lists "die Schöpfung der Null" (the creation of zero) among the later extensions, beside the negative and fractional numbers.
- **Planck (1911)** gives an oscillator hν/2 at absolute zero, and **Einstein and Stern (1913)** argue for it from hydrogen's specific heat, then admit in a footnote that their derivation of the radiation law needs hν instead, and leave the discrepancy to "spätere Untersuchungen" (later work). The first case for a full zero did not yet know how full.

So the mathematics makes zero the empty thing and at once puts it in a container, which is the ledger's {0}; it does not say a physical zero is never empty. That stays the ledger's READING.

**The other side of the relational argument is now a source.** Newton is the most-named person in the sources, because Leibniz and Mach argue with him, but revision 2 cited only them. His Scholium is in now: "Absolute Space, in its own nature, without relation to anything external, remains always similar and immovable."

**The nearest a source comes to the thesis.** Goldstone, in his 1960 CERN preprint, of a field whose symmetry allows many ground states: "The phase of χ is not determined. Fixing it destroys the symmetry." That is about a field's phase, not an origin of the world, so the ledger keeps its own line as a READING beside it.

---

## Willow's tools against the reading

The first 35 checks became the answer key of a pre-registered study in willow
(`demo/soil-phys-001`, on its branch of that name): can willow's own tools
stand in for reading these sources? Frozen before it ran, run once:

| Tool | Result |
|------|--------|
| `misquote`, each deciding quote in its source | 29 of 30 readable quotes found; the one missed, Leibniz's, was past the 500 characters the kernel (willow's known bug #89) reads of a line in that study's text, and is found once the line is broken ([willow/README.md](willow/README.md)) |
| `claim-check`, every part of a true line in one passage of the right source | 6 of 25; a claim of eight to fifteen words rarely has every word in one passage, and six sources aren't in English |
| The kernel, a plain question per line, the right source in its top three | 17 of 25, but it also served something to 8 of 10 off-topic questions: a short question over a large pile |

So `misquote` can stand in for finding a quote; `claim-check` can't stand in for reading a claim; and the kernel's finds have to be read beside how freely it serves short questions. The reading stays the evidence here.

---

## Provenance

Read in this repo's states:

| Ledger mark | State | Why |
|-------------|-------|-----|
| SOURCE, CHECKED | `measured` | The line was held against the work's own text, read at first hand |
| SOURCE, not checked | `assumed` | The work is cited, not held in full here; the line rests on the citation |
| READING | none | An interpretation, not evidence; no state raises it |

A CHECKED line held against a reprint, a translation or an author's later lecture says so in the line.

---

## Claim boundaries

- **Held in full: 34 of 49 works.** Not held in full: Weyl (1918, 1929), Ehrenfest, von Neumann, Anderson, Penrose, Wilson, Wolfram, Dirac, Feigenbaum, Planck 1901 and Nambu's 1960 paper (paywalled, or no open copy found), two books under copyright (Spencer-Brown, Mandelbrot), and CODATA, held as NIST's index page. Einstein's hole argument (1913-14) is cited in a line but not catalogued. Their SOURCE lines are `assumed`.
- **Some checks rest on secondary forms of a work:** Sakharov's 1991 reprint, Kaluza in translation, Mach's 1893 translation, Casimir's academy reprint, Nambu's 2008 Nobel lecture for his 1960 idea. Each is named where it is used.
- **Some open copies are not the holder's own:** Zermelo's and Einstein and Stern's scans are CC0 deposits on Zenodo whose uploader isn't named (both works are public domain in the US, and each was read against its printed page numbers); Planck's 1911 paper is a retyped German text on a staff page at the Royal Observatory Edinburgh, not a scan; Frege's is Project Gutenberg's transcription; Dedekind's is the Internet Archive's OCR of RCIN's scan of the 1888 edition.
- **Scans were read, not searched,** where they have no text layer: Solomonoff, Klein, Casimir and Goldstone's preprint.
- **Nothing here says the thesis is right.** The checks show what the cited works say. Whether {0} is the right picture of physics is the ledger's READING, and stays one.
