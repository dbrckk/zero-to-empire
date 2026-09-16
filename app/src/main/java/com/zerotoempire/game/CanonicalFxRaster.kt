package com.zerotoempire.game

/**
 * Semantic contract for authored production VFX whose generation prompts are
 * documented in tools/sprites/hf_sprite_factory.py.
 *
 * Gameplay code uses effect meaning while this resolver owns the opaque
 * production asset ids. Do not add a semantic alias without a documented source.
 */
internal enum class CanonicalFx {
    WELDING_SPARK_BURST,
    CYAN_ENERGY_PULSE,
    WARM_ENERGY_PULSE,
    CONSTRUCTION_DUST_BURST,
}

internal fun canonicalFxRasterRes(effect: CanonicalFx): Int = when (effect) {
    CanonicalFx.WELDING_SPARK_BURST -> R.drawable.zte_fx_00_final
    CanonicalFx.CYAN_ENERGY_PULSE -> R.drawable.zte_fx_05_final
    CanonicalFx.WARM_ENERGY_PULSE -> R.drawable.zte_fx_06_final
    CanonicalFx.CONSTRUCTION_DUST_BURST -> R.drawable.zte_fx_07_final
}

internal fun powerCorePulseFx(eraIndex: Int): CanonicalFx? = when (eraIndex) {
    in 0..2 -> CanonicalFx.WARM_ENERGY_PULSE
    in 3..5 -> CanonicalFx.CYAN_ENERGY_PULSE
    in 6..8 -> null
    else -> CanonicalFx.WARM_ENERGY_PULSE
}
