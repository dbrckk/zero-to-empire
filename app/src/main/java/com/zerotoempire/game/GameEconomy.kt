package com.zerotoempire.game

/**
 * Central deterministic economy rules.
 * Keep balance formulas here so gameplay, offline progress and tests use the same model.
 */
object GameEconomy {
    private val milestones = listOf(
        1000 to 128.0,
        500 to 64.0,
        250 to 32.0,
        100 to 16.0,
        50 to 8.0,
        25 to 4.0,
        10 to 2.0
    )

    fun milestoneMultiplier(level: Int): Double =
        milestones.firstOrNull { (requiredLevel, _) -> level >= requiredLevel }?.second ?: 1.0
}
