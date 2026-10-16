"""The offline identity viewer is an export-only review surface, not a publisher."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from character_identity_polish_mobile_review import write_mobile_review


class MobileIdentityReviewTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.file = Path(temp.name) / "mobile-polish.html"
        self.row = {
            "id": "CHR-ENG-WALK", "frames": 8,
            "reference_id": "CHR-ENG-IDLE",
            "source_sha256": "1" * 64,
            "alternative_sha256": "2" * 64,
            "head_rgb_before": 14.29, "head_rgb_after": 3.08,
            "original_png": b"original verified bytes",
            "alternative_png": b"alternative verified bytes",
        }

    def test_self_contained_readable_and_no_runtime_promotion(self):
        result = write_mobile_review([self.row], self.file, 219)
        self.assertEqual(result["assets"], 1)
        self.assertEqual(result["strict_done_added"], 0)
        self.assertTrue(result["review_only"])
        html = self.file.read_text(encoding="utf-8")
        self.assertIn("CHR-ENG-WALK", html)
        self.assertIn("CHR-ENG-IDLE", html)
        self.assertIn("14.29", html)
        self.assertIn("data:image/png;base64,", html)
        self.assertIn("Exporter les observations", html)
        self.assertIn("42 px", html)
        self.assertIn("review_only:true", html)
        self.assertNotIn("__DATA__", html)
        self.assertNotIn("http://", html)
        self.assertNotIn("https://", html)
        self.assertNotIn("fetch(", html)
        self.assertNotIn("localStorage", html)

    def test_injection_attempt_in_label_is_encoded_before_script(self):
        changed = dict(self.row, id="CHR-ENG-WALK</script><script>alert(1)</script>")
        write_mobile_review([changed], self.file, 219)
        html = self.file.read_text(encoding="utf-8")
        self.assertNotIn("</script><script>alert(1)</script>", html)
        self.assertIn("\\u003c/script", html)

    def test_duplicate_ids_and_invalid_frame_counts_block_output(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            write_mobile_review([self.row, self.row], self.file, 219)
        self.assertFalse(self.file.exists())
        with self.assertRaisesRegex(ValueError, "frame count"):
            write_mobile_review([dict(self.row, frames=17)], self.file, 219)
        self.assertFalse(self.file.exists())

    def test_invalid_strict_done_not_misrepresented(self):
        with self.assertRaisesRegex(ValueError, "strict DONE"):
            write_mobile_review([self.row], self.file, 236)
        self.assertFalse(self.file.exists())

    def test_zero_safe_alternatives_displays_no_fake_candidate(self):
        result = write_mobile_review([], self.file, 219)
        self.assertEqual(result["assets"], 0)
        html = self.file.read_text(encoding="utf-8")
        self.assertIn("Aucune alternative sûre disponible", html)
        self.assertNotIn("data:image/png;base64,", html)


if __name__ == "__main__":
    unittest.main()
