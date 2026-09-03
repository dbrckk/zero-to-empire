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

private const val IncomeSparkleFrameSize = 128
private const val IncomeSparkleColumns = 4
private const val IncomeSparkleFrameCount = 8

/** Compact income feedback sparkle; reduced motion retains a quiet static glint. */
@Composable
internal fun IncomePickupSparkle(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_09_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }
    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) while (true) {
            delay(125)
            frame = (frame + 1) % IncomeSparkleFrameCount
            if (frame == 0) delay(1_250)
        }
    }
    Canvas(modifier) {
        val effectSize = size.minDimension * .34f
        val destination = Offset(size.width * .60f, size.height * .10f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                (frame % IncomeSparkleColumns) * IncomeSparkleFrameSize,
                (frame / IncomeSparkleColumns) * IncomeSparkleFrameSize
            ),
            srcSize = IntSize(IncomeSparkleFrameSize, IncomeSparkleFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .82f
        )
    }
}
