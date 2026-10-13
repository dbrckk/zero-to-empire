# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **225/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | AWAITING_REVIEW | 38367845734 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-WORK | OP | WORK | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | REJECTED_SEMANTIC | 38367845734 | Kaggle generator rejected candidate: carry-too-static mean-change=0.062<0.120 |
| CHR-OP-REPAIR | OP | REPAIR | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38367845734 | Fresh kaggle-character-sheet dispatch 38367912706 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WALK | LOG | WALK | REJECTED_SEMANTIC | 38367845734 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.166 |
| CHR-LOG-WORK | LOG | WORK | REJECTED_SEMANTIC | 38367845734 | Kaggle generator rejected candidate: image-risk:FACE_HEADGEAR_STRUCTURE_DRIFT_RISK,TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK |
| CHR-LOG-CARRY | LOG | CARRY | REJECTED_SEMANTIC | 38367845734 | Kaggle generator rejected candidate: carry-too-static mean-change=0.062<0.120 |
| CHR-LOG-REPAIR | LOG | REPAIR | AWAITING_REVIEW | 38367845734 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-CELEB | LOG | CELEB | REJECTED_SEMANTIC | 38367845734 | Kaggle generator rejected candidate: celeb-upper-silhouette-jump=0.641>0.450; retry-details=edge contact |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38337667460 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38367912706 is active; semantic review remains required after candidate collection. |
| CHR-ENG-WORK | ENG | WORK | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38367912706 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CARRY | ENG | CARRY | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-REPAIR | ENG | REPAIR | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38367912706 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CELEB | ENG | CELEB | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38367912706 is active; semantic review remains required after candidate collection. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
