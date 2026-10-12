"""Ground shadow cleanup regressions; image-only recovery, no approvals."""
import unittest
from PIL import Image, ImageDraw
from character_ground_shadow_cleanup import remove_baked_ground_shadow


def character(shadow: bool = True, white_shoes: bool = False):
    image = Image.new("RGBA", (256, 256))
    d = ImageDraw.Draw(image)
    if shadow:
        d.ellipse((62, 210, 196, 238), fill=(210, 211, 211, 255))
    d.ellipse((109, 20, 149, 67), fill=(167, 118, 83, 255))
    d.rounded_rectangle((100, 69, 158, 154), radius=14, fill=(56, 71, 84, 255))
    d.line((107, 150, 106, 222), fill=(66, 74, 86, 255), width=21)
    d.line((150, 150, 158, 225), fill=(65, 76, 91, 255), width=21)
    sole = (204, 204, 205, 255) if white_shoes else (48, 55, 70, 255)
    d.rounded_rectangle((93, 218, 123, 235), radius=5, fill=sole)
    d.rounded_rectangle((151, 221, 185, 237), radius=5, fill=sole)
    return image


class GroundShadowCleanupTests(unittest.TestCase):
    def test_long_neutral_shadow_removed_without_erasing_dark_boots(self):
        source=character()
        clean, removed = remove_baked_ground_shadow(source)
        self.assertGreater(removed, 50)
        self.assertEqual(clean.getpixel((72, 226))[3], 0)
        self.assertEqual(clean.getpixel((104, 229))[:3], (48, 55, 70))
        self.assertEqual(clean.getpixel((166, 231))[:3], (48, 55, 70))
        self.assertEqual(clean.getpixel((128, 42)), source.getpixel((128, 42)))

    def test_without_shadow_has_no_changes(self):
        source=character(shadow=False)
        clean, removed = remove_baked_ground_shadow(source)
        self.assertEqual(removed, 0)
        self.assertEqual(clean.tobytes(), source.tobytes())

    def test_pale_shoes_do_not_get_erased_without_external_shadow(self):
        source=character(shadow=False, white_shoes=True)
        clean, removed = remove_baked_ground_shadow(source)
        self.assertEqual(removed, 0)
        self.assertEqual(clean.tobytes(), source.tobytes())

    def test_darker_shadow_trapped_between_boots_is_removed(self):
        original = character(shadow=False)
        trapped = Image.new("RGBA", (256, 256))
        draw = ImageDraw.Draw(trapped)
        draw.rectangle((120, 174, 146, 232), fill=(132, 132, 132, 255))
        draw.ellipse((80, 221, 173, 235), fill=(132, 132, 132, 255))
        trapped.alpha_composite(original)
        before_face = trapped.getpixel((128, 42))
        before_boot = trapped.getpixel((105, 228))
        cleaned, removed = remove_baked_ground_shadow(trapped)
        self.assertGreater(removed, 100)
        self.assertEqual(cleaned.getpixel((130, 226))[3], 0)
        self.assertEqual(cleaned.getpixel((128, 42)), before_face)
        self.assertEqual(cleaned.getpixel((105, 228)), before_boot)

    def test_gray_pants_with_connected_feet_are_not_split(self):
        source = Image.new("RGBA", (256, 256))
        draw = ImageDraw.Draw(source)
        draw.ellipse((112, 20, 150, 70), fill=(175, 125, 88, 255))
        draw.rounded_rectangle((93, 70, 167, 174), radius=15,
                               fill=(56, 65, 79, 255))
        draw.rectangle((96, 167, 164, 233), fill=(155, 155, 155, 255))
        cleaned, removed = remove_baked_ground_shadow(source)
        self.assertEqual(removed, 0)
        self.assertEqual(cleaned.tobytes(), source.tobytes())

    def test_wrong_shape_is_left_untouched(self):
        source=Image.new("RGBA", (128, 128), (225, 225, 225, 255))
        clean, removed = remove_baked_ground_shadow(source)
        self.assertEqual(removed, 0)
        self.assertEqual(clean.tobytes(), source.tobytes())


if __name__ == "__main__":
    unittest.main()
