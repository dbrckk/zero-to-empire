#!/usr/bin/env python3
"""Build an auditable Google Play Console upload media pack, without any secrets."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[2]
SCREEN = Path("marketing/play-store-assets/screenshots")
FILES = [
    Path("marketing/play-store-assets/zero-to-empire-icon-512.png"),
    Path("marketing/play-store-assets/zero-to-empire-feature-1024x500.png"),
    *[SCREEN / (name + ".png") for name in
      ("01-empire", "02-managers", "03-upgrades", "04-goals", "05-store")],
    Path("marketing/play-store-assets/screenshots/screenshots-manifest.json"),
    Path("marketing/play-store-assets/store-artwork-manifest.json"),
    Path("marketing/play-store-listing.md"),
    Path("marketing/play-store-listing-fr-FR.md"),
    Path("marketing/privacy-policy.md"),
    Path("marketing/data-safety.md"),
    Path("marketing/PLAY_STORE_RELEASE_RUNBOOK.md"),
]

README = """ZERO → EMPIRE — GOOGLE PLAY UPLOAD MEDIA PACK
=============================================
This pack contains five actual, cropped Android emulator gameplay screenshots
(1080x2160, 24-bit RGB PNG), the final Play launcher icon (512x512 RGBA),
the 1024x500 RGB feature graphic, English and French listing copy, and
the privacy/Data Safety working documents.

1) In Google Play Console, create the game using package
   com.zerotoempire.game, then upload the icon, feature image and screenshots.
2) Copy language-specific fields from the two play-store-listing Markdown files.
3) Use the PUBLIC URL of the hosted privacy policy, not this .md file.
4) Complete ads, purchases, content rating, audiences, data safety, developer
   contact details and testing requirements. Product IDs must match the app.
5) Build a SIGNED production AAB using the protected Production Release Gate,
   configured with your own upload keystore and real AdMob IDs.
6) Distribute the AAB via Play internal/closed testing, check purchases,
   restore, consent, ads, crashes and physical-device performance.
7) Only then submit to Google Play. This pack is NOT proof of Play approval.

Screenshots originate from a successful DEBUG Android emulator run. No invented
UI, financial statistics, rankings, testimonial or promotional claims are added.
Check the attached JSON manifest for per-file content hashes and source commits.

This archive intentionally contains NO Google Play signing keys, AdMob account
secrets, passwords, access tokens or production bundle.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    q=json.loads((ROOT/"art/production/master-asset-queue.json").read_text())
    assert len(q["assets"])==235
    assert sum(row["strict_status"]=="DONE" for row in q["assets"])==235
    evidence=json.loads((ROOT/SCREEN/"screenshots-manifest.json").read_text())
    assert evidence["screenshot_count"]==5
    preflight=ROOT/"marketing/play-store-assets/play-release-preflight.json"
    if preflight.is_file():
        p=json.loads(preflight.read_text())
        issues=[k for k,v in p["repo_checks"].items()
                if k!="production_signing_and_ad_ids_configured" and not v]
        if issues: raise ValueError(f"Preflight media/policy failures: {issues}")
    manifest={
        "format":"zero-to-empire-play-console-media-pack-v1",
        "canonical_assets_approved":235,
        "source_commit":os.getenv("GITHUB_SHA","local"),
        "signed_aab_included":False,
        "play_console_submitted":False,
        "play_console_approved":False,
        "screenshots_source_run":evidence["source_run_id"],
        "files":[]
    }
    for rel in FILES:
        p=ROOT/rel
        if not p.is_file() or p.stat().st_size==0: raise FileNotFoundError(rel)
        manifest["files"].append({
            "path":rel.as_posix(),
            "size_bytes":p.stat().st_size,
            "sha256":hashlib.sha256(p.read_bytes()).hexdigest()
        })
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(args.out,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for rel in FILES:
            p=ROOT/rel
            zi=zipfile.ZipInfo(rel.as_posix(),date_time=(2026,10,19,0,0,0))
            zi.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(zi,p.read_bytes())
        archive.writestr("READ_ME_FIRST.txt", README)
        archive.writestr("submission-pack-manifest.json",
                         json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
    with zipfile.ZipFile(args.out) as archive:
        if archive.testzip() is not None:
            raise ValueError("Corrupt zip member")
        assert len(archive.namelist())==len(FILES)+2
    print(f"PLAY_CONSOLE_UPLOAD_PACK_READY={args.out}")
    print(f"PLAY_CONSOLE_UPLOAD_PACK_FILES={len(FILES)+2}")
    print(f"SIGNED_AAB_INCLUDED=0")
    print(f"GOOGLE_PLAY_SUBMISSION_COMPLETE=0")


if __name__=="__main__":
    main()
