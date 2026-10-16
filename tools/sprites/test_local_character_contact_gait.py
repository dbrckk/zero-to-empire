"""Pixel-independent gait contract for locally authored WALK/CARRY candidates."""
from __future__ import annotations
import math
import unittest
from local_character_contact_gait import foot_pose,torso_weight_shift,STANCE_FRACTION,FLOOR_ANKLE_Y

class ContactGaitTests(unittest.TestCase):
    def test_stance_feet_are_anchored_vertically_even_while_torso_bobs(self):
        for action in ("WALK","CARRY"):
            for side in ("L","R"):
                for i in range(80):
                    phase=2*math.pi*i/80
                    bounce=1.4*(1-math.cos(phase*2))
                    leg=foot_pose(phase,side,action,bounce)
                    if leg.planted:
                        self.assertAlmostEqual(leg.ankle_y,FLOOR_ANKLE_Y,places=6)

    def test_exact_half_cycle_leg_antiphase(self):
        for action in ("WALK","CARRY"):
            for i in range(24):
                phase=i*2*math.pi/24
                l=foot_pose(phase,"L",action)
                r=foot_pose(phase+math.pi,"R",action)
                self.assertAlmostEqual(l.cycle,r.cycle,places=8)
                self.assertAlmostEqual(l.ankle_x-l.hip_x,r.ankle_x-r.hip_x,places=8)
                self.assertAlmostEqual(l.ankle_y,r.ankle_y,places=8)

    def test_swing_clears_ground_without_crossed_legs(self):
        for action in ("WALK","CARRY"):
            raised=0
            for i in range(48):
                phase=2*math.pi*i/48
                left=foot_pose(phase,"L",action)
                right=foot_pose(phase,"R",action)
                self.assertLess(left.ankle_x,right.ankle_x)
                self.assertGreater(left.ankle_y,197)
                self.assertGreater(right.ankle_y,197)
                self.assertLess(max(left.ankle_x,right.ankle_x),179)
                raised+=int(not left.planted)+int(not right.planted)
            self.assertGreater(raised,20)

    def test_swing_knees_turn_forward_instead_of_overshooting_silhouette(self):
        for action in ("WALK","CARRY"):
            for phase in (math.pi/2,3*math.pi/2):
                for side in ("L","R"):
                    pose=foot_pose(phase,side,action)
                    if not pose.planted:
                        # The lifted knee should remain within one compact
                        # 3/4-view shin offset, not splay outside the worker.
                        self.assertLess(abs(pose.knee_x-pose.ankle_x),20)
                        self.assertLess(pose.ankle_y,FLOOR_ANKLE_Y)

    def test_loop_is_periodic_without_coordinate_jumps(self):
        for action in ("WALK","CARRY"):
            for side in ("L","R"):
                first=foot_pose(0,side,action)
                last=foot_pose(2*math.pi,side,action)
                for coord in ("knee_x","knee_y","ankle_x","ankle_y","boot_angle"):
                    self.assertAlmostEqual(getattr(first,coord),getattr(last,coord),places=7)

    def test_engineer_gait_exaggerates_readable_steps_without_crossed_legs(self):
        ankles = {"L": [], "R": []}
        lift = {"L": [], "R": []}
        stance_counts = {"L": 0, "R": 0}
        for index in range(8):
            phase = 2 * math.pi * index / 8
            poses = {}
            for side in ("L", "R"):
                pose = foot_pose(phase, side, "WALK", profile="eng-walk")
                poses[side] = pose
                ankles[side].append(pose.ankle_x)
                lift[side].append(FLOOR_ANKLE_Y - pose.ankle_y)
                stance_counts[side] += int(pose.planted)
                if pose.planted:
                    self.assertEqual(pose.ankle_y, FLOOR_ANKLE_Y)
            self.assertLess(poses["L"].ankle_x, poses["R"].ankle_x)
        for side in ("L", "R"):
            self.assertGreater(max(ankles[side]) - min(ankles[side]), 36)
            self.assertGreater(max(lift[side]), 20)
            self.assertGreaterEqual(stance_counts[side], 4)
            start = foot_pose(0, side, "WALK", profile="eng-walk")
            end = foot_pose(2 * math.pi, side, "WALK", profile="eng-walk")
            self.assertAlmostEqual(start.ankle_x, end.ankle_x)
            self.assertAlmostEqual(start.ankle_y, end.ankle_y)
        with self.assertRaises(ValueError):
            foot_pose(0, "L", "CARRY", profile="eng-walk")
        self.assertEqual(foot_pose(0,"L","CARRY").hip_x,106)

    def test_loaded_carry_has_less_sway_than_unladen_walk(self):
        self.assertGreater(abs(torso_weight_shift(math.pi/2,"WALK")),
                           abs(torso_weight_shift(math.pi/2,"CARRY")))
        self.assertEqual(torso_weight_shift(math.pi/2,"IDLE"),0.0)

if __name__=="__main__":
    unittest.main()
