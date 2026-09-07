# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read this file before any new work on this repository and update it at every assistant intervention that changes goals, state, decisions, blockers, or next actions.

## Global continuity rule
- This repository must always keep a recent, concrete record of the latest changes and the next objectives.
- The assistant must update this file whenever it works on the repository and before ending an intervention that materially changes project state.
- Do not rely on chat history as the only source of continuity.
- Apply the same `PROJECT_CONTINUITY.md` convention to every actively worked repository going forward.
- Never mark an objective complete from intent alone: record the commit/run/CI evidence that proves completion.

## Primary objective
Bring **Zero → Empire** to full production completion, with the current immediate art objective being **100% of the canonical final sprite manifest**.

Canonical art sources:
- `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`
- `docs/art/FINAL_AAA_SPRITE_PROGRESS.md`

Locked scope: **235 final deliverables**.

## Non-negotiable sprite completion gate
An asset is not strict `DONE` until it is individually authored/generated, semantically correct, technically clean, transparent where required, committed to the final runtime path, actually referenced/visible in runtime, and validated by green Android CI. Candidate sheets, concept collages, technically valid but semantically wrong generations, or merely integrated files do not increment strict DONE.

## Current handoff — 2026-09-07
### Current trusted state
- Strict committed progress ledger remains **112 / 235 DONE** until a later strict reconciliation proves a higher number.
- `BLD-03-T2` through `BLD-03-T6` were integrated by run 75 (`e14b6897...`) but still require canonical reconciliation/green-CI proof before silently increasing strict DONE.
- Run 77 (`34102566634`) produced 21 technically valid building candidates; full-resolution semantic review rejected **21 / 21**. Review: `docs/art/reviews/RUN_77_SEMANTIC_REVIEW.md`.
- Run 78 (`34116344191`) returned Kaggle `ERROR`, but root-cause review shows the generator intentionally ended with zero fresh validated candidates rather than an infrastructure/authentication crash. Review: `docs/art/reviews/RUN_78_PIPELINE_REVIEW.md` (`cdfdcc56...`).

### Run 78 evidence
- Backlog at launch: `BLD=70`, `STATIC=0`, `CHAR_FX=24`, `SKIPPED_RUNTIME=14`.
- Five families died immediately at T0 because one seed produced background/slab contamination: BLD-05, BLD-08, BLD-09, BLD-10, BLD-12.
- BLD-13 rendered all tiers T0→T6 successfully with coverage growth **15.2% → 32.7%**.
- Previous family QA rejected BLD-13 only because raw alpha centroid drift measured **7.9** against a fixed limit of **7**; this metric was judged too brittle after canonical bottom-center normalization.
- Strict DONE delta from run 78: **+0**.

### Generator evolution after run 78
- Canonical `tools/sprites/kaggle_building_family_factory.py` upgraded directly to **v12 retry-normalized** (`4b42a628...`).
- v12 is now the source of truth; no hidden temporary v11 mutation is required.
- T0 gets up to **4 seed retries**; later tiers get adaptive retries and adaptive img2img strength.
- QA now uses adjacent identity IoU, normalized bbox geometry, coverage progression, final-vs-initial growth, ground-slab detection, internal-hole detection and horizontal drift.
- T0 uses a smaller canonical frame envelope to preserve starter-tier read.
- Prompts explicitly prohibit floor cards, terrain slabs, horizons, workers, vehicles, pseudo-text, disconnected props and accidental alpha holes.
- `kaggle/github_mass_factory.py` upgraded to deterministic **v6 retry-normalized** routing (`f01de81c...`).
- Building waves are capped at **28 manifest tiers** so retries can spend compute on recovery instead of breadth.
- `.github/workflows/kaggle-mass-sprite-factory.yml` now defaults to 28 and injects batch count with a validated regex instead of brittle source-string substitution (`0dba6f1d...`).
- Pillow is pinned `<12` in the runner/kernel dependency path to eliminate the observed compatibility conflict with the Kaggle environment.

### User-approved wave trigger mechanism
- Mass generation remains user-controlled: manual `workflow_dispatch` or a push to `ops/sprite-wave-trigger.txt` after an explicit `Go` / `Continue`.
- The current user instruction explicitly authorizes continuing and improving sprite production, so the next wave may be launched now.

## Immediate next actions — ordered
1. Trigger **wave 79** using the v12/v6 retry-normalized pipeline.
2. Inspect the run status and retrieve the QA artifact when produced.
3. Review every emitted candidate at full resolution. Technical validation is not semantic approval.
4. Promote only complete coherent families that preserve identity and unmistakably progress from tiny T0 starter to T6 ultimate structure.
5. Reconcile `FINAL_AAA_SPRITE_MANIFEST.md` and `FINAL_AAA_SPRITE_PROGRESS.md` only after runtime integration and green Android CI.
6. Continue successive user-approved waves until the building backlog is exhausted, then route static assets, character sheets and FX through equally strict dedicated factories.
7. Repeat generate → technical QA → semantic QA → promotion → runtime integration → green CI until **235 / 235 strict DONE**.

## Known unresolved art targets
- Remaining building families/tiers after `BLD-03`, with coherent family identity and unmistakable monotonic T0→T6 growth.
- `TER-07` Expansion energy conduit remains unresolved unless superseded by a later accepted promotion.
- Character/FX backlog still requires its dedicated sheet-production lane once building/static routing no longer dominates.
- Any TODO/ART/RUNTIME item in the canonical manifest must pass the same strict completion gate.

## Operating principle
Quality beats nominal throughput. A failed/rejected generation wave is valid QA evidence but is **not progress toward DONE**. Optimize the generator from failure evidence, then retry. Never replace a strict counter with an optimistic candidate count.
