# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |
| CHR-OP-WORK | OP | WORK | AWAITING_REVIEW | 38185962170 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |
| CHR-OP-CELEB | OP | CELEB | AWAITING_REVIEW | 38185962170 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-WALK | LOG | WALK | REJECTED_SEMANTIC | 38185962170 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.112 |
| CHR-LOG-WORK | LOG | WORK | AWAITING_REVIEW | 38185962170 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-CARRY | LOG | CARRY | AWAITING_REVIEW | 38185962170 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-REPAIR | LOG | REPAIR | REJECTED_SEMANTIC | 38185962170 | Kaggle generator rejected candidate: image-risk:LOWER_LIMB_STRUCTURE_UNVERIFIED,PALETTE_IDENTITY_DISCONTINUITY_RISK; retry-details=edge contact |
| CHR-LOG-CELEB | LOG | CELEB | REJECTED_SEMANTIC | 38185962170 | Kaggle generator rejected candidate: frame-3-failed; retry-details=edge contact |
| CHR-ENG-IDLE | ENG | IDLE | DISPATCHED | 38170795132 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |
| CHR-ENG-WALK | ENG | WALK | DISPATCHED | 38170795132 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |
| CHR-ENG-WORK | ENG | WORK | DISPATCHED | 38170795132 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CARRY | ENG | CARRY | DISPATCHED | 38170795132 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |
| CHR-ENG-REPAIR | ENG | REPAIR | DISPATCHED | 38170795132 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CELEB | ENG | CELEB | DISPATCHED | 38170795132 | Fresh kaggle-character-sheet dispatch 38185997333 is active; semantic review remains required after candidate collection. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
