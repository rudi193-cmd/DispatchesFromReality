# Study 2: the result

**Run once, 2026-11-04, 03:24 Mountain time,** under the freeze in commit
`5182284`, on the same three pinned files as Study 1 ([result.json](result.json)).
Sean's wagers are rows 1 to 3 of the study's willow record, written at 03:20,
before the run; the verdicts are rows 4 to 6. `kernel.py verify`: the chain
holds. One correction to the frozen plan: it gives the wagers' time as "about
03:40"; the record shows 03:20, which is the time that counts.

---

## The verdicts

Held-out months February 2025 to March 2026: 53,152 events. The burst rule
found three burst months in them: **June 2025, October 2025 and March 2026.**

| | Prediction | Measured | Rule (pooling / against) | Verdict | 95% of 200 resamples | Sean's odds |
|---|---|---|---|---|---|---|
| P1 | Rising floor | 0.49 (all), 0.36 (100 or more) | 1.1 / 1.0 | **against** | 0.46 to 0.80, and 0.33 to 0.52 | 55% |
| P3 | Carryover across issues | 0.94 | 0.95 / 0.85 | inconclusive | 0.60 to 3.76 | 15% |
| P4 | Returning organizations | 0.71 | 0.8 / 0.5 | inconclusive | 0.67 to 0.81 | 55% |
| P2 | Spread that sticks (reported, not tested) | 0.74 | | | 0.57 to 1.35 | none |

---

## What each one says

**P1 came out `against`, and the measure is the first thing to doubt.** The
rule fits a line to the 8 quiet months before each burst and asks whether the
months after rise above it. Here are the active counties, month by month:

| Month | Active counties | Of them, 100 or more | |
|---|---|---|---|
| 2024-10 to 2025-01 | 472, 393, 274, 430 | 176, 91, 32, 146 | |
| 2025-02 to 2025-05 | 408, 543, 977, 699 | 190, 216, 726, 245 | |
| **2025-06** | **1,250** | **972** | burst |
| 2025-07 to 2025-09 | 731, 626, 766 | 153, 75, 167 | |
| **2025-10** | **1,406** | **1,120** | burst |
| 2025-11 to 2026-02 | 322, 288, 962, 470 | 66, 37, 320, 209 | |
| **2026-03** | **1,611** | **1,127** | burst |

The 8 "quiet" months before June 2025 run from October 2024 to May 2025:
down to the post-election low of December, then up to April's 977, a month
the rule calls quiet only because 2025 as a whole was so high. The line fitted to that ramp points steeply up,
and the summer could not keep pace with it. So P1 reads the end of a ramp as
a fall. **The frozen rule also let the trend window cross January 2025, the
change of term, which Study 1's rules did not allow:** an oversight in the
design, found by the run.

Against that, read the counts plainly: the quiet months of summer 2025 (626
to 766 active counties) sit well above the quiet months of 2024 (about 400).
That is what a rising floor looks like, measured crudely and without a
control. Then November and December 2025 (322 and 288) fall below 2024's.
Neither of those is a test; both are worth knowing.

**P3 is one burst, compared with the other term.** Only June 2025 had six
months of room, and its matched placebos, quiet months 3 to 12 months away,
all fell before it, in June 2024 to March 2025: mostly the end of the Biden
term and the transition. The ratio, 0.94, sits just under the line, and the
resamples run from 0.60 to 3.76. This says nothing either way.

**P4 points the other way from returning.** In the held-out bursts, 63
percent of events named an organization seen before, against 89 percent in
quiet months. Only 3.5 percent of resamples reach the pooling line. The 2025
bursts drew in a great many new names. That is inconclusive by the rule, but
it leans toward bursts recruiting new groups, not drawing on old ones, which
is the opposite of what P4 predicted.

---

## The wagers

Proposed for Sean's seal: P1, P3 and P4 all did not come out `pooling`. Once
sealed, the Brier score over the three is 0.21, better than a coin at 50
percent; the 15 percent call on P3 earns most of it.

---

## Both studies, side by side

| | Study 1, 2017 to 2025 | Study 2, Feb 2025 to Mar 2026 |
|---|---|---|
| P1 Rising floor | pooling, on a thin control | against, on a measure that misreads a ramp |
| P2 Spread that sticks | inconclusive (undetermined) | reported only: 0.74 |
| P3 Carryover across issues | could not be computed | inconclusive, one burst |
| P4 Returning organizations | inconclusive at the line | inconclusive, leaning new |

**What two studies support:** not pooling as a finding. The one prediction
that passed in Study 1 failed in Study 2, and the reason it failed is as much
the instrument as the world. What holds across both is narrower: bursts are
frequent, quiet months between them move a lot, and the organizations that
carry a burst are a mix of old and new, newer in 2025 than before.

---

## What a third study would need, written before any of it is tried

- A P1 control that survives a ramp: a seasonal baseline (the same months a
  year earlier), or a trend window that may not cross a change of term.
- The full second term, so that P2 and P3 have room.
- Population per county, so that recruitment can be read against how many
  people a place has.

Each a new freeze, its result reported beside these two.
