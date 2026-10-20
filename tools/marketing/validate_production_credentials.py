#!/usr/bin/env python3
"""Fail-closed production credential preflight; never prints credential values."""
from __future__ import annotations
import base64
import binascii
import os
import re
import sys

SECRETS = (
    "ZERO_EMPIRE_KEYSTORE_BASE64",
    "ZERO_EMPIRE_KEYSTORE_PASSWORD",
    "ZERO_EMPIRE_KEY_ALIAS",
    "ZERO_EMPIRE_KEY_PASSWORD",
    "ADMOB_APP_ID",
    "REWARDED_AD_UNIT_ID",
    "INTERSTITIAL_AD_UNIT_ID",
)
TEST_PUBLISHER = "3940256099942544"
APP_ID = re.compile(r"^ca-app-pub-([0-9]{16})~([0-9]{10})$")
UNIT_ID = re.compile(r"^ca-app-pub-([0-9]{16})/([0-9]{10})$")
MAX_KEYSTORE_BYTES = 1024 * 1024

def check(env: dict[str, str]) -> list[str]:
    problems: list[str] = []
    for name in SECRETS:
        if not env.get(name, "").strip():
            problems.append(f"{name}: missing")
    app = env.get("ADMOB_APP_ID", "").strip()
    rewarded = env.get("REWARDED_AD_UNIT_ID", "").strip()
    interstitial = env.get("INTERSTITIAL_AD_UNIT_ID", "").strip()
    app_match = APP_ID.fullmatch(app)
    rewarded_match = UNIT_ID.fullmatch(rewarded)
    interstitial_match = UNIT_ID.fullmatch(interstitial)
    for name, match in (("ADMOB_APP_ID", app_match), ("REWARDED_AD_UNIT_ID", rewarded_match),
                        ("INTERSTITIAL_AD_UNIT_ID", interstitial_match)):
        if env.get(name, "").strip() and not match:
            problems.append(f"{name}: invalid identifier format")
        if match and match.group(1) == TEST_PUBLISHER:
            problems.append(f"{name}: Google sample publisher is forbidden in production")
    if app_match and rewarded_match and app_match.group(1) != rewarded_match.group(1):
        problems.append("REWARDED_AD_UNIT_ID: publisher does not match AdMob application")
    if app_match and interstitial_match and app_match.group(1) != interstitial_match.group(1):
        problems.append("INTERSTITIAL_AD_UNIT_ID: publisher does not match AdMob application")
    if rewarded and interstitial and rewarded == interstitial:
        problems.append("Rewarded and interstitial ad units must be distinct")
    raw = env.get("ZERO_EMPIRE_KEYSTORE_BASE64", "").strip()
    if raw:
        if len(raw) > MAX_KEYSTORE_BYTES * 2:
            problems.append("ZERO_EMPIRE_KEYSTORE_BASE64: input exceeds allowed size")
        else:
            try:
                decoded = base64.b64decode(raw, validate=True)
                if not 32 <= len(decoded) <= MAX_KEYSTORE_BYTES:
                    problems.append("ZERO_EMPIRE_KEYSTORE_BASE64: invalid keystore byte length")
                elif not (decoded.startswith(bytes.fromhex("FEEDFEED")) or decoded.startswith(b"0")):
                    problems.append("ZERO_EMPIRE_KEYSTORE_BASE64: not a recognized JKS/PKCS12 container")
            except (ValueError, binascii.Error):
                problems.append("ZERO_EMPIRE_KEYSTORE_BASE64: invalid single-line Base64")
    return problems

if __name__ == "__main__":
    errors = check(dict(os.environ))
    for error in errors:
        print("::error::" + error)
    if errors:
        print(f"PRODUCTION_CREDENTIAL_PREFLIGHT=FAIL ({len(errors)} checks)")
        sys.exit(1)
    print("PRODUCTION_CREDENTIAL_PREFLIGHT=PASS (formats only; keystore signature validated later)")
