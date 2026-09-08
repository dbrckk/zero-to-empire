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

## Current trusted state — 2026-09-08 13:13 +02:00
- Strict ledger remains **112 / 235 DONE**.
- Run 80 semantic delta +0; run 81 +0; run 82 +0; run 83 +0.

## Wave 84 — GitHub collector timed out; CircleCI recovery path activated
- Trigger commit `c51bb50d9e05e0498068b900844845a53585523e`.
- GitHub Actions run `34200990117`, job `101979474170`, run number 84.
- Main GitHub collector exhausted its 135-minute polling window while Kaggle still reported `KernelWorkerStatus.RUNNING` through the final poll.
- No normal `kaggle-sprite-batch` artifact existed at GitHub collector shutdown; this is not a semantic failure of v16.2.
- GitHub recovery trigger was already prepared for the existing kernel, but the user explicitly requested using CircleCI for long-running follow-up once GitHub Actions reaches its limit.

## CircleCI long-running Kaggle recovery — ACTIVE CONFIGURATION
- Added `.circleci/config.yml` in commit `4433f9ec427e95e1018e2084aac7f57533659c66`.
- Added/activated `ops/circleci-recovery-trigger.txt` in commit `792fae00548a5d69846e81f4c949d24f4babf48c` for wave84/source run `34200990117`.
- Workflow/job: `circleci-kaggle-recovery` / `recover-kaggle-sprite-run`.
- The CircleCI job is **recovery-only**: it never runs `kaggle kernels push`, so it cannot overwrite or compete with the existing Kaggle generation.
- It monitors the existing `zero-to-empire-sprite-factory` kernel for up to 270 minutes (4.5h), emitting status every minute.
- It downloads existing Kaggle outputs/logs whether the kernel reaches COMPLETE, ERROR, or the CircleCI watch expires.
- It stores `/tmp/kaggle-recovery` as CircleCI artifacts under `kaggle-recovered-sprite-batch`.
- It requires CircleCI project/context environment variables `KAGGLE_USERNAME` and `KAGGLE_KEY`. These are separate from GitHub Actions secrets; if they are not already configured in CircleCI, the preflight will fail explicitly rather than silently.
- Immediate GitHub combined-status lookup right after trigger commit returned no status entries yet; do not claim CircleCI job success/running until a CircleCI check/status is actually observed.
- CircleCI config syntax follows current CircleCI 2.1 conventions; `run.no_output_timeout` is set to 5h, while the monitor itself emits output every minute.

## Wave 83 — resolved code failure
- Recovery proved v16.1 anchor-score recursion (`maximum recursion depth exceeded`).
- 48 T0 anchor attempts, 0 branches, 0 successful families, 0 candidates.
- No semantic conclusion from run83; strict delta +0.

## Building generator v16.2
`tools/sprites/kaggle_building_family_factory_v16.py`, recursion-safe scorer preserved through `V15_ANCHOR_SCORE`.
- Shape-first T0, six anchors, silhouette filtering and conservative source-locked T1→T6.
- Positive wording tightened for family 10, family 13 and T6 roof form.
- Wave84 remains the first intended valid semantic experiment once its actual Kaggle outputs/logs are recovered.

## Character lane
`tools/sprites/kaggle_character_sheet_factory_v1.py`, commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`.
- Fixed canonical 1024×1024 RGBA atlas, 4×4 256px cells.

## FX lane — proven runtime contract and v1.2 factory
Concrete runtime evidence:
- `app/src/main/java/com/zerotoempire/game/ElectricArc.kt`
- `app/src/main/java/com/zerotoempire/game/DroneThruster.kt`
Both use Compose `Canvas.drawImage` with 8 frames, 4×2 grid, 128×128 source frames => 512×256 atlas.

FX factory commit `f22f4769aaef97a6ef19933c1a699461de6c00b9`:
- engine `procedural-fx-v1.2-runtime-atlas`;
- renders internally at 256×256, downsamples to 128×128;
- packs exactly 4×2 => 512×256 RGBA;
- preserves one-shot/loop temporal QA and FX-07 ballistic polygonal debris.
- Runtime visibility and green CI remain mandatory before strict DONE.

## Run 82 baseline
Run `34145936891`, artifact `10030821750`: 28 technical exports, 28 semantic rejects due cranes/site contamination.

## Workflow reliability
- GitHub Actions main collector polls 135 minutes, then stops to avoid losing evidence to the hard runner ceiling.
- `.github/workflows/kaggle-recover-existing-run.yml` remains available as a short recovery fallback.
- For long Kaggle jobs after GitHub collector exhaustion, prefer the CircleCI recovery lane now that `.circleci/config.yml` exists.
- CircleCI artifact storage is used for recovered evidence; do not mark sprites DONE merely because artifacts were collected.

## Immediate next actions
1. Check whether CircleCI has posted a status/check for trigger commit `792fae00548a5d69846e81f4c949d24f4babf48c`.
2. If CircleCI preflight fails for missing `KAGGLE_USERNAME`/`KAGGLE_KEY`, preserve that exact blocker; those variables must exist in the connected CircleCI project/context because GitHub secrets are not automatically shared with CircleCI.
3. When CircleCI recovery completes, inspect recovered `branch-search-report.json`, generated-targets, QA/contact sheets, candidates and kernel log.
4. Verify startup `building-family-flux-v16.2-shape-first-recursion-safe`, ensure silhouette scoring runs without recursion, and measure complete-family semantic acceptance versus run82's 0/4.
5. Reject cranes/gantries/booms, broad site cards, people, vehicles, text, detached props, civic/monument drift, identity drift or fake tier progression.
6. Promote only complete genuinely valid families; then runtime refs + manifest/progress reconciliation + green Android CI before strict increment.
7. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Prefer evidence from existing runtime code over assumed formats. Use CircleCI for long-running Kaggle recovery after GitHub Actions reaches its collection ceiling, without ever launching a competing kernel.