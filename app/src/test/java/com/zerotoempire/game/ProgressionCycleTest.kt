package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Test

class ProgressionCycleTest {
    @Test
    fun repeatedPrestigeOfflineCyclePreservesOnlyPermanentProgress() {
        val activeBoost = System.currentTimeMillis() + 3_600_000L
        val runOne = GameState(
            cash = 5e12,
            lifetimeCash = 5e12,
            businesses = defaultBusinesses().mapIndexed { index, b ->
                when (index) {
                    0 -> b.copy(level = 250)
                    1 -> b.copy(level = 100)
                    else -> b
                }
            },
            hiredManagerIds = setOf(0, 1),
            upgradeRanks = mapOf("income" to 3, "offline" to 2, "prestige" to 1),
            gems = 321,
            boostEndsAtMillis = activeBoost
        )

        val afterFirstPrestige = Progression.prestigeReset(runOne)
        assertNotNull(afterFirstPrestige)
        afterFirstPrestige!!
        assertEquals(321, afterFirstPrestige.gems)
        assertEquals(runOne.upgradeRanks, afterFirstPrestige.upgradeRanks)
        assertEquals(activeBoost, afterFirstPrestige.boostEndsAtMillis)
        assertTrue(afterFirstPrestige.businesses.all { it.level == 0 })
        assertTrue(afterFirstPrestige.hiredManagerIds.isEmpty())

        val rebuiltBusiness = afterFirstPrestige.businesses.first().copy(level = 100)
        val runTwo = afterFirstPrestige.copy(
            cash = 1e16,
            lifetimeCash = 1e16,
            businesses = afterFirstPrestige.businesses.map { if (it.id == rebuiltBusiness.id) rebuiltBusiness else it },
            hiredManagerIds = setOf(rebuiltBusiness.id)
        )

        val start = 1_700_000_000_000L
        val reward = OfflineProgress.calculate(runTwo.copy(boostEndsAtMillis = 0L), start, start + 3_600_000L)
        assertTrue(reward.eligible)
        assertTrue(reward.cash > 0.0)
        assertTrue(reward.cash.isFinite())

        val creditedRun = runTwo.copy(
            cash = EconomyMath.safeAdd(runTwo.cash, reward.cash),
            lifetimeCash = EconomyMath.safeAdd(runTwo.lifetimeCash, reward.cash)
        )
        val afterSecondPrestige = Progression.prestigeReset(creditedRun)
        assertNotNull(afterSecondPrestige)
        afterSecondPrestige!!

        assertTrue(afterSecondPrestige.prestigePoints > afterFirstPrestige.prestigePoints)
        assertEquals(321, afterSecondPrestige.gems)
        assertEquals(runOne.upgradeRanks, afterSecondPrestige.upgradeRanks)
        assertEquals(activeBoost, afterSecondPrestige.boostEndsAtMillis)
        assertTrue(afterSecondPrestige.businesses.all { it.level == 0 })
        assertTrue(afterSecondPrestige.hiredManagerIds.isEmpty())
        assertEquals(10.0, afterSecondPrestige.cash, 0.0)
        assertEquals(10.0, afterSecondPrestige.lifetimeCash, 0.0)
    }
}
