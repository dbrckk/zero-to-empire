# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **120 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09 08:54 +02:00
- Last fully reconciled aggregate: **119 / 235 strict DONE**; Buildings 23/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 2/18.
- Reconcile Sprite Progress Ledger run `34319385940` completed SUCCESS for that 119-state.

## Latest intervention — FX-11 strict evidence audit and canonical promotion
- Audited `FX-11 — hologram scan sweep` provenance from commit `e254506bb6f86537dffbd6970dc85df8d01434d6` (`art: add final hologram scan FX`).
- Production ledger records the accepted atlas as **8 x 128x128 RGBA, 4x2**, **65.1% transparent**, every cell populated and isolated. An earlier FX-11 attempt was explicitly rejected because ambient cyan bloom connected multiple cells and eliminated transparent gutters.
- `HologramScanSweep.kt` decodes `R.drawable.zte_fx_11_final`, uses exactly 8 frames / 4 columns / 128px cells at 125ms per frame, and freezes frame 0 under reduced motion.
- Active gameplay visibility is explicit: `WorldBusinessVisual` invokes `HologramScanSweep` for business 8 at tier >= 4 in the active city rendering route.
- FX-11 runtime/call-site code predates and is unchanged in Android CI #628 / run `34317783009`, which completed SUCCESS and supplies the descendant green build/test/lint gate.
- One-off promotion workflow `.github/workflows/promote-fx11-strict.yml`, commit `3daa956faf030e95d7c16b4a274bbb219bcf614b`, completed SUCCESS as run `34321018016`; it verified the exact manifest row, runtime resource and active call site before committing only FX-11 from RUNTIME to DONE.
- This continuity update intentionally triggers canonical reconciliation. Do not report **120 / 235** until reconciliation succeeds.

## Previous strict promotions
- FX-10 electric arc: provenance `2a0684b154f6e0243322ddf35ecb0e9157cf5e41`; 8x128 RGBA 4x2, 93.4% transparent, isolated cells; active business 7 tier>=4; promotion run `34319279960`; reconciliation `34319385940`; strict state became 119.
- FX-09 income pickup sparkle: provenance `93e6ba0350da934a9e29e3848b1a0f61542989e5`; 8x128 RGBA 4x2, 93.9% transparent, isolated cells; active business 6 tier>=4; promotion run `34318904226`.
- BLD-03 T2-T6: run75 semantically approved, 5/5 technical QA pass, active canonical renderer, Android CI #628 green; manifest promotion/reconciliation established 117 before FX promotions.

## Remaining reconciliation lane
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1` remain RUNTIME. Runtime visibility is proven, but do not promote until their own semantic + technical evidence is explicitly established.
- Continue auditing FX-12 through FX-17 individually; no blanket promotion.
- FX-08 requires its own audit.

## Canonical business progression contract
- `CanonicalBusinessTier.kt`: `<10 T0`, `10..24 T1`, `25..49 T2`, `50..99 T3`, `100..249 T4`, `250..499 T5`, `>=500 T6`.
- `CanonicalBusinessRaster.kt` compile-time binds BLD-02/03 resources; mapping/boundary tests are green on Android CI #627 / run `34313368691`.

## GPU state / blockers
- Kaggle new-account credentials are valid and kernel push works, but wave88 failed because runtime DNS/network access could not resolve `github.com`. Do not retrigger unchanged until notebook UI proves both usable GPU and Internet.
- Lightning AI Studio exists and CLI access works, but `lit-t4-1` was unavailable in that cluster. No Lightning GPU execution has occurred.
- Building generator v16.4 remains committed at `fa41f56442a2e62227045b272676780c5a8f5ca8` and has not executed cleanly.

## Next actions
1. Reconcile FX-11 promotion; only then accept 120/235.
2. Audit FX-12, then FX-13..17 individually; promote only complete strict-gate rows.
3. Audit BLD-02-T4..T6 and BLD-03-T0..T1 semantic provenance.
4. Audit FX-08 separately.
5. Do not retry Kaggle until GPU + Internet are actually usable.
6. Continue until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
