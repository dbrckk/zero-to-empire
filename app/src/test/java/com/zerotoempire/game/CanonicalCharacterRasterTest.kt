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
    fun `all reviewed character action sheets resolve to distinct packaged assets`() {
        val resources = ReviewedCharacterRole.entries.flatMap { role ->
            ReviewedCharacterAction.entries.map { action ->
                reviewedCharacterRasterRes(role, action)
            }
        }
        assertEquals(
            ReviewedCharacterRole.entries.size * ReviewedCharacterAction.entries.size,
            resources.toSet().size,
        )
        resources.forEach { assertNotEquals(0, it) }
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
    fun `character atlas contract matches production sheets`() {
        assertEquals(1024, REVIEWED_CHARACTER_ATLAS_SIDE)
        assertEquals(256, REVIEWED_CHARACTER_CELL_SIDE)
        assertEquals(4, REVIEWED_CHARACTER_COLUMNS)
        assertEquals(4, REVIEWED_CHARACTER_ROWS)
        assertEquals(
            REVIEWED_CHARACTER_ATLAS_SIDE,
            REVIEWED_CHARACTER_CELL_SIDE * REVIEWED_CHARACTER_COLUMNS,
        )
        assertEquals(
            REVIEWED_CHARACTER_ATLAS_SIDE,
            REVIEWED_CHARACTER_CELL_SIDE * REVIEWED_CHARACTER_ROWS,
        )
    }

    @Test
    fun `ambient population only loops actions documented as continuous`() {
        assertEquals(
            setOf(ReviewedCharacterAction.IDLE, ReviewedCharacterAction.WALK, ReviewedCharacterAction.WORK),
            ReviewedCharacterAction.entries.filter(::reviewedCharacterActionLoopsAmbiently).toSet(),
        )
    }
}
