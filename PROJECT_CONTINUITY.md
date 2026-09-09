# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **117 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09 08:16 +02:00
- **117 / 235 strict DONE**. Canonical aggregate derived from the 235 manifest rows.
- Canonical family totals: Buildings 23/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 0/18.
- Reconcile Sprite Progress Ledger run `34318256472` completed **SUCCESS** after the strict promotion and synchronized manifest/progress/continuity aggregates.

## Latest intervention — BLD-03 T2–T6 promoted strict DONE
- Android CI #628 / run `34317783009` completed **SUCCESS** for commit `cc06340730e7a81316dfa6b5bdd36dbec8b0ff3f`, proving the active canonical BLD-02/03 renderer compiles/tests/lints successfully.
- Active runtime chain: `PremiumZeroToEmpireApp` -> `AscendantCityEmpireWorld` -> `AscendantHeroLot` / `AscendantWorldLot` -> `WorldBusinessVisual` -> `canonicalBusinessRasterRes` -> canonical Android WebP -> Compose `Image`.
- Run75 promotion workflow explicitly selected only semantically approved `BLD-03-T2` through `BLD-03-T6`; integration commit `e14b6897e32a557736a4e9c06d55b925864993d1` preserved the five masters/runtime WebPs and technical QA reports 5/5 automatic pass with clean edges.
- With semantic approval, technical QA, final runtime files, active gameplay visibility and green Android CI all proven, `BLD-03-T2` through `BLD-03-T6` are now canonical **DONE**.
- Strict count increased **112 -> 117**.
- Manifest repair/promotion workflow run `34318174752` completed SUCCESS and commit `30010d66ee94748a97055a0b1ddf4c79faf752a4` restored the complete manifest while promoting only the five proven rows.
- Reconciliation workflow was hardened in commit `19b69d7481aef2adc4722eecbe087092aa8b8053` so manifest, progress and continuity counts are synchronized from the 235 canonical rows; run `34318256472` completed SUCCESS.

## Remaining reconciliation lane
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1` remain `RUNTIME`. Runtime visibility is proven, but do not promote until their own semantic + technical evidence is explicitly established.
- `FX-08` through `FX-17` remain `RUNTIME`; audit active call sites/visibility and semantic/technical evidence next.

## Canonical business progression contract
- `CanonicalBusinessTier.kt`, commit `f85c4ea5474d0e7e779e0341bf995ab74ef1c113`: `<10 T0`, `10..24 T1`, `25..49 T2`, `50..99 T3`, `100..249 T4`, `250..499 T5`, `>=500 T6`.
- Gameplay milestones `0,10,25,50,100,250,500,1000` map to `T0,T1,T2,T3,T4,T5,T6,T6`.
- `CanonicalBusinessRaster.kt`, commit `e5cf2cd73c8184586fe18ba47cf3399625fc4ad4`, compile-time binds BLD-02/03 resources.
- Mapping/boundary tests are green on Android CI #627 / run `34313368691`.

## Android CI baseline
- Root-wrapper failure from #622 was repaired by commit `de1f0df61f2793aa6dcdb4ebcca3aec7ad6f4e09`, which provisions Gradle 8.13 explicitly.
- #623 passed APK build, unit tests, lint and artifact upload.
- #628 passed after live canonical BLD-02/03 renderer integration.

## GPU state / blockers
- Kaggle new-account credentials are valid and kernel push works, but wave88 failed because runtime DNS/network access could not resolve `github.com`. Do not retrigger unchanged until notebook UI proves both usable GPU and Internet.
- In the user-visible Kaggle notebook UI, GPU T4 x2 / P100 were still grayed at last check; phone verification was requested but not yet confirmed.
- Lightning AI Studio exists and CLI access works, but `lit-t4-1` was unavailable in that cluster. No Lightning GPU execution has occurred.
- Building generator v16.4 remains committed at `fa41f56442a2e62227045b272676780c5a8f5ca8` and has not executed cleanly.

## Next actions
1. Audit `BLD-02-T4..T6` and `BLD-03-T0..T1` semantic/technical provenance; promote only rows with complete evidence.
2. Audit `FX-08..17` active runtime call sites/visibility and provenance; promote only complete strict-gate rows.
3. Do not retry Kaggle until GPU + Internet are actually usable.
4. Continue buildings -> statics -> characters -> FX until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
