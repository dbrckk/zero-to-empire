package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class CanonicalBusinessRasterTest {
    private val milestoneLevels = listOf(0, 10, 25, 50, 100, 250, 500, 1000)

    @Test
    fun `BLD-02 and BLD-03 resolve every gameplay milestone`() {
        listOf(2, 3).forEach { businessId ->
            milestoneLevels.forEach { level ->
                val resource = canonicalBusinessRasterRes(businessId, level)
                assertTrue("business=$businessId level=$level must resolve", resource != null && resource != 0)
            }
        }
    }

    @Test
    fun `final two gameplay milestones intentionally share T6`() {
        listOf(2, 3).forEach { businessId ->
            assertEquals(
                canonicalBusinessRasterRes(businessId, 500),
                canonicalBusinessRasterRes(businessId, 1000)
            )
        }
    }

    @Test
    fun `unsupported group01 businesses remain on existing renderer`() {
        assertNull(canonicalBusinessRasterRes(0, 500))
        assertNull(canonicalBusinessRasterRes(1, 500))
        assertNull(canonicalBusinessRasterRes(4, 500))
    }

    @Test
    fun `tiers produce seven distinct resources per canonical business`() {
        listOf(2, 3).forEach { businessId ->
            val resources = listOf(0, 10, 25, 50, 100, 250, 500)
                .map { canonicalBusinessRasterRes(businessId, it) }
            assertEquals(7, resources.toSet().size)
        }
    }
}
