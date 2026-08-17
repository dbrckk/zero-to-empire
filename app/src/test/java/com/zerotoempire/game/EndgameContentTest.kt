package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class EndgameContentTest {
    @Test fun businessCatalogContainsPostGalacticTier() {
        val businesses = defaultBusinesses()
        assertEquals(14, businesses.size)
        assertEquals("Intergalactic Gateway", businesses[10].name)
        assertEquals("Cosmic Foundry", businesses[11].name)
        assertEquals("Reality Engine", businesses[12].name)
        assertEquals("Transcendent Nexus", businesses[13].name)
    }

    @Test fun endgameBusinessesScaleStrictly() {
        val endgame = defaultBusinesses().filter { it.id >= 10 }
        endgame.zipWithNext().forEach { (a, b) ->
            assertTrue(b.baseCost > a.baseCost)
            assertTrue(b.baseIncome > a.baseIncome)
        }
    }

    @Test fun everyBusinessHasManager() {
        val managedIds = Managers.catalog.map { it.businessId }.toSet()
        defaultBusinesses().forEach { assertTrue(it.id in managedIds) }
    }

    @Test fun managerMultipliersIncreaseIntoEndgame() {
        val endgame = Managers.catalog.filter { it.businessId >= 9 }
        endgame.zipWithNext().forEach { (a, b) -> assertTrue(b.incomeMultiplier > a.incomeMultiplier) }
    }
}
