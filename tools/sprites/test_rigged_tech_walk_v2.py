"""Offline, deterministic modular textured walk regression suite."""
from __future__ import annotations
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from rigged_tech_walk_v2 import (
 CANVAS, GROUND, PART_NAMES, build, draw_frame, foot_local, foot_roll,
 ik, load_kit, pose, check,
)

KIT=Path(__file__).with_name('skin-tech-v1.webp')
if not KIT.exists():
 KIT=Path('/mnt/data/tech-modular-v1.webp')

class RigMathTests(unittest.TestCase):
 def test_closed_loop_and_foot_contact(self):
  for t in (.0,.01,.17,.32,.53,.62,.83,.99):
   a,b=pose(t),pose(t+1)
   for k in ('root','left','right','handL','handR'):
    for va,vb in zip(a[k],b[k]): self.assertAlmostEqual(va,vb,places=8)
   for k in ('rollL','rollR'): self.assertAlmostEqual(a[k],b[k],places=8)
   for k in ('lockL','lockR'): self.assertEqual(a[k],b[k])
   p=a
   for side in ('left','right'):
    self.assertLessEqual(p[side][1],GROUND+1e-8)
   self.assertLessEqual(abs(p['rollL']),.23)
   self.assertLessEqual(abs(p['rollR']),.23)

 def test_world_space_stance_lock(self):
  speed=92/.62
  for offset in (0,.5):
   for j in range(1,999):
    t=j/1000
    phase=(t+offset)%1
    if .02<phase<.60:
     p=foot_local(t+offset)
     q=foot_local(t+offset+.0001)
     self.assertTrue(p[2] and q[2])
     self.assertAlmostEqual(p[0]+speed*t,q[0]+speed*(t+.0001),places=7)
     self.assertEqual(p[1],GROUND)

 def test_inverse_kinematics_lengths(self):
  for t in (.0,.025,.125,.25,.375,.5,.75,.975):
   p=pose(t)
   for hip,foot,sgn in [((p['root'][0]-13,p['root'][1]),p['left'],1),
                        ((p['root'][0]+13,p['root'][1]),p['right'],1)]:
    joint=ik(hip,foot,94,99,sgn)
    self.assertAlmostEqual(__import__('math').dist(hip,joint),94,delta=.015)
    self.assertAlmostEqual(__import__('math').dist(foot,joint),99,delta=.015)

class RenderTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.kit=load_kit(KIT)

 def test_all_twelve_pieces_present(self):
  self.assertEqual(len(PART_NAMES),12)
  for name in PART_NAMES:
   self.assertIsNotNone(self.kit[name].getchannel('A').getbbox(),name)

 def test_stable_identity_alpha_and_dimensions(self):
  a,pa,ba=draw_frame(.125,self.kit)
  b,pb,bb=draw_frame(.125,self.kit)
  c,_,_=draw_frame(.375,self.kit)
  self.assertEqual(a.size,(CANVAS,CANVAS))
  self.assertEqual(a.mode,'RGBA')
  self.assertEqual(hashlib.sha256(a.tobytes()).digest(),hashlib.sha256(b.tobytes()).digest())
  self.assertNotEqual(hashlib.sha256(a.tobytes()).digest(),hashlib.sha256(c.tobytes()).digest())
  self.assertEqual(a.getpixel((0,0))[3],0)
  for side in ('left','right'):
   self.assertLess(ba[side]['sole_error_px'],1)

 def test_optional_spine_flex_is_safe_and_backward_compatible(self):
  # The old WALK output must remain pixel-for-pixel unchanged when no spine
  # control is supplied; existing runtime art must not silently regress.
  for t in (0,.125,.375,.625):
   original,_,_=draw_frame(t,self.kit)
   neutral=pose(t);neutral['torso_lean_rad']=0.0
   unchanged,_,_=draw_frame(t,self.kit,neutral)
   self.assertEqual(original.tobytes(),unchanged.tobytes())
   tilted=pose(t);tilted['torso_lean_rad']=.05
   img,_,boot=draw_frame(t,self.kit,tilted)
   self.assertEqual(img.size,(CANVAS,CANVAS))
   self.assertIsNotNone(img.getchannel('A').getbbox())
   self.assertTrue(all(b['sole_error_px']<=1 for b in boot.values()))
  for invalid in (.09,-.09,float('nan'),float('inf')):
   bad=pose(.125);bad['torso_lean_rad']=invalid
   with self.subTest(invalid=invalid),self.assertRaises(ValueError):
    draw_frame(.125,self.kit,bad)

 def test_build_export_review_gate(self):
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp)/'render'
   manifest,bundle=build(KIT,out,frames=8,fps=8)
   qa=manifest['qa']
   self.assertTrue(qa['technical_pass'],qa)
   self.assertEqual(manifest['strict_status'],'NEEDS_REVIEW')
   self.assertTrue(manifest['human_visual_review_required'])
   self.assertFalse(qa['visual_review_pass'])
   self.assertFalse(qa['semantic_review_pass'])
   self.assertFalse(qa['edge_touch_frames'])
   self.assertTrue(qa['alpha_channel_present'])
   self.assertEqual(len(list((out/'frames').glob('*.png'))),8)
   self.assertEqual(len(json.loads((out/'footstep-events.json').read_text())),8)
   self.assertEqual(len(json.loads((out/'frame-poses.json').read_text())),8)
   self.assertEqual(json.loads((out/'footstep-events.json').read_text())[0]['footstep'],'right')
   self.assertEqual(json.loads((out/'footstep-events.json').read_text())[4]['footstep'],'left')
   with Image.open(out/'atlas.png') as atlas:
    self.assertEqual(atlas.size,(3072,1024))
    self.assertEqual(atlas.mode,'RGBA')
   self.assertTrue(bundle.is_file())
   self.assertTrue((out/'REVIEW_REQUIRED.txt').exists())

 def test_reject_invalid_config(self):
  for n,fps in ((7,12),(65,12),(8,30),(8,1)):
   with tempfile.TemporaryDirectory() as tmp:
    with self.assertRaises(ValueError):build(KIT,Path(tmp),frames=n,fps=fps)

if __name__=='__main__':unittest.main()
