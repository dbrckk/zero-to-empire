package com.zerotoempire.game

import org.junit.Assert.assertEquals
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
    fun resetStateRetainsPermanentPowerButResetsRunEconomy() {
        val boostEnd = System.currentTimeMillis() + 600_000L
        val before = GameState(
            cash = 1e15,
            lifetimeCash = 1e15,
            prestigePoints = 3,
            gems = 90,
            upgradeRanks = mapOf("income" to 5, "prestige" to 4),
            boostEndsAtMillis = boostEnd,
            businesses = defaultBusinesses().mapIndexed { index, b -> if (index < 4) b.copy(level = 100) else b }
        )
        val total = Progression.prestigeReward(before.lifetimeCash)
        val reset = GameState(
            prestigePoints = total,
            gems = before.gems,
            upgradeRanks = before.upgradeRanks,
            boostEndsAtMillis = before.boostEndsAtMillis
        )

        assertEquals(10.0, reset.cash, 0.0)
        assertEquals(10.0, reset.lifetimeCash, 0.0)
        assertEquals(0, reset.businesses.sumOf { it.level })
        assertEquals(before.gems, reset.gems)
        assertEquals(before.upgradeRanks, reset.upgradeRanks)
        assertEquals(boostEnd, reset.boostEndsAtMillis)
        assertTrue(reset.prestigePoints > before.prestigePoints)
        assertTrue(reset.prestigeMultiplier > before.copy(prestigePoints = before.prestigePoints).prestigeMultiplier)
    }

    @Test
    fun nextRunCanEarnAdditionalLegacy() {
        val firstTotal = Progression.prestigeReward(1e12)
        val laterTotal = Progression.prestigeReward(1e18)
        assertTrue(laterTotal - firstTotal > 0)
    }

    @Test
    fun pathologicalPrestigeInputsAreBounded() {
        assertEquals(0, Progression.prestigeReward(Double.NaN))
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(Double.POSITIVE_INFINITY))
        assertEquals(0, Progression.prestigeReward(-1.0))
    }
}
