"""Exercise the real lightweight character action QA without loading Flux/GPU.

The production module imports PyTorch/diffusers at module load. Extract only
its pure PIL functions through Python AST, so these tests execute the exact
shipping action gate without requiring Kaggle or model downloads.
"""
from __future__ import annotations

import ast
import sys
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "sprites"))
from character_semantic_gate import idle_visual_activity, celebration_arm_reach_counts
from character_acceptance_policy import motion_floor

FUNCTIONS = {
    "alpha_iou",
    "lower_body_motion",
    "upper_body_transition_changes",
    "appearance_signature",
    "appearance_distance",
    "walk_consistency_qa",
    "action_qa",
}


def load_shipping_action_gate():
    source = (ROOT / "tools" / "sprites" / "kaggle_character_sheet_factory_v1.py").read_text(
        encoding="utf-8"
    )
    tree = ast.parse(source)
    selected = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name in FUNCTIONS
    ]
    if {node.name for node in selected} != FUNCTIONS:
        raise AssertionError("Production sprite action gate lost a required function")
    module = ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[]))
    namespace = {
        "Image": Image,
        "idle_visual_activity": idle_visual_activity,
        "celebration_arm_reach_counts": celebration_arm_reach_counts,
        "motion_floor": motion_floor,
        "production_first_enabled": lambda: False,  # Legacy strict regression suite
    }
    exec(compile(module, str(ROOT / "tools" / "sprites" / "kaggle_character_sheet_factory_v1.py"), "exec"), namespace)
    return namespace["action_qa"]


def worker():
    im = Image.new("RGBA", (256, 256))
    d = ImageDraw.Draw(im)
    d.ellipse((111, 24, 145, 63), fill=(201, 122, 69, 255))
    d.rectangle((99, 65, 158, 160), fill=(49, 87, 108, 255))
    d.line((103, 84, 82, 144), fill=(49, 87, 108, 255), width=13)
    d.line((152, 84, 176, 144), fill=(49, 87, 108, 255), width=13)
    d.line((111, 154, 100, 225), fill=(33, 55, 66, 255), width=16)
    d.line((145, 154, 158, 225), fill=(33, 55, 66, 255), width=16)
    return im


class ProductionActionQATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = staticmethod(load_shipping_action_gate())

    def test_exactly_frozen_idle_is_rejected(self):
        frozen = worker()
        passed, reason = self.gate([frozen.copy() for _ in range(6)], "IDLE")
        self.assertFalse(passed)
        self.assertIn("idle-frozen", reason)

    def test_subtle_eye_blink_idle_is_retained_for_manual_review(self):
        frames = []
        for index in range(6):
            frame = worker()
            if index in (1, 3, 5):
                ImageDraw.Draw(frame).rectangle((115, 37, 140, 44), fill=(18, 19, 23, 255))
            frames.append(frame)
        passed, reason = self.gate(frames, "IDLE")
        self.assertTrue(passed, reason)
        self.assertIn("pixel-activity=", reason)

    def test_stationary_carry_does_not_pass_for_a_walk_cycle(self):
        static = worker()
        passed, reason = self.gate([static.copy() for _ in range(8)], "CARRY")
        self.assertFalse(passed)
        self.assertIn("carry-too-static", reason)

    def test_single_last_frame_arm_jerk_is_not_celebration(self):
        neutral = worker()
        last = worker()
        ImageDraw.Draw(last).line((153, 88, 164, 5), fill=(49, 87, 108, 255), width=14)
        passed, reason = self.gate([neutral.copy() for _ in range(7)] + [last], "CELEB")
        self.assertFalse(passed)
        self.assertTrue(
            "celeb-too-static" in reason
            or "celeb-unreadable-gesture" in reason
            or "celeb-no-progressive-arm-raise" in reason,
            reason,
        )

    def test_static_walk_is_rejected(self):
        same = worker()
        passed, reason = self.gate([same.copy() for _ in range(8)], "WALK")
        self.assertFalse(passed)
        self.assertIn("walk-too-static", reason)


if __name__ == "__main__":
    unittest.main()
