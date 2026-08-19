package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class OfflineAutomationTest {
    @Test
    fun ownedBusinessWithoutManagerProducesNoOfflineCash() {
        val business = defaultBusinesses().first().copy(level = 100)
        val state = GameState(
            businesses = defaultBusinesses().map { if (it.id == business.id) business else it }
        )

        assertTrue(state.incomePerSecond > 0.0)
        assertEquals(0.0, state.automatedIncomePerSecond, 0.0)

        val reward = OfflineProgress.calculate(state, 1_000_000L, 1_000_000L + 3_600_000L)
        assertEquals(0.0, reward.cash, 0.0)
    }

    @Test
    fun hiredManagerEnablesOfflineProductionForItsBusiness() {
        val business = defaultBusinesses().first().copy(level = 100)
        val state = GameState(
            businesses = defaultBusinesses().map { if (it.id == business.id) business else it },
            hiredManagerIds = setOf(business.id)
        )

        assertTrue(state.automatedIncomePerSecond > 0.0)
        val reward = OfflineProgress.calculate(state, 1_000_000L, 1_000_000L + 3_600_000L)
        assertTrue(reward.eligible)
        assertTrue(reward.cash > 0.0)
    }

    @Test
    fun onlyManagedBusinessesContributeOffline() {
        val first = defaultBusinesses()[0].copy(level = 100)
        val second = defaultBusinesses()[1].copy(level = 100)
        val state = GameState(
            businesses = defaultBusinesses().map {
                when (it.id) {
                    first.id -> first
                    second.id -> second
                    else -> it
                }
            },
            hiredManagerIds = setOf(first.id)
        )

        assertTrue(state.incomePerSecond > state.automatedIncomePerSecond)
        assertEquals(state.businessIncome(first) *
            state.prestigeMultiplier *
            state.legacyMasteryMultiplier *
            state.portfolioDepthMultiplier *
            state.transcendenceMultiplier *
            state.globalUpgradeMultiplier *
            state.boostMultiplier *
            state.eventMultiplier,
            state.automatedIncomePerSecond,
            0.0001
        )
    }
}
