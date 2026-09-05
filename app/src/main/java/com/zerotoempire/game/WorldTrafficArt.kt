package com.zerotoempire.game

import androidx.annotation.DrawableRes
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.withTransform
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize

/** Reviewed FLUX vehicle sprites used as physical traffic in the city stage. */
private val worldTrafficSprites = intArrayOf(
    R.drawable.zte_vehicle_00_final,
    R.drawable.zte_vehicle_01_final,
    R.drawable.zte_vehicle_02_final,
    R.drawable.zte_vehicle_03_final,
    R.drawable.zte_vehicle_04_final,
    R.drawable.zte_vehicle_05_final,
    R.drawable.zte_vehicle_06_final,
    R.drawable.zte_vehicle_07_final,
    R.drawable.zte_vehicle_08_final,
    R.drawable.zte_vehicle_10_final,
)

@Composable
internal fun ReviewedWorldTraffic(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val sprites = remember { worldTrafficSprites.map { ImageBitmap.imageResource(context.resources, it) } }
    Box(modifier) {
        Canvas(Modifier.fillMaxSize()) {
            if (sprites.isEmpty()) return@Canvas
            val placements = listOf(
                Triple(.45f, .37f, .090f), Triple(.54f, .43f, .105f), Triple(.43f, .50f, .112f),
                Triple(.58f, .58f, .125f), Triple(.39f, .66f, .132f), Triple(.63f, .73f, .145f),
                Triple(.34f, .79f, .090f), Triple(.69f, .84f, .150f), Triple(.46f, .89f, .158f),
                Triple(.57f, .94f, .090f),
            )
            placements.forEachIndexed { index, (xf, yf, wf) ->
                drawTrafficSprite(sprites[index % sprites.size], xf, yf, wf)
            }
        }
    }
}

private fun DrawScope.drawTrafficSprite(image: ImageBitmap, xFraction: Float, yFraction: Float, widthFraction: Float) {
    val targetWidth = (size.width * widthFraction).toInt().coerceAtLeast(1)
    val ratio = image.height.toFloat() / image.width.toFloat()
    val targetHeight = (targetWidth * ratio).toInt().coerceAtLeast(1)
    val x = (size.width * xFraction - targetWidth / 2f).toInt()
    val y = (size.height * yFraction - targetHeight * .72f).toInt()
    drawOval(
        color = Color.Black.copy(alpha = .28f),
        topLeft = Offset(x + targetWidth * .12f, y + targetHeight * .73f),
        size = androidx.compose.ui.geometry.Size(targetWidth * .76f, targetHeight * .14f),
    )
    drawImage(
        image = image,
        srcOffset = IntOffset.Zero,
        srcSize = IntSize(image.width, image.height),
        dstOffset = IntOffset(x, y),
        dstSize = IntSize(targetWidth, targetHeight),
    )
}
