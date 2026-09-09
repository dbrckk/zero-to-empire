package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test

class CanonicalBusinessTierTest {
    @Test
    fun `eight gameplay milestones map monotonically to seven canonical tiers`() {
        val milestones = listOf(0, 10, 25, 50, 100, 250, 500, 1000)
        val expected = listOf(0, 1, 2, 3, 4, 5, 6, 6)
        assertEquals(expected, milestones.map(::canonicalBusinessTier))
    }

    @Test
    fun `tier boundaries are stable between milestones`() {
        val cases = mapOf(
            -1 to 0,
            9 to 0,
            10 to 1,
            24 to 1,
            25 to 2,
            49 to 2,
            50 to 3,
            99 to 3,
            100 to 4,
            249 to 4,
            250 to 5,
            499 to 5,
            500 to 6,
            999 to 6,
            1000 to 6,
            Int.MAX_VALUE to 6
        )
        cases.forEach { (level, tier) -> assertEquals("level=$level", tier, canonicalBusinessTier(level)) }
    }
}
