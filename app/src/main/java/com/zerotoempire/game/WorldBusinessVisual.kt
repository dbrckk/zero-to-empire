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
 * Sprite-first runtime bridge from authored production assets to the live world.
 *
 * Every authored business family resolves through canonicalBusinessRasterRes so
 * a single tested T0..T6 contract drives visible gameplay. Canvas drawing is kept
 * only for motion, mastery, upgrade and late-tier VFX layered around primary art.
 */
@Composable
internal fun WorldBusinessVisual(
    businessId: Int,
    level: Int,
    size: Dp,
    modifier: Modifier = Modifier
) {
    val tier = WorldSpriteRegistry.tierForLevel(level)
    val drawable = canonicalBusinessRasterRes(businessId, level)

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
            BusinessTierVfxBeforePrimary(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )
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
            BusinessTierVfxAfterPrimary(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )

            if (businessId in 0..3 && tier >= 1) {
                FoundryWorkerTraffic(
                    businessId = businessId,
                    modifier = Modifier.fillMaxSize()
                )
            }
            if (WorldSpriteRegistry.masteryForLevel(level)) {
                MasteryCrownShimmer(modifier = Modifier.fillMaxSize())
            }
            UpgradeConstructionFlash(level = level, modifier = Modifier.fillMaxSize())
        }
    } else {
        Box(modifier = modifier.size(size)) {
            BusinessTierVfxBeforePrimary(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )
            BusinessArtIcon(businessId, level, size)
            BusinessTierVfxAfterPrimary(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )
            UpgradeConstructionFlash(level = level, modifier = Modifier.fillMaxSize())
        }
    }
}

/**
 * Existing late-tier effects that visually sit behind their primary business art.
 * Keeping them separate from the raster resolver prevents procedural VFX from
 * becoming a fallback identity for businesses that already have authored sprites.
 */
@Composable
private fun BusinessTierVfxBeforePrimary(
    businessId: Int,
    tier: Int,
    modifier: Modifier = Modifier,
) {
    if (tier < 4) return
    when (businessId) {
        6 -> IncomePickupSparkle(modifier = modifier)
        7 -> ElectricArc(modifier = modifier)
        8 -> HologramScanSweep(modifier = modifier)
        9 -> DroneThruster(modifier = modifier)
        10 -> PhaseDistortion(modifier = modifier)
        11 -> OrbitalIonTrail(modifier = modifier)
        12 -> StellarFlare(modifier = modifier)
    }
}

/** Effects that intentionally sit above the authored primary art. */
@Composable
private fun BusinessTierVfxAfterPrimary(
    businessId: Int,
    tier: Int,
    modifier: Modifier = Modifier,
) {
    if (businessId == 13 && tier >= 4) {
        SingularityLensPulse(modifier = modifier)
    }
}
