# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read this file before any new work on this repository and update it at every assistant intervention that changes goals, state, decisions, blockers, or next actions.

## Global continuity rule
- Keep a recent concrete record of changes, evidence, blockers and next objectives.
- Update this file at every material assistant intervention.
- Do not rely on chat history alone.
- Apply the same `PROJECT_CONTINUITY.md` convention to every actively worked repository.
- Never mark completion from intent or candidate generation alone.

## Primary objective
Bring **Zero → Empire** to full production completion. Immediate art objective: **235 / 235 canonical final sprites strict DONE**.

## Strict completion gate
A sprite is strict DONE only after individual production, semantic correctness, technical/alpha validation, final runtime commit/reference, actual runtime visibility, manifest/progress reconciliation and green Android CI. Candidate count is never DONE count.

## Current trusted state — 2026-09-08
- Strict ledger remains **112 / 235 DONE**.
- Runs 80–84 have strict delta +0.

## Wave 84 — recovered and semantically reviewed
- Original Actions run `34200990117` outlived the GitHub collector.
- Recovery run `34219375395` succeeded; artifact `10053866830`.
- v16.2 exported 21 technical candidates: BLD-11/12/13 T0–T6; semantic result **0/21 promoted**.
- It substantially reduced crane/gantry contamination; remaining defects were floor/site slabs, ground patches, detached residue, loose props and baked FX.

## Building generator v16.3
File `tools/sprites/kaggle_building_family_factory_v16.py`, commit `60656bdaa97e7a4821fb115472c31803eb6ba509`.
Startup `building-family-flux-v16.3-isolated-static-source`.
Static-object contract excludes surrounding floor/site pads, cast-shadow cards, detached props and emitted FX.

## Wave 85 — RECOVERY ACTIVE
- Source trigger `fc21ec0e2faaec18ed1a0cc09e112aafa79a88c4`.
- Original Actions run `34224023209`, job `102053645197`, run 85.
- Original collector ended failure after 135 minutes with `KAGGLE_FINAL_STATUS=UNKNOWN`; its logs prove Kaggle was still RUNNING through the final poll at 16:19 +02:00. This is not generator/semantic failure.
- Recovery trigger commit `24e0bba86ac0a3d66c3c6a7f76bd19aed4a005a9`.
- Recovery workflow is now confirmed: run `34238873539`, job `102103587968`, workflow `Recover Existing Kaggle Sprite Run`, run number 3.
- Latest check: recovery is `in_progress`; setup/checkout/Kaggle CLI succeeded and step `Wait for existing kernel only` is active. Download/upload/report steps are pending.
- Recovery is non-destructive and does not push a replacement kernel.
- Do not launch another building wave while this recovery is active.

## CircleCI long-run recovery lane
`.circleci/config.yml` can monitor an existing Kaggle kernel without pushing a new one, but no CircleCI status has yet been observed on GitHub. GitHub recovery is currently active and authoritative for wave85.

## Character lane
`tools/sprites/kaggle_character_sheet_factory_v1.py`, commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`; canonical 1024×1024 RGBA atlas, 4×4 256px cells.

## FX lane
`tools/sprites/kaggle_fx_sheet_factory_v1.py`, commit `f22f4769aaef97a6ef19933c1a699461de6c00b9`; runtime contract 8 frames, 4×2 grid, 128×128 runtime cell, 512×256 atlas.

## Immediate next actions
1. Query recovery run `34238873539` first.
2. If still active, do not launch redundant generation.
3. When terminal, fetch artifacts/logs and inspect all v16.3 candidates/reports.
4. Perform full semantic review, especially floor pads, cast shadows, detached props, baked FX, cranes, people, vehicles, text and identity drift.
5. Compare complete-family semantic acceptance against run84's 0/3.
6. Promote only genuinely valid complete families, then runtime refs + manifest/progress reconciliation + green Android CI before strict increment.
7. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. QA should confirm quality rather than reject whole batches. Optimize semantic acceptance rate × validated sprites/GPU-hour, preserve long-run evidence, and never inflate strict DONE.
