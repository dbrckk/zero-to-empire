"""Tests for approved legacy IDLE anchoring; no external models or GPU."""
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw
from character_approved_idle_fallback import load_approved_idle_anchor


def approved_atlas(path: Path, doubled: bool = False):
    atlas = Image.new("RGBA", (1024, 1024))
    d = ImageDraw.Draw(atlas)
    d.ellipse((107, 27, 149, 73), fill=(242, 165, 95, 255))
    d.rounded_rectangle((96, 70, 164, 158), radius=13, fill=(215, 137, 48, 255))
    d.line((108, 154, 102, 222), fill=(72, 74, 81, 255), width=16)
    d.line((146, 154, 152, 222), fill=(72, 74, 81, 255), width=16)
    if doubled:
        d.ellipse((24, 36, 73, 82), fill=(255, 162, 90, 255))
        d.rectangle((20, 85, 76, 222), fill=(217, 144, 58, 255))
    atlas.save(path)


class ApprovedIdleFallbackTests(unittest.TestCase):
    def test_reuses_exact_existing_strict_done_visual_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            m = root / "manifest.md"
            m.write_text(
                "| CHR-LOG-IDLE | worker | idle | `file.webp` | DONE |\n",
                encoding="utf-8")
            original = root / "zte_chr_log_idle_final.png"
            approved_atlas(original)
            image, reason = load_approved_idle_anchor("LOG", m, root)
            self.assertIsNotNone(image, reason)
            self.assertEqual(image.size, (1024, 1024))
            self.assertEqual(image.getpixel((0, 0)), (139, 139, 139))
            self.assertNotEqual(image.getpixel((512, 320)), (139, 139, 139))
            self.assertIn("visual-reference-only", reason)
            self.assertTrue(original.is_file())

    def test_runtimes_unapproved_idle_never_becomes_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            m = root / "manifest.md"
            m.write_text(
                "| CHR-ENG-IDLE | engineer | idle | `file.webp` | RUNTIME |\n",
                encoding="utf-8")
            approved_atlas(root / "zte_chr_eng_idle_final.png")
            image, reason = load_approved_idle_anchor("ENG", m, root)
            self.assertIsNone(image)
            self.assertEqual(reason, "role-not-eligible-for-existing-idle-fallback")
            m.write_text("| CHR-LOG-IDLE | worker | idle | `file.webp` | RUNTIME |\n",
                         encoding="utf-8")
            approved_atlas(root / "zte_chr_log_idle_final.png")
            image, reason = load_approved_idle_anchor("LOG", m, root)
            self.assertIsNone(image)
            self.assertEqual(reason, "source-idle-not-uniquely-strict-done")

    def test_rejects_duplicate_person_in_single_cell(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = root / "manifest.md"
            manifest.write_text(
                "| CHR-LOG-IDLE | worker | idle | `file.webp` | DONE |\n",
                encoding="utf-8")
            approved_atlas(root / "zte_chr_log_idle_final.png", doubled=True)
            image, reason = load_approved_idle_anchor("LOG", manifest, root)
            self.assertIsNone(image)
            self.assertEqual(reason, "strict-done-idle-not-tall-single-subject")


if __name__ == "__main__":
    unittest.main()
