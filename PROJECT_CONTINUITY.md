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

Canonical sources:
- `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`
- `docs/art/FINAL_AAA_SPRITE_PROGRESS.md`

## Strict completion gate
A sprite is strict DONE only after individual production, semantic correctness, technical/alpha validation, final runtime commit/reference, actual runtime visibility, manifest/progress reconciliation and green Android CI. Candidate count is never DONE count.

## Current trusted state — 2026-09-07 19:02 +02:00
- Strict ledger remains **112 / 235 DONE** pending evidence-based reconciliation.
- BLD-03-T2..T6 from run 75 remain integrated but not added to strict count without canonical/CI proof.
- Run 80: 21 technical candidates, semantic rejection 21/21; strict delta +0.
- Run 81: Kaggle successfully generated and technically validated **56 / 56** candidates across 8 complete building families, but strict full-resolution semantic review rejected **56 / 56**; strict delta +0.

## Run 81 — exact evidence
GitHub Actions run `34132705535`, artifact `10026804547`.
- 56 exported candidates: BLD-04, BLD-05, BLD-08, BLD-09, BLD-10, BLD-11, BLD-12, BLD-13, each T0→T6.
- 32 T0 anchor attempts, 16 completed branch attempts, 8 selected complete families.
- Kaggle reported `KAGGLE_BUILDING_SUCCESS=56`, `KAGGLE_FRESH_CANDIDATES=56`, `QA_TOTAL=56 QA_AUTO_PASS=56`, `KAGGLE_EXPORT_COUNT=56`.
- Semantic review: `docs/art/reviews/RUN_81_SEMANTIC_REVIEW.md` (`f239df13...`).
- Dominant rejection pattern: construction cranes / orange boom arms across nearly all families, plus broad platform/site-card bases and loose site props.
- Positive evidence: family continuity and T0→T6 growth are now strong; the pipeline is no longer a raw-yield problem.

## Run 81 CI gate bug — fixed
The GitHub job showed failure even though all 56 candidates existed because the workflow parsed QA reports using obsolete keys `sprites/results`, while the current report schema stores rows under `assets`.
- Fixed in `.github/workflows/kaggle-mass-sprite-factory.yml` commit `6321ddc31fea331f46ed83310926dfe2e45f2e24`.
- Future QA coverage gate accepts `assets`, with backward-compatible fallback to `sprites/results`.
- This was a workflow parser bug, not a Kaggle generation failure.

## Building generator — v15.2 live semantic validation
Commit `9e1146622d47101ee9fe816955f02181a2cf35ff`.
Startup marker: `KAGGLE_STARTUP=building-family-flux-v15.2-live-semantic-validation`.

Changes derived directly from run 81:
1. Prompts now demand a **finished operating industrial factory**, not a construction-site interpretation.
2. Strong explicit negatives: crane, tower crane, jib, boom arm, hoist, gantry crane, scaffolding, temporary frame, workers, vehicles, roads, slabs/platforms/site cards and loose props.
3. New `boom_score()` inspects the upper alpha silhouette for crane-like long thin horizontal structures.
4. T0 anchors with boom contamination or slab score > .12 are rejected before branch evolution.
5. T1→T6 live gate rejects boom contamination and slabs > .16 during generation.
6. Failed tiers are regenerated with fresh seeds up to 3 contextual attempts; repeatedly bad branches are aborted early.
7. Final branch score penalizes both max slab and max crane-boom contamination.
8. Full semantic review remains mandatory because geometric heuristics cannot replace visual judgment.

## Wave 82 — launched
- Trigger commit: `44ecebae70c3a52ca5a33d3d8f72c30783efafb4`.
- GitHub Actions run: **`34145936891`**.
- Requested count: 56 manifest tiers.
- Generator: `building-family-flux-v15.2-live-semantic-validation`.
- Objective: preserve v15 multi-branch yield while rejecting crane-boom and slab contamination **during** generation.
- Latest verified state: `queued` immediately after trigger.
- Do not launch a conflicting additional wave while this one is queued/running.

## Character lane
- Factory: `tools/sprites/kaggle_character_sheet_factory_v1.py` (`5bec3b27922106c6d2120cf28b56a008aeb4b026`).
- Routed automatically after building/static backlog.
- Identity anchor + img2img pose evolution, transparent isolation, fixed feet pivot, silhouette/cycle QA.
- `character-sheet-report.json` retained in workflow artifacts.

## FX lane
- Factory: `tools/sprites/kaggle_fx_sheet_factory_v1.py` (`80f59093fbe5ece291ee4f057e1b780c7b2539e5`).
- Routed by `f1b3cdf8839d9dcb13cd6386f09252e29cbcc883`.
- Procedural 8-frame transparent sheets with live per-frame QA and sheet-level duplicate/drift QA.
- `fx-sheet-report.json` retained by workflow.

## Immediate next actions
1. Query run `34145936891` first on the next intervention.
2. Verify v15.2 startup marker and inspect live metrics: `KAGGLE_ANCHOR_LIVE_REJECT`, `KAGGLE_LIVE_REJECT`, `KAGGLE_BRANCH_EARLY_ABORT`, boom/slab reasons.
3. When complete, retrieve all artifacts and review every surviving family at full resolution.
4. Compare wave-82 semantic yield against run 81; specifically measure whether cranes/site cards disappear rather than merely whether technical candidate count changes.
5. Promote only genuinely valid families; integrate runtime/references, reconcile manifest/progress and require green Android CI before strict increment.
6. Then continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Known unresolved targets
- Remaining building families after BLD-03.
- `TER-07` Expansion energy conduit unless superseded by accepted promotion.
- Character/FX factories exist but still need real production validation before strict DONE credit.

## Operating principle
Maximize **validated sprites per GPU-hour**. Preserve high candidate throughput, but move semantic rejection as early as possible so GPU time is spent on branches that can plausibly pass full-resolution review.