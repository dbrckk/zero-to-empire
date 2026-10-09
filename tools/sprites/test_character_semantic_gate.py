"""Synthetic visual failure tests, no external models and no automatic approval."""
import unittest
from PIL import Image,ImageDraw
from character_semantic_gate import clip_risk,frame_geometry,palette_distance,color_signature


def person(i=0,color=(80,144,187,255)):
    frame=Image.new('RGBA',(256,256))
    d=ImageDraw.Draw(frame)
    d.ellipse((113+i,20,144+i,52),fill=color)
    d.polygon([(108+i,57),(148+i,57),(155+i,140),(99+i,140)],fill=color)
    d.line((101+i,74,80+i,131),fill=color,width=10)
    d.line((145+i,74,174+i,131),fill=color,width=10)
    d.line((114+i,135,104+i,221),fill=color,width=15)
    d.line((138+i,135,150+i,221),fill=color,width=15)
    d.line((99+i,222,111+i,222),fill=color,width=11)
    d.line((142+i,222,157+i,222),fill=color,width=11)
    return frame


def portrait(i=0):
    frame=Image.new('RGBA',(256,256))
    d=ImageDraw.Draw(frame)
    d.ellipse((33+i,10,224+i,198),fill=(85,151,189,255))
    d.polygon([(70+i,173),(175+i,173),(205+i,239),(47+i,239)],
              fill=(85,151,189,255))
    return frame


class SemanticGateTests(unittest.TestCase):
    def test_consistent_full_body_is_not_blocked(self):
        result=clip_risk([person(i%3) for i in range(8)])
        self.assertNotEqual(result['risk_level'],'BLOCKING')
        self.assertFalse(result['image_only_semantic_approval'])

    def test_portraits_and_fragments_block(self):
        result=clip_risk([portrait(i%2) for i in range(8)])
        self.assertEqual(result['risk_level'],'BLOCKING')
        self.assertIn('MULTIPLE_NON_FULL_BODY_FRAMES',result['flags'])

    def test_unrelated_costume_palettes_are_detected(self):
        frames=[person(0,(210,30,45,255)) if i%2 else
                person(0,(12,185,210,255)) for i in range(8)]
        result=clip_risk(frames)
        self.assertIn('PALETTE_IDENTITY_DISCONTINUITY_RISK',result['flags'])

    def test_empty_frame_fails_hard(self):
        self.assertFalse(frame_geometry(Image.new('RGBA',(256,256)))['valid'])
        frames=[person() for _ in range(7)]+[Image.new('RGBA',(256,256))]
        self.assertEqual(clip_risk(frames)['risk_level'],'BLOCKING')

    def test_same_palette_is_identical(self):
        signature=color_signature(person())
        self.assertAlmostEqual(palette_distance(signature,signature),0)
        with self.assertRaises(ValueError):
            clip_risk([person()])


if __name__=='__main__':
    unittest.main()
