package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import java.time.ZoneId

class OfflineProgressBoundaryTest {
    private val utc = ZoneId.of("UTC")

    @Test
    fun exactlyThirtySecondsIsEligibleWhenAutomated() {
        val state = automatedState()
        val start = 1_700_000_000_000L
        val reward = OfflineProgress.calculate(state, start, start + 30_000L, utc)

        assertEquals(30L, reward.elapsedSeconds)
        assertEquals(30L, reward.paidSeconds)
        assertTrue(reward.cash > 0.0)
        assertTrue(reward.eligible)
    }

    @Test
    fun lessThanThirtySecondsIsNotEligible() {
        val state = automatedState()
        val start = 1_700_000_000_000L
        val reward = OfflineProgress.calculate(state, start, start + 29_999L, utc)

        assertEquals(29L, reward.elapsedSeconds)
        assertEquals(29L, reward.paidSeconds)
        assertTrue(reward.cash > 0.0)
        assertFalse(reward.eligible)
    }

    @Test
    fun boostExpirySplitsOfflineIncomeExactlyAtBoundary() {
        val base = automatedState()
        val start = 1_700_000_000_000L
        val state = base.copy(boostEndsAtMillis = start + 60_000L)
        val reward = OfflineProgress.calculate(state, start, start + 120_000L, utc)

        val expected = base.automatedBaseIncomePerSecond * .75 * (60.0 * 2.0 + 60.0)
        assertEquals(expected, reward.cash, expected * 1e-9 + 1e-9)
    }

    @Test
    fun rewardAtOfflineCapDoesNotGrowWithLongerAbsence() {
        val state = automatedState()
        val start = 1_700_000_000_000L
        val capEnd = start + 8L * 3600L * 1000L
        val capped = OfflineProgress.calculate(state, start, capEnd, utc)
        val muchLater = OfflineProgress.calculate(state, start, start + 30L * 24L * 3600L * 1000L, utc)

        assertEquals(8L * 3600L, capped.paidSeconds)
        assertEquals(capped.paidSeconds, muchLater.paidSeconds)
        assertEquals(capped.cash, muchLater.cash, capped.cash * 1e-9 + 1e-9)
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
