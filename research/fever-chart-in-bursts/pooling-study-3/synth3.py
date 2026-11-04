#!/usr/bin/env python3
"""Study 1's synthetic worlds, run on through September 2027, for Study 3's power check.

    python synth3.py --world pooling|reset|exhaustion --to FILE.csv [--seed N]

Same counties, coverage and mechanisms as ../pooling-study/synth.py (imported,
not copied), over 129 months, with Study 2's two 2025 bursts and two in Study
3's held-out months: November 2026 and May 2027. Standard library only.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pooling-study"))
import synth  # noqa: E402

synth.MONTHS = 129  # January 2017 to September 2027
synth.BURSTS = {**synth.BURSTS, 99: "democracy", 104: "immigration",
                118: "democracy", 124: "immigration"}

if __name__ == "__main__":
    raise SystemExit(synth.main(sys.argv[1:]))
