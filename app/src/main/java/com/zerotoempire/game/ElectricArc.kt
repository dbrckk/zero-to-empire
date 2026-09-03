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

private const val ArcFrameSize = 128
private const val ArcColumns = 4
private const val ArcFrameCount = 8

/** Mars Empire power arc, frozen on frame zero under reduced motion. */
@Composable
internal fun ElectricArc(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_10_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }
    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) while (true) {
            delay(125)
            frame = (frame + 1) % ArcFrameCount
        }
    }
    Canvas(modifier) {
        val effectSize = size.minDimension * .58f
        val destination = Offset((size.width - effectSize) * .5f, (size.height - effectSize) * .5f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset((frame % ArcColumns) * ArcFrameSize, (frame / ArcColumns) * ArcFrameSize),
            srcSize = IntSize(ArcFrameSize, ArcFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .66f
        )
    }
}
