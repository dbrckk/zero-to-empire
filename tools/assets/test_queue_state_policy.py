#!/usr/bin/env python3
"""Regression checks for canonical autofactory queue state preservation."""
from __future__ import annotations

import importlib.util
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/sprites/asset_queue_utils.py"
spec = importlib.util.spec_from_file_location("asset_queue_utils", MODULE_PATH)
queue_utils = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(queue_utils)
sys.path.insert(0, str(ROOT / "tools/sprites"))


class QueueStatePolicyTests(unittest.TestCase):
    def test_critical_review_and_retry_state_is_persisted(self) -> None:
        required = {
            "strict_status",
            "pipeline_status",
            "attempts",
            "last_run_id",
            "last_generator",
            "last_error",
            "review_reason",
            "generation_epoch",
            "epoch_attempts",
            "infra_failures",
            "dispatch_token",
        }
        self.assertTrue(required.issubset(set(queue_utils.PERSISTED_ASSET_STATE_FIELDS)))

    def test_persisted_fields_are_unique(self) -> None:
        fields = queue_utils.PERSISTED_ASSET_STATE_FIELDS
        self.assertEqual(len(fields), len(set(fields)))


class DispatchCorrelationTests(unittest.TestCase):
    def _load_orchestrator(self, token: str):
        os.environ["AUTOF_TRIGGER_WORKFLOW"] = "Kaggle Mass Sprite Factory"
        os.environ["AUTOF_TRIGGER_CONCLUSION"] = "failure"
        os.environ["AUTOF_TRIGGER_RUN_ID"] = "999"
        os.environ["AUTOF_TRIGGER_DISPATCH_TOKEN"] = token
        spec = importlib.util.spec_from_file_location("asset_wave_orchestrator_test", ROOT / "tools/sprites/asset_wave_orchestrator.py")
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        return module

    def test_stale_callback_cannot_mutate_newer_dispatch(self) -> None:
        orchestrator = self._load_orchestrator("wave-A")
        queue = {"assets": [
            {
                "id": "CHR-ENG-REPAIR",
                "pipeline_status": "DISPATCHED",
                "last_generator": "kaggle-character-sheet",
                "dispatch_token": "wave-B",
                "infra_failures": 0,
                "attempts": 1,
                "generation_epoch": "identity-lock-v1.12",
                "epoch_attempts": 1,
            }
        ]}
        orchestrator.update_from_trigger(queue)
        asset = queue["assets"][0]
        self.assertEqual(asset["pipeline_status"], "DISPATCHED")
        self.assertEqual(asset["infra_failures"], 0)
        self.assertEqual(asset["attempts"], 1)
        self.assertIsNone(asset.get("last_run_id"))

    def test_current_epoch_attempt_limit_takes_precedence_over_legacy_total_attempts(self) -> None:
        orchestrator = self._load_orchestrator("")
        asset = {
            "id": "CHR-OP-WALK",
            "pipeline_status": "PENDING_KAGGLE",
            "last_generator": "kaggle-character-sheet",
            "infra_failures": 0,
            "attempts": 1,
            "generation_epoch": orchestrator.CHARACTER_GENERATION_EPOCH,
            "epoch_attempts": orchestrator.CHARACTER_EPOCH_ATTEMPT_LIMIT,
        }
        self.assertFalse(orchestrator.character_retry_available(asset))

    def test_current_epoch_still_allows_retry_below_epoch_limit(self) -> None:
        orchestrator = self._load_orchestrator("")
        asset = {
            "id": "CHR-OP-WALK",
            "pipeline_status": "PENDING_KAGGLE",
            "last_generator": "kaggle-character-sheet",
            "infra_failures": 0,
            "attempts": 99,
            "generation_epoch": orchestrator.CHARACTER_GENERATION_EPOCH,
            "epoch_attempts": orchestrator.CHARACTER_EPOCH_ATTEMPT_LIMIT - 1,
        }
        self.assertTrue(orchestrator.character_retry_available(asset))

    def test_character_batch_size_supports_multi_role_burst(self) -> None:
        orchestrator = self._load_orchestrator("")
        self.assertEqual(orchestrator.CHARACTER_BATCH_SIZE, 12)

    def test_character_epoch_allows_three_informed_attempts(self) -> None:
        orchestrator = self._load_orchestrator("")
        self.assertEqual(orchestrator.CHARACTER_EPOCH_ATTEMPT_LIMIT, 3)

    def test_character_epoch_is_v117_articulated_border_fix(self) -> None:
        orchestrator = self._load_orchestrator("")
        self.assertEqual(orchestrator.CHARACTER_GENERATION_EPOCH,
                         "identity-lock-v1.17-articulated-border-fix")

    def test_new_epoch_reopens_semantic_reject_even_with_high_legacy_attempts(self) -> None:
        orchestrator = self._load_orchestrator("")
        asset = {
            "pipeline_status": "REJECTED_SEMANTIC",
            "generation_epoch": "identity-lock-v1.9",
            "epoch_attempts": 3,
            "attempts": 99,
            "infra_failures": 0,
            "last_error": "Semantic rejection: action unreadable.",
        }
        self.assertTrue(orchestrator.character_retry_available(asset))

    def test_current_epoch_semantic_retry_ignores_legacy_infra_failures(self) -> None:
        orchestrator = self._load_orchestrator("")
        asset = {
            "pipeline_status": "REJECTED_SEMANTIC",
            "generation_epoch": orchestrator.CHARACTER_GENERATION_EPOCH,
            "epoch_attempts": 0,
            "attempts": 8,
            "infra_failures": 3,
            "last_error": "Semantic rejection: unreadable repair action.",
        }
        self.assertTrue(orchestrator.character_retry_available(asset))

    def test_current_infra_failure_limit_still_blocks_real_infra_error(self) -> None:
        orchestrator = self._load_orchestrator("")
        asset = {
            "pipeline_status": "PENDING_KAGGLE",
            "generation_epoch": orchestrator.CHARACTER_GENERATION_EPOCH,
            "epoch_attempts": 0,
            "attempts": 8,
            "infra_failures": 3,
            "last_error": "Kaggle producer: failure; infrastructure retry 3/3 scheduled",
        }
        self.assertFalse(orchestrator.character_retry_available(asset))

    def test_character_sync_normalizes_rejected_to_semantic_rejection(self) -> None:
        text = (ROOT / "tools/sprites/asset_queue_utils.py").read_text(encoding="utf-8")
        self.assertIn('normalized_status = "REJECTED_SEMANTIC"', text)
        self.assertIn('status in {"REJECTED", "REJECTED_SEMANTIC"}', text)

    def test_main_applies_trigger_before_controlled_queue_sync(self) -> None:
        text = (ROOT / "tools/sprites/asset_wave_orchestrator.py").read_text(encoding="utf-8")
        trigger = text.index("    update_from_trigger(queue)")
        sync = text.index("    sync_controlled_queues(queue)", trigger)
        self.assertLess(trigger, sync)

    def test_character_decision_allows_three_roles_in_one_burst(self) -> None:
        text = (ROOT / "tools/sprites/asset_wave_orchestrator.py").read_text(encoding="utf-8")
        self.assertIn("burst_groups = ordered[:3]", text)

    def test_character_burst_builder_exists_and_caps_at_batch_size(self) -> None:
        orchestrator = self._load_orchestrator("")
        self.assertTrue(hasattr(orchestrator, "prepare_character_burst"))
        self.assertEqual(orchestrator.CHARACTER_BATCH_SIZE, 12)

    def test_successful_character_outcomes_mirror_into_master(self) -> None:
        orchestrator = self._load_orchestrator("")
        queue = {"assets": [
            {"id": "CHR-OP-IDLE", "pipeline_status": "DISPATCHED", "last_generator": "kaggle-character-sheet"},
            {"id": "CHR-OP-WALK", "pipeline_status": "DISPATCHED", "last_generator": "kaggle-character-sheet"},
        ]}
        active = queue["assets"]
        original = orchestrator.load_json
        try:
            orchestrator.load_json = lambda path, default=None: {
                "targets": [
                    {"id": "CHR-OP-IDLE", "status": "AWAITING_REVIEW"},
                    {"id": "CHR-OP-WALK", "status": "REJECTED", "review_reason": "walk-too-static"},
                ]
            }
            orchestrator.mirror_character_outcomes_from_controlled(queue, active)
        finally:
            orchestrator.load_json = original
        self.assertEqual(queue["assets"][0]["pipeline_status"], "AWAITING_REVIEW")
        self.assertEqual(queue["assets"][1]["pipeline_status"], "REJECTED_SEMANTIC")
        self.assertIn("walk-too-static", queue["assets"][1]["review_reason"])


if __name__ == "__main__":
    unittest.main()
