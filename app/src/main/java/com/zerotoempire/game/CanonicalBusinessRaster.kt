package com.zerotoempire.game

/**
 * Resolves canonical tiered raster art for the complete Group 01 business set.
 *
 * Business IDs 0..3 are compile-time bound to every canonical T0..T6 production
 * drawable. Businesses outside that complete authored set return null so callers
 * can retain their existing procedural fallback until their own sprite family is
 * wired through the same contract.
 */
internal fun canonicalBusinessRasterRes(businessId: Int, level: Int): Int? {
    val tier = canonicalBusinessTier(level)
    return when (businessId) {
        0 -> when (tier) {
            0 -> R.drawable.zte_business_00_t0_final
            1 -> R.drawable.zte_business_00_t1_final
            2 -> R.drawable.zte_business_00_t2_final
            3 -> R.drawable.zte_business_00_t3_final
            4 -> R.drawable.zte_business_00_t4_final
            5 -> R.drawable.zte_business_00_t5_final
            6 -> R.drawable.zte_business_00_t6_final
            else -> error("canonicalBusinessTier returned unsupported tier $tier")
        }
        1 -> when (tier) {
            0 -> R.drawable.zte_business_01_t0_final
            1 -> R.drawable.zte_business_01_t1_final
            2 -> R.drawable.zte_business_01_t2_final
            3 -> R.drawable.zte_business_01_t3_final
            4 -> R.drawable.zte_business_01_t4_final
            5 -> R.drawable.zte_business_01_t5_final
            6 -> R.drawable.zte_business_01_t6_final
            else -> error("canonicalBusinessTier returned unsupported tier $tier")
        }
        2 -> when (tier) {
            0 -> R.drawable.zte_business_02_t0_final
            1 -> R.drawable.zte_business_02_t1_final
            2 -> R.drawable.zte_business_02_t2_final
            3 -> R.drawable.zte_business_02_t3_final
            4 -> R.drawable.zte_business_02_t4_final
            5 -> R.drawable.zte_business_02_t5_final
            6 -> R.drawable.zte_business_02_t6_final
            else -> error("canonicalBusinessTier returned unsupported tier $tier")
        }
        3 -> when (tier) {
            0 -> R.drawable.zte_business_03_t0_final
            1 -> R.drawable.zte_business_03_t1_final
            2 -> R.drawable.zte_business_03_t2_final
            3 -> R.drawable.zte_business_03_t3_final
            4 -> R.drawable.zte_business_03_t4_final
            5 -> R.drawable.zte_business_03_t5_final
            6 -> R.drawable.zte_business_03_t6_final
            else -> error("canonicalBusinessTier returned unsupported tier $tier")
        }
        else -> null
    }
}
