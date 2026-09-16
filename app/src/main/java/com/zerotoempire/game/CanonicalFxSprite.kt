package com.zerotoempire.game

import androidx.compose.foundation.Image
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource

/**
 * Sprite-first renderer for semantic authored VFX.
 *
 * The final raster carries the visual identity. Runtime drawing may be layered
 * around it for motion accents, but should not replace the authored sprite.
 */
@Composable
internal fun CanonicalFxSprite(
    effect: CanonicalFx,
    progress: Float,
    modifier: Modifier = Modifier,
    alpha: Float = 1f,
    startScale: Float = .55f,
    endScale: Float = 1.10f,
) {
    val p = progress.coerceIn(0f, 1f)
    val scale = startScale + (endScale - startScale) * p
    Image(
        painter = painterResource(canonicalFxRasterRes(effect)),
        contentDescription = null,
        contentScale = ContentScale.Fit,
        modifier = modifier.graphicsLayer {
            scaleX = scale
            scaleY = scale
            this.alpha = (alpha * (1f - p)).coerceIn(0f, 1f)
        },
    )
}
