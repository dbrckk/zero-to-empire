from pathlib import Path
import tempfile
import unittest

from tools.assets.manifest import ManifestError, load_manifest, require_asset


class ManifestTest(unittest.TestCase):
    def write_manifest(self, text: str) -> Path:
        handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False)
        handle.write(text)
        handle.close()
        return Path(handle.name)

    def test_parses_exact_runtime_mapping(self):
        path = self.write_manifest(
            "| ID | Asset | Description | Runtime target | Status |\n"
            "|---|---|---|---|---|\n"
            "| ONB-00 | Onboarding step 0 | Power-core ignition illustration. | `app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp` | TODO |\n"
        )
        asset = load_manifest(path)["ONB-00"]
        self.assertEqual(
            asset.runtime_path,
            "app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp",
        )
        self.assertEqual(asset.status, "TODO")

    def test_unknown_id_is_rejected(self):
        path = self.write_manifest(
            "| ID | Asset | Description | Runtime target | Status |\n"
            "|---|---|---|---|---|\n"
            "| ONB-00 | Onboarding step 0 | Core illustration. | `app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp` | TODO |\n"
        )
        with self.assertRaises(ManifestError):
            require_asset(load_manifest(path), "ONB-99")

    def test_duplicate_id_is_rejected(self):
        path = self.write_manifest(
            "| ID | Asset | Description | Runtime target | Status |\n"
            "|---|---|---|---|---|\n"
            "| ONB-00 | First | One. | `app/src/main/res/drawable-nodpi/one.webp` | TODO |\n"
            "| ONB-00 | Second | Two. | `app/src/main/res/drawable-nodpi/two.webp` | TODO |\n"
        )
        with self.assertRaises(ManifestError):
            load_manifest(path)

    def test_real_manifest_preserves_known_business_mapping(self):
        assets = load_manifest(Path("docs/art/FINAL_AAA_SPRITE_MANIFEST.md"))
        asset = require_asset(assets, "BLD-00-T0")
        self.assertEqual(
            asset.runtime_path,
            "app/src/main/res/drawable-nodpi/zte_business_00_t0_final.webp",
        )
        self.assertEqual(asset.status, "DONE")


if __name__ == "__main__":
    unittest.main()
