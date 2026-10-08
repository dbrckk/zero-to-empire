"""Unattended walk generator regression tests. Run: python -m unittest ..."""
import json
import math
import tempfile
import unittest
from pathlib import Path
from PIL import Image

from autonomous_walk import WalkSettings, foot_local, foot_roll, pose, verify_motion, export, GROUND


class WalkGeometryTests(unittest.TestCase):
    def test_cyclic_pose_and_left_right_symmetry(self):
        cfg = WalkSettings()
        for phase in (0,.05,.13,.27,.5,.61,.73,.99):
            a=pose(phase,cfg)
            b=pose(phase+1,cfg)
            for joint in ('root','left','right','handL','handR'):
                self.assertAlmostEqual(a[joint]['x'],b[joint]['x'],places=7)
                self.assertAlmostEqual(a[joint]['y'],b[joint]['y'],places=7)
            l=foot_local(phase+.5,cfg)
            r=foot_local(phase,cfg)
            self.assertAlmostEqual(a['left']['x']-a['root']['x'],l[0])
            self.assertAlmostEqual(a['right']['x']-a['root']['x'],r[0])

    def test_planted_feet_exact_world_lock(self):
        cfg=WalkSettings()
        speed=cfg.stride/cfg.stance_fraction
        for side,phase_offset in [('left',.5),('right',0)]:
            for i in range(1,999):
                t=i/1000
                u=(t+phase_offset)%1
                if 0<u<cfg.stance_fraction and u+.0005<cfg.stance_fraction:
                    first=pose(t,cfg)[side]
                    second=pose(t+.0005,cfg)[side]
                    self.assertAlmostEqual(first['x']+speed*t,second['x']+speed*(t+.0005),places=5)
                    self.assertEqual(first['y'],GROUND)
                    self.assertEqual(second['y'],GROUND)

    def test_pose_physical_envelope(self):
        qa=verify_motion(WalkSettings())
        self.assertTrue(qa['technical_motion_pass'],qa)
        self.assertEqual(qa['kinematic_reach_violations'],0)
        self.assertEqual(qa['penetrations'],0)
        self.assertLess(qa['max_planted_world_slip_px_per_sample'],1e-6)
        self.assertGreater(qa['max_swing_clearance_px'],30)
        self.assertTrue(all(label!='air' for label in qa['frame_contact_labels']))

    def test_heel_toe_continuity_and_symmetry(self):
        cfg=WalkSettings()
        eps=1e-7
        for threshold in (0.0,cfg.stance_fraction,1.0):
            self.assertLess(abs(foot_roll(threshold-eps,cfg)-foot_roll(threshold+eps,cfg)),1e-4)
        for i in range(200):
            t=i/200
            p=pose(t,cfg)
            self.assertAlmostEqual(p['rollL'],foot_roll(t+.5,cfg),places=9)
            self.assertAlmostEqual(p['rollR'],foot_roll(t,cfg),places=9)
            self.assertLessEqual(abs(p['rollL']),.23)
            self.assertLessEqual(abs(p['rollR']),.23)

    def test_reject_unphysical_config(self):
        for kwargs in ({'stride':200},{'clearance':130},{'stance_fraction':.4},{'fps':45},{'frames':7}):
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):WalkSettings(**kwargs).validate()


class BuildTests(unittest.TestCase):
    def test_real_export_and_safety_gate(self):
        studio=Path(__file__).parent/'pose_studio.html'
        if not studio.exists():studio=Path(__file__).parent/'index.html'
        with tempfile.TemporaryDirectory() as work:
            cfg=WalkSettings(frames=8)
            root=Path(work)/'build'
            manifest=export(root,cfg,studio)
            self.assertTrue(manifest['qa']['technical_pass'],manifest['qa'])
            self.assertEqual(manifest['strict_status'],'NEEDS_REVIEW')
            self.assertTrue(manifest['human_visual_review_required'])
            self.assertFalse(manifest['qa']['visual_review_pass'])
            self.assertEqual(len(list((root/'frames').glob('*.png'))),8)
            with Image.open(root/'atlas.png') as atlas:
                self.assertEqual(atlas.size,(2048,1024))
                self.assertEqual(atlas.mode,'RGBA')
            events=json.loads((root/'frame-events.json').read_text())
            self.assertEqual(len(events['frames']),8)
            self.assertEqual(events['strict_status'],'NEEDS_REVIEW')
            self.assertEqual(events['frames'][0]['footstep_event'],'right')
            self.assertEqual(events['frames'][4]['footstep_event'],'left')
            self.assertTrue(all(abs(f['left_foot_roll_degrees'])<=14 for f in events['frames']))
            self.assertTrue(all(abs(f['right_foot_roll_degrees'])<=14 for f in events['frames']))
            self.assertIn('function polishTechSkin(',studio.read_text(encoding='utf-8'))
            frame_poses=json.loads((root/'frame-poses.json').read_text())
            self.assertEqual(len(frame_poses['poses']),8)
            project=json.loads((root/'project.json').read_text())
            self.assertEqual(len(project['poses']),8)
            self.assertEqual(project['strict_status'],'NEEDS_REVIEW')
            self.assertTrue((root.parent/'CHR-TECH-WALK-autonomous-pose-v2.zip').exists())


if __name__=='__main__': unittest.main()
