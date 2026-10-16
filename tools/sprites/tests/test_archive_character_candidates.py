#!/usr/bin/env python3
"""Offline candidate archive tests; no cloud/GPU credentials required."""
import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from archive_character_candidates import archive_candidates, PNG_SIGNATURE


class CandidateArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "download"
        (self.root / "output" / "candidates").mkdir(parents=True)
        self.bundle = Path(self.temp.name) / "release.zip"
        self.qa = self.root / "output" / "github-qa-report.json"

    def write_file(self, name, payload=None):
        target = self.root / "output" / "candidates" / name
        target.write_bytes(payload if payload is not None else PNG_SIGNATURE + b"test-candidate-png")
        return target

    def write_qa(self, rows):
        self.qa.write_text(json.dumps({"assets": rows}), encoding="utf-8")

    def test_saves_only_real_qa_passing_candidates_with_hashes(self):
        passing = "zte_chr_op_celeb_final.png"
        failing = "zte_chr_log_work_final.png"
        self.write_file(passing)
        self.write_file(failing)
        self.write_qa([
            {"file": passing, "pass": True,
             "deferred_art_warnings": ["CELEBRATION_NO_OVERHEAD_ARM_GESTURE_RISK"]},
            {"file": failing, "pass": False, "issues": ["bad-frame"]},
        ])
        manifest = archive_candidates(self.root, self.bundle, 38815707999)
        self.assertEqual(manifest["candidate_count"], 1)
        self.assertFalse(manifest["automatic_runtime_promotion"])
        self.assertFalse(manifest["automatic_semantic_approval"])
        self.assertEqual(manifest["assets"][0]["deferred_art_warnings"],
                         ["CELEBRATION_NO_OVERHEAD_ARM_GESTURE_RISK"])
        with zipfile.ZipFile(self.bundle) as packed:
            self.assertEqual(set(packed.namelist()),
                             {"candidate-index.json", "candidates/" + passing})
            self.assertEqual(manifest["assets"][0]["sha256"],
                             hashlib.sha256(packed.read("candidates/" + passing)).hexdigest())

    def test_missing_passing_image_fails_closed(self):
        self.write_qa([{"file": "zte_chr_eng_idle_final.png", "pass": True}])
        with self.assertRaisesRegex(ValueError, "missing or ambiguous"):
            archive_candidates(self.root, self.bundle, 123)

    def test_invalid_signature_fails_closed(self):
        self.write_file("zte_chr_eng_walk_final.png", b"NOT_A_PNG" + b"x" * 30)
        self.write_qa([{"file": "zte_chr_eng_walk_final.png", "pass": True}])
        with self.assertRaisesRegex(ValueError, "not PNG"):
            archive_candidates(self.root, self.bundle, 123)

    def test_duplicate_qa_rows_fail_closed(self):
        name = "zte_chr_op_walk_final.png"
        self.write_file(name)
        self.write_qa([{"file": name, "pass": True}, {"file": name, "pass": True}])
        with self.assertRaisesRegex(ValueError, "duplicate QA"):
            archive_candidates(self.root, self.bundle, 123)

    def write_clean_reject_evidence(self, statuses=None, generated=None):
        rows = statuses if statuses is not None else [
            {"id": "CHR-ENG-IDLE", "status": "REJECT",
             "reason": "role-anchor-validation-failed"},
            {"id": "CHR-ENG-WORK", "status": "REJECT",
             "reason": "required-role-idle-candidate-rejected"},
            {"id": "CHR-ENG-REPAIR", "status": "REJECT",
             "reason": "required-role-idle-candidate-rejected"},
        ]
        (self.root / "output" / "character-sheet-report.json").write_text(
            json.dumps(rows), encoding="utf-8")
        (self.root / "output" / "generated-targets.json").write_text(
            json.dumps(generated if generated is not None else {
                "count": 0, "lane": "CONTROLLED_CHARACTER_SHEETS",
                "targets": [],
            }), encoding="utf-8")

    def test_real_all_reject_collector_without_frame_qa_is_not_workflow_failure(self):
        # 38831389791: generated-targets.json count=0, three rejected
        # character-sheet-report.json entries and NO github-qa-report.json.
        self.write_clean_reject_evidence()
        manifest = archive_candidates(self.root, self.bundle, 38831389791)
        self.assertEqual(manifest["candidate_count"], 0)
        self.assertEqual(manifest["rejected_target_ids"],
                         ["CHR-ENG-IDLE", "CHR-ENG-WORK", "CHR-ENG-REPAIR"])
        self.assertFalse(manifest["automatic_semantic_approval"])
        self.assertFalse(manifest["automatic_runtime_promotion"])
        self.assertFalse(self.bundle.exists())

    def test_missing_frame_qa_with_png_fails_closed_even_if_rejects_claimed(self):
        self.write_clean_reject_evidence()
        self.write_file("zte_chr_eng_work_final.png")
        with self.assertRaisesRegex(ValueError, "missing technical QA report"):
            archive_candidates(self.root, self.bundle, 123)

    def test_missing_frame_qa_without_rejection_proof_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "complete rejection evidence"):
            archive_candidates(self.root, self.bundle, 123)

    def test_malformed_all_rejected_proof_cannot_silently_skip_archive(self):
        invalid = [
            [{"id": "CHR-ENG-WORK", "status": "PASS"}],
            [{"id": "CHR-ENG-WORK", "status": "REJECT"},
             {"id": "CHR-ENG-WORK", "status": "REJECT"}],
            [{"id": "UNEXPECTED-ID", "status": "REJECT"}],
            [],
        ]
        for records in invalid:
            with self.subTest(records=records):
                self.write_clean_reject_evidence(statuses=records)
                with self.assertRaises(ValueError):
                    archive_candidates(self.root, self.bundle, 123)
                self.assertFalse(self.bundle.exists())

    def test_missing_qa_reject_requires_zero_produced_target_manifest(self):
        self.write_clean_reject_evidence(generated={
            "count": 1, "lane": "CONTROLLED_CHARACTER_SHEETS",
            "targets": [{"id": "CHR-ENG-WORK"}],
        })
        with self.assertRaisesRegex(ValueError, "not cleanly rejected"):
            archive_candidates(self.root, self.bundle, 123)

    def test_rejected_only_writes_no_release_asset(self):
        self.write_qa([{"file": "zte_chr_eng_repair_final.png", "pass": False}])
        manifest = archive_candidates(self.root, self.bundle, 123)
        self.assertEqual(manifest["candidate_count"], 0)
        self.assertFalse(self.bundle.exists())


if __name__ == "__main__":
    unittest.main()
