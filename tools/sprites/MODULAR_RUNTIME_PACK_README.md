# TECH runtime review atlas packaging

All six TECH clips are synthesized **without Kaggle, image regeneration per frame or manual Pose Studio operations**. The existing single-skin IK renderer builds the character and the new packaging stage generates compact game-scale atlases, metadata and a browser playback diagnostic.

## Reproducible one-command stages

```bash
python -m pip install pillow numpy
python tools/sprites/rigged_tech_actions_v3.py \
  --skin tools/sprites/skin-tech-v1.webp \
  --output build/tech-actions-v3 --frames 24 --fps 12 --all
python tools/sprites/package_tech_actions_runtime.py \
  --source build/tech-actions-v3 \
  --output build/tech-actions-runtime-review
python -m unittest discover -s tools/sprites -p test_package_tech_actions_runtime.py -v
```

The GitHub workflow `.github/workflows/modular-tech-actions.yml` runs these stages unattended and publishes the result as a **review-only** Actions artifact.

## Output

- `atlases/{walk,carry,idle,work,repair,celeb}-{128,256}.png`: 24-frame RGBA atlases in 6 columns × 4 rows.
- `runtime-manifest.json`: timing, row-major UV ordering, per-frame visual bounds, fixed pivots, identity hashes and strict review flags.
- `events/{action}.json`: original footstep, screen update, repair and celebration events.
- `review-player.html`: six animations side by side, independent of external UI libraries, with speed adjustment and responsive layout.
- `game-scale-overview.jpg`: a quick 6-action comparison.
- `REVIEW_REQUIRED.txt`: explicit release gate.

Pivots derive from (252,449) in the 512×512 source canvas. The variants contain pixel pivots scaled to their canvas size. **Visual alpha bounds are not collision or damage hitboxes**; gameplay hitboxes must be designed and approved separately.

## Strict release safeguard

The package refuses missing assets, conflicting skin hashes, missing review markers, unapproved QA, unexpectedly sized frames, missing frame indices, clipped silhouettes or a malformed source index. Four regression tests cover success and intentional attempts to bypass the review gate.

The pipeline NEVER edits `art/production/master-asset-queue.json`, NEVER marks assets `strict DONE` and NEVER copies candidates over release resources. Original visual quality limits (stiff articulated seams, boot motion, hand-object overlap and small-screen readability) remain open for genuine independent visual/semantic review.
