package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test

class StoreProductResolverTest {
    @Test
    fun exactKnownProductResolves() {
        assertEquals(StoreProduct.GEM_PACK_SMALL, StoreProductResolver.resolve(listOf("gems_small")))
    }

    @Test
    fun unknownOrAmbiguousProductsNeverResolve() {
        assertNull(StoreProductResolver.resolve(emptyList()))
        assertNull(StoreProductResolver.resolve(listOf("unknown")))
        assertNull(StoreProductResolver.resolve(listOf("gems_small", "gems_medium")))
        assertNull(StoreProductResolver.resolve(listOf("gems_small", "unknown")))
    }
}
