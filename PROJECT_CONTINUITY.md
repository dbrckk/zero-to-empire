# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **117 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09 08:10 +02:00
- **117 / 235 strict DONE**. Canonical aggregate derived from the 235 manifest rows.
- Canonical family totals: Buildings 18/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 0/18.
- `Reconcile Sprite Progress Ledger` runs `34301830088` and `34301864372` both completed SUCCESS.

## Latest intervention — BLD-02/03 canonical rasters now wired into the active world
- Verified Android CI #626 / run `34313359325` ended **cancelled**, not as a compile/test failure; its descendant test commit was validated by Android CI #627 / run `34313368691`, which completed **SUCCESS**.
- Existing mapping contract remains green: `CanonicalBusinessTier.kt` maps gameplay milestones to T0..T6 with 500/1000 sharing T6; `CanonicalBusinessRaster.kt` binds business IDs 2 and 3 to all seven canonical drawable resources; mapping and boundary tests pass on #627.
- Commit `cc06340730e7a81316dfa6b5bdd36dbec8b0ff3f` updates `WorldBusinessVisual.kt` so business IDs 2 (BLD-02 / Workshop) and 3 (BLD-03 / Factory) resolve their visible base raster through `canonicalBusinessRasterRes(businessId, level)` for every T0..T6 tier. IDs 0/1 retain their existing authored-resource path and unsupported businesses retain procedural fallback.
- Active runtime call chain is explicit in source: `PremiumZeroToEmpireApp` -> `AscendantCityEmpireWorld` -> `AscendantHeroLot` / `AscendantWorldLot` -> `WorldBusinessVisual` -> `canonicalBusinessRasterRes` -> `R.drawable.zte_business_02_t*` / `zte_business_03_t*` -> Compose `Image(painterResource(...))`.
- This means BLD-02/03 canonical WebPs are now selected by live gameplay rather than merely packaged resources. `BusinessGroup01Art.kt` remains the fallback renderer and no longer blocks world visibility for IDs 2/3.
- Android CI #628 / run `34317783009` started for the live-world renderer commit and was **in_progress** at last verification. Do not promote strict DONE until it is green and semantic evidence for each candidate is reconciled.

## Canonical business progression contract
- `CanonicalBusinessTier.kt`, commit `f85c4ea5474d0e7e779e0341bf995ab74ef1c113`: `<10 T0`, `10..24 T1`, `25..49 T2`, `50..99 T3`, `100..249 T4`, `250..499 T5`, `>=500 T6`.
- Gameplay milestones `0,10,25,50,100,250,500,1000` map to `T0,T1,T2,T3,T4,T5,T6,T6`.
- `CanonicalBusinessRaster.kt`, commit `e5cf2cd73c8184586fe18ba47cf3399625fc4ad4`, compile-time binds BLD-02/03 resources.
- `CanonicalBusinessRasterTest.kt`, commit `010f743205f33e00a6695be7467045ef8eb697ae`, and `CanonicalBusinessTierTest.kt`, commit `1fade114a205ded2c475397f78a8ab92761db4aa`, lock the contract.

## Android CI baseline
- Root-wrapper failure from #622 was repaired by commit `de1f0df61f2793aa6dcdb4ebcca3aec7ad6f4e09`, which provisions Gradle 8.13 explicitly.
- #623 passed APK build, unit tests, lint and artifact upload.
- Commit `d3ec47365f82a47f12cd41f3d740517f1ef28a25` expanded Android CI path coverage to `art/production/**` and the canonical sprite manifest.

## Productive reconciliation lane
- BLD-02 T4–T6 and BLD-03 T0–T6 are canonical `RUNTIME`; their active runtime selection is now implemented, but semantic evidence + green #628 + ledger promotion are still required before DONE.
- BLD-03 T2–T6 were previously evidence-reconciled to RUNTIME by run `34278218123` and commit `1acf87c70e3dd7722a748a3eba4a01e76249f79e`; run75 technical QA passes all five.
- FX-08..17 remain canonical `RUNTIME`; audit active call sites/visibility next.

## GPU state / blockers
- Kaggle new-account credentials are valid and kernel push works, but wave88 failed because runtime DNS/network access could not resolve `github.com`. Do not retrigger unchanged until notebook UI proves both usable GPU and Internet.
- In the user-visible Kaggle notebook UI, GPU T4 x2 / P100 were still grayed at last check. User was directed to complete phone verification; no confirmation yet.
- Lightning AI Studio exists and CLI access works, but `lit-t4-1` was unavailable in that cluster. No Lightning GPU execution has occurred.
- Building generator v16.4 remains committed at `fa41f56442a2e62227045b272676780c5a8f5ca8` and has not executed cleanly.

## Next actions
1. Verify Android CI #628 `34317783009`; repair immediately on failure.
2. Reconcile semantic evidence for BLD-02 T4–T6 and BLD-03 T0–T6. Promote only rows with semantic + technical evidence, active runtime visibility and green CI.
3. Audit FX-08..17 active runtime call sites/visibility and promote only where every strict gate is proven.
4. Do not retry Kaggle until GPU + Internet are actually usable.
5. Continue buildings -> statics -> characters -> FX until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
