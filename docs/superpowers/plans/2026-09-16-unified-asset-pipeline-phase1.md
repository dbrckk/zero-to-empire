# Unified Asset Pipeline Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first production-safe slice of the unified asset pipeline: authoritative manifest parsing, candidate metadata validation, reuse of the existing static image QA contract, provider isolation, QA artifacts, and one onboarding asset candidate that cannot promote itself to runtime.

**Architecture:** Keep `docs/art/FINAL_AAA_SPRITE_MANIFEST.md` authoritative and add small Python modules under `tools/assets/` around it. The pipeline accepts an explicit manifest ID, resolves only the documented runtime path, writes generated/imported files to an ID-scoped candidate directory, runs deterministic QA, emits review artifacts, and stops before runtime promotion. Existing Hugging Face image generation and static processing thresholds are reused rather than forked.

**Tech Stack:** Python 3.12 standard library, Pillow 11.3.0, existing Hugging Face/Cloudflare/Kaggle generation code, GitHub Actions, Android Gradle CI, Jetpack Compose runtime for later onboarding integration.

**Spec:** `docs/art/UNIFIED_ASSET_PIPELINE.md`

## Global Constraints

- `docs/art/FINAL_AAA_SPRITE_MANIFEST.md` remains the semantic source of truth.
- One manifest ID maps to one documented runtime role and one runtime path; mappings are never inferred from filenames, image content, generation order or visual similarity.
- Provider output never writes directly to `app/src/main/res` or `main`.
- Semantic review is a mandatory gate distinct from technical QA.
- Existing static isolation/normalization thresholds from `tools/sprites/hf_static_manifest_factory.py` must not change in this phase.
- Candidate generation must be explicit by manifest ID; no silent mass generation.
- No economy, progression, save, billing or unlock behavior changes.
- A candidate may not become `DONE` without runtime visibility and relevant green CI.

---

### Task 1: Authoritative manifest parser

**Files:**
- Create: `tools/assets/__init__.py`
- Create: `tools/assets/manifest.py`
- Create: `tools/assets/test_manifest.py`
- Read: `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`

**Interfaces:**
- Produces: `ManifestAsset(id: str, name: str, description: str, runtime_path: str, status: str)`
- Produces: `load_manifest(path: Path) -> dict[str, ManifestAsset]`
- Produces: `require_asset(assets: Mapping[str, ManifestAsset], asset_id: str) -> ManifestAsset`

- [ ] **Step 1: Write failing parser tests**

```python
from pathlib import Path
import tempfile
import unittest

from tools.assets.manifest import load_manifest, require_asset, ManifestError


class ManifestTest(unittest.TestCase):
    def write_manifest(self, text: str) -> Path:
        handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False)
        handle.write(text)
        handle.close()
        return Path(handle.name)

    def test_parses_exact_runtime_mapping(self):
        path = self.write_manifest(
            "| ID | Asset | Description | Runtime target | Status |\n"
            "|---|---|---|---|---|\n"
            "| ONB-00 | Onboarding step 0 | Power-core ignition illustration. | `app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp` | TODO |\n"
        )
        asset = load_manifest(path)["ONB-00"]
        self.assertEqual(asset.runtime_path, "app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp")
        self.assertEqual(asset.status, "TODO")

    def test_unknown_id_is_rejected(self):
        path = self.write_manifest(
            "| ID | Asset | Description | Runtime target | Status |\n"
            "|---|---|---|---|---|\n"
            "| ONB-00 | Onboarding step 0 | Core illustration. | `app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp` | TODO |\n"
        )
        with self.assertRaises(ManifestError):
            require_asset(load_manifest(path), "ONB-99")
```

- [ ] **Step 2: Run the tests and verify RED**

Run:

```bash
python -m unittest tools.assets.test_manifest -v
```

Expected: import failure because `tools.assets.manifest` does not exist.

- [ ] **Step 3: Implement the parser minimally**

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping
import re

ROW = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$"
)


class ManifestError(ValueError):
    pass


@dataclass(frozen=True)
class ManifestAsset:
    id: str
    name: str
    description: str
    runtime_path: str
    status: str


def load_manifest(path: Path) -> dict[str, ManifestAsset]:
    assets: dict[str, ManifestAsset] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ROW.match(line)
        if not match:
            continue
        asset_id, name, description, runtime_path, status = (part.strip() for part in match.groups())
        if asset_id.upper() == "ID" or set(asset_id) == {"-"}:
            continue
        normalized_id = asset_id.upper()
        if normalized_id in assets:
            raise ManifestError(f"duplicate manifest id: {normalized_id}")
        assets[normalized_id] = ManifestAsset(normalized_id, name, description, runtime_path, status.upper())
    if not assets:
        raise ManifestError(f"no manifest assets parsed from {path}")
    return assets


