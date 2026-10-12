# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | REJECTED_SEMANTIC | 38201816567 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.167 |
| CHR-OP-WORK | OP | WORK | REJECTED_SEMANTIC | 38185962170 | Manual full-frame review of collector 38185962170 REJECTED: hand tool is detached/morphs between box, camera-like wheel and panel, not consistently held or operated; unsafe to promote. |
| CHR-OP-CARRY | OP | CARRY | AWAITING_REVIEW | 38201816567 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-REPAIR | OP | REPAIR | REJECTED_SEMANTIC | 38201816567 | Kaggle generator rejected candidate: frame-5-failed; retry-details=edge contact / detached-artifact component=2452/10701 |
| CHR-OP-CELEB | OP | CELEB | REJECTED_SEMANTIC | 38185962170 | Manual full-frame review of collector 38185962170 REJECTED: poses remain mostly standing neutral; a wheel-like accessory appears near the final frame; no coherent progressive raised-arm celebration. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38201851009 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38201851009 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38201851009 is active; semantic review remains required after candidate collection. |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38201851009 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38201851009 is active; semantic review remains required after candidate collection. |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38201816567 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | DISPATCHED | 38201816567 | Fresh kaggle-character-sheet dispatch 38201851009 is active; semantic review remains required after candidate collection. |
| CHR-ENG-WORK | ENG | WORK | AWAITING_REVIEW | 38201816567 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-CARRY | ENG | CARRY | DISPATCHED | 38201816567 | Fresh kaggle-character-sheet dispatch 38201851009 is active; semantic review remains required after candidate collection. |
| CHR-ENG-REPAIR | ENG | REPAIR | AWAITING_REVIEW | 38201816567 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-CELEB | ENG | CELEB | DISPATCHED | 38201816567 | Fresh kaggle-character-sheet dispatch 38201851009 is active; semantic review remains required after candidate collection. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
