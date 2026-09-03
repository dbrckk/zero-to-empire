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

private const val UpgradeFlashFrameSize = 128
private const val UpgradeFlashColumns = 4
private const val UpgradeFlashFrameCount = 8

/** One-shot authored flash replayed whenever a business level changes. */
@Composable
internal fun UpgradeConstructionFlash(trigger: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_08_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(UpgradeFlashFrameCount) }
    LaunchedEffect(trigger, reducedMotion) {
        if (trigger <= 0) return@LaunchedEffect
        if (reducedMotion) {
            frame = 3
            delay(140)
            frame = UpgradeFlashFrameCount
        } else {
            repeat(UpgradeFlashFrameCount) { index ->
                frame = index
                delay(125)
            }
            frame = UpgradeFlashFrameCount
        }
    }
    if (frame >= UpgradeFlashFrameCount) return
    Canvas(modifier) {
        val effectSize = size.minDimension * .62f
        val destination = Offset((size.width - effectSize) * .5f, size.height * .16f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                (frame % UpgradeFlashColumns) * UpgradeFlashFrameSize,
                (frame / UpgradeFlashColumns) * UpgradeFlashFrameSize
            ),
            srcSize = IntSize(UpgradeFlashFrameSize, UpgradeFlashFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .84f
        )
    }
}
