# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **220/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38201816567 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.167 |
| CHR-OP-WORK | OP | WORK | DISPATCHED | 38185962170 | Manual full-frame review of collector 38185962170 REJECTED: hand tool is detached/morphs between box, camera-like wheel and panel, not consistently held or operated; unsafe to promote. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38201816567 | Manual visual review of collector 38201816567 REJECTED: 8 frames show box handles/panels morphing, gloves inconsistently contacting box, face/glasses shifts and pronounced baked floor shadows; mask gait metric pass is insufficient for a coherent AAA carrying loop. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | 38201816567 | Kaggle generator rejected candidate: frame-5-failed; retry-details=edge contact / detached-artifact component=2452/10701 |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38185962170 | Manual full-frame review of collector 38185962170 REJECTED: poses remain mostly standing neutral; a wheel-like accessory appears near the final frame; no coherent progressive raised-arm celebration. |
| CHR-LOG-WALK | LOG | WALK | REJECTED_SEMANTIC | 38220177038 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.109 |
| CHR-LOG-WORK | LOG | WORK | REJECTED_SEMANTIC | 38220177038 | Manual full-frame review of collector 38220177038 REJECTED: work console/blue screen changes dimensions and floats away from gloves, frame 5 has cropped/non-standard character silhouette, helmet/face switch across sequence; cross-frame identity and hand-tool contact not stable. |
| CHR-LOG-CARRY | LOG | CARRY | REJECTED_SEMANTIC | 38220177038 | Kaggle generator rejected candidate: carry-too-static mean-change=0.065<0.120 |
| CHR-LOG-REPAIR | LOG | REPAIR | REJECTED_SEMANTIC | 38220177038 | Manual full-frame review of collector 38220177038 REJECTED: facial identity, helmet model, clothing colors and repair tool all morph across frames; disconnected wire/prop on frame 6 and different prop geometry frame 8-10; no single coherent repair interaction. |
| CHR-LOG-CELEB | LOG | CELEB | REJECTED_SEMANTIC | 38220177038 | Manual full-frame review of collector 38220177038 REJECTED: character mostly stands neutral for first 7 frames with unrelated face and pose drift; final frame abruptly adds floating gold rays without a readable progressive arm-raise/celebration. |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38201816567 | Visually plausible standalone ENG IDLE from collector 38201816567, but HOLD semantic approval until full six-action same-identity family and Android runtime evidence; current in-flight wave 38201875119 may supply a newer same-run reference. |
| CHR-ENG-WALK | ENG | WALK | DISPATCHED | 38220177038 | Kaggle generator rejected candidate: required-role-idle-candidate-rejected; retry-details=The same-run IDLE identity sheet must pass generation and visual-risk QA before sibling actions are generated. |
| CHR-ENG-WORK | ENG | WORK | DISPATCHED | 38201816567 | Manual visual review of collector 38201816567 REJECTED: worker changes facial identity/headwear and instrumentation across frames, a detached equipment panel includes generated pseudo-text ENG, no consistent tool-hand contact or action. |
| CHR-ENG-CARRY | ENG | CARRY | DISPATCHED | 38220177038 | Kaggle generator rejected candidate: required-role-idle-candidate-rejected; retry-details=The same-run IDLE identity sheet must pass generation and visual-risk QA before sibling actions are generated. |
| CHR-ENG-REPAIR | ENG | REPAIR | DISPATCHED | 38201816567 | Manual visual review of collector 38201816567 REJECTED: varying face/helmet, repair props morph between panel/ring/hand tool, floating disconnected gear and inadequate animation continuity; does not share stable ENG IDLE identity. |
| CHR-ENG-CELEB | ENG | CELEB | DISPATCHED | 38220177038 | Kaggle generator rejected candidate: required-role-idle-candidate-rejected; retry-details=The same-run IDLE identity sheet must pass generation and visual-risk QA before sibling actions are generated. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
