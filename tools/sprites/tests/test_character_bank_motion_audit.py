"""Regression tests: mobile motion warnings must never approve candidate artwork."""
from __future__ import annotations

import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit_character_bank_motion import analyze


class MobileMotionAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bank = self.root / "bank.zip"
        self.report = self.root / "audit.json"
        self.asset_id = "CHR-ENG-WORK"
        self.filename = "zte_chr_eng_work_final.png"
        self.metadata = {
            "target_total": 235,
            "strict_done": 219,
            "candidate_count": 1,
            "automatic_semantic_approval": False,
            "automatic_runtime_promotion": False,
        }

    def png(self, *, moving=False):
        atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
        brush = ImageDraw.Draw(atlas)
        for i in range(10):
            x, y = (i % 4) * 256, (i // 4) * 256
            move = (i % 2) * 45 if moving else 0
            brush.rectangle(
                (x + 68 + move, y + 38, x + 155 + move, y + 232),
                fill=(8, 100, 160, 255),
            )
        buffer = io.BytesIO()
        atlas.save(buffer, format="PNG")
        return buffer.getvalue()

    def write_bank(self, *, moving=False, digest=None, approve=False):
        blob = self.png(moving=moving)
        entry = {
            "id": self.asset_id, "filename": self.filename,
            "bytes": len(blob),
            "sha256": digest if digest is not None else hashlib.sha256(blob).hexdigest(),
            "deferred_art_warnings": ["FACE_HEADGEAR_STRUCTURE_DRIFT_RISK"],
            "source_type": "repo-local-original",
            "strict_approved": approve,
            "runtime_promoted": False,
        }
        data = dict(self.metadata, bank_entries=[entry])
        with zipfile.ZipFile(self.bank, "w") as packed:
            packed.writestr("candidate-bank-index.json", json.dumps(data))
            packed.writestr("candidates/" + self.filename, blob)

    def test_still_work_requires_attention_but_is_not_automatically_approved(self):
        self.write_bank()
        result = analyze(self.bank, self.report)
        self.assertEqual(result["candidate_count"], 1)
        self.assertEqual(result["motion_attention_count"], 1)
        item = result["assets"][0]
        self.assertIn("LOW_MOBILE_FRAME_CHANGE_REVIEW", item["new_motion_flags"])
        self.assertIn("NEAR_STATIC_TRANSITIONS_REVIEW", item["new_motion_flags"])
        self.assertIn("FACE_HEADGEAR_STRUCTURE_DRIFT_RISK", item["review_flags"])
        self.assertFalse(item["strict_approved"])
        self.assertFalse(item["runtime_promoted"])
        self.assertFalse(result["automatic_semantic_approval"])
        self.assertEqual(json.loads(self.report.read_text())["mobile_render_px"], 42)

    def test_distinct_poses_have_higher_observable_motion(self):
        self.write_bank(moving=True)
        moved = analyze(self.bank, self.report)
        self.assertNotIn("LOW_MOBILE_FRAME_CHANGE_REVIEW",
                         moved["assets"][0]["new_motion_flags"])
        self.assertGreater(moved["assets"][0]["motion_metrics"]["mean_frame_change"], 0.012)

    def test_sha_mismatch_fails_closed(self):
        self.write_bank(digest="0" * 64)
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            analyze(self.bank, self.report)
        self.assertFalse(self.report.exists())

    def test_strict_approved_metadata_fails_closed(self):
        self.write_bank(approve=True)
        with self.assertRaisesRegex(ValueError, "Untrusted candidate"):
            analyze(self.bank, self.report)

    def test_report_requires_review_only_bank(self):
        self.write_bank()
        with zipfile.ZipFile(self.bank, "r") as existing:
            data = {name: existing.read(name) for name in existing.namelist()}
        meta = json.loads(data["candidate-bank-index.json"])
        meta["automatic_runtime_promotion"] = True
        data["candidate-bank-index.json"] = json.dumps(meta).encode()
        with zipfile.ZipFile(self.bank, "w") as updated:
            for name, blob in data.items():
                updated.writestr(name, blob)
        with self.assertRaisesRegex(ValueError, "Untrusted candidate bank"):
            analyze(self.bank, self.report)


if __name__ == "__main__":
    unittest.main()
