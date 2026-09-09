# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **118 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09 08:26 +02:00
- **118 / 235 strict DONE**. Canonical aggregate derived from the 235 manifest rows.
- Last fully reconciled family totals: Buildings 23/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 0/18.
- Reconcile Sprite Progress Ledger run `34318256472` completed **SUCCESS** for the previous 117-state.

## Latest intervention — FX-09 strict evidence audit and canonical promotion
- Audited `FX-09 — income pickup sparkle` provenance from commit `93e6ba0350da934a9e29e3848b1a0f61542989e5`.
- The production ledger in that commit records the accepted sheet as **8 x 128x128 RGBA, 4x2**, **93.9% transparent**, with every cell populated and isolated. Two earlier attempts were explicitly rejected for frame fragmentation and edge clipping before the accepted version was retained.
- `IncomePickupSparkle.kt` decodes `R.drawable.zte_fx_09_final`, advances exactly 8 frames from a 4-column 128px atlas, and freezes to frame 0 under reduced motion.
- Active gameplay visibility is explicit: `WorldBusinessVisual` invokes `IncomePickupSparkle` for business 6 at tier >= 4. This route is reached from the active `AscendantCityEmpireWorld` business rendering path.
- The FX-09 runtime file and call site are unchanged in Android CI #628 / run `34317783009`, which completed **SUCCESS**; this supplies the descendant green Android build/test/lint gate for the audited asset.
- One-off promotion workflow `.github/workflows/promote-fx09-strict.yml`, commit `88a1a0635c4f698fb4af65097bc1854eb923398e`, completed **SUCCESS** as run `34318904226` and produced bot commit `6224b995643685c2be910c832779e9c3ad88fc3b`, changing only FX-09 from `RUNTIME` to canonical `DONE`.
- This continuity update intentionally triggers `Reconcile Sprite Progress Ledger`; do not claim the aggregate as 118 until that reconciliation succeeds and synchronizes manifest/progress/continuity.

## Previous completed intervention — BLD-03 T2–T6 strict DONE
- Android CI #628 / run `34317783009` completed **SUCCESS** for commit `cc06340730e7a81316dfa6b5bdd36dbec8b0ff3f`, proving the active canonical BLD-02/03 renderer compiles/tests/lints successfully.
- Active runtime chain: `PremiumZeroToEmpireApp` -> `AscendantCityEmpireWorld` -> `AscendantHeroLot` / `AscendantWorldLot` -> `WorldBusinessVisual` -> `canonicalBusinessRasterRes` -> canonical Android WebP -> Compose `Image`.
- Run75 promotion workflow explicitly selected only semantically approved `BLD-03-T2` through `BLD-03-T6`; integration commit `e14b6897e32a557736a4e9c06d55b925864993d1` preserved the five masters/runtime WebPs and technical QA reports 5/5 automatic pass with clean edges.
- Manifest repair/promotion workflow run `34318174752` completed SUCCESS and bot commit `30010d66ee94748a97055a0b1ddf4c79faf752a4` promoted only the five proven rows.
- Reconciliation run `34318256472` completed SUCCESS, establishing **117 / 235** before the FX-09 promotion.

## Remaining reconciliation lane
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1` remain `RUNTIME`. Runtime visibility is proven, but do not promote until their own semantic + technical evidence is explicitly established.
- Continue auditing `FX-10` through `FX-17` individually. Do not blanket-promote the lane; each row needs identity-specific semantic evidence, technical QA, active call-site proof and green descendant CI.
- `FX-08` also requires a separate audit; it is not covered by the FX-09 evidence.

## Canonical business progression contract
- `CanonicalBusinessTier.kt`, commit `f85c4ea5474d0e7e779e0341bf995ab74ef1c113`: `<10 T0`, `10..24 T1`, `25..49 T2`, `50..99 T3`, `100..249 T4`, `250..499 T5`, `>=500 T6`.
- Gameplay milestones `0,10,25,50,100,250,500,1000` map to `T0,T1,T2,T3,T4,T5,T6,T6`.
- `CanonicalBusinessRaster.kt`, commit `e5cf2cd73c8184586fe18ba47cf3399625fc4ad4`, compile-time binds BLD-02/03 resources.
- Mapping/boundary tests are green on Android CI #627 / run `34313368691`.

## Android CI baseline
- Root-wrapper failure from #622 was repaired by commit `de1f0df61f2793aa6dcdb4ebcca3aec7ad6f4e09`, which provisions Gradle 8.13 explicitly.
- #623 passed APK build, unit tests, lint and artifact upload.
- #628 passed after live canonical BLD-02/03 renderer integration and contains unchanged FX-09 runtime/call-site code.

## GPU state / blockers
- Kaggle new-account credentials are valid and kernel push works, but wave88 failed because runtime DNS/network access could not resolve `github.com`. Do not retrigger unchanged until notebook UI proves both usable GPU and Internet.
- In the user-visible Kaggle notebook UI, GPU T4 x2 / P100 were still grayed at last check; phone verification was requested but not yet confirmed.
- Lightning AI Studio exists and CLI access works, but `lit-t4-1` was unavailable in that cluster. No Lightning GPU execution has occurred.
- Building generator v16.4 remains committed at `fa41f56442a2e62227045b272676780c5a8f5ca8` and has not executed cleanly.

## Next actions
1. Verify the reconciliation triggered by this continuity update; expected canonical aggregate if successful: **118 / 235**, FX **1 / 18**.
2. Audit FX-10 next, then FX-11..17 individually; promote only complete strict-gate rows.
3. Audit `BLD-02-T4..T6` and `BLD-03-T0..T1` semantic provenance; do not infer semantic acceptance from technical PASS alone.
4. Do not retry Kaggle until GPU + Internet are actually usable.
5. Continue buildings -> statics -> characters -> FX until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
