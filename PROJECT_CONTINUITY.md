# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **125 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09 10:33 +02:00
- Fully reconciled aggregate: **124 / 235 strict DONE**; Buildings 23/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 7/18.
- Reconcile Sprite Progress Ledger run `34329526375` completed SUCCESS after FX-15 and synchronized manifest/progress/continuity to 124.

## Latest intervention — FX-16 strict evidence audit and canonical promotion
- Audited `FX-16 — singularity lens pulse` provenance from commit `58444287c9ab76f53dedb40730c95731502cebd9` (`art: integrate pending foundry sprites and apex FX`).
- Production ledger records the accepted atlas as **8 x 128x128 RGBA, 4x2**, **76.3% transparent**, with every cell populated and isolated.
- `SingularityLensPulse.kt` decodes `R.drawable.zte_fx_16_final`, uses exactly 8 frames / 4 columns / 128px cells at 125ms per frame, and freezes frame 0 under reduced motion.
- Active gameplay visibility is explicit: `WorldBusinessVisual` invokes `SingularityLensPulse` for Apex business 13 at tier >= 4 in the active city rendering route.
- FX-16 runtime/call-site code predates and is unchanged in Android CI #628 / run `34317783009`, which completed SUCCESS and supplies the descendant green build/test/lint gate.
- One-off promotion workflow `.github/workflows/promote-fx16-strict.yml`, commit `13cd59ad50d72eebff4e5ef934be15063be9023f`, completed SUCCESS as run `34329600834`; bot commit `2cf353d239e53f4c4eac0ee1ad408a90e8ce4763` changed only FX-16 from RUNTIME to DONE after verifying the exact manifest row, runtime resource and active call site.
- This continuity update intentionally triggers canonical reconciliation. Do not report **125 / 235** until that reconciliation succeeds.

## Previous strict promotions
- FX-15 stellar flare: provenance `58444287c9ab76f53dedb40730c95731502cebd9`; 8x128 RGBA 4x2, 66.8% transparent, isolated cells; active business 12 tier>=4; promotion run `34329411998`; reconciliation `34329526375`; strict state became 124.
- FX-14 orbital ion trail: provenance `d361322ac5541e44317c98734eadfc36db328a9a`; active business 11 tier>=4; promotion run `34329210343`; reconciliation `34329311278`.
- FX-13 phase distortion: provenance `4cac096866878ddd0aa05307aa4357e5bdbc1800`; active business 10 tier>=4; promotion run `34321571309`; reconciliation `34321649961`.
- FX-12, FX-11, FX-10 and FX-09 are strict DONE through their audited semantic/technical/runtime/CI lanes.
- BLD-03 T2-T6: run75 semantic approval + 5/5 technical QA + active canonical renderer + Android CI #628 green.

## Remaining reconciliation lane
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1` remain RUNTIME pending explicit semantic provenance.
- Audit FX-17 individually; no blanket promotion.
- FX-08 requires its own audit.

## GPU state / blockers
- Kaggle credentials/push work, but wave88 runtime DNS could not resolve `github.com`; do not retrigger unchanged until notebook UI proves usable GPU + Internet.
- Lightning AI Studio CLI works but requested T4 accelerator was unavailable in that cluster; no Lightning GPU execution yet.
- Building generator v16.4 (`fa41f56442a2e62227045b272676780c5a8f5ca8`) remains unexecuted cleanly.

## Next actions
1. Reconcile FX-16 promotion; only then accept 125/235.
2. Audit FX-17 individually.
3. Audit BLD-02-T4..T6 and BLD-03-T0..T1 semantic provenance.
4. Audit FX-08 separately.
5. Do not retry Kaggle until GPU + Internet are actually usable.
6. Continue until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
