package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import java.time.LocalDate

class WeeklyChallengeTest {
    private val date = LocalDate.of(2026, 8, 18)

    @Test
    fun weeklyCountersUseBaselinesInsteadOfLifetimeTotals() {
        val key = ChallengeRotation.weeklyKey(date)
        val meta = PlayerMeta(
            totalTaps = 10_450,
            totalPurchases = 4_120,
            prestigeCount = 27,
            challengeWeekKey = key,
            challengeWeekTapBase = 10_000,
            challengeWeekPurchaseBase = 4_000,
            challengeWeekPrestigeBase = 26
        )
        val challenges = ChallengeRotation.current(GameState(), meta, date)

        assertEquals(450.0, challenges.first { it.metric == ChallengeMetric.TAPS }.progress, 0.0)
        assertEquals(120.0, challenges.first { it.metric == ChallengeMetric.PURCHASES }.progress, 0.0)
        assertEquals(1.0, challenges.first { it.metric == ChallengeMetric.PRESTIGES }.progress, 0.0)
        assertFalse(challenges.first { it.metric == ChallengeMetric.TAPS }.completed)
    }

    @Test
    fun claimsRemainScopedToIsoWeek() {
        val key = ChallengeRotation.weeklyKey(date)
        val meta = PlayerMeta(
            totalTaps = 600,
            challengeWeekKey = key,
            claimedChallengeIds = setOf("$key:tap")
        )
        val challenge = ChallengeRotation.current(GameState(), meta, date).first { it.metric == ChallengeMetric.TAPS }

        assertTrue(challenge.completed)
        assertTrue(challenge.claimed)
    }
}
