package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.FilterQuality
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlin.math.roundToInt

private const val FX_COLUMNS = 4
private const val FX_ROWS = 2
private const val FX_FRAME_COUNT = FX_COLUMNS * FX_ROWS

internal fun canonicalFxFrameIndex(progress: Float): Int =
    (progress.coerceIn(0f, 1f) * FX_FRAME_COUNT)
        .toInt()
        .coerceIn(0, FX_FRAME_COUNT - 1)

/**
 * Sprite-first renderer for authored 4x2 production VFX sheets.
 *
 * Only one 128x128 source cell is drawn at a time; the sheet itself is never
 * exposed as a single UI image. Runtime drawing may still be layered around the
 * authored frame for motion accents, but does not replace its visual identity.
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
    val context = LocalContext.current
    val sheet = remember(effect) {
        BitmapFactory.decodeResource(context.resources, canonicalFxRasterRes(effect)).asImageBitmap()
    }
    val p = progress.coerceIn(0f, 1f)
    val scale = startScale + (endScale - startScale) * p
    val frameIndex = canonicalFxFrameIndex(p)
    val frameWidth = sheet.width / FX_COLUMNS
    val frameHeight = sheet.height / FX_ROWS
    val sourceOffset = IntOffset(
        x = (frameIndex % FX_COLUMNS) * frameWidth,
        y = (frameIndex / FX_COLUMNS) * frameHeight,
    )

    Canvas(
        modifier = modifier.graphicsLayer {
            scaleX = scale
            scaleY = scale
        }
    ) {
        val side = size.minDimension.roundToInt().coerceAtLeast(1)
        val destinationOffset = IntOffset(
            x = ((size.width - side) / 2f).roundToInt(),
            y = ((size.height - side) / 2f).roundToInt(),
        )
        drawImage(
            image = sheet,
            srcOffset = sourceOffset,
            srcSize = IntSize(frameWidth, frameHeight),
            dstOffset = destinationOffset,
            dstSize = IntSize(side, side),
            alpha = (alpha * (1f - p)).coerceIn(0f, 1f),
            filterQuality = FilterQuality.High,
        )
    }
}
