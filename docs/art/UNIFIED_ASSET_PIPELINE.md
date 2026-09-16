# Unified AAA Asset Production Pipeline

## Goal

Replace provider-specific promotion paths with one auditable production contract. Generated or externally sourced art is always a candidate until semantic, technical, visual, runtime and CI gates have passed.

## Non-negotiable rules

1. `docs/art/FINAL_AAA_SPRITE_MANIFEST.md` remains the semantic source of truth.
2. One manifest ID maps to one documented runtime role and one runtime path. The pipeline never guesses mappings from filenames, image content, generation order or visual similarity.
3. Authored sprites are primary visuals. Canvas/procedural drawing is reserved for overlays, VFX and explicit fallbacks.
4. Provider output never writes directly to `app/src/main/res` or `main`.
5. A candidate cannot become `DONE` merely because generation succeeded. `DONE` retains the manifest's existing definition: cleaned, integrated, visible and CI-green.
6. External assets require recorded source and license metadata before promotion.

## Production states

`TODO -> CANDIDATE -> CLEAN -> REVIEWED -> RUNTIME -> DONE`

- `TODO`: required by the authoritative manifest.
- `CANDIDATE`: raw provider/external output exists under `art/incoming/`.
- `CLEAN`: deterministic alpha, padding, dimensions and isolation QA passed.
- `REVIEWED`: semantic identity and visual quality were explicitly accepted for the manifest ID.
- `RUNTIME`: converted to the documented Android path and referenced by runtime code.
- `DONE`: relevant unit/build/emulator checks are green and the asset is visible in the intended screen/world context.

No automated stage may infer `REVIEWED` from technical image metrics.

## Provider strategy

The orchestrator selects providers by capability, not by runtime mapping.

### Static authored art

Preferred generation lane:

1. FLUX.1-schnell-compatible provider.
2. Qwen-Image-compatible provider when configured.
3. Existing Hugging Face / Cloudflare / Kaggle lanes as availability fallbacks.

Provider failure or quota exhaustion changes only candidate generation. It never changes the manifest identity or target path.

### External reusable art

CC0/permissive packs such as Kenney may supply generic UI or props only when an explicit manifest record documents the source asset, license and semantic role. Imported filenames are not treated as semantic evidence.

### Character animation

Character masters and action semantics are separate contracts. A rig/animation tool may produce frames only for an already documented character role/action. The reviewed frame counts in `CanonicalCharacterRaster.kt` are authoritative for actions currently documented by runtime.

## Canonical orchestration

A future `tools/assets/asset_pipeline.py` is the only entry point allowed to coordinate production:

1. Parse the authoritative manifest.
2. Select explicit requested IDs; never silently generate all unknown work.
3. Resolve a configured provider.
4. Store raw output in an ID-scoped candidate directory.
5. Run deterministic background isolation/normalization.
6. Run technical QA: alpha, safety padding, dimensions, dominant component, corruption and Android-safe naming.
7. Generate a contact sheet and machine-readable QA report.
8. Require semantic review before promotion.
9. Convert accepted art to the exact manifest runtime path.
10. Run tests/build checks appropriate to the changed category.
11. Open/update a branch and PR; do not push production candidates directly to `main`.
12. Mark `DONE` only after relevant CI is green and runtime visibility is proven.

Existing isolation and normalization logic in `tools/sprites/hf_static_manifest_factory.py` should be extracted/reused rather than reimplemented with divergent thresholds.

## Candidate metadata

Each candidate must have machine-readable metadata adjacent to the image:

```json
{
  "manifest_id": "PRP-00",
  "semantic_role": "value copied from authoritative manifest",
  "runtime_path": "exact path copied from authoritative manifest",
  "source_type": "generated|external",
  "provider": "provider/model or pack name",
  "source_url": "optional source URL",
  "license": "SPDX identifier or documented license name",
  "prompt_sha256": "for generated art",
  "asset_sha256": "content hash",
  "review": "pending|accepted|rejected"
}
```

The orchestrator must reject metadata whose `manifest_id`, semantic role or runtime path disagrees with the authoritative manifest.

## Static asset QA

Promotion requires all applicable checks:

- decodable PNG/WebP;
- transparency where required;
- transparent safety padding;
- subject coverage inside category bounds;
- dominant connected component for isolated sprites;
- no baked UI rectangle for world sprites;
- exact Android-safe runtime name;
- output dimensions within the manifest/category contract;
- content hash recorded;
- semantic review accepted.

Technical QA can reject automatically. It cannot accept semantics automatically.

## Animation QA

Animation/sheet promotion additionally requires:

- documented role and action;
- documented frame count;
- stable frame dimensions and padding;
- stable pivot/feet/contact anchor within tolerance;
- no accidental background rectangles;
- no duplicate/corrupt frames;
- reduced-motion path able to freeze decorative loops;
- runtime animation test where practical.

Rigging output is a build artifact, not semantic evidence.

## CI / PR gate

The unified workflow must use least privilege. Candidate generation and QA need `contents: read`. A dedicated promotion job may create/update an asset branch/PR after review. Direct bot pushes to `main` from legacy sprite workflows should be removed or converted to manual fallbacks once the unified pipeline is proven.

Relevant checks include, depending on the batch:

- deterministic Python QA tests;
- Android unit tests;
- Android build;
- emulator smoke for onboarding/runtime navigation changes;
- generated contact sheet/report uploaded as CI artifacts.

A failed or unavailable provider is not an asset failure. A failed QA/build/runtime check is.

## First migration slice

Do not attempt all 235 assets at once. The first implementation slice is deliberately small and testable:

1. add the manifest parser/validator and candidate metadata schema;
2. add tests proving unknown IDs and mismatched runtime paths are rejected;
3. wrap the existing static factory behind the orchestrator without changing its image thresholds;
4. produce QA artifacts but never promote automatically;
5. migrate one documented TODO static asset end-to-end on a PR;
6. only then migrate animation and external-pack import lanes.

This sequence prevents another unreviewed collage/sheet from being treated as production art and keeps provider automation independent from semantic mapping.