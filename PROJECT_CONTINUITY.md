# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **123 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09 10:31 +02:00
- Fully reconciled aggregate: **123 / 235 strict DONE**; Buildings 23/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 6/18.
- Reconcile Sprite Progress Ledger run `34329311278` completed SUCCESS after FX-14 and synchronized manifest/progress/continuity to 123.

## Latest intervention — FX-15 strict evidence audit and canonical promotion
- Audited `FX-15 — stellar flare` provenance from commit `58444287c9ab76f53dedb40730c95731502cebd9` (`art: integrate pending foundry sprites and apex FX`).
- Production ledger records the accepted atlas as **8 x 128x128 RGBA, 4x2**, **66.8% transparent**, with every cell populated and isolated.
- `StellarFlare.kt` decodes `R.drawable.zte_fx_15_final`, uses exactly 8 frames / 4 columns / 128px cells at 125ms per frame, and freezes frame 0 under reduced motion.
- Active gameplay visibility is explicit: `WorldBusinessVisual` invokes `StellarFlare` for Apex business 12 at tier >= 4 in the active city rendering route.
- FX-15 runtime/call-site code predates and is unchanged in Android CI #628 / run `34317783009`, which completed SUCCESS and supplies the descendant green build/test/lint gate.
- One-off promotion workflow `.github/workflows/promote-fx15-strict.yml`, commit `9a547055516fb0de7649ac69714c157ff2bbb38d`, completed SUCCESS as run `34329411998`; bot commit `8d7e1e4a31385b04ade77057419f9899ca5e31bf` changed only FX-15 from RUNTIME to DONE after verifying the exact manifest row, runtime resource and active call site.
- This continuity update intentionally triggers canonical reconciliation. Do not report **124 / 235** until that reconciliation succeeds.

## Previous strict promotions
- FX-14 orbital ion trail: provenance `d361322ac5541e44317c98734eadfc36db328a9a`; 8x128 RGBA 4x2, transparent/isolated cells; active business 11 tier>=4; promotion run `34329210343`; reconciliation `34329311278`; strict state became 123.
- FX-13 phase distortion: provenance `4cac096866878ddd0aa05307aa4357e5bdbc1800`; 8x128 RGBA 4x2, 70.0% transparent, isolated cells; active business 10 tier>=4; promotion run `34321571309`; reconciliation `34321649961`.
- FX-12 drone thruster: provenance `07f07302a1a4c08a4da1ed22ffacdf26fe8c13e7`; 8x128 RGBA 4x2, 82.5% transparent, isolated cells; active business 9 tier>=4; promotion run `34321311693`; reconciliation `34321406718`.
- FX-11 hologram scan sweep: provenance `e254506bb6f86537dffbd6970dc85df8d01434d6`; 8x128 RGBA 4x2, 65.1% transparent, isolated cells; active business 8 tier>=4; promotion run `34321018016`; reconciliation `34321131681`.
- FX-10 electric arc and FX-09 income pickup sparkle are strict DONE through their audited runtime/QA lanes.
- BLD-03 T2-T6: run75 semantic approval + 5/5 technical QA + active canonical renderer + Android CI #628 green.

## Remaining reconciliation lane
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1` remain RUNTIME pending explicit semantic provenance.
- Continue auditing FX-16 and FX-17 individually; no blanket promotion.
- FX-08 requires its own audit.

## GPU state / blockers
- Kaggle credentials/push work, but wave88 runtime DNS could not resolve `github.com`; do not retrigger unchanged until notebook UI proves usable GPU + Internet.
- Lightning AI Studio CLI works but requested T4 accelerator was unavailable in that cluster; no Lightning GPU execution yet.
- Building generator v16.4 (`fa41f56442a2e62227045b272676780c5a8f5ca8`) remains unexecuted cleanly.

## Next actions
1. Reconcile FX-15 promotion; only then accept 124/235.
2. Audit FX-16, then FX-17 individually.
3. Audit BLD-02-T4..T6 and BLD-03-T0..T1 semantic provenance.
4. Audit FX-08 separately.
5. Do not retry Kaggle until GPU + Internet are actually usable.
6. Continue until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
