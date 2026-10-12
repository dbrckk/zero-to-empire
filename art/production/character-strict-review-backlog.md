# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | REJECTED_SEMANTIC | 38309355566 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.176 |
| CHR-OP-WORK | OP | WORK | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | REJECTED_SEMANTIC | 38309355566 | Kaggle generator rejected candidate: carry-too-static mean-change=0.095<0.120 |
| CHR-OP-REPAIR | OP | REPAIR | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CELEB | OP | CELEB | REJECTED_SEMANTIC | 38296422676 | Visual frame-by-frame review of collector 38296422676: all eight poses keep both hands at waist/hip height; no raised-arm celebration despite technical arm-frames=8/8. Clothes, boot and cargo strap change between frames; gray cast ground shadow persists. REJECTED_SEMANTIC: false positive in old shoulder-wide mask reach detector. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | 38296422676 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | 38296422676 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | 38296422676 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | 38296422676 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | 38296422676 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | DISPATCHED | 38309355566 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |
| CHR-ENG-WORK | ENG | WORK | DISPATCHED | 38309355566 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CARRY | ENG | CARRY | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-REPAIR | ENG | REPAIR | DISPATCHED | 38309355566 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CELEB | ENG | CELEB | DISPATCHED | 38309355566 | Fresh kaggle-character-sheet dispatch 38309413055 is active; semantic review remains required after candidate collection. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
