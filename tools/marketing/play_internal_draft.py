#!/usr/bin/env python3
"""Auditable, explicitly gated Google Play INTERNAL DRAFT deployment.

A successful production release run is mandatory. No production rollout, no
testers served, and no Google credentials are stored in generated artifacts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from zipfile import ZipFile

PACKAGE = "com.zerotoempire.game"
SOURCE_WORKFLOW = ".github/workflows/production-release.yml"
ARTIFACT_PREFIX = "zero-to-empire-production-"
BUNDLE_REL = Path("app/build/outputs/bundle/release/app-release.aab")
MAX_BUNDLE_BYTES = 200 * 1024 * 1024


def verify_run(run: dict, repo: str) -> str:
    """Reject unrelated, incomplete or unsigned-source GitHub workflow runs."""
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError("Invalid GitHub repository")
    if run.get("conclusion") != "success" or run.get("status") != "completed":
        raise ValueError("Production Release Gate workflow has not succeeded")
    if run.get("event") != "workflow_dispatch":
        raise ValueError("Expected manually initiated signed release workflow")
    if run.get("head_branch") != "main":
        raise ValueError("Signed bundle must come from main")
    if run.get("repository", {}).get("full_name") != repo:
        raise ValueError("Signed workflow repository differs from current repository")
    workflow_path = run.get("path", "").split("@", 1)[0]
    if workflow_path != SOURCE_WORKFLOW:
        raise ValueError("Not a Production Release Gate workflow run")
    sha = run.get("head_sha", "")
    if not re.fullmatch(r"[a-fA-F0-9]{40}", sha):
        raise ValueError("Invalid signed release source SHA")
    return sha.lower()


def read_properties(path: Path) -> dict[str, str]:
    props = {}
    for row in path.read_text(encoding="utf-8").splitlines():
        if not row.strip():
            continue
        if "=" not in row:
            raise ValueError("Malformed production metadata")
        name, value = row.split("=", 1)
        if name in props:
            raise ValueError("Duplicate production metadata field")
        props[name] = value
    return props


def verify_artifact(directory: Path, run: dict, repo: str) -> dict:
    source_sha = verify_run(run, repo)
    directory = directory.resolve(strict=True)
    artifact = directory / BUNDLE_REL
    metadata_path = directory / "production-release-metadata.txt"
    digest_path = directory / "production-aab.sha256"
    signature_path = directory / "production-signature-validation.txt"
    gate_path = directory / "production-release-validation.txt"
    for path in (artifact, metadata_path, digest_path, signature_path, gate_path):
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"Missing signed release evidence: {path.name}")
    if artifact.stat().st_size > MAX_BUNDLE_BYTES:
        raise ValueError("Bundle exceeds 200 MiB upload safety limit")
    metadata = read_properties(metadata_path)
    code = metadata.get("version_code", "")
    name = metadata.get("version_name", "")
    if metadata.get("git_sha", "").lower() != source_sha:
        raise ValueError("Signed artifact source SHA differs from release workflow")
    if metadata.get("application_id") != PACKAGE:
        raise ValueError("Application ID differs from release package")
    if not re.fullmatch(r"[1-9][0-9]{0,9}", code) or int(code) > 2100000000:
        raise ValueError("Invalid Google Play versionCode")
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:[.-][A-Za-z0-9]+)*", name):
        raise ValueError("Invalid release versionName")
    digest_line = digest_path.read_text(encoding="utf-8").strip()
    match = re.fullmatch(
        r"([a-fA-F0-9]{64})\s+\*?app/build/outputs/bundle/release/app-release\.aab",
        digest_line,
    )
    if not match:
        raise ValueError("AAB SHA256 manifest has an unexpected path or format")
    actual_digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    if match.group(1).lower() != actual_digest:
        raise ValueError("Signed AAB SHA256 integrity failure")
    if "PRODUCTION_RELEASE_GATE_PASS=1" not in gate_path.read_text(encoding="utf-8"):
        raise ValueError("Signed release gate evidence missing")
    signature = signature_path.read_text(encoding="utf-8")
    if "jar verified." not in signature or not re.search(
        r"upload_cert_sha256=[0-9A-Fa-f:]{64,95}", signature
    ):
        raise ValueError("Upload signing certificate evidence missing")
    with ZipFile(artifact) as bundle:
        if bundle.testzip() is not None:
            raise ValueError("Signed bundle ZIP integrity failed")
        required = {
            "base/manifest/AndroidManifest.xml",
            "base/dex/classes.dex",
            "BundleConfig.pb",
        }
        if not required.issubset(bundle.namelist()):
            raise ValueError("Required Play bundle modules are missing")
    return {
        "package": PACKAGE,
        "version_code": int(code),
        "version_name": name,
        "source_sha": source_sha,
        "bundle_sha256": actual_digest,
        "bundle_path": str(artifact),
    }


def draft_internal_release(info: dict, service_account_json: str) -> dict:
    """May modify ONLY the Google Play internal test track, as a non-serving draft."""
    if not service_account_json:
        raise ValueError("GOOGLE_PLAY_SERVICE_ACCOUNT_JSON repository secret is missing")
    creds_dict = json.loads(service_account_json)
    if creds_dict.get("type") != "service_account" or not creds_dict.get("private_key"):
        raise ValueError("Expected a Google Cloud service-account JSON key")
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from googleapiclient.errors import HttpError

    creds = service_account.Credentials.from_service_account_info(
        creds_dict, scopes=["https://www.googleapis.com/auth/androidpublisher"]
    )
    client = build("androidpublisher", "v3", credentials=creds, cache_discovery=False)
    edits = client.edits()
    edit_id = edits.insert(packageName=PACKAGE, body={}).execute()["id"]
    try:
        existing = edits.tracks().get(
            packageName=PACKAGE, editId=edit_id, track="internal"
        ).execute()
    except HttpError as exc:
        if exc.resp.status != 404:
            raise
        existing = {"releases": []}
    if existing.get("releases"):
        raise ValueError(
            "Internal track already has releases: refusing to overwrite them; "
            "review existing track in Play Console first"
        )
    media = MediaFileUpload(
        info["bundle_path"],
        mimetype="application/octet-stream",
        resumable=True,
        chunksize=5 * 1024 * 1024,
    )
    result = edits.bundles().upload(
        packageName=PACKAGE, editId=edit_id, media_body=media
    ).execute(num_retries=3)
    if int(result.get("versionCode", -1)) != info["version_code"]:
        raise ValueError("Google Play uploaded versionCode differs from signed AAB")
    remote_sha = result.get("sha256", "").lower()
    if remote_sha and remote_sha != info["bundle_sha256"]:
        raise ValueError("Google Play reported a different SHA256 for uploaded AAB")
    release = {
        "name": info["version_name"],
        "versionCodes": [str(info["version_code"])],
        "status": "draft",
        "releaseNotes": [
            {"language": "fr-FR", "text": "Première version de ZERO → EMPIRE : construction, automatisation et Ascension."},
            {"language": "en-US", "text": "Initial release: businesses, automation, offline progress and Ascension."},
        ],
    }
    edits.tracks().update(
        packageName=PACKAGE,
        editId=edit_id,
        track="internal",
        body={"track": "internal", "releases": [release]},
    ).execute()
    # Never replace in-review changes or roll out to testers/public automatically.
    edits.commit(
        packageName=PACKAGE,
        editId=edit_id,
        changesNotSentForReview=True,
        changesInReviewBehavior="ERROR_IF_IN_REVIEW",
    ).execute()
    return {"track": "internal", "status": "draft", "version_code": info["version_code"]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-json", type=Path, required=True)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--mode", choices=("verify_only", "create_internal_draft"), default="verify_only")
    parser.add_argument("--confirmation", default="")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    run = json.loads(args.run_json.read_text(encoding="utf-8"))
    info = verify_artifact(args.artifact_dir, run, args.repository)
    report = {
        "schema": 1, "repository": args.repository,
        "package": info["package"], "source_sha": info["source_sha"],
        "version_code": info["version_code"], "version_name": info["version_name"],
        "bundle_sha256": info["bundle_sha256"],
        "signature_evidence_verified": True,
        "play_internal_draft_committed": False,
        "public_release_submitted": False,
    }
    if args.mode == "create_internal_draft":
        if args.confirmation != "CREATE_INTERNAL_DRAFT":
            raise ValueError("Explicit confirmation CREATE_INTERNAL_DRAFT is required")
        result = draft_internal_release(
            info, os.environ.get("GOOGLE_PLAY_SERVICE_ACCOUNT_JSON", "")
        )
        report["play_internal_draft_committed"] = result["status"] == "draft"
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        "PLAY_INTERNAL_RESULT=" +
        ("DRAFT_COMMITTED_NOT_SERVED" if report["play_internal_draft_committed"]
         else "SIGNED_ARTIFACT_VALIDATED_ONLY")
    )
    print("SIGNED_AAB_SHA256=" + info["bundle_sha256"])


if __name__ == "__main__":
    main()
