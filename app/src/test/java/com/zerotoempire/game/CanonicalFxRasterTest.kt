package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class CanonicalFxRasterTest {
    @Test
    fun `verified authored effects resolve to their production sprite ids`() {
        val expected = mapOf(
            CanonicalFx.WELDING_SPARK_BURST to R.drawable.zte_fx_00_final,
            CanonicalFx.CYAN_ENERGY_PULSE to R.drawable.zte_fx_05_final,
            CanonicalFx.WARM_ENERGY_PULSE to R.drawable.zte_fx_06_final,
            CanonicalFx.CONSTRUCTION_DUST_BURST to R.drawable.zte_fx_07_final,
        )

        expected.forEach { (effect, resource) ->
            assertEquals(resource, canonicalFxRasterRes(effect))
            assertNotEquals(0, resource)
        }
    }

    @Test
    fun `verified semantic effects never silently share one sprite`() {
        val resources = CanonicalFx.entries.map(::canonicalFxRasterRes)
        assertEquals(CanonicalFx.entries.size, resources.toSet().size)
        assertTrue(resources.all { it != 0 })
    }

    @Test
    fun `power core only uses authored pulse colors that actually exist`() {
        assertEquals(CanonicalFx.WARM_ENERGY_PULSE, powerCorePulseFx(0))
        assertEquals(CanonicalFx.WARM_ENERGY_PULSE, powerCorePulseFx(2))
        assertEquals(CanonicalFx.CYAN_ENERGY_PULSE, powerCorePulseFx(3))
        assertEquals(CanonicalFx.CYAN_ENERGY_PULSE, powerCorePulseFx(5))
        assertNull(powerCorePulseFx(6))
        assertNull(powerCorePulseFx(8))
        assertEquals(CanonicalFx.WARM_ENERGY_PULSE, powerCorePulseFx(9))
    }

    @Test
    fun `sprite sheet progress selects exactly one of eight frames`() {
        assertEquals(0, canonicalFxFrameIndex(-1f))
        assertEquals(0, canonicalFxFrameIndex(0f))
        assertEquals(0, canonicalFxFrameIndex(.124f))
        assertEquals(1, canonicalFxFrameIndex(.125f))
        assertEquals(3, canonicalFxFrameIndex(.499f))
        assertEquals(4, canonicalFxFrameIndex(.5f))
        assertEquals(7, canonicalFxFrameIndex(.999f))
        assertEquals(7, canonicalFxFrameIndex(1f))
        assertEquals(7, canonicalFxFrameIndex(2f))
    }
}
