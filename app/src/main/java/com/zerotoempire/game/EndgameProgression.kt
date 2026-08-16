package com.zerotoempire.game

import kotlin.math.ln
import kotlin.math.max
import kotlin.math.pow

/**
 * Progression beyond the Galactic era. This layer deliberately uses logarithmic
 * growth so mature saves keep gaining power without making Double values explode.
 */
object EndgameProgression {
    private const val START = 1e18

    fun transcendenceLevel(lifetimeCash: Double): Int {
        if (!lifetimeCash.isFinite() || lifetimeCash < START) return 0
        val decades = ln(max(START, lifetimeCash) / START) / ln(10.0)
        return (decades / 3.0).toInt().coerceAtLeast(0)
    }

    fun transcendenceMultiplier(lifetimeCash: Double): Double {
        if (lifetimeCash < START || !lifetimeCash.isFinite()) return 1.0
        val decades = (ln(lifetimeCash / START) / ln(10.0)).coerceAtLeast(0.0)
        return 1.0 + 0.11 * decades.pow(0.82)
    }

    fun title(lifetimeCash: Double): String = when (transcendenceLevel(lifetimeCash)) {
        0 -> "GALACTIC"
        1 -> "INTERGALACTIC"
        2 -> "COSMIC"
        3 -> "REALITY ENGINE"
        else -> "TRANSCENDENT"
    }
}
