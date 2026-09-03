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

private const val LensFrameSize = 128
private const val LensColumns = 4
private const val LensFrameCount = 8

/** Apex singularity accent. Decorative animation stops under reduced motion/battery saver. */
@Composable
internal fun SingularityLensPulse(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_16_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) {
            while (true) {
                delay(125)
                frame = (frame + 1) % LensFrameCount
            }
        }
    }

    Canvas(modifier) {
        val effectSize = size.minDimension * .82f
        val destination = Offset(
            x = (size.width - effectSize) * .5f,
            y = (size.height - effectSize) * .5f
        )
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % LensColumns) * LensFrameSize,
                y = (frame / LensColumns) * LensFrameSize
            ),
            srcSize = IntSize(LensFrameSize, LensFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .78f
        )
    }
}
