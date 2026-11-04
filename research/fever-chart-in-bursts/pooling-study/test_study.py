"""Tests for the pooling study: the rules on known worlds, and the reader.

    python -m unittest test_study.py

The power check is the point: on synthetic worlds whose answer is known,
score.py must call pooling `pooling` on every prediction, and must never call
reset or exhaustion `pooling` on any. Standard library only.
"""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import score
import synth


def verdicts(world: str, seed: int) -> list[str]:
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / f"{world}.csv"
        synth.main(["--world", world, "--to", str(p), "--seed", str(seed)])
        r = score.run(score.read([p]))
    return [v["verdict"] for k, v in r.items() if k.startswith("P")]


class PowerCheck(unittest.TestCase):
    def test_pooling_world_reads_as_pooling(self):
        for seed in (1, 2, 3):
            self.assertEqual(verdicts("pooling", seed), ["pooling"] * 4, seed)

    def test_no_other_world_reads_as_pooling(self):
        for world in ("reset", "exhaustion"):
            for seed in (1, 2, 3):
                self.assertNotIn("pooling", verdicts(world, seed), (world, seed))


class Reader(unittest.TestCase):
    def row(self, **kw):
        base = {"date": "2019-05-04", "fips_code": "1001", "online": "0", "type": "rally",
                "valence": "1", "issues": "racism", "size_cat": "2", "organizations": ""}
        base.update(kw)
        return score.normalize(base)

    def test_county_codes_get_their_leading_zero_back(self):
        self.assertEqual(self.row()["county"], "01001")
        self.assertEqual(self.row(fips_code="1001.0")["county"], "01001")

    def test_out_of_window_online_and_countyless_events_are_left_out(self):
        self.assertIsNone(self.row(date="2017-01-19"))
        self.assertIsNotNone(self.row(date="2017-01-20"))
        self.assertIsNotNone(self.row(date="2025-01-19"))
        self.assertIsNone(self.row(date="2025-01-20"))
        self.assertIsNone(self.row(online="1"))
        self.assertIsNone(self.row(fips_code=""))

    def test_strikes_are_left_out_but_not_the_climate_strikes(self):
        self.assertIsNone(self.row(type="strike"))
        self.assertIsNotNone(self.row(type="strike", issues="environment"))
        self.assertIsNone(self.row(type="strike", issues="environment", valence="0"))

    def test_hunger_strikes_stay_in(self):
        self.assertIsNotNone(self.row(type="hunger strike"))
        self.assertIsNotNone(self.row(type="demonstration; hunger-strike"))
        self.assertIsNone(self.row(type="strike; picket"))

    def test_placeholders_are_empty(self):
        self.assertEqual(self.row(organizations="NA")["orgs"], [])
        self.assertEqual(self.row(organizations="none")["orgs"], [])
        self.assertEqual(self.row(organizations="NA; Sunrise")["orgs"], ["sunrise"])

    def test_phase_column_names_all_read(self):
        self.assertEqual(self.row(issues="", issue_tags="guns; labor")["issues"], ["guns", "labor"])
        self.assertIsNone(self.row(type="", event_type="strike"))


class Freeze(unittest.TestCase):
    def test_every_frozen_file_is_as_frozen(self):
        here = Path(__file__).resolve().parent
        frozen = here / "FROZEN.json"
        if not frozen.exists():
            self.skipTest("not frozen yet")
        for name, digest in json.loads(frozen.read_text())["files"].items():
            got = hashlib.sha256((here / name).read_bytes()).hexdigest()
            self.assertEqual(got, digest, f"{name} changed since the freeze: a new freeze, with its reason")


if __name__ == "__main__":
    unittest.main()
