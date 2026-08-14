package com.zerotoempire.game

import kotlin.math.floor
import kotlin.math.max
import kotlin.math.min
import kotlin.math.pow

data class Mission(
    val id: String,
    val title: String,
    val target: Double,
    val rewardGems: Int,
    val progress: Double = 0.0,
    val claimed: Boolean = false
) {
    val completed: Boolean get() = progress >= target
    val fraction: Float get() = min(1.0, progress / target).toFloat()
}

data class Achievement(
    val id: String,
    val title: String,
    val description: String,
    val unlocked: Boolean = false
)

data class PlayerMeta(
    val gems: Int = 0,
    val totalTaps: Long = 0,
    val totalPurchases: Long = 0,
    val prestigeCount: Int = 0,
    val streakDays: Int = 0,
    val lastDailyClaimEpochDay: Long = -1L,
    val boostEndsAtMillis: Long = 0L
)

object Progression {
    fun prestigeReward(lifetimeCash: Double): Int =
        floor((max(0.0, lifetimeCash) / 1_000_000.0).pow(0.42)).toInt()

    fun dailyReward(day: Int): Int = listOf(5, 7, 10, 15, 20, 30, 50)[day.coerceIn(0, 6)]

    fun initialMissions() = listOf(
        Mission("tap_50", "Tap 50 times", 50.0, 5),
        Mission("buy_25", "Buy 25 businesses", 25.0, 8),
        Mission("earn_100k", "Earn 100K", 100_000.0, 12)
    )

    fun achievements(state: GameState, meta: PlayerMeta) = listOf(
        Achievement("first", "First Step", "Own your first business", state.businesses.any { it.level > 0 }),
        Achievement("million", "Millionaire", "Earn 1M lifetime cash", state.lifetimeCash >= 1_000_000.0),
        Achievement("century", "Industrial Machine", "Own 100 total business levels", state.businesses.sumOf { it.level } >= 100),
        Achievement("reborn", "Reborn", "Prestige for the first time", meta.prestigeCount > 0)
    )
}
