# OP/LOG active character wave — semantic review (2026-10-13)

- Canonical asset creation and integration location: **this repository** (`dbrckk/zero-to-empire`).
- GPU submission: [38337737784](https://github.com/dbrckk/zero-to-empire/actions/runs/38337737784).
- Collector and original PNG artifact: [38367845734](https://github.com/dbrckk/zero-to-empire/actions/runs/38367845734), artifact `kaggle-async-character-batch`.
- Review evidence in that artifact: `output/review-panels/review-frames-op.png`, `review-frames-log.png`, head strips and per-animation mobile panels.
- Total: **4 technical candidates out of 10 requested sheets** (including 2 context-only IDLEs). **0 newly approved strict DONE.**

| Asset | GPU technical result | Human semantic result |
|---|---|---|
| CHR-OP-IDLE | CANDIDATE | Context-only reference. Plausible orange helmet and dark coveralls, but not promoted as a replacement. |
| CHR-OP-WALK | CANDIDATE | **REJECT**. No clear heel-to-toe stepping; nearly stationary feet and changing clothing details despite numerical motion score. |
| CHR-OP-CARRY | REJECT | Too static, mean-change=0.062 < 0.120. |
| CHR-OP-CELEB | REJECT | Celebration upper-body gesture unreadable; only 2/7 meaningful transitions. |
| CHR-LOG-IDLE | CANDIDATE | Context-only white-helmet, orange-jacket identity reference; not promoted. |
| CHR-LOG-WALK | REJECT | Insufficient lower-body motion=0.166. |
| CHR-LOG-WORK | REJECT | Headgear/face drift and equipment color inconsistency. |
| CHR-LOG-CARRY | REJECT | Too static, mean-change=0.062 < 0.120. |
| CHR-LOG-REPAIR | CANDIDATE | **REJECT**. Hand tools morph, no stable contact point, boots/face change; movement score alone is not proof of repair. |
| CHR-LOG-CELEB | REJECT | Excessive upper-body silhouette jump=0.641. |

## Operational correction

The async collector had only `workflow_dispatch` and no schedule or file-based trigger. That caused an active GPU wave to remain uncollected until manually dispatched. It now has a 15-minute cron, push trigger on `ops/kaggle-collector-trigger.txt`, and `cancel-in-progress: false` to avoid interrupting artifact retrieval. A regression test verifies all three controls. This successfully collected the current wave and automatically submitted the next **OP+ENG** wave, [38367943017](https://github.com/dbrckk/zero-to-empire/actions/runs/38367943017).

## Acceptance criteria

Keep every remaining asset's source, candidate evidence, review decision, approved PNG/atlas, Android runtime conversion and manifest tracking inside this repository and its linked GitHub Actions artifacts. External Kaggle/Pollinations providers are generation workers, **not authoritative storage or a substitute for committing approved assets**. Reject fake motion, identity drift, floating tools, broken props and invalid Android evidence. No technical candidate counts as strict DONE until approved, integrated and runtime-validated.
