package com.zerotoempire.game

/**
 * Resolves canonical tiered raster art for Group 01 businesses that have
 * production WebP assets ready for runtime wiring.
 *
 * Business IDs 2 (Workshop / BLD-02) and 3 (Factory / BLD-03) are deliberately
 * compile-time bound to every canonical T0..T6 drawable. Other business IDs
 * return null until their canonical raster sets satisfy the same production
 * contract.
 */
internal fun canonicalBusinessRasterRes(businessId: Int, level: Int): Int? {
    val tier = canonicalBusinessTier(level)
    return when (businessId) {
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
