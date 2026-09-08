# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read before work and update at every material intervention. Never rely on chat history alone.

## Primary objective
Reach **235 / 235 canonical final sprites strict DONE**. Strict DONE requires semantic + technical validation, final runtime reference/visibility, manifest/progress reconciliation and green Android CI.

## Trusted state — 2026-09-08 18:56 +02:00
- **112 / 235 strict DONE**.
- Runs 80–85: strict delta +0.

## Building generator v16.4 — COMMITTED
`tools/sprites/kaggle_building_family_factory_v16.py`, commit `fa41f56442a2e62227045b272676780c5a8f5ca8`.
Startup: `building-family-flux-v16.4-footprint-locked-two-phase`.
Wave85 proved prose-only anti-ground wording insufficient, so v16.4 changes generation dynamics rather than weakening QA:
- tier img2img strengths cut to T1 .16, T2 .19, T3 .22, T4 .24, T5 .26, T6 .28;
- two-phase evolution: T0–T3 massing, T4–T6 detail while preserving established footprint;
- positive spatial footprint contract: wall-base plinth flush beneath walls, neutral gray immediately outside, one centered self-contained object;
- stronger low/broad anchor preference including lower-mass/base-fill metrics;
- tier-dependent adjacent footprint IoU floor to prevent late tiers from replacing the source with a new scene;
- existing slab QA remains strict; no threshold weakening to manufacture yield.

## Wave 86 — TRIGGERED
- Trigger commit `05116418e34f6025e6bc4b0851978a9f7e9c25fb`.
- Count 56, generator v16.4.
- Experiment objective: beat wave84 complete-family semantic acceptance 0/3 and wave85 0/8 by source-level footprint locking and lower-denoise evolution.
- Do not launch another building wave while wave86 is active.

## Wave 85 — TERMINAL ERROR / 0 YIELD
- Source run `34224023209`; recovery artifact `10066542877`.
- Kaggle terminal `KernelWorkerStatus.ERROR`.
- Startup v16.3 confirmed; 56 attempted, 56 rejected, 0 candidates.
- 48 anchors, 16 branches, 124 context attempts, 67 live rejections, 16 early aborts; all eight attempted families failed.
- Dominant failure remained ground/slab contamination, including late-tier slab scores up to 0.46.

## Wave84 baseline
Artifact `10053866830`: v16.2 exported BLD-11/12/13 T0–T6 (21 technical candidates), semantic acceptance 0/21 = 0/3 complete families.

## CircleCI
`.circleci/config.yml` contains a long recovery lane, but no CircleCI status has been observed on GitHub. Do not assume it is executing.

## Other prepared lanes
- Character: `tools/sprites/kaggle_character_sheet_factory_v1.py`, canonical 1024×1024 RGBA 4×4 atlas.
- FX: `tools/sprites/kaggle_fx_sheet_factory_v1.py`, runtime 8-frame 4×2 512×256 atlas.

## Next actions
1. Locate the GitHub Actions run created by wave86 trigger `05116418e34f6025e6bc4b0851978a9f7e9c25fb` and confirm startup v16.4.
2. Let the active kernel finish; use non-destructive recovery if GitHub collector expires.
3. Inspect every exported candidate/contact sheet/report semantically: ground/slabs, shadows, detached residue/props, baked FX, cranes, people, vehicles, text, alpha, identity and progression.
4. Compare complete-family semantic acceptance against wave84 0/3 and wave85 0/8.
5. Promote only complete valid families; strict increment only after runtime + manifest/progress reconciliation + green Android CI.
6. Continue buildings → statics → characters → FX until **235 / 235**.

## Operating principle
Generate the right asset first; QA should confirm rather than routinely reject. Optimize validated semantic yield, preserve evidence, and never inflate strict DONE.
