# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-09 00:05 +02:00
- **112 / 235 strict DONE**.
- No strict increment without all gates.

## Night intervention — Android CI coverage hardened
- Observed that reconciliation commit `1acf87c70e3dd7722a748a3eba4a01e76249f79e` had no workflow runs because `android.yml` only triggered for `app/**` and build-system paths.
- This meant a canonical manifest/status reconciliation could land without a fresh Android verification, despite strict DONE explicitly requiring green Android CI.
- Updated `.github/workflows/android.yml` in commit `d3ec47365f82a47f12cd41f3d740517f1ef28a25` so both push and PR triggers now also cover `art/production/**` and `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`.
- Android CI run `34283943481` (run #622) was automatically created for that commit and was queued at handoff.
- This closes the trigger-coverage gap for future semantic/QA evidence and canonical manifest reconciliation. Strict count remains 112/235 until the run is green and runtime reference/visibility is proven.

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
- BLD-02 T4–T6 and BLD-03 T0–T1 are also currently `RUNTIME` in the canonical manifest.
- Next evidence target is runtime code reference/visibility for these assets; do not promote based on file presence alone.
- FX-08..17 remain candidates for evidence-first reconciliation.

## Alternative GPU backend investigation
- Lightning AI Studio `zero-to-empire` exists and CLI access works.
- T4 switch attempt returned `accelerator lit-t4-1 not found for this lightning cluster`; no Lightning GPU execution has occurred yet.

## Next actions
1. Check Android CI run `34283943481`; diagnose/fix if not green.
2. Prove runtime code reference/visibility for BLD-02 T4–T6 and BLD-03 T0–T6; only promote assets with semantic + technical evidence and green CI.
3. Reconcile FX-08..17 using the same evidence-first approach.
4. Do not retry Kaggle until the new account exposes usable GPU + Internet in its notebook UI.
5. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
