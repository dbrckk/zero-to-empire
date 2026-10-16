#!/usr/bin/env python3
"""Fast, dependency-free regression checks for asset production admission."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from character_acceptance_policy import motion_floor, visual_risk_decision
from asset_wave_orchestrator import (CHARACTER_GENERATION_EPOCH,
                                     CHARACTER_EPOCH_ATTEMPT_LIMIT,
                                     character_retry_available, mark_dispatch)


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

    def test_new_repair_algorithm_reopens_only_a_bounded_epoch(self):
        # The actual CHR-ENG-REPAIR master record had four rejected attempts
        # in v1.21; an explicit new repair rig can receive another bounded
        # attempt without deleting the old rejection/evidence history.
        candidate = {
            "id": "CHR-ENG-REPAIR", "lane": "kaggle-character-sheet",
            "strict_status": "NEEDS_REVIEW",
            "pipeline_status": "REJECTED_SEMANTIC",
            "last_generator": "kaggle-character-sheet",
            "last_error": "Kaggle candidate failed: silhouette jump=0.24",
            "generation_epoch": "production-first-v1.21-art-deferred",
            "epoch_attempts": 4, "attempts": 22, "infra_failures": 0,
        }
        self.assertEqual(CHARACTER_GENERATION_EPOCH,
                         "production-first-v1.22-planted-repair-poses")
        self.assertEqual(CHARACTER_EPOCH_ATTEMPT_LIMIT, 4)
        self.assertTrue(character_retry_available(candidate))
        dispatched = mark_dispatch({"assets": [candidate]},
                                   ["CHR-ENG-REPAIR"], "kaggle-character-sheet")
        self.assertEqual(dispatched, ["CHR-ENG-REPAIR"])
        self.assertEqual(candidate["generation_epoch"], CHARACTER_GENERATION_EPOCH)
        self.assertEqual(candidate["epoch_attempts"], 1)
        self.assertEqual(candidate["attempts"], 23)
        self.assertEqual(candidate["pipeline_status"], "DISPATCHED")
        self.assertEqual(candidate["strict_status"], "NEEDS_REVIEW")
        candidate["pipeline_status"] = "REJECTED_SEMANTIC"
        candidate["epoch_attempts"] = 4
        self.assertFalse(character_retry_available(candidate))
        # A produced candidate must not be regenerated just because
        # strict semantic review is still pending.
        candidate["pipeline_status"] = "AWAITING_REVIEW"
        candidate["epoch_attempts"] = 1
        self.assertFalse(character_retry_available(candidate))

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
