package com.zerotoempire.game

import kotlin.math.pow

data class Business(
    val id: Int,
    val name: String,
    val emoji: String,
    val baseCost: Double,
    val baseIncome: Double,
    val level: Int = 0,
    val automated: Boolean = false
) {
    val nextCost: Double get() = baseCost * 1.15.pow(level)
    val incomePerSecond: Double get() = baseIncome * level * milestoneMultiplier
    private val milestoneMultiplier: Double
        get() = when {
            level >= 100 -> 10.0
            level >= 50 -> 5.0
            level >= 25 -> 2.0
            else -> 1.0
        }
}

data class GameState(
    val cash: Double = 10.0,
    val lifetimeCash: Double = 10.0,
    val prestigePoints: Int = 0,
    val businesses: List<Business> = defaultBusinesses()
) {
    val prestigeMultiplier: Double get() = 1.0 + prestigePoints * 0.1
    val incomePerSecond: Double get() = businesses.sumOf { it.incomePerSecond } * prestigeMultiplier
}

fun defaultBusinesses() = listOf(
    Business(0, "Street Stand", "☕", 10.0, 1.0),
    Business(1, "Corner Shop", "🏪", 120.0, 8.0),
    Business(2, "Workshop", "🔧", 1_500.0, 70.0),
    Business(3, "Factory", "🏭", 25_000.0, 900.0),
    Business(4, "Tech Company", "💻", 500_000.0, 15_000.0),
    Business(5, "Megacity", "🌆", 15_000_000.0, 400_000.0),
    Business(6, "Moon Colony", "🌕", 800_000_000.0, 18_000_000.0),
    Business(7, "Mars Empire", "🔴", 75_000_000_000.0, 1_200_000_000.0)
)
