# ZERO → EMPIRE — Google Play production release runbook

Last repository audit: **19 October 2026**. Goal: ship the currently user-approved V1 assets, postpone cosmetic character animation refinements to V1.1.

## Release status versus external prerequisites

| Area | Repository automation | Human / account verification |
| --- | --- | --- |
| Android API compliance | `compileSdk=36`, `targetSdk=36`, `minSdk=26` | Confirm no policy extension is needed on release date |
| Android package | `com.zerotoempire.game`; dedicated signed bundle workflow | Verify package has not previously been registered under a different Play account |
| Asset approval | Explicit user approval of 16 original character animations; promotion gated on lossless runtime conversion, tests, lint and bundle creation | Ensure latest `master-asset-queue.json` is **235/235** after the workflow succeeds |
| Gameplay | Unit, lint, app debug build and real Android emulator functional smoke | Install **signed** AAB from a Play testing track and test purchases, ads, no-crash navigation and restore |
| Signing | `.github/workflows/production-release.yml` validates keystore fingerprint and bundle signature | Create / securely preserve own **upload key**, enroll in **Play App Signing**, add CI secrets |
| Monetization | Play Billing + Mobile Ads + UMP integrations, configuration fail-closed on test Ad IDs | Register real AdMob app and units and four Play one-time products, validate UMP disclosure |
| Privacy | Local privacy document and hosted page https://dazzling-rift-vw8829a.shipstatic.com/ | Verify the link externally, developer contact method and final Google SDK disclosures |
| Listing media | Reproducible 512px Play icon and 1024×500 RGB feature PNG pipeline; raw emulator gameplay screenshots | Review screenshots captured from **final signed candidate**, not just debug, and choose compliant store imagery |
| Store text | English `marketing/play-store-listing.md` and French `marketing/play-store-listing-fr-FR.md` | Paste into locale fields; select category, contact info and countries |
| Audience / policies | Data Safety working sheet `marketing/data-safety.md` | Complete Play Console forms (ads, in-app purchases, target audience, rating, data security) |
| Production access | No automation can waive Google Play testing criteria | New personal developer accounts created after 13 Nov 2023 usually require **12 opted-in testers for 14 continuous days** plus production access application |

Do **not** call a debug APK or an unsigned AAB a production release.

## Step 1: Verify all asset and gameplay gates

On GitHub open **Actions** and confirm the following completed successfully for the same release commit:

1. **Promote user-approved original characters**: `235/235` strict assets on `main` and 16 runtime WebP atlases.
2. **Android CI**: unit tests, lint, release bundle, merged-manifest allowlist.
3. **Android Emulator Smoke**: UI onboarding, tabs, tap economy, manager automation, offline return, persistence, character QA and crash scan.
4. **Play Store Artwork Pack**: `marketing/play-store-assets/zero-to-empire-icon-512.png` and `zero-to-empire-feature-1024x500.png`, plus `store-artwork-manifest.json` hashes.

Download the release image/screenshots archive via the Actions artifacts. The smoke screenshots in `play-store-preview/` are raw Android **debug** emulator captures, not evidence that the signed release has been tested.

## Step 2: Supply production secrets securely

In **GitHub → dbrckk/zero-to-empire → Settings → Secrets and variables → Actions**, create **repository secrets** (never commit their contents):

```text
ZERO_EMPIRE_KEYSTORE_BASE64
ZERO_EMPIRE_KEYSTORE_PASSWORD
ZERO_EMPIRE_KEY_ALIAS
ZERO_EMPIRE_KEY_PASSWORD
ADMOB_APP_ID
REWARDED_AD_UNIT_ID
INTERSTITIAL_AD_UNIT_ID
```

The keystore must be an upload key that you control and store securely offline. `ZERO_EMPIRE_KEYSTORE_BASE64` is the binary `.jks` keystore converted into a **single-line Base64** string. The three ad identifiers must be real IDs for the correct AdMob app/units; the script intentionally rejects Google's test IDs for a signed release. Use different rewarded and interstitial unit IDs.

Keep a secure offline backup of your keystore and passwords. Losing an upload key can require a Google Play upload-key reset.

## Step 3: Generate the signed release bundle

From GitHub **Actions → Production Release Gate → Run workflow**, enter:

- `version_code`: a positive integer **higher than any previously uploaded version code** (for a truly new app, often `1`).
- `version_name`: e.g. `1.0.0`.

The workflow checks source manifest privacy policy, requires production AdMob IDs, validates keystore credentials, compiles and signs `app-release.aab`, verifies certificate fingerprints and archive integrity, checks R8 mapping and exports the AAB plus SHA-256 and mapping file as `zero-to-empire-production-<version>-<code>` artifact.

Without valid credentials this workflow correctly **fails** instead of producing a deceptively publishable build.

## Step 4: Configure the Play Console

1. Create the game application with package `com.zerotoempire.game`. Choose Games → Simulation or other truthful category.
2. Complete developer identity/contact, countries, content rating, ads, IAP, target audience and policy declarations.
3. Paste English and French texts from `marketing/`. Upload 512px launcher icon and 1024×500 feature graphic from `marketing/play-store-assets/`.
4. Verify privacy policy at https://dazzling-rift-vw8829a.shipstatic.com/ and reconcile `marketing/data-safety.md` with current Google Mobile Ads, UMP and Play Billing SDK disclosures. Confirm users have a **publicly functioning privacy contact channel**.
5. Create one-time Play Billing products matching **exactly**: `remove_ads_lifetime`, `starter_pack`, `gems_small`, `gems_medium`. Set regional prices and availability; verify acknowledgment, consumption and restoration on a tester purchase.
6. Configure the real AdMob application, rewarded/interstitial units and consent messaging. Test with **test devices** in the Play-distributed candidate.
7. Upload the signed `.aab` to an **internal test track**. Test install/upgrade, onboarding, offline restore, UI layouts, music/sound preferences, commerce, reward flow, non-consenting ads behavior, backup/restore and crashes on at least one physical Android device.
8. If required for your developer account, complete the **closed test with 12 opted-in testers continuously for at least 14 days**, then request production access.
9. Inspect Android Vitals / pre-launch report and fix material crashes, ANRs or severe layout problems before submitting to production.
10. Publish with a controlled initial rollout when Google has approved the app.

## Store asset requirements

Google Play currently requires a **512×512, at most 1,024 KiB, 32-bit PNG** icon and a **1024×500, 24-bit RGB JPEG/PNG** feature graphic. The repository's export workflow verifies these mechanically. Genuine phone screenshots remain a separate mandatory item.

## Explicit release blockers that code cannot invent

- Production upload keystore **and secret passwords**.
- Real AdMob production identifiers.
- Play Console / Billing and compliance selections.
- Confirmed contact information and public privacy contact mechanism.
- Google Play's internal / closed testing and final distribution approval.

The technical pipeline must not report the game as already **published** or a **signed production AAB** as available until the Actions artifact and Play Console actually confirm it.

## Official sources

- Target API level: https://support.google.com/googleplay/android-developer/answer/11926878
- Store images: https://support.google.com/googleplay/android-developer/answer/9866151
- Data safety and privacy policy: https://support.google.com/googleplay/android-developer/answer/10144311
- Play testing for new personal accounts: https://support.google.com/googleplay/android-developer/answer/14151465
