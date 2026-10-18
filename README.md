# ZERO → EMPIRE

A premium-feeling Android idle/incremental game built with Kotlin and Jetpack Compose.

## Product pillars

- Satisfying 5–30 second micro-loop
- Meaningful offline progression
- Layered automation and prestige
- Fast visual feedback, haptics and motion
- Rewarded ads that accelerate without blocking play
- Ethical IAP and optional ad removal
- Data-driven economy that can be balanced without rewriting UI
- Viral, shareable progression milestones

## Core loop

Earn → Invest → Automate → Multiply → Unlock → Prestige → Expand

The player starts with a tiny street stand and compounds their way through increasingly absurd economic scales: businesses, factories, cities, nations, planets and beyond.

## Technical direction

- Kotlin
- Jetpack Compose + Material 3
- MVVM / unidirectional state flow
- Kotlin Coroutines + StateFlow
- DataStore for durable local state
- Google Play Billing integration layer
- Ad provider abstraction
- Offline earnings with capped, validated elapsed time
- Deterministic economy formulas

## Release candidate status — 19 October 2026

- **235/235 canonical game assets approved and installed**: the character promotion pipeline passed full runtime checks, debug build, unit tests, Android lint and unsigned release bundle assembly.
- **Android API 36** target; application ID `com.zerotoempire.game`.
- Play Store artwork exported in `marketing/play-store-assets/`, and localized copy in `marketing/play-store-listing-fr-FR.md`.
- A public [privacy policy](https://dazzling-rift-vw8829a.shipstatic.com/) is hosted and linked in the store checklist.
- **Not yet live on Google Play.** The signed upload AAB, AdMob production settings, Play Billing console products, Play Console compliance declarations and signed-track testing require configuration.
- Publish readiness can be inspected via [Google Play Release Preflight](https://github.com/dbrckk/zero-to-empire/actions/workflows/play-submission-preflight.yml). Signing is intentionally fail-closed until valid private credentials are configured.

See **[Play Store release runbook](marketing/PLAY_STORE_RELEASE_RUNBOOK.md)** for the exact steps and links. The initial version deliberately keeps user-approved character animation quality stable; visual polish is scheduled for a later update.
