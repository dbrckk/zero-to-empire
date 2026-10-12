# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **220/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38281171130 is active; semantic review remains required after candidate collection. |
| CHR-OP-WORK | OP | WORK | REJECTED_SEMANTIC | 38281126201 | Manual complete 10-frame review of Kaggle collector 38281126201: face/headgear relatively stable, but all ten poses remain near idle; wrist tools and screens appear/disappear or morph, frame 7 changes uniform/arm proportions, and no fixed work target or tool-contact action is visible. REJECTED for premium work semantics. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38281171130 is active; semantic review remains required after candidate collection. |
| CHR-OP-REPAIR | OP | REPAIR | REJECTED_SEMANTIC | 38281126201 | Manual complete 10-frame review of Kaggle collector 38281126201: face stable but arms/tools change randomly, frame 7 shows a large disconnected disc/console over torso; no consistent repair point or progressive repair animation. REJECTED for props and action semantics. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38281171130 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38281171130 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38281171130 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38281171130 is active; semantic review remains required after candidate collection. |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38281171130 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | 38281126201 | Fresh kaggle-character-sheet dispatch 38281171130 is active; semantic review remains required after candidate collection. |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38263062708 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | 38263062708 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.098 |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | 38263062708 | Kaggle generator rejected candidate: image-risk:BAKED_GROUND_SHADOW_RISK; retry-details=edge contact |
| CHR-ENG-CARRY | ENG | CARRY | REJECTED_SEMANTIC | 38263062708 | Kaggle generator rejected candidate: image-risk:BAKED_GROUND_SHADOW_RISK,LOWER_LIMB_STRUCTURE_UNVERIFIED |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | 38263062708 | Kaggle generator rejected candidate: image-risk:FACE_HEADGEAR_STRUCTURE_DRIFT_RISK |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | 38263062708 | Kaggle generator rejected candidate: celeb-upper-silhouette-jump=0.660>0.450 |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
