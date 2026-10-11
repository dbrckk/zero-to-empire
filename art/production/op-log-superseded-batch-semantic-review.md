# OP + LOG — independent semantic review of superseded Kaggle batch

- **Original Kaggle producer run:** [38170846318](https://github.com/dbrckk/zero-to-empire/actions/runs/38170846318)
- **Recovered review evidence:** [38175207078](https://github.com/dbrckk/zero-to-empire/actions/runs/38175207078), artifact `kaggle-superseded-character-batch-38170820039`
- **Generator dispatch token:** `38170820039` (v1.18 initial)
- **Status:** reviewed, no strict promotion authorised.
- **Result:** 12 attempts; 8 candidate atlases pass deterministic technical QA, 4 animation QA rejections; **0 newly approved as strict DONE**.
- **Current canonical target:** 219/235 strict DONE, 16 remain. The separately submitted newer run `38174945678` must not inherit approvals from this source.

## Source-specific frame review

| Asset | Generator / technical QA | Semantic outcome and observed defect |
|---|---|---|
| CHR-OP-IDLE | CANDIDATE, technical PASS | Context-only reference sheet; not a new strict count. Identity must be checked jointly against accepted actions before an IDLE replacement. |
| CHR-OP-WALK | REJECT | Lower-body motion too static (0.156); no readable alternating walk. |
| CHR-OP-WORK | CANDIDATE, technical PASS | **REJECTED SEMANTIC:** device changes form and is not consistently held/operated by the worker. |
| CHR-OP-CARRY | REJECT | Mean motion 0.115 below 0.120 requirement; an edge-contact retry was recorded. |
| CHR-OP-REPAIR | CANDIDATE, technical PASS | **REJECTED SEMANTIC:** inconsistent repair object (box, circle/ring), unstable tooling, and visible variation in character identity. |
| CHR-OP-CELEB | CANDIDATE, technical PASS | **REJECTED SEMANTIC:** mostly near-idle frames followed by an abrupt final arm raise rather than a coherent celebration. |
| CHR-LOG-IDLE | CANDIDATE, technical PASS | Context-only reference sheet; not a new strict count. Identity must be checked jointly against accepted actions before an IDLE replacement. |
| CHR-LOG-WALK | REJECT | Lower-body motion too static (0.174); weak locomotion. |
| CHR-LOG-WORK | CANDIDATE, technical PASS | **REJECTED SEMANTIC:** equipment appears disconnected from the hands and changes; headgear/outfit drift in later frames. |
| CHR-LOG-CARRY | REJECT | Mean motion 0.069 below 0.120 requirement; not a readable carrying loop. |
| CHR-LOG-REPAIR | CANDIDATE, technical PASS | **REJECTED SEMANTIC:** tools and props morph between panels, coils and loose cables, without a consistent repair point. |
| CHR-LOG-CELEB | CANDIDATE, technical PASS | **REJECTED SEMANTIC:** eight mostly neutral stances, not a legible celebration. |

## Required changes before reconsideration

The next coherent role-family candidate must use one stable face, helmet, outfit and silhouette across all actions; attach unchanged props to the hands and work point; create visible limb movement appropriate to WALK, WORK, CARRY, REPAIR and CELEB; preserve the frame pivot, full-body framing and transparent margins.

The ten action-specific rejection-memory entries from this review are stored in `art/production/generation-rejection-ledger.json`, citing producer run `38170846318`. These instructions guide future generation only. Technical QA results are not semantic approval; neither this review nor a generated contact sheet may change `strict_status` to `DONE` automatically.
