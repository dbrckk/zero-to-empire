# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **121 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09 09:01 +02:00
- Fully reconciled aggregate before the current FX-13 promotion: **121 / 235 strict DONE**; Buildings 23/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 4/18.
- Reconcile Sprite Progress Ledger run `34321406718` completed SUCCESS after FX-12 and synchronized manifest/progress/continuity to 121.

## Latest intervention — FX-13 strict evidence audit and canonical promotion
- Audited `FX-13 — phase distortion` provenance from commit `4cac096866878ddd0aa05307aa4357e5bdbc1800` (`art: add final phase distortion FX`).
- Production ledger records the accepted atlas as **8 x 128x128 RGBA, 4x2**, **70.0% transparent**, with every cell populated and isolated.
- `PhaseDistortion.kt` decodes `R.drawable.zte_fx_13_final`, uses exactly 8 frames / 4 columns / 128px cells at 125ms per frame, and freezes frame 0 under reduced motion.
- Active gameplay visibility is explicit: `WorldBusinessVisual` invokes `PhaseDistortion` for business 10 at tier >= 4 in the active city rendering route.
- FX-13 runtime/call-site code predates and is unchanged in Android CI #628 / run `34317783009`, which completed SUCCESS and supplies the descendant green build/test/lint gate.
- One-off promotion workflow `.github/workflows/promote-fx13-strict.yml`, commit `9b6c33151c0da13d718f221e3fc7cd95ecd0c313`, completed SUCCESS as run `34321571309`; bot commit `431b87367b42a9785ed629460d1aba2cc2fbdf32` changed only FX-13 from RUNTIME to DONE after verifying the exact manifest row, runtime resource and active call site.
- This continuity update intentionally triggers canonical reconciliation. Do not report **122 / 235** until that reconciliation succeeds.

## Previous strict promotions
- FX-12 drone thruster: provenance `07f07302a1a4c08a4da1ed22ffacdf26fe8c13e7`; 8x128 RGBA 4x2, 82.5% transparent, isolated cells; active business 9 tier>=4; promotion run `34321311693`; reconciliation `34321406718`; strict state became 121.
- FX-11 hologram scan sweep: provenance `e254506bb6f86537dffbd6970dc85df8d01434d6`; 8x128 RGBA 4x2, 65.1% transparent, isolated cells after one rejected bloom-contaminated attempt; active business 8 tier>=4; promotion run `34321018016`; reconciliation `34321131681`.
- FX-10 electric arc: provenance `2a0684b154f6e0243322ddf35ecb0e9157cf5e41`; 8x128 RGBA 4x2, 93.4% transparent, isolated cells; active business 7 tier>=4; promotion run `34319279960`.
- FX-09 income pickup sparkle: provenance `93e6ba0350da934a9e29e3848b1a0f61542989e5`; 8x128 RGBA 4x2, 93.9% transparent, isolated cells; active business 6 tier>=4; promotion run `34318904226`.
- BLD-03 T2-T6: run75 semantic approval + 5/5 technical QA + active canonical renderer + Android CI #628 green.

## Reconciliation infrastructure
- `.github/workflows/reconcile-sprite-progress-ledger.yml` was hardened in commit `0a4c4de24c725afad5e9a721d15c9343000a2c95` to derive aggregate state from the stable primary continuity anchor.
- Recent reconciliation runs `34321131681` and `34321406718` both succeeded.

## Remaining reconciliation lane
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1` remain RUNTIME pending explicit semantic provenance.
- Continue auditing FX-14 through FX-17 individually; no blanket promotion.
- FX-08 requires its own audit.

## GPU state / blockers
- Kaggle credentials/push work, but wave88 runtime DNS could not resolve `github.com`; do not retrigger unchanged until notebook UI proves usable GPU + Internet.
- Lightning AI Studio CLI works but requested T4 accelerator was unavailable in that cluster; no Lightning GPU execution yet.
- Building generator v16.4 (`fa41f56442a2e62227045b272676780c5a8f5ca8`) remains unexecuted cleanly.

## Next actions
1. Reconcile FX-13 promotion; only then accept 122/235.
2. Audit FX-14, then FX-15..17 individually.
3. Audit BLD-02-T4..T6 and BLD-03-T0..T1 semantic provenance.
4. Audit FX-08 separately.
5. Do not retry Kaggle until GPU + Internet are actually usable.
6. Continue until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
