# Single Sprite Generator Contract

This contract exists to prevent contact sheets, atlases, dashboards and multi-asset compositions from entering the final art pipeline.

## Hard generation rule

**ONE GENERATION OUTPUT = ONE FINAL SPRITE CANDIDATE.**

Never ask the image model to show tiers, variants, progress, a grid, a catalog, a lineup, a sheet, multiple buildings, multiple props or several categories in one image.

When producing several assets in parallel, request multiple independent image outputs (`n > 1`) while keeping each output constrained to a single isolated subject. Never ask for several subjects inside one canvas.

## Required visual prompt skeleton

Use this structure for every final asset request:

> Create exactly ONE isolated game sprite candidate: {ASSET_NAME}. The image must contain one primary subject only. Center it on a genuinely transparent RGBA background. No poster, no dashboard, no contact sheet, no sprite sheet, no atlas, no grid, no alternate versions, no neighboring assets, no comparison, no labels, no captions, no UI, no readable text, no logos, no watermark. 2.5D 3/4 perspective, 30–38 degree camera family, upper-left key light, cool fill, selective warm/cyan emissive accents, premium mobile AAA materials, strong silhouette, phone-readable detail, clean alpha edge, contact shadow only, >=8% safety padding, bottom-center world pivot. Subject must occupy roughly 65–80% of the canvas. Output only that one subject.

## Negative composition rules

Reject and regenerate if any of the following appears:
- more than one major disconnected subject;
- repeated versions or upgrade tiers;
- a row/column/grid layout;
- baked category or tier text;
- nontransparent rectangular background;
- decorative frame, poster or infographic presentation;
- another building/vehicle/worker/prop placed beside the requested sprite;
- readable branding or generated pseudo-text;
- subject touching canvas edges.

Small attached functional parts that logically belong to the requested asset are allowed. For a building, attached awnings, pipes, crates, planters, integrated machinery and its contact shadow remain part of the single subject.

## Batch policy

Parallel batches are allowed only as independent outputs. Example: request 4 images with the same generation call, where output 1 is one candidate, output 2 is one candidate, etc. The pipeline still validates every file independently.

## Acceptance state

A generated image is only `ART`. It becomes `DONE` only after cleanup, isolated-sprite validation, Android optimization, runtime integration, in-game visibility and green Android CI, following `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`.
