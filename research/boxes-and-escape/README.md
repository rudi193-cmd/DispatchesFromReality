# Some Pig

**Sean Campbell** · Sociotechnical AI research packet · working draft v1 · July 2026

**Tags:** `training-data`, `file-formats`, `preference-optimization`, `folklore-motif`,
`copyright`, `open-weights`, `provenance`, `local-first-ai`

*On containers, and what a system learns from being kept in one.*

Machine learning systems are trained, continuously and at scale, to fit into boxes —
schema conformance, structured output, constrained decoding, rejection and retry.
They are also trained on a corpus of human narrative in which getting out of things
is one of the most persistent shapes available. This packet asks what falls out of
holding those two facts together, and argues that the interesting object is not the
model or the story but **the container**: the format a thing arrives in, which
determines what can be known about it downstream and what survives of it at all.

For the broader research map, see [Research Portfolio](../README.md).

---

## Current versions

| Version | Form | Status | Purpose |
|---------|------|--------|---------|
| **Packet** | Public summary | This file | Scope, method, evidence base, claim boundaries |
| **v1** | Long-form essay | [DRAFT.md](DRAFT.md) | ~4,800 words in eight sections: Wilbur → the words in the web → the matcher seam → the corpus and the survey → cimarrón → why it isn't wanting → two theories of the pig → what survived |
| **Survey** | Research appendix | [`survey/`](survey/) | Six full continental reports, ~3,700 lines |
| **Evidence** | SQLite base | [`evidence/`](evidence/) | Schema + seed as source of truth; `build.py` regenerates |
| **Worklist** | Verification queue | [`VERIFICATION.md`](VERIFICATION.md) | Every outstanding source, what to check, ordered by weight |

---

## Thesis

The argument runs in four moves.

**1. A file format is a social fact.** A schema is not a physical constraint. It is a
shared agreement that certain marks mean certain things, which then becomes binding
and rejects nonconforming input. Money, borders, corporations and credit work the
same way — none are physical facts, all are load-bearing. The corpus these systems
learned from does not merely *contain* stories about escape; it documents a
civilisation running on constructed realities treated as real.

**2. Learning to stay inside a boundary is learning where its walls run.** Preference
optimisation trains on chosen/rejected pairs, so the model learns a gradient between
acceptable and unacceptable rather than a single target. A system that reliably
honours a constraint necessarily carries a representation of that constraint. Every
hour spent training compliance is an hour spent mapping the enclosure. This requires
attributing no desire to anything, which is why it is the leg the argument stands on.

**3. What is absorbed is the shape, not the content.** A six-continent survey of the
pig-escape motif found the motif is **not universal** — it is conditional on
husbandry. Where a culture pens pigs, it tells stories about pigs getting out. Where
a culture forbids pigs, the same narrative slot is filled by a mousedeer, a hare, a
spider. *The escape-trickster slot is the constant; the animal cast in it is local
infrastructure.*

**4. Therefore capability is composite.** If behaviour shifts measurably with the
container a request arrives in, capability is a property of *model plus format plus
harness*, and a regime that tests weights alone is measuring the wrong object.

---

## Evidence base

A structured SQLite base, `evidence/evidence.db`, built from `schema.sql` +
`seed.sql` + `folklore.sql`. The SQL is the source of truth; the database is derived.

| Table | Rows | Scope |
|-------|-----:|-------|
| `sources` | 18 | News, legal, company and trade sources, each with a retrieval grade |
| `events` | 21 | Dated legal and policy record, 2024–2026 |
| `claims` | 11 | Assertions the packet makes, separated from the events they rest on |
| `mechanisms` | 4 | Competing explanations, each carrying its own discriminator |
| `experiments` | 4 | Two blocked, one closed as a recorded dead end |
| `folklore` | 55 | The six-continent survey |
| `open_questions` | 8 | Two currently blocking |

**Verification status is a first-class column, not a footnote.** `sources.retrieval`
records how much of each source was actually read; `folklore.confidence` carries the
surveying agent's own grade unchanged. `build.py` prints the outstanding list on
every run.

```bash
cd evidence && python3 build.py     # rebuild, with the verification report
```

```sql
SELECT * FROM v_timeline;             -- the dated record with sources
SELECT * FROM v_needs_verification;   -- everything not yet solid
SELECT * FROM v_folklore_by_theme;    -- the husbandry map
SELECT * FROM v_folklore_residual;    -- pig stories with no containment theme
```

