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

## Current 235-asset character completion lane (October 2026)

The unified orchestration design above is the desired long-term architecture.
The currently operational strict-completion lane uses these explicit, auditable
components while that migration is not complete:

- Canonical state: `art/production/master-asset-queue.json` and
  `docs/art/FINAL_AAA_SPRITE_MANIFEST.md` (235 assets excluding ONB-00).
- Producer queue: `art/production/controlled-character-regen-queue.json`
  with one IDLE identity anchor for each OP/LOG/ENG action family.
- GPU owner: `art/production/kaggle-async-state.json`; an `ACTIVE` wave
  must **not** be replaced by a code-only push or another producer request.
- Producer: `Kaggle Mass Sprite Factory`; preflight skips duplicate active
  waves. The controlled generator records either an image candidate or an
  explicit rejection for every requested action.
- Collector: `Kaggle Async Character Collector`, scheduled every five minutes.
  Its in-progress job is never cancelled by a newer check; it uploads
  `kaggle-async-character-batch` with candidate PNGs, action QA, generated
  target report, full-frame character review and enlarged face/headgear strips.
- Historical GPU collision: `Kaggle Superseded Character Evidence` stores
  separately recovered older runs; recovered evidence **never** grants
  automatic strict promotion or replaces the canonical active wave.
- Review provenance: the master/controlled queue stores
  `review_artifact_run_id`. Use the collector run, not an unrelated submit
  run, when resolving an exact candidate image. Explicitly approved IDLE
  replacements must come from the same role-family artifact.
- Promotion: `promote-approved-kaggle-characters.yml` accepts only declared
  manifest IDs with an exact reviewed artifact source; it performs runtime
  conversion/QA, Android character audit, debug build, existing tests, lint
  and release bundle validation **before** updating `strict_status`.
- Semantics: `image-only` alpha, palette, gait and motion metrics may reject,
  but cannot approve identity, actual carried objects, hand/tool contact,
  animation readability, costume continuity or premium visual quality.
  Review the full frames and enlarged head strips. Never claim 235/235 merely
  because 235 image files or 235 technically passing QA rows exist.

### October 12: evidence-driven animation gates

The LOG/ENG collector `38220177038` exposed several machine-passing but
semantically invalid animations, including a one-frame 175px body amid normal
218px frames, neutral celebrations with gold rays only at the end, and faces
redrawn into different people despite broadly similar uniform palettes.

The character-only, **rejection-side** tests now include:

- `FRAME_SCALE_COLLAPSE_RISK`: any action frame whose visible body height
  falls below 82% of the animation's median is blocked; prevents isolated
  shortened/fragmented bodies.
- `FACE_HEADGEAR_STRUCTURE_DRIFT_RISK`: normalized, aligned 68x68 head and
  helmet pixel texture must not change drastically from the first frame
  (threshold .19) on WALK/WORK/CARRY/REPAIR; supplements color histograms.
- `celebration_arm_reach_counts`: at least three frames of a CELEB loop
  must actually place visible arms above/outside the upper torso, rather than
  counting a final sparkle effect or changing face as a gesture.
- `idle_visual_activity`: IDLE may show subtle breathing or blinking with
  nearly identical alpha silhouettes, but cannot be a completely frozen
  sequence. This replaces the excessive .025 alpha-only motion minimum,
  which unnecessarily prevented an ENG batch.
- Existing frame-level technical, pose, appearance, connected components,
  sprite atlas and Android runtime checks remain mandatory.
- None of these image-only tests, even if all pass, constitutes visual
  semantic approval or changes `strict_status` automatically.

Each threshold has a regression using synthetic 256px sprites, while real
review examples and rejected asset IDs are documented in
`art/production/log-eng-fourth-wave-review.md`. The reason-to-retry hints
are retained in `art/production/generation-rejection-ledger.json`.

### Known defects from recovered OP/LOG wave

The superseded OP/LOG source `38170846318` was recovered as artifact
`38175207078`. Eight of twelve sheets were technical candidates, but
action-level review identified identity/prop drift and unreadable motion;
zero new actions were manually approved. The precise action-specific findings
are in `art/production/op-log-superseded-batch-semantic-review.md` and
`art/production/generation-rejection-ledger.json`. Later generation
epochs must use this evidence to avoid silently repeating defects.

The 235-item ledger is authoritative for progress. The latest live count
must always be recomputed from `strict_status == DONE` rather than copied
from documentation, summaries or producer-reported candidate counts.

### Sprite transparency and floor-shadow rejection (v1.19)

`tools/sprites/character_semantic_gate.py` inspects the visible-alpha
silhouette near the feet before an asset can enter manual review. A persistent
nearly solid horizontal band wider than the two legs is a **baked floor-shadow
risk**, not acceptable character transparency. The new signal is
`BAKED_GROUND_SHADOW_RISK`; the generated evidence includes
`baked_ground_band_suspected_frames` and
`max_ground_band_to_leg_width`.

This gate was calibrated against the recovered LOG wave in
[collector 38220177038](https://github.com/dbrckk/zero-to-empire/actions/runs/38220177038):
the floor-band signature appeared in all six IDLE frames and eight of eight
CELEB frames. The synthetic QA fixture confirms that separated boots without a
ground oval remain unflagged, while recurring ovals are blocked. A single
unusual wide stance is insufficient by itself to reject an entire atlas.

The review-only report from `build_character_review_panels.py` now runs the
latest image-risk checks on **historical candidates**, independent of the
version that generated their pixels. This is not an automatic approval: even
`risk_level=NOT_DETECTED` still requires same-person identity, continuous
hand/tool interaction, correct motion and Android runtime acceptance. These
checks apply to subsequent producer kernels, not an already running GPU job.
