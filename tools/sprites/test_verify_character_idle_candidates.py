"""Offline collector fallback QA checks, without model/GPU or strict promotion."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

from verify_character_idle_candidates import annotate_report


def atlas(two_heads: bool) -> Image.Image:
    im = Image.new("RGBA", (1024, 1024))
    for i in range(6):
        tile = Image.new("RGBA", (256, 256))
        painter = ImageDraw.Draw(tile)
        if two_heads:
            painter.ellipse((76, 20, 108, 63), fill=(235, 169, 55, 255))
            painter.ellipse((144, 20, 176, 63), fill=(235, 169, 55, 255))
            painter.rectangle((75, 65, 180, 162), fill=(204, 126, 41, 255))
            painter.line((91, 156, 84, 232), fill=(60, 66, 75, 255), width=18)
            painter.line((161, 156, 170, 232), fill=(60, 66, 75, 255), width=18)
        else:
            painter.ellipse((111, 20, 145, 62), fill=(237, 169, 53, 255))
            painter.rectangle((95, 65, 161, 162), fill=(64, 75, 91, 255))
            painter.line((112, 155, 102, 232), fill=(63, 70, 80, 255), width=16)
            painter.line((146, 155, 160, 232), fill=(63, 70, 80, 255), width=16)
        im.alpha_composite(tile, ((i % 4) * 256, (i // 4) * 256))
    return im


class CollectorSingleSubjectQA(unittest.TestCase):
    def test_realistic_two_worker_pair_overrides_producer_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            atlas(True).save(directory / "zte_chr_log_idle_final.png")
            atlas(False).save(directory / "zte_chr_op_idle_final.png")
            report = {"assets": [
                {"file": "zte_chr_log_idle_final.png", "pass": True, "issues": []},
                {"file": "zte_chr_op_idle_final.png", "pass": True, "issues": []},
            ]}
            output = annotate_report(directory, report)
            self.assertFalse(output["assets"][0]["pass"])
            self.assertEqual(
                output["assets"][0]["idle_identity_risk"]["head_counts"], [2]*6
            )
            self.assertIn("idle-visual-risk:MULTIPLE_IDLE_HEADS_RISK",
                          output["assets"][0]["issues"])
            self.assertTrue(output["assets"][1]["pass"])
            self.assertEqual(
                output["assets"][1]["idle_identity_risk"]["head_counts"], [1]*6
            )
            self.assertEqual(output["automatic_pass"], 1)
            self.assertEqual(output["needs_review"], 1)
            again = annotate_report(directory, output)
            self.assertEqual(again["assets"][0]["issues"].count(
                "idle-visual-risk:MULTIPLE_IDLE_HEADS_RISK"), 1)

    def test_missing_idle_candidate_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = {"assets": [
                {"file": "zte_chr_log_idle_final.png", "pass": True, "issues": []}
            ]}
            output = annotate_report(Path(tmp), report)
            self.assertFalse(output["assets"][0]["pass"])
            self.assertIn("idle-visual-risk:IDLE_VISUAL_QA_ERROR",
                          output["assets"][0]["issues"])

    def test_non_idle_status_is_never_altered(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = {"assets": [
                {"file": "zte_chr_log_work_final.png", "pass": True, "issues": []},
            ]}
            output = annotate_report(Path(tmp), report)
            self.assertTrue(output["assets"][0]["pass"])
            self.assertNotIn("idle_identity_risk", output["assets"][0])


if __name__ == "__main__":
    unittest.main()
