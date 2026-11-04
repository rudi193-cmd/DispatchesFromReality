# Pooling: the pre-registration

**Status: DRAFT, not frozen.** Nothing in this folder has been run on real
data, and the data have not been downloaded. This plan becomes the
pre-registration when `FROZEN.json` is committed holding the SHA-256 of every
file here, alone, before any row is read. Until then, every rule below is
open to change.

**What has been read so far, said plainly:** the three CCC data dictionaries
and coding guidelines; the Dataverse metadata (file ids, sizes, MD5s,
versions); and the Phase 3 file's header row, by a request for its first 3,000
bytes. No event row from any phase.

**What the authors already know, said plainly:** both of us have seen the
headlines about 2017 and 2020. That is why no prediction is about the
size of a burst. All four are about what the quiet stretches between bursts
look like, which neither of us has seen.

---

## The question

[The Fever Chart in Bursts](../DRAFT.md) proposes that each burst of protest
fades as an event but leaves something behind: networks, organizations,
places that keep protesting. In systems terms, the flows spike and drop while
a stock accumulates. The competing readings are **reset** (each burst leaves
nothing; the next one starts from zero) and **exhaustion** (each burst leaves
less than nothing, as in Brinton's France after 1795). This study asks which
one the Crowd Counting Consortium's US event data look like.

---

## The data

| File | Dataset | Version | Dataverse file id |
|------|---------|---------|-------------------|
| `ccc_compiled_20172020.csv` | CCC US Protest Event Data, 2017-2020 (doi:10.7910/DVN/6OPP7H) | 1.1 | 10808404 |
| `ccc_compiled_20212024.csv` | CCC US Protest Event Data, 2021-2024 (doi:10.7910/DVN/9MMYDI) | 2.1 | 10822959 |
| `ccc-phase3-public.csv` | CCC US Protest Event Data, 2025- (doi:10.7910/DVN/RI9JFU) | 18.0 | 14226873 |

[sources.json](sources.json) pins each by id, version and the MD5 Dataverse
publishes; [fetch.py](fetch.py) downloads and checks them, and adds each
SHA-256 in the freeze commit. The Phase 3 dataset is updated monthly, so the
version is pinned, not "latest".

**Window: two full presidential terms, 20 January 2017 to 19 January 2025.**
Events are kept by their date, so the two partial months at the ends hold only
the days inside the terms. A term is the cleanest unit the data allow: each
one is a complete political cycle, and the boundary between them falls on
CCC's own Phase 1 to Phase 2 handover.

- **The first three months are a warm-up.** CCC began by counting the Women's
  March of 21 January 2017 and, its Phase 1 dictionary says, relied on Google
  searches through March; the Count Love crawl began feeding it in April. No
  county's "first" month can fall in January to March 2017, and those months
  are measured against their own year's median like any other.
- **The Phase 3 file contributes 19 days,** 1 to 19 January 2025.
- **The second Trump term is out of scope** until it is complete. Testing it
  then is a new study with its own freeze, run against these same rules.

---

## Rules

Every rule here is a line of [score.py](score.py), and the two must agree.

**An event is in scope** when it has a date in the window and a county (FIPS
code, leading zero restored), is not online-only, and is not a labor strike.
CCC stopped coding strikes in April 2023, so all are dropped, keeping the
carve-out its Phase 2 dictionary recommends: the late-2010s student climate
"strikes" (valence 1, an environment tag).

**The unit is a county-month:** a county is active in a month when it has at
least one event in scope. Counting active counties, not events, keeps the
Phase 2 change to one record per day of a multi-day event from inflating the
later years.

**A burst month** has at least 1.5 times its calendar year's median number of
active counties. Measuring against the year's own median, not a fixed level,
absorbs coverage that grows from year to year. Every other month is quiet.

**A placebo month** is a quiet month at least 6 months from any burst. P1 and
P3 take the same measurement around placebo months as around bursts and
divide one by the other, so whatever moves every month alike, including
coverage, cancels.

---

## The four predictions

Each gets one of three verdicts: **pooling**, **against** (reset or
exhaustion), or **inconclusive**. The thresholds are the pairs in score.py.

| | Prediction | Measure | Pooling at or above | Against at or below |
|---|---|---|---|---|
| **P1** | **Rising floor.** Quiet months get busier after each burst | Median active counties in the 6 quiet months after a burst over the 6 before, divided by the same step around placebo months; geometric mean | 1.1 in both variants | 1.0 in both |
| **P2** | **Spread that sticks.** Counties first recruited in a burst keep protesting | Share of counties whose first month (after a 3-month warm-up) is a burst and that are active in a quiet month within 12 months, over the same share for counties first recruited in a quiet month | 0.85 | 0.65 |
| **P3** | **Carryover across issues.** Burst turnout leads to protest on other issues | After each burst, counties that turned out on its top issue against counties active in the prior 12 months that stayed home, stratified by prior activity; outcome is quiet months with an event on another issue. Burst ratio over the placebo ratio | 0.95 | 0.85 |
| **P4** | **Returning organizations.** Bursts draw on groups already active | From 2022, share of events naming an organization seen since January 2021, in burst months over quiet months | 0.8 | 0.5 |

P1's two variants: all events, and events of 100 people or more (size
category 2 and up, the most likely to be in the news whatever else CCC was
watching).

