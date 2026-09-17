from pathlib import Path
import json
import tempfile
import unittest

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


def valid_metadata(**overrides):
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
        meta = valid_metadata(
            runtime_path="app/src/main/res/drawable-nodpi/zte_wrong.webp"
        )
        with self.assertRaises(MetadataError):
            meta.validate_against(ASSET)

    def test_manifest_id_spoof_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(manifest_id="ONB-01").validate_against(ASSET)

    def test_semantic_role_spoof_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(semantic_role="Different meaning").validate_against(ASSET)

    def test_invalid_review_state_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(review="approved").validate_against(ASSET)

    def test_invalid_source_type_is_rejected(self):
        with self.assertRaises(MetadataError):
            valid_metadata(source_type="scraped").validate_against(ASSET)

    def test_sha256_file_is_deterministic(self):
        with tempfile.NamedTemporaryFile(delete=False) as handle:
            handle.write(b"zero-to-empire")
            path = Path(handle.name)
        self.assertEqual(
            sha256_file(path),
            "0bb4d5bfeca2c346f313004c18b4a28e0df3b815f87728a9f03a57f348316da4",
        )

    def test_metadata_json_is_stable_and_sorted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "metadata.json"
            meta = valid_metadata()
            write_metadata(path, meta)
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.endswith("\n"))
            payload = json.loads(text)
            self.assertEqual(payload["manifest_id"], "ONB-00")
            self.assertEqual(payload["runtime_path"], ASSET.runtime_path)
            self.assertEqual(text, json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    unittest.main()
