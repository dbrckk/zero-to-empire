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
import androidx.compose.ui.graphics.drawscope.drawImage
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val CrownFrameSize = 128
private const val CrownColumns = 4
private const val CrownFrameCount = 8

/** Raster mastery accent. Reduced-motion and battery-saver users receive frame zero. */
@Composable
internal fun MasteryCrownShimmer(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_17_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) {
            while (true) {
                delay(125)
                frame = (frame + 1) % CrownFrameCount
            }
        }
    }

    Canvas(modifier) {
        val crownSize = size.minDimension * .31f
        val destination = Offset(
            x = (size.width - crownSize) * .5f,
            y = size.height * .015f
        )
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % CrownColumns) * CrownFrameSize,
                y = (frame / CrownColumns) * CrownFrameSize
            ),
            srcSize = IntSize(CrownFrameSize, CrownFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(crownSize.toInt(), crownSize.toInt()),
            alpha = .96f
        )
    }
}
