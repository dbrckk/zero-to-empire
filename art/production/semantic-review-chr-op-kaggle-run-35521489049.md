# CHR-OP semantic review — Kaggle run 35521489049

Date: 2026-09-20
Verdict: **REJECT IDLE/WALK for runtime promotion**

## Passed
- both atlases pass strict technical QA;
- WALK is now a single subject in every frame;
- stylization is materially closer to the canonical 2.5D game-art direction;
- frame pivots and silhouette continuity are technically stable.

## Remaining blocker
IDLE and WALK do not read as the exact same operator. Head/hair/headgear changes across animations, including a hard hat in WALK that is absent in IDLE. The v1.2 factory locks identity only within each individual animation, not across animations of the same role.

## v1.3 correction
- one shared role identity anchor is created from the first OP animation;
- later OP animations begin from that same anchor via conservative img2img;
- OP headgear is explicitly fixed to one rust-orange safety hard hat in every animation;
- per-frame variations stay anchored to the animation's identity-preserving first frame.

No runtime promotion and no strict DONE increment from run 35521489049.
