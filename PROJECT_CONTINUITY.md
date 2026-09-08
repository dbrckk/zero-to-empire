# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-08 18:56 +02:00
- **112 / 235 strict DONE**.
- Runs 80–85: strict delta +0.

## Building generator v16.4 — COMMITTED BUT NOT YET EXECUTED
`tools/sprites/kaggle_building_family_factory_v16.py`, commit `fa41f56442a2e62227045b272676780c5a8f5ca8`.
Startup target: `building-family-flux-v16.4-footprint-locked-two-phase`.
Changes vs v16.3:
- tier img2img strengths cut to T1 .16, T2 .19, T3 .22, T4 .24, T5 .26, T6 .28;
- T0–T3 massing phase, T4–T6 detail phase while preserving footprint;
- positive spatial footprint contract with wall-base plinth flush under walls and neutral gray immediately outside;
- stronger low/broad anchor preference including base-fill metric;
- tier-dependent adjacent footprint IoU floor;
- slab QA remains strict.

## Wave 86 — BLOCKED BEFORE GPU EXECUTION
- Trigger commit `05116418e34f6025e6bc4b0851978a9f7e9c25fb`.
- GitHub Actions run `34254137128`, job `102155550794`, completed failure.
- Kaggle push failed immediately with: `Maximum weekly GPU quota of 30.00 hours reached.`
- Therefore v16.4 did **not** run and has no generation-quality evidence yet.
- The workflow then observed the previous Kaggle kernel still in terminal ERROR state and downloaded the prior 20,452-byte evidence set only (`branch-search-report.json` + old kernel log), artifact `10067157434`.
- Do not misclassify wave86 as a v16.4 generator failure; it is an infrastructure/quota block before execution.
- Do not repeatedly retrigger Kaggle while the weekly GPU quota remains exhausted.

## Productive no-GPU lane while quota is blocked
- Run75 integration commit `e14b6897e32a557736a4e9c06d55b925864993d1` contains reviewed BLD-03 T2–T6 masters and runtime WebP outputs; technical QA reports all five automatic-pass with clean edges.
- These five assets are not yet counted strict DONE because current progress ledger remains 112/235 and their runtime visibility + canonical manifest/progress reconciliation + green Android CI still need explicit proof.
- Reconcile already-integrated assets before spending more GPU time.

## Wave 85 — TERMINAL GENERATION FAILURE / 0 YIELD
- Source run `34224023209`; recovery artifact `10066542877`.
- v16.3 startup confirmed; 56 attempted, 56 rejected, 0 candidates.
- Dominant failure remained ground/slab contamination.

## Wave84 baseline
Artifact `10053866830`: v16.2 exported BLD-11/12/13 T0–T6 (21 technical candidates), semantic acceptance 0/21 = 0/3 complete families.

## CircleCI
CircleCI cannot bypass Kaggle's account-level GPU quota. `.circleci/config.yml` remains useful only for longer collection/recovery once Kaggle can actually start a kernel.

## Other prepared lanes
- Character: `tools/sprites/kaggle_character_sheet_factory_v1.py`, canonical 1024×1024 RGBA 4×4 atlas.
- FX: `tools/sprites/kaggle_fx_sheet_factory_v1.py`, runtime 8-frame 4×2 512×256 atlas.

## Next actions
1. Do not rerun Kaggle until quota availability changes.
2. Reconcile run75 BLD-03 T2–T6: prove active runtime references/visibility, update manifest/progress only if semantically valid, and require green Android CI before strict increment.
3. Reconcile other already ART/RUNTIME-integrated assets that remain outside strict DONE where evidence exists.
4. When GPU quota returns, run v16.4 unchanged first so its source-level footprint experiment gets a clean test.
5. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
