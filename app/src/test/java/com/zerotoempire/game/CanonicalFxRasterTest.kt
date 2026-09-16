package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class CanonicalFxRasterTest {
    @Test
    fun `all semantic effects resolve to final authored sprites`() {
        val expected = mapOf(
            CanonicalFx.COIN_BURST to R.drawable.zte_fx_coin_burst_final,
            CanonicalFx.MONEY_RAIN to R.drawable.zte_fx_money_rain_final,
            CanonicalFx.RANK_UP_FLARE to R.drawable.zte_fx_rank_up_flare_final,
            CanonicalFx.RING_PULSE to R.drawable.zte_fx_ring_pulse_final,
            CanonicalFx.SPARK to R.drawable.zte_fx_spark_final,
            CanonicalFx.STARBURST to R.drawable.zte_fx_starburst_final,
        )

        expected.forEach { (effect, resource) ->
            assertEquals(resource, canonicalFxRasterRes(effect))
            assertNotEquals(0, resource)
        }
    }

    @Test
    fun `semantic effects never silently share one sprite`() {
        val resources = CanonicalFx.entries.map(::canonicalFxRasterRes)
        assertEquals(CanonicalFx.entries.size, resources.toSet().size)
        assertTrue(resources.all { it != 0 })
    }
}
