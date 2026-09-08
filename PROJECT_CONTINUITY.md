# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-08 21:22 +02:00
- **112 / 235 strict DONE**.
- No strict increment without all gates.

## Building generator v16.4 — COMMITTED / FIRST CLEAN EXECUTION IN PROGRESS
`tools/sprites/kaggle_building_family_factory_v16.py`, commit `fa41f56442a2e62227045b272676780c5a8f5ca8`.
Startup target: `building-family-flux-v16.4-footprint-locked-two-phase`.
Core experiment: low-denoise tier evolution, T0–T3 massing then T4–T6 detail, footprint-locked positive spatial contract, stronger low/broad anchor preference, tier-dependent adjacent footprint IoU floor, strict slab QA unchanged.

## Wave 88 — NEW KAGGLE ACCOUNT TEST
- User configured new Kaggle credentials in GitHub Actions secrets and confirmed completion.
- Trigger commit `3475d6e31d9d78990942d3bef3b45a904fe4ad0c`.
- GitHub Actions run `34268429978`, workflow `Kaggle Mass Sprite Factory`, run number 88.
- At verification the run is `in_progress`.
- This is the first run intended to use the new Kaggle account; do not infer success until authentication, kernel push, GPU execution and artifacts are verified.
- v16.4 remains unchanged for comparability.

## Wave 87 — OLD ACCOUNT QUOTA FAILURE
- Run `34266340628`, job `102196557494`, completed failure.
- GitHub Actions itself worked correctly: credentials existed, Kaggle authentication succeeded, kernel preparation succeeded.
- Kaggle rejected the kernel push with `Maximum weekly GPU quota of 30.00 hours reached.`
- Therefore wave87 produced no new v16.4 generation-quality evidence.

## Productive reconciliation lane
- Run75 integration commit `e14b6897e32a557736a4e9c06d55b925864993d1` contains reviewed BLD-03 T2–T6 masters and runtime WebP outputs; technical QA passes all five.
- These remain outside strict DONE until active runtime visibility/reference, semantic evidence, canonical ledger reconciliation and green Android CI are explicitly proven.
- Other ART/RUNTIME-integrated candidates to reconcile: BLD-02-T4/T5/T6, BLD-03-T0/T1, FX-08..17.

## Alternative GPU backend investigation
- Lightning AI Studio `zero-to-empire` exists and CLI access works.
- T4 switch attempt returned Lightning cluster error `accelerator lit-t4-1 not found for this lightning cluster`; no Lightning GPU execution has occurred yet.
- Keep Lightning as fallback work, but Kaggle remains preferred while the new account is being validated.

## Next actions
1. Observe wave88 and verify new-account authentication, successful kernel push, actual GPU execution, v16.4 startup and artifact generation.
2. If v16.4 executes, preserve artifacts/contact sheets/reports and perform strict semantic review before any promotion.
3. In parallel, reconcile run75 and other already-integrated assets for strict progress where evidence supports it.
4. If new Kaggle credentials fail or GPU is unavailable, diagnose the exact account/configuration failure rather than repeatedly retriggering.
5. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
