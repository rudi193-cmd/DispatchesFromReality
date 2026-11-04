# Study 3: pooling on months not yet collected

**Sean Campbell** · Study draft · November 2026 · **not frozen, not run**

Frozen before its data exist: held-out months April 2026 to September 2027,
plus the November 2026 midterm as a test of the pressure valve. The data are
chosen by a rule, the first CCC release that covers each window.

| File | What |
|------|------|
| [PLAN.md](PLAN.md) | The predictions, the data rule, the power check, wagers |
| [score3.py](score3.py) | The rules as code; reuses Study 2's reader |
| [fetch3.py](fetch3.py) | Finds and checks the first qualifying release |
| [synth3.py](synth3.py) | Synthetic worlds through September 2027 |
| [test_study3.py](test_study3.py) | The window, the data rule, the verdict gate, the freeze |
| [power-check.txt](power-check.txt) | The power check's raw verdicts |
