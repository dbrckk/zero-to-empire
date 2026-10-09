package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class AmbientCharacterMotionTest {
    private val walk = ReviewedCharacterAction.WALK
    private val work = ReviewedCharacterAction.WORK

    @Test
    fun `walk moves through its lane rather than marching in place`() {
        val first = ambientCharacterMotion(walk, 0, 0, .18f, false)
        val middle = ambientCharacterMotion(walk, 40, 0, .18f, false)
        val end = ambientCharacterMotion(walk, 80, 0, .18f, false)
        assertEquals(-.09f, first.xOffsetFraction, 0.0001f)
        assertEquals(0f, middle.xOffsetFraction, 0.0001f)
        assertEquals(.09f, end.xOffsetFraction, 0.0001f)
        assertFalse(first.facingLeft)
        assertTrue(ambientCharacterMotion(walk, 84, 0, .18f, false).facingLeft)
    }

    @Test
    fun `all adjacent world frames have continuous bounded displacement and phase`() {
        val snapshots = (0..336).map { frame ->
            ambientCharacterMotion(walk, frame, 7, .18f, false)
        }
        snapshots.zipWithNext().forEach { (a,b) ->
            assertTrue(kotlin.math.abs(a.xOffsetFraction - b.xOffsetFraction) <= .00226f)
            assertTrue(a.spriteFrame in 0..7)
            assertTrue(b.spriteFrame in 0..7)
            assertTrue(a.xOffsetFraction in -.0901f.. .0901f)
        }
        assertEquals(snapshots[0], snapshots[168])
        assertEquals(snapshots[0], snapshots[336])
    }

    @Test
    fun `turnaround freezes the sprite until facing direction changes`() {
        for (frame in 80..83) {
            val moment = ambientCharacterMotion(walk, frame, 0, .12f, false)
            assertEquals(0, moment.spriteFrame)
            assertFalse(moment.facingLeft)
            assertEquals(.06f, moment.xOffsetFraction, .00001f)
        }
        for (frame in 164..167) {
            val moment = ambientCharacterMotion(walk, frame, 0, .12f, false)
            assertEquals(0, moment.spriteFrame)
            assertTrue(moment.facingLeft)
            assertEquals(-.06f, moment.xOffsetFraction, .00001f)
        }
    }

    @Test
    fun `reduced motion freezes travel and source atlas pose`() {
        val first = ambientCharacterMotion(walk, 0, 5, .2f, true)
        for (frame in listOf(1, 15, 80, 167, 300_000)) {
            assertEquals(first, ambientCharacterMotion(walk, frame, 5, .2f, true))
        }
        assertEquals(0f, first.xOffsetFraction, 0f)
        assertFalse(first.facingLeft)
    }

    @Test
    fun `stationary actions animate without drifting through buildings`() {
        for (frame in -10..150) {
            val moment = ambientCharacterMotion(work, frame, 4, .2f, false)
            assertEquals(0f, moment.xOffsetFraction, 0f)
            assertEquals(Math.floorMod(frame + 4, 10), moment.spriteFrame)
            assertFalse(moment.facingLeft)
        }
    }

    @Test
    fun `nonpositive travel amplitude cannot create fake walking movement`() {
        for (amplitude in listOf(0f, -.1f)) {
            val moment = ambientCharacterMotion(walk, 73, 2, amplitude, false)
            assertEquals(0f, moment.xOffsetFraction, 0f)
            assertEquals(Math.floorMod(75, 8), moment.spriteFrame)
        }
    }
}
