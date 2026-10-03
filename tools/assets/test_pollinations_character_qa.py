#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "tools/sprites/pollinations_character_sheet_factory.py"
spec = importlib.util.spec_from_file_location("pollinations_character_sheet_factory", MODULE)
factory = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(factory)


class PollinationsCharacterQaTests(unittest.TestCase):
    def test_source_bbox_rejects_edge_cropped_torso(self):
        with self.assertRaisesRegex(RuntimeError, "source edge"):
            factory.validate_source_full_body((30, 8, 220, 255), 256, 256, "CARRY", False)

    def test_source_bbox_rejects_short_nonrepair_fragment(self):
        with self.assertRaisesRegex(RuntimeError, "source short"):
            factory.validate_source_full_body((50, 50, 205, 170), 256, 256, "IDLE", False)

    def test_source_bbox_allows_full_body_with_safe_margin(self):
        self.assertTrue(factory.validate_source_full_body((55, 12, 200, 240), 256, 256, "IDLE", False))

    def test_static_nonwalk_actions_are_rejected(self):
        frame = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        d = ImageDraw.Draw(frame)
        d.rectangle((95, 30, 160, 235), fill=(120, 140, 150, 255))
        for action in ("WORK", "CARRY", "REPAIR", "CELEB"):
            ok, why = factory.actionqa([frame.copy() for _ in range(6)], action)
            self.assertFalse(ok, (action, why))

    def test_idle_requires_small_but_nonzero_motion(self):
        a = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        b = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        ImageDraw.Draw(a).rectangle((95, 30, 160, 235), fill=(120, 140, 150, 255))
        ImageDraw.Draw(b).rectangle((98, 30, 163, 235), fill=(120, 140, 150, 255))
        ok, _ = factory.actionqa([a, b, a, b], "IDLE")
        self.assertTrue(ok)


if __name__ == "__main__":
    unittest.main()
