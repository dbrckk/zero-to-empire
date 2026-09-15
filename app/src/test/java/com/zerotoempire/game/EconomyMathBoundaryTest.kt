package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class EconomyMathBoundaryTest {
    @Test
    fun finiteNormalizesInvalidAndExtremeValues() {
        assertEquals(0.0, EconomyMath.finite(Double.NaN), 0.0)
        assertEquals(0.0, EconomyMath.finite(Double.NEGATIVE_INFINITY), 0.0)
        assertEquals(0.0, EconomyMath.finite(-1.0), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.finite(Double.POSITIVE_INFINITY), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.finite(Double.MAX_VALUE), 0.0)
    }

    @Test
    fun safeAddSaturatesInsteadOfOverflowing() {
        assertEquals(
            EconomyMath.MAX_VALUE,
            EconomyMath.safeAdd(EconomyMath.MAX_VALUE, EconomyMath.MAX_VALUE),
            0.0
        )
        assertEquals(
            EconomyMath.MAX_VALUE,
            EconomyMath.safeAdd(EconomyMath.MAX_VALUE * .9, EconomyMath.MAX_VALUE * .2),
            0.0
        )
    }

    @Test
    fun growthCostStaysFiniteAtExtremeLevels() {
        val cost = EconomyMath.growthCost(10.0, Int.MAX_VALUE)
        assertTrue(cost.isFinite())
        assertEquals(EconomyMath.MAX_VALUE, cost, 0.0)
    }

    @Test
    fun geometricCostStaysFiniteForHugePurchases() {
        val cost = EconomyMath.geometricCost(10.0, 0, Int.MAX_VALUE)
        assertTrue(cost.isFinite())
        assertEquals(EconomyMath.MAX_VALUE, cost, 0.0)
    }

    @Test
    fun bulkQuoteWithExtremeCashRemainsBoundedAndAffordable() {
        val business = defaultBusinesses().first()
        val quote = BulkPurchase.quote(business, EconomyMath.MAX_VALUE, BuyMode.MAX)

        assertTrue(quote.count in 1..1_000_000)
        assertTrue(quote.totalCost.isFinite())
        assertTrue(quote.totalCost <= EconomyMath.MAX_VALUE)
    }

    @Test
    fun milestoneDistanceDoesNotOverflowNearIntMax() {
        val business = defaultBusinesses().first().copy(level = Int.MAX_VALUE - 1)
        val distance = BulkPurchase.levelsToNextMilestone(business)

        assertEquals(1, distance)
    }
}
