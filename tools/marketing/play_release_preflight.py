#!/usr/bin/env python3
"""Read-only Google Play submission preflight. Never prints secret values."""
from __future__ import annotations

import json
import os
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "marketing/play-store-assets/play-release-preflight.json"
SECRET_NAMES = (
    "ZERO_EMPIRE_KEYSTORE_BASE64",
    "ZERO_EMPIRE_KEYSTORE_PASSWORD",
    "ZERO_EMPIRE_KEY_ALIAS",
    "ZERO_EMPIRE_KEY_PASSWORD",
    "ADMOB_APP_ID",
    "REWARDED_AD_UNIT_ID",
    "INTERSTITIAL_AD_UNIT_ID",
)
PRODUCTS = ("remove_ads_lifetime", "starter_pack", "gems_small", "gems_medium")


def png_info(path: Path) -> dict:
    raw = path.read_bytes()
    assert raw[:8] == b"\\x89PNG\\r\n\\x1a\n".decode("unicode_escape").encode("latin1"), str(path)
    assert raw[12:16] == b"IHDR", path
    width, height = struct.unpack(">II", raw[16:24])
    return {"width": width, "height": height, "bit_depth": raw[24],
            "color_type": raw[25], "bytes": len(raw)}


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def audit() -> dict:
    queue = json.loads(text("art/production/master-asset-queue.json"))
    done = sum(a["strict_status"] == "DONE" for a in queue["assets"])
    build = text("app/build.gradle.kts")
    catalog = text("app/src/main/java/com/zerotoempire/game/Monetization.kt")
    listing = text("marketing/play-store-listing-fr-FR.md")
    privacy = text("marketing/privacy-policy.md")
    tests = {
        "all_235_assets_approved": done == 235 and len(queue["assets"]) == 235,
        "play_2026_target_api_36": "targetSdk = 36" in build and "compileSdk = 36" in build,
        "package_id_fixed": 'applicationId = "com.zerotoempire.game"' in build,
        "billing_products_declared": all('"' + item + '"' in catalog for item in PRODUCTS),
        "privacy_policy_source_exists": len(privacy) > 700,
        "public_privacy_page_documented": "https://dazzling-rift-vw8829a.shipstatic.com/" in text("marketing/play-store-listing.md"),
    }
    m = re.search(r"^## Description courte[^\n]*\n\n([^\n]+)", listing, re.MULTILINE)
    short = m.group(1).strip() if m else ""
    m = re.search(r"^## Description complète[^\n]*\n\n(.*?)(?=^## |\\Z)", listing, re.MULTILINE | re.DOTALL)
    long = m.group(1).strip() if m else ""
    tests["french_short_description_within_80"] = 10 <= len(short) <= 80
    tests["french_full_description_within_4000"] = 100 <= len(long) <= 4000

    icon_path = ROOT / "marketing/play-store-assets/zero-to-empire-icon-512.png"
    feature_path = ROOT / "marketing/play-store-assets/zero-to-empire-feature-1024x500.png"
    if icon_path.is_file():
        icon = png_info(icon_path)
        tests["play_icon_size_type"] = (icon["width"], icon["height"], icon["bit_depth"], icon["color_type"]) == (512,512,8,6) and icon["bytes"] <= 1024*1024
    else: tests["play_icon_size_type"] = False
    if feature_path.is_file():
        feature = png_info(feature_path)
        tests["play_feature_size_type"] = (feature["width"], feature["height"], feature["bit_depth"], feature["color_type"]) == (1024,500,8,2)
    else: tests["play_feature_size_type"] = False
    secret_present = {name: bool(os.getenv(name, "").strip()) for name in SECRET_NAMES}
    tests["production_signing_and_ad_ids_configured"] = all(secret_present.values())
    report = {
        "schema_version": 1,
        "repo_checks": tests,
        "strict_done": done,
        "target_assets": 235,
        "production_secrets_present_by_name_only": secret_present,
        "missing_secret_names": sorted(k for k,v in secret_present.items() if not v),
        "signed_aab_created": False,
        "play_console_verified": False,
        "production_published": False,
        "note": "A passing source audit is not a signed bundle, purchase test or Play Console approval."
    }
    return report


if __name__ == "__main__":
    report = audit()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for k,v in report["repo_checks"].items():
        print(("PASS" if v else "NEEDS_ACTION") + " " + k)
    print("MISSING_SECRET_NAMES=" + ",".join(report["missing_secret_names"]))
    if not all(v for k,v in report["repo_checks"].items() if k != "production_signing_and_ad_ids_configured"):
        raise SystemExit("Repository Play assets or policy preflight failed")
