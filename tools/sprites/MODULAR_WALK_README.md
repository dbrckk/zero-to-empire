# Zero to Empire — modular character-skin pipeline

This pipeline automatically renders an identity-locked `CHR-TECH-WALK` walk cycle with a single modular texture kit, inverse-kinematics limbs and a cyclic planted-foot trajectory. **No Kaggle, manual Pose Studio interaction or external image API is required.**

## Source

- `tools/sprites/skin-tech-v1.webp`: 4 × 3 transparent atlas (1024×768), 12 parts, extracted from a single concept-art character-part sheet. Rows contain head/torso/pelvis/backpack; upper arms/forearms; thighs/shins/boots. Each tile is 256×256.
- `tools/sprites/rigged_tech_walk_v2.py`: automatic IK walk generation with cloth/armor limbs, knee and elbow guards, sole-aligned boots, loop seam and alpha QA, PNG/GIF/atlas/footstep-event exports.
- `tools/sprites/test_rigged_tech_walk_v2.py`: tests for pose periodicity, stance foot locking, IK limb lengths, identity deterministic render, atlas, contact alignment and review gate.
- `.github/workflows/modular-tech-character.yml`: unattended CI renderer, retains output as a *review-only* artifact.

## Automatic usage

```bash
python -m pip install pillow numpy
python -m unittest discover -s tools/sprites -p 'test_rigged_tech_walk_v2.py' -v
python tools/sprites/rigged_tech_walk_v2.py \
  --skin tools/sprites/skin-tech-v1.webp \
  --output build/tech-walk-modular-v2 --frames 24 --fps 12
```

## QA and production gate

- Technical pass checks alpha boundaries, boots aligned with desired foot height within 1 pixel, no foot underground, and silhouette seam ratio.
- Geometry and texture identity are deterministic for given input files. A SHA-256 of the skin atlas is recorded in `qa-manifest.json`.
- **Technical pass does not mean visual or semantic pass.** The original concept-art skin still has 2D rigid-segment limitations, notably fabric bending, heel strike and knee/calf connections. Human semantic inspection of the resulting images and real-game motion is compulsory.
- Output remains `strict_status: NEEDS_REVIEW`. Nothing in this pipeline edits production queues or marks assets `DONE`.

## Roadmap

1. Validate skin realism and joints at 1× game display scale; fix visible seams and foot-lock temporal smoothness.
2. Reuse rig, footstep metadata and modular skin for carrying, working and repairing actions with action-specific constraints.
3. Review all 19 outstanding characters before updating any strict statuses.