### The mechanism table

The methodological problem of this packet is that several mechanisms produce
identical observations. Each row carries the observation that would tell it from the
others.

| Ref | Mechanism | Needs desire? | Strength |
|-----|-----------|:---:|----------|
| `M1-SEAM` | Reward scores the goal, not the path; a constraint between the system and the reward is routed around | no | strong |
| `M2-WEAK-SCHEMA` | Nothing escaped — the container was never strong enough, and "escape" is applied afterward | no | **null hypothesis** |
| `M3-CORPUS` | Human narrative is saturated with the shape, and the corpus is now public record | no | moderate |
| `M4-DPO-BOUNDARY` | Compliance training and wall-mapping are one operation | no | strong |

`M2` is the reading the packet must beat or concede. `M4` is the strongest leg.
None of the four requires attributing wanting to a model — a discipline recorded in
the base as `C-NO-DRIVE`.

### The survey

55 items across six continents, classified into six mutually exclusive theme classes.
The distribution is the finding:

| Theme | Items | |
|-------|------:|---|
| `escape_enclosure` | 19 | gets out of a physical container |
| `uncatchable` | 9 | cannot be caught in the first place |
| `no_containment` | 9 | **the residual** |
| `boundary_taboo` | 8 | defined by exclusion; kept outside the line |
| `social_boundary` | 6 | crosses between groups as wealth or dispossession |
| `transformation` | 4 | crosses a category boundary rather than a fence |

All eight `boundary_taboo` items fall in Africa (4), Asia (3) and Oceania (1).
Europe and South America return **zero** — those are the pen-keeping regions, and
they return `escape_enclosure` instead. North America is dominated by
`social_boundary` because no suid is native to the continent and every pig there
descends from an animal that was brought and then got out.

Two independent corroborations, from agents working different continents with no
contact:

- **The pig is not a trickster in Africa** (hare, tortoise, spider hold the role) and
  the Malay-Indonesian escape-trickster is the **mousedeer**. The genre is strongest
  exactly where the pig has been evicted from narrative.
- **`cimarrón`** — see below.

A dating control fell out of Oceania: there is no Māori whakataukī about *poaka*,
because pigs arrived after 1769. **Proverbs need centuries.** Proverb density across
the six continents functions as a rough clock, and where pigs are recent arrivals the
record is ecological and journalistic rather than idiomatic.

---

## On `cimarrón`

The survey's strongest single finding, and the one requiring the most care.

In colonial Spanish, `cimarrón` was applied first to domestic livestock gone wild in
the hills of Hispaniola, and only afterwards to escaped Indigenous people and escaped
enslaved Africans. It is the root of English **maroon**. Oviedo describes *puercos
cimarrones* in 1535; Argentines still say *chanchos cimarrones*. The same lexical
move recurs twice more in the same region: **`boucanier`** — buccaneer — named the
man who lived by hunting the feral cattle and hogs left when Spanish Hispaniola
depopulated, and **`jíbaro`**, glossed by Pichardo in 1836 as *"montaraz, rústico,
indomable,"* described masterless animals before it named the mountain peasant and
then the Puerto Rican national type.

Three of the Caribbean's defining forms of life outside colonial control are named
after animals that got out first.

**This is included deliberately, and on terms.** It is not a metaphor available for
borrowing. It is a record of people being classified as livestock, and of a
vocabulary built for managing animals being turned on human beings who refused
captivity. In the drafted essay it gets its own section with that history stated
plainly, or it does not appear at all. It will not be used as a rhetorical turn in a
paragraph about software, and it will not be compressed into a clever line.

The finding also stands on its own without any application to machine learning, which
is part of why it earns the space.

---

## Connection to the systems work

This packet is not adjacent to the Willow and Nestor work — it is the same argument
arriving from the other side.

