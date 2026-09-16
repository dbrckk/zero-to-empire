import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

from tools.assets.manifest import ManifestAsset
from tools.assets.metadata import CandidateMetadata, sha256_file, write_metadata
from tools.assets.qa_report import build_report, write_report


ASSET = ManifestAsset(
    id="ONB-00",
    name="Onboarding step 0",
    description="Power-core ignition illustration.",
    runtime_path="app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp",
    status="TODO",
)


class QaReportTest(unittest.TestCase):
    def candidate_dir(self, review: str = "pending") -> Path:
        directory = Path(tempfile.mkdtemp())
        image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle((88, 78, 168, 178), fill=(220, 170, 80, 255))
        candidate = directory / "candidate.png"
        image.save(candidate, "PNG")
        metadata = CandidateMetadata(
            manifest_id=ASSET.id,
            semantic_role=ASSET.description,
            runtime_path=ASSET.runtime_path,
            source_type="generated",
            provider="fake-provider",
            source_url=None,
            license="generated-test",
            prompt_sha256="a" * 64,
            asset_sha256=sha256_file(candidate),
            review=review,
        )
        write_metadata(directory / "metadata.json", metadata)
        return directory

    def test_pending_semantic_review_can_never_be_approved(self):
        report = build_report(ASSET, self.candidate_dir("pending"))
        self.assertEqual(report["technical_status"], "pass")
        self.assertEqual(report["semantic_review"], "pending")
        self.assertFalse(report["approved"])
        self.assertEqual(report["runtime_path"], ASSET.runtime_path)
        self.assertIn("alpha_coverage", report["metrics"])
        self.assertIn("dominant_component", report["metrics"])

    def test_accepted_semantics_plus_technical_pass_is_approved(self):
        report = build_report(ASSET, self.candidate_dir("accepted"))
        self.assertTrue(report["approved"])

    def test_report_json_is_stable(self):
        directory = self.candidate_dir("pending")
        path = write_report(directory, build_report(ASSET, directory))
        text = path.read_text(encoding="utf-8")
        self.assertTrue(text.endswith("\n"))
        data = json.loads(text)
        self.assertEqual(data["manifest_id"], "ONB-00")


if __name__ == "__main__":
    unittest.main()
