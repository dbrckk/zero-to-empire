package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class EconomyInvariantTest {
    @Test
    fun bulkPurchaseNeverSpendsMoreThanAvailableCash() {
        val business = defaultBusinesses().first().copy(level = 12)
        val budgets = listOf(0.0, business.nextCost * .99, business.nextCost, 1e6, 1e12)

        budgets.forEach { cash ->
            BuyMode.entries.forEach { mode ->
                val quote = BulkPurchase.quote(business, cash, mode)
                assertTrue("negative count for $mode", quote.count >= 0)
                assertTrue("negative cost for $mode", quote.totalCost >= 0.0)
                assertTrue("non-finite cost for $mode", quote.totalCost.isFinite())
                if (quote.valid) {
                    assertTrue("quote exceeds budget for $mode", quote.totalCost <= cash)
                }
            }
        }
    }

    @Test
    fun bulkCostIsMonotonicWithQuantity() {
        val business = defaultBusinesses().first().copy(level = 25)
        var previous = 0.0
        for (count in 1..100) {
            val cost = BulkPurchase.cost(business, count)
            assertTrue(cost.isFinite())
            assertTrue(cost >= previous)
            previous = cost
        }
    }

    @Test
    fun offlineProgressRejectsClockRollback() {
        val state = automatedState()
        val reward = OfflineProgress.calculate(
            state = state,
            lastSeenMillis = 2_000_000L,
            nowMillis = 1_000_000L
        )

        assertEquals(0L, reward.elapsedSeconds)
        assertEquals(0L, reward.paidSeconds)
        assertEquals(0.0, reward.cash, 0.0)
        assertFalse(reward.eligible)
    }

    @Test
    fun offlineProgressPaysOnlyAutomatedBusinesses() {
        val businesses = defaultBusinesses().mapIndexed { index, business ->
            if (index == 0) business.copy(level = 20) else business
        }
        val manual = GameState(businesses = businesses)
        val automated = manual.copy(hiredManagerIds = setOf(businesses.first().id))
        val now = 10_000_000L
        val since = now - 3600_000L

        val manualReward = OfflineProgress.calculate(manual, since, now)
        val automatedReward = OfflineProgress.calculate(automated, since, now)

        assertEquals(0.0, manualReward.cash, 0.0)
        assertTrue(automatedReward.cash > 0.0)
    }

    @Test
    fun offlineRewardCannotExceedConfiguredCap() {
        val state = automatedState().copy(upgradeRanks = mapOf("offline" to 8))
        val now = 10_000_000_000L
        val reward = OfflineProgress.calculate(
            state,
            lastSeenMillis = now - 30L * 24L * 3600L * 1000L,
            nowMillis = now
        )

        assertEquals(16L * 3600L, reward.paidSeconds)
        assertTrue(reward.elapsedSeconds > reward.paidSeconds)
    }

    private fun automatedState(): GameState {
        val businesses = defaultBusinesses().mapIndexed { index, business ->
            if (index == 0) business.copy(level = 20) else business
        }
        return GameState(
            businesses = businesses,
            hiredManagerIds = setOf(businesses.first().id)
        )
    }
}
