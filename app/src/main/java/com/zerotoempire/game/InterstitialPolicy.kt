package com.zerotoempire.game

import android.content.Context
import java.time.LocalDate

enum class NaturalBreakPoint { PRESTIGE, ERA_UNLOCK }

data class InterstitialPolicyState(
    val sessionStartedAtMillis: Long,
    val sessionShows: Int = 0,
    val lastShownAtMillis: Long = 0L,
    val dayEpoch: Long = LocalDate.now().toEpochDay(),
    val dayShows: Int = 0
)

object InterstitialPolicy {
    const val MIN_SESSION_AGE_MS = 12L * 60_000L
    const val MIN_GAP_MS = 8L * 60_000L
    const val MAX_PER_SESSION = 2
    const val MAX_PER_DAY = 4

    fun canShow(
        state: InterstitialPolicyState,
        nowMillis: Long,
        currentEpochDay: Long,
        breakPoint: NaturalBreakPoint,
        onboardingCompleted: Boolean,
        adsRemoved: Boolean
    ): Boolean {
        if (adsRemoved || !onboardingCompleted) return false
        if (breakPoint !in setOf(NaturalBreakPoint.PRESTIGE, NaturalBreakPoint.ERA_UNLOCK)) return false
        if (nowMillis - state.sessionStartedAtMillis < MIN_SESSION_AGE_MS) return false
        if (state.sessionShows >= MAX_PER_SESSION) return false
        val showsToday = if (state.dayEpoch == currentEpochDay) state.dayShows else 0
        if (showsToday >= MAX_PER_DAY) return false
        if (state.lastShownAtMillis > 0 && nowMillis - state.lastShownAtMillis < MIN_GAP_MS) return false
        return true
    }

    fun recordShow(
        state: InterstitialPolicyState,
        nowMillis: Long,
        currentEpochDay: Long
    ): InterstitialPolicyState {
        val sameDay = state.dayEpoch == currentEpochDay
        return state.copy(
            sessionShows = state.sessionShows + 1,
            lastShownAtMillis = nowMillis,
            dayEpoch = currentEpochDay,
            dayShows = if (sameDay) state.dayShows + 1 else 1
        )
    }
}

class InterstitialFrequencyStore(context: Context) {
    private val prefs = context.getSharedPreferences("zero_empire_ad_frequency", Context.MODE_PRIVATE)
    private val sessionStart = System.currentTimeMillis()
    private var sessionShows = 0

    fun snapshot(): InterstitialPolicyState = InterstitialPolicyState(
        sessionStartedAtMillis = sessionStart,
        sessionShows = sessionShows,
        lastShownAtMillis = prefs.getLong("last_shown", 0L),
        dayEpoch = prefs.getLong("day_epoch", LocalDate.now().toEpochDay()),
        dayShows = prefs.getInt("day_shows", 0)
    )

    fun recordShow(nowMillis: Long = System.currentTimeMillis()) {
        val today = LocalDate.now().toEpochDay()
        val updated = InterstitialPolicy.recordShow(snapshot(), nowMillis, today)
        sessionShows = updated.sessionShows
        prefs.edit()
            .putLong("last_shown", updated.lastShownAtMillis)
            .putLong("day_epoch", updated.dayEpoch)
            .putInt("day_shows", updated.dayShows)
            .apply()
    }
}
