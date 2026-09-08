# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-09 01:04 +02:00
- **112 / 235 strict DONE**.
- No strict increment without all gates.

## Night intervention — Android CI execution repaired
- Android CI run `34283943481` (#622), job `102255012735`, completed **failure** before any Android compilation.
- Exact root cause: the repository has no `gradlew` at the root, but `.github/workflows/android.yml` executed `chmod +x gradlew`; the job failed with `chmod: cannot access 'gradlew': No such file or directory`.
- The previous `gradle/actions/setup-gradle` step itself succeeded and reported wrapper jars valid, so the failure was workflow/repository mismatch, not app compilation.
- Updated `.github/workflows/android.yml` in commit `de1f0df61f2793aa6dcdb4ebcca3aec7ad6f4e09` to provision **Gradle 8.13** explicitly via `gradle/actions/setup-gradle`, verify it with `gradle --version`, and run `gradle assembleDebug`, `gradle testDebugUnitTest`, and `gradle lintDebug` directly. This is aligned with AGP `8.12.1` declared in the root build.
- Android CI run `34288618789` (#623), job `102269896071`, was automatically triggered. Setup JDK 17, Gradle 8.13 provisioning and toolchain verification all passed; `Build debug APK` was in progress at handoff.
- This converts the previous guaranteed wrapper-path failure into a real Android build/test/lint gate.

## Runtime-reference evidence audit — BLD-02 / BLD-03
- Canonical manifest currently has BLD-02 T4–T6 and BLD-03 T0–T6 at `RUNTIME`.
- `BusinessGroup01Art.kt` still renders business IDs 2 and 3 procedurally through Compose `Canvas` (`drawWorkshopAAA` / `drawFactoryAAA`) and contains no reference to `zte_business_02_t*_final.webp` or `zte_business_03_t*_final.webp`.
- `BusinessGroup01Evolution.kt` similarly adds procedural tier overlays for IDs 2 and 3.
- Therefore file presence is **not** sufficient evidence that the new raster masters are actually visible in-game. Do not promote these ten assets to DONE until the runtime rendering path is changed/proven to consume the canonical WebP resources and CI is green.

## Previous intervention — Android CI coverage hardened
- Observed that reconciliation commit `1acf87c70e3dd7722a748a3eba4a01e76249f79e` had no workflow runs because `android.yml` only triggered for `app/**` and build-system paths.
- Updated `.github/workflows/android.yml` in commit `d3ec47365f82a47f12cd41f3d740517f1ef28a25` so both push and PR triggers also cover `art/production/**` and `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`.

## Previous intervention — reconcile reviewed run75 BLD-03 T2–T6
- Added `.github/workflows/reconcile-run75-bld03-status.yml`, commit `8e7e18e876c04479fde60d7dec0f7c77cb677b6e`.
- GitHub Actions run `34278218123`, job `102236382927`, completed **success**.
- The reconciliation verified, for every BLD-03 T2–T6 tier, that both the reviewed PNG master and final runtime WebP are non-empty, and that `art/production/run75-bld03-qa.json` exists before touching the canonical manifest.
- It changed only `TODO -> RUNTIME`; it deliberately cannot mark these assets `DONE`.
- Reconciliation commit: `1acf87c70e3dd7722a748a3eba4a01e76249f79e`.

## Building generator v16.4 — COMMITTED / STILL NOT EXECUTED CLEANLY
`tools/sprites/kaggle_building_family_factory_v16.py`, commit `fa41f56442a2e62227045b272676780c5a8f5ca8`.
Startup target: `building-family-flux-v16.4-footprint-locked-two-phase`.
Core experiment: low-denoise tier evolution, T0–T3 massing then T4–T6 detail, footprint-locked positive spatial contract, stronger low/broad anchor preference, tier-dependent adjacent footprint IoU floor, strict slab QA unchanged.

## Wave 88 — NEW KAGGLE ACCOUNT / AUTH + GPU PUSH WORK, INTERNET BLOCKS RUNTIME
- Trigger commit `3475d6e31d9d78990942d3bef3b45a904fe4ad0c`.
- GitHub Actions run `34268429978`, job `102203616121`, completed failure.
- New Kaggle credentials are valid; kernel push succeeded and Kaggle accepted the GPU job.
- Kernel failed because runtime DNS/network access was unavailable: `Could not resolve host: github.com`.
- Do not retrigger unchanged until Kaggle Internet access and GPU eligibility are actually usable in the UI.

## Productive reconciliation lane
- BLD-03 T2–T6 are canonical `RUNTIME`, not DONE.
- BLD-02 T4–T6 and BLD-03 T0–T1 are also `RUNTIME`.
- FX-08..17 remain candidates for evidence-first reconciliation.

## Alternative GPU backend investigation
- Lightning AI Studio `zero-to-empire` exists and CLI access works.
- T4 switch attempt returned `accelerator lit-t4-1 not found for this lightning cluster`; no Lightning GPU execution has occurred yet.

## Next actions
1. Check Android CI run `34288618789`; diagnose/fix any real compile/test/lint failure until green.
2. Replace/prove the procedural BusinessGroup01 rendering path for business IDs 2 and 3 with canonical tier-specific WebP resources while preserving reduced-motion behavior where applicable; then require green CI before any `RUNTIME -> DONE` promotion.
3. Reconcile FX-08..17 using the same evidence-first approach.
4. Do not retry Kaggle until the new account exposes usable GPU + Internet in its notebook UI.
5. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
