package com.zerotoempire.game

import kotlin.math.floor
import kotlin.math.ln
import kotlin.math.pow

enum class BuyMode(val fixedCount: Int?) {
    X1(1), X10(10), X25(25), MAX(null)
}

data class BulkQuote(val count: Int, val totalCost: Double) {
    val valid: Boolean get() = count > 0 && totalCost.isFinite() && totalCost >= 0.0
}

object BulkPurchase {
    private const val GROWTH = 1.15
    private const val MAX_SAFE_LEVELS = 1_000_000

    fun cost(business: Business, count: Int): Double {
        if (count <= 0) return 0.0
        val first = business.baseCost * GROWTH.pow(business.level)
        return first * (GROWTH.pow(count) - 1.0) / (GROWTH - 1.0)
    }

    fun affordableCount(business: Business, cash: Double): Int {
        if (!cash.isFinite() || cash < business.nextCost) return 0
        val first = business.baseCost * GROWTH.pow(business.level)
        val inside = 1.0 + cash * (GROWTH - 1.0) / first
        if (!inside.isFinite()) return MAX_SAFE_LEVELS
        return floor(ln(inside) / ln(GROWTH)).toInt().coerceIn(0, MAX_SAFE_LEVELS)
    }

    fun quote(business: Business, cash: Double, mode: BuyMode): BulkQuote {
        val count = mode.fixedCount ?: affordableCount(business, cash)
        if (count <= 0) return BulkQuote(0, 0.0)
        val total = cost(business, count)
        return if (total <= cash * (1.0 + 1e-12)) BulkQuote(count, total) else {
            var adjusted = count
            while (adjusted > 0 && cost(business, adjusted) > cash) adjusted--
            BulkQuote(adjusted, cost(business, adjusted))
        }
    }

    fun crossedMilestones(fromLevel: Int, toLevel: Int): List<Int> =
        listOf(10, 25, 50, 100, 250, 500, 1000).filter { it in (fromLevel + 1)..toLevel }
}
