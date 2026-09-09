# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **121 / 235 canonical final sprites strict DONE** toward **235 / 235**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI. Never promote from file presence alone.

## Trusted state — 2026-09-09 08:58 +02:00
- Last fully reconciled aggregate: **120 / 235 strict DONE**; Buildings 23/98, Power Core 7/7, Characters 0/24, Vehicles 18/18, Machines 28/28, Props 28/28, Terrain/infrastructure 13/14, FX 3/18.
- Reconcile Sprite Progress Ledger run `34321131681` completed SUCCESS after the FX-11 promotion and synchronized the canonical aggregate to 120.

## Latest intervention — FX-12 strict evidence audit and canonical promotion
- Audited `FX-12 — drone thruster` provenance from commit `07f07302a1a4c08a4da1ed22ffacdf26fe8c13e7` (`art: add final drone thruster FX`).
- Production ledger records the accepted atlas as **8 x 128x128 RGBA, 4x2**, **82.5% transparent**, every cell populated and isolated.
- `DroneThruster.kt` decodes `R.drawable.zte_fx_12_final`, uses exactly 8 frames / 4 columns / 128px cells at 125ms per frame, and freezes frame 0 under reduced motion.
- Active gameplay visibility is explicit: `WorldBusinessVisual` invokes `DroneThruster` for business 9 at tier >= 4 in the active city rendering route.
- FX-12 runtime/call-site code predates and is unchanged in Android CI #628 / run `34317783009`, which completed SUCCESS and supplies the descendant green build/test/lint gate.
- One-off promotion workflow `.github/workflows/promote-fx12-strict.yml`, commit `d612fc78bca5f3e309ba6799de723cee0fb5c062`, completed SUCCESS as run `34321311693`; bot commit `67233846bab3d44e618a866aadcba8bb713e6d61` changed only FX-12 from RUNTIME to DONE after verifying the exact manifest row, runtime resource and active call site.
- This continuity update intentionally triggers canonical reconciliation. Do not report **121 / 235** until that reconciliation succeeds.

## Previous strict promotions
- FX-11 hologram scan sweep: provenance `e254506bb6f86537dffbd6970dc85df8d01434d6`; 8x128 RGBA 4x2, 65.1% transparent, isolated cells after one rejected bloom-contaminated attempt; active business 8 tier>=4; promotion run `34321018016`; reconciliation `34321131681`; strict state became 120.
- FX-10 electric arc: provenance `2a0684b154f6e0243322ddf35ecb0e9157cf5e41`; 8x128 RGBA 4x2, 93.4% transparent, isolated cells; active business 7 tier>=4; promotion run `34319279960`.
- FX-09 income pickup sparkle: provenance `93e6ba0350da934a9e29e3848b1a0f61542989e5`; 8x128 RGBA 4x2, 93.9% transparent, isolated cells; active business 6 tier>=4; promotion run `34318904226`.
- BLD-03 T2-T6: run75 semantic approval + 5/5 technical QA + active canonical renderer + Android CI #628 green.

## Reconciliation infrastructure
- `.github/workflows/reconcile-sprite-progress-ledger.yml` was hardened in commit `0a4c4de24c725afad5e9a721d15c9343000a2c95` to derive aggregate state from the stable primary continuity anchor instead of a fragile secondary status sentence.
- Run `34321131681` succeeded with that implementation.

## Remaining reconciliation lane
- `BLD-02-T4`, `BLD-02-T5`, `BLD-02-T6`, `BLD-03-T0`, `BLD-03-T1` remain RUNTIME pending explicit semantic provenance.
- Continue auditing FX-13 through FX-17 individually; no blanket promotion.
- FX-08 requires its own audit.

## GPU state / blockers
- Kaggle credentials/push work, but wave88 runtime DNS could not resolve `github.com`; do not retrigger unchanged until notebook UI proves usable GPU + Internet.
- Lightning AI Studio CLI works but requested T4 accelerator was unavailable in that cluster; no Lightning GPU execution yet.
- Building generator v16.4 (`fa41f56442a2e62227045b272676780c5a8f5ca8`) remains unexecuted cleanly.

## Next actions
1. Reconcile FX-12 promotion; only then accept 121/235.
2. Audit FX-13, then FX-14..17 individually.
3. Audit BLD-02-T4..T6 and BLD-03-T0..T1 semantic provenance.
4. Audit FX-08 separately.
5. Do not retry Kaggle until GPU + Internet are actually usable.
6. Continue until **235 / 235**.

## Operating principle
Generate/integrate the right asset first; QA confirms rather than inflates. Optimize validated semantic yield, preserve evidence, and never increase strict DONE without every gate.
