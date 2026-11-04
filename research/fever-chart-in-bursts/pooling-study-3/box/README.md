# Study 3's willow record

The [Study 3](../README.md) record, kept in the repo on purpose: the session
that runs the study, months from now, appends its verdicts to this same chain,
below Sean's wagers.

- Rows 1 to 4: Sean's wagers, written before the freeze and before the data
  existed (P1 0.35, P3 0.55, P4 0.55, P5 0.55).
- Verdict rows are appended by `score3.py --box`, unsealed. Code never seals.
- The key is not here and never will be. `kernel.json` names where Sean keeps
  it (`~/.willow-keys/pooling-box-3.key`); edit that line if it lives elsewhere.

Check it any time from a Willow clone: `python kernel.py verify --box <this folder>`.