def require_asset(assets: Mapping[str, ManifestAsset], asset_id: str) -> ManifestAsset:
    key = asset_id.strip().upper()
    try:
        return assets[key]
    except KeyError as exc:
        raise ManifestError(f"manifest asset not found: {key}") from exc
```

- [ ] **Step 4: Run parser tests GREEN**

```bash
python -m unittest tools.assets.test_manifest -v
```

Expected: all parser tests pass.

- [ ] **Step 5: Add a real-manifest smoke assertion**

Add a test that loads `docs/art/FINAL_AAA_SPRITE_MANIFEST.md` and asserts `BLD-00-T0` resolves to the existing `zte_business_00_t0_final.webp` path. This proves the parser matches the repository's current table format.

- [ ] **Step 6: Commit**

```bash
git add tools/assets/__init__.py tools/assets/manifest.py tools/assets/test_manifest.py
git commit -m "test(art): add authoritative asset manifest parser"
```

---

### Task 2: Candidate metadata contract and anti-spoof validation

**Files:**
- Create: `tools/assets/metadata.py`
- Create: `tools/assets/test_metadata.py`

**Interfaces:**
- Consumes: `ManifestAsset`
- Produces: `CandidateMetadata`
- Produces: `CandidateMetadata.validate_against(asset: ManifestAsset) -> None`
- Produces: `sha256_file(path: Path) -> str`
- Produces: `write_metadata(path: Path, metadata: CandidateMetadata) -> None`

- [ ] **Step 1: Write tests proving mappings cannot be forged**

```python
import unittest
from tools.assets.manifest import ManifestAsset
from tools.assets.metadata import CandidateMetadata, MetadataError


ASSET = ManifestAsset(
    id="ONB-00",
    name="Onboarding step 0",
    description="Power-core ignition illustration.",
    runtime_path="app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp",
    status="TODO",
)


class MetadataTest(unittest.TestCase):
    def test_exact_manifest_mapping_is_accepted(self):
        meta = CandidateMetadata(
            manifest_id="ONB-00",
            semantic_role="Power-core ignition illustration.",
            runtime_path=ASSET.runtime_path,
            source_type="generated",
            provider="hf-static",
            source_url=None,
            license="generated",
            prompt_sha256="a" * 64,
            asset_sha256="b" * 64,
            review="pending",
        )
        meta.validate_against(ASSET)

    def test_runtime_path_spoof_is_rejected(self):
        meta = CandidateMetadata(
            manifest_id="ONB-00",
            semantic_role=ASSET.description,
            runtime_path="app/src/main/res/drawable-nodpi/zte_wrong.webp",
            source_type="generated",
            provider="hf-static",
            source_url=None,
            license="generated",
            prompt_sha256="a" * 64,
            asset_sha256="b" * 64,
            review="pending",
        )
        with self.assertRaises(MetadataError):
            meta.validate_against(ASSET)
```

Also add mismatched `manifest_id`, semantic role and invalid `review` tests.

- [ ] **Step 2: Run tests RED**

```bash
python -m unittest tools.assets.test_metadata -v
```

Expected: import failure for `tools.assets.metadata`.

- [ ] **Step 3: Implement immutable metadata**

Use `@dataclass(frozen=True)`. `validate_against()` must compare `manifest_id`, `semantic_role`, and `runtime_path` exactly with the manifest record. Allowed reviews are only `pending`, `accepted`, `rejected`; source types are only `generated`, `external`, `manual`.

- [ ] **Step 4: Implement deterministic SHA-256 helpers**

```python
def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
```

`write_metadata()` must use `json.dumps(..., indent=2, sort_keys=True)` and a trailing newline so diffs are stable.

- [ ] **Step 5: Run tests GREEN**

```bash
python -m unittest tools.assets.test_metadata -v
```

- [ ] **Step 6: Commit**

```bash
git add tools/assets/metadata.py tools/assets/test_metadata.py
git commit -m "test(art): lock candidate metadata to manifest mappings"
```

---

### Task 3: Extract the existing static processing contract without changing thresholds

**Files:**
- Create: `tools/assets/static_processing.py`
- Create: `tools/assets/test_static_processing.py`
- Modify: `tools/sprites/hf_static_manifest_factory.py`

**Interfaces:**
- Produces: `isolate(image: Image.Image) -> Image.Image`
- Produces: `normalize(master: Image.Image, side: int) -> Image.Image`
- Produces: `validate(image: Image.Image) -> tuple[float, float]`
- Produces: `components(alpha: Image.Image) -> tuple[int, float]`

- [ ] **Step 1: Write characterization tests before moving code**

Create a synthetic 256×256 RGB image with a black border and a centered bright 80×100 subject. Assert:

```python
isolated = isolate(source)
self.assertEqual(isolated.mode, "RGBA")
self.assertEqual(isolated.getpixel((0, 0))[3], 0)
self.assertGreater(isolated.getpixel((128, 128))[3], 200)

