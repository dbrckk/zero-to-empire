package com.zerotoempire.game

import java.io.File
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class ReviewedTerrainLayerTest {
    @Test
    fun `reviewed terrain layer references every final terrain sprite`() {
        val relativePath = "src/main/java/com/zerotoempire/game/ReviewedTerrainLayer.kt"
        val source = listOf(File(relativePath), File("app/$relativePath"))
            .firstOrNull(File::exists)
            ?.readText()
            ?: error("Unable to locate ReviewedTerrainLayer.kt from ${System.getProperty("user.dir")}")

        val referencedIds = Regex("zte_terrain_(\\d{2})_final")
            .findAll(source)
            .map { it.groupValues[1].toInt() }
            .toSet()

        assertEquals((0..13).toSet(), referencedIds)
        assertTrue("TER-07 must be visible in the reviewed runtime layer", 7 in referencedIds)
    }
}
