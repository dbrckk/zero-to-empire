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
    ACTIONS, GROUND, build_action, draw_frame, pose_for, spine_lean,
)
import rigged_tech_walk_v2 as core
from action_contact import work_contact, repair_contact, repair_spark_intensity, work_event_indices

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

    def test_action_spine_cycle_and_contact_are_stable(self):
        for action in ACTIONS:
            for i in range(96):
                t=i/96
                before=pose_for(t,action)
                after=pose_for(t+1,action)
                lean=spine_lean(t,action)
                self.assertTrue(math.isfinite(lean))
                self.assertAlmostEqual(before['torso_lean_rad'],lean,places=9)
                self.assertAlmostEqual(before['torso_lean_rad'],after['torso_lean_rad'],places=9)
                self.assertLessEqual(abs(lean),.085)
                for side in ('left','right'):
                    for v0,v1 in zip(before[side],after[side]):
                        self.assertAlmostEqual(v0,v1,places=7)
                x,y=before['root']
                co,si=math.cos(lean),math.sin(lean)
                for hand,dx,dy in [('handL',-24,-86),('handR',23,-85)]:
                    anchor=(x+dx*co-dy*si,y+dx*si+dy*co)
                    self.assertLessEqual(math.dist(anchor,before[hand]),118)

    def test_spine_offset_does_not_move_foot_targets(self):
        for action in ('WALK','CARRY'):
            for i in range(24):
                t=i/24
                p=pose_for(t,action)
                base=core.pose(t)
                self.assertEqual(p['left'],base['left'])
                self.assertEqual(p['right'],base['right'])
                self.assertEqual(p['lockL'],base['lockL'])
                self.assertEqual(p['lockR'],base['lockR'])

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
            self.assertGreaterEqual(max(math.dist(hand[0], q) for q in hand), 18)

    def test_celebration_is_overhead_and_periodic(self):
        for i in range(192):
            t=i/192
            p=pose_for(t,"CELEB")
            x,y=p["root"]
            angle=p["torso_lean_rad"]
            co,si=math.cos(angle),math.sin(angle)
            for hand,dx,dy in (("handL",-24,-86),("handR",23,-85)):
                shoulder=(x+dx*co-dy*si,y+dx*si+dy*co)
                self.assertGreaterEqual(shoulder[1]-p[hand][1],65)
                self.assertLessEqual(math.dist(shoulder,p[hand]),118)
            self.assertGreaterEqual(p["handR"][0]-p["handL"][0],135)
            q=pose_for(t+1,"CELEB")
            for key in ("handL","handR"):
                for a,b in zip(p[key],q[key]):
                    self.assertAlmostEqual(a,b,places=7)

    def test_action_contacts_and_overlaid_feedback_are_phase_correct(self):
        for i in range(96):
            t=i/96
            work=pose_for(t,"WORK")
            contact=work_contact(work)
            self.assertTrue(contact["handL_on_screen"],contact)
            self.assertTrue(contact["handR_on_screen"],contact)
            repair=pose_for(t,"REPAIR")
            self.assertTrue(repair_contact(repair)["torch_reachable"])
            self.assertLessEqual(repair_contact(repair)["torch_length_px"],70)

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

    def test_six_actions_use_reversible_joint_fabric(self):
        # Compare output against the SAME action/props rendered with the
        # old joint treatment; no pose, timing or event changes are permitted.
        for action in ACTIONS:
            for t in (.125,.375):
                current,p,b = draw_frame(action,t,self.kit)
                # One-identity, repeatable output with fabric enabled.
                duplicate,_,_ = draw_frame(action,t,self.kit)
                self.assertEqual(current.tobytes(),duplicate.tobytes())
                self.assertEqual(current.mode,'RGBA')
                self.assertTrue(all(v['sole_error_px']<=1 for v in b.values()))
        # WALK has no action props, making a strict binary before/after valid.
        sample=.125
        new,_,_=draw_frame('WALK',sample,self.kit)
        old,_,_=core.draw_frame(sample,self.kit,
                                 pose_for(sample,'WALK'),joint_fabric=False)
        self.assertNotEqual(new.tobytes(),old.tobytes())
        self.assertEqual(old.tobytes(),
                         core.draw_frame(sample,self.kit,pose_for(sample,'WALK'))[0].tobytes())

    def test_each_export_remains_a_review_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            for action in ACTIONS:
                with self.subTest(action=action):
                    out = Path(tmp) / action
                    manifest, bundle = build_action(KIT, out, action, frames=8, fps=8)
                    qa = manifest["qa"]
                    self.assertTrue(qa["technical_pass"], qa)
                    self.assertTrue(qa["action_kinematic_pass"], qa)
                    self.assertTrue(qa["game_scale_motion_pass"], qa)
                    self.assertTrue(qa["spine_lean_in_range"], qa)
                    self.assertLessEqual(qa["spine_lean_max_degrees"],5)
                    self.assertEqual(manifest["asset_id"], f"CHR-TECH-{action}")
                    self.assertEqual(manifest["strict_status"], "NEEDS_REVIEW")
                    self.assertTrue(qa["weight_transfer_pass"],qa)
                    self.assertTrue(qa["interaction_contact_pass"],qa)
                    self.assertTrue(qa["celebration_raised_arm_pass"], qa)
                    self.assertTrue(qa["celebration_wide_arm_pass"], qa)
                    if action=="CELEB":
                        self.assertGreaterEqual(qa["celebration_min_arm_raise_px"],65)
                        self.assertGreaterEqual(qa["celebration_min_wrist_span_px"],135)
                    else:
                        self.assertIsNone(qa["celebration_min_arm_raise_px"])
                    self.assertFalse(qa["work_screen_violation_frames"])
                    self.assertFalse(qa["repair_tool_violation_frames"])
                    if action=="REPAIR":
                        self.assertGreater(qa["repair_torch_length_range_px"][0],18)
                        self.assertLess(qa["repair_torch_length_range_px"][1],70)
                    self.assertEqual(manifest["weight_transfer"]["enabled"],
                                     action in ("WALK","CARRY"))
                    self.assertEqual(manifest["phase_origin_frame"],
                                     round(8*5/24) if action=="WORK" else 0)
                    if action=="WORK":
                        self.assertLess(qa["seam_to_median_ratio"],1.65)
                    self.assertTrue(manifest["renderer_features"]["joint_fabric"])
                    self.assertTrue(manifest["renderer_features"]["spine_flex"])
                    self.assertTrue(manifest["renderer_features"]["foot_roll"])
                    self.assertTrue(manifest["renderer_features"]["soft_deform"])
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
                    if action=="REPAIR":
                        phase_origin=manifest["phase_origin_frame"]
                        for i,e in enumerate(events):
                            enabled=repair_spark_intensity(
                                ((i+phase_origin)%8)/8)>0
                            self.assertEqual(e["vfx_event"]=="weld-sparks",enabled)
                    if action=="WORK":
                        expected=list(work_event_indices(8,manifest["phase_origin_frame"]))
                        actual=[i for i,e in enumerate(events)
                                if e["vfx_event"]=="data-update"]
                        self.assertEqual(actual,expected)
                        self.assertEqual(manifest["work_pulse_event_frames"],expected)
                    if action in ("WALK","CARRY"):
                        self.assertEqual(events[0]["footstep"], "right")
                        self.assertEqual(events[4]["footstep"], "left")
                    with Image.open(out / "atlas.png") as atlas:
                        self.assertEqual(atlas.size, (3072, 1024))
                        self.assertEqual(atlas.mode, "RGBA")


if __name__ == "__main__":
    unittest.main()
