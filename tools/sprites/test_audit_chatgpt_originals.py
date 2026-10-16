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

    def test_walk_flags_disproportionate_loop_snap(self):
        with tempfile.TemporaryDirectory() as temp:
            atlas = Image.new("RGBA", (1024, 1024))
            for index in range(8):
                frame = Image.new("RGBA", (256, 256))
                draw = ImageDraw.Draw(frame)
                # Seven nearby poses followed by a distant final pose.
                offset = index * 2 if index < 7 else 95
                draw.rectangle((40 + offset, 175, 65 + offset, 225),
                               fill=(220, 170, 120, 255))
                atlas.alpha_composite(frame, ((index % 4) * 256,
                                              (index // 4) * 256))
            path = Path(temp) / "walk-snap.png"
            atlas.save(path)
            result = inspect(path, "ENG", "WALK")
            self.assertIn("LOCOMOTION_LOOP_SEAM_SNAP_RISK", result["flags"])
            self.assertEqual(result["risk_level"], "BLOCKING")

    def test_repair_detects_tool_snap_even_with_stationary_legs(self):
        with tempfile.TemporaryDirectory() as temp:
            atlas = Image.new("RGBA", (1024, 1024))
            for index in range(10):
                frame = Image.new("RGBA", (256, 256))
                draw = ImageDraw.Draw(frame)
                draw.rectangle((95, 170, 130, 230), fill=(190, 150, 110, 255))
                x = 40 + index if index < 9 else 170
                draw.rectangle((x, 30, x + 25, 65), fill=(255, 230, 140, 255))
                atlas.alpha_composite(frame, ((index % 4) * 256,
                                              (index // 4) * 256))
            path = Path(temp) / "repair-tool-snap.png"
            atlas.save(path)
            result = inspect(path, "ENG", "REPAIR")
            self.assertIn("UPPER_BODY_LOOP_SEAM_SNAP_RISK", result["flags"])
            self.assertEqual(result["risk_level"], "BLOCKING")
            self.assertGreater(result["upper_body_loop_seam_change"], .30)

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
