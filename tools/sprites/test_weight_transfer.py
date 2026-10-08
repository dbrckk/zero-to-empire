"""Pure tests for cyclic IK-supported gait loading (no sprite approvals)."""
from __future__ import annotations
import math
import unittest
import rigged_tech_walk_v2 as core
from weight_transfer import AMPLITUDES_PX, support_bias, stance_load, transfer_pose
from rigged_tech_actions_v3 import pose_for


class WeightTransferTests(unittest.TestCase):
    def test_load_is_smooth_periodic_and_bounded(self):
        for i in range(2000):
            t=i/2000
            self.assertAlmostEqual(support_bias(t),support_bias(t+1),places=8)
            self.assertLessEqual(abs(support_bias(t)),1+1e-9)
            self.assertTrue(0<=stance_load(t)<=1)
        for t in (0,.5,1):
            self.assertLess(abs(support_bias(t-1e-7)-support_bias(t+1e-7)),.0001)

    def test_foot_targets_and_grips_unchanged(self):
        for action in ('WALK','CARRY'):
            for i in range(384):
                t=i/384
                old=core.pose(t)
                new=pose_for(t,action)
                self.assertEqual(new['left'],old['left'])
                self.assertEqual(new['right'],old['right'])
                self.assertEqual(new['lockL'],old['lockL'])
                self.assertEqual(new['lockR'],old['lockR'])
                self.assertLessEqual(abs(new['weight_transfer_px']),AMPLITUDES_PX[action]+1e-6)
                self.assertAlmostEqual(new['root'][0]-old['root'][0],
                                       new['handL'][0]-old['handL'][0],places=8)
                if action=='CARRY':
                    x,y=new['root']
                    self.assertEqual(new['handL'],(x+29,y-55))
                    self.assertEqual(new['handR'],(x+103,y-55))
                for offset,side in ((-13,'left'),(13,'right')):
                    hip=(new['root'][0]+offset,new['root'][1])
                    self.assertLess(math.dist(hip,new[side]),193)

    def test_wrist_reach_and_cyclic_shift(self):
        for action in ('WALK','CARRY'):
            max_jump=0
            poses=[pose_for(i/192,action) for i in range(192)]
            for i,p in enumerate(poses):
                for hand,dx,dy in (('handL',-24,-86),('handR',23,-85)):
                    lean=p['torso_lean_rad']
                    x,y=p['root']
                    shoulder=(x+dx*math.cos(lean)-dy*math.sin(lean),
                              y+dx*math.sin(lean)+dy*math.cos(lean))
                    self.assertLessEqual(math.dist(shoulder,p[hand]),118)
                nxt=poses[(i+1)%len(poses)]
                jump=abs(p['weight_transfer_px']-nxt['weight_transfer_px'])
                max_jump=max(max_jump,jump)
            self.assertLess(max_jump,1.1)

    def test_deterministic_and_no_source_mutation(self):
        p=core.pose(.1875)
        original=p.copy()
        result=transfer_pose(p,.1875,'WALK')
        self.assertEqual(p,original)
        self.assertEqual(result,transfer_pose(p,.1875,'WALK'))
        self.assertNotEqual(result['root'],p['root'])
        for action in ('IDLE','WORK','REPAIR','CELEB'):
            with self.assertRaises(ValueError):transfer_pose(p,.1,action)


if __name__=='__main__':unittest.main()
