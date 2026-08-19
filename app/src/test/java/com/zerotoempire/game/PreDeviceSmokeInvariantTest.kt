package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PreDeviceSmokeInvariantTest {
    @Test
    fun catalogsAreCompleteAndInternallyConsistent() {
        val businesses = defaultBusinesses()
        val managers = Managers.catalog

        assertEquals(14, businesses.size)
        assertEquals(14, managers.size)
        assertEquals((0..13).toList(), businesses.map { it.id })
        assertEquals((0..13).toList(), managers.map { it.businessId })
        assertEquals(businesses.map { it.id }.toSet().size, businesses.size)
        assertEquals(managers.map { it.businessId }.toSet().size, managers.size)
        assertTrue(businesses.all { it.baseCost > 0.0 && it.baseCost.isFinite() })
        assertTrue(businesses.all { it.baseIncome > 0.0 && it.baseIncome.isFinite() })
        assertTrue(managers.all { it.cost > 0.0 && it.cost.isFinite() })
        assertTrue(managers.all { it.incomeMultiplier >= 1.0 && it.incomeMultiplier.isFinite() })
    }

    @Test
    fun upgradesHaveUniqueIdsAndPlayableBounds() {
        val upgrades = Upgrades.catalog
        assertEquals(upgrades.size, upgrades.map { it.id }.toSet().size)
        assertTrue(upgrades.all { it.gemCost > 0 })
        assertTrue(upgrades.all { it.maxRank > 0 })
        assertTrue(upgrades.all { it.rank in 0..it.maxRank })
    }

    @Test
    fun everyManagerMatchesARealBusinessAndRevealPath() {
        val businesses = defaultBusinesses().associateBy { it.id }
        Managers.catalog.forEach { manager ->
            val business = businesses[manager.businessId]
            assertTrue("manager ${manager.name} has no business", business != null)
            assertTrue(ContentUnlocks.thresholdForBusiness(manager.businessId).isFinite())
        }
    }

    @Test
    fun freshInstallHasImmediatePlayableAction() {
        val state = GameState()
        val first = state.businesses.first()
        assertTrue(ContentUnlocks.isBusinessVisible(first.id, state.lifetimeCash))
        val quote = BulkPurchase.quote(first, state.cash, BuyMode.X1)
        assertEquals(1, quote.count)
        assertTrue(quote.totalCost <= state.cash)
    }

    @Test
    fun finalBusinessAndManagerRemainReachableBeforeNumericCeiling() {
        val finalBusiness = defaultBusinesses().last()
        val finalManager = Managers.catalog.last()
        assertTrue(ContentUnlocks.thresholdForBusiness(finalBusiness.id) < EconomyMath.MAX_VALUE)
        assertTrue(finalBusiness.baseCost < EconomyMath.MAX_VALUE)
        assertTrue(finalManager.cost < EconomyMath.MAX_VALUE)
        assertTrue(ContentUnlocks.isBusinessVisible(finalBusiness.id, 1e30))
    }
}
