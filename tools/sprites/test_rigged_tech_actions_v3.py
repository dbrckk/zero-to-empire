"""Regression checks for unattended six-animation TECH rig and non-bypassable review."""
from __future__ import annotations

import hashlib
import json
import math
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from rigged_tech_actions_v3 import (
    ACTIONS, GROUND, build_action, draw_frame, pose_for,
)
import rigged_tech_walk_v2 as core

KIT = Path(__file__).with_name("skin-tech-v1.webp")


class MultiActionGeometryTests(unittest.TestCase):
    def test_each_action_is_strictly_periodic(self):
        for action in ACTIONS:
            for phase in (0, .0125, .125, .35, .5, .625, .97):
                a = pose_for(phase, action)
                b = pose_for(phase + 1, action)
                for joint in ("root", "left", "right", "handL", "handR"):
                    for av, bv in zip(a[joint], b[joint]):
                        self.assertAlmostEqual(av, bv, places=7)
                for key in ("lockL", "lockR"):
                    self.assertEqual(a[key], b[key])

    def test_stationary_actions_keep_feet_grounded_and_hands_reachable(self):
        for action in ("IDLE", "WORK", "REPAIR", "CELEB"):
            for i in range(48):
                p = pose_for(i / 48, action)
                self.assertTrue(p["lockL"] and p["lockR"])
                self.assertEqual(p["left"][1], GROUND)
                self.assertEqual(p["right"][1], GROUND)
                x, y = p["root"]
                self.assertLess(math.dist((x - 24, y - 86), p["handL"]), 118)
                self.assertLess(math.dist((x + 23, y - 85), p["handR"]), 118)

    def test_carry_grip_is_fixed_relative_to_crate(self):
        for i in range(48):
            p = pose_for(i / 48, "CARRY")
            x, y = p["root"]
            self.assertEqual(p["handL"], (x + 29, y - 55))
            self.assertEqual(p["handR"], (x + 103, y - 55))

    def test_action_motion_is_not_identical_across_frames(self):
        for action in ("WORK", "REPAIR", "CELEB"):
            hand = [pose_for(i / 24, action)["handR"] for i in range(24)]
            self.assertGreater(max(math.dist(hand[0], q) for q in hand), 5)

    def test_invalid_action_and_impossible_settings_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(ValueError):
                build_action(KIT, root / "bad", "ATTACK")
            self.assertFalse((root / "bad").exists())
            with self.assertRaises(ValueError):
                build_action(KIT, root / "bad2", "WALK", 7, 12)
            self.assertFalse((root / "bad2").exists())


class MultiActionRendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kit = core.load_kit(KIT)

    def test_deterministic_unique_per_action(self):
        for action in ACTIONS:
            first, _, _ = draw_frame(action, .125, self.kit)
            second, _, _ = draw_frame(action, .125, self.kit)
            self.assertEqual(
                hashlib.sha256(first.tobytes()).digest(),
                hashlib.sha256(second.tobytes()).digest())
            self.assertEqual(first.mode, "RGBA")
            self.assertEqual(first.getpixel((0, 0))[3], 0)

    def test_each_export_remains_a_review_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            for action in ACTIONS:
                with self.subTest(action=action):
                    out = Path(tmp) / action
                    manifest, bundle = build_action(KIT, out, action, frames=8, fps=8)
                    qa = manifest["qa"]
                    self.assertTrue(qa["technical_pass"], qa)
                    self.assertTrue(qa["action_kinematic_pass"], qa)
                    self.assertEqual(manifest["asset_id"], f"CHR-TECH-{action}")
                    self.assertEqual(manifest["strict_status"], "NEEDS_REVIEW")
                    self.assertTrue(manifest["human_visual_review_required"])
                    self.assertFalse(qa["visual_review_pass"])
                    self.assertFalse(qa["semantic_review_pass"])
                    self.assertEqual(len(qa["hand_reach_violations"]), 0)
                    self.assertTrue(bundle.is_file())
                    self.assertTrue((out / "REVIEW_REQUIRED.txt").is_file())
                    self.assertTrue((out / "contact-game-scale.jpg").is_file())
                    self.assertEqual(len(list((out / "frames").glob("*.png"))), 8)
                    events = json.loads((out / "animation-events.json").read_text())
                    self.assertEqual(len(events), 8)
                    if action not in ("WALK", "CARRY"):
                        self.assertTrue(all(e["footstep"] is None for e in events))
                    else:
                        self.assertEqual(events[0]["footstep"], "right")
                        self.assertEqual(events[4]["footstep"], "left")
                    with Image.open(out / "atlas.png") as atlas:
                        self.assertEqual(atlas.size, (3072, 1024))
                        self.assertEqual(atlas.mode, "RGBA")


if __name__ == "__main__":
    unittest.main()
