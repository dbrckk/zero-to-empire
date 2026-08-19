package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class EconomySafetyTest {
    @Test
    fun finiteClampsNanInfinityAndOverflow() {
        assertEquals(0.0, EconomyMath.finite(Double.NaN), 0.0)
        assertEquals(0.0, EconomyMath.finite(-1.0), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.finite(Double.POSITIVE_INFINITY), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.finite(Double.MAX_VALUE), 0.0)
    }

    @Test
    fun safeAddSaturatesInsteadOfOverflowing() {
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.safeAdd(EconomyMath.MAX_VALUE, 1.0), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.safeAdd(EconomyMath.MAX_VALUE * .9, EconomyMath.MAX_VALUE * .2), 0.0)
        assertTrue(EconomyMath.safeAdd(10.0, 20.0).isFinite())
    }

    @Test
    fun growthCostRemainsFiniteAtExtremeLevel() {
        val cost = EconomyMath.growthCost(10.0, Int.MAX_VALUE)
        assertTrue(cost.isFinite())
        assertEquals(EconomyMath.MAX_VALUE, cost, 0.0)
    }

    @Test
    fun extremeGameStateNeverProducesNaNOrInfinity() {
        val maxedBusinesses = defaultBusinesses().map { it.copy(level = Int.MAX_VALUE) }
        val state = GameState(
            cash = EconomyMath.MAX_VALUE,
            lifetimeCash = EconomyMath.MAX_VALUE,
            prestigePoints = Int.MAX_VALUE,
            businesses = maxedBusinesses,
            hiredManagerIds = maxedBusinesses.map { it.id }.toSet(),
            upgradeRanks = mapOf("income" to Int.MAX_VALUE, "tap" to Int.MAX_VALUE, "prestige" to Int.MAX_VALUE)
        )

        assertTrue(state.incomePerSecond.isFinite())
        assertTrue(state.automatedIncomePerSecond.isFinite())
        assertTrue(state.tapValue.isFinite())
        assertTrue(state.incomePerSecond <= EconomyMath.MAX_VALUE)
        assertTrue(state.tapValue <= EconomyMath.MAX_VALUE)
    }

    @Test
    fun prestigeResetPreservesPermanentResourcesAndBoost() {
        val boostEnd = 9_999_999_999L
        val state = GameState(
            cash = 123_456.0,
            lifetimeCash = 1e18,
            prestigePoints = 0,
            businesses = defaultBusinesses().mapIndexed { index, b -> if (index == 0) b.copy(level = 100) else b },
            hiredManagerIds = setOf(0),
            upgradeRanks = mapOf("income" to 4, "prestige" to 2),
            gems = 777,
            boostEndsAtMillis = boostEnd
        )

        val reset = Progression.prestigeReset(state)
        assertNotNull(reset)
        reset!!
        assertEquals(10.0, reset.cash, 0.0)
        assertEquals(10.0, reset.lifetimeCash, 0.0)
        assertTrue(reset.businesses.all { it.level == 0 })
        assertTrue(reset.hiredManagerIds.isEmpty())
        assertEquals(777, reset.gems)
        assertEquals(state.upgradeRanks, reset.upgradeRanks)
        assertEquals(boostEnd, reset.boostEndsAtMillis)
        assertTrue(reset.prestigePoints > 0)
    }

    @Test
    fun prestigeCannotRepeatWithoutNewRunProgress() {
        val first = Progression.prestigeReset(GameState(lifetimeCash = 1e12, prestigePoints = 0))
        assertNotNull(first)
        assertNull(Progression.prestigeReset(first!!))
    }

    @Test
    fun prestigeRewardHandlesNonFiniteInputs() {
        assertEquals(0, Progression.prestigeReward(Double.NaN))
        assertEquals(0, Progression.prestigeReward(Double.NEGATIVE_INFINITY))
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(Double.POSITIVE_INFINITY))
        assertTrue(Progression.prestigeReward(EconomyMath.MAX_VALUE) >= 0)
    }
}
