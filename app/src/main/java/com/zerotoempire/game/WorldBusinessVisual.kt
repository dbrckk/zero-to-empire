package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
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
        0 to 0 -> R.drawable.zte_business_00_t0_final
        0 to 1 -> R.drawable.zte_business_00_t1_final
        0 to 2 -> R.drawable.zte_business_00_t2_final
        0 to 3 -> R.drawable.zte_business_00_t3_final
        0 to 4 -> R.drawable.zte_business_00_t4_final
        0 to 5 -> R.drawable.zte_business_00_t5_final
        0 to 6 -> R.drawable.zte_business_00_t6_final
        1 to 0 -> R.drawable.zte_business_01_t0_final
        1 to 1 -> R.drawable.zte_business_01_t1_final
        1 to 2 -> R.drawable.zte_business_01_t2_final
        1 to 3 -> R.drawable.zte_business_01_t3_final
        1 to 4 -> R.drawable.zte_business_01_t4_final
        1 to 5 -> R.drawable.zte_business_01_t5_final
        1 to 6 -> R.drawable.zte_business_01_t6_final
        2 to 0 -> R.drawable.zte_business_02_t0_final
        2 to 1 -> R.drawable.zte_business_02_t1_final
        2 to 2 -> R.drawable.zte_business_02_t2_final
        2 to 3 -> R.drawable.zte_business_02_t3_final
        2 to 4 -> R.drawable.zte_business_02_t4_final
        2 to 5 -> R.drawable.zte_business_02_t5_final
        2 to 6 -> R.drawable.zte_business_02_t6_final
        3 to 0 -> R.drawable.zte_business_03_t0_final
        3 to 1 -> R.drawable.zte_business_03_t1_final
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

        val authoredSize = size * (1f + tier.coerceAtMost(6) * .055f)
        Box(modifier = modifier.size(authoredSize)) {
            Image(
                painter = painterResource(drawable),
                contentDescription = null,
                modifier = Modifier
                    .fillMaxSize()
                    .graphicsLayer {
                        scaleX = reveal.value
                        scaleY = reveal.value
                        alpha = .72f + reveal.value * .28f
                    },
                contentScale = ContentScale.Fit
            )

            // The first Foundry evolution gains authored worker/delivery traffic so the district
            // reads as a living production space instead of a static icon collection.
            if (businessId in 0..3 && tier >= 1) {
                FoundryWorkerTraffic(
                    businessId = businessId,
                    modifier = Modifier.fillMaxSize()
                )
            }
            if (WorldSpriteRegistry.masteryForLevel(level)) {
                MasteryCrownShimmer(modifier = Modifier.fillMaxSize())
            }
        }
    } else {
        Box(modifier = modifier.size(size)) {
            if (businessId == 7 && tier >= 4) ElectricArc(modifier = Modifier.fillMaxSize())
            if (businessId == 8 && tier >= 4) HologramScanSweep(modifier = Modifier.fillMaxSize())
            if (businessId == 9 && tier >= 4) DroneThruster(modifier = Modifier.fillMaxSize())
            if (businessId == 10 && tier >= 4) PhaseDistortion(modifier = Modifier.fillMaxSize())
            if (businessId == 11 && tier >= 4) OrbitalIonTrail(modifier = Modifier.fillMaxSize())
            if (businessId == 12 && tier >= 4) StellarFlare(modifier = Modifier.fillMaxSize())
            BusinessArtIcon(businessId, level, size)
            if (businessId == 13 && tier >= 4) SingularityLensPulse(modifier = Modifier.fillMaxSize())
        }
    }
}
