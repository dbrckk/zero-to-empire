#!/usr/bin/env python3
"""Regression checks for canonical autofactory queue state preservation."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/sprites/asset_queue_utils.py"
spec = importlib.util.spec_from_file_location("asset_queue_utils", MODULE_PATH)
queue_utils = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(queue_utils)


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
        }
        self.assertTrue(required.issubset(set(queue_utils.PERSISTED_ASSET_STATE_FIELDS)))

    def test_persisted_fields_are_unique(self) -> None:
        fields = queue_utils.PERSISTED_ASSET_STATE_FIELDS
        self.assertEqual(len(fields), len(set(fields)))


if __name__ == "__main__":
    unittest.main()
