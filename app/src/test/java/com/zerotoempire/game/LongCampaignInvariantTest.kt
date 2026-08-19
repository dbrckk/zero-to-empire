package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class LongCampaignInvariantTest {
    @Test
    fun repeatedPrestigeCyclesRemainFiniteAndProgressiveUntilSaturation() {
        var points = 0
        val progressiveRuns = listOf(1e12, 1e15, 1e18, 1e21, 1e24, 1e27, 1e28)

        progressiveRuns.forEach { lifetime ->
            val state = GameState(
                lifetimeCash = lifetime,
                prestigePoints = points,
                gems = 500,
                upgradeRanks = mapOf("income" to 10, "prestige" to 10),
                boostEndsAtMillis = 9_999_999_999L
            )
            val reset = Progression.prestigeReset(state)
            assertNotNull("run at $lifetime should earn additional legacy", reset)
            reset!!
            val previousPoints = points
            points = reset.prestigePoints

            assertTrue(points > previousPoints)
            assertTrue(reset.prestigeMultiplier.isFinite())
            assertTrue(reset.legacyMasteryMultiplier.isFinite())
            assertTrue(reset.incomePerSecond.isFinite())
            assertEquals(500, reset.gems)
            assertEquals(state.upgradeRanks, reset.upgradeRanks)
            assertEquals(state.boostEndsAtMillis, reset.boostEndsAtMillis)
            assertTrue(reset.businesses.all { it.level == 0 })
            assertTrue(reset.hiredManagerIds.isEmpty())
        }

        val saturated = Progression.prestigeReset(GameState(lifetimeCash = 1e30, prestigePoints = points))
        assertNotNull(saturated)
        assertEquals(Int.MAX_VALUE, saturated!!.prestigePoints)
        assertNull(Progression.prestigeReset(GameState(lifetimeCash = EconomyMath.MAX_VALUE, prestigePoints = Int.MAX_VALUE)))
    }

    @Test
    fun matureManagedEmpireCanGoOfflineAndReturnWithoutOverflow() {
        val businesses = defaultBusinesses().map { business ->
            business.copy(level = if (business.id >= 10) 1_000 else 5_000)
        }
        val state = GameState(
            cash = 1e150,
            lifetimeCash = 1e150,
            prestigePoints = 1_000_000,
            businesses = businesses,
            hiredManagerIds = businesses.map { it.id }.toSet(),
            upgradeRanks = mapOf("income" to 20, "offline" to 8, "prestige" to 15),
            boostEndsAtMillis = 0L
        )

        val start = 1_800_000_000_000L
        val reward = OfflineProgress.calculate(state, start, start + 7L * 24L * 60L * 60L * 1_000L)

        assertTrue(reward.eligible)
        assertEquals(16L * 60L * 60L, reward.paidSeconds)
        assertTrue(reward.cash.isFinite())
        assertTrue(reward.cash > 0.0)
        assertTrue(reward.cash <= EconomyMath.MAX_VALUE)

        val returned = state.copy(
            cash = EconomyMath.safeAdd(state.cash, reward.cash),
            lifetimeCash = EconomyMath.safeAdd(state.lifetimeCash, reward.cash)
        )
        assertTrue(returned.cash.isFinite())
        assertTrue(returned.lifetimeCash.isFinite())
        assertTrue(returned.incomePerSecond.isFinite())
        assertTrue(returned.tapValue.isFinite())
    }

    @Test
    fun transcendenceFrontierStillSupportsPurchasesAndPrestigeMath() {
        val nexus = defaultBusinesses().last().copy(level = 1_000)
        val state = GameState(
            cash = EconomyMath.MAX_VALUE,
            lifetimeCash = EconomyMath.MAX_VALUE,
            prestigePoints = 10_000_000,
            businesses = defaultBusinesses().map { if (it.id == nexus.id) nexus else it },
            hiredManagerIds = setOf(nexus.id),
            upgradeRanks = mapOf("income" to 20, "prestige" to 15)
        )

        val quote = BulkPurchase.quote(nexus, state.cash, BuyMode.MAX)
        assertTrue(quote.count >= 0)
        assertTrue(quote.totalCost.isFinite())
        assertTrue(state.incomePerSecond.isFinite())
        assertTrue(state.automatedIncomePerSecond.isFinite())
        assertTrue(Progression.prestigeReward(state.lifetimeCash) >= state.prestigePoints)
    }
}
