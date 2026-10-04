# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **216/235**
- Strict DONE: **216/235**
- Semantic review remaining: **19**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review note |
|---|---|---|---|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; visible face/clothing/headgear drift across frames and the sequence still reads as pose changes rather than one coherent alternating walk cycle. |
| CHR-OP-WORK | OP | WORK | DISPATCHED | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; identity drifts between frames and the tool/work interaction is inconsistent, with several frames reading as neutral standing. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; no rectangular crate is carried between both hands and the animation reads as standing with changing accessories. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; identity/body details drift and there is no consistent repair tool visibly contacting one repair point. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; no clear arm-raise celebration occurs and the frames remain mostly neutral standing poses. |
| CHR-TECH-WALK | TECH | WALK | DISPATCHED | Kaggle generator rejected candidate: walk-too-static lower-motion=0.141 |
| CHR-TECH-WORK | TECH | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; identity/headgear and accessories drift between frames and the sequence lacks one consistent visible tool contacting a stable work point. |
| CHR-TECH-CARRY | TECH | CARRY | REJECTED_SEMANTIC | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; identity and headgear drift, the crate appears only in some frames or changes form, and there is no coherent two-hand carrying stride. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | Kaggle generator rejected candidate: walk-too-static lower-motion=0.205 |
| CHR-LOG-WORK | LOG | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; face/headgear/body details vary significantly and the frames remain mostly neutral standing without one readable repeated work interaction. |
| CHR-LOG-CARRY | LOG | CARRY | REJECTED_SEMANTIC | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; severe identity/headgear drift, front/back turntable changes, and the crate is inconsistent or absent instead of being held with both hands through a carrying stride. |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | Semantic review 2026-10-03: rejected; identity/clothing/headgear drift strongly across frames and there is no consistent visible repair tool contacting a repair point. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | Kaggle generator rejected candidate: celeb-too-static mean-change=0.094<0.100 |
| CHR-ENG-IDLE | ENG | IDLE | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; atlas is almost entirely cropped head/torso fragments, not a full-body idle loop. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; sequence behaves like a front/back turntable with identity/clothing drift rather than a stable three-quarter walk cycle. |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; action remains mostly static with weak or absent readable work motion. |
| CHR-ENG-CARRY | ENG | CARRY | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; frames are cropped head/torso fragments with no crate and no carrying stride. |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; first frame is severely cropped, face/helmet/body proportions drift strongly across frames, and the sequence lacks a readable repair/tool interaction. |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; severe crop and major identity/body drift, with no readable celebration arm-raise cycle. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
