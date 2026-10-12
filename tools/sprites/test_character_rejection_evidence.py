"""Synthetic tests for opt-in review evidence; never creates approval."""
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image, ImageDraw
from character_rejection_evidence import save_rejected_idle_preview


class RejectionEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_rejected_idle_keeps_exact_frames_and_no_approval(self):
        frames=[]
        for index in range(6):
            frame=Image.new("RGBA", (256, 256))
            ImageDraw.Draw(frame).rectangle((98, 27, 158, 229),
                                             fill=(30 + index * 20, 62, 90, 255))
            frames.append(frame)
        result=save_rejected_idle_preview(frames,"CHR-ENG-IDLE",
                                          "gray shadow suspect",self.root)
        self.assertIsNotNone(result)
        image_path,report_path=result
        self.assertTrue(image_path.is_file())
        data=json.loads(report_path.read_text())
        self.assertEqual(data["status"],"REJECTED")
        self.assertTrue(data["review_only"])
        self.assertFalse(data["strict_promotion_permitted"])
        self.assertFalse(data["technical_or_semantic_approval"])
        self.assertEqual(data["visible_frames"],6)
        with Image.open(image_path) as atlas:
            self.assertEqual(atlas.size,(1024,1024))
            for index,source in enumerate(frames):
                cell=atlas.crop(((index%4)*256,(index//4)*256,
                                 ((index%4)+1)*256,((index//4)+1)*256))
                self.assertEqual(cell.convert("RGBA").tobytes(),source.tobytes())

    def test_non_idle_asset_and_no_frames_never_write_preview(self):
        frames=[Image.new("RGBA",(256,256)) for _ in range(6)]
        self.assertIsNone(save_rejected_idle_preview(
            frames,"CHR-LOG-WORK","not an idle",self.root))
        self.assertIsNone(save_rejected_idle_preview(
            [],"CHR-ENG-IDLE","no frames",self.root))
        self.assertFalse(any(self.root.iterdir()))

    def test_bad_dimensions_are_not_silently_published(self):
        with self.assertRaises(ValueError):
            save_rejected_idle_preview([Image.new("RGBA",(1024,1024))],
                                       "CHR-ENG-IDLE","wrong dimensions",self.root)


if __name__ == "__main__":
    unittest.main()
