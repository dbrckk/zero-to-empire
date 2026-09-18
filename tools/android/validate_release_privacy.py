#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]

BUILD = ROOT / "app/build.gradle.kts"
COMMERCE = ROOT / "app/src/main/java/com/zerotoempire/game/CommerceUi.kt"
IN_APP_POLICY = ROOT / "app/src/main/java/com/zerotoempire/game/PrivacyPolicy.kt"
PUBLIC_POLICY = ROOT / "marketing/privacy-policy.md"
DATA_SAFETY = ROOT / "marketing/data-safety.md"
STORE_LISTING = ROOT / "marketing/play-store-listing.md"

required_files = [BUILD, COMMERCE, IN_APP_POLICY, PUBLIC_POLICY, DATA_SAFETY, STORE_LISTING]
missing = [str(path.relative_to(ROOT)) for path in required_files if not path.is_file()]
if missing:
    raise SystemExit("Missing release privacy file(s): " + ", ".join(missing))

build = BUILD.read_text(encoding="utf-8")
commerce = COMMERCE.read_text(encoding="utf-8")
in_app = IN_APP_POLICY.read_text(encoding="utf-8")
public = PUBLIC_POLICY.read_text(encoding="utf-8")
data_safety = DATA_SAFETY.read_text(encoding="utf-8")
listing = STORE_LISTING.read_text(encoding="utf-8")

sensitive_prefixes = (
    "com.android.billingclient:billing:",
    "com.google.android.gms:play-services-ads:",
    "com.google.android.ump:user-messaging-platform:",
)

dependencies = re.findall(r'implementation\("([^"]+)"\)', build)
sensitive_dependencies = sorted(
    dep for dep in dependencies if dep.startswith(sensitive_prefixes)
)

if not sensitive_dependencies:
    raise SystemExit("No billing/ads/consent dependencies detected; validator assumptions are stale.")

for dependency in sensitive_dependencies:
    if dependency not in data_safety:
        raise SystemExit(
            f"Data Safety sheet is stale: missing exact production dependency {dependency}"
        )

required_public_headings = (
    "## Advertising and consent",
    "## Purchases",
    "## Local game data",
    "## Diagnostics and analytics",
    "## Third-party services",
    "## Contact",
)
for heading in required_public_headings:
    if heading not in public:
        raise SystemExit(f"Public privacy policy is missing required section: {heading}")

required_in_app_terms = (
    "PRIVACY_POLICY_VERSION",
    "Google User Messaging Platform",
    "Google Mobile Ads",
    "Google Play Billing",
    "Local game data",
    "Third-party services",
)
for term in required_in_app_terms:
    if term not in in_app:
        raise SystemExit(f"In-app privacy policy is missing required term: {term}")

if 'Text("PRIVACY POLICY")' not in commerce or "PrivacyPolicyDialog" not in commerce:
    raise SystemExit("Store no longer exposes the in-app privacy policy.")

for source in ("marketing/privacy-policy.md", "marketing/data-safety.md"):
    if f"`{source}`" not in listing:
        raise SystemExit(f"Play Store listing no longer references {source}")

if "android:usesCleartextTraffic=\"false\"" not in (
    ROOT / "app/src/main/AndroidManifest.xml"
).read_text(encoding="utf-8"):
    raise SystemExit("Release privacy assumptions changed: cleartext traffic is no longer disabled.")

print("Release privacy/Data Safety static validation passed.")
print("Sensitive SDK inventory:")
for dependency in sensitive_dependencies:
    print(f"- {dependency}")
