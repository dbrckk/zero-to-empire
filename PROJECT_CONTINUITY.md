# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-08 23:05 +02:00
- **112 / 235 strict DONE**.
- No strict increment without all gates.

## Night intervention — reconcile reviewed run75 BLD-03 T2–T6
- Added `.github/workflows/reconcile-run75-bld03-status.yml`, commit `8e7e18e876c04479fde60d7dec0f7c77cb677b6e`.
- GitHub Actions run `34278218123`, job `102236382927`, completed **success**.
- The reconciliation verified, for every BLD-03 T2–T6 tier, that both the reviewed PNG master and final runtime WebP are non-empty, and that `art/production/run75-bld03-qa.json` exists before touching the canonical manifest.
- It changed only `TODO -> RUNTIME`; it deliberately cannot mark these assets `DONE`.
- This fixed an observed ledger inconsistency: the run75 promotion workflow explicitly calls the five masters `semantically approved`, processes them to final runtime assets, and commits them, while the canonical manifest still listed BLD-03 T2–T6 as TODO.
- Reconciliation commit produced by the workflow: `1acf87c70e3dd7722a748a3eba4a01e76249f79e`.
- BLD-03 T2 runtime file was independently confirmed present on `main` with blob SHA `e5fe48c9b47aa2bf28e169371ab02649e9141276`; the workflow verified all five tiers before commit.
- Strict count remains 112/235 until runtime reference/visibility and green Android CI are proven.

## Building generator v16.4 — COMMITTED / STILL NOT EXECUTED CLEANLY
`tools/sprites/kaggle_building_family_factory_v16.py`, commit `fa41f56442a2e62227045b272676780c5a8f5ca8`.
Startup target: `building-family-flux-v16.4-footprint-locked-two-phase`.
Core experiment: low-denoise tier evolution, T0–T3 massing then T4–T6 detail, footprint-locked positive spatial contract, stronger low/broad anchor preference, tier-dependent adjacent footprint IoU floor, strict slab QA unchanged.

## Wave 88 — NEW KAGGLE ACCOUNT / AUTH + GPU PUSH WORK, INTERNET BLOCKS RUNTIME
- Trigger commit `3475d6e31d9d78990942d3bef3b45a904fe4ad0c`.
- GitHub Actions run `34268429978`, job `102203616121`, completed failure.
- New Kaggle credentials are valid: Kaggle authentication succeeded.
- Kernel push succeeded: `Kernel version 1 successfully pushed`.
- Kaggle accepted the GPU job and it reached `KernelWorkerStatus.QUEUED`, so this is not the previous weekly-quota rejection.
- Kernel then failed after ~1 minute because runtime DNS/network access was unavailable: `fatal: unable to access 'https://github.com/dbrckk/zero-to-empire.git/': Could not resolve host: github.com`.
- Artifact `10072830442` contains only the kernel log, no generated candidates.
- Therefore v16.4 still has no clean generation-quality evidence from wave88.
- Do not retrigger unchanged until Kaggle Internet access for this notebook/account is enabled, because the current kernel also needs network for package/model downloads.

## Kaggle internet / account requirement
- Kernel metadata already requests `enable_internet: true`, but the new account/API-created kernel did not actually receive network access.
- In Kaggle UI, the notebook is visible. Current editor showed accelerator choices grayed out, so the account still needs the Kaggle-side eligibility/verification state resolved before relying on GPU execution.
- Do not waste additional Kaggle pushes until GPU/Internet are selectable in the UI.

## Wave 87 — OLD ACCOUNT QUOTA FAILURE
- Run `34266340628`, job `102196557494`, completed failure.
- GitHub Actions itself worked correctly; Kaggle rejected the old-account push with `Maximum weekly GPU quota of 30.00 hours reached.`

## Productive reconciliation lane
- Run75 integration commit `e14b6897e32a557736a4e9c06d55b925864993d1` contains reviewed BLD-03 T2–T6 masters and runtime WebP outputs; technical QA passes all five.
- BLD-03 T2–T6 are now canonical `RUNTIME`, not DONE.
- Other ART/RUNTIME-integrated candidates to reconcile next: BLD-02-T4/T5/T6, BLD-03-T0/T1, FX-08..17.

## Alternative GPU backend investigation
- Lightning AI Studio `zero-to-empire` exists and CLI access works.
- T4 switch attempt returned Lightning cluster error `accelerator lit-t4-1 not found for this lightning cluster`; no Lightning GPU execution has occurred yet.
- Keep Lightning as fallback work, but Kaggle remains preferred if Internet/GPU eligibility can be enabled on the new account.

## Next actions
1. Verify Android CI on reconciliation commit `1acf87c70e3dd7722a748a3eba4a01e76249f79e`.
2. Prove runtime reference/visibility for BLD-03 T2–T6; only then consider DONE after green Android CI.
3. Reconcile BLD-02-T4/T5/T6, BLD-03-T0/T1 and FX-08..17 using the same evidence-first approach.
4. Do not retry Kaggle until the new account exposes usable GPU + Internet in its notebook UI.
5. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
