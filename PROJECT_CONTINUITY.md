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

## Current trusted state — 2026-09-08 14:38 +02:00
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
- SHAPE cards explicitly require the foundation to end exactly under the wall/building footprint.
- Family cards prefer attached/sealed service equipment instead of emitted or freestanding elements.
- Static-object contract injected into T0 and T1-T6 prompts:
  - visible object ends at structural foundation edge;
  - neutral studio background starts immediately around the building;
  - all pipes/tanks/vents/service modules physically attached;
  - no surrounding pavement/floor/site pad/road/terrain/cast-shadow card;
  - no barrels/crates/tools/vehicles/workers/detached props;
  - no emitted smoke/steam/flame/sparks/particles;
  - no text/labels/flags/signs/scenery.
- Goal is generation-first cleanup, not post-hoc rejection.

## Wave 85 — ACTIVE
- User authorized with `Go`.
- Trigger commit `fc21ec0e2faaec18ed1a0cc09e112aafa79a88c4`.
- GitHub Actions run `34224023209`, job `102053645197`, run number 85.
- Latest check at 14:38 +02:00: `in_progress` at `Wait for Kaggle`.
- Setup, checkout, credentials, dependencies, Kaggle auth, kernel preparation and push/start are all green.
- Requested 56 tiers using `building-family-flux-v16.3-isolated-static-source`.
- Objective: eliminate floor pads, cast-shadow cards, detached props and baked smoke/flame/steam at the source while preserving run84 crane reduction.
- Do not launch a redundant building wave while run85 is active.

## CircleCI long-run recovery lane
- User requested CircleCI for long Kaggle monitoring because GitHub collector windows are too short.
- `.circleci/config.yml` monitors an existing Kaggle kernel up to 4.5 hours without `kaggle kernels push`.
- CircleCI recovery trigger updated for wave85 in commit `7f45179142e94fd241edd49712d896a5fb65c742` with `source_run=34224023209`.
- Latest GitHub commit-status check still reports `total_count=0`; no CircleCI status is being propagated yet.
- Therefore the repo-side CircleCI lane is armed but still not empirically firing/reporting.
- If CircleCI starts, prefer it for long monitoring/recovery of run85. If not, do not relaunch Kaggle merely because the GitHub collector expires; preserve evidence with the non-destructive recovery workflow.

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
1. Query run85 first on the next intervention.
2. If CircleCI status appears, prefer it for long monitoring/recovery of run85.
3. If run85 completes, retrieve all candidates/reports/logs and perform full semantic review, with special attention to floor pads/cast shadows/loose props/baked FX.
4. Compare complete-family semantic acceptance against run84's 0/3 complete exported families.
5. Promote only complete genuinely valid families, then runtime refs + manifest/progress reconciliation + green Android CI before strict increment.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. QA should confirm quality rather than reject whole batches. Optimize semantic acceptance rate × validated sprites/GPU-hour, preserve long-run evidence, and never inflate strict DONE.
