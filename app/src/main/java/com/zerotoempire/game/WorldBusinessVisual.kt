package com.zerotoempire.game

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.Dp

/**
 * Progressive runtime bridge from authored production assets to the live world.
 * Missing tiers deliberately fall back to BusinessArtIcon so rollout can happen safely asset by asset.
 */
@Composable
internal fun WorldBusinessVisual(
    businessId: Int,
    level: Int,
    size: Dp,
    modifier: Modifier = Modifier
) {
    val tier = WorldSpriteRegistry.tierForLevel(level)
    val drawable = when (businessId to tier) {
        0 to 0 -> R.drawable.zte_business_00_t0_runtime
        else -> null
    }

    if (drawable != null) {
        Image(
            painter = painterResource(drawable),
            contentDescription = null,
            modifier = modifier.size(size),
            contentScale = ContentScale.Fit
        )
    } else {
        BusinessArtIcon(businessId, level, size)
    }
}
