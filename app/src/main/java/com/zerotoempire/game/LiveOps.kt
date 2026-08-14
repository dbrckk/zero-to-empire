package com.zerotoempire.game

import java.time.DayOfWeek
import java.time.LocalDate

data class LiveEvent(
    val id: String,
    val name: String,
    val description: String,
    val incomeMultiplier: Double,
    val icon: String
)

object LiveOps {
    fun currentEvent(date: LocalDate = LocalDate.now()): LiveEvent? = when (date.dayOfWeek) {
        DayOfWeek.FRIDAY -> LiveEvent("friday_rush", "Friday Rush", "Global profits are doubled today.", 2.0, "⚡")
        DayOfWeek.SATURDAY -> LiveEvent("golden_saturday", "Golden Saturday", "Build your empire with +50% production.", 1.5, "✨")
        DayOfWeek.SUNDAY -> LiveEvent("legacy_sunday", "Legacy Sunday", "Prestige runs generate faster progress.", 1.35, "👑")
        else -> null
    }
}

data class DailyQuest(
    val id: String,
    val label: String,
    val target: Int,
    val rewardGems: Int
)

object DailyQuests {
    val quests = listOf(
        DailyQuest("tap_daily", "Make 100 power taps", 100, 5),
        DailyQuest("buy_daily", "Buy 30 business levels", 30, 7),
        DailyQuest("boost_daily", "Activate a profit boost", 1, 8)
    )
}
