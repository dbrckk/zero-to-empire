# ZERO → EMPIRE — Google Play internal draft automation

This workflow is **optional** and **manual-only**. It cannot publish to production
and deliberately will not distribute a version to testers. Its default mode only
verifies the signed AAB built by the existing Production Release Gate.

## One-time prerequisites

1. Create ZERO → EMPIRE in [Google Play Console](https://play.google.com/console)
   with package `com.zerotoempire.game`; verify Play App Signing and the upload key.
2. Configure the seven existing signing/AdMob repository secrets listed in
   [PLAY_STORE_RELEASE_RUNBOOK.md](PLAY_STORE_RELEASE_RUNBOOK.md).
3. Run [Production Release Gate](../.github/workflows/production-release.yml)
   with your chosen fresh version code and version name. Keep the **successful
   GitHub Actions run ID**. Only its signed `app-release.aab` is accepted.
4. For automated internal draft creation, enable Google Play Developer API on a
   Google Cloud project and create a **restricted service account**. Invite its
   service-account email from Play Console **Users and permissions** and grant
   only the app/release rights needed for internal-test upload. Avoid granting
   finance, billing, or account-administrator permissions for this workflow.
5. Store the complete downloaded service-account JSON key as the GitHub Actions
   repository secret **`GOOGLE_PLAY_SERVICE_ACCOUNT_JSON`** (do not base64
   encode it). Never commit it, paste it into a chat, or place it in an Actions
   artifact. Rotate/revoke it promptly if exposed.

**Google's publishing API initial-upload limitation:** the Android Publisher
Edits API is documented as requiring an existing app with at least one APK
previously uploaded from Play Console. For a new app, first upload a signed
bundle **manually through Play Console**; then enable this optional API workflow.
Check any current Google Play Console requirements shown by your account.

## Run on GitHub Actions

Open [Google Play Internal Draft (Manual Only)](../.github/workflows/play-internal-draft.yml)
and choose **Run workflow** on `main`.

- `production_run_id`: successful signed Production Release Gate run ID
- `mode` = `verify_only` (default): download and independently validate the
  source run identity, version metadata, AAB hash, bundle structure and signature.
  **No Google Play mutation and no service-account secret required.**
- `mode` = `create_internal_draft`: same checks, then submit only to the
  `internal` track with release status `draft`. This requires the service-account
  secret and `confirmation` = `CREATE_INTERNAL_DRAFT`.

A draft is **not served to testers**. Review the internal testing release
inside Play Console before activating distribution. This workflow never uses
the production track, and will refuse to overwrite any pre-existing internal
track releases. It also refuses to commit if an app edit is already in review.

## Evidence / guardrails

- Only successful, manually started `production-release.yml` runs from the
  repository's `main` branch qualify.
- Both artifact checksum and source commit must match the original signing run.
  An independent `jarsigner -verify` check is required.
- The workflow archives a non-secret JSON verification report. It includes
  immutable hashes, not account credentials.
- No production rollout, app-listing edits, tester enrollments, or policy
  declarations are performed.
- Google Play product catalogs (`remove_ads_lifetime`, `starter_pack`,
  `gems_small`, `gems_medium`) and AdMob ad units must be configured
  separately before real-money/rewarded-ad testing.
- If your new personal developer account falls under the current Google Play
  closed-testing requirement, follow the requisite tester enrollment period.
  An internal draft does not satisfy or bypass it.

## Official documentation

- [Google Play Developer API setup](https://developers.google.com/android-publisher/getting_started)
- [Publishing Edits API and initial upload prerequisites](https://developers.google.com/android-publisher/edits)
- [Google Play draft track semantics](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks)
- [Signing and publishing checklist](PLAY_STORE_RELEASE_RUNBOOK.md)
