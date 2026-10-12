"""Image-only headgear identity registration checks; no GPU or semantic approval."""
import unittest
from PIL import Image, ImageDraw
from character_head_identity_lock import lock_head_to_idle


def make_person(helmet=(245, 88, 38, 255), raised_arm=False):
    frame = Image.new("RGBA", (256, 256))
    draw = ImageDraw.Draw(frame)
    draw.ellipse((105, 25, 151, 73), fill=helmet)
    draw.rounded_rectangle((92, 78, 162, 164), radius=16, fill=(68, 81, 97, 255))
    draw.line((104, 92, 79, 144), fill=(65, 78, 92, 255), width=15)
    draw.line((149, 92, 178, 143), fill=(65, 78, 92, 255), width=15)
    draw.line((110, 159, 102, 225), fill=(51, 62, 71, 255), width=17)
    draw.line((144, 159, 155, 225), fill=(51, 62, 71, 255), width=17)
    if raised_arm:
        draw.line((147, 90, 144, 0), fill=(66, 80, 94, 255), width=16)
    return frame


class HeadIdentityLockTests(unittest.TestCase):
    def test_identical_upright_reference_restores_stable_headgear(self):
        anchor = make_person((241, 71, 40, 255))
        target = make_person((23, 218, 228, 255))
        result, applied, reason = lock_head_to_idle(target, anchor)
        self.assertTrue(applied, reason)
        self.assertEqual(reason, "same-run-idle-headgear-reference")
        self.assertEqual(result.size, (256, 256))
        # Center of the head stays a real part of the same IDLE reference.
        self.assertEqual(result.getpixel((128, 44))[:3], (241, 71, 40))
        self.assertNotEqual(target.getpixel((128, 44))[:3], result.getpixel((128, 44))[:3])

    def test_raised_arm_with_unreliable_top_alignment_is_not_pasted(self):
        source = make_person()
        target = make_person((12, 225, 234, 255), raised_arm=True)
        result, applied, reason = lock_head_to_idle(target, source)
        self.assertFalse(applied)
        self.assertIn(reason, {"unsafe-top-silhouette", "unsafe-body-scale"})
        self.assertEqual(result.tobytes(), target.tobytes())

    def test_wide_incompatible_head_shape_is_not_pasted(self):
        source = make_person()
        target = make_person((25, 223, 234, 255))
        # Keep the rest of the body while replacing the helmet silhouette
        # with an oversized incompatible rectangular obstruction.
        ImageDraw.Draw(target).rectangle((60, 12, 195, 87), fill=(18, 200, 226, 255))
        restored, applied, reason = lock_head_to_idle(target, source)
        self.assertFalse(applied)
        self.assertIn(reason, {"unsafe-head-silhouette-overlap", "unsafe-body-scale"})
        self.assertEqual(restored.tobytes(), target.tobytes())

    def test_empty_frames_cannot_be_identity_references(self):
        image = Image.new("RGBA", (256, 256))
        result, applied, reason = lock_head_to_idle(make_person(), image)
        self.assertFalse(applied)
        self.assertEqual(reason, "missing-full-body-head-anchor")
        self.assertEqual(result.size, (256, 256))


if __name__ == "__main__":
    unittest.main()
