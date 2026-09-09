# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-09 04:06 +02:00
- **112 / 235 strict DONE** according to the canonical row statuses used by project continuity; no strict increment was made in this intervention.
- No strict increment without all gates.

## Night intervention — continuity count now mechanically tied to canonical manifest
- Verified `Reconcile Sprite Progress Ledger` run `34293344248` completed **SUCCESS** on commit `e3ec14b4b87265c12281392f7f14aac172d1d2df`.
- Verified the reconciled manifest ledger is now authoritative at **112 / 235 DONE**, with family totals: Buildings 18/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 0/18.
- Hardened `.github/workflows/reconcile-sprite-progress-ledger.yml` in commit `f295332abd9d660ca8604e67f144c25190ce7227` so the same canonical-row computation also reconciles the trusted strict-DONE line in `PROJECT_CONTINUITY.md`.
- The workflow now triggers on manifest, workflow, or continuity changes and commits only aggregate state; it still **never changes per-asset TODO/RUNTIME/DONE status**.
- This removes a second drift path: the manifest footer and continuity headline can no longer silently disagree after future status changes.
- Validation run `34301830088` was queued immediately after the workflow change; verify its final result next. No asset promotion occurred.

## Previous night intervention — canonical progress ledger made self-reconciling
- Verified Android CI run `34288618789` (#623), job `102269896071`, completed **SUCCESS**: JDK 17, Gradle 8.13, debug APK, unit tests, lint and APK upload all passed. The repaired Android gate is now proven operational.
- Found a material bookkeeping inconsistency: the manifest footer still reported `DONE: 52 / 235` while project continuity tracked 112 strict DONE and many manifest rows are already `DONE`. This made aggregate progress untrustworthy even when individual canonical rows were correct.
- Added `.github/workflows/reconcile-sprite-progress-ledger.yml` in commit `e3ec14b4b87265c12281392f7f14aac172d1d2df`.
- The workflow derives aggregate progress exclusively from the 235 canonical manifest rows, refuses to run if row count, uniqueness, asset-family classification, or planned family totals drift, and **never changes per-asset status**.
- Workflow run `34293344248` completed **SUCCESS** and reconciled the footer/count to 112/235.

## Runtime-reference evidence audit — BLD-02 / BLD-03
- Canonical manifest currently has BLD-02 T4–T6 and BLD-03 T0–T6 at `RUNTIME`.
- `BusinessGroup01Art.kt` still renders business IDs 2 and 3 procedurally through Compose `Canvas` (`drawWorkshopAAA` / `drawFactoryAAA`) and contains no reference to `zte_business_02_t*_final.webp` or `zte_business_03_t*_final.webp`.
- `BusinessGroup01Evolution.kt` similarly adds procedural tier overlays for IDs 2 and 3; its progression has levels 0,10,25,50,100,250,500,1000, which must be mapped deliberately onto canonical T0–T6 before raster replacement.
- The canonical WebP files are present under `app/src/main/res/drawable-nodpi`, but file presence is not visibility evidence. Do not promote these assets to DONE until the runtime rendering path consumes the canonical resources and CI is green.

## Android CI history
- Run `34283943481` (#622) failed before compilation because the repository has no root `gradlew` while the workflow tried `chmod +x gradlew`.
- Commit `de1f0df61f2793aa6dcdb4ebcca3aec7ad6f4e09` changed Android CI to provision Gradle 8.13 explicitly and run `gradle assembleDebug`, `gradle testDebugUnitTest`, and `gradle lintDebug`.
- Run `34288618789` (#623) subsequently passed all build/test/lint gates.
- Commit `d3ec47365f82a47f12cd41f3d740517f1ef28a25` previously expanded Android CI path coverage to `art/production/**` and `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`.

## Previous intervention — reconcile reviewed run75 BLD-03 T2–T6
- Added `.github/workflows/reconcile-run75-bld03-status.yml`, commit `8e7e18e876c04479fde60d7dec0f7c77cb677b6e`.
- GitHub Actions run `34278218123`, job `102236382927`, completed **success**.
- It verified reviewed PNG masters, runtime WebP outputs and `art/production/run75-bld03-qa.json`, then changed only `TODO -> RUNTIME`.
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
- FX-08..17 are canonical `RUNTIME`; they still require runtime-reference/visibility evidence before DONE.

## Alternative GPU backend investigation
- Lightning AI Studio `zero-to-empire` exists and CLI access works.
- T4 switch attempt returned `accelerator lit-t4-1 not found for this lightning cluster`; no Lightning GPU execution has occurred yet.

## Next actions
1. Verify synchronization workflow run `34301830088` is green; if it fails, repair the aggregate reconciliation guard before any status mutation.
2. Replace/prove the procedural BusinessGroup01 rendering path for business IDs 2 and 3 with canonical tier-specific WebP resources, explicitly defining the 8 gameplay progression stages → 7 canonical raster tiers mapping; then require green Android CI before any `RUNTIME -> DONE` promotion.
3. Audit FX-08..17 runtime call sites and visibility, promoting only assets with semantic evidence + active reference + green CI.
4. Do not retry Kaggle until the new account exposes usable GPU + Internet in its notebook UI.
5. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
