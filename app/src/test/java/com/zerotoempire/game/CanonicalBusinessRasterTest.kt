package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class CanonicalBusinessRasterTest {
    private val milestoneLevels = listOf(0, 10, 25, 50, 100, 250, 500, 1000)
    private val canonicalBusinesses = (0..13).toList()

    @Test
    fun `all authored businesses resolve every gameplay milestone`() {
        canonicalBusinesses.forEach { businessId ->
            milestoneLevels.forEach { level ->
                val resource = canonicalBusinessRasterRes(businessId, level)
                assertTrue("business=$businessId level=$level must resolve", resource != null && resource != 0)
            }
        }
    }

    @Test
    fun `final two gameplay milestones intentionally share T6`() {
        canonicalBusinesses.forEach { businessId ->
            assertEquals(
                canonicalBusinessRasterRes(businessId, 500),
                canonicalBusinessRasterRes(businessId, 1000)
            )
        }
    }

    @Test
    fun `ids outside authored business catalog remain unsupported`() {
        assertNull(canonicalBusinessRasterRes(-1, 500))
        assertNull(canonicalBusinessRasterRes(14, 500))
    }

    @Test
    fun `tiers produce seven distinct resources per canonical business`() {
        canonicalBusinesses.forEach { businessId ->
            val resources = listOf(0, 10, 25, 50, 100, 250, 500)
                .map { canonicalBusinessRasterRes(businessId, it) }
            assertEquals("business=$businessId", 7, resources.toSet().size)
        }
    }
}
