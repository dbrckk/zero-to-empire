"""Regression tests for verified PNG-to-WebP character promotion."""
import io
import unittest
from PIL import Image
from promote_user_approved_characters import assert_render_equivalent


class CharacterRuntimeEquivalenceTests(unittest.TestCase):
    def setUp(self):
        self.source = Image.new("RGBA", (3, 1))
        self.source.putdata([(233, 12, 12, 0), (5, 73, 99, 7), (140, 51, 211, 180)])

    def test_lossless_webp_after_alpha_cleanup(self):
        prepared = self.source.copy()
        prepared.putalpha(prepared.getchannel("A").point(lambda a: 0 if a < 8 else a))
        encoded = io.BytesIO()
        prepared.save(encoded, "WEBP", lossless=True, method=4, exact=True)
        encoded.seek(0)
        with Image.open(encoded) as runtime:
            assert_render_equivalent(self.source, runtime, "TEST")

    def test_invisible_rgb_is_not_an_approval_failure(self):
        runtime = Image.new("RGBA", (3, 1))
        runtime.putdata([(0, 0, 0, 0), (0, 0, 0, 0), (140, 51, 211, 180)])
        assert_render_equivalent(self.source, runtime, "TEST")

    def test_detects_visible_color_corruption(self):
        runtime = Image.new("RGBA", (3, 1))
        runtime.putdata([(0, 0, 0, 0), (0, 0, 0, 0), (141, 51, 211, 180)])
        with self.assertRaises(AssertionError):
            assert_render_equivalent(self.source, runtime, "TEST")

    def test_detects_alpha_corruption(self):
        runtime = Image.new("RGBA", (3, 1))
        runtime.putdata([(0, 0, 0, 0), (0, 0, 0, 8), (140, 51, 211, 180)])
        with self.assertRaises(AssertionError):
            assert_render_equivalent(self.source, runtime, "TEST")


if __name__ == "__main__":
    unittest.main()
