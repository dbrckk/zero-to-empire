from pathlib import Path
import tempfile
import unittest

from tools.assets.manifest import load_manifest, require_asset, ManifestError


class ManifestTest(unittest.TestCase):
    def write_manifest(self, text: str) -> Path:
        handle = tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", suffix=".md", delete=False
        )
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
            "| PRP-00 | A | First. | `a.webp` | TODO |\n"
            "| PRP-00 | B | Second. | `b.webp` | TODO |\n"
        )
        with self.assertRaises(ManifestError):
            load_manifest(path)

    def test_real_manifest_mapping_is_exact(self):
        manifest = Path("docs/art/FINAL_AAA_SPRITE_MANIFEST.md")
        asset = require_asset(load_manifest(manifest), "BLD-00-T0")
        self.assertEqual(
            asset.runtime_path,
            "app/src/main/res/drawable-nodpi/zte_business_00_t0_final.webp",
        )
        self.assertEqual(asset.status, "DONE")

    def test_real_manifest_defines_first_onboarding_authored_target(self):
        manifest = Path("docs/art/FINAL_AAA_SPRITE_MANIFEST.md")
        asset = require_asset(load_manifest(manifest), "ONB-00")
        self.assertEqual(
            asset.runtime_path,
            "app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp",
        )
        self.assertEqual(asset.status, "TODO")


if __name__ == "__main__":
    unittest.main()
