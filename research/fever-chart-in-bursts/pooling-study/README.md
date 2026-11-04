# Pooling: a pre-registered test on protest data

**Sean Campbell** · Study draft · November 2026 · **not frozen, not run**

Tests the [Fever Chart packet](../README.md)'s proposal that protest bursts
leave a stock behind, against the readings that they reset or exhaust, on the
Crowd Counting Consortium's US event data, 2017 to 2025. Four predictions,
each with its rule and its thresholds written down before any data row is
read.

| File | What |
|------|------|
| [PLAN.md](PLAN.md) | The pre-registration: data, window, rules, the four predictions, threats, the power check, the order from here |
| [sources.json](sources.json) | The three data files, pinned by Dataverse id, version and MD5 |
| [fetch.py](fetch.py) | Downloads and checks them; `--pin` adds their SHA-256s in the freeze commit |
| [score.py](score.py) | The rules as code; writes each verdict as a willow record row |
| [synth.py](synth.py) | Synthetic pooling, reset and exhaustion worlds, for the power check |
| [test_study.py](test_study.py) | The power check and the reader's tests: `python -m unittest test_study.py` |
| [stack.md](stack.md) | The willow stack to run over the box once the verdicts are in |

Standard library only, Python 3.9 or newer.

**Where it stands:** the power check passes (pooling worlds read as `pooling`
on every prediction, reset and exhaustion worlds on none). The plan is waiting
on Sean's edits and wagers, then the freeze.
