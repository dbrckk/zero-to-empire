package com.zerotoempire.game

import java.time.LocalDate
import java.time.temporal.WeekFields
import kotlin.math.min

enum class ChallengeMetric { TAPS, PURCHASES, LIFETIME_CASH, PRESTIGES }

data class TimedChallenge(
    val id: String,
    val title: String,
    val description: String,
    val metric: ChallengeMetric,
    val target: Double,
    val rewardGems: Int,
    val progress: Double,
    val claimed: Boolean
) {
    val completed: Boolean get() = progress >= target
    val fraction: Float get() = min(1.0, progress / target).toFloat()
}

object ChallengeRotation {
    fun weeklyKey(date: LocalDate = LocalDate.now()): String {
        val wf = WeekFields.ISO
        return "${date.get(wf.weekBasedYear())}-W${date.get(wf.weekOfWeekBasedYear())}"
    }

    fun current(state: GameState, meta: PlayerMeta, date: LocalDate = LocalDate.now()): List<TimedChallenge> {
        val key = weeklyKey(date)
        val baselineReady = meta.challengeWeekKey == key
        fun claimed(suffix: String) = "$key:$suffix" in meta.claimedChallengeIds
        val weeklyTaps = if (baselineReady) (meta.totalTaps - meta.challengeWeekTapBase).coerceAtLeast(0L).toDouble() else 0.0
        val weeklyPurchases = if (baselineReady) (meta.totalPurchases - meta.challengeWeekPurchaseBase).coerceAtLeast(0L).toDouble() else 0.0
        val weeklyPrestiges = if (baselineReady) (meta.prestigeCount - meta.challengeWeekPrestigeBase).coerceAtLeast(0).toDouble() else 0.0
        return listOf(
            TimedChallenge("$key:tap", "Tap Storm", "Generate capital manually 500 times this week.", ChallengeMetric.TAPS, 500.0, 20, weeklyTaps, claimed("tap")),
            TimedChallenge("$key:scale", "Scale Up", "Purchase 150 business levels this week.", ChallengeMetric.PURCHASES, 150.0, 30, weeklyPurchases, claimed("scale")),
            TimedChallenge("$key:wealth", "Capital Surge", "Reach 10M lifetime cash in the current run.", ChallengeMetric.LIFETIME_CASH, 10_000_000.0, 40, state.lifetimeCash, claimed("wealth")),
            TimedChallenge("$key:ascend", "Legacy Run", "Complete 2 ascensions this week.", ChallengeMetric.PRESTIGES, 2.0, 50, weeklyPrestiges, claimed("ascend"))
        )
    }
}

object BalanceGuard {
    fun recommendedPrestigeWindowSeconds(lifetimeCash: Double): Long = when {
        lifetimeCash < 1e6 -> 900L
        lifetimeCash < 1e9 -> 1_800L
        lifetimeCash < 1e12 -> 3_600L
        lifetimeCash < 1e15 -> 7_200L
        else -> 10_800L
    }

    fun economyHealth(state: GameState): Double {
        if (state.incomePerSecond <= 0.0) return 0.0
        val nextAffordable = state.businesses.minOfOrNull { it.nextCost } ?: return 0.0
        return (state.incomePerSecond / nextAffordable).coerceIn(0.0, 1.0)
    }
}
