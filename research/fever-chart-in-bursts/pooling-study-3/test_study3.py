"""Tests for Study 3: its window, its data rule, its verdict gate, the freeze.

    python -m unittest test_study3.py

The power check itself is slow (every P1 and P5 verdict rests on 200
resamples), so it is run once by hand and kept in power-check.txt; PLAN.md
reports it. These tests hold the rules that make the study what it says.
"""
import hashlib
import json
import unittest
from pathlib import Path

import fetch3
import score3


class Window(unittest.TestCase):
    def test_each_part_has_its_own_end(self):
        score3.set_window("valve")
        self.assertEqual(score3.score2.LAST_DAY, "2027-03-31")
        score3.set_window("main")
        self.assertEqual(score3.score2.LAST_DAY, "2027-09-30")
        self.assertEqual(score3.score2.label(score3.score2.H0), "2026-04")

    def test_data_must_reach_two_months_past_each_window(self):
        self.assertEqual(fetch3.NEED, {"valve": "2027-05-31", "main": "2027-11-30"})
        self.assertEqual(fetch3.FROZEN_ON, "2026-11-04")


class Gate(unittest.TestCase):
    def test_pooling_needs_the_resamples_to_agree(self):
        agree = [[1.2, 1.2]] * 100
        split = [[1.2, 1.2]] * 90 + [[0.9, 0.9]] * 10
        self.assertEqual(score3.gated([1.2, 1.2], agree, (1.05, 0.97), "against")[0], "pooling")
        self.assertEqual(score3.gated([1.2, 1.2], split, (1.05, 0.97), "against")[0], "inconclusive")

    def test_the_low_verdict_needs_them_too(self):
        low = [[0.8, 0.8]] * 100
        self.assertEqual(score3.gated([0.8, 0.8], low, (1.1, 0.9), "drop")[0], "drop")
        self.assertEqual(score3.gated([0.8, None], low, (1.1, 0.9), "drop")[0], "inconclusive")


class Freeze(unittest.TestCase):
    def test_every_frozen_file_is_as_frozen(self):
        here = Path(__file__).resolve().parent
        frozen = here / "FROZEN.json"
        if not frozen.exists():
            self.skipTest("not frozen yet")
        for name, digest in json.loads(frozen.read_text())["files"].items():
            got = hashlib.sha256((here / name).resolve().read_bytes()).hexdigest()
            self.assertEqual(got, digest, f"{name} changed since the freeze: a new freeze, with its reason")


if __name__ == "__main__":
    unittest.main()