normalized = normalize(isolated, 1024)
self.assertEqual(normalized.size, (1024, 1024))
coverage, dominant = validate(normalized)
self.assertLess(coverage, 0.70)
self.assertGreaterEqual(dominant, 0.88)
```

Add a test proving `validate()` rejects an image touching the 4% safety edge.

- [ ] **Step 2: Run tests RED**

```bash
python -m unittest tools.assets.test_static_processing -v
```

Expected: module missing.

- [ ] **Step 3: Move the existing functions verbatim**

Move `_border_reference`, `isolate`, `components`, `normalize`, and `validate` from `tools/sprites/hf_static_manifest_factory.py` into `tools/assets/static_processing.py` with the exact existing constants:

- background hard distance: `28.0`
- background soft distance: `74.0`
- normalized max subject: `82%`
- bottom padding target: `8%`
- QA safety edge: `4%`
- dominant component minimum: `88%`
- alpha coverage maximum: `70%`

Do not tune these values in this task.

- [ ] **Step 4: Change the legacy factory to import the shared functions**

At the top of `hf_static_manifest_factory.py` import:

```python
from tools.assets.static_processing import isolate, normalize, validate
```

Delete only the duplicate moved function bodies and imports that become unused. Keep provider/network behavior unchanged.

- [ ] **Step 5: Run characterization tests plus syntax check**

```bash
python -m unittest tools.assets.test_static_processing -v
python -m py_compile tools/sprites/hf_static_manifest_factory.py tools/assets/static_processing.py
```

- [ ] **Step 6: Commit**

```bash
git add tools/assets/static_processing.py tools/assets/test_static_processing.py tools/sprites/hf_static_manifest_factory.py
git commit -m "refactor(art): share static sprite processing contract"
```

---

### Task 4: Provider adapter and explicit orchestrator CLI

**Files:**
- Create: `tools/assets/providers/__init__.py`
- Create: `tools/assets/providers/hf_static.py`
- Create: `tools/assets/asset_pipeline.py`
- Create: `tools/assets/test_asset_pipeline.py`

**Interfaces:**
- Produces: `ProviderResult(image: Image.Image, provider: str, source_url: str | None, license: str)`
- Produces: `HfStaticProvider.generate(asset: ManifestAsset, prompt: str) -> ProviderResult`
- Produces: `prepare_candidate(asset_id: str, provider, root: Path, manifest_path: Path) -> Path`
- Candidate directory contract: `art/incoming/assets/<MANIFEST_ID>/candidate.png` and `metadata.json`

- [ ] **Step 1: Write RED tests with a fake provider**

The fake provider returns a deterministic Pillow image and records the `ManifestAsset` it received. Tests must prove:

1. unknown IDs fail before the provider is called;
2. only the exact requested ID is generated;
3. output is written under `art/incoming/assets/<ID>/`;
4. metadata runtime path equals the manifest path;
5. the function never writes under `app/src/main/res`;
6. review is `pending`.

- [ ] **Step 2: Run tests RED**

```bash
python -m unittest tools.assets.test_asset_pipeline -v
```

- [ ] **Step 3: Implement provider abstraction around existing HF code**

`HfStaticProvider` may import generation/prompt helpers from `tools/sprites/hf_static_manifest_factory.py` in this phase. It must return raw provider output only; it must not know the runtime destination.

- [ ] **Step 4: Implement `prepare_candidate()`**

Flow:

```text
load manifest -> require explicit ID -> reject status DONE unless --force-candidate is supplied for QA-only regeneration -> build documented prompt -> provider.generate -> isolate -> normalize -> validate -> write candidate.png -> write metadata.json -> return candidate directory
```

The default path must never copy into `drawable-nodpi`.

- [ ] **Step 5: Add CLI**

Supported commands in Phase 1:

```bash
python tools/assets/asset_pipeline.py inspect --id ONB-00
python tools/assets/asset_pipeline.py prepare --id ONB-00 --provider hf-static
python tools/assets/asset_pipeline.py validate --id ONB-00
```

`inspect` is network-free. `prepare` requires provider credentials. `validate` validates existing candidate metadata/image only.

- [ ] **Step 6: Run tests GREEN**

```bash
python -m unittest tools.assets.test_asset_pipeline -v
python -m py_compile tools/assets/asset_pipeline.py tools/assets/providers/hf_static.py
```

- [ ] **Step 7: Commit**

```bash
git add tools/assets/providers tools/assets/asset_pipeline.py tools/assets/test_asset_pipeline.py
git commit -m "feat(art): add explicit gated asset orchestrator"
```

---

### Task 5: Machine-readable QA report and contact sheet artifact

**Files:**
- Create: `tools/assets/qa_report.py`
- Create: `tools/assets/test_qa_report.py`
- Reuse: `tools/sprites/build_sprite_contact_sheet.py`

**Interfaces:**
- Produces: `build_report(asset: ManifestAsset, candidate_dir: Path) -> dict`
- Produces: `write_report(candidate_dir: Path, report: Mapping) -> Path`
- Output: `art/incoming/assets/<ID>/qa-report.json`

- [ ] **Step 1: Write report tests**

The report must include at least:

```json
{
  "manifest_id": "ONB-00",
  "runtime_path": "...",
  "technical_status": "pass",
  "semantic_review": "pending",
  "asset_sha256": "...",
  "metrics": {
    "alpha_coverage": 0.0,
    "dominant_component": 0.0
  }
}
```

Test that a `pending` semantic review can never produce an overall `approved` field set to true.

- [ ] **Step 2: Run RED**

```bash
python -m unittest tools.assets.test_qa_report -v
```

- [ ] **Step 3: Implement deterministic report writing**

Use sorted JSON and record the exact manifest/runtime mapping plus technical metrics returned by the shared static validator.

- [ ] **Step 4: Invoke the existing contact sheet tool as a presentation artifact only**

Do not treat contact-sheet success as semantic acceptance. The orchestrator should expose a command that can run:

```bash
python tools/sprites/build_sprite_contact_sheet.py \
  --input art/incoming/assets/ONB-00 \
  --output art/incoming/assets/ONB-00/contact-sheet.png \
  --report art/incoming/assets/ONB-00/contact-sheet-report.json
