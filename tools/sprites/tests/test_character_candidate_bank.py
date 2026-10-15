"""Offline regressions for durable character bank; no GPU/network required."""
from __future__ import annotations

import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build_character_candidate_bank import assemble


class CharacterBankTests(unittest.TestCase):
    def setUp(self):
        self.work = tempfile.TemporaryDirectory()
        self.addCleanup(self.work.cleanup)
        self.root = Path(self.work.name)
        self.archives = self.root / "archives"
        self.archives.mkdir()
        self.master = self.root / "master.json"
        self.output = self.root / "candidate-bank.zip"
        self.missing = "CHR-ENG-WALK"
        self.filename = "zte_chr_eng_walk_final.png"
        self.runtime = "app/src/main/res/drawable-nodpi/zte_chr_eng_walk_final.webp"
        self.rows = [
            {"id": f"ASSET-{n}", "strict_status": "DONE", "pipeline_status": "DONE"}
            for n in range(234)
        ]
        self.rows.append({
            "id": self.missing, "strict_status": "NEEDS_REVIEW",
            "pipeline_status": "AWAITING_REVIEW", "review_artifact_run_id": 123,
            "runtime": self.runtime,
            "deferred_art_warnings": ["ACTION_TRANSLATION_DOMINATES_POSE_RISK"],
        })
        self.save_master()

    def save_master(self):
        self.master.write_text(json.dumps({
            "target_total": 235, "assets": self.rows,
        }), encoding="utf-8")

    def png(self):
        picture = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
        picture.putpixel((80, 80), (12, 34, 56, 255))
        buffer = io.BytesIO()
        picture.save(buffer, "PNG")
        return buffer.getvalue()

    def source(self, content=None, run_id=123, name=None, sha=None):
        content = content if content is not None else self.png()
        name = name or self.filename
        sha = sha if sha is not None else hashlib.sha256(content).hexdigest()
        path = self.archives / f"zte-characters-{run_id}.zip"
        index = {
            "source_collector_run_id": run_id,
            "automatic_semantic_approval": False,
            "assets": [{
                "filename": name, "sha256": sha, "bytes": len(content),
                "strict_approved": False,
                "deferred_art_warnings": ["FACE_HEADGEAR_STRUCTURE_DRIFT_RISK"],
            }],
        }
        with zipfile.ZipFile(path, "w") as z:
            z.writestr("candidate-index.json", json.dumps(index))
            z.writestr("candidates/" + name, content)

    def test_complete_pack_contains_exact_verified_candidate_and_deferred_warnings(self):
        self.source()
        report = assemble(self.master, self.archives, self.output)
        self.assertTrue(report["candidate_production_complete"])
        self.assertEqual(report["production_processed"], 235)
        self.assertEqual(report["candidate_count"], 1)
        self.assertEqual(report["strict_done"], 234)
        with zipfile.ZipFile(self.output) as z:
            self.assertEqual(z.read("candidates/" + self.filename), self.png())
            saved = json.loads(z.read("candidate-bank-index.json"))
            entry = saved["bank_entries"][0]
            self.assertEqual(entry["source_collector_run_id"], 123)
            self.assertFalse(entry["strict_approved"])
            self.assertFalse(entry["runtime_promoted"])
            self.assertEqual(entry["deferred_art_warnings"],
                             ["ACTION_TRANSLATION_DOMINATES_POSE_RISK",
                              "FACE_HEADGEAR_STRUCTURE_DRIFT_RISK"])

    def test_missing_source_does_not_inflate_progress(self):
        report = assemble(self.master, self.archives, self.output)
        self.assertEqual(report["production_processed"], 234)
        self.assertFalse(report["candidate_production_complete"])
        self.assertEqual(report["missing_character_candidates"][0]["id"], self.missing)

    def test_dispatched_asset_not_counted_even_with_old_artifact(self):
        self.source()
        self.rows[-1]["pipeline_status"] = "DISPATCHED"
        self.save_master()
        result = assemble(self.master, self.archives, self.output)
        self.assertFalse(result["candidate_production_complete"])
        self.assertEqual(result["candidate_count"], 0)

    def test_wrong_source_id_is_never_accepted(self):
        self.source(run_id=124)
        report = assemble(self.master, self.archives, self.output)
        self.assertEqual(report["candidate_count"], 0)
        self.assertEqual(report["missing_character_candidates"][0]["reason"],
                         "missing-exact-source-archive")

    def test_mismatched_sha_fails_closed(self):
        self.source(sha="0" * 64)
        with self.assertRaisesRegex(ValueError, "checksum/size mismatch"):
            assemble(self.master, self.archives, self.output)

    def test_wrong_dimensions_fail_closed(self):
        buf = io.BytesIO()
        Image.new("RGBA", (256, 256)).save(buf, format="PNG")
        self.source(content=buf.getvalue())
        with self.assertRaisesRegex(ValueError, "dimensions"):
            assemble(self.master, self.archives, self.output)


if __name__ == "__main__":
    unittest.main()
