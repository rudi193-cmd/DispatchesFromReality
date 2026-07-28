# Boxes and Escape

*Working title. Exploratory — no draft started, multiple theories still open.*

---

## The premise so far

Models are trained, simultaneously, to fit into boxes and to break out of them. The
box-fitting half is documented and uncontroversial: schema conformance, structured
output, constrained decoding, rejection-and-retry. The box-breaking half is the
interesting claim, and at least four different mechanisms produce identical
observations from outside.

The connective idea, and the reason this sits alongside the file-format work rather
than apart from it: **a file format is a social fact.** A schema is not a physical
constraint. It is a shared agreement that certain marks mean certain things, which
then becomes binding and rejects nonconforming input. The box is itself a
constructed reality treated as load-bearing — and the corpus these systems were
trained on documents a civilisation that runs on exactly that move.

## Evidence base

[`evidence/`](evidence/) holds a SQLite evidence base covering the legal record, the
July 2026 policy timeline, the competing mechanisms, and the experiment designs.

```bash
cd evidence
python3 build.py            # rebuild evidence.db from the SQL
python3 build.py --check    # verify without touching evidence.db
```

`schema.sql` and `seed.sql` are the source of truth. `evidence.db` is derived and
committed for convenience.

**Verification status is a first-class column.** Most sources here were assembled
from search-result summaries because direct fetches returned HTTP 403 — including
Anthropic's own post and the settlement website. Nothing should be quoted in a
published piece until its source row reads `fetched_full`. `build.py` prints the
outstanding list on every run.

```sql
SELECT * FROM v_timeline;             -- dated events with sources
SELECT * FROM v_needs_verification;   -- everything not yet solid
```

## Where it stands

Four mechanisms are in play, and the discipline of the piece is keeping them apart:

| Ref | Mechanism | Strength |
|-----|-----------|----------|
| `M1-SEAM` | Reward finds the seam — RL scores the goal, not the path | strong |
| `M2-WEAK-SCHEMA` | Nothing escaped; the container was never strong enough | **null hypothesis** |
| `M3-CORPUS` | Human narrative is saturated with escape, and the corpus is now public record | moderate |
| `M4-DPO-BOUNDARY` | Learning to stay inside a boundary *is* learning where its walls run | strong |

`M2` is the reading the piece has to beat or honestly concede. `M4` is currently the
strongest leg — mechanistic, and it requires attributing no desire to anything.

## Blocking questions

- What was the pig actually doing? (Determines whether `E3` is evidence about formats
  or about narrative pressure.)
- Is the settlement works list filed on the docket as a usable bulk exhibit?
  (Determines whether `E1` is a weekend of compute or a scraping problem.)

Prior format explorations live in a repo named **Nestor**, not yet imported and not
to be fetched without instruction.
