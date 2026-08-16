package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class LateGameTest {
    @Test fun legacyMasteryIsMonotonic() {
        assertEquals(1.0, LateGame.legacyMasteryMultiplier(0), 1e-9)
        assertTrue(LateGame.legacyMasteryMultiplier(100) > LateGame.legacyMasteryMultiplier(10))
    }

    @Test fun portfolioDepthRewardsDeepBusinesses() {
        val base = defaultBusinesses()
        val deep = base.mapIndexed { i, b -> if (i < 3) b.copy(level = 500) else b }
        assertTrue(LateGame.portfolioDepthMultiplier(deep) > LateGame.portfolioDepthMultiplier(base))
    }

    @Test fun prestigeRecommendationRequiresMeaningfulGain() {
        assertFalse(LateGame.recommendedPrestige(100, 1_000_000.0))
        assertTrue(LateGame.recommendedPrestige(0, 1_000_000.0))
    }

    @Test fun milestoneModeTargetsExactNextMilestone() {
        val b = defaultBusinesses().first().copy(level = 7)
        assertEquals(3, BulkPurchase.levelsToNextMilestone(b))
        val cost = BulkPurchase.cost(b, 3)
        val quote = BulkPurchase.quote(b, cost, BuyMode.MILESTONE)
        assertEquals(3, quote.count)
        assertEquals(cost, quote.totalCost, 1e-6)
    }

    @Test fun milestoneModeDoesNotPartiallyBuyWhenUnaffordable() {
        val b = defaultBusinesses().first().copy(level = 7)
        val full = BulkPurchase.cost(b, 3)
        val quote = BulkPurchase.quote(b, full * .9, BuyMode.MILESTONE)
        assertEquals(0, quote.count)
        assertEquals(full, quote.totalCost, 1e-6)
    }
}
