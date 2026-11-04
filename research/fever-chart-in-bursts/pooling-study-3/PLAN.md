# Study 3: the pre-registration

**Status: DRAFT, not frozen.** Frozen when `FROZEN.json` is committed alone.
This study is different from the first two in one way that matters: **its data
do not exist yet.** On 4 November 2026, CCC's published data reach 31 May
2026. Study 3 scores months after that, on versions CCC has not released.

---

## What it asks

| | Prediction | Part | Measure | Pooling at or above | Low verdict at or below |
|---|---|---|---|---|---|
| **P1** | Rising floor | main | Each held-out burst: 4 usable quiet months after it over the same months a year earlier, divided by the same for 4 before; geometric mean over bursts | 1.05 in both variants | 0.97 in both (`against`) |
| **P3** | Carryover across issues | main | Study 2's rule, unchanged | 0.95 | 0.85 (`against`) |
| **P4** | Returning organizations | main | Study 2's rule, unchanged | 0.8 | 0.5 (`against`) |
| **P5** | The midterm as pressure valve | valve | Usable months of December 2026 to March 2027 over the same months a year earlier, divided by the same for July to October 2026 | 1.1 in both variants | 0.9 in both (`drop`) |
| P2 | Spread that sticks | main | Study 2's rule | reported, not tested | |

Both variants: all events, and events of 100 people or more.

**Every P1 and P5 verdict also needs 200 county resamples to agree:** for
`pooling`, every variant's 2.5th percentile at 1.0 or above; for the low
verdict, every variant's 97.5th percentile at 1.0 or below. The power check
below is why.

**P5 is new, and it asks the paper's own question.** The draft calls election
night a test of the pressure valve: a working election lets pressure out
through the system instead of around it. If it does, protest should ease
after the midterm, relative to the year before. If burst energy pools
instead, it should rise. **A `drop` cannot tell a valve from exhaustion**;
both predict it. P5 can only tell either of them from pooling.

---

## The data, chosen by a rule

[fetch3.py](fetch3.py) takes Study 1's pinned Phase 1 and 2 files for history,
and for Phase 3, **the first version released after 4 November 2026 whose
latest event reaches two months past the part's window**:

| Part | Window | History | Needs data through | Expected |
|---|---|---|---|---|
| valve (P5) | November 2026 election | to 31 March 2027 | 31 May 2027 | late 2027 |
| main (P1, P3, P4) | Held out April 2026 to September 2027 | to 30 September 2027 | 30 November 2027 | early 2028 |

CCC releases irregularly: version 18 (10 September 2026) reached 31 May 2026,
a lag of about three months. The two-month margin is because CCC keeps adding
events to recent months as reports surface.

Each version's file is checked against the MD5 Dataverse publishes. Only its
date column is read in choosing it. A run on 4 November 2026 found no
qualifying version, as it should.

---

## What was learned before this, said plainly

- **Study 1 and Study 2** ran, and both results are public. Every rule here
  was written after them, and after an [exploratory pass](../pooling-exploratory/README.md)
  on months both had scored.
- **The exploratory pass found one precedent for P5:** after the November 2018
  midterm, quiet months ran at 0.63 of the year before. One case, seen, and
  the reason P5 exists. It is also the reason a `drop` would not surprise us.
- **April and May 2026 are in the current file** and fall inside the held-out
  window. No prediction has been computed on them; the only thing read of them
  is that the file's latest date is 31 May 2026.

---

## The power check

On Study 1's synthetic worlds, run on through September 2027 with bursts in
November 2026 and May 2027 ([synth3.py](synth3.py)), seeds 1 to 5, every
verdict with its 200-resample gate ([power-check.txt](power-check.txt)):

| World | P1 | P3 | P4 | P5 |
|---|---|---|---|---|
| pooling | 0 of 5 `pooling` (all inconclusive) | 2 of 5 `pooling` | 5 of 5 `pooling` | 0 of 5 `pooling` |
| reset | none `pooling` | none `pooling` (all `against`) | none `pooling` (all `against`) | none `pooling` |
| exhaustion | none `pooling` (1 `against`) | none `pooling` (all `against`) | none `pooling` (all `against`) | none `drop`, none `pooling` |

**Said plainly: the gate trades power for safety.** No world reads falsely
as pooling on any prediction. But at the synthetic worlds' effect size, P1
and P5 never reach a verdict either way: one or two bursts, or one election,
are too few for the resamples to agree on a 5 to 10 percent effect. **P1 and
P5 can only detect large effects.** The real effects seen so far have been
large (Study 1's P1 at 1.29 and 1.75; the 2018 midterm's 0.63), so a verdict
is possible, but an `inconclusive` P1 or P5 should be read as "not large
enough to see", not as evidence either way. P4 is strong, P3 moderate.

**Before the gate,** on point values alone, P1 and P5 each gave a false
`pooling` in one reset world of five. The gate is there to stop that.

---

## Wagers

Waiting on Sean, before the freeze: odds that each of P1, P3, P4 and P5
comes out `pooling`.

---

## The order, from here

1. Sean wagers; the plan is frozen alone.
2. A scheduled task checks once a month for a qualifying version.
3. When the valve data exist, P5 runs once; when the main data exist, P1, P3
   and P4 run once. Each writes its verdicts to the study's willow record and
   is reported beside Studies 1 and 2.
