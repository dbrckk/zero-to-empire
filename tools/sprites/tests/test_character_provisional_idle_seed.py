"""Engineer IDLE anchoring: provenance/technical-pass ONLY, never strict DONE."""
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
from character_provisional_idle_seed import prepare, load_seed, SEED_DIR, PNG_NAME


class ProvisionalEngineerSeedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.archive = self.root / "zte-characters-38825860064.zip"
        self.master = self.root / "master-asset-queue.json"
        self.queue = self.root / "controlled-character-regen-queue.json"
        self.shipped = self.root / "kernel-overlay"
        self.row = {
            "id": "CHR-ENG-IDLE",
            "strict_status": "NEEDS_REVIEW",
            "pipeline_status": "AWAITING_REVIEW",
            "review_artifact_run_id": 38825860064,
        }
        self.save_state()
        atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
        draw = ImageDraw.Draw(atlas)
        draw.ellipse((102, 24, 156, 78), fill=(223, 184, 119, 255))
        draw.rounded_rectangle((96, 72, 158, 161), radius=12,
                               fill=(55, 82, 97, 255))
        draw.line((106, 153, 103, 225), width=17, fill=(36, 43, 48, 255))
        draw.line((149, 153, 156, 225), width=17, fill=(36, 43, 48, 255))
        buffer = io.BytesIO()
        atlas.save(buffer, "PNG")
        self.blob = buffer.getvalue()
        self.source_row = {
            "filename": PNG_NAME,
            "sha256": hashlib.sha256(self.blob).hexdigest(),
            "bytes": len(self.blob),
            "strict_approved": False,
            "runtime_promoted": False,
            "deferred_art_warnings": [],
        }
        self.write_archive()

    def save_state(self):
        self.master.write_text(json.dumps({"target_total": 235, "assets": [self.row]}))
        self.queue.write_text(json.dumps({"targets": [
            {"id": "CHR-ENG-IDLE", "status": "PENDING_KAGGLE"},
            {"id": "CHR-ENG-WORK", "status": "PENDING_KAGGLE"},
            {"id": "CHR-ENG-REPAIR", "status": "PENDING_KAGGLE"},
        ]}))

    def write_archive(self, *, run=38825860064, rows=None, approved=False):
        index = {
            "source_collector_run_id": run,
            "automatic_semantic_approval": approved,
            "automatic_runtime_promotion": False,
            "candidate_count": 1,
            "assets": [self.source_row] if rows is None else rows,
        }
        with zipfile.ZipFile(self.archive, "w") as output:
            output.writestr("candidate-index.json", json.dumps(index))
            output.writestr("candidates/" + PNG_NAME, self.blob)

    def test_actual_review_only_seed_is_pinned_and_usable_as_visual_reference(self):
        meta = prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)
        self.assertFalse(meta["strict_approved"])
        self.assertFalse(meta["automatic_semantic_approval"])
        self.assertFalse(meta["runtime_promoted"])
        self.assertEqual(meta["source_collector_run_id"], 38825860064)
        self.assertEqual((self.shipped / SEED_DIR / PNG_NAME).read_bytes(), self.blob)
        image, label = load_seed("ENG", self.shipped)
        self.assertIsNotNone(image, label)
        self.assertEqual(image.size, (1024, 1024))
        self.assertEqual(image.getpixel((0, 0)), (139, 139, 139))
        self.assertIn("review-only", label)
        self.assertEqual(self.row["strict_status"], "NEEDS_REVIEW")
        self.assertIsNone(load_seed("OP", self.shipped)[0])

    def test_prevent_wrong_collector_provenance_even_if_name_is_correct(self):
        self.row["review_artifact_run_id"] = 999999
        self.save_state()
        with self.assertRaisesRegex(ValueError, "pinned"):
            prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)

    def test_review_status_may_not_be_strict_done(self):
        self.row["strict_status"] = "DONE"
        self.save_state()
        with self.assertRaisesRegex(ValueError, "canonical ENG-IDLE"):
            prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)

    def test_tampered_archived_bytes_cannot_supply_identity(self):
        self.source_row["sha256"] = "0" * 64
        self.write_archive()
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)

    def test_source_cannot_claim_semantic_approval(self):
        self.write_archive(approved=True)
        with self.assertRaisesRegex(ValueError, "review-only candidate"):
            prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)

    def test_no_identity_reference_if_source_image_is_corrupt(self):
        self.blob = b"not a png" * 30
        self.source_row["sha256"] = hashlib.sha256(self.blob).hexdigest()
        self.source_row["bytes"] = len(self.blob)
        self.write_archive()
        with self.assertRaisesRegex(ValueError, "PNG bytes"):
            prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)

    def test_modified_seed_is_rejected_at_kaggle_runtime(self):
        prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)
        (self.shipped / SEED_DIR / PNG_NAME).write_bytes(b"changed")
        image, reason = load_seed("ENG", self.shipped)
        self.assertIsNone(image)
        self.assertIn("SHA-256", reason)

    def test_missing_provisional_overlay_returns_no_seed_not_approval(self):
        image, reason = load_seed("ENG", self.root)
        self.assertIsNone(image)
        self.assertEqual(reason, "provisional-seed-not-shipped")

    def test_never_accept_unrequested_engineer_seed(self):
        self.queue.write_text(json.dumps({"targets": [
            {"id": "CHR-ENG-IDLE", "status": "PENDING_KAGGLE"}
        ]}))
        with self.assertRaisesRegex(ValueError, "pending engineer action"):
            prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)


if __name__ == "__main__":
    unittest.main()
