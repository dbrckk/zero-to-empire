"""Offline framing tests: no build artifacts or user review necessary."""
import unittest
from PIL import Image, ImageDraw
from focused_sprite_atlas import CANVAS, PIVOT, shared_crop, view_pivot, framed_sprite


class FramingTests(unittest.TestCase):
    def test_shared_camera_for_six_animation_unions(self):
        union=[(163,47,357,467),(171,47,368,467),(167,49,341,459),
               (174,49,368,459),(174,49,376,459),(137,48,372,459)]
        crop=shared_crop(union)
        self.assertEqual(crop,(28,33,476,481))
        self.assertEqual(shared_crop(list(reversed(union))),crop)
        self.assertAlmostEqual(CANVAS/(crop[2]-crop[0]),1.142857,places=5)
        for b in union:
            self.assertLessEqual(crop[0],b[0]);self.assertLessEqual(crop[1],b[1])
            self.assertGreaterEqual(crop[2],b[2]);self.assertGreaterEqual(crop[3],b[3])

    def test_metadata_preserves_exact_world_pivot(self):
        crop=(28,33,476,481)
        for size in (96,128,256):
            pt=view_pivot(crop,size)
            self.assertEqual(len(pt),2)
            self.assertAlmostEqual(pt[0],size/2,places=3)
            self.assertAlmostEqual(pt[1],round((449-33)*size/448,3),places=3)

    def test_framed_sprite_does_not_clip_visual_effects(self):
        image=Image.new('RGBA',(CANVAS,CANVAS))
        d=ImageDraw.Draw(image)
        d.ellipse((137,48,372,459),fill=(20,80,130,200))
        d.ellipse((130,90,142,102),fill=(45,210,255,1))
        crop=shared_crop([image.getchannel('A').getbbox()])
        for size in (96,128):
            got=framed_sprite(image,crop,size)
            self.assertEqual(got.size,(size,size))
            self.assertEqual(got.mode,'RGBA')
            self.assertIsNotNone(got.getchannel('A').getbbox())
        with self.assertRaisesRegex(ValueError,'clip'):
            framed_sprite(image,(160,33,480,481),96)

    def test_invalid_camera_bounds_and_pivots_are_rejected(self):
        for bounds in ([],[(-1,2,100,200)],[(200,400,100,450)],[(1,1,514,300)]):
            with self.subTest(bounds=bounds),self.assertRaises(ValueError):
                shared_crop(bounds)
        with self.assertRaisesRegex(ValueError,'Foot pivot'):
            shared_crop([(0,0,30,30)],margin=0,pivot=(900,900))
        with self.assertRaisesRegex(ValueError,'Pivot outside'):
            view_pivot((0,0,100,100),96)
        with self.assertRaises(ValueError):
            framed_sprite(Image.new('RGB',(512,512)),(0,0,512,512),96)

    def test_full_extent_uses_legacy_safe_fallback(self):
        crop=shared_crop([(0,0,512,512)])
        self.assertEqual(crop,(0,0,512,512))
        image=Image.new('RGBA',(512,512))
        ImageDraw.Draw(image).rectangle((0,0,511,511),fill=(100,150,160,255))
        result=framed_sprite(image,crop,96)
        self.assertEqual(result.getchannel('A').getbbox(),(0,0,96,96))


if __name__=='__main__':unittest.main()
