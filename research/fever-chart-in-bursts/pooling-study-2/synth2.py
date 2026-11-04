#!/usr/bin/env python3
"""Study 1's synthetic worlds, run on through March 2026, for Study 2's power check.

    python synth2.py --world pooling|reset|exhaustion --to FILE.csv [--seed N]

Same counties, coverage and mechanisms as ../pooling-study/synth.py (imported,
not copied), over 111 months instead of 97, with two bursts in the held-out
months (April and September 2025) besides Study 1's five. Standard library only.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pooling-study"))
import synth  # noqa: E402

synth.MONTHS = 111  # January 2017 to March 2026
synth.BURSTS = {**synth.BURSTS, 99: "democracy", 104: "immigration"}

if __name__ == "__main__":
    raise SystemExit(synth.main(sys.argv[1:]))
