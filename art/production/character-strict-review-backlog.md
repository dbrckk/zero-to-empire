# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **219/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38223743012 | Kaggle generator rejected candidate: required-role-idle-candidate-rejected; retry-details=The same-run IDLE identity sheet must pass generation and visual-risk QA before sibling actions are generated. |
| CHR-OP-WORK | OP | WORK | DISPATCHED | 38223743012 | Kaggle generator rejected candidate: required-role-idle-candidate-rejected; retry-details=The same-run IDLE identity sheet must pass generation and visual-risk QA before sibling actions are generated. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38223743012 | Kaggle generator rejected candidate: required-role-idle-candidate-rejected; retry-details=The same-run IDLE identity sheet must pass generation and visual-risk QA before sibling actions are generated. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | 38223743012 | Kaggle generator rejected candidate: required-role-idle-candidate-rejected; retry-details=The same-run IDLE identity sheet must pass generation and visual-risk QA before sibling actions are generated. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38223743012 | Kaggle generator rejected candidate: required-role-idle-candidate-rejected; retry-details=The same-run IDLE identity sheet must pass generation and visual-risk QA before sibling actions are generated. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | 38220177038 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.109 |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | 38220177038 | Manual full-frame review of collector 38220177038 REJECTED: work console/blue screen changes dimensions and floats away from gloves, frame 5 has cropped/non-standard character silhouette, helmet/face switch across sequence; cross-frame identity and hand-tool contact not stable. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | 38220177038 | Kaggle generator rejected candidate: carry-too-static mean-change=0.065<0.120 |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | 38220177038 | Manual full-frame review of collector 38220177038 REJECTED: facial identity, helmet model, clothing colors and repair tool all morph across frames; disconnected wire/prop on frame 6 and different prop geometry frame 8-10; no single coherent repair interaction. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | 38220177038 | Manual full-frame review of collector 38220177038 REJECTED: character mostly stands neutral for first 7 frames with unrelated face and pose drift; final frame abruptly adds floating gold rays without a readable progressive arm-raise/celebration. |
| CHR-ENG-IDLE | ENG | IDLE | REJECTED_SEMANTIC | 38223743012 | Full-frame manual review of collector 38223743012 REJECTED: helmet/face identity is materially more coherent across six frames, but a long baked gray ground-shadow bar appears in 5/6 frames (BAKED_GROUND_SHADOW_RISK); all six feet/ankle profiles remain fused (LOWER_LIMB_STRUCTURE_UNVERIFIED). Transparent standalone idle is not release-grade. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | 38223743012 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.196 |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | 38223743012 | Full-frame manual review of collector 38223743012 REJECTED: head identity stabilized by 10/10 IDLE locks, but tools/panels and glove-hand attachment change across ten frames; mostly idle body poses rather than readable work motion. Ground shadows contaminate 9/10 frames, image-only risk BLOCKING. |
| CHR-ENG-CARRY | ENG | CARRY | REJECTED_SEMANTIC | 38223743012 | Full-frame manual review of collector 38223743012 REJECTED: crate shape and face continuity improved and 8 frames passed technical QA, but leg/feet sequence is mostly planted with sudden silhouette jump (max adjacent alpha-change 0.683); baked ground shadow 7/8 frames and foot structure not verifiable. Not a convincing walking carry loop. |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | 38223743012 | Full-frame manual review of collector 38223743012 REJECTED: stable head mask but inconsistent tools, missing repair target, changing belts/gloves/boots and an unanchored cable in frame 7; abrupt pose jump (max adjacent alpha-change 0.501), inconsistent floor shadow in several frames. No coherent frame-to-frame repair contact. |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | 38223743012 | Kaggle generator rejected candidate: celeb-upper-silhouette-jump=0.630>0.450 |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
