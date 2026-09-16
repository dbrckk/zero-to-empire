import unittest

from PIL import Image, ImageDraw

from tools.assets.static_processing import isolate, normalize, validate


class StaticProcessingTest(unittest.TestCase):
    def test_isolate_normalize_and_validate_centered_subject(self):
        source = Image.new("RGB", (256, 256), (0, 0, 0))
        draw = ImageDraw.Draw(source)
        draw.rectangle((88, 78, 168, 178), fill=(220, 170, 80))

        isolated = isolate(source)
        self.assertEqual(isolated.mode, "RGBA")
        self.assertEqual(isolated.getpixel((0, 0))[3], 0)
        self.assertGreater(isolated.getpixel((128, 128))[3], 200)

        normalized = normalize(isolated, 1024)
        self.assertEqual(normalized.size, (1024, 1024))
        coverage, dominant = validate(normalized)
        self.assertLess(coverage, 0.70)
        self.assertGreaterEqual(dominant, 0.88)

    def test_validate_rejects_subject_touching_safety_edge(self):
        image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 80, 90, 180), fill=(220, 170, 80, 255))
        with self.assertRaisesRegex(RuntimeError, "transparent safety padding failed"):
            validate(image)

    def test_validate_rejects_disconnected_primary_subjects(self):
        image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle((40, 80, 105, 175), fill=(220, 170, 80, 255))
        draw.rectangle((150, 80, 215, 175), fill=(80, 170, 220, 255))
        with self.assertRaisesRegex(RuntimeError, "subject isolation failed"):
            validate(image)


if __name__ == "__main__":
    unittest.main()
