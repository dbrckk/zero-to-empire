package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class PrestigeResetTest {
    @Test
    fun prestigeResetKeepsOnlyPermanentProgress() {
        val state = GameState(
            cash = 9.0e12,
            lifetimeCash = 1.0e15,
            prestigePoints = 3,
            businesses = defaultBusinesses().mapIndexed { index, b -> b.copy(level = index + 20) },
            hiredManagerIds = setOf(0, 1, 2, 3),
            upgradeRanks = mapOf("income" to 4, "tap" to 2, "offline" to 3, "prestige" to 5),
            gems = 777,
            boostEndsAtMillis = 9_000_000L
        )

        val reset = Progression.prestigeReset(state)
        assertNotNull(reset)
        reset!!
        assertEquals(10.0, reset.cash, 0.0)
        assertEquals(10.0, reset.lifetimeCash, 0.0)
        assertTrue(reset.prestigePoints > state.prestigePoints)
        assertEquals(Progression.prestigeReward(state.lifetimeCash), reset.prestigePoints)
        assertTrue(reset.businesses.all { it.level == 0 })
        assertTrue(reset.hiredManagerIds.isEmpty())
        assertEquals(state.upgradeRanks, reset.upgradeRanks)
        assertEquals(777, reset.gems)
        assertEquals(9_000_000L, reset.boostEndsAtMillis)
    }

    @Test
    fun prestigeResetRejectsRunWithoutNewLegacyPoints() {
        assertNull(Progression.prestigeReset(GameState(lifetimeCash = 10.0, prestigePoints = 0)))
    }

    @Test
    fun prestigeResetAtNumericCeilingCannotWrapPoints() {
        val reset = Progression.prestigeReset(
            GameState(lifetimeCash = EconomyMath.MAX_VALUE, prestigePoints = Int.MAX_VALUE - 1)
        )
        assertNotNull(reset)
        assertEquals(Int.MAX_VALUE, reset!!.prestigePoints)
        assertNull(Progression.prestigeReset(reset.copy(lifetimeCash = EconomyMath.MAX_VALUE)))
    }

    @Test
    fun prestigeReadinessAtIntegerCeilingNeverWrapsNegative() {
        assertEquals(0.0, LateGame.prestigeReadiness(Int.MAX_VALUE, EconomyMath.MAX_VALUE), 0.0)
        assertFalse(LateGame.recommendedPrestige(Int.MAX_VALUE, EconomyMath.MAX_VALUE))
        val nearCeiling = LateGame.prestigeReadiness(Int.MAX_VALUE - 1, EconomyMath.MAX_VALUE)
        assertTrue(nearCeiling >= 0.0)
        assertTrue(nearCeiling.isFinite())
    }
}
