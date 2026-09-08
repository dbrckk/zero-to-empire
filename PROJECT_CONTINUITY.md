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

## Current trusted state — 2026-09-08 09:41 +02:00
- Strict ledger remains **112 / 235 DONE**.
- Run 80 semantic delta +0; run 81 +0; run 82 +0.

## Wave 83 — GitHub collector timed out; Kaggle result recovery active
- Trigger commit `153ab7be267a8a1c8169b0374bac86a411795af0`.
- Original GitHub Actions run `34189278981`, job `101943816015` is completed FAILURE.
- Failure is specifically the GitHub-side 135-minute recovery guard: `KAGGLE_FINAL_STATUS=UNKNOWN`; `Require successful Kaggle kernel` failed.
- Kaggle was continuously `RUNNING` from 05:06Z through the final poll at 07:20Z. There is no evidence in the GitHub log that the Kaggle kernel itself failed.
- At timeout, `kaggle kernels output` returned no files because the kernel was still running; therefore the original run has no artifact.
- Do NOT interpret this as a v16.1 semantic failure and do NOT launch a replacement generation until the existing kernel state is recovered.

### Non-destructive recovery
- Added `.github/workflows/kaggle-recover-existing-run.yml` in commit `910a388ffc636c5c7090b6c01c6bfc9de609c944`.
- Recovery workflow never pushes/replaces a Kaggle kernel. It only polls the already-running `zero-to-empire-sprite-factory`, downloads outputs when available, and uploads them as `kaggle-recovered-sprite-batch`.
- Trigger commit `70dd70145a5ab7e945c25215db628c099aab09bd` writes `ops/kaggle-recovery-trigger.txt` for wave83 recovery.
- First immediate Actions query after trigger returned no run yet; re-query on next intervention before doing anything else.

## Run 82 baseline
Run `34145936891`, artifact `10030821750`, workflow SUCCESS.
- v15.2 requested 56 tiers; 28 technically validated exports across BLD-05/08/10/11.
- Semantic review rejected all 28 because cranes/gantries/booms and site/platform bases survived.
- Review: `docs/art/reviews/RUN_82_SEMANTIC_REVIEW.md`.

## Building generator v16.1
`tools/sprites/kaggle_building_family_factory_v16.py`; startup `building-family-flux-v16.1-shape-first-source-locked`.
- Shape-first T0, positive family design cards, conservative source-locked T1→T6, six T0 anchors, silhouette filtering.
- Wave83 is the first empirical v16.1 run; no semantic conclusion until recovered outputs/logs exist.

## Character lane
`tools/sprites/kaggle_character_sheet_factory_v1.py`, commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`.
- Fixed canonical 1024×1024 RGBA atlas, 4×4 256px cells.

## FX lane
`tools/sprites/kaggle_fx_sheet_factory_v1.py`, commit `8a837c11a37be85bad0f5380557e99089895f67f`.
- v1.1 temporal QA; one-shot attack/peak/decay checks; FX-07 includes polygonal ballistic debris.
- 2048×256 horizontal strips remain candidate-only until runtime integration is proven.

## Immediate next actions
1. Query Actions for trigger commit `70dd70145a5ab7e945c25215db628c099aab09bd` and inspect the recovery run.
2. If recovery finds wave83 COMPLETE, download `kaggle-recovered-sprite-batch`, inspect logs/reports/candidates and perform full semantic review.
3. If existing Kaggle kernel is still RUNNING, do not replace it; let recovery collector continue.
4. If Kaggle reports ERROR, diagnose recovered logs/evidence before another generation.
5. Only after wave83 is resolved decide whether to promote valid families or tune v16.1 and launch the next wave.
6. Strict count changes only after runtime integration, reconciliation and green Android CI.

## Operating principle
Generate the right asset first. Preserve evidence from long-running jobs instead of blindly restarting them. Optimize semantic acceptance rate × validated sprites/GPU-hour, never raw image count.