---

## Threats, and what each rule does about them

| Threat | From | Handling |
|---|---|---|
| **Coverage grew.** A full-time manager from late 2020, a second in late 2023, a Twitter list, then Instagram (2023 to 2024), then Telegram (2022) | Phase 2 dictionary | Bursts are measured against their own year; P1 and P3 are divided by placebo months; P1 must also hold for events of 100 or more. A growth that hits burst windows harder than placebo windows would still get through, and nothing here can rule that out |
| **The Phase 1 to Phase 2 handover,** January 2021: the Count Love crawl ended and CCC ran its own. It falls on the term boundary | Phase 1 dictionary | No P1 window may straddle January 2021, so each P1 step sits inside one term. P2 and P3 follow-up windows may cross it, and that is a known weakness |
| **Multi-day events** became one record per day in Phase 2 | Phase 2 dictionary | Counting active county-months, not events, for P1 to P3. P4 counts events, and the change affects burst and quiet months alike |
| **Strikes** dropped from April 2023 | Phase 2 dictionary | All strikes out, with the codebook's carve-out |
| **Repeating events** (a weekly vigil) recorded until someone reports they stopped, flagged only from July 2026 | Phase 3 guidelines | Inside the window they cannot be told apart from other events. A vigil kept on the books after it ended would raise a quiet floor on its own, which works in pooling's favor; P1's placebo comparison absorbs it only if such vigils are spread evenly over time |
| **Organizations** have their own field only from 2021; Phase 1 mixes organizations and kinds of people in `actors` | Both dictionaries | P4 reads 2021 on only, by exact name, which misses a group that changes its name |
| **Issue tags** come from regular expressions that may differ between phases | Phase 2 dictionary | P3 compares within each burst's own 12 months; a carryover window that crosses a phase boundary uses two tag lists |
| **Geocoding** places events by city name, then county | All dictionaries | County, not city, is the unit |
| **The data's authors and the paper's sources overlap:** Chenoweth co-leads CCC and wrote the decline finding the draft cites | Dataset citations | This study tests a different claim, but the reader should know the source is not independent of the argument it is checked against |

---

## The power check

Rules that cannot tell a pooling world from a reset world cannot be trusted
on the real one. [synth.py](synth.py) builds three synthetic worlds with the
same counties, burst months and coverage (which doubles over the window in
every world), differing only in what a burst leaves behind. [test_study.py](test_study.py)
holds the result. On seeds 1 to 5:

| World | Runs | Every prediction `pooling` | Any prediction `pooling` |
|---|---|---|---|
| pooling | 5 | 5 | 5 |
| reset | 5 | 0 | 0 (three runs had P1 `inconclusive`, the rest `against`) |
| exhaustion | 5 | 0 | 0 |

**Said plainly:** the first version of P1 (a yearly floor over the year's
peak) and of P3 (a permutation test on issue tags) could not tell the worlds
apart, and were rewritten as the placebo comparisons above. The P2 and P3
thresholds were then set from where the synthetic worlds fell. All of that
was done on synthetic data only, before any real row was read, and is the
reason the freeze has to come before the fetch.

---

## The order, from here

1. **Edit this plan.** Every threshold, the window and the burst rule are
   open until the freeze.
2. **Wager.** Sean writes a probability for each prediction coming out
   `pooling`, as `forecasts` wagers on a willow box, before the freeze. The
   claims to wager on are the four rows of the predictions table.
3. **Freeze.** `fetch.py --to DATA --pin` downloads the three files and adds
   their SHA-256s; then `FROZEN.json`, holding the SHA-256 of every file in
   this folder, is committed alone. That commit is the pre-registration.
4. **Run once.** `score.py --events DATA/*.csv --out results/result.json
   --box BOX --willow WILLOW` writes the four verdicts as rows on the box's
   record, with the hashes of the data and the script. Nothing is sealed by
   code.
5. **Report everything.** Every verdict goes into the draft, `against` and
   `inconclusive` as plainly as `pooling`. A rule changed after the run is a
   new freeze, with its reason, and the first result stays on record.

---

## What a result would mean for the paper

- **All four `pooling`:** the stock is visible in the data, and the draft's
  proposal becomes a finding about 2017 to 2025, still not a forecast.
- **Mixed:** the draft says which part of the stock shows up and which does
  not. P4 alone, for example, would say organizations persist without places
  or issues spreading.
- **`against`:** the bursts-and-pooling section is rewritten, and the paper's
  revision to Brinton loses its evidence. If P1 and P2 fall below 1, the data
  look more like his 1795 than like a pile.