```

If the legacy contact-sheet script requires multiple images, adapt only its input discovery so one candidate is legal; do not change semantic status automatically.

- [ ] **Step 5: Run tests GREEN**

```bash
python -m unittest tools.assets.test_qa_report -v
```

- [ ] **Step 6: Commit**

```bash
git add tools/assets/qa_report.py tools/assets/test_qa_report.py tools/assets/asset_pipeline.py tools/sprites/build_sprite_contact_sheet.py
git commit -m "feat(art): emit review-only asset QA artifacts"
```

---

### Task 6: Register the first onboarding authored-art target without changing runtime yet

**Files:**
- Modify: `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`
- Modify: `tools/assets/test_manifest.py`
- Read: `app/src/main/java/com/zerotoempire/game/OnboardingArt.kt`

**Interfaces:**
- Produces manifest ID: `ONB-00`
- Runtime target: `app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp`

- [ ] **Step 1: Add a failing real-manifest test for `ONB-00`**

```python
def test_real_manifest_defines_first_onboarding_authored_target(self):
    assets = load_manifest(Path("docs/art/FINAL_AAA_SPRITE_MANIFEST.md"))
    asset = require_asset(assets, "ONB-00")
    self.assertEqual(asset.runtime_path, "app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp")
    self.assertEqual(asset.status, "TODO")
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tools.assets.test_manifest.ManifestTest.test_real_manifest_defines_first_onboarding_authored_target -v
```

Expected: `manifest asset not found: ONB-00`.

- [ ] **Step 3: Add an onboarding section to the authoritative manifest**

Add only the first target in this phase:

```markdown
## I. Onboarding authored illustrations

