# Sprite-first Business Runtime Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make authored business WebP sprites the primary runtime art for Group 01 businesses that already have complete T0-T6 production sets.

**Architecture:** Keep `canonicalBusinessTier(level)` as the tier contract and `canonicalBusinessRasterRes(businessId, level)` as the single resource resolver. `WorldBusinessVisual` already renders resolved raster assets first and uses procedural art only when resolution returns null; this slice removes the duplicate inline 0/1 map and extends the canonical resolver so the complete Group 01 family (IDs 0-3) follows one tested sprite-first path. Mastery/motion VFX remain layered separately.

**Tech Stack:** Kotlin, Jetpack Compose, Android resources, JUnit4, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-16-sprite-first-graphics.md`

## Global Constraints

- Do not change economy, saves, purchases, unlocks, billing or progression behavior.
- Authored WebP art is primary whenever a complete validated sprite family exists.
- Canvas remains permitted for VFX/mastery overlays and genuine missing-asset fallback paths.
- Reduced-motion and low-power modes must not hide the primary sprite.
- T0-T6 mapping must stay aligned with `canonicalBusinessTier(level)`.

---

### Task 1: Expand canonical Group 01 raster coverage

**Files:**
- Modify: `app/src/test/java/com/zerotoempire/game/CanonicalBusinessRasterTest.kt`
- Modify: `app/src/main/java/com/zerotoempire/game/CanonicalBusinessRaster.kt`

- [x] **Step 1: Write the failing test** — require IDs 0-3 at all gameplay milestones and seven distinct T0-T6 resources.
- [x] **Step 2: Verify RED** — Android CI #709 built successfully, then failed only the two expected `CanonicalBusinessRasterTest` assertions.
- [x] **Step 3: Write minimal implementation** — add explicit ID 0/1 T0-T6 mappings to the existing canonical 2/3 mappings.
- [ ] **Step 4: Verify GREEN** — exact-head Android CI pending.

### Task 2: Centralize sprite-first runtime selection

**Files:**
- Modify: `app/src/main/java/com/zerotoempire/game/WorldBusinessVisual.kt`

**Observed baseline:** `WorldBusinessVisual` was already raster-first for IDs 0/1 through a duplicate local mapping and for IDs 2/3 through `canonicalBusinessRasterRes`.

- [x] **Step 1: Preserve the existing raster-first behavior** — no visual/economy behavior change required.
- [x] **Step 2: Remove split-brain mapping** — delete the inline ID 0/1 resource switch and resolve all complete Group 01 sprites through `canonicalBusinessRasterRes`.
- [x] **Step 3: Preserve fallback/VFX semantics** — unsupported business families still use `BusinessArtIcon`; mastery and motion effects remain layered over authored sprites.
- [ ] **Step 4: Verify compile/tests/lint** — exact-head Android CI pending.

### Task 3: Verify release safety and runtime smoke

- [ ] **Step 1: Android CI** — debug build, unit tests, lint, release AAB and merged release-manifest audit must pass.
- [ ] **Step 2: Runtime smoke** — validate onboarding, Power Core, Street Stand, manager automation, offline earnings and restart persistence on the merged main head if the smoke workflow is main-only.
- [x] **Step 3: Review PR scope** — changed files are limited to two art-runtime files, one art test and two design/plan docs; no economy/save/billing files changed.
- [ ] **Step 4: Merge only after fresh green evidence** — squash merge after exact-head verification.
