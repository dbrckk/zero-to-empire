package com.zerotoempire.game

import kotlin.math.pow

data class Business(
    val id: Int,
    val name: String,
    val emoji: String,
    val baseCost: Double,
    val baseIncome: Double,
    val level: Int = 0
) {
    val nextCost: Double get() = baseCost * 1.15.pow(level)
    val incomePerSecond: Double get() = baseIncome * level * GameEconomy.milestoneMultiplier(level)
    val nextMilestone: Int? get() = listOf(25, 50, 100, 250, 500, 1000).firstOrNull { it > level }
}

data class GameState(
    val cash: Double = 10.0,
    val lifetimeCash: Double = 10.0,
    val prestigePoints: Int = 0,
    val businesses: List<Business> = defaultBusinesses()
) {
    val prestigeMultiplier: Double get() = 1.0 + prestigePoints * 0.12
    val incomePerSecond: Double get() = businesses.sumOf { it.incomePerSecond } * prestigeMultiplier
    val empireLevel: Int get() = when {
        lifetimeCash >= 1e18 -> 7
        lifetimeCash >= 1e15 -> 6
        lifetimeCash >= 1e12 -> 5
        lifetimeCash >= 1e9 -> 4
        lifetimeCash >= 1e6 -> 3
        lifetimeCash >= 1e3 -> 2
        lifetimeCash >= 100 -> 1
        else -> 0
    }
}

fun defaultBusinesses() = listOf(
    Business(0, "Street Stand", "☕", 10.0, 1.0),
    Business(1, "Corner Shop", "🏪", 120.0, 8.0),
    Business(2, "Workshop", "🔧", 1_500.0, 70.0),
    Business(3, "Factory", "🏭", 25_000.0, 900.0),
    Business(4, "Tech Company", "💻", 500_000.0, 15_000.0),
    Business(5, "Megacity", "🌆", 15_000_000.0, 400_000.0),
    Business(6, "Moon Colony", "🌕", 800_000_000.0, 18_000_000.0),
    Business(7, "Mars Empire", "🔴", 75_000_000_000.0, 1_200_000_000.0),
    Business(8, "Dyson Network", "☀️", 12_000_000_000_000.0, 160_000_000_000.0),
    Business(9, "Galactic Exchange", "🌌", 4_000_000_000_000_000.0, 35_000_000_000_000.0)
)
