# Exploratory: a seasonal baseline for the rising floor

**Not a test, not frozen.** Written after both studies, and run on months both
had already scored, to choose Study 3's instrument knowing how it behaves.
Nothing here is a finding, and nothing here is evidence for or against
pooling.

[seasonal.py](seasonal.py) measures each burst against the same calendar
months a year earlier: the 4 usable quiet months after the burst over their
year-earlier months, divided by the same for the 4 before. Season and steady
growth in coverage cancel, and a ramp before the burst no longer sets the bar
for the months after, which is what broke Study 2's trend line.

---

## On the synthetic worlds

Seeds 1 to 5, "clean" windows (no other burst inside a burst's span):

| World | All events | 100 or more |
|---|---|---|
| pooling | 1.09 to 1.13 | 1.07 to 1.17 |
| reset | 1.00 to 1.04 | 1.00 to 1.05 |
| exhaustion | 0.78 to 0.88 | 0.78 to 0.90 |

The three worlds separate, with no overlap, which neither earlier P1 managed
on short windows.

---

## On the real months already seen

[seasonal-result.json](seasonal-result.json):

| Variant | All events | 100 or more | Bursts measured |
|---|---|---|---|
| Clean windows | 0.94 | 1.18 | 4 of 17 |
| Any span | 1.21 | 1.31 | 8 of 17 |

**What it shows:**

- **Clean windows are rare.** Bursts come so often (17 in 111 months) that
  only 4 had 4 usable quiet months on each side without another burst in
  between. A 12-month held-out window could easily have none.
- **Without the clean rule, 2020 takes over.** The "any span" figures are
  driven by September and December 2019 (1.85 and 3.27), whose after-windows
  run past the lockdown into summer 2020. That rule should not be used.
- **The three clean Octobers agree, mildly.** After October 2021, 2022 and
  2023, quiet months ran 7 to 10 percent above the year before (all events).
- **After the 2018 midterm, the floor fell.** The quiet months after November
  2018 ran at 0.63 of the year before: a post-election lull. One case, already
  seen, but it bears directly on the November 2026 midterm, which Study 3's
  window includes.

---

## What this means for Study 3

- Use the seasonal measure, with clean windows, for P1.
- Give the held-out window room: 18 months, not 12.
- Ask the midterm question directly, since the paper calls tonight's election
  a test of the pressure valve, and since the one seen precedent is a lull.
