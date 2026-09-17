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
    SMALL_FURNACE_FLAME,
    LARGE_PLASMA_FLAME,
    INDUSTRIAL_SMOKE_PUFF,
    STEAM_VENT,
    CYAN_ENERGY_PULSE,
    WARM_ENERGY_PULSE,
    CONSTRUCTION_DUST_BURST,
    UPGRADE_CONSTRUCTION_FLASH,
    INCOME_PICKUP_SPARKLE,
    ELECTRIC_ARC,
    HOLOGRAM_SCAN_SWEEP,
    DRONE_THRUSTER,
    PHASE_DISTORTION,
    ORBITAL_ION_TRAIL,
    STELLAR_FLARE,
    SINGULARITY_LENS_PULSE,
    MASTERY_CROWN_SHIMMER,
}

internal fun canonicalFxRasterRes(effect: CanonicalFx): Int = when (effect) {
    CanonicalFx.WELDING_SPARK_BURST -> R.drawable.zte_fx_00_final
    CanonicalFx.SMALL_FURNACE_FLAME -> R.drawable.zte_fx_01_final
    CanonicalFx.LARGE_PLASMA_FLAME -> R.drawable.zte_fx_02_final
    CanonicalFx.INDUSTRIAL_SMOKE_PUFF -> R.drawable.zte_fx_03_final
    CanonicalFx.STEAM_VENT -> R.drawable.zte_fx_04_final
    CanonicalFx.CYAN_ENERGY_PULSE -> R.drawable.zte_fx_05_final
    CanonicalFx.WARM_ENERGY_PULSE -> R.drawable.zte_fx_06_final
    CanonicalFx.CONSTRUCTION_DUST_BURST -> R.drawable.zte_fx_07_final
    CanonicalFx.UPGRADE_CONSTRUCTION_FLASH -> R.drawable.zte_fx_08_final
    CanonicalFx.INCOME_PICKUP_SPARKLE -> R.drawable.zte_fx_09_final
    CanonicalFx.ELECTRIC_ARC -> R.drawable.zte_fx_10_final
    CanonicalFx.HOLOGRAM_SCAN_SWEEP -> R.drawable.zte_fx_11_final
    CanonicalFx.DRONE_THRUSTER -> R.drawable.zte_fx_12_final
    CanonicalFx.PHASE_DISTORTION -> R.drawable.zte_fx_13_final
    CanonicalFx.ORBITAL_ION_TRAIL -> R.drawable.zte_fx_14_final
    CanonicalFx.STELLAR_FLARE -> R.drawable.zte_fx_15_final
    CanonicalFx.SINGULARITY_LENS_PULSE -> R.drawable.zte_fx_16_final
    CanonicalFx.MASTERY_CROWN_SHIMMER -> R.drawable.zte_fx_17_final
}

internal fun powerCorePulseFx(eraIndex: Int): CanonicalFx? = when (eraIndex) {
    in 0..2 -> CanonicalFx.WARM_ENERGY_PULSE
    in 3..5 -> CanonicalFx.CYAN_ENERGY_PULSE
    in 6..8 -> null
    else -> CanonicalFx.WARM_ENERGY_PULSE
}
