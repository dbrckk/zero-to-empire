"""Regression coverage for character motion audit loop closure."""
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw
from audit_chatgpt_originals import inspect


class CharacterLoopSeamTests(unittest.TestCase):
    def test_walk_reports_last_to_first_change(self):
        with tempfile.TemporaryDirectory() as temp:
            atlas = Image.new("RGBA", (1024, 1024))
            for index in range(8):
                frame = Image.new("RGBA", (256, 256))
                draw = ImageDraw.Draw(frame)
                # Last frame intentionally returns to first, giving a zero
                # seam change despite motion between intermediate frames.
                offset = 0 if index in (0, 7) else 10 + index * 5
                draw.rectangle((95 + offset, 175, 125 + offset, 225),
                               fill=(220, 170, 120, 255))
                atlas.alpha_composite(frame, ((index % 4) * 256,
                                              (index // 4) * 256))
            path = Path(temp) / "walk.png"
            atlas.save(path)
            result = inspect(path, "ENG", "WALK")
            self.assertEqual(len(result["lower_body_adjacent_changes"]), 8)
            self.assertEqual(result["lower_body_loop_seam_change"], 0.0)
            self.assertGreater(max(result["lower_body_adjacent_changes"]), 0)

    def test_carry_reports_wraparound_too(self):
        with tempfile.TemporaryDirectory() as temp:
            atlas = Image.new("RGBA", (1024, 1024))
            draw = ImageDraw.Draw(atlas)
            draw.rectangle((100, 180, 120, 225), fill=(255, 255, 255, 255))
            draw.rectangle((3 * 256 + 180, 180, 3 * 256 + 200, 225),
                           fill=(255, 255, 255, 255))
            path = Path(temp) / "carry.png"
            atlas.save(path)
            result = inspect(path, "LOG", "CARRY")
            self.assertGreater(result["lower_body_loop_seam_change"], 0)


if __name__ == "__main__":
    unittest.main()
