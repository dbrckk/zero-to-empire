package com.zerotoempire.game

import kotlin.math.floor
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
    val unlocked: Boolean = false,
    val claimed: Boolean = false,
    val rewardGems: Int = 10
)

data class PlayerMeta(
    val gems: Int = 0,
    val totalTaps: Long = 0,
    val totalPurchases: Long = 0,
    val prestigeCount: Int = 0,
    val streakDays: Int = 0,
    val lastDailyClaimEpochDay: Long = -1L,
    val boostEndsAtMillis: Long = 0L,
    val claimedMissionIds: Set<String> = emptySet(),
    val claimedAchievementIds: Set<String> = emptySet(),
    val claimedChallengeIds: Set<String> = emptySet(),
    val challengeWeekKey: String = "",
    val challengeWeekTapBase: Long = 0L,
    val challengeWeekPurchaseBase: Long = 0L,
    val challengeWeekPrestigeBase: Int = 0,
    val onboardingCompleted: Boolean = false,
    val highestEraSeen: Int = 0,
    val adsRemoved: Boolean = false,
    val starterPackOwned: Boolean = false
)

object Progression {
    fun prestigeReward(lifetimeCash: Double): Int {
        if (lifetimeCash.isNaN() || lifetimeCash <= 0.0) return 0
        if (lifetimeCash == Double.POSITIVE_INFINITY) return Int.MAX_VALUE
        val reward = floor((lifetimeCash.coerceAtMost(EconomyMath.MAX_VALUE) / 1_000_000.0).pow(0.42))
        if (!reward.isFinite() || reward >= Int.MAX_VALUE.toDouble()) return Int.MAX_VALUE
        return reward.toInt().coerceAtLeast(0)
    }

    /**
     * Produces the next run after an ascension. Run-local cash, lifetime cash,
     * business levels and managers reset. Premium/permanent currency, upgrades,
     * accumulated legacy points and an already-earned timed boost survive.
     * Returns null when the run has not earned any additional legacy point.
     */
    fun prestigeReset(state: GameState): GameState? {
        val totalPoints = prestigeReward(state.lifetimeCash)
        if (totalPoints <= state.prestigePoints) return null
        return GameState(
            prestigePoints = totalPoints,
            gems = state.gems.coerceAtLeast(0),
            upgradeRanks = state.upgradeRanks,
            boostEndsAtMillis = state.boostEndsAtMillis.coerceAtLeast(0L)
        )
    }

    fun dailyReward(day: Int): Int = listOf(5, 7, 10, 15, 20, 30, 50)[day.coerceIn(0, 6)]

    fun missions(state: GameState, meta: PlayerMeta) = listOf(
        Mission("tap_50", "Tap 50 times", 50.0, 5, meta.totalTaps.toDouble(), "tap_50" in meta.claimedMissionIds),
        Mission("buy_25", "Buy 25 business levels", 25.0, 8, meta.totalPurchases.toDouble(), "buy_25" in meta.claimedMissionIds),
        Mission("earn_100k", "Earn 100K lifetime", 100_000.0, 12, state.lifetimeCash, "earn_100k" in meta.claimedMissionIds),
        Mission("prestige_1", "Ascend once", 1.0, 20, meta.prestigeCount.toDouble(), "prestige_1" in meta.claimedMissionIds)
    )

    fun achievements(state: GameState, meta: PlayerMeta): List<Achievement> {
        val ids = meta.claimedAchievementIds
        val totalLevels = state.businesses.sumOf { it.level.toLong() }
        val dynasty = DynastyProgression.status(state, meta).rank.level
        fun a(id: String, title: String, description: String, unlocked: Boolean, reward: Int) =
            Achievement(id, title, description, unlocked, id in ids, reward)

        return listOf(
            // First-session / early campaign
            a("first", "First Step", "Own your first asset", state.businesses.any { it.level > 0 }, 5),
            a("tap_500", "Hands On", "Tap the Power Core 500 times", meta.totalTaps >= 500L, 8),
            a("buy_100", "Builder", "Purchase 100 asset levels across your career", meta.totalPurchases >= 100L, 10),
            a("million", "Millionaire", "Earn 1M lifetime cash in a run", state.lifetimeCash >= 1e6, 10),
            a("century", "Industrial Machine", "Own 100 total asset levels in one run", totalLevels >= 100L, 15),
            a("manager_1", "Delegation", "Hire your first manager", state.hiredManagerIds.isNotEmpty(), 10),
            a("reborn", "Reborn", "Ascend for the first time", meta.prestigeCount > 0, 20),

            // Mid campaign
            a("tap_5000", "Capital Pulse", "Tap the Power Core 5,000 times", meta.totalTaps >= 5_000L, 15),
            a("buy_1000", "Mass Expansion", "Purchase 1,000 asset levels across your career", meta.totalPurchases >= 1_000L, 20),
            a("managers_5", "Executive Board", "Hire 5 managers in one run", state.hiredManagerIds.size >= 5, 20),
            a("levels_1000", "Vertical Integration", "Own 1,000 total asset levels in one run", totalLevels >= 1_000L, 25),
            a("prestige_10", "Iterative Empire", "Complete 10 ascensions", meta.prestigeCount >= 10, 30),
            a("streak_14", "Two Week Operator", "Maintain a 14 day login streak", meta.streakDays >= 14, 20),
            a("era_planetary", "Off-World Balance Sheet", "Reach the Planetary era", meta.highestEraSeen >= 4 || state.empireLevel >= 4, 25),

            // Long campaign
            a("tap_50000", "Human Metronome", "Tap the Power Core 50,000 times", meta.totalTaps >= 50_000L, 35),
            a("buy_10000", "Empire Logistics", "Purchase 10,000 asset levels across your career", meta.totalPurchases >= 10_000L, 40),
            a("prestige_50", "Legacy Engine", "Complete 50 ascensions", meta.prestigeCount >= 50, 50),
            a("streak_30", "Monthly Discipline", "Maintain a 30 day login streak", meta.streakDays >= 30, 40),
            a("era_galactic", "Galactic Balance Sheet", "Reach the Galactic era", meta.highestEraSeen >= 6 || state.empireLevel >= 6, 45),
            a("all_managers", "Board of Fourteen", "Hire every manager in one run", state.hiredManagerIds.size >= Managers.catalog.size, 60),

            // Dynasty ladder: persistent multi-month status targets
            a("dynasty_5", "Dynasty: Established", "Reach Dynasty Rank 5", dynasty >= 5, 15),
            a("dynasty_10", "Dynasty: Influential", "Reach Dynasty Rank 10", dynasty >= 10, 25),
            a("dynasty_20", "Dynasty: Dominant", "Reach Dynasty Rank 20", dynasty >= 20, 50),
            a("dynasty_30", "Dynasty: Sovereign", "Reach Dynasty Rank 30", dynasty >= 30, 75),
            a("dynasty_45", "Dynasty: Eternal", "Reach Dynasty Rank 45", dynasty >= 45, 120),
            a("dynasty_60", "Dynasty: Apex", "Reach the maximum Dynasty Rank 60", dynasty >= 60, 200),

            // Endgame
            a("prestige_250", "Century of Rebirths", "Complete 250 ascensions", meta.prestigeCount >= 250, 125),
            a("streak_90", "Quarter-Year Empire", "Maintain a 90 day login streak", meta.streakDays >= 90, 100),
            a("beyond_everything", "Beyond Everything", "Reach the Transcendent era and the current frontier of Zero → Empire", state.lifetimeCash >= 1e30 || meta.highestEraSeen >= EmpireEras.catalog.lastIndex, 150)
        )
    }
}
