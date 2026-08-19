package com.zerotoempire.game

import kotlin.math.floor
import kotlin.math.ln

enum class BuyMode(val fixedCount: Int?) {
    X1(1), X10(10), X25(25), MILESTONE(null), MAX(null)
}

data class BulkQuote(val count: Int, val totalCost: Double) {
    val valid: Boolean get() = count > 0 && totalCost.isFinite() && totalCost >= 0.0
}

object BulkPurchase {
    private const val GROWTH = 1.15
    private const val MAX_SAFE_LEVELS = 1_000_000
    private val milestones = listOf(10, 25, 50, 100, 250, 500, 1000)

    fun cost(business: Business, count: Int): Double =
        EconomyMath.geometricCost(business.baseCost, business.level, count)

    fun affordableCount(business: Business, cash: Double): Int {
        val available = EconomyMath.finite(cash)
        val first = business.nextCost
        if (available < first) return 0
        if (first >= EconomyMath.MAX_VALUE) return 1

        val inside = 1.0 + available * (GROWTH - 1.0) / first
        if (!inside.isFinite()) return MAX_SAFE_LEVELS
        return floor(ln(inside) / ln(GROWTH)).toInt().coerceIn(1, MAX_SAFE_LEVELS)
    }

    fun levelsToNextMilestone(business: Business): Int {
        val next = milestones.firstOrNull { it > business.level }
            ?: if (business.level <= Int.MAX_VALUE - 1000) (((business.level / 1000) + 1) * 1000) else Int.MAX_VALUE
        return (next - business.level).coerceAtLeast(1)
    }

    fun quote(business: Business, cash: Double, mode: BuyMode): BulkQuote {
        val available = EconomyMath.finite(cash)
        val requested = when (mode) {
            BuyMode.MILESTONE -> levelsToNextMilestone(business)
            BuyMode.MAX -> affordableCount(business, available)
            else -> mode.fixedCount ?: 1
        }
        if (requested <= 0) return BulkQuote(0, 0.0)

        val total = cost(business, requested)
        if (total <= available * (1.0 + 1e-12)) return BulkQuote(requested, total)
        if (mode == BuyMode.MILESTONE) return BulkQuote(0, total)

        // Fixed modes are at most 25. MAX already uses affordableCount, so this loop stays bounded.
        var adjusted = requested.coerceAtMost(25)
        while (adjusted > 0 && cost(business, adjusted) > available) adjusted--
        return BulkQuote(adjusted, cost(business, adjusted))
    }

    fun crossedMilestones(fromLevel: Int, toLevel: Int): List<Int> =
        if (toLevel <= fromLevel) emptyList() else milestones.filter { it > fromLevel && it <= toLevel }
}
