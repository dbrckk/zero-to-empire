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

    @Test fun commandCenterPrioritizesClaimableThenActiveThenDone() {
        val active = challenge(id = "active", progress = 5.0)
        val done = challenge(id = "done", progress = 10.0, claimed = true)
        val claimable = challenge(id = "claimable", progress = 10.0)

        val ordered = ChallengeOrdering.forCommandCenter(listOf(done, active, claimable))

        assertEquals(listOf("claimable", "active", "done"), ordered.map { it.id })
    }

    @Test fun commandCenterOrderingIsStableInsideSamePriority() {
        val activeA = challenge(id = "active-a", progress = 1.0)
        val activeB = challenge(id = "active-b", progress = 2.0)
        val claimableA = challenge(id = "claimable-a", progress = 10.0)
        val claimableB = challenge(id = "claimable-b", progress = 12.0)
        val doneA = challenge(id = "done-a", progress = 10.0, claimed = true)
        val doneB = challenge(id = "done-b", progress = 11.0, claimed = true)

        val ordered = ChallengeOrdering.forCommandCenter(
            listOf(activeA, doneA, claimableA, activeB, claimableB, doneB)
        )

        assertEquals(
            listOf("claimable-a", "claimable-b", "active-a", "active-b", "done-a", "done-b"),
            ordered.map { it.id }
        )
    }

    @Test fun commandCenterOrderingDoesNotMutateSourceList() {
        val source = listOf(
            challenge(id = "done", progress = 10.0, claimed = true),
            challenge(id = "claimable", progress = 10.0),
            challenge(id = "active", progress = 1.0)
        )

        ChallengeOrdering.forCommandCenter(source)

        assertEquals(listOf("done", "claimable", "active"), source.map { it.id })
    }

    @Test fun prestigeWindowIncreasesWithEconomyScale() {
        assertTrue(BalanceGuard.recommendedPrestigeWindowSeconds(1e15) > BalanceGuard.recommendedPrestigeWindowSeconds(1e6))
    }

    private fun challenge(id: String, progress: Double, claimed: Boolean = false) = TimedChallenge(
        id = id,
        title = id,
        description = id,
        metric = ChallengeMetric.TAPS,
        target = 10.0,
        rewardGems = 1,
        progress = progress,
        claimed = claimed
    )
}
