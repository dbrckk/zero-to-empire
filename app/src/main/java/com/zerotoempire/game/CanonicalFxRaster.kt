package com.zerotoempire.game

/**
 * Semantic contract for authored production VFX.
 *
 * Keep gameplay code coupled to an effect meaning rather than opaque numbered
 * sprite sheets. Every entry resolves to one distinct final packaged raster.
 */
internal enum class CanonicalFx {
    COIN_BURST,
    MONEY_RAIN,
    RANK_UP_FLARE,
    RING_PULSE,
    SPARK,
    STARBURST,
}

internal fun canonicalFxRasterRes(effect: CanonicalFx): Int = when (effect) {
    CanonicalFx.COIN_BURST -> R.drawable.zte_fx_coin_burst_final
    CanonicalFx.MONEY_RAIN -> R.drawable.zte_fx_money_rain_final
    CanonicalFx.RANK_UP_FLARE -> R.drawable.zte_fx_rank_up_flare_final
    CanonicalFx.RING_PULSE -> R.drawable.zte_fx_ring_pulse_final
    CanonicalFx.SPARK -> R.drawable.zte_fx_spark_final
    CanonicalFx.STARBURST -> R.drawable.zte_fx_starburst_final
}
