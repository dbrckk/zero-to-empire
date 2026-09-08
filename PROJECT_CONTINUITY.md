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

## Current trusted state — 2026-09-08 16:31 +02:00
- Strict ledger remains **112 / 235 DONE**.
- Runs 80, 81, 82, 83 and 84 all have strict delta +0.

## Wave 84 — recovered and semantically reviewed
- Original Actions run `34200990117` outlived the 135-minute GitHub collector while Kaggle was still RUNNING.
- Non-destructive recovery run `34219375395` completed SUCCESS.
- Recovered artifact `10053866830`, `kaggle-recovered-sprite-batch`, ~33.6 MB.
- Startup confirmed: `KAGGLE_STARTUP=building-family-flux-v16.2-shape-first-recursion-safe`.
- Technical counters: 48 anchors, 16 branches, 128 context attempts, 61 live rejections, 13 early aborts.
- 21 technically valid candidates exported: BLD-11, BLD-12, BLD-13 T0-T6.
- Full semantic review: `docs/art/reviews/RUN_84_SEMANTIC_REVIEW.md`.
- Semantic result: **0/21 promoted**.
- Run84 reduced crane/gantry contamination substantially; remaining defects were floor/site slabs, ground patches, detached residue, loose props and baked FX.

## Building generator v16.3 — isolated static source
File `tools/sprites/kaggle_building_family_factory_v16.py`.
- Commit `60656bdaa97e7a4821fb115472c31803eb6ba509`.
- Startup marker: `building-family-flux-v16.3-isolated-static-source`.
- Source strengths T1..T6 = .20/.25/.30/.35/.40/.45.
- Static-object contract explicitly excludes surrounding floor/site pads, cast-shadow cards, detached props and emitted FX.

## Wave 85 — KAGGLE STILL RUNNING; RECOVERY REQUESTED
- Trigger commit `fc21ec0e2faaec18ed1a0cc09e112aafa79a88c4`.
- Original GitHub Actions run `34224023209`, job `102053645197`, run number 85.
- GitHub collector completed `failure` at 16:20 +02:00 only because its 135-minute poll ended with `KAGGLE_FINAL_STATUS=UNKNOWN`.
- Log shows Kaggle remained `KernelWorkerStatus.RUNNING` continuously through the final poll at 16:19 +02:00.
- Download step ran but Kaggle exposed no outputs while the kernel was still active; therefore no artifact was uploaded.
- This is **not a generator failure and not semantic evidence**.
- Non-destructive recovery trigger updated for wave85 in commit `24e0bba86ac0a3d66c3c6a7f76bd19aed4a005a9` with `source_run=34224023209` and `mode=recover-existing-only`.
- Immediate Actions query on that trigger commit returned no run yet; re-check on next intervention.
- Do not push or launch another Kaggle kernel until the existing wave85 kernel reaches a terminal state and its outputs/log are recovered.

## CircleCI long-run recovery lane
- `.circleci/config.yml` monitors an existing Kaggle kernel up to 4.5 hours without pushing a new kernel.
- GitHub still has not shown a CircleCI status, so CircleCI execution remains unconfirmed.
- Prefer CircleCI if it begins reporting; otherwise use the GitHub non-destructive recovery workflow.

## Character lane
`tools/sprites/kaggle_character_sheet_factory_v1.py`, commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`.
- Canonical 1024×1024 RGBA atlas, 4×4 256px cells.

## FX lane
`tools/sprites/kaggle_fx_sheet_factory_v1.py`, commit `f22f4769aaef97a6ef19933c1a699461de6c00b9`.
- Runtime contract: 8 frames, 4×2 grid, 128×128 runtime cell, 512×256 atlas.

## Immediate next actions
1. Check for a recovery workflow run from commit `24e0bba86ac0a3d66c3c6a7f76bd19aed4a005a9`.
2. If recovery is active, do not launch a redundant wave.
3. When wave85 reaches terminal state, retrieve log, reports, contact sheets and every candidate.
4. Perform full semantic review with special attention to floor pads, cast shadows, detached props, baked FX, cranes, people, vehicles, text and identity drift.
5. Compare complete-family acceptance against run84's 0/3.
6. Promote only genuinely valid complete families; then runtime refs, canonical manifest/progress reconciliation and green Android CI before strict increment.
7. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. QA should confirm quality rather than reject whole batches. Optimize semantic acceptance rate × validated sprites/GPU-hour, preserve long-run evidence, and never inflate strict DONE.
