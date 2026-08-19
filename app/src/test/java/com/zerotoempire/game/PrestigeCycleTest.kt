package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class PrestigeCycleTest {
    @Test
    fun prestigeRewardGrowsAcrossRunsAndStaysFinite() {
        val first = Progression.prestigeReward(1e9)
        val second = Progression.prestigeReward(1e15)
        val endgame = Progression.prestigeReward(1e30)
        assertTrue(first > 0)
        assertTrue(second > first)
        assertTrue(endgame > second)
        assertTrue(endgame > 0)
    }

    @Test
    fun productionResetRetainsPermanentPowerButResetsRunEconomy() {
        val boostEnd = 9_999_999_999L
        val before = GameState(
            cash = 1e15,
            lifetimeCash = 1e15,
            prestigePoints = 3,
            gems = 90,
            upgradeRanks = mapOf("income" to 5, "prestige" to 4),
            boostEndsAtMillis = boostEnd,
            businesses = defaultBusinesses().mapIndexed { index, b -> if (index < 4) b.copy(level = 100) else b },
            hiredManagerIds = setOf(0, 1, 2)
        )
        val reset = Progression.prestigeReset(before)
        assertNotNull(reset)
        reset!!

        assertEquals(10.0, reset.cash, 0.0)
        assertEquals(10.0, reset.lifetimeCash, 0.0)
        assertEquals(0L, reset.businesses.sumOf { it.level.toLong() })
        assertTrue(reset.hiredManagerIds.isEmpty())
        assertEquals(before.gems, reset.gems)
        assertEquals(before.upgradeRanks, reset.upgradeRanks)
        assertEquals(boostEnd, reset.boostEndsAtMillis)
        assertTrue(reset.prestigePoints > before.prestigePoints)
        assertEquals(0.0, reset.incomePerSecond, 0.0)
        assertEquals(0.0, reset.automatedIncomePerSecond, 0.0)
        assertTrue(reset.tapValue.isFinite())
        assertTrue(reset.tapValue > 1.0)
    }

    @Test
    fun sameRunCannotPrestigeTwiceWithoutNewProgress() {
        val first = Progression.prestigeReset(GameState(lifetimeCash = 1e12))
        assertNotNull(first)
        assertNull(Progression.prestigeReset(first!!))
    }

    @Test
    fun laterRunEarnsMoreLegacyButNeverCarriesAutomation() {
        val first = Progression.prestigeReset(GameState(lifetimeCash = 1e12))!!
        val laterRun = first.copy(
            cash = 1e18,
            lifetimeCash = 1e18,
            businesses = defaultBusinesses().map { it.copy(level = 250) },
            hiredManagerIds = defaultBusinesses().map { it.id }.toSet()
        )
        val second = Progression.prestigeReset(laterRun)
        assertNotNull(second)
        second!!

        assertTrue(second.prestigePoints > first.prestigePoints)
        assertTrue(second.hiredManagerIds.isEmpty())
        assertFalse(second.businesses.any { it.level > 0 })
        assertEquals(10.0, second.lifetimeCash, 0.0)
    }

    @Test
    fun maxLegacySaveCannotOverflowOrPrestigeAgain() {
        val maxed = GameState(
            cash = EconomyMath.MAX_VALUE,
            lifetimeCash = EconomyMath.MAX_VALUE,
            prestigePoints = Int.MAX_VALUE
        )
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(maxed.lifetimeCash))
        assertNull(Progression.prestigeReset(maxed))
        assertTrue(maxed.prestigeMultiplier.isFinite())
        assertTrue(maxed.tapValue.isFinite())
    }

    @Test
    fun pathologicalPrestigeInputsAreBounded() {
        assertEquals(0, Progression.prestigeReward(Double.NaN))
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(Double.POSITIVE_INFINITY))
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(EconomyMath.MAX_VALUE))
        assertEquals(0, Progression.prestigeReward(-1.0))
    }
}
