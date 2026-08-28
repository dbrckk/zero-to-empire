package com.zerotoempire.game

import kotlin.math.ln
import kotlin.math.sqrt

/**
 * Long-horizon campaign progression built only from already-persisted player data.
 * It therefore works with every existing save without migrations.
 *
 * Dynasty is intentionally cosmetic/status progression for now: it gives the
 * player a months-long ladder without destabilising the tuned economy.
 */
data class DynastyRank(
    val level: Int,
    val title: String,
    val renownRequired: Double
)

data class DynastyStatus(
    val rank: DynastyRank,
    val next: DynastyRank?,
    val renown: Double,
    val progress: Float
)

object DynastyProgression {
    const val MAX_RANK = 60

    private val titles = listOf(
        "Street Spark", "Local Operator", "District Builder", "City Founder",
        "Industrial Architect", "Market Baron", "National Power", "Global Magnate",
        "Orbital Pioneer", "Planetary Governor", "Stellar Director", "System Sovereign",
        "Galactic Regent", "Cluster Chancellor", "Cosmic Architect", "Reality Broker",
        "Transcendent Founder", "Eternal Strategist", "Infinite Industrialist", "Empire Ascendant"
    )

    val ranks: List<DynastyRank> = (1..MAX_RANK).map { level ->
        DynastyRank(
            level = level,
            title = titleFor(level),
            renownRequired = threshold(level)
        )
    }

    /** Persistent campaign score. Every source survives ordinary ascensions. */
    fun renown(state: GameState, meta: PlayerMeta): Double {
        val legacy = sqrt(state.prestigePoints.coerceAtLeast(0).toDouble()) * 34.0
        val ascensions = sqrt(meta.prestigeCount.coerceAtLeast(0).toDouble()) * 38.0
        val purchases = ln(1.0 + meta.totalPurchases.coerceAtLeast(0).toDouble()) * 18.0
        val taps = ln(1.0 + meta.totalTaps.coerceAtLeast(0).toDouble()) * 7.0
        val eras = meta.highestEraSeen.coerceAtLeast(0) * 72.0
        val streak = sqrt(meta.streakDays.coerceAtLeast(0).toDouble()) * 9.0
        return (legacy + ascensions + purchases + taps + eras + streak).coerceAtLeast(0.0)
    }

    fun status(state: GameState, meta: PlayerMeta): DynastyStatus {
        val score = renown(state, meta)
        val current = ranks.lastOrNull { score >= it.renownRequired } ?: ranks.first()
        val next = ranks.getOrNull(current.level)
        val progress = if (next == null) 1f else {
            val span = (next.renownRequired - current.renownRequired).coerceAtLeast(1.0)
            ((score - current.renownRequired) / span).toFloat().coerceIn(0f, 1f)
        }
        return DynastyStatus(current, next, score, progress)
    }

    private fun threshold(level: Int): Double {
        if (level <= 1) return 0.0
        val n = level - 1.0
        return 32.0 * n * n + 16.0 * n * n * n / MAX_RANK
    }

    private fun titleFor(level: Int): String {
        val index = ((level - 1) * titles.size / MAX_RANK).coerceIn(0, titles.lastIndex)
        return titles[index]
    }
}
