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

    def test_rejected_only_writes_no_release_asset(self):
        self.write_qa([{"file": "zte_chr_eng_repair_final.png", "pass": False}])
        manifest = archive_candidates(self.root, self.bundle, 123)
        self.assertEqual(manifest["candidate_count"], 0)
        self.assertFalse(self.bundle.exists())


if __name__ == "__main__":
    unittest.main()
