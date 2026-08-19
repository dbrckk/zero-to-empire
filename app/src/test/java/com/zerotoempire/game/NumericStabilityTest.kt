package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class NumericStabilityTest {
    @Test
    fun extremeBusinessCostsRemainFinite() {
        val business = defaultBusinesses().last().copy(level = 100_000)
        assertTrue(business.nextCost.isFinite())
        assertEquals(EconomyMath.MAX_VALUE, business.nextCost, 0.0)
        assertTrue(BulkPurchase.cost(business, 25).isFinite())
    }

    @Test
    fun extremeStateIncomeAndTapRemainFinite() {
        val businesses = defaultBusinesses().map { it.copy(level = 1_000_000) }
        val state = GameState(
            cash = EconomyMath.MAX_VALUE,
            lifetimeCash = EconomyMath.MAX_VALUE,
            prestigePoints = Int.MAX_VALUE,
            businesses = businesses,
            hiredManagerIds = businesses.map { it.id }.toSet(),
            upgradeRanks = mapOf("tap" to 10, "income" to 20, "offline" to 8, "prestige" to 15)
        )

        assertTrue(state.incomePerSecond.isFinite())
        assertTrue(state.automatedIncomePerSecond.isFinite())
        assertTrue(state.tapValue.isFinite())
        assertTrue(state.incomePerSecond <= EconomyMath.MAX_VALUE)
    }

    @Test
    fun safeAddSaturatesInsteadOfOverflowing() {
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.safeAdd(EconomyMath.MAX_VALUE, 1e299), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.safeAdd(Double.POSITIVE_INFINITY, 1.0), 0.0)
    }

    @Test
    fun maxBulkQuoteNeverReturnsInfinity() {
        val business = defaultBusinesses().first().copy(level = 4_500)
        val quote = BulkPurchase.quote(business, EconomyMath.MAX_VALUE, BuyMode.MAX)
        assertTrue(quote.count >= 0)
        assertTrue(quote.totalCost.isFinite())
        assertTrue(quote.totalCost <= EconomyMath.MAX_VALUE)
    }
}
