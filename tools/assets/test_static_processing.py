import unittest

from PIL import Image

from tools.assets.static_processing import isolate, normalize, validate


class StaticProcessingCharacterizationTest(unittest.TestCase):
    def test_isolate_normalize_and_validate_preserve_existing_contract(self):
        source = Image.new("RGB", (256, 256), (0, 0, 0))
        for y in range(78, 178):
            for x in range(88, 168):
                source.putpixel((x, y), (230, 180, 90))

        isolated = isolate(source)
        self.assertEqual(isolated.mode, "RGBA")
        self.assertEqual(isolated.getpixel((0, 0))[3], 0)
        self.assertGreater(isolated.getpixel((128, 128))[3], 200)

        normalized = normalize(isolated, 1024)
        self.assertEqual(normalized.size, (1024, 1024))
        coverage, dominant = validate(normalized)
        self.assertLess(coverage, 0.70)
        self.assertGreaterEqual(dominant, 0.88)

    def test_validate_rejects_subject_inside_four_percent_safety_edge(self):
        image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        for y in range(80, 176):
            for x in range(0, 72):
                image.putpixel((x, y), (220, 190, 120, 255))

        with self.assertRaisesRegex(RuntimeError, "transparent safety padding failed"):
            validate(image)


if __name__ == "__main__":
    unittest.main()
