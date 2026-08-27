package com.zerotoempire.game

import kotlin.math.exp
import kotlin.math.ln

/** Numerical guardrails for extremely mature saves. */
object EconomyMath {
    const val MAX_VALUE: Double = 1e300
    private const val COST_GROWTH = 1.15
    private val lnGrowth = ln(COST_GROWTH)
    private val lnMax = ln(MAX_VALUE)

    fun finite(value: Double): Double = when {
        value.isNaN() || value <= 0.0 -> 0.0
        value.isInfinite() || value > MAX_VALUE -> MAX_VALUE
        else -> value
    }

    fun safeAdd(a: Double, b: Double): Double {
        val left = finite(a)
        val right = finite(b)
        if (left >= MAX_VALUE - right) return MAX_VALUE
        return left + right
    }

    fun growthCost(baseCost: Double, level: Int): Double {
        if (baseCost <= 0.0 || !baseCost.isFinite()) return MAX_VALUE
        val safeLevel = level.coerceAtLeast(0)
        if (safeLevel == 0) return baseCost.coerceAtMost(MAX_VALUE)
        val exponent = ln(baseCost) + safeLevel * lnGrowth
        if (!exponent.isFinite() || exponent >= lnMax) return MAX_VALUE
        return exp(exponent).coerceAtMost(MAX_VALUE)
    }

    fun geometricCost(baseCost: Double, startLevel: Int, count: Int): Double {
        if (count <= 0) return 0.0
        val first = growthCost(baseCost, startLevel)
        if (first >= MAX_VALUE) return MAX_VALUE
        if (count == 1) return first
        val growthExponent = count.toDouble() * lnGrowth
        if (!growthExponent.isFinite() || growthExponent >= lnMax) return MAX_VALUE
        val factor = exp(growthExponent)
        if (!factor.isFinite()) return MAX_VALUE
        val total = first * (factor - 1.0) / (COST_GROWTH - 1.0)
        return finite(total)
    }
}
