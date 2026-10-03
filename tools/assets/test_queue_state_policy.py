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
                "generation_epoch": "identity-lock-v1.8",
                "epoch_attempts": 1,
            }
        ]}
        orchestrator.update_from_trigger(queue)
        asset = queue["assets"][0]
        self.assertEqual(asset["pipeline_status"], "DISPATCHED")
        self.assertEqual(asset["infra_failures"], 0)
        self.assertEqual(asset["attempts"], 1)
        self.assertIsNone(asset.get("last_run_id"))


if __name__ == "__main__":
    unittest.main()
