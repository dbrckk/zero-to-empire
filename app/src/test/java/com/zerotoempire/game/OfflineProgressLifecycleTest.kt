package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import java.time.ZoneOffset

class OfflineProgressLifecycleTest {
    private val automatedState = GameState(
        businesses = GameState().businesses.mapIndexed { index, business ->
            if (index == 0) business.copy(level = 10) else business
        },
        hiredManagerIds = setOf(0)
    )

    @Test
    fun shortLifecycleInterruptionsNeverSurfaceOfflineReward() {
        val start = 1_700_000_000_000L

        val reward = OfflineProgress.calculate(
            state = automatedState,
            lastSeenMillis = start,
            nowMillis = start + 29_999L,
            zoneId = ZoneOffset.UTC
        )

        assertFalse(reward.eligible)
        assertEquals(29L, reward.paidSeconds)
    }

    @Test
    fun thirtySecondBackgroundBoundaryIsEligibleWhenIncomeIsAutomated() {
        val start = 1_700_000_000_000L

        val reward = OfflineProgress.calculate(
            state = automatedState,
            lastSeenMillis = start,
            nowMillis = start + 30_000L,
            zoneId = ZoneOffset.UTC
        )

        assertTrue(reward.cash > 0.0)
        assertEquals(30L, reward.paidSeconds)
        assertTrue(reward.eligible)
    }

    @Test
    fun invalidOrReversedLifecycleTimestampsCannotGrantOfflineCash() {
        val timestamp = 1_700_000_000_000L

        val equal = OfflineProgress.calculate(
            state = automatedState,
            lastSeenMillis = timestamp,
            nowMillis = timestamp,
            zoneId = ZoneOffset.UTC
        )
        val reversed = OfflineProgress.calculate(
            state = automatedState,
            lastSeenMillis = timestamp,
            nowMillis = timestamp - 60_000L,
            zoneId = ZoneOffset.UTC
        )

        assertEquals(0.0, equal.cash, 0.0)
        assertEquals(0.0, reversed.cash, 0.0)
        assertFalse(equal.eligible)
        assertFalse(reversed.eligible)
    }
}
