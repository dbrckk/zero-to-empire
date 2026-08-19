package com.zerotoempire.game

import kotlin.math.min

data class RewardDay(val day: Int, val gems: Int, val multiplierMinutes: Int = 0, val special: String? = null)

object LoginCalendar {
    val sevenDay = listOf(
        RewardDay(1, 5), RewardDay(2, 7), RewardDay(3, 10, 5),
        RewardDay(4, 12), RewardDay(5, 15, 10), RewardDay(6, 20),
        RewardDay(7, 50, 30, "LEGENDARY CHEST")
    )
    fun rewardFor(streak: Int) = sevenDay[(streak.coerceAtLeast(1) - 1) % sevenDay.size]
}

data class ChestReward(val gems: Int, val boostMinutes: Int, val label: String)

object RewardChest {
    fun milestone(level: Int): ChestReward = when {
        level >= 1000 -> ChestReward(100, 60, "COSMIC VAULT")
        level >= 500 -> ChestReward(50, 30, "EMPIRE VAULT")
        level >= 100 -> ChestReward(20, 15, "GOLD VAULT")
        else -> ChestReward(5, 5, "SUPPLY DROP")
    }
}

data class OnboardingState(val step: Int = 0, val completed: Boolean = false) {
    fun advance(): OnboardingState {
        val next = min(step + 1, 5)
        return copy(step = next, completed = next >= 5)
    }
}

object OnboardingCopy {
    val steps = listOf(
        "Tap the core to generate your first capital.",
        "Buy your first asset. Assets generate income every second while you play.",
        "Scale assets to reach powerful milestone multipliers.",
        "Hire managers to boost production and keep their assets earning while you're away.",
        "Ascend when growth slows. Every legacy makes the next empire stronger."
    )
}
