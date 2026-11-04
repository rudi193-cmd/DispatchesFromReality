"""Tests for Study 2: the power check on extended worlds, the reader, the freeze.

    python -m unittest test_study2.py

Study 2 is short (19 held-out months, two synthetic bursts), so the power
check asks less than Study 1's: no false pooling in reset or exhaustion
worlds on any prediction, and no `against` in the pooling world. How often
the pooling world reaches `pooling` is reported in PLAN.md, not required.
"""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import score2
import synth2


def verdicts(world: str, seed: int) -> list[str]:
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / f"{world}.csv"
        synth2.synth.main(["--world", world, "--to", str(p), "--seed", str(seed)])
        r = score2.run(score2.read([p]))
    return [v["verdict"] for k, v in r.items() if k.startswith("P")]


class PowerCheck(unittest.TestCase):
    def test_pooling_world_is_never_against(self):
        for seed in (1, 2, 3):
            self.assertNotIn("against", verdicts("pooling", seed), seed)

    def test_no_other_world_reads_as_pooling(self):
        for world in ("reset", "exhaustion"):
            for seed in (1, 2, 3):
                self.assertNotIn("pooling", verdicts(world, seed), (world, seed))


class Reader(unittest.TestCase):
    def row(self, **kw):
        base = {"date": "2025-05-04", "fips_code": "1001", "online": "0", "type": "rally",
                "valence": "1", "issues": "democracy", "size_cat": "2", "organizations": ""}
        base.update(kw)
        return score2.normalize(base)

    def test_window_runs_from_study_one_start_to_march_2026(self):
        self.assertIsNone(self.row(date="2017-01-19"))
        self.assertIsNotNone(self.row(date="2017-01-20"))
        self.assertIsNotNone(self.row(date="2026-03-31"))
        self.assertIsNone(self.row(date="2026-04-01"))

    def test_organization_names_are_loosened(self):
        self.assertEqual(self.row(organizations="The Sunrise Movement")["orgs"], ["sunrise movement"])
        self.assertEqual(self.row(organizations="Women's March; NA")["orgs"], ["women s march"])
        self.assertEqual(score2.org_name("Jobs & Justice"), score2.org_name("jobs and justice"))

    def test_study_one_reader_rules_hold(self):
        self.assertIsNone(self.row(type="strike; picket"))
        self.assertIsNotNone(self.row(type="hunger strike"))
        self.assertIsNone(self.row(online="1"))
        self.assertEqual(self.row(fips_code="1001.0")["county"], "01001")


class Freeze(unittest.TestCase):
    def test_every_frozen_file_is_as_frozen(self):
        here = Path(__file__).resolve().parent
        frozen = here / "FROZEN.json"
        if not frozen.exists():
            self.skipTest("not frozen yet")
        for name, digest in json.loads(frozen.read_text())["files"].items():
            path = (here / name).resolve()
            got = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(got, digest, f"{name} changed since the freeze: a new freeze, with its reason")


if __name__ == "__main__":
    unittest.main()
