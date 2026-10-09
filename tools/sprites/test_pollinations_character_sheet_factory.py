"""Offline regression checks: generation MUST return separate full-body frames."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from PIL import Image,ImageDraw

import pollinations_character_sheet_factory as factory
from character_semantic_gate import clip_risk


def full_body():
    frame=Image.new('RGBA',(256,256))
    d=ImageDraw.Draw(frame)
    d.ellipse((112,14,145,47),fill=(52,132,156,255))
    d.rectangle((105,48,151,139),fill=(47,122,151,255))
    d.line((115,139,99,223),fill=(52,132,156,255),width=15)
    d.line((140,139,155,223),fill=(52,132,156,255),width=15)
    return frame


class IndependentFrameTests(unittest.TestCase):
    def test_prompt_never_requests_multi_pose_atlas(self):
        for action in ('IDLE','WORK','CARRY','CELEB'):
            item={'id':'CHR-LOG-'+action,'role':'LOG','action':action}
            prompt=factory.independent_frame_prompt(item,'left foot forward')
            self.assertIn('ONE single standalone',prompt)
            self.assertIn('NOT a sprite sheet',prompt)
            self.assertIn('NO multiple people',prompt)
            self.assertIn('NO detached body parts',prompt)
        with self.assertRaises(ValueError):
            factory.independent_frame_prompt({'role':'LOG','action':'WALK'},'walk')

    def test_each_pose_is_its_own_image_not_an_atlas_slice(self):
        item={'id':'CHR-LOG-CARRY','role':'LOG','action':'CARRY'}
        requests=[]
        def fetch(prompt,seed):
            requests.append((prompt,seed))
            return Image.new('RGBA',(1024,1024))
        def extract(raw,action,standalone=False):
            self.assertEqual(action,'CARRY')
            self.assertTrue(standalone)
            self.assertEqual(raw.size,(1024,1024))
            return full_body(),.21
        with tempfile.TemporaryDirectory() as tmp, \
             patch.object(factory,'OUT',Path(tmp)), \
             patch.object(factory,'fetch',side_effect=fetch), \
             patch.object(factory,'cutout',side_effect=extract):
            # A source image saved before the new generation strategy must
            # never contaminate a modern identity-locked animation.
            old=Path(tmp)/'pollinations-frame-cache'/'CHR-LOG-CARRY'
            old.mkdir(parents=True,exist_ok=True)
            Image.new('RGBA',(256,256)).save(old/'00.png')
            first=factory.generate_independent_frames(item,49017)
            self.assertTrue((old/factory.STANDALONE_CACHE_EPOCH/'00.png').is_file())
            self.assertEqual(len(first),8)
            self.assertEqual(len(requests),8)
            self.assertEqual(len({seed for _,seed in requests}),8)
            self.assertTrue(all(f.size==(256,256) for f in first))
            self.assertNotEqual(clip_risk(first)['risk_level'],'BLOCKING')
            again=factory.generate_independent_frames(item,49017)
            self.assertEqual(len(again),8)
            self.assertEqual(len(requests),8) # cache, no web calls

    def test_margin_padding_does_not_erase_missing_body_parts(self):
        near_edge=Image.new('RGBA',(768,768))
        d=ImageDraw.Draw(near_edge)
        d.rectangle((110,23,650,758),fill=(80,125,155,255))
        padded=factory.safe_source_margin(near_edge)
        self.assertGreater(padded.height,near_edge.height)
        self.assertGreater(padded.width,near_edge.width)
        bb=padded.getchannel('A').getbbox()
        factory.validate_source_full_body(bb,padded.width,padded.height,
                                          'CARRY',standalone=True)
        self.assertEqual(padded.getchannel('A').getbbox()[3]-
                         padded.getchannel('A').getbbox()[1],736)
        cropped=near_edge.copy()
        ImageDraw.Draw(cropped).rectangle((110,0,650,758),
                                          fill=(80,125,155,255))
        with self.assertRaisesRegex(RuntimeError,'touches edge'):
            factory.safe_source_margin(cropped)

    def test_unexpected_action_cannot_use_generic_fallback(self):
        for action in ('WALK','REPAIR'):
            with self.assertRaises(ValueError):
                factory.generate_independent_frames(
                    {'id':'CHR-LOG-'+action,'role':'LOG','action':action},22)


if __name__=='__main__':
    unittest.main()
