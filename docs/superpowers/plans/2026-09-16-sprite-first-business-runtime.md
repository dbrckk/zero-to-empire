# Sprite-first Business Runtime Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make authored business WebP sprites the primary runtime art for Group 01 businesses that already have complete T0-T6 production sets.

**Architecture:** Keep `canonicalBusinessTier(level)` as the single tier mapping. Extend `canonicalBusinessRasterRes(businessId, level)` so complete Group 01 sprite families resolve directly to Android drawables. Update the business visual composable to render the resolved raster first and retain procedural Canvas only when no canonical runtime asset exists; procedural mastery/VFX may remain layered above the raster.

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

**Interfaces:**
- Consumes: `canonicalBusinessTier(level: Int): Int`
- Produces: `canonicalBusinessRasterRes(businessId: Int, level: Int): Int?` resolving business IDs 0, 1, 2 and 3 for all T0-T6 tiers.

- [ ] **Step 1: Write the failing test**

Change the resolver coverage tests so IDs 0, 1, 2 and 3 must resolve every gameplay milestone, each must expose seven distinct tier resources, 500 and 1000 must share T6, and only IDs outside the complete Group 01 set remain unsupported.

- [ ] **Step 2: Run test to verify it fails**

Run through Android CI: `gradle --no-daemon testDebugUnitTest`.
Expected: `CanonicalBusinessRasterTest` fails because IDs 0 and 1 still return null.

- [ ] **Step 3: Write minimal implementation**

Add explicit T0-T6 `R.drawable.zte_business_00_*_final` and `R.drawable.zte_business_01_*_final` mappings to `canonicalBusinessRasterRes` without changing tier thresholds.

- [ ] **Step 4: Run test to verify it passes**

Run through Android CI: `gradle --no-daemon testDebugUnitTest`.
Expected: all canonical raster tests pass.

- [ ] **Step 5: Commit**

Commit message: `feat(art): wire complete group01 business sprites`

### Task 2: Prefer canonical raster art in the business composable

**Files:**
- Modify: the runtime business visual composable that currently chooses procedural business art.
- Test: add or extend a pure resolver/policy test if selection logic needs extraction.

**Interfaces:**
- Consumes: `canonicalBusinessRasterRes(businessId, level)`.
- Produces: a stable sprite-first selection path where canonical raster is primary and procedural business art is fallback-only.

- [ ] **Step 1: Write the failing test**

Extract a pure selection policy only if needed and assert that businesses 0-3 select canonical raster while an unsupported business selects procedural fallback.

- [ ] **Step 2: Run test to verify it fails**

Run `gradle --no-daemon testDebugUnitTest` in Android CI.
Expected: the new policy test fails before production wiring exists.

- [ ] **Step 3: Write minimal implementation**

Render the canonical drawable with Compose `Image`/`painterResource` as the primary content. Keep existing procedural renderer only for `null` canonical resources. Preserve mastery/VFX layers separately.

- [ ] **Step 4: Run test to verify it passes**

Run unit tests plus debug build/lint through Android CI.
Expected: green.

- [ ] **Step 5: Commit**

Commit message: `feat(art): prefer canonical business raster at runtime`

### Task 3: Verify release safety and runtime smoke

**Files:**
- No production changes unless verification exposes a regression.

**Interfaces:**
- Consumes: final branch head.
- Produces: evidence that the sprite-first migration compiles, preserves release manifest policy, and does not break functional smoke.

- [ ] **Step 1: Run Android CI**

Expected: debug build, unit tests, lint, release AAB and merged release-manifest audit all pass.

- [ ] **Step 2: Run Android Emulator Smoke**

Expected: onboarding, power-core tap, Street Stand purchase, manager automation, offline earnings and restart persistence remain green.

- [ ] **Step 3: Review PR diff**

Confirm no economy/save/billing behavior changed and no binary asset replacement was introduced in this slice.

- [ ] **Step 4: Merge only after fresh green evidence**

Use squash merge after exact-head CI verification.
