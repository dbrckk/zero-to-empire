package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val StellarFlareFrameSize = 128
private const val StellarFlareColumns = 4
private const val StellarFlareFrameCount = 8

/** Reality Engine plasma accent, frozen on its complete first frame under reduced motion. */
@Composable
internal fun StellarFlare(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_15_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) {
            while (true) {
                delay(125)
                frame = (frame + 1) % StellarFlareFrameCount
            }
        }
    }

    Canvas(modifier) {
        val effectSize = size.minDimension * .74f
        val destination = Offset(
            x = (size.width - effectSize) * .5f,
            y = size.height * .12f
        )
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % StellarFlareColumns) * StellarFlareFrameSize,
                y = (frame / StellarFlareColumns) * StellarFlareFrameSize
            ),
            srcSize = IntSize(StellarFlareFrameSize, StellarFlareFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .72f
        )
    }
}
