package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class AmbientTrafficMotionTest {
    @Test
    fun `reduced motion freezes traffic in place`() {
        val sample = ambientTrafficMotion(
            worldFrame = 123,
            phaseFrames = 47,
            travelX = .12f,
            travelY = .07f,
            reducedMotion = true,
        )
        assertEquals(0f, sample.deltaX, 0f)
        assertEquals(0f, sample.deltaY, 0f)
        assertEquals(.92f, sample.alpha, 0f)
    }

    @Test
    fun `traffic motion repeats every 180 frames`() {
        val a = ambientTrafficMotion(31, 17, .12f, .07f, false)
        val b = ambientTrafficMotion(31 + 180, 17, .12f, .07f, false)
        assertEquals(a.deltaX, b.deltaX, 0f)
        assertEquals(a.deltaY, b.deltaY, 0f)
        assertEquals(a.alpha, b.alpha, 0f)
    }

    @Test
    fun `traffic alpha remains visible and bounded`() {
        repeat(180) { frame ->
            val sample = ambientTrafficMotion(frame, 0, .12f, .07f, false)
            assertTrue(sample.alpha in 0.60f..0.98f)
            assertTrue(sample.deltaX in -0.061f..0.061f)
            assertTrue(sample.deltaY in -0.036f..0.036f)
        }
    }
}
