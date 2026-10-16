"""42px gameplay storyboard is a provenance-verified review aid."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build_character_mobile_motion_storyboard import build, _selected_frames
from test_character_role_contact_sheet import RoleConsistencySheetTests


class GameplayMotionStoryboardTests(unittest.TestCase):
    save = RoleConsistencySheetTests.save

    def setUp(self):
        # Reuse synthetic OP/LOG/ENG candidate bank with SHA-matched audit.
        RoleConsistencySheetTests.setUp(self)
        self.output = self.root / "motion-storyboard.png"

    def test_frames_include_first_middle_and_loop_seam(self):
        self.assertEqual(_selected_frames(6), (0, 2, 4, 5))
        self.assertEqual(_selected_frames(8), (0, 2, 5, 7))
        self.assertEqual(_selected_frames(10), (0, 3, 6, 9))

    def test_42px_both_lighting_conditions_and_no_promotion(self):
        report = build(self.bank, self.audit, self.output)
        self.assertEqual(report["candidate_count"], 3)
        self.assertEqual(report["frames_per_action"], 4)
        self.assertEqual(report["actual_render_px"], 42)
        self.assertEqual(report["nearest_neighbor_zoom"], 3)
        self.assertEqual(report["strict_done_unchanged"], 219)
        self.assertEqual(report["strict_done_added"], 0)
        with Image.open(self.output) as png:
            self.assertEqual(png.format, "PNG")
            self.assertEqual(png.size, (798, 1082))
            self.assertNotEqual(png.getpixel((255, 150)), png.getpixel((255, 296)))

    def test_corrupt_audit_rejected_without_creating_output(self):
        data = json.loads(self.audit.read_text())
        data["assets"][0]["sha256"] = "0" * 64
        self.audit.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Stale or incomplete"):
            build(self.bank, self.audit, self.output)
        self.assertFalse(self.output.exists())

    def test_automatic_approval_forbidden(self):
        data = json.loads(self.audit.read_text())
        data["automatic_semantic_approval"] = True
        self.audit.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Untrusted review-only"):
            build(self.bank, self.audit, self.output)


if __name__ == "__main__":
    unittest.main()
