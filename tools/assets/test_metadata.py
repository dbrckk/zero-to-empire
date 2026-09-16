import tempfile
import unittest
from pathlib import Path

from tools.assets.manifest import ManifestAsset
from tools.assets.metadata import (
    CandidateMetadata,
    MetadataError,
    sha256_file,
    write_metadata,
)


ASSET = ManifestAsset(
    id="ONB-00",
    name="Onboarding step 0",
    description="Power-core ignition illustration.",
    runtime_path="app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp",
    status="TODO",
)


def valid_metadata(**overrides) -> CandidateMetadata:
    values = dict(
        manifest_id="ONB-00",
        semantic_role=ASSET.description,
        runtime_path=ASSET.runtime_path,
        source_type="generated",
        provider="hf-static",
        source_url=None,
        license="generated",
        prompt_sha256="a" * 64,
        asset_sha256="b" * 64,
        review="pending",
    )
    values.update(overrides)
    return CandidateMetadata(**values)


class MetadataTest(unittest.TestCase):
    def test_exact_manifest_mapping_is_accepted(self):
        valid_metadata().validate_against(ASSET)

    def test_runtime_path_spoof_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(
                runtime_path="app/src/main/res/drawable-nodpi/zte_wrong.webp"
            ).validate_against(ASSET)

    def test_manifest_id_spoof_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(manifest_id="ONB-99").validate_against(ASSET)

    def test_semantic_role_spoof_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(semantic_role="unrelated store icon").validate_against(ASSET)

    def test_invalid_review_state_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(review="approved").validate_against(ASSET)

    def test_invalid_source_type_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(source_type="guessed").validate_against(ASSET)

    def test_sha256_file_is_deterministic(self):
        with tempfile.NamedTemporaryFile("wb", delete=False) as handle:
            handle.write(b"zero-to-empire")
            path = Path(handle.name)
        first = sha256_file(path)
        second = sha256_file(path)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 64)

    def test_metadata_json_is_stable_and_sorted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "metadata.json"
            write_metadata(path, valid_metadata())
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.endswith("\n"))
            self.assertLess(text.index('"asset_sha256"'), text.index('"manifest_id"'))


if __name__ == "__main__":
    unittest.main()
