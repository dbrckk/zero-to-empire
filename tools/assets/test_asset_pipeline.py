import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

from tools.assets.asset_pipeline import prepare_candidate
from tools.assets.manifest import ManifestError
from tools.assets.providers import ProviderResult


MANIFEST_TEXT = """\
| ID | Asset | Description | Runtime target | Status |
|---|---|---|---|---|
| ONB-00 | Onboarding step 0 | Power-core ignition illustration. | `app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp` | TODO |
| ONB-01 | Onboarding step 1 | Production illustration. | `app/src/main/res/drawable-nodpi/zte_onboarding_01_final.webp` | TODO |
"""


class FakeProvider:
    def __init__(self):
        self.assets = []

    def generate(self, asset, prompt):
        self.assets.append(asset.id)
        image = Image.new("RGB", (256, 256), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle((88, 78, 168, 178), fill=(220, 170, 80))
        return ProviderResult(
            image=image,
            provider="fake-provider",
            source_url=None,
            license="generated-test",
        )


class AssetPipelineTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.manifest = self.root / "manifest.md"
        self.manifest.write_text(MANIFEST_TEXT, encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_unknown_id_fails_before_provider_is_called(self):
        provider = FakeProvider()
        with self.assertRaises(ManifestError):
            prepare_candidate("ONB-99", provider, self.root, self.manifest)
        self.assertEqual(provider.assets, [])

    def test_only_requested_id_is_generated(self):
        provider = FakeProvider()
        prepare_candidate("ONB-01", provider, self.root, self.manifest)
        self.assertEqual(provider.assets, ["ONB-01"])

    def test_candidate_is_id_scoped_and_never_written_to_runtime(self):
        provider = FakeProvider()
        directory = prepare_candidate("ONB-00", provider, self.root, self.manifest)
        self.assertEqual(directory, self.root / "art/incoming/assets/ONB-00")
        self.assertTrue((directory / "candidate.png").is_file())
        self.assertTrue((directory / "metadata.json").is_file())
        self.assertFalse((self.root / "app/src/main/res").exists())

    def test_metadata_preserves_authoritative_runtime_mapping(self):
        provider = FakeProvider()
        directory = prepare_candidate("ONB-00", provider, self.root, self.manifest)
        metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
        self.assertEqual(metadata["manifest_id"], "ONB-00")
        self.assertEqual(
            metadata["runtime_path"],
            "app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp",
        )
        self.assertEqual(metadata["review"], "pending")


if __name__ == "__main__":
    unittest.main()
