"""Repair animation should move the hands, not teleport the whole subject."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from character_repair_pose_plan import REPAIR_POSES, repair_strength


class RepairRigContinuityTests(unittest.TestCase):
    def test_full_ten_frame_cycle_retains_one_planted_foot_pivot(self):
        self.assertEqual(len(REPAIR_POSES), 10)
        self.assertEqual(len(set(REPAIR_POSES)), 10)
        for i, pose in enumerate(REPAIR_POSES):
            with self.subTest(frame=i):
                self.assertIn("same planted stance" if i not in (0, 9)
                              else ("BOTH FEET PLANTED" if i == 0 else "first medium crouch"),
                              pose)
                self.assertNotIn("half-kneel", pose.lower())
                self.assertNotIn("standing up", pose.lower() if i != 2 else "")
                self.assertNotIn("new repair", pose.lower())
        self.assertIn("seamless loop", REPAIR_POSES[-1])
        self.assertIn("fixed positions", REPAIR_POSES[0])

    def test_strengths_are_bounded_and_allow_articulation(self):
        values = []
        for i in range(10):
            for attempt in range(3):
                for mode in ("default", "framing", "single", "identity"):
                    strength = repair_strength(i, attempt, mode)
                    self.assertGreaterEqual(strength, .43)
                    self.assertLessEqual(strength, .63)
                    values.append(strength)
                    self.assertLessEqual(repair_strength(i, attempt, "identity"), strength)
        self.assertGreater(len(set(values)), 15)
        self.assertGreater(repair_strength(9, 2, "default"),
                           repair_strength(1, 0, "default"))

    def test_invalid_attempts_cannot_bypass_bounded_policy(self):
        for args in ((-1, 0, "default"), (10, 0, "default"),
                     (3, -1, "default"), (3, 3, "default"),
                     (3, 1, "approve")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                repair_strength(*args)

    def test_generator_uses_plan_and_preserves_original_qa_gates(self):
        generator = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text()
        mass = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text()
        kernel = Path("kaggle/github_mass_factory.py").read_text()
        self.assertIn("from character_repair_pose_plan import REPAIR_POSES, repair_strength", generator)
        self.assertIn("'REPAIR':list(REPAIR_POSES)", generator)
        self.assertIn("strength=repair_strength(fi,attempt,mode)", generator)
        self.assertIn("if min(ious)<.28:return False", generator)
        self.assertIn("sheet_qa(frames,i['action'])", generator)
        self.assertIn("action_qa(frames,i['action'])", generator)
        self.assertIn("visual_risk_decision(", generator)
        self.assertIn("character_repair_pose_plan.py", mass)
        self.assertIn("character_repair_pose_plan.py", kernel)
        self.assertNotIn("strict_status", Path("tools/sprites/character_repair_pose_plan.py").read_text())
        self.assertNotIn("app/src/main/res/", Path("tools/sprites/character_repair_pose_plan.py").read_text())


if __name__ == "__main__":
    unittest.main()
