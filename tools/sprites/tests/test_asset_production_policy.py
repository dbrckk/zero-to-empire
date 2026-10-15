#!/usr/bin/env python3
"""Fast, dependency-free regression checks for asset production admission."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from character_acceptance_policy import motion_floor, visual_risk_decision


class ProductionFirstTests(unittest.TestCase):
    def test_relaxed_motion_admits_previous_static_rejections(self):
        self.assertLess(motion_floor("WALK", production_first=True, lower_body=True), .087)
        self.assertLess(motion_floor("CARRY", production_first=True), .062)
        self.assertLess(motion_floor("WORK", production_first=True), .083)
        self.assertLess(motion_floor("CELEB", production_first=True), .081)

    def test_strict_floors_unchanged(self):
        self.assertEqual(motion_floor("WALK", production_first=False, lower_body=True), .22)
        self.assertEqual(motion_floor("CARRY", production_first=False), .12)

    def test_art_warnings_do_not_block_candidate(self):
        risk = {"risk_level": "BLOCKING", "flags": [
            "FACE_HEADGEAR_STRUCTURE_DRIFT_RISK", "BAKED_GROUND_SHADOW_RISK"]}
        blocked, warnings = visual_risk_decision(risk, production_first=True)
        self.assertEqual(blocked, [])
        self.assertEqual(len(warnings), 2)
        self.assertEqual(visual_risk_decision(risk, production_first=False), (risk["flags"], []))

    def test_structural_risks_remain_blocking(self):
        risk = {"risk_level": "BLOCKING", "flags": [
            "MULTIPLE_IDLE_HEADS_RISK", "FACE_HEADGEAR_STRUCTURE_DRIFT_RISK"]}
        self.assertEqual(
            visual_risk_decision(risk, production_first=True),
            (["MULTIPLE_IDLE_HEADS_RISK"], ["FACE_HEADGEAR_STRUCTURE_DRIFT_RISK"]))
        self.assertEqual(visual_risk_decision({"risk_level": "BLOCKING"}, production_first=True),
                         (["UNKNOWN_BLOCKING_RISK"], []))

    def test_unknown_risk_is_not_silently_waived(self):
        risk = {"risk_level": "BLOCKING", "flags": ["NEW_TECHNICAL_RISK"]}
        self.assertEqual(visual_risk_decision(risk, production_first=True)[0], ["NEW_TECHNICAL_RISK"])


if __name__ == "__main__":
    unittest.main()
