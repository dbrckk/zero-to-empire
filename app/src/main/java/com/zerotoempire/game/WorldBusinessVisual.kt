package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.Dp

/**
 * Progressive runtime bridge from authored production assets to the live world.
 * Missing raster tiers deliberately fall back to BusinessArtIcon until their optimized
 * runtime resource is actually committed. Never reference a not-yet-packaged drawable.
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
        0 to 1 -> R.drawable.zte_business_00_t1_runtime
        1 to 0 -> R.drawable.zte_business_01_t0_runtime
        2 to 0 -> R.drawable.zte_business_02_t0_runtime
        3 to 0 -> R.drawable.zte_business_03_t0_runtime
        else -> null
    }

    if (drawable != null) {
        val context = LocalContext.current
        val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
        val reveal = remember(businessId, tier) { Animatable(1f) }

        LaunchedEffect(businessId, tier, reducedMotion) {
            if (reducedMotion) {
                reveal.snapTo(1f)
            } else {
                reveal.snapTo(.88f)
                reveal.animateTo(
                    targetValue = 1f,
                    animationSpec = tween(durationMillis = 380, easing = FastOutSlowInEasing)
                )
            }
        }

        // Authored tiers gain a little physical presence as the lot evolves, while the
        // one-shot reveal keeps upgrades tactile without adding a permanent animation loop.
        val authoredSize = size * (1f + tier.coerceAtMost(6) * .055f)
        Image(
            painter = painterResource(drawable),
            contentDescription = null,
            modifier = modifier
                .size(authoredSize)
                .graphicsLayer {
                    scaleX = reveal.value
                    scaleY = reveal.value
                    alpha = .72f + reveal.value * .28f
                },
            contentScale = ContentScale.Fit
        )
    } else {
        BusinessArtIcon(businessId, level, size)
    }
}
