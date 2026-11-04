# Pooling: a pre-registered test on protest data

**Sean Campbell** · Pre-registered study · November 2026 · **frozen, not run**

Tests the [Fever Chart packet](../README.md)'s proposal that protest bursts
leave a stock behind, against the readings that they reset or exhaust, on the
Crowd Counting Consortium's US event data across two full presidential
terms, January 2017 to January 2025. Four predictions,
each with its rule and its thresholds written down before any data row is
read.

| File | What |
|------|------|
| [PLAN.md](PLAN.md) | The pre-registration: data, window, rules, the four predictions, threats, the power check, the order from here |
| [sources.json](sources.json) | The three data files, pinned by Dataverse id, version and MD5 |
| [fetch.py](fetch.py) | Downloads and checks them; `--pin` adds their SHA-256s in the freeze commit |
| [score.py](score.py) | The rules as code; writes each verdict as a willow record row |
| [synth.py](synth.py) | Synthetic pooling, reset and exhaustion worlds, for the power check |
| [test_study.py](test_study.py) | The power check, the reader's tests, and the freeze check: `python -m unittest test_study.py` |
| [wiring.py](wiring.py) | The dry run: does the reader read the real files at all (counts only) |
| `FROZEN.json` | The SHA-256 of every file here at the freeze |
| [stack.md](stack.md) | The willow stack to run over the box once the verdicts are in |

Standard library only, Python 3.9 or newer.

**Where it stands:** frozen on 2026-11-04 with Sean's wagers on record. The
power check passes (pooling worlds read as `pooling` on every prediction,
reset and exhaustion worlds on none), and the dry run's two reader bugs were
fixed before the freeze. Next is the one run.
