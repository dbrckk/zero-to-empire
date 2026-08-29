package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class InterstitialPolicyTest {
    private val day = 20_000L
    private val sessionStart = 1_000_000L

    @Test fun blocksDuringEarlySession() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 5 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun allowsExactlyAtSessionWarmupBoundary() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertTrue(InterstitialPolicy.canShow(s, sessionStart + InterstitialPolicy.MIN_SESSION_AGE_MS, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun allowsAtNaturalBreakAfterWarmup() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertTrue(InterstitialPolicy.canShow(s, sessionStart + 13 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun removeAdsAlwaysWins() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 30 * 60_000L, day, NaturalBreakPoint.ERA_UNLOCK, true, true))
    }

    @Test fun onboardingMustBeComplete() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 30 * 60_000L, day, NaturalBreakPoint.PRESTIGE, false, false))
    }

    @Test fun enforcesMinimumGap() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, lastShownAtMillis = now - 2 * 60_000L, dayEpoch = day, dayShows = 1)
        assertFalse(InterstitialPolicy.canShow(s, now, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun blocksOneMillisecondBeforeMinimumGap() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            lastShownAtMillis = now - InterstitialPolicy.MIN_GAP_MS + 1,
            dayEpoch = day,
            dayShows = 1
        )
        assertFalse(InterstitialPolicy.canShow(s, now, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun allowsExactlyAtMinimumGap() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            lastShownAtMillis = now - InterstitialPolicy.MIN_GAP_MS,
            dayEpoch = day,
            dayShows = 1
        )
        assertTrue(InterstitialPolicy.canShow(s, now, day, NaturalBreakPoint.ERA_UNLOCK, true, false))
    }

    @Test fun enforcesSessionCap() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, sessionShows = InterstitialPolicy.MAX_PER_SESSION, dayEpoch = day, dayShows = 2)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 60 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun enforcesDailyCap() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day, dayShows = InterstitialPolicy.MAX_PER_DAY)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 60 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun staleDailyCapDoesNotCarryIntoNewDay() {
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            dayEpoch = day - 1,
            dayShows = InterstitialPolicy.MAX_PER_DAY
        )
        assertTrue(InterstitialPolicy.canShow(s, sessionStart + 60 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun recordShowIncrementsSessionAndSameDayCounters() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            sessionShows = 1,
            lastShownAtMillis = 42L,
            dayEpoch = day,
            dayShows = 2
        )

        val updated = InterstitialPolicy.recordShow(s, now, day)

        assertEquals(2, updated.sessionShows)
        assertEquals(now, updated.lastShownAtMillis)
        assertEquals(day, updated.dayEpoch)
        assertEquals(3, updated.dayShows)
    }

    @Test fun recordShowResetsDailyCounterOnNewDay() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            sessionShows = 1,
            dayEpoch = day - 1,
            dayShows = InterstitialPolicy.MAX_PER_DAY
        )

        val updated = InterstitialPolicy.recordShow(s, now, day)

        assertEquals(2, updated.sessionShows)
        assertEquals(day, updated.dayEpoch)
        assertEquals(1, updated.dayShows)
    }
}
