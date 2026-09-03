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

private const val IonTrailFrameSize = 128
private const val IonTrailColumns = 4
private const val IonTrailFrameCount = 8

/** Cosmic Foundry orbit accent, frozen on frame zero under reduced motion. */
@Composable
internal fun OrbitalIonTrail(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_14_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) {
            while (true) {
                delay(125)
                frame = (frame + 1) % IonTrailFrameCount
            }
        }
    }

    Canvas(modifier) {
        val effectSize = size.minDimension * .76f
        val destination = Offset((size.width - effectSize) * .5f, size.height * .08f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                (frame % IonTrailColumns) * IonTrailFrameSize,
                (frame / IonTrailColumns) * IonTrailFrameSize
            ),
            srcSize = IntSize(IonTrailFrameSize, IonTrailFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .68f
        )
    }
}
