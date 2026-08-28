package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class DynastyProgressionTest {
    @Test
    fun ranks_are_monotonic_and_start_at_zero_requirement() {
        val ranks = DynastyProgression.ranks
        assertEquals(DynastyProgression.MAX_RANK, ranks.size)
        assertEquals(0.0, ranks.first().renownRequired, 0.0)
        assertEquals((1..DynastyProgression.MAX_RANK).toList(), ranks.map { it.level })
        ranks.zipWithNext().forEach { (a, b) ->
            assertTrue("rank thresholds must increase", b.renownRequired > a.renownRequired)
        }
    }

    @Test
    fun fresh_save_starts_at_rank_one() {
        val status = DynastyProgression.status(GameState(), PlayerMeta())
        assertEquals(1, status.rank.level)
        assertTrue(status.progress in 0f..1f)
    }

    @Test
    fun persistent_career_stats_raise_dynasty_rank() {
        val fresh = DynastyProgression.status(GameState(), PlayerMeta()).rank.level
        val veteranState = GameState(prestigePoints = 50_000)
        val veteranMeta = PlayerMeta(
            totalTaps = 100_000,
            totalPurchases = 50_000,
            prestigeCount = 150,
            streakDays = 90,
            highestEraSeen = 10
        )
        val veteran = DynastyProgression.status(veteranState, veteranMeta)
        assertTrue(veteran.rank.level > fresh)
        assertTrue(veteran.renown > 0.0)
    }

    @Test
    fun dynasty_status_never_exceeds_rank_cap() {
        val extremeState = GameState(prestigePoints = Int.MAX_VALUE)
        val extremeMeta = PlayerMeta(
            totalTaps = Long.MAX_VALUE,
            totalPurchases = Long.MAX_VALUE,
            prestigeCount = Int.MAX_VALUE,
            streakDays = Int.MAX_VALUE,
            highestEraSeen = Int.MAX_VALUE
        )
        val status = DynastyProgression.status(extremeState, extremeMeta)
        assertEquals(DynastyProgression.MAX_RANK, status.rank.level)
        assertEquals(1f, status.progress, 0f)
    }
}
