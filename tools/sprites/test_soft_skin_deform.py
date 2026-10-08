"""Tests for deterministic, opt-in bending of TECH modular atlas textures."""
from __future__ import annotations
import math
import unittest
from pathlib import Path
from PIL import Image
from soft_skin_deform import signed_joint_bend, soft_limb
import rigged_tech_walk_v2 as core
from rigged_tech_actions_v3 import ACTIONS, draw_frame as draw_action, pose_for

KIT = Path(__file__).with_name("skin-tech-v1.webp")


class DeformedSkinTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kit = core.load_kit(KIT)

    def test_bend_orientation_and_continuity(self):
        self.assertEqual(signed_joint_bend((0,0),(0,10),(0,20)),0)
        self.assertLess(signed_joint_bend((0,0),(0,10),(10,20)),0)
        self.assertGreater(signed_joint_bend((0,0),(0,10),(-10,20)),0)
        self.assertLessEqual(abs(signed_joint_bend((0,0),(0,10),(20,20))),5)

    def test_reject_invalid_curves_and_textures(self):
        for offset in (8,-8,float("nan"),float("inf")):
            with self.subTest(offset=offset),self.assertRaises(ValueError):
                soft_limb(Image.new("RGBA",(512,512)),self.kit["thigh_near"],
                          (100,150),(100,245),bend_px=offset)
        with self.assertRaises(ValueError):
            soft_limb(Image.new("RGB",(512,512)),self.kit["thigh_near"],
                      (100,150),(100,245))

    def test_opt_in_preserves_exact_legacy_pixels(self):
        for t in (0,.125,.375,.625):
            prior,_,_=core.draw_frame(t,self.kit,joint_fabric=True)
            explicit,_,_=core.draw_frame(t,self.kit,joint_fabric=True,soft_deform=False)
            changed,_,boots=core.draw_frame(t,self.kit,joint_fabric=True,soft_deform=True)
            duplicate,_,_=core.draw_frame(t,self.kit,joint_fabric=True,soft_deform=True)
            self.assertEqual(prior.tobytes(),explicit.tobytes())
            self.assertEqual(changed.tobytes(),duplicate.tobytes())
            self.assertNotEqual(prior.tobytes(),changed.tobytes())
            self.assertTrue(all(item["sole_error_px"]<=1 for item in boots.values()))

    def test_24_frame_walk_geometry_and_review_lock(self):
        frames=[];positions=[];boots=[]
        for i in range(24):
            img,p,b=core.draw_frame(i/24,self.kit,joint_fabric=True,soft_deform=True)
            frames.append(img);positions.append(p);boots.append(b)
        qa=core.check(frames,positions,boots)
        self.assertTrue(qa["technical_pass"],qa)
        self.assertFalse(qa["visual_review_pass"])
        self.assertFalse(qa["semantic_review_pass"])
        self.assertEqual(qa["strict_status"],"NEEDS_REVIEW")

    def test_six_action_renderer_is_deterministic_not_clipped(self):
        for action in ACTIONS:
            for t in (.125,.375):
                a,p,boots=draw_action(action,t,self.kit)
                b,_,_=draw_action(action,t,self.kit)
                with self.subTest(action=action,time=t):
                    self.assertEqual(a.tobytes(),b.tobytes())
                    self.assertEqual(a.mode,"RGBA")
                    self.assertEqual(a.size,(512,512))
                    box=a.getchannel("A").getbbox()
                    self.assertIsNotNone(box)
                    self.assertGreaterEqual(min(box[0],box[1],512-box[2],512-box[3]),6)
                    self.assertTrue(all(info["sole_error_px"]<=1 for info in boots.values()))
        # The WALK candidate must be soft deformed, unlike the explicit old path.
        source=pose_for(.125,"WALK")
        new,_,_=draw_action("WALK",.125,self.kit)
        legacy,_,_=core.draw_frame(.125,self.kit,source,joint_fabric=True,
                                   soft_deform=False)
        self.assertNotEqual(new.tobytes(),legacy.tobytes())


if __name__=="__main__":
    unittest.main()
