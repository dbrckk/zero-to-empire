# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-08
- **112 / 235 strict DONE**.
- Runs 80–85: strict delta +0.

## Building generator v16.3
`tools/sprites/kaggle_building_family_factory_v16.py`, commit `60656bdaa97e7a4821fb115472c31803eb6ba509`.
Startup confirmed in wave85 logs: `building-family-flux-v16.3-isolated-static-source`.
Goal was to eliminate floor/site pads, cast-shadow cards, detached props and baked FX at generation source while preserving v16.2's reduction in crane/gantry contamination.

## Wave 85 — TERMINAL ERROR, EVIDENCE RECOVERED
- Source run `34224023209`, original job `102053645197`.
- Recovery attempt 3: run `34249420747`, job `102139713593`, completed workflow success because recovery mechanics worked.
- Kaggle itself became `KernelWorkerStatus.ERROR` at 16:40:58Z; recovery reports `RECOVERY_FINAL_STATUS=ERROR`.
- Artifact `10066542877` recovered successfully, 20,452 bytes.
- Artifact contains only `zero-to-empire-sprite-factory.log` and `output/branch-search-report.json`; there are no PNG candidates/contact sheets/generated-targets/batch QA outputs.
- v16.3 startup is explicitly present in the log.
- Final counters: `KAGGLE_BUILDING_SUCCESS=0`, `KAGGLE_BUILDING_REJECTED=56`, `KAGGLE_BUILDING_ATTEMPTED=56`, `KAGGLE_FRESH_CANDIDATES=0`.
- Branch search: 48 anchor attempts, 16 branch attempts, 124 context attempts, 67 live rejections, 16 early aborts. Families 4,5,8,9,10,11,12,13 all `accepted=false` and `branches_completed=0`.
- Dominant observed failure remains ground/slab contamination. Example late failures: BLD-12-T5 slab 0.24–0.26; BLD-13-T5 slab 0.28–0.46. T0 also repeatedly retried for `ground slab`.
- Important interpretation: this is now a genuine generation/acceptance failure, not merely a collector timeout. v16.3 improved source instructions but did not solve the slab prior strongly enough to yield even one complete family.
- No strict increment from wave85.

## Wave84 baseline
Recovery artifact `10053866830`: v16.2 exported BLD-11/12/13 T0–T6 (21 technical candidates), semantic acceptance 0/21. Main remaining defects: slabs/ground patches, detached residue/props and baked FX.

## Next generator objective
Do NOT rerun v16.3 unchanged. Build v16.4 around a source-level architectural change rather than more rejection wording: reduce/remodel the model's ground-plane prior, use tighter object-centric source/anchor conditioning, preserve a compact sealed foundation footprint, lower late-tier evolution drift, and separate massing from detail so T5/T6 cannot invent site slabs. Recalibrate slab QA only after visual/source behavior improves; do not simply weaken the gate to manufacture yield.

## CircleCI
`.circleci/config.yml` contains a long recovery lane, but no CircleCI status has been observed on GitHub. Do not assume it is executing.

## Other prepared lanes
- Character: `tools/sprites/kaggle_character_sheet_factory_v1.py`, canonical 1024×1024 RGBA 4×4 atlas.
- FX: `tools/sprites/kaggle_fx_sheet_factory_v1.py`, runtime 8-frame 4×2 512×256 atlas.

## Next actions
1. Inspect v16.3 source around prompt construction, alpha/background extraction, anchor selection, tier evolution and slab scoring.
2. Implement v16.4 source-level anti-ground strategy; do not merely add negative prompt tokens.
3. Trigger a fresh building wave only after v16.4 is committed and routing/startup updated.
4. On outputs, semantically inspect every complete family and compare accepted-family yield against wave84 0/3 and wave85 0/8.
5. Promote only complete valid families; strict increment only after runtime + manifest/progress + green Android CI.
6. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
