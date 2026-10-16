"""Protect deterministic role face/helmet retouch proposals from silent approvals."""
from __future__ import annotations

import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit_character_bank_motion import analyze
from build_character_identity_polish import build


class CharacterIdentityPolishTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.bank = self.root / "bank.zip"
        self.audit = self.root / "audit.json"
        self.output = self.root / "polish.zip"
        self.report = self.root / "polish.json"
        self.comparison = self.root / "polish.png"
        self.mobile = self.root / "polish-mobile.html"
        self.entries = []
        self.blobs = {}
        self.write_atlases()

    @staticmethod
    def atlas(count: int, head_color: tuple[int, int, int],
              bad_frame: int | None = None) -> bytes:
        atlas = Image.new("RGBA", (1024, 1024))
        for index in range(count):
            frame = Image.new("RGBA", (256, 256))
            artist = ImageDraw.Draw(frame)
            if index != bad_frame:
                artist.ellipse((107, 20, 151, 82), fill=(*head_color, 255))
                artist.rectangle((95, 84, 162, 178), fill=(52, 71, 94, 255))
                artist.rectangle((105, 177, 118, 235), fill=(38, 46, 55, 255))
                artist.rectangle((142, 177, 156, 235), fill=(38, 46, 55, 255))
            else:
                artist.ellipse((120, 117, 140, 145), fill=(*head_color, 255))
                artist.rectangle((115, 141, 146, 176), fill=(52, 71, 94, 255))
            atlas.alpha_composite(frame, ((index % 4) * 256, (index // 4) * 256))
        out = io.BytesIO()
        atlas.save(out, "PNG")
        return out.getvalue()

    def write_atlases(self, *, same_head=False, bad_frame=None):
        reference_color = (252, 122, 14)
        diverged_color = reference_color if same_head else (8, 180, 233)
        data = [
            ("CHR-OP-WALK", 8, reference_color, None),
            ("CHR-OP-WORK", 10, diverged_color, bad_frame),
        ]
        self.entries = []
        self.blobs = {}
        for aid, count, col, damage in data:
            fname = "zte_chr_" + aid.split("-")[1].lower() + "_" + aid.split("-")[2].lower() + "_final.png"
            blob = self.atlas(count, col, damage)
            self.blobs[fname] = blob
            self.entries.append({
                "id": aid, "filename": fname, "sha256": hashlib.sha256(blob).hexdigest(),
                "bytes": len(blob), "strict_approved": False,
                "runtime_promoted": False, "source_type": "collected-kaggle",
                "deferred_art_warnings": [],
            })
        self.save()
        analyze(self.bank, self.audit)

    def save(self):
        with zipfile.ZipFile(self.bank, "w") as packed:
            packed.writestr("candidate-bank-index.json", json.dumps({
                "candidate_count": len(self.entries),
                "bank_entries": self.entries, "strict_done": 219,
                "target_total": 235,
                "automatic_semantic_approval": False,
                "automatic_runtime_promotion": False,
            }))
            for name, blob in self.blobs.items():
                packed.writestr("candidates/" + name, blob)

    def test_proposes_complete_review_only_identity_retouch(self):
        result = build(self.bank, self.audit, self.output, self.report, self.comparison,
                       self.mobile)
        self.assertEqual(result["identity_flags_to_review"], 1)
        self.assertEqual(result["alternatives_created"], 1)
        self.assertEqual(result["not_safe_to_polish"], [])
        self.assertEqual(result["strict_done_unchanged"], 219)
        self.assertTrue(result["review_only"])
        self.assertFalse(result["automatic_semantic_approval"])
        self.assertFalse(result["automatic_runtime_promotion"])
        row = result["alternatives"][0]
        self.assertEqual(row["id"], "CHR-OP-WORK")
        self.assertEqual(row["reference_id"], "CHR-OP-WALK")
        self.assertEqual(row["frames_head_locked"], 10)
        self.assertEqual(row["frames"], 10)
        self.assertLess(row["head_rgb_after"], row["head_rgb_before"] * .65)
        self.assertEqual(row["mobile_motion_before"]["mobile_render_px"], 42)
        self.assertEqual(row["mobile_motion_after"]["mobile_render_px"], 42)
        self.assertEqual(
            row["mobile_motion_before"]["mean_lower_body_change"],
            row["mobile_motion_after"]["mean_lower_body_change"],
        )
        self.assertEqual(
            result["mobile_motion_regression_review_count"],
            sum(x["mobile_motion_regression_review"] for x in result["alternatives"]),
        )
        self.assertFalse(row["strict_approved"])
        self.assertFalse(row["runtime_promoted"])
        with zipfile.ZipFile(self.output) as packed:
            self.assertEqual(len(packed.namelist()), 3)
            blob = packed.read(row["path"])
            self.assertEqual(hashlib.sha256(blob).hexdigest(), row["alternative_sha256"])
            with Image.open(io.BytesIO(blob)) as sprite:
                self.assertEqual(sprite.size, (1024, 1024))
                self.assertEqual(sprite.mode, "RGBA")
                original = Image.open(io.BytesIO(self.blobs["zte_chr_op_work_final.png"]))
                # The change is strictly restricted to head/neck; legs and
                # lower torso of EVERY frame remain pixel-exact.
                for i in range(10):
                    a = original.crop(((i % 4) * 256, (i // 4) * 256 + 126,
                                       (i % 4 + 1) * 256, (i // 4 + 1) * 256))
                    b = sprite.crop(((i % 4) * 256, (i // 4) * 256 + 126,
                                     (i % 4 + 1) * 256, (i // 4 + 1) * 256))
                    self.assertIsNone(ImageChops.difference(a, b).getbbox())
        self.assertEqual(json.loads(self.report.read_text()), result)
        with Image.open(self.comparison) as png:
            self.assertEqual(png.size, (786, 352))
        html = self.mobile.read_text(encoding="utf-8")
        self.assertIn("CHR-OP-WORK", html)
        self.assertIn(row["source_sha256"], html)
        self.assertIn(row["alternative_sha256"], html)
        self.assertIn("data:image/png;base64,", html)
        self.assertIn("Exporter les observations", html)
        self.assertIn("42 px", html)
        self.assertNotIn("__DATA__", html)
        self.assertNotIn("http://", html)
        self.assertNotIn("https://", html)

    def test_one_unsafe_pose_rejects_entire_proposal_not_just_one_frame(self):
        self.write_atlases(bad_frame=4)
        result = build(self.bank, self.audit, self.output, self.report,
                       mobile_review_path=self.mobile)
        self.assertEqual(result["alternatives_created"], 0)
        self.assertEqual(result["identity_flags_to_review"], 1)
        self.assertEqual(result["not_safe_to_polish"][0]["id"], "CHR-OP-WORK")
        self.assertIn("frame-4:", result["not_safe_to_polish"][0]["reason"])
        with zipfile.ZipFile(self.output) as packed:
            self.assertFalse(any(name.startswith("review-alternatives/")
                                 for name in packed.namelist()))
        self.assertNotIn("data:image/png;base64,", self.mobile.read_text())

    def test_mobile_motion_regression_rejects_entire_retouch(self):
        from unittest.mock import patch
        import build_character_identity_polish as module

        original = module.motion_stats
        calls = [0]

        def deteriorated_second_atlas(blob, count):
            result = original(blob, count)
            calls[0] += 1
            if calls[0] % 2 == 0:
                result["mean_frame_change"] = result["mean_frame_change"] * .5
            return result

        with patch.object(module, "motion_stats", side_effect=deteriorated_second_atlas):
            report = build(self.bank, self.audit, self.output, self.report)
        self.assertEqual(report["alternatives_created"], 0)
        self.assertEqual(report["not_safe_to_polish"][0]["id"], "CHR-OP-WORK")
        self.assertEqual(report["not_safe_to_polish"][0]["reason"],
                         "mobile-motion-regression-after-head-polish")
        with zipfile.ZipFile(self.output) as packed:
            self.assertFalse(any(x.startswith("review-alternatives/")
                                 for x in packed.namelist()))

    def test_consistent_actions_are_not_needlessly_modified(self):
        self.write_atlases(same_head=True)
        result = build(self.bank, self.audit, self.output, self.report)
        self.assertEqual(result["alternatives_created"], 0)
        self.assertEqual(result["identity_flags_to_review"], 0)

    def test_invalid_candidate_sha_fails_closed(self):
        self.entries[-1]["sha256"] = "f" * 64
        self.save()
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            build(self.bank, self.audit, self.output, self.report)
        self.assertFalse(self.output.exists())

    def test_audit_reference_is_same_role_verified_and_not_forged(self):
        data = json.loads(self.audit.read_text())
        row = next(x for x in data["assets"] if x["id"] == "CHR-OP-WORK")
        row["head_identity_metrics"]["reference_id"] = "CHR-ENG-IDLE"
        self.audit.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Invalid canonical role identity anchor"):
            build(self.bank, self.audit, self.output, self.report)

    def test_audit_metric_cannot_be_forged_to_force_proposal(self):
        data = json.loads(self.audit.read_text())
        row = next(x for x in data["assets"] if x["id"] == "CHR-OP-WORK")
        row["head_identity_metrics"]["mean_head_rgb_change"] = 31.99
        self.audit.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "head difference metrics"):
            build(self.bank, self.audit, self.output, self.report)

    def test_forged_same_role_anchor_is_rejected(self):
        data = json.loads(self.audit.read_text())
        data["head_identity_reference"]["OP"] = "CHR-OP-WORK"
        row = next(x for x in data["assets"] if x["id"] == "CHR-OP-WORK")
        row["head_identity_metrics"]["reference_id"] = "CHR-OP-WORK"
        self.audit.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Invalid canonical role identity anchor"):
            build(self.bank, self.audit, self.output, self.report)
        self.assertFalse(self.output.exists())

    def test_self_anchor_cannot_claim_identity_warning(self):
        data = json.loads(self.audit.read_text())
        row = next(x for x in data["assets"] if x["id"] == "CHR-OP-WALK")
        row["new_identity_flags"] = ["CROSS_ACTION_HEAD_IDENTITY_REVIEW"]
        self.audit.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Invalid anchor self-comparison"):
            build(self.bank, self.audit, self.output, self.report)
        self.assertFalse(self.output.exists())

    def test_no_auto_promotion_even_when_source_falsely_claims_approval(self):
        self.entries[1]["strict_approved"] = True
        self.save()
        with self.assertRaisesRegex(ValueError, "untrusted bank entry"):
            build(self.bank, self.audit, self.output, self.report)


if __name__ == "__main__":
    unittest.main()
