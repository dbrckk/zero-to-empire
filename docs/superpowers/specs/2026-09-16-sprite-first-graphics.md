# Sprite-first Graphics Design

## Goal

Move Zero to Empire to a sprite-first rendering model: authored WebP assets are the primary visuals for gameplay entities, while Compose Canvas is reserved for overlays and VFX.

## Agreed direction

Option A: Sprite-first + procedural VFX.

- Buildings, managers, machines, vehicles, currency/meta icons and other representative gameplay art should resolve to authored runtime assets when production assets exist.
- Canvas remains valid for glow, aura, trails, particles, scanlines, impact flashes, motion accents and mastery overlays.
- Production should not silently fall back to a procedural primary renderer for an entity that has a complete validated authored sprite set.
- Reduced-motion and low-power modes keep the authored sprite visible and only reduce or disable VFX.
- Existing economy, saves, billing, unlocks and progression behavior must not change.

## Migration strategy

Ship the migration in independently testable slices:

1. Business sprites: wire complete canonical T0-T6 sets into runtime resolution, starting with Group 01.
2. Manager portraits: replace Canvas primary portraits where authored portraits exist.
3. Meta/navigation icons: use authored icon assets; keep lightweight animated accents optional.
4. Machines, vehicles and world props: resolve reviewed production sprites through a single registry.
5. Onboarding/store/upgrades/goals and secondary UI art.

Each slice must add coverage before implementation and must preserve procedural rendering only as a fallback for asset families that are genuinely incomplete.
