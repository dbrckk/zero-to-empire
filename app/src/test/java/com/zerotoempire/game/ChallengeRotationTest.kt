package com.zerotoempire.game

import org.junit.Assert.*
import org.junit.Test
import java.time.LocalDate

class ChallengeRotationTest {
    @Test fun weeklyKeyIsStableInsideSameIsoWeek() {
        val a = ChallengeRotation.weeklyKey(LocalDate.of(2026, 8, 10))
        val b = ChallengeRotation.weeklyKey(LocalDate.of(2026, 8, 14))
        assertEquals(a, b)
    }

    @Test fun weeklyKeyChangesAcrossWeeks() {
        val a = ChallengeRotation.weeklyKey(LocalDate.of(2026, 8, 14))
        val b = ChallengeRotation.weeklyKey(LocalDate.of(2026, 8, 17))
        assertNotEquals(a, b)
    }

    @Test fun completedChallengeCannotLoseCompletion() {
        val date = LocalDate.of(2026, 8, 14)
        val key = ChallengeRotation.weeklyKey(date)
        val meta = PlayerMeta(
            totalTaps = 600,
            challengeWeekKey = key,
            challengeWeekTapBase = 0L
        )
        val challenge = ChallengeRotation.current(GameState(), meta, date).first { it.metric == ChallengeMetric.TAPS }
        assertTrue(challenge.completed)
        assertEquals(1f, challenge.fraction)
    }

    @Test fun claimedChallengeIsScopedToItsWeek() {
        val date = LocalDate.of(2026, 8, 14)
        val key = ChallengeRotation.weeklyKey(date)
        val meta = PlayerMeta(totalTaps = 600, claimedChallengeIds = setOf("$key:tap"))
        val current = ChallengeRotation.current(GameState(), meta, date).first { it.metric == ChallengeMetric.TAPS }
        val nextWeek = ChallengeRotation.current(GameState(), meta, date.plusWeeks(1)).first { it.metric == ChallengeMetric.TAPS }
        assertTrue(current.claimed)
        assertFalse(nextWeek.claimed)
    }

    @Test fun prestigeWindowIncreasesWithEconomyScale() {
        assertTrue(BalanceGuard.recommendedPrestigeWindowSeconds(1e15) > BalanceGuard.recommendedPrestigeWindowSeconds(1e6))
    }
}
