# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **216/235**
- Strict DONE: **216/235**
- Semantic review remaining: **19**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review note |
|---|---|---|---|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | Kaggle generator rejected candidate: frame-0-failed |
| CHR-OP-WORK | OP | WORK | DISPATCHED | Kaggle generator rejected candidate: frame-0-failed |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | Kaggle generator rejected candidate: frame-0-failed |
| CHR-OP-REPAIR | OP | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-04 of late v1.10 async output from run 37181577039: rejected; severe face/body/headgear drift across frames and the sequence is mostly standing/tool-holding rather than one readable repair interaction. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | Kaggle generator rejected candidate: frame-0-failed |
| CHR-TECH-WALK | TECH | WALK | DISPATCHED | Kaggle generator rejected candidate: duplicate-adjacent-frame |
| CHR-TECH-WORK | TECH | WORK | DISPATCHED | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; identity/headgear and accessories drift between frames and the sequence lacks one consistent visible tool contacting a stable work point. |
| CHR-TECH-CARRY | TECH | CARRY | DISPATCHED | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; identity and headgear drift, the crate appears only in some frames or changes form, and there is no coherent two-hand carrying stride. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | Kaggle generator rejected candidate: walk-too-static lower-motion=0.164 |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; face/headgear/body details vary significantly and the frames remain mostly neutral standing without one readable repeated work interaction. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; severe identity/headgear drift, front/back turntable changes, and the crate is inconsistent or absent instead of being held with both hands through a carrying stride. |
| CHR-LOG-REPAIR | LOG | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-04 of late v1.10 async output from run 37181577039: rejected; logistics identity/headgear changes materially across frames and no stable repair point/tool contact is maintained. |
| CHR-LOG-CELEB | LOG | CELEB | REJECTED_SEMANTIC | Semantic review 2026-10-04 of late v1.10 async output from run 37181577039: rejected; frames remain mostly static neutral standing with no clear overhead arm-raise celebration and visible identity/headgear variation. |
| CHR-ENG-IDLE | ENG | IDLE | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; atlas is almost entirely cropped head/torso fragments, not a full-body idle loop. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; sequence behaves like a front/back turntable with identity/clothing drift rather than a stable three-quarter walk cycle. |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; action remains mostly static with weak or absent readable work motion. |
| CHR-ENG-CARRY | ENG | CARRY | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; frames are cropped head/torso fragments with no crate and no carrying stride. |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; first frame is severely cropped, face/helmet/body proportions drift strongly across frames, and the sequence lacks a readable repair/tool interaction. |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; severe crop and major identity/body drift, with no readable celebration arm-raise cycle. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