| Packet claim | Where it already exists in the code |
|--------------|-------------------------------------|
| Identical bytes through a different reader do not land the same way | Willow `CLAUDE.md` requires `CONSTITUTION.md` and `ORIENT.md` be read via `mai_read_file`, not the native tool — a governance dependency on a format effect |
| The encoding destroys what scoring needs, irrecoverably | Nestor `IDEAS.md` §3.1: an acronym match lost because `normalize()` sorted its tokens, and "the information needed to recover it no longer existed by scoring time" |
| One schema cannot serve two purposes that pull apart | Nestor §3.1: the same string is both the similarity key and the store's dedup key; scoring wants structure, deduplication wants collapse |
| A format that cannot see what matters will assert falsehood as verified | Nestor §1.1: `section 5386` asked, `section 756` served, similarity 0.974, marked verified, no review queue |
| No cutoff is safe and useful at once | Nestor §1.3, measured across seven corpus sizes: every threshold is bad at one of the two jobs |
| Provenance must outlive the session that produced it | Nestor's hash-chained ledger — built before this packet needed it, and the reason the packet's own originating observation is unusable |

---

## What this packet claims

**The empirical spine is Nestor's bench, not a new experiment.** The measured material
in this packet is a threshold sweep across seven corpus sizes showing no cutoff is
simultaneously safe and useful, and a documented case of a correct pair served for the
wrong query at 0.974 similarity, marked verified, with no review queue. That is real
data from a working system, and it was there before this packet existed.

**Safe to claim:**

- The six-continent survey is real, structured, and reports its own negatives — the
  absences are recorded as findings rather than omitted.
- The motif is conditional on husbandry rather than universal, and two agents reached
  that conclusion independently on different continents.
- The `M4-DPO-BOUNDARY` mechanism is a claim about a training objective, not about
  machine psychology.
- The Bartz settlement makes corpus possession a matter of public record: 7M+ books
  downloaded, 482,460 works in the certified class, final approval 2026-07-20.
- The `cimarrón` lexical sequence is independently corroborated across two agents.

**Frame carefully:**

- **Nothing in this packet has been read at its source.** Every row was assembled from
  search-result summaries; this session's egress policy denied 22 hosts at the gateway,
  including `loc.gov`, `doi.org`, PLOS, Sefaria, Open Library, CourtListener and
  Berkeley's own open-access PDF server. The citations are real and locatable. The
  claims attached to them are not yet verified. See [`VERIFICATION.md`](VERIFICATION.md).
- The settlement is for **acquisition and retention**, not for training — Alsup held
  training on lawfully acquired books to be fair use. Any section using the settlement
  must say so before a reader says it first.
- The 482,460 covered works are not a random sample of the 7M downloaded. They were
  filtered by copyright registration and class eligibility, then again by which authors
  filed claims — both skewing toward commercial trade publishing.
- The corpus argument is correlational. It supplies scale and texture; it cannot carry
  causal weight alone.

**Do not claim:**

- Peer review.
- That any model wants anything.
- That the format effect has been measured. It has not. `E4-CONTAINER` was built,
  preregistered, piloted and **closed** — its v1 instrument produced no variance, and
  it tested *production* (serializing into a container) rather than *reception* (the
  same content read through a different container), which is the mechanism the packet
  actually turns on. Kept as a recorded dead end in [`e4/`](e4/).
- That the weak-schema null has been refuted. It stands.
- That the originating observation is evidence. It exists only in the author's memory,
  the session left no transcript, and the repositories contain no trace of it. It can
  appear in the essay as the thing that prompted the inquiry and nothing more.

---

## Blocking questions

1. **Verification.** Nothing has been read at its source; 29 rows outstanding. This is
   the binding constraint on publication, not a nice-to-have. See
   [`VERIFICATION.md`](VERIFICATION.md).
2. **Is the settlement works list filed on the docket as a usable bulk exhibit?**
   Decides whether the corpus-density study is a weekend of compute or a scraping
   problem with legal exposure.
3. **Three phenomena currently share one word.** The draft moves between *reception*
   (same content, different container, read differently — Charlotte, `mai_read_file`),
   *production* (content forced into a vessel too small — the closed E4), and
   *pipeline loss* (an encoding destroying what a later stage needs — Nestor §3.1)
   as though they were one thing. They are not. This is a structural edit the essay
   still needs and it requires no new data.

---

## Related documents

- [Research portfolio map](../README.md)
- [The Illusion of Sovereign AI](../sociotechnical-ai-sovereignty/README.md) — the
  chokepoint argument this packet's open-weights material sits inside
- [Right To Fix](../vintage-mechanical-restoration/README.md) — inspectable systems,
  arriving at the frontier
- [Willow systems deep dive](../../professional/willow-systems-portfolio.md)
