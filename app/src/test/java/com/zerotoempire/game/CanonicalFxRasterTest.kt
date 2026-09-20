package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class CanonicalFxRasterTest {
    @Test
    fun `ambient world maps reviewed historical effects to visible eras`() {
        assertEquals(
            listOf(CanonicalFx.SMALL_FURNACE_FLAME, CanonicalFx.INDUSTRIAL_SMOKE_PUFF),
            ambientProductionFx(0),
        )
        assertEquals(
            listOf(CanonicalFx.LARGE_PLASMA_FLAME, CanonicalFx.INDUSTRIAL_SMOKE_PUFF),
            ambientProductionFx(4),
        )
        assertEquals(
            listOf(CanonicalFx.MASTERY_CROWN_SHIMMER),
            ambientProductionFx(9),
        )
    }

    @Test
    fun `all manifest authored effects resolve to their production sprite ids`() {
        val expected = mapOf(
            CanonicalFx.WELDING_SPARK_BURST to R.drawable.zte_fx_00_final,
            CanonicalFx.SMALL_FURNACE_FLAME to R.drawable.zte_fx_01_final,
            CanonicalFx.LARGE_PLASMA_FLAME to R.drawable.zte_fx_02_final,
            CanonicalFx.INDUSTRIAL_SMOKE_PUFF to R.drawable.zte_fx_03_final,
            CanonicalFx.STEAM_VENT to R.drawable.zte_fx_04_final,
            CanonicalFx.CYAN_ENERGY_PULSE to R.drawable.zte_fx_05_final,
            CanonicalFx.WARM_ENERGY_PULSE to R.drawable.zte_fx_06_final,
            CanonicalFx.CONSTRUCTION_DUST_BURST to R.drawable.zte_fx_07_final,
            CanonicalFx.UPGRADE_CONSTRUCTION_FLASH to R.drawable.zte_fx_08_final,
            CanonicalFx.INCOME_PICKUP_SPARKLE to R.drawable.zte_fx_09_final,
            CanonicalFx.ELECTRIC_ARC to R.drawable.zte_fx_10_final,
            CanonicalFx.HOLOGRAM_SCAN_SWEEP to R.drawable.zte_fx_11_final,
            CanonicalFx.DRONE_THRUSTER to R.drawable.zte_fx_12_final,
            CanonicalFx.PHASE_DISTORTION to R.drawable.zte_fx_13_final,
            CanonicalFx.ORBITAL_ION_TRAIL to R.drawable.zte_fx_14_final,
            CanonicalFx.STELLAR_FLARE to R.drawable.zte_fx_15_final,
            CanonicalFx.SINGULARITY_LENS_PULSE to R.drawable.zte_fx_16_final,
            CanonicalFx.MASTERY_CROWN_SHIMMER to R.drawable.zte_fx_17_final,
        )

        assertEquals(CanonicalFx.entries.toSet(), expected.keys)
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
