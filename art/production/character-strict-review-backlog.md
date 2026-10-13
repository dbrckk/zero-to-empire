# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38309355566 | Fresh kaggle-character-sheet dispatch 38337702043 is active; semantic review remains required after candidate collection. |
| CHR-OP-WORK | OP | WORK | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38309355566 | Fresh kaggle-character-sheet dispatch 38337702043 is active; semantic review remains required after candidate collection. |
| CHR-OP-REPAIR | OP | REPAIR | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38296422676 | Fresh kaggle-character-sheet dispatch 38337702043 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38337702043 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38337702043 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38337702043 is active; semantic review remains required after candidate collection. |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38337702043 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | 38337667460 | Fresh kaggle-character-sheet dispatch 38337702043 is active; semantic review remains required after candidate collection. |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38337667460 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | 38337667460 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.160; retry-details=detached-artifact component=742/9992 / detached-artifact component=906/9838 / detached-artifact component=770/10485 / detached-artifact component=853/10351 |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | 38337667460 | Kaggle generator rejected candidate: image-risk:HEAD_FACE_HEADGEAR_COLOR_DISCONTINUITY_RISK,FACE_HEADGEAR_STRUCTURE_DRIFT_RISK,LOWER_LIMB_STRUCTURE_UNVERIFIED; retry-details=detached-artifact component=792/8793 / detached-artifact component=1043/9864 / detached-artifact component=1207/10230 |
| CHR-ENG-CARRY | ENG | CARRY | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | 38337667460 | Kaggle generator rejected candidate: frame-1-failed; retry-details=detached-artifact component=757/8638 / detached-artifact component=682/10176 / detached-artifact component=1029/8813 |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | 38337667460 | Kaggle generator rejected candidate: celeb-upper-silhouette-jump=0.702>0.450 |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
