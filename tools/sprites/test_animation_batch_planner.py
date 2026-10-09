"""Contract tests for pending animation planning without GPU or queue mutation."""
from __future__ import annotations

import hashlib
import json
import unittest

from animation_batch_planner import (
    ROOT, MASTER, MANIFEST, CHR_FRAMES, frame_contract, items, task_for,
)
from process_final_sprites import CHR_EXPECTED_FRAMES


class AnimationBatchPlannerTests(unittest.TestCase):
    def test_frame_contract_matches_existing_android_runtime(self):
        self.assertEqual({k.lower(): v for k,v in CHR_FRAMES.items()}, CHR_EXPECTED_FRAMES)
        self.assertEqual(frame_contract("CHR-TECH-WALK"), (8,256,4,2,"feet-center"))
        self.assertEqual(frame_contract("CHR-TECH-WORK"), (10,256,4,3,"feet-center"))
        self.assertEqual(frame_contract("CHR-TECH-CELEB"), (8,256,4,2,"feet-center"))
        self.assertEqual(frame_contract("MCH-00"), (8,512,4,2,"machine-base-center"))

    def test_promotion_is_never_inferred_from_existing_webp(self):
        for asset in items("ALL"):
            self.assertFalse(asset["semantic_approved"])
            self.assertFalse(asset["automatic_promotion_permitted"])
            self.assertNotEqual(asset["manifest_status"],"DONE")
            self.assertGreater(asset["frames"],0)
            self.assertEqual(asset["sheet_width"],4*asset["cell"])

    def test_exactly_pending_master_character_ids_are_planned(self):
        queue=json.loads(MASTER.read_text(encoding="utf-8"))
        expected={
            a["id"] for a in queue["assets"]
            if a["id"].startswith(("CHR-","MCH-")) and a["strict_status"]!="DONE"
        }
        plans=items("ALL")
        self.assertEqual({a["id"] for a in plans},expected)
        self.assertEqual([a for a in plans if a["family"]=="MCH"], items("MCH"))
        self.assertEqual([a for a in plans if a["family"]=="CHR"], items("CHR"))
        self.assertEqual(len(plans),len(expected))

    def test_invalid_candidates_are_repaired_before_review(self):
        self.assertEqual(task_for("BLOCKED"),"regenerate")
        self.assertEqual(task_for("REJECTED_SEMANTIC"),"regenerate")
        self.assertEqual(task_for("AWAITING_REVIEW"),"semantic-review")
        self.assertEqual(task_for("DONE"),"generate")
        ranks={"regenerate":0,"semantic-review":1,"generate":2}
        plans=items("ALL")
        self.assertEqual([ranks[a["task"]] for a in plans],sorted(ranks[a["task"]] for a in plans))

    def test_plan_is_read_only(self):
        files=[MASTER,MANIFEST]
        before=[hashlib.sha256(p.read_bytes()).hexdigest() for p in files]
        items("ALL")
        after=[hashlib.sha256(p.read_bytes()).hexdigest() for p in files]
        self.assertEqual(before,after)


if __name__=="__main__":
    unittest.main()
