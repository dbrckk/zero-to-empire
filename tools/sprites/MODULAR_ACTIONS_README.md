# Autonomous TECH animation library — six review candidates

The same 12-piece character texture atlas and two-bone IK rig produce all six clips with no Kaggle, prompt-by-frame regeneration, or manual Pose Studio interaction.

| Asset | Motion | Special element |
| --- | --- | --- |
| CHR-TECH-WALK | Alternating grounded walk | Footstep events |
| CHR-TECH-CARRY | Carrying a box while walking | Two fixed cargo grips |
| CHR-TECH-IDLE | Breathing at rest | Cyclic status light |
| CHR-TECH-WORK | Working with a display | Moving hands and UI |
| CHR-TECH-REPAIR | Welding equipment | Tool and timed sparks |
| CHR-TECH-CELEB | Raised-arm celebration | Particle accents |

## One-command production

```bash
python -m pip install pillow numpy
python -m unittest discover -s tools/sprites -p 'test_rigged_tech_actions_v3.py' -v
python tools/sprites/rigged_tech_actions_v3.py --skin tools/sprites/skin-tech-v1.webp --output build/tech-actions-v3 --frames 24 --fps 12 --all
```

This produces 144 RGBA frames, six atlases, six looping GIFs, six normal and six 96px game-scale contact sheets, six event timelines, six QA manifests, six ZIP packages and a production-index.json. GitHub Actions workflow `.github/workflows/modular-tech-actions.yml` runs the same process automatically.

The shared `rigged_tech_walk_v2.py` supports optional pose_override, prop_underlay, and prop_overlay callbacks. Without them, the original WALK rendering remains unchanged.

## Safety / acceptance

Machine tests check cyclic continuity, foot-ground placement, footstep events, cargo grip, arm reach, alpha boundaries, movement distinctness and determinism. These are *technical checks*, not artistic approval.

Known limitations: stiff 2D fabric and metal pieces, mechanical knees and ankles, equipment and hand overlap at small scale, and near-static facial expression. The clips need actual playback at the target game camera size and an independent semantic/visual review.

All six candidates explicitly retain `strict_status: NEEDS_REVIEW`, `visual_review_pass: false` and `semantic_review_pass: false`. The scripts NEVER modify the canonical production queue, bypass the manual review gate or claim to have completed the 235-asset backlog.

## Next steps

1. Refine silhouette and shoe roll at 96px, and separate optional VFX layers.
2. Create a unified on-device visual review sheet for six loops.
3. Review each generated action in game context before integrating into runtime assets.
