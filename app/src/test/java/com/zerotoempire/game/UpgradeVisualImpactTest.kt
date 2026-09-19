package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test

class UpgradeVisualImpactTest {
    @Test
    fun `initial or non-increasing levels produce no upgrade impact`() {
        assertEquals(UpgradeVisualImpact.NONE, upgradeVisualImpact(0, 0))
        assertEquals(UpgradeVisualImpact.NONE, upgradeVisualImpact(25, 25))
        assertEquals(UpgradeVisualImpact.NONE, upgradeVisualImpact(50, 49))
    }

    @Test
    fun `ordinary purchases use level impact`() {
        assertEquals(UpgradeVisualImpact.LEVEL, upgradeVisualImpact(1, 2))
        assertEquals(UpgradeVisualImpact.LEVEL, upgradeVisualImpact(10, 24))
        assertEquals(UpgradeVisualImpact.LEVEL, upgradeVisualImpact(500, 999))
    }

    @Test
    fun `canonical tier crossings use tier impact`() {
        val boundaries = listOf(
            9 to 10,
            24 to 25,
            49 to 50,
            99 to 100,
            249 to 250,
            499 to 500,
        )
        boundaries.forEach { (from, to) ->
            assertEquals("$from->$to", UpgradeVisualImpact.TIER, upgradeVisualImpact(from, to))
        }
    }

    @Test
    fun `bulk purchases crossing multiple tiers still use one tier impact`() {
        assertEquals(UpgradeVisualImpact.TIER, upgradeVisualImpact(8, 260))
        assertEquals(UpgradeVisualImpact.TIER, upgradeVisualImpact(20, 600))
    }

    @Test
    fun `first crossing of level 1000 is mastery impact`() {
        assertEquals(UpgradeVisualImpact.MASTERY, upgradeVisualImpact(999, 1000))
        assertEquals(UpgradeVisualImpact.MASTERY, upgradeVisualImpact(500, 1200))
        assertEquals(UpgradeVisualImpact.LEVEL, upgradeVisualImpact(1000, 1001))
    }
}
