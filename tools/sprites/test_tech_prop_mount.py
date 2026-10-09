"""Safety and frame-stability checks for mounted WORK/REPAIR hardware."""
from __future__ import annotations

import math
import unittest

from PIL import Image
from tech_prop_mount import SUPPORTS, mount_geometry, draw_mount
from rigged_tech_actions_v3 import pose_for


class TechPropMountTests(unittest.TestCase):
    def test_all_512_phase_samples_keep_belt_and_device_connected(self):
        for action in ("WORK","REPAIR"):
            for i in range(512):
                p=pose_for(i/512,action)
                g=mount_geometry(action,p['root'])
                self.assertTrue(g['all_links_connected'])
                self.assertTrue(g['same_rig_origin'])
                a,b=g['segment_lengths_px']
                self.assertGreater(a,9)
                self.assertLess(b,65)
                self.assertLess(a+b,110)
                x,y=p['root']
                self.assertEqual(g['belt_socket'],
                    (x+SUPPORTS[action][0][0],y+SUPPORTS[action][0][1]))

    def test_mount_follows_idle_bob_without_world_drift(self):
        for action in ("WORK","REPAIR"):
            for i in range(128):
                t=i/128
                a=mount_geometry(action,pose_for(t,action)['root'])
                b=mount_geometry(action,pose_for(t+1,action)['root'])
                for key in ('belt_socket','hinge','device_socket'):
                    self.assertAlmostEqual(a[key][0],b[key][0],places=8)
                    self.assertAlmostEqual(a[key][1],b[key][1],places=8)

    def test_software_draw_is_deterministic_and_not_clipped(self):
        for action in ("WORK","REPAIR"):
            pose=pose_for(.125,action)
            images=[]
            for _ in range(2):
                frame=Image.new('RGBA',(512,512))
                geom=draw_mount(frame,pose,action)
                self.assertTrue(geom['all_links_connected'])
                bbox=frame.getchannel('A').getbbox()
                self.assertIsNotNone(bbox)
                self.assertTrue(min(bbox[0],bbox[1],512-bbox[2],512-bbox[3])>7)
                images.append(frame)
            self.assertEqual(images[0].tobytes(),images[1].tobytes())

    def test_reject_invalid_roots_actions_canvases(self):
        for action in ('WORK','REPAIR'):
            for bad in ((float('nan'),240),(252,float('inf'))):
                with self.assertRaises(ValueError):
                    mount_geometry(action,bad)
            with self.assertRaises(ValueError):
                draw_mount(Image.new('RGB',(512,512)),
                           pose_for(.25,action),action)
        with self.assertRaises(ValueError):
            mount_geometry('IDLE',(252,270))


if __name__=='__main__':
    unittest.main()
