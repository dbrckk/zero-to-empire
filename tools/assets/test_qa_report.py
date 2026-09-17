import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from tools.assets.qa_report import build_candidate_qa_artifacts


class CandidateQaReportTest(unittest.TestCase):
    def make_candidate(self, root: Path) -> Path:
        candidate_dir = root / "ONB-00"
        candidate_dir.mkdir(parents=True)
        image = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
        for y in range(300, 724):
            for x in range(340, 684):
                image.putpixel((x, y), (230, 180, 90, 255))
        image.save(candidate_dir / "candidate.png")
        (candidate_dir / "metadata.json").write_text(
            json.dumps({
                "manifest_id": "ONB-00",
                "runtime_path": "app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp",
                "review": "pending",
            }),
            encoding="utf-8",
        )
        return candidate_dir

    def test_builds_machine_readable_report_and_contact_sheet(self):
        with tempfile.TemporaryDirectory() as tmp:
            candidate_dir = self.make_candidate(Path(tmp))
            report_path, sheet_path = build_candidate_qa_artifacts(candidate_dir)

            self.assertTrue(report_path.is_file())
            self.assertTrue(sheet_path.is_file())
            payload = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["manifest_id"], "ONB-00")
            self.assertEqual(payload["review"], "pending")
            self.assertEqual(payload["candidate_file"], "candidate.png")
            self.assertIn("automatic_checks", payload)
            self.assertIn("pass", payload["automatic_checks"])

    def test_missing_candidate_image_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            candidate_dir = Path(tmp) / "ONB-00"
            candidate_dir.mkdir()
            (candidate_dir / "metadata.json").write_text(
                json.dumps({"manifest_id": "ONB-00", "review": "pending"}),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(FileNotFoundError, "candidate.png"):
                build_candidate_qa_artifacts(candidate_dir)

    def test_metadata_manifest_id_must_match_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            candidate_dir = self.make_candidate(Path(tmp))
            metadata_path = candidate_dir / "metadata.json"
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            metadata["manifest_id"] = "ONB-99"
            metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "manifest_id"):
                build_candidate_qa_artifacts(candidate_dir)


if __name__ == "__main__":
    unittest.main()
