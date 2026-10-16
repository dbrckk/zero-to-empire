"""PNG contact sheet is an SHA-verified manual review aid, never promotion."""
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
from build_character_role_contact_sheet import build


class RoleConsistencySheetTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.bank = self.root / "bank.zip"
        self.audit = self.root / "audit.json"
        self.output = self.root / "role-comparison.png"
        self.entries = []
        self.records = []
        self.blobs = {}
        for i, role in enumerate(("OP", "LOG", "ENG")):
            action = "WALK" if role != "ENG" else "IDLE"
            asset_id = f"CHR-{role}-{action}"
            filename = f"zte_chr_{role.lower()}_{action.lower()}_final.png"
            atlas = Image.new("RGBA", (1024, 1024))
            artist = ImageDraw.Draw(atlas)
            artist.ellipse((100, 25, 158, 85),
                           fill=(80 + i * 50, 130, 150, 255))
            artist.rectangle((103, 78, 152, 215),
                             fill=(50, 125 + i * 20, 85, 255))
            memory = io.BytesIO()
            atlas.save(memory, format="PNG")
            blob = memory.getvalue()
            self.blobs[filename] = blob
            checksum = hashlib.sha256(blob).hexdigest()
            self.entries.append({
                "id": asset_id, "filename": filename, "sha256": checksum,
                "bytes": len(blob), "strict_approved": False,
                "runtime_promoted": False, "source_type": "collected-kaggle",
            })
            self.records.append({
                "id": asset_id, "sha256": checksum, "strict_approved": False,
                "runtime_promoted": False,
                "new_identity_flags": ["CROSS_ACTION_HEAD_IDENTITY_REVIEW"] if role == "LOG" else [],
                "new_motion_flags": ["LOW_MOBILE_FRAME_CHANGE_REVIEW"] if role == "OP" else [],
                "head_identity_metrics": {
                    "reference_id": asset_id, "mean_head_rgb_change": 0.0,
                },
            })
        self.save()

    def save(self):
        with zipfile.ZipFile(self.bank, "w") as result:
            result.writestr("candidate-bank-index.json", json.dumps({
                "candidate_count": len(self.entries),
                "bank_entries": self.entries, "strict_done": 219,
                "automatic_semantic_approval": False,
                "automatic_runtime_promotion": False,
            }))
            for name, blob in self.blobs.items():
                result.writestr("candidates/" + name, blob)
        self.audit.write_text(json.dumps({
            "review_only": True, "candidate_count": len(self.records),
            "automatic_semantic_approval": False,
            "automatic_runtime_promotion": False,
            "assets": self.records,
        }))

    def test_role_sheet_is_readable_png_and_does_not_approve_candidates(self):
        report = build(self.bank, self.audit, self.output)
        self.assertTrue(report["review_only"])
        self.assertEqual(report["asset_count"], 3)
        self.assertEqual(report["identity_attention_count"], 1)
        self.assertEqual(report["strict_done_unchanged"], 219)
        self.assertEqual(report["strict_done_added"], 0)
        with Image.open(self.output) as image:
            self.assertEqual(image.format, "PNG")
            self.assertEqual(image.size, (1344, 1026))
            self.assertGreater(len(image.getcolors(1 << 20) or []), 10)

    def test_sha_tampering_of_png_or_audit_fails_closed(self):
        self.entries[0]["sha256"] = "0" * 64
        self.save()
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            build(self.bank, self.audit, self.output)
        self.assertFalse(self.output.exists())
        self.entries[0]["sha256"] = hashlib.sha256(
            self.blobs[self.entries[0]["filename"]]).hexdigest()
        self.records[0]["sha256"] = "a" * 64
        self.save()
        with self.assertRaisesRegex(ValueError, "Stale or incomplete"):
            build(self.bank, self.audit, self.output)

    def test_missing_audit_coverage_is_not_silently_ignored(self):
        self.records.pop()
        self.save()
        with self.assertRaisesRegex(ValueError, "does not cover precisely"):
            build(self.bank, self.audit, self.output)

    def test_semantically_approved_candidate_or_audit_must_be_rejected(self):
        self.entries[0]["strict_approved"] = True
        self.save()
        with self.assertRaisesRegex(ValueError, "untrusted candidate"):
            build(self.bank, self.audit, self.output)
        self.entries[0]["strict_approved"] = False
        self.records[0]["runtime_promoted"] = True
        self.save()
        with self.assertRaisesRegex(ValueError, "Stale or incomplete"):
            build(self.bank, self.audit, self.output)

    def test_empty_first_frame_is_blocking_even_with_valid_hash(self):
        filename = self.entries[0]["filename"]
        memory = io.BytesIO()
        Image.new("RGBA", (1024, 1024)).save(memory, "PNG")
        self.blobs[filename] = memory.getvalue()
        digest = hashlib.sha256(self.blobs[filename]).hexdigest()
        self.entries[0]["sha256"] = digest
        self.entries[0]["bytes"] = len(self.blobs[filename])
        self.records[0]["sha256"] = digest
        self.save()
        with self.assertRaisesRegex(ValueError, "Empty candidate first frame"):
            build(self.bank, self.audit, self.output)


if __name__ == "__main__":
    unittest.main()
