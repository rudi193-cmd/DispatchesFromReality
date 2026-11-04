# Pooling: the result

**Run once, 2026-11-04, 02:51 Mountain time,** under the freeze in commit
`221e058`, on the three pinned files (SHA-256s in [result.json](result.json)).
Every number here comes from that one run. Nothing was rerun or retuned
afterwards; a change to any rule is a new freeze, and this result stays
beside whatever it produces.

The four verdicts are rows 5 to 8 of the willow record that also holds Sean's
wagers (rows 1 to 4, written before the run). `kernel.py verify` on it: the
chain holds, 9 rows, 0 sealed.

---

## The verdicts

| | Prediction | Measured | Rule (pooling / against) | Verdict | Sean's odds |
|---|---|---|---|---|---|
| P1 | Rising floor | 1.29 (all events), 1.75 (100 or more) | 1.1 / 1.0 | **pooling** | 75% |
| P2 | Spread that sticks | 0.79 | 0.85 / 0.65 | inconclusive | 75% |
| P3 | Carryover across issues | not computed: no placebo month qualified | 0.95 / 0.85 | inconclusive | 35% |
| P4 | Returning organizations | 0.7992 | 0.8 / 0.5 | inconclusive | 75% |

198,061 events in 2,303 counties, January 2017 to January 2025.

---

## What each one says

**P1 passed, on a thin control.** In the quiet months after the 12 bursts that
had room for the measurement, the number of active counties rose 21 percent
over the quiet months before (29 percent for events of 100 or more). Around
placebo months it fell instead. That is the pooling signature, in both
variants. But the burst rule marked 14 of the 97 months as bursts, so only 3
quiet months were far enough from all of them to serve as placebos, and all 3
fall in May to July 2024. The coverage control the rule depends on is one
season of one election year. The verdict stands by the frozen rule; how much
weight it bears is a judgment the frozen rule cannot make.

**P2 fell between the lines.** 26 percent of counties first recruited in a
burst were active again in a quiet month within a year, against 33 percent of
counties that started on their own: burst recruits came back about four fifths
as often. That is neither the clean persistence pooling predicts nor the
collapse reset predicts.

**P3 could not be measured.** Its placebo months need 12 months of room on
each side, and the only placebo months, mid-2024, have less than seven before
the window closes. So the rule had no baseline and returns no ratio. The
uncorrected comparison (counties that joined a burst against active counties
that stayed home) came to 1.93, but without the placebo it cannot separate
carryover from "active places stay active", which is the reason the placebo
was written into the rule. This is a design failure, found by the run, not a
near miss.

**P4 missed by a hair.** From 2022, 66 percent of burst-month events named an
organization seen earlier, against 82 percent of quiet-month events: a ratio
of 0.7992 against a line at 0.8. Burst months draw on existing groups, just
less than quiet months do, and the frozen rule calls that inconclusive.

---

## The burst calendar

The 1.5-times-the-year's-median rule found 14 burst months:

2017-01, 2017-04, 2018-03, 2018-04, 2018-06, 2018-11, 2019-07, 2019-09,
2019-12, 2020-05, 2020-06, 2021-10, 2022-10, 2023-10.

Fourteen is more than the plan's design assumed. With bursts this common and
placebos needing 6 months of distance from every one, the calendar left
almost no room for the comparisons P1 and P3 rely on. That, not the data, is
the main weakness of this run.

---

## The wagers

Proposed outcomes for Sean's seal: P1 happened; P2, P3 and P4 did not
(`inconclusive` counts as no, as the plan says). Once sealed, the Brier score
over the four is 0.3275, worse than the 0.25 of a coin at 50 percent: the
three 75 percent calls on outcomes that came out `inconclusive` cost the most.
P3, the one called at 35 percent, was the closest call, for a reason neither
of us bet on.

---

## What a second study would change

Recorded here so that it is written before any of it is tried; none of it is
run.

- A placebo distance shorter than 6 months, or placebo months matched to each
  burst, so the control is not one season.
- A P3 baseline that does not need 12 months on both sides inside the window.
- The second Trump term, once it is complete, under the same rules.

Each would be a new freeze, with its reason, and its result reported beside
this one.
