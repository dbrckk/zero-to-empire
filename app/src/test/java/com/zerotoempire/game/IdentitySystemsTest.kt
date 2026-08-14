package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class IdentitySystemsTest {
    @Test
    fun eraProgressionIsStrictlyIncreasing() {
        val thresholds = EmpireEras.catalog.map { it.requiredLifetimeCash }
        assertEquals(thresholds.sorted(), thresholds)
        assertEquals(thresholds.distinct().size, thresholds.size)
    }

    @Test
    fun currentEraMatchesThresholds() {
        assertEquals("SCRAPPY START", EmpireEras.current(0.0).name)
        assertEquals("LOCAL HUSTLE", EmpireEras.current(1_000.0).name)
        assertEquals("INDUSTRIAL AGE", EmpireEras.current(1_000_000.0).name)
        assertEquals("GALACTIC", EmpireEras.current(1e18).name)
    }

    @Test
    fun viralMilestonesUnlockInOrder() {
        assertNull(ViralMilestones.latestUnlocked(999_999.0))
        assertEquals("million", ViralMilestones.latestUnlocked(1e6)?.id)
        assertEquals("billion", ViralMilestones.latestUnlocked(1e9)?.id)
        assertEquals("galaxy", ViralMilestones.latestUnlocked(1e18)?.id)
        assertTrue(ViralMilestones.catalog.zipWithNext().all { (a, b) -> a.minimumLifetimeCash < b.minimumLifetimeCash })
    }
}
