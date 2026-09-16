package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Test

class CanonicalCharacterRasterTest {
    @Test
    fun `reviewed idle character roles resolve to packaged authored sprites`() {
        val expected = mapOf(
            ReviewedCharacterRole.OPERATOR to R.drawable.zte_chr_op_idle_final,
            ReviewedCharacterRole.TECHNICIAN to R.drawable.zte_chr_tech_idle_final,
            ReviewedCharacterRole.LOGISTICS to R.drawable.zte_chr_log_idle_final,
            ReviewedCharacterRole.ENGINEER to R.drawable.zte_chr_eng_idle_final,
        )

        expected.forEach { (role, resource) ->
            assertEquals(resource, reviewedCharacterIdleRasterRes(role))
            assertNotEquals(0, resource)
        }
    }

    @Test
    fun `reviewed idle roles never silently share one sprite`() {
        val resources = ReviewedCharacterRole.entries.map(::reviewedCharacterIdleRasterRes)
        assertEquals(ReviewedCharacterRole.entries.size, resources.toSet().size)
    }

    @Test
    fun `documented authored character actions keep their production frame counts`() {
        val expected = mapOf(
            ReviewedCharacterAction.IDLE to 6,
            ReviewedCharacterAction.WALK to 8,
            ReviewedCharacterAction.WORK to 10,
            ReviewedCharacterAction.CARRY to 8,
            ReviewedCharacterAction.REPAIR to 10,
            ReviewedCharacterAction.CELEBRATE to 8,
        )
        assertEquals(expected, ReviewedCharacterAction.entries.associateWith(::reviewedCharacterFrameCount))
    }

    @Test
    fun `ambient population only loops actions documented as continuous`() {
        assertEquals(
            setOf(ReviewedCharacterAction.IDLE, ReviewedCharacterAction.WALK, ReviewedCharacterAction.WORK),
            ReviewedCharacterAction.entries.filter(::reviewedCharacterActionLoopsAmbiently).toSet(),
        )
    }
}
