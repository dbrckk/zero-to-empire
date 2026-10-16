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

    def authored_original(self):
        original = self.root / "original"
        (original / "candidates").mkdir(parents=True)
        (original / "src_svg" / "ENG" / "WALK").mkdir(parents=True)
        manifest = []
        qa = []
        counts = {"IDLE": 6, "WALK": 8, "WORK": 10,
                  "CARRY": 8, "REPAIR": 10, "CELEB": 8}
        for role in ("OP", "LOG", "ENG"):
            for action, frames in counts.items():
                asset_id = f"CHR-{role}-{action}"
                manifest.append({
                    "id": asset_id, "file": f"zte_chr_{role.lower()}_{action.lower()}_final.png",
                    "frames": frames, "role": role, "action": action,
                    "strict_approved": False, "context_only": False,
                })
                qa.append({
                    "id": asset_id, "frames": frames,
                    "technical_geometry_pass": True, "semantic_approved": False,
                    "android_validated": False, "strict_done_added": 0,
                })
        (original / "creation-manifest.json").write_text(
            json.dumps({"review_only": True, "strict_done_added": 0,
                        "assets": manifest}))
        (original / "candidate-qa.json").write_text(
            json.dumps({"review_only": True, "assets": qa}))
        picture = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
        from PIL import ImageDraw
        for i in range(8):
            x = (i % 4) * 256
            y = (i // 4) * 256
            ImageDraw.Draw(picture).rounded_rectangle(
                (x + 78 + i % 3, y + 34, x + 186 + i % 3, y + 218),
                radius=10, fill=(40, 95, 120, 255))
            (original / "src_svg" / "ENG" / "WALK" / f"{i:02d}.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg"></svg>')
        picture.save(original / "candidates" / self.filename, "PNG")
        return original

    def test_local_original_completes_candidate_scope_while_remote_is_dispatched(self):
        local = self.authored_original()
        self.rows[-1]["pipeline_status"] = "DISPATCHED"
        self.save_master()
        master_before = self.master.read_bytes()
        report = assemble(self.master, self.archives, self.output, local_original=local)
        self.assertTrue(report["candidate_production_complete"])
        self.assertEqual(report["production_processed"], 235)
        self.assertEqual(report["canonical_queue_production_processed"], 234)
        self.assertEqual(report["local_original_fallback_ids"], [self.missing])
        entry = report["bank_entries"][0]
        self.assertEqual(entry["source_type"], "repo-local-original")
        self.assertEqual(entry["editable_pose_count"], 8)
        self.assertTrue(entry["editable_source"].endswith("/ENG/WALK"))
        self.assertNotIn("source_collector_run_id", entry)
        self.assertFalse(entry["strict_approved"])
        self.assertFalse(entry["runtime_promoted"])
        self.assertEqual(self.master.read_bytes(), master_before)
        with zipfile.ZipFile(self.output) as archive:
            self.assertEqual(archive.read("candidates/" + self.filename),
                             (local / "candidates" / self.filename).read_bytes())

    def test_prefer_real_collected_candidate_to_local_original(self):
        local = self.authored_original()
        self.source()
        report = assemble(self.master, self.archives, self.output, local_original=local)
        entry = report["bank_entries"][0]
        self.assertEqual(entry["source_type"], "collected-kaggle")
        self.assertEqual(entry["source_collector_run_id"], 123)
        self.assertEqual(report["local_original_fallback_ids"], [])

    def complete_eng_original(self):
        original = self.authored_original()
        counts = {"IDLE": 6, "WORK": 10, "CARRY": 8,
                  "REPAIR": 10, "CELEB": 8}
        from PIL import ImageDraw
        for action, frames in counts.items():
            atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
            folder = original / "src_svg" / "ENG" / action
            folder.mkdir(parents=True)
            for i in range(frames):
                x = (i % 4) * 256
                y = (i // 4) * 256
                ImageDraw.Draw(atlas).rounded_rectangle(
                    (x + 78 + i % 3, y + 34, x + 186 + i % 3, y + 218),
                    radius=10, fill=(40, 95, 120, 255))
                (folder / f"{i:02d}.svg").write_text(
                    '<svg xmlns="http://www.w3.org/2000/svg"></svg>')
            atlas.save(original / "candidates" /
                       f"zte_chr_eng_{action.lower()}_final.png", "PNG")
        return original

    def test_explicit_engineer_cohort_creates_separate_six_action_review_bank(self):
        local = self.complete_eng_original()
        self.rows = [
            {"id": f"ASSET-{n}", "strict_status": "DONE", "pipeline_status": "DONE"}
            for n in range(229)
        ]
        for action in ("IDLE", "WALK", "WORK", "CARRY", "REPAIR", "CELEB"):
            self.rows.append({
                "id": "CHR-ENG-" + action,
                "strict_status": "NEEDS_REVIEW",
                "pipeline_status": "AWAITING_REVIEW",
                "review_artifact_run_id": 123,
                "runtime": "app/src/main/res/drawable-nodpi/"
                           f"zte_chr_eng_{action.lower()}_final.webp",
            })
        self.save_master()
        self.source()
        normal_path = self.root / "canonical.zip"
        normal = assemble(self.master, self.archives, normal_path,
                          local_original=local)
        self.assertEqual(
            next(x for x in normal["bank_entries"] if x["id"] == self.missing)["source_type"],
            "collected-kaggle")
        original_master = self.master.read_bytes()
        preferred = assemble(
            self.master, self.archives, self.output,
            local_original=local, engineer_role_coherent_review=True)
        self.assertEqual(preferred["source_selection_profile"], "engineer-local-role-review")
        self.assertEqual(len(preferred["local_original_preferred_ids"]), 6)
        self.assertEqual(preferred["local_original_fallback_ids"], [ ])
        self.assertEqual(preferred["strict_done"], 229)
        self.assertTrue(preferred["candidate_production_complete"])
        self.assertEqual(preferred["production_processed"], 235)
        self.assertEqual(self.master.read_bytes(), original_master)
        with zipfile.ZipFile(normal_path) as unchanged:
            self.assertEqual(unchanged.read("candidates/" + self.filename), self.png())
        self.assertTrue(all(x["source_type"] == "repo-local-original"
                            for x in preferred["bank_entries"]))
        self.assertTrue(all(x["strict_approved"] is False and
                            x["runtime_promoted"] is False
                            for x in preferred["bank_entries"]))
        with zipfile.ZipFile(self.output) as alternative:
            for action in ("IDLE", "WALK", "WORK", "CARRY", "REPAIR", "CELEB"):
                name = f"zte_chr_eng_{action.lower()}_final.png"
                self.assertEqual(
                    alternative.read("candidates/" + name),
                    (local / "candidates" / name).read_bytes())

    def test_engineer_coherent_option_rejects_incomplete_role_or_missing_source(self):
        with self.assertRaisesRegex(ValueError, "requires verified local originals"):
            assemble(self.master, self.archives, self.output,
                     engineer_role_coherent_review=True)
        local = self.complete_eng_original()
        with self.assertRaisesRegex(ValueError, "six pending local ENG actions"):
            assemble(self.master, self.archives, self.output,
                     local_original=local, engineer_role_coherent_review=True)
        self.assertFalse(self.output.exists())

    def test_local_manifest_claims_do_not_waive_technical_frame_QA(self):
        local = self.authored_original()
        Image.new("RGBA", (1024, 1024), (0, 0, 0, 0)).save(
            local / "candidates" / self.filename)
        with self.assertRaisesRegex(ValueError, "independent frame/alpha QA"):
            assemble(self.master, self.archives, self.output, local_original=local)

    def test_local_original_requires_all_editable_svg_frames(self):
        local = self.authored_original()
        (local / "src_svg" / "ENG" / "WALK" / "01.svg").unlink()
        with self.assertRaisesRegex(ValueError, "Missing editable authored SVG"):
            assemble(self.master, self.archives, self.output, local_original=local)

    def test_local_original_fails_closed_when_qa_claims_artistic_approval(self):
        local = self.authored_original()
        qa_file = local / "candidate-qa.json"
        data = json.loads(qa_file.read_text())
        for item in data["assets"]:
            if item["id"] == self.missing:
                item["semantic_approved"] = True
        qa_file.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Untrusted local manifest/QA"):
            assemble(self.master, self.archives, self.output, local_original=local)


if __name__ == "__main__":
    unittest.main()
