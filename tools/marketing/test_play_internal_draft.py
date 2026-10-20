#!/usr/bin/env python3
"""Offline security regression tests for the Google Play internal draft gate."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from play_internal_draft import (
    PACKAGE, BUNDLE_REL, SOURCE_WORKFLOW, verify_artifact, verify_run,
)

SHA = "a" * 40
REPO = "dbrckk/zero-to-empire"


def run_info(**overrides):
    run = {
        "status": "completed", "conclusion": "success",
        "event": "workflow_dispatch", "head_branch": "main",
        "repository": {"full_name": REPO},
        "path": SOURCE_WORKFLOW + "@main",
        "head_sha": SHA,
    }
    run.update(overrides)
    return run


def synthetic_release(root: Path, source_sha: str = SHA) -> Path:
    bundle = root / BUNDLE_REL
    bundle.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(bundle, "w") as z:
        for path in (
            "base/manifest/AndroidManifest.xml",
            "base/dex/classes.dex",
            "BundleConfig.pb",
        ):
            z.writestr(path, b"fixture")
    (root / "production-release-metadata.txt").write_text(
        "application_id=" + PACKAGE + "\nversion_code=1\nversion_name=1.0.0\n"
        "git_sha=" + source_sha + "\n",
        encoding="utf-8",
    )
    digest = hashlib.sha256(bundle.read_bytes()).hexdigest()
    (root / "production-aab.sha256").write_text(
        digest + "  " + BUNDLE_REL.as_posix() + "\n", encoding="utf-8",
    )
    (root / "production-signature-validation.txt").write_text(
        "jar verified.\nupload_cert_sha256=" + "AA:" * 31 + "AA\n",
        encoding="utf-8",
    )
    (root / "production-release-validation.txt").write_text(
        "PRODUCTION_RELEASE_GATE_PASS=1\n", encoding="utf-8",
    )
    return bundle


class PlayInternalDraftTests(unittest.TestCase):
    def test_accept_good_signed_release_metadata(self):
        with tempfile.TemporaryDirectory() as t:
            synthetic_release(Path(t))
            result = verify_artifact(Path(t), run_info(), REPO)
            self.assertEqual(result["version_code"], 1)
            self.assertEqual(result["package"], PACKAGE)

    def test_reject_forged_source_sha(self):
        with tempfile.TemporaryDirectory() as t:
            synthetic_release(Path(t), "b" * 40)
            with self.assertRaisesRegex(ValueError, "source SHA"):
                verify_artifact(Path(t), run_info(), REPO)

    def test_reject_unsigned_or_failed_workflow(self):
        for value in ("failure", "cancelled", None):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    verify_run(run_info(conclusion=value), REPO)

    def test_reject_wrong_workflow(self):
        with self.assertRaisesRegex(ValueError, "Not a Production"):
            verify_run(run_info(path=".github/workflows/android.yml@main"), REPO)

    def test_reject_other_repository(self):
        with self.assertRaisesRegex(ValueError, "repository differs"):
            verify_run(run_info(), "someone/other-game")

    def test_reject_non_main(self):
        with self.assertRaisesRegex(ValueError, "must come from main"):
            verify_run(run_info(head_branch="experimental"), REPO)

    def test_reject_untrusted_artifact_hash(self):
        with tempfile.TemporaryDirectory() as t:
            bundle = synthetic_release(Path(t))
            with bundle.open("ab") as f:
                f.write(b"tampered")
            with self.assertRaisesRegex(ValueError, "SHA256"):
                verify_artifact(Path(t), run_info(), REPO)

    def test_reject_missing_signing_evidence(self):
        with tempfile.TemporaryDirectory() as t:
            synthetic_release(Path(t))
            (Path(t) / "production-signature-validation.txt").unlink()
            with self.assertRaisesRegex(ValueError, "Missing signed release evidence"):
                verify_artifact(Path(t), run_info(), REPO)

    def test_reject_wrong_version_code(self):
        with tempfile.TemporaryDirectory() as t:
            synthetic_release(Path(t))
            p = Path(t) / "production-release-metadata.txt"
            p.write_text(p.read_text().replace("version_code=1", "version_code=2100000001"))
            with self.assertRaisesRegex(ValueError, "versionCode"):
                verify_artifact(Path(t), run_info(), REPO)

    def test_reject_missing_required_base_dex(self):
        with tempfile.TemporaryDirectory() as t:
            synthetic_release(Path(t))
            bundle = Path(t) / BUNDLE_REL
            with ZipFile(bundle, "w") as z:
                z.writestr("base/manifest/AndroidManifest.xml", "fixture")
                z.writestr("BundleConfig.pb", "fixture")
            digest = hashlib.sha256(bundle.read_bytes()).hexdigest()
            (Path(t) / "production-aab.sha256").write_text(
                digest + "  " + BUNDLE_REL.as_posix() + "\n"
            )
            with self.assertRaisesRegex(ValueError, "modules"):
                verify_artifact(Path(t), run_info(), REPO)


if __name__ == "__main__":
    unittest.main()
