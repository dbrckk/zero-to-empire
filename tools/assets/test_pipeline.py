import tempfile
import unittest
from pathlib import Path

from PIL import Image

from tools.assets.manifest import ManifestAsset
from tools.assets.pipeline import build_candidate


class FakeProvider:
    name = "fake-provider"
    source_type = "generated"
    license = "test-only"

    def generate(self, asset: ManifestAsset, prompt: str) -> Image.Image:
        image = Image.new("RGB", (256, 256), (0, 0, 0))
        for y in range(78, 178):
            for x in range(88, 168):
                image.putpixel((x, y), (230, 180, 90))
        return image


class UnifiedCandidatePipelineTest(unittest.TestCase):
    def test_build_candidate_writes_review_artifacts_without_publishing_runtime_asset(self):
        asset = ManifestAsset(
            "PRP-TEST",
            "Test Prop",
            "single authored industrial test prop",
            "app/src/main/res/drawable-nodpi/prop_test.png",
            "TODO",
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            runtime = root / asset.runtime_path
            result = build_candidate(
                asset=asset,
                provider=FakeProvider(),
                prompt="test prop on black background",
                target_side=1024,
                candidate_root=root / "art/incoming/candidates",
            )

            self.assertEqual(result.image_path.name, "candidate.png")
            self.assertEqual(result.metadata_path.name, "metadata.json")
            self.assertTrue(result.image_path.is_file())
            self.assertTrue(result.metadata_path.is_file())
            self.assertFalse(runtime.exists())
            self.assertIn("PRP-TEST", result.image_path.parts)

    def test_build_candidate_rejects_non_todo_manifest_asset(self):
        asset = ManifestAsset("PRP-DONE", "Done", "done prop", "drawable/done.png", "DONE")
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "not TODO"):
                build_candidate(
                    asset=asset,
                    provider=FakeProvider(),
                    prompt="done",
                    target_side=1024,
                    candidate_root=Path(tmp),
                )


if __name__ == "__main__":
    unittest.main()
