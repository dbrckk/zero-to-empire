# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38367845734 | Manual full-frame review of collector 38367845734 REJECTED: eight poses preserve almost identical standing legs, mostly lateral pixel wobble and changed trousers/gloves; no convincing heel-to-toe gait or foot lift despite technical walk-motion=0.236. |
| CHR-OP-WORK | OP | WORK | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38367845734 | Kaggle generator rejected candidate: carry-too-static mean-change=0.062<0.120 |
| CHR-OP-REPAIR | OP | REPAIR | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38427591142 | Kaggle generator rejected candidate: celeb-too-static mean-change=0.081<0.100 |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | 38367845734 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.166 |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | 38367845734 | Kaggle generator rejected candidate: image-risk:FACE_HEADGEAR_STRUCTURE_DRIFT_RISK,TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | 38367845734 | Kaggle generator rejected candidate: carry-too-static mean-change=0.062<0.120 |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | 38367845734 | Manual full-frame review of collector 38367845734 REJECTED: tool changes from flat blue console to gloves and gold rings; no fixed repair contact point, lower legs and boots morph, helmet/face varies. Technical repair-motion=0.219 does not establish action semantics. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | 38367845734 | Kaggle generator rejected candidate: celeb-upper-silhouette-jump=0.641>0.450; retry-details=edge contact |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38427591142 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | 38427591142 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.087 |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | 38427591142 | Kaggle generator rejected candidate: work-too-static mean-change=0.083<0.100; retry-details=edge contact |
| CHR-ENG-CARRY | ENG | CARRY | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | 38427591142 | Kaggle generator rejected candidate: image-risk:FACE_HEADGEAR_STRUCTURE_DRIFT_RISK |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | 38427591142 | Kaggle generator rejected candidate: celeb-too-static mean-change=0.096<0.100 |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
