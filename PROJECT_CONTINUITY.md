# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-08
- **112 / 235 strict DONE**.
- Runs 80–84: strict delta +0.

## Building generator v16.3
`tools/sprites/kaggle_building_family_factory_v16.py`, commit `60656bdaa97e7a4821fb115472c31803eb6ba509`.
Startup: `building-family-flux-v16.3-isolated-static-source`.
Goal: eliminate floor/site pads, cast-shadow cards, detached props and baked FX at generation source while preserving v16.2's reduction in crane/gantry contamination.

## Wave 85 — KERNEL STILL RUNNING; RECOVERY ATTEMPT 2 REQUESTED
- Source run `34224023209`, original job `102053645197`.
- Original GitHub collector expired while Kaggle remained RUNNING; not a generator failure.
- Recovery attempt 1: run `34238873539`, job `102103587968`, completed SUCCESS as a workflow but ended `RECOVERY_FINAL_STATUS=UNKNOWN`.
- Its log shows the same Kaggle kernel was still `KernelWorkerStatus.RUNNING` on every poll through 15:16 UTC / 17:16 +02:00.
- Because the kernel was still active, `kaggle kernels output` exposed no files; upload-artifact correctly reported no files and no artifact was created.
- No semantic conclusion can be drawn from attempt 1.
- Non-destructive recovery attempt 2 triggered by commit `bcd28ecc548bd039f196f09d22b6cf169f0cc4ba` via `ops/kaggle-recovery-trigger.txt`.
- Attempt 2 remains `recover-existing-only`; it MUST NOT push or replace the existing kernel.
- Do not launch a new building generation wave until wave85 reaches terminal state and outputs/log are recovered.

## Wave84 baseline
Recovery artifact `10053866830`: v16.2 exported BLD-11/12/13 T0–T6 (21 technical candidates), semantic acceptance 0/21. Main remaining defects: slabs/ground patches, detached residue/props and baked FX.

## CircleCI
`.circleci/config.yml` contains a long recovery lane, but no CircleCI status has been observed on GitHub. Do not assume it is executing.

## Other prepared lanes
- Character: `tools/sprites/kaggle_character_sheet_factory_v1.py`, canonical 1024×1024 RGBA 4×4 atlas.
- FX: `tools/sprites/kaggle_fx_sheet_factory_v1.py`, runtime 8-frame 4×2 512×256 atlas.

## Next actions
1. Find/query the recovery workflow created from commit `bcd28ecc548bd039f196f09d22b6cf169f0cc4ba`.
2. When terminal, fetch its logs and artifact immediately.
3. If outputs exist, inspect reports/contact sheets/all candidate PNGs and verify v16.3 startup.
4. Full semantic review: slabs, shadows, detached residue/props, baked FX, cranes, people, vehicles, text, alpha defects, identity drift and progression.
5. Compare complete-family semantic acceptance to wave84's 0/3.
6. Promote only complete valid families; strict increment only after runtime + manifest/progress + green Android CI.
7. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
