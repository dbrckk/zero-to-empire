# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **112 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09
- **112 / 235 strict DONE**. No strict increment in this intervention.
- Canonical ledger family totals after reconciliation: Buildings 18/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 0/18.
- `Reconcile Sprite Progress Ledger` runs `34301830088` and `34301864372` both completed **SUCCESS**. Aggregate continuity/manifest drift guard is operational.

## Latest intervention — BLD-02/03 canonical resources compile-time bound
- Verified Android CI #625 / run `34309140201` completed **SUCCESS**, validating the previously added 8-gameplay-stage → 7-canonical-tier contract and its boundary tests.
- Verified all BLD-02 and BLD-03 canonical runtime WebPs `zte_business_02_t0..t6_final.webp` and `zte_business_03_t0..t6_final.webp` exist under `app/src/main/res/drawable-nodpi/` with non-zero sizes.
- Added `app/src/main/java/com/zerotoempire/game/CanonicalBusinessRaster.kt`, commit `e5cf2cd73c8184586fe18ba47cf3399625fc4ad4`. It compile-time binds business ID 2 (BLD-02 / Workshop) and ID 3 (BLD-03 / Factory) to all seven canonical Android drawable resources through `canonicalBusinessTier(level)`. Unsupported Group-01 business IDs intentionally return null and retain their existing renderer.
- Added `app/src/test/java/com/zerotoempire/game/CanonicalBusinessRasterTest.kt`, commit `010f743205f33e00a6695be7467045ef8eb697ae`. Tests require both businesses to resolve every gameplay milestone, require 500/1000 to share T6, require seven distinct tier resources, and require unsupported business IDs to remain unresolved.
- Android CI #626 / run `34313359325` was **in progress** at last inspection for the resource-binding commit. Android CI #627 / run `34313368691` was **queued** for the mapping tests. A later intervention must verify final conclusions and repair immediately on failure.
- This is a material integration prerequisite, but it is **not yet runtime visibility**: `BusinessGroup01Art.kt` still calls procedural `drawWorkshopAAA` / `drawFactoryAAA`. Therefore no BLD-02/03 row is promoted to strict DONE in this intervention.

## Canonical business progression contract
- `app/src/main/java/com/zerotoempire/game/CanonicalBusinessTier.kt`, commit `f85c4ea5474d0e7e779e0341bf995ab74ef1c113`, maps levels `<10 -> T0`, `10..24 -> T1`, `25..49 -> T2`, `50..99 -> T3`, `100..249 -> T4`, `250..499 -> T5`, `>=500 -> T6`.
- Gameplay milestones `0,10,25,50,100,250,500,1000` therefore map exactly to `T0,T1,T2,T3,T4,T5,T6,T6`; the final two milestones intentionally share T6 rather than inventing a non-canonical T7.
- `CanonicalBusinessTierTest.kt`, commit `1fade114a205ded2c475397f78a8ab92761db4aa`, locks milestone and boundary behavior including negative and `Int.MAX_VALUE` inputs.

## Android CI baseline
- Run `34283943481` (#622) failed before compilation because the repository had no root `gradlew` while the workflow tried `chmod +x gradlew`.
- Commit `de1f0df61f2793aa6dcdb4ebcca3aec7ad6f4e09` changed Android CI to provision Gradle 8.13 explicitly.
- Run `34288618789` (#623) subsequently passed APK build, unit tests, lint and artifact upload.
- Commit `d3ec47365f82a47f12cd41f3d740517f1ef28a25` expanded Android CI path coverage to `art/production/**` and the canonical sprite manifest.

## Ledger safeguards
- `.github/workflows/reconcile-sprite-progress-ledger.yml` derives aggregates exclusively from the 235 canonical rows, checks uniqueness/family totals, synchronizes the manifest footer and continuity strict count, and never changes individual TODO/RUNTIME/DONE statuses.
- Run `34293344248` reconciled the previously stale manifest aggregate to 112/235.

## Productive reconciliation lane
- BLD-02 T4–T6 and BLD-03 T0–T6 are canonical `RUNTIME`; they require active canonical WebP runtime rendering + visibility + green Android CI before DONE.
- BLD-03 T2–T6 were previously evidence-reconciled to RUNTIME by run `34278218123` and commit `1acf87c70e3dd7722a748a3eba4a01e76249f79e`.
- FX-08..17 are canonical `RUNTIME`; audit runtime call sites/visibility before any promotion.

## GPU state / blockers
- Kaggle new-account credentials are valid and kernel push works, but accepted GPU job wave 88 failed because runtime DNS/network access could not resolve `github.com` (`Could not resolve host: github.com`). Do not retrigger unchanged until notebook UI proves both usable GPU and Internet.
- Lightning AI Studio exists and CLI access works, but attempted `lit-t4-1` accelerator was unavailable for the cluster. No Lightning GPU execution has occurred.
- Building generator v16.4 remains committed at `tools/sprites/kaggle_building_family_factory_v16.py` (`fa41f56442a2e62227045b272676780c5a8f5ca8`) but has not executed cleanly.

## Next actions
1. Verify Android CI #626 `34313359325` and #627 `34313368691`; repair immediately if compile-time resource binding or tests fail.
2. Replace BLD-02/03 procedural base rendering inside `BusinessGroup01Art.kt` with `Image(painterResource(canonicalBusinessRasterRes(...)))` or an equivalent canonical raster path, while preserving progression overlays only when they do not obscure the canonical art.
3. Add explicit runtime-reference evidence and obtain green Android CI after renderer wiring; only then assess each BLD-02/03 RUNTIME row for strict DONE promotion.
4. Audit FX-08..17 runtime call sites and visibility next.
5. Do not retry Kaggle until GPU + Internet are actually usable.
6. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
