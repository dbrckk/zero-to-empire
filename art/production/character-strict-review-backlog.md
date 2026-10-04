# Character strict-review backlog

Generated from art/production/master-asset-queue.json after production completion.

- Production processed: **215/235**
- Strict DONE: **215/235**
- Semantic review remaining: **20**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review note |
|---|---|---|---|---|
| CHR-OP-WALK | OP | WALK | REJECTED_SEMANTIC | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; visible face/clothing/headgear drift across frames and the sequence still reads as pose changes rather than one coherent alternating walk cycle. |
| CHR-OP-WORK | OP | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; identity drifts between frames and the tool/work interaction is inconsistent, with several frames reading as neutral standing. |
| CHR-OP-CARRY | OP | CARRY | REJECTED_SEMANTIC | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; no rectangular crate is carried between both hands and the animation reads as standing with changing accessories. |
| CHR-OP-REPAIR | OP | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; identity/body details drift and there is no consistent repair tool visibly contacting one repair point. |
| CHR-OP-CELEB | OP | CELEB | REJECTED_SEMANTIC | Semantic review 2026-10-03 of Kaggle v1.9 run 37149965973: rejected; no clear arm-raise celebration occurs and the frames remain mostly neutral standing poses. |
| CHR-TECH-IDLE | TECH | IDLE | DISPATCHED | Semantic review 2026-10-03: rejected; atlas is heavily cropped to head/torso fragments, lacks full-body framing, and shows no usable idle animation. |
| CHR-TECH-WALK | TECH | WALK | DISPATCHED | Semantic review 2026-10-03: rejected; poses read as standing/turntable frames rather than a coherent alternating walk cycle, with visible head/identity drift. |
| CHR-TECH-WORK | TECH | WORK | DISPATCHED | Semantic review 2026-10-03: rejected; technically valid atlas is too static and the work/tool action is not readable at gameplay size. |
| CHR-TECH-CARRY | TECH | CARRY | DISPATCHED | Semantic review 2026-10-03: rejected; no crate/component is consistently visible between both hands and the sequence reads as static standing rather than carrying. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | Semantic review 2026-10-03: rejected; large identity/clothing drift across frames and no coherent alternating walk cycle. |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | Semantic review 2026-10-03: rejected; action is too static and lacks a clearly readable work/tool interaction. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | Semantic review 2026-10-03: rejected; frames are torso/leg fragments with turntable orientation changes and no visible crate carried between both hands. |
| CHR-LOG-REPAIR | LOG | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; identity/clothing/headgear drift strongly across frames and there is no consistent visible repair tool contacting a repair point. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | Semantic review 2026-10-03: rejected; atlas is severely cropped to head/torso fragments and does not contain a readable arm-raise celebration sequence. |
| CHR-ENG-IDLE | ENG | IDLE | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; atlas is almost entirely cropped head/torso fragments, not a full-body idle loop. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; sequence behaves like a front/back turntable with identity/clothing drift rather than a stable three-quarter walk cycle. |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; action remains mostly static with weak or absent readable work motion. |
| CHR-ENG-CARRY | ENG | CARRY | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; frames are cropped head/torso fragments with no crate and no carrying stride. |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; first frame is severely cropped, face/helmet/body proportions drift strongly across frames, and the sequence lacks a readable repair/tool interaction. |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; severe crop and major identity/body drift, with no readable celebration arm-raise cycle. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change strict_status to DONE.
