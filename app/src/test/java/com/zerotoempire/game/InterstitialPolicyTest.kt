package com.zerotoempire.game

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

    @Test fun enforcesSessionCap() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, sessionShows = 2, dayEpoch = day, dayShows = 2)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 60 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun enforcesDailyCap() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day, dayShows = 4)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 60 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }
}
