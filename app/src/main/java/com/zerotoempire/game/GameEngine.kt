package com.zerotoempire.game

import java.time.LocalDate
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
    val rawIncomePerSecond: Double get() = baseIncome * level * GameEconomy.milestoneMultiplier(level)
    val nextMilestone: Int? get() = listOf(10, 25, 50, 100, 250, 500, 1000).firstOrNull { it > level }
}

data class GameState(
    val cash: Double = 10.0,
    val lifetimeCash: Double = 10.0,
    val prestigePoints: Int = 0,
    val businesses: List<Business> = defaultBusinesses(),
    val hiredManagerIds: Set<Int> = emptySet(),
    val upgradeRanks: Map<String, Int> = emptyMap(),
    val gems: Int = 0,
    val boostEndsAtMillis: Long = 0L
) {
    val prestigeUpgradeRank: Int get() = upgradeRanks["prestige"] ?: 0
    val incomeUpgradeRank: Int get() = upgradeRanks["income"] ?: 0
    val tapUpgradeRank: Int get() = upgradeRanks["tap"] ?: 0
    val prestigeMultiplier: Double get() = 1.0 + prestigePoints * (0.12 * (1.0 + prestigeUpgradeRank * .08))
    val legacyMasteryMultiplier: Double get() = LateGame.legacyMasteryMultiplier(prestigePoints)
    val portfolioDepthMultiplier: Double get() = LateGame.portfolioDepthMultiplier(businesses)
    val transcendenceMultiplier: Double get() = EndgameProgression.transcendenceMultiplier(lifetimeCash)
    val globalUpgradeMultiplier: Double get() = 1.0 + incomeUpgradeRank * .10
    val boostMultiplier: Double get() = if (System.currentTimeMillis() < boostEndsAtMillis) 2.0 else 1.0
    val eventMultiplier: Double get() = LiveOps.currentEvent(LocalDate.now())?.incomeMultiplier ?: 1.0

    fun businessIncome(b: Business): Double {
        val manager = Managers.catalog.firstOrNull { it.businessId == b.id && it.businessId in hiredManagerIds }
        return b.rawIncomePerSecond * (manager?.incomeMultiplier ?: 1.0)
    }

    private val globalIncomeMultiplier: Double
        get() = prestigeMultiplier * legacyMasteryMultiplier * portfolioDepthMultiplier * transcendenceMultiplier * globalUpgradeMultiplier * boostMultiplier * eventMultiplier

    /** All owned businesses generate while the player is active. */
    val incomePerSecond: Double get() = businesses.sumOf(::businessIncome) * globalIncomeMultiplier

    /** Only manager-operated businesses continue generating while the app is away. */
    val automatedIncomePerSecond: Double
        get() = businesses.filter { it.id in hiredManagerIds }.sumOf(::businessIncome) * globalIncomeMultiplier

    val tapValue: Double get() = (1.0 + incomePerSecond * .05) * prestigeMultiplier * legacyMasteryMultiplier * transcendenceMultiplier * (1.0 + tapUpgradeRank * .25)
    val empireLevel: Int get() = EmpireEras.current(lifetimeCash).index
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
    Business(9, "Galactic Exchange", "🌌", 4.0e15, 3.5e13),
    Business(10, "Intergalactic Gateway", "◎", 2.0e18, 1.8e16),
    Business(11, "Cosmic Foundry", "◇", 8.0e21, 8.5e19),
    Business(12, "Reality Engine", "✦", 3.0e25, 4.2e23),
    Business(13, "Transcendent Nexus", "✧", 1.2e29, 2.4e27)
)
