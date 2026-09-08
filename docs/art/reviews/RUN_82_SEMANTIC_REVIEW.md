# Run 82 semantic review

Run: GitHub Actions `34145936891`  
Artifact: `10030821750`  
Generator: `v15.2-live-semantic-validation`

## Technical result
- Workflow: SUCCESS.
- Requested: 56 building tiers.
- Fresh technically validated exports: 28.
- Accepted technical families: BLD-05, BLD-08, BLD-10, BLD-11 (T0→T6).
- Rejected before export: BLD-04, BLD-09, BLD-12, BLD-13.
- Anchor attempts: 32.
- Branch attempts: 16.
- Context attempts: 117.
- Live rejections: 42.
- Early branch aborts: 10.
- Kernel generation time reached roughly 8,489 seconds (~141.5 min) before final export/report work.

## Semantic review
**PROMOTE: 0 / 28.** Strict DONE delta: **+0**.

The live detector improved technical selectivity and prevented four complete bad families from being exported, but the exported contact sheet still contains a systematic semantic contaminant that the geometric detector missed: visible orange/yellow construction cranes, gantries, suspended booms and temporary site equipment surrounding or attached to essentially every accepted family.

### BLD-05 — REJECT family
- T0 already contains a roof crane/boom and construction-site accessories.
- The crane motif grows with the building and remains visually dominant through T6.
- Large slab/site-card treatment becomes increasingly visible.
- Reads as a building under construction rather than a clean final operating production sprite.

### BLD-08 — REJECT family
- T0 starts with a crane/hoist immediately beside the building.
- Later tiers add larger tower/jib crane structures, flags/markers and site furniture.
- T5/T6 are especially dominated by construction cranes despite `max-boom=0.00` in the structural report, demonstrating a false negative in the boom detector.

### BLD-10 — REJECT family
- T0→T6 consistently contain large paired overhead crane/gantry structures.
- Round site/platform base remains visually prominent.
- The family progression is coherent, but it is coherent around an invalid construction-site composition.

### BLD-11 — REJECT family
- T0 already contains a large crane beside the compact building.
- Crane structures remain or multiply throughout the sequence.
- T6 becomes a large industrial building but is still framed by obvious construction cranes and temporary equipment.

## What v15.2 improved
- Technical yield became selective rather than indiscriminate: 28/56 exported instead of 56/56.
- Live QA caught many slab and boom failures during generation.
- 42 contextual rejections and 10 early aborts avoided exporting four failed families.
- Family continuity and scale progression remain generally strong.

## Critical finding
`boom_score()` is not a reliable semantic crane detector. The report gives accepted families `max-boom=0.00` while the contact sheet visibly shows large cranes. Geometric alpha heuristics cannot replace source-generation control or semantic image understanding.

The next production run must therefore **not** simply tighten the same detector. It should use v16.1 shape-first positive source locking, where the T0 prompt first establishes a clean industrial building mass before secondary machinery/detail is introduced. A bad T0 source must never seed an entire family.

## Decision
No run82 image is promoted to runtime. Canonical strict ledger remains **112 / 235 DONE**.