| ID | Asset | Description | Runtime target | Status |
|---|---|---|---|---|
| ONB-00 | Onboarding step 0 primary illustration | Authored replacement for the current step-0 radial Power Core/ignition visual in `OnboardingStepArt`; isolated scene art with no baked UI text. | `app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp` | TODO |
```

This description is grounded in the existing step-0 Canvas implementation in `OnboardingArt.kt`; it does not invent a new gameplay meaning.

- [ ] **Step 4: Run parser tests GREEN**

```bash
python -m unittest tools.assets.test_manifest -v
```

- [ ] **Step 5: Commit**

```bash
git add docs/art/FINAL_AAA_SPRITE_MANIFEST.md tools/assets/test_manifest.py
git commit -m "docs(art): register first authored onboarding target"
```

---

### Task 7: Add a read-only GitHub Actions candidate workflow

**Files:**
- Create: `.github/workflows/unified-asset-pipeline.yml`
- Create: `tools/assets/test_workflow_policy.py`

**Interfaces:**
- Workflow input: `asset_id` (required string)
- Workflow input: `provider` (choice, initial value `hf-static`)
- Artifact output: candidate PNG, `metadata.json`, `qa-report.json`, contact sheet
- No commit/push/main mutation in Phase 1

- [ ] **Step 1: Write policy tests against workflow text**

The test reads `.github/workflows/unified-asset-pipeline.yml` and asserts:

- `permissions: contents: read`
- workflow uses `workflow_dispatch`
- workflow requires `asset_id`
- no `git push`
- no `contents: write`
- no `pull_request_target`

- [ ] **Step 2: Run RED**

```bash
python -m unittest tools.assets.test_workflow_policy -v
```

- [ ] **Step 3: Implement the workflow**

Workflow sequence:

```text
checkout -> Python 3.12 -> Pillow 11.3.0 -> unit tests -> inspect manifest ID -> prepare candidate -> validate candidate -> build QA report/contact sheet -> upload artifacts
```

Provider secrets must be read only by the generation step. A quota/provider failure may exit with the existing availability code and must not alter manifest status.

- [ ] **Step 4: Run all Python tests locally**

```bash
python -m unittest discover -s tools/assets -p 'test_*.py' -v
```

- [ ] **Step 5: Run Android regression checks because no runtime code should have changed**

```bash
gradle --no-daemon testDebugUnitTest lintDebug assembleDebug
```

Expected: all existing Android unit tests, lint and debug build remain green.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/unified-asset-pipeline.yml tools/assets/test_workflow_policy.py
git commit -m "ci(art): add read-only unified asset candidate workflow"
```

---

### Task 8: Produce and review the first candidate, but do not integrate it automatically

**Files:**
- Generated artifact only: `art/incoming/assets/ONB-00/*`
- No runtime file in this task
- No change to `OnboardingArt.kt` in this task

**Interfaces:**
- Consumes manifest ID `ONB-00`
- Produces review artifact bundle only

- [ ] **Step 1: Run the workflow or local provider for `ONB-00`**

```bash
python tools/assets/asset_pipeline.py prepare --id ONB-00 --provider hf-static
python tools/assets/asset_pipeline.py validate --id ONB-00
```

- [ ] **Step 2: Verify the candidate directory contains exactly the expected review files**

```text
art/incoming/assets/ONB-00/candidate.png
art/incoming/assets/ONB-00/metadata.json
art/incoming/assets/ONB-00/qa-report.json
art/incoming/assets/ONB-00/contact-sheet.png
```

- [ ] **Step 3: Verify metadata mapping manually against the manifest**

Required exact values:

```text
manifest_id = ONB-00
runtime_path = app/src/main/res/drawable-nodpi/zte_onboarding_00_final.webp
review = pending
```

- [ ] **Step 4: Review visual quality before any runtime promotion**

Reject the candidate if it contains any of these:

- baked text/UI labels;
- collage or multiple unrelated panels;
- watermarks/logos;
- clipped subject;
- background rectangle when transparency is expected;
- style/camera mismatch with current authored game assets.

If rejected, keep `review: rejected` and generate another candidate. Do not change the runtime mapping.

- [ ] **Step 5: Stop at semantic-review gate**

Phase 1 is complete when the pipeline can produce a technically valid `ONB-00` review bundle without touching `drawable-nodpi`, `OnboardingArt.kt`, economy, progression or `main` directly.

- [ ] **Step 6: Open a dedicated implementation PR and require CI**

PR summary must list:

- manifest/parser/schema tests;
- anti-spoof mapping tests;
- static processing characterization tests;
- workflow policy tests;
- candidate QA artifact link;
- Android unit/lint/debug results.

Do not merge until all relevant checks are green.

---

## Plan self-review

- **Spec coverage:** manifest authority, exact mapping, metadata provenance, semantic-review gate, shared static QA, explicit provider selection, candidate-only output, QA artifacts, read-only CI and one first onboarding candidate are covered.
- **Deferred intentionally:** automatic PR creation/promotion, external-pack importer, Qwen adapter, character rig/animation and runtime onboarding replacement are separate follow-up plans after this slice proves the gate architecture.
- **Placeholder scan:** no TBD/TODO implementation placeholders remain in this plan; every task has concrete files, commands and acceptance behavior.
- **Type consistency:** `ManifestAsset`, `CandidateMetadata`, `ProviderResult` and candidate path conventions are used consistently across tasks.
