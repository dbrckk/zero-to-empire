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

    def test_operator_support_travel_has_constant_speed(self):
        # Dense phase sampling avoids judging only the eight rendered frames.
        for side in ("L", "R"):
            support = []
            for i in range(2000):
                phase = 2*math.pi*i/2000
                p = foot_pose(phase,side,"WALK",profile="op-walk")
                if p.planted:
                    support.append((p.cycle,p.ankle_x-p.hip_x,p.ankle_y))
            support.sort()
            self.assertGreater(len(support),500)
            self.assertTrue(all(abs(y-FLOOR_ANKLE_Y)<1e-8 for _,_,y in support))
            for (c0,x0,_),(c1,x1,_) in zip(support,support[1:]):
                speed=(x1-x0)/(c1-c0)
                self.assertAlmostEqual(speed,-38.0/.58,places=6)

    def test_operator_recovery_is_raised_and_loop_is_closed(self):
        for side in ("L","R"):
            poses=[foot_pose(2*math.pi*i/256,side,"WALK",profile="op-walk")
                   for i in range(256)]
            self.assertTrue(any(not p.planted and p.ankle_y < FLOOR_ANKLE_Y-19
                                for p in poses))
            start=foot_pose(0,side,"WALK",profile="op-walk")
            end=foot_pose(2*math.pi,side,"WALK",profile="op-walk")
            for name in ("ankle_x","ankle_y","knee_x","knee_y","boot_angle"):
                self.assertAlmostEqual(getattr(start,name),getattr(end,name),places=7)

    def test_loaded_carry_has_less_sway_than_unladen_walk(self):
        self.assertGreater(abs(torso_weight_shift(math.pi/2,"WALK")),
                           abs(torso_weight_shift(math.pi/2,"CARRY")))
        self.assertEqual(torso_weight_shift(math.pi/2,"IDLE"),0.0)

if __name__=="__main__":
    unittest.main()
