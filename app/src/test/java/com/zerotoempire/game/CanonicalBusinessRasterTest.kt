package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class CanonicalBusinessRasterTest {
    private val milestoneLevels = listOf(0, 10, 25, 50, 100, 250, 500, 1000)
    private val canonicalGroup01Businesses = listOf(0, 1, 2, 3)

    @Test
    fun `all complete group01 businesses resolve every gameplay milestone`() {
        canonicalGroup01Businesses.forEach { businessId ->
            milestoneLevels.forEach { level ->
                val resource = canonicalBusinessRasterRes(businessId, level)
                assertTrue("business=$businessId level=$level must resolve", resource != null && resource != 0)
            }
        }
    }

    @Test
    fun `final two gameplay milestones intentionally share T6`() {
        canonicalGroup01Businesses.forEach { businessId ->
            assertEquals(
                canonicalBusinessRasterRes(businessId, 500),
                canonicalBusinessRasterRes(businessId, 1000)
            )
        }
    }

    @Test
    fun `businesses outside complete group01 set remain unsupported`() {
        assertNull(canonicalBusinessRasterRes(4, 500))
        assertNull(canonicalBusinessRasterRes(9, 500))
    }

    @Test
    fun `tiers produce seven distinct resources per canonical business`() {
        canonicalGroup01Businesses.forEach { businessId ->
            val resources = listOf(0, 10, 25, 50, 100, 250, 500)
                .map { canonicalBusinessRasterRes(businessId, it) }
            assertEquals(7, resources.toSet().size)
        }
    }
}
