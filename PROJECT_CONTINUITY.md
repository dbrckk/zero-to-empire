# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-08 22:22 +02:00
- **112 / 235 strict DONE**.
- No strict increment without all gates.

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
- Artifact `10072830442` contains only the kernel log (~960-byte zip), no generated candidates.
- Therefore v16.4 still has no clean generation-quality evidence from wave88.
- Do not retrigger unchanged until Kaggle Internet access for this notebook/account is enabled, because the current kernel also needs network for package/model downloads.

## Kaggle internet requirement
- Kernel metadata already requests `enable_internet: true`, but this new account/API-created kernel did not actually receive network access.
- Practical next unblock: open the new account's `zero-to-empire-sprite-factory` notebook in Kaggle UI, ensure phone verification is complete, enable the notebook Internet toggle, save/run a version once, then retry from GitHub Actions.
- If Kaggle UI still cannot provide network, investigate account-level restriction instead of wasting GPU retries.

## Wave 87 — OLD ACCOUNT QUOTA FAILURE
- Run `34266340628`, job `102196557494`, completed failure.
- GitHub Actions itself worked correctly; Kaggle rejected the old-account push with `Maximum weekly GPU quota of 30.00 hours reached.`

## Productive reconciliation lane
- Run75 integration commit `e14b6897e32a557736a4e9c06d55b925864993d1` contains reviewed BLD-03 T2–T6 masters and runtime WebP outputs; technical QA passes all five.
- These remain outside strict DONE until active runtime visibility/reference, semantic evidence, canonical ledger reconciliation and green Android CI are explicitly proven.
- Other ART/RUNTIME-integrated candidates to reconcile: BLD-02-T4/T5/T6, BLD-03-T0/T1, FX-08..17.

## Alternative GPU backend investigation
- Lightning AI Studio `zero-to-empire` exists and CLI access works.
- T4 switch attempt returned Lightning cluster error `accelerator lit-t4-1 not found for this lightning cluster`; no Lightning GPU execution has occurred yet.
- Keep Lightning as fallback work, but Kaggle remains preferred if Internet can be enabled on the new account.

## Next actions
1. User enables Kaggle notebook Internet access once in UI on the new account; do not rerun unchanged before that.
2. Then trigger a new wave using v16.4 unchanged and verify: auth → push → queued/running → v16.4 startup → candidates/artifacts.
3. If Internet remains blocked, continue no-GPU reconciliation and finish an alternate GPU backend rather than burning runs.
4. Reconcile run75 and other already-integrated assets for strict progress where evidence supports it.
5. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
