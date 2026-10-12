# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **222/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38296422676 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |
| CHR-OP-WORK | OP | WORK | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38296422676 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |
| CHR-OP-CELEB | OP | CELEB | AWAITING_REVIEW | 38296422676 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-WALK | LOG | WALK | REJECTED_SEMANTIC | 38296422676 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.098 |
| CHR-LOG-WORK | LOG | WORK | AWAITING_REVIEW | 38296422676 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-CARRY | LOG | CARRY | REJECTED_SEMANTIC | 38296422676 | Kaggle generator rejected candidate: carry-too-static mean-change=0.077<0.120 |
| CHR-LOG-REPAIR | LOG | REPAIR | REJECTED_SEMANTIC | 38296422676 | Kaggle generator rejected candidate: identity/silhouette jump=0.24; retry-details=edge contact |
| CHR-LOG-CELEB | LOG | CELEB | REJECTED_SEMANTIC | 38296422676 | Kaggle generator rejected candidate: celeb-unreadable-gesture upper-transitions=1/7; retry-details=edge contact |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38263062708 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | DISPATCHED | 38263062708 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |
| CHR-ENG-WORK | ENG | WORK | DISPATCHED | 38263062708 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CARRY | ENG | CARRY | DISPATCHED | 38263062708 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |
| CHR-ENG-REPAIR | ENG | REPAIR | DISPATCHED | 38263062708 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CELEB | ENG | CELEB | DISPATCHED | 38263062708 | Fresh kaggle-character-sheet dispatch 38296483142 is active; semantic review remains required after candidate collection. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
