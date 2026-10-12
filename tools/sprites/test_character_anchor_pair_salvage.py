"""Synthetic multi-person role-anchor recovery tests; no semantic approval."""
import unittest
from PIL import Image, ImageDraw
from character_anchor_pair_salvage import salvage_two_full_body_subjects


def pair(second=True, overlapping=False, second_short=False):
    bg=(219,219,219)
    image=Image.new('RGB',(1024,1024),bg)
    alpha=Image.new('L',(1024,1024))
    draw=ImageDraw.Draw(image)
    mask=ImageDraw.Draw(alpha)
    left=(120,90,315,800)
    right=(270 if overlapping else 670,100,480 if overlapping else 850,
           375 if second_short else 815)
    draw.rounded_rectangle(left,radius=36,fill=(56,85,112))
    mask.rounded_rectangle(left,radius=36,fill=255)
    if second:
        draw.rounded_rectangle(right,radius=32,fill=(144,65,70))
        mask.rounded_rectangle(right,radius=32,fill=255)
    image.putpixel((0,0),bg)
    isolated=image.convert('RGBA')
    isolated.putalpha(alpha)
    return image,isolated


class PairAnchorRecoveryTests(unittest.TestCase):
    def test_one_person_is_kept_from_two_separate_full_bodies(self):
        image,isolated=pair()
        result,evidence=salvage_two_full_body_subjects(image,isolated)
        self.assertIsNotNone(result,evidence)
        self.assertTrue(evidence['discarded_second_subject'])
        self.assertFalse(evidence['semantic_approval'])
        self.assertEqual(result.size,(1024,1024))
        self.assertEqual(result.getpixel((512,512)),(56,85,112))
        self.assertEqual(result.getpixel((800,512)),(219,219,219))

    def test_single_person_is_not_falsely_salvaged(self):
        image,isolated=pair(second=False)
        result,reason=salvage_two_full_body_subjects(image,isolated)
        self.assertIsNone(result)
        self.assertEqual(reason,'no-independent-full-body-pair')

    def test_overlap_is_left_for_manual_rejection(self):
        image,isolated=pair(overlapping=True)
        result,reason=salvage_two_full_body_subjects(image,isolated)
        self.assertIsNone(result)
        self.assertEqual(reason,'no-independent-full-body-pair')

    def test_short_detached_panel_is_not_treated_as_another_worker(self):
        image,isolated=pair(second_short=True)
        result,reason=salvage_two_full_body_subjects(image,isolated)
        self.assertIsNone(result)
        self.assertIn(reason,{
            'secondary-component-not-a-full-body-person',
            'multi-subject-parts-not-two-tall-figures'
        })


if __name__=='__main__':
    unittest.main()
