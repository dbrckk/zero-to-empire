# Run 80 semantic review

Run: `34125123246`
Artifact: `10020955827`
Generator: `building-family-flux-v14-prompt-safe-monotonic`

## Technical result
- Workflow conclusion: SUCCESS.
- Fresh candidates exported: 21.
- Families exported: BLD-08 T0-T6, BLD-09 T0-T6, BLD-13 T0-T6.
- GitHub technical QA passed for all exported candidates.

## Full-resolution semantic result
**0 / 21 promoted. Strict DONE delta: +0.**

### BLD-08
Rejected as a family. The sequence has clear size progression, but T0 already contains an oversized paved/platform footprint, multiple small human figures, a crane/hoist, signage/emblems and loose site props. Later tiers retain large floor-card/base treatment and introduce additional decorative/utility elements that violate the one-building cutout contract. The family is industrial in spirit but not clean enough for final runtime.

### BLD-09
Rejected as a family. The white/cyan sequence reads increasingly like a civic/science campus or monument complex rather than a coherent production building. Large platform footprints remain visible and detached site furniture/markers appear. Identity drifts substantially across the family despite technical growth passing.

### BLD-13
Rejected as a family. The sequence evolves into a tall civic/religious/clock-tower/castle-like landmark. It no longer reads as the required industrial stellar precision works. Tiers add ornamental spires/crowns and architectural language inconsistent with the intended factory DNA.

## What improved vs runs 77-79
- v14 solved the previous zero-yield problem: 21 technically valid candidates survived family QA.
- T0→T6 scale progression is now visible rather than flattened by normalization.
- Alpha isolation is cleaner and the workflow/QA path completed successfully.

## Remaining root cause
The dominant blocker is now semantic contamination, not technical yield. FLUX is still inventing people, cranes, flags, paved site cards and civic/religious architecture. A single seed branch per family is therefore too risky even when structural QA is green.

## Required next strategy
1. Over-generate multiple T0 anchors per family.
2. Reject contaminated T0 anchors before spending GPU on T1-T6.
3. Evolve at least two surviving branches when possible.
4. Score complete branches for identity, growth, compactness, slab contamination and drift; export only the best branch.
5. Strengthen prompts against people, cranes, flags, monuments, churches, civic towers and presentation platforms.
6. Keep human/full-resolution semantic review as the final gate before promotion.
