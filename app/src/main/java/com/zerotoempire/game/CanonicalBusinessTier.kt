package com.zerotoempire.game

/**
 * Maps the eight gameplay progression milestones used by business evolution
 * (0, 10, 25, 50, 100, 250, 500, 1000) onto the seven canonical raster tiers
 * T0..T6.
 *
 * The final two gameplay milestones intentionally share T6. This preserves a
 * monotonic visual progression without inventing a non-canonical T7 asset.
 */
internal fun canonicalBusinessTier(level: Int): Int = when {
    level >= 500 -> 6
    level >= 250 -> 5
    level >= 100 -> 4
    level >= 50 -> 3
    level >= 25 -> 2
    level >= 10 -> 1
    else -> 0
}
