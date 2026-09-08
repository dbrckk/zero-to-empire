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

## Current trusted state — 2026-09-08 13:41 +02:00
- Strict ledger remains **112 / 235 DONE**.
- Runs 80, 81, 82, 83 and 84 all have strict delta +0.

## Wave 84 — recovered and semantically reviewed
- Original Actions run `34200990117` outlived the 135-minute GitHub collector while Kaggle was still RUNNING.
- Non-destructive recovery run `34219375395` completed SUCCESS.
- Recovered artifact `10053866830`, `kaggle-recovered-sprite-batch`, ~33.6 MB.
- Startup confirmed: `KAGGLE_STARTUP=building-family-flux-v16.2-shape-first-recursion-safe`.
- Recursion bug is fixed: `KAGGLE_V16_SILHOUETTE` metrics executed normally.
- Technical counters: 48 anchors, 16 branches, 128 context attempts, 61 live rejections, 13 early aborts.
- 21 technically valid candidates exported: BLD-11, BLD-12, BLD-13 T0-T6.
- Full semantic review: `docs/art/reviews/RUN_84_SEMANTIC_REVIEW.md`, commit `6adf057821d1bd92b19dbd1bba503744538f4859`.
- Semantic result: **0/21 promoted**.
- Run84 is still a meaningful improvement over run82: dominant crane/gantry contamination is largely gone.
- Remaining dominant defects: broad floor/site slabs, cast-shadow/ground patches, detached residue, loose props, and baked smoke/flame/steam.

## Building generator v16.3 — isolated static source
File `tools/sprites/kaggle_building_family_factory_v16.py`.
- Updated in commit `60656bdaa97e7a4821fb115472c31803eb6ba509`.
- Startup marker: `building-family-flux-v16.3-isolated-static-source`.
- Source evolution strengths reduced again to preserve clean anchors: T1..T6 = .20/.25/.30/.35/.40/.45.
- Steps increased to 9/7/7/8/8/9/9 for cleaner source/detail convergence.
- SHAPE cards now explicitly require the foundation to end exactly under the wall/building footprint.
- Family cards prefer attached/sealed service equipment instead of emitted or freestanding elements.
- New static-object contract is injected into T0 and T1-T6 prompts:
  - visible object ends at structural foundation edge;
  - neutral studio background starts immediately around the building;
  - all pipes/tanks/vents/service modules physically attached;
  - no surrounding pavement/floor/site pad/road/terrain/cast-shadow card;
  - no barrels/crates/tools/vehicles/workers/detached props;
  - no emitted smoke/steam/flame/sparks/particles;
  - no text/labels/flags/signs/scenery.
- Goal is generation-first cleanup, not post-hoc rejection.

## CircleCI long-run recovery lane
- User requested CircleCI for long Kaggle monitoring because GitHub collector windows are too short.
- `.circleci/config.yml` exists and monitors an existing Kaggle kernel up to 4.5 hours without `kaggle kernels push`.
- Trigger marker exists in `ops/circleci-recovery-trigger.txt`.
- No CircleCI status has appeared on GitHub commits so far, indicating the CircleCI GitHub push trigger is not firing or status reporting is disabled.
- Repo-side CircleCI config is ready; one-time external CircleCI project trigger/environment configuration may still be required.
- Until CircleCI actually fires, GitHub's non-destructive recovery lane remains usable for preserving long-running Kaggle outputs, but do not launch redundant kernels merely because a collector expired.

## Character lane
`tools/sprites/kaggle_character_sheet_factory_v1.py`, commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`.
- Fixed canonical 1024×1024 RGBA atlas, 4×4 256px cells.

## FX lane — proven runtime contract and v1.2 factory
Concrete runtime evidence:
- `app/src/main/java/com/zerotoempire/game/ElectricArc.kt`
- `app/src/main/java/com/zerotoempire/game/DroneThruster.kt`
Both use Compose `Canvas.drawImage` with 8 frames, 4×2 grid, 128×128 source frames => 512×256 atlas.
FX factory commit `f22f4769aaef97a6ef19933c1a699461de6c00b9` outputs the matching 512×256 runtime atlas after 256px internal rendering and temporal QA.

## Run 82 baseline
Run `34145936891`, artifact `10030821750`: 28 technical exports, 28 semantic rejects, dominated by cranes/gantries/site construction motifs.

## Immediate next actions
1. Do not promote any run84 candidate.
2. Prefer CircleCI for long monitoring once its push trigger is actually observed; otherwise preserve evidence using the existing non-destructive recovery workflow.
3. Next building generation should use v16.3 and specifically measure whether floor pads/cast shadows/loose props/baked FX disappear while retaining run84's crane reduction.
4. Full-resolution semantic review remains mandatory for every exported family.
5. Promote only complete genuinely valid families, then runtime refs + manifest/progress reconciliation + green Android CI before strict increment.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. QA should confirm quality rather than reject whole batches. Optimize semantic acceptance rate × validated sprites/GPU-hour, preserve long-run evidence, and never inflate strict DONE.