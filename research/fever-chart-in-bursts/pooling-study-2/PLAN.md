# Study 2: the pre-registration

**Status: frozen, not run.** `FROZEN.json` holds the SHA-256 of every file
here, and the commit that adds it, alone, is the pre-registration. A change
after that is a new freeze, with its reason.

---

## Why a second study, said plainly

[Study 1](../pooling-study/PLAN.md) ran once on January 2017 to January 2025.
[Its result](../pooling-study/results/README.md): the rising floor held on a
control of three placebo months from one season; P2 was undetermined; P3
could not be computed; P4 sat on its line. Every rule below was written
**after seeing that result**, by people who have also seen the 2025 headlines.
What makes this a test and not a retelling is that it is scored on months no
rule had been computed on: **February 2025 to March 2026.** Everything before
February 2025 is read only as history.

**What has been read before the freeze:** the counts-only dry run below. No
month, county, burst or prediction has been computed on the held-out months.

---

## The data

The same three pinned files as Study 1, by the same SHA-256s
([../pooling-study/sources.json](../pooling-study/sources.json)). Nothing new
is downloaded.

**The window:** history from 20 January 2017; held-out months from February
2025 (January 2025 straddles the term change) to **March 2026**. The pinned
Phase 3 file reaches 31 May 2026, and its last two months are left out: CCC
keeps adding events to recent months as reports surface, so the newest months
are the thinnest, which would bias every after-burst window down.

---

## What changed from Study 1, and why

| | Study 1 | Study 2 | Why |
|---|---|---|---|
| **P1 control** | Placebo months at least 6 months from every burst | Each burst's own trend: a line fitted to the 8 quiet months before it, and the 4 quiet months after compared with where the line says they would be | Bursts are common (14 of 97 months in Study 1), so clean placebo months barely exist. Matched placebo months were tried first, on synthetic data only, and failed for the same reason: a placebo near a burst measures that burst's step |
| **P3 baseline** | Placebos with 12 months of room each side | Each burst's matched placebos, quiet months 3 to 12 months from it and at least 2 from every burst, with a 6-month follow-up | Study 1's baseline had no room inside the window |
| **P4 names** | Exact | Case, punctuation, "&" and a leading "the" loosened | A renamed group counted as new |
| **P2** | Tested | **Reported, not tested** | On the synthetic worlds, held-out P2 called two reset or exhaustion runs out of ten `pooling`. A test that can give false pooling is not a test. P2 waits for the full term |
| **Error bars** | Added after | Part of the frozen run: 200 county resamples, reported, deciding nothing | |

The thresholds are Study 1's: P1 1.1 / 1.0 in both variants, P3 0.95 / 0.85,
P4 0.8 / 0.5. Every rule is a line of [score2.py](score2.py).

---

## The power check

[synth2.py](synth2.py) runs Study 1's three synthetic worlds on through March
2026, with two bursts in the held-out months. Seeds 1 to 5:

| World | P1 | P3 | P4 |
|---|---|---|---|
| pooling | 0 of 5 `pooling` (all inconclusive) | 3 of 5 `pooling` | 5 of 5 `pooling` |
| reset | none `pooling` | none `pooling` | none `pooling` |
| exhaustion | none `pooling` | none `pooling` | none `pooling` |

[test_study2.py](test_study2.py) holds the part that matters most: no reset or
exhaustion world reads as pooling, and the pooling world never reads as
`against`.

**Said plainly: P1 has almost no power here.** Two synthetic bursts in 14
months, at the synthetic worlds' effect size, never cleared 1.1. Study 1's
real effect was larger (1.29 and 1.75), so P1 could still pass on real data,
but an `inconclusive` P1 in Study 2 should be read as "too short to tell", not
as evidence against. P3 is moderate. P4 is strong.

---

## The dry run

[wiring2.py](wiring2.py), counts only, on the Phase 3 file: 63,147 rows read,
55,275 kept within the window, **53,152 in the held-out months**, the latest
kept date 31 March 2026. Of the held-out rows, 31,878 name an organization and
52,621 carry an issue tag. Phases 1 and 2 hold no held-out rows, as expected.

---

## Threats

| Threat | Handling |
|---|---|
| **The rules were written after Study 1's result** | Scored only on held-out months; the changes and their reasons are listed above |
| **Fourteen months is short** | P2 not tested; P1's low power said in advance |
| **Recent months are under-collected** | The last two months of the pinned file are left out |
| **Phase 3 coding differs** (guidelines 3.0, the repeater flag) | The reader is Study 1's; repeaters are not removed, since Study 1 could not remove them either |
| **History is Study 1's data** | Used only to say who protested before, which organizations existed, and where a burst's trend line runs |
| **The second term is unfinished** | This is a first look; the full-term study comes when it ends |

---

## Wagers

Sean's stated odds that each comes out `pooling` in the held-out months,
given 2026-11-04 at about 03:40 Mountain time, before the freeze and before
any prediction was computed on those months. `against` and `inconclusive`
count as no. P2 is reported, not wagered.

| | Prediction | Sean's odds |
|---|---|---|
| P1 | Rising floor | 55% |
| P3 | Carryover across issues | 15% |
| P4 | Returning organizations | 55% |

The claims as `forecasts` records them, word for word:

    Pooling study 2 P1, rising floor: pooling
    Pooling study 2 P3, carryover across issues: pooling
    Pooling study 2 P4, returning organizations: pooling

---

## The order, from here

1. Sean edits this plan and wagers: done.
2. `FROZEN.json` is committed alone: done.
3. One run: `score2.py --events DATA/*.csv --draws 200 --out results/result.json --box BOX --willow WILLOW`.
4. Every verdict reported, beside Study 1's.
