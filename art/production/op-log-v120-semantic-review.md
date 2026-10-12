# OP + LOG v1.20 — technical vs semantic results

**Production dispatch:** `38281171130`  
**GPU submit run:** [38281199147](https://github.com/dbrckk/zero-to-empire/actions/runs/38281199147)  
**Collector artifact:** [38296422676](https://github.com/dbrckk/zero-to-empire/actions/runs/38296422676) (`kaggle-async-character-batch`)  
**Later retroactive audit:** [38297696128](https://github.com/dbrckk/zero-to-empire/actions/runs/38297696128)  
**Review outcome:** 0 new strict DONE. Strict total remains **219/235**.

## Source outcomes

| Asset | Producer | Independent review |
|---|---|---|
| CHR-OP-IDLE | Candidate | Context-only identity anchor. A gray cast ground shadow is visible at the feet; this is not an approved replacement. |
| CHR-OP-WALK | Rejected | Leg movement too static (lower-body motion 0.196 vs required 0.220). |
| CHR-OP-CARRY | Rejected | Lower-body carrying stride 0.178, below required 0.190. |
| CHR-OP-CELEB | Candidate technically | **Rejected semantically:** all eight frames keep arms by the hips/waist despite generator reporting 8/8 raised-arm frames. Clothing and boots visibly vary, with floor-shadow contamination. |
| CHR-LOG-IDLE | Candidate | Context-only identity anchor. Overall recognizable LOG uniform, but foot shadow and animation subtlety still need explicit visual review. |
| CHR-LOG-WALK | Rejected | Lower-body motion 0.098, below required 0.220. |
| CHR-LOG-WORK | Candidate technically | **Rejected semantically:** arms mostly stay down and the device shifts/morphs between hands and a cyan floating box rather than visibly operating a fixed workstation. |
| CHR-LOG-CARRY | Rejected | Carry mean motion 0.077, below required 0.120. |
| CHR-LOG-REPAIR | Rejected | Adjacent identity/silhouette discontinuity, recorded 0.24. |
| CHR-LOG-CELEB | Rejected | Celebration has only 1/7 meaningful upper-body transitions. |

## Real-artifact false-positive correction

The previous `celebration_arm_reach_counts` detector counted opaque pixels more than 34px away from the **entire full-body bounding-box centre**, so a left-of-centre face/helmet and wide shoulder could be mistaken for an upraised arm. The OP source produced a false technical `arm-frames=8/8` success.

The current detector uses a median **head-centred** horizontal reference and counts extended pixels only up to **helmet height**, excluding ordinary shoulders. The retroactive workflow downloaded the exact original `38296422676` collector images and independently ran `verify_character_action_candidates.py`.

**Measured regression:** OP-CELEB was originally technical PASS, but is now BLOCKING with `CELEBRATION_NO_OVERHEAD_ARM_GESTURE_RISK` and `raised_arm_frames=0`. Audit output is uploaded under `retroactive-character-motion-38296422676`. All audit updates are review-only and do not mutate canonical sprites.

## Experimental non-GPU WALK alternatives

[Review run 38298038776](https://github.com/dbrckk/zero-to-empire/actions/runs/38298038776) contains v2 CPU identity-locked WALK strips for OP, ENG and TECH. The mesh distortion is blended below the thigh instead of sharply shearing the crotch; this reduces the severe gap seen in the v1 screenshot while preserving the face, outfit, and a repeatable eight-frame loop.

**It is not premium walking yet:** arms remain largely static and there is still visible boot sliding. LOG IDLE was not accepted as a safe source for this independent comparison. These outputs remain explicitly `NEEDS_REVIEW`, are not imported into Android, and cannot count toward the 235 target without visual and runtime approval.

## Next acceptance requirements

A complete role family needs a coherent face/headgear/uniform, anchored identical crates/tools, clear pose changes with leg or arm motion (not silhouette or camera shifts), unbaked transparent backgrounds, correct runtime atlas geometry and verified Android behavior. A successful technical QA or an experimental mesh strip is **not** a completed asset.
