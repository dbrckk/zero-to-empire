package com.zerotoempire.game

import kotlin.math.ln
import kotlin.math.max
import kotlin.math.pow
import kotlin.math.sqrt

/** Long-horizon progression helpers. Pure functions keep balancing testable. */
object LateGame {
    /** Softly accelerates mature empires without creating an unbounded exponential runaway. */
    fun legacyMasteryMultiplier(prestigePoints: Int): Double {
        val p = prestigePoints.coerceAtLeast(0).toDouble()
        return 1.0 + 0.08 * sqrt(p) + 0.015 * ln(1.0 + p).pow(2.0)
    }

    /** Additional production from reaching deep business tiers. */
    fun portfolioDepthMultiplier(businesses: List<Business>): Double {
        val tierScore = businesses.sumOf { b ->
            when {
                b.level >= 1000 -> 5
                b.level >= 500 -> 4
                b.level >= 250 -> 3
                b.level >= 100 -> 2
                b.level >= 50 -> 1
                else -> 0
            }
        }
        return 1.0 + tierScore * 0.035
    }

    /** A recommended prestige becomes attractive at ~25%+ permanent improvement. */
    fun prestigeReadiness(currentPoints: Int, lifetimeCash: Double): Double {
        val total = Progression.prestigeReward(lifetimeCash)
        val gain = (total - currentPoints).coerceAtLeast(0)
        if (gain == 0) return 0.0
        return (gain.toDouble() / max(1, currentPoints).toDouble()).coerceAtMost(4.0)
    }

    fun recommendedPrestige(currentPoints: Int, lifetimeCash: Double): Boolean =
        prestigeReadiness(currentPoints, lifetimeCash) >= 0.25 ||
            (currentPoints == 0 && Progression.prestigeReward(lifetimeCash) >= 1)
}
