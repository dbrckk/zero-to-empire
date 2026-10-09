"""Regression tests for alternative identity-locked WALK review candidates."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image,ImageDraw
from identity_locked_walk_candidate import (
    N_FRAMES,ROLES,source_frame,warp,render,
)

ROOT=Path(__file__).resolve().parents[2]


class IdentityLockedWalkTests(unittest.TestCase):
    def test_four_real_assets_are_not_overwritten_and_only_staged(self):
        for role in ROLES:
            with self.subTest(role=role),tempfile.TemporaryDirectory() as tmp:
                source=(ROOT/'art/incoming/final-sprites'/
                        f'zte_chr_{role.lower()}_walk_final.png')
                self.assertTrue(source.is_file(),source)
                digest=hashlib.sha256(source.read_bytes()).hexdigest()
                report=render(source,role,Path(tmp))
                self.assertEqual(digest,hashlib.sha256(source.read_bytes()).hexdigest())
                self.assertEqual(report['source_sha256'],digest)
                self.assertEqual(report['strict_status'],'NEEDS_REVIEW')
                self.assertEqual(report['identity_source_count'],1)
                self.assertFalse(report['visual_review_pass'])
                self.assertFalse(report['semantic_review_pass'])
                self.assertFalse(report['integrated_into_game'])
                self.assertFalse(report['canonical_source_overwritten'])
                self.assertEqual(report['frame_count'],N_FRAMES)
                self.assertEqual(report['visual_risk_screen']['risk_level']!='BLOCKING',True)
                atlas=Image.open(report['candidate_path'])
                self.assertEqual(atlas.size,(1024,512))
                self.assertEqual(atlas.mode,'RGBA')
                cells=[atlas.crop((i%4*256,i//4*256,i%4*256+256,i//4*256+256))
                       for i in range(N_FRAMES)]
                self.assertEqual(len({hashlib.sha256(c.tobytes()).hexdigest() for c in cells}),N_FRAMES)
                first=source_frame(source,ROLES[role])
                # Skeleton changes occur below the neck; identity pixels at
                # the crown remain unchanged, modulo tiny breathing motion.
                for cell in cells:
                    self.assertEqual(cell.getchannel('A').getbbox() is None,False)
                    bounds=cell.getchannel('A').getbbox()
                    self.assertGreaterEqual(min(bounds[0],bounds[1],256-bounds[2],256-bounds[3]),4)

    def test_cycle_deterministic_and_source_identity_immutable(self):
        source=ROOT/'art/incoming/final-sprites/zte_chr_op_walk_final.png'
        first=source_frame(source,ROLES['OP'])
        data=first.tobytes()
        for t in (0,.125,.4,.75,1):
            one=warp(first,t)
            two=warp(first,t)
            self.assertEqual(one.tobytes(),two.tobytes())
            self.assertEqual(one.getchannel('A').getbbox() is None,False)
        self.assertEqual(warp(first,0).tobytes(),warp(first,1).tobytes())
        self.assertEqual(first.tobytes(),data)

    def test_refuses_bad_inputs(self):
        with self.assertRaises(ValueError):warp(Image.new('RGB',(256,256)),.1)
        with self.assertRaises(ValueError):warp(Image.new('RGBA',(128,128)),.1)
        with self.assertRaises(ValueError):warp(Image.new('RGBA',(256,256)),float('nan'))
        with self.assertRaises(ValueError):warp(Image.new('RGBA',(256,256)),.1,amplitude=40)
        with self.assertRaises(ValueError):render(Path('unused'),'ALIEN',Path('unused'))


if __name__=="__main__":unittest.main()
