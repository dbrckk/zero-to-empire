package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/**
 * Short-lived, Canvas-only feedback for successful asset purchases.
 * It deliberately has no idle animation: zero GPU/CPU cost between purchases.
 */
@Composable
fun AssetPurchaseImpact(
    serial: Int,
    purchaseCount: Int,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val progress = remember { Animatable(1f) }

    LaunchedEffect(serial) {
        if (serial <= 0) return@LaunchedEffect
        progress.snapTo(0f)
        progress.animateTo(
            1f,
            animationSpec = tween(
                durationMillis = when {
                    reduced -> 180
                    lowPower -> 360
                    else -> 520
                }
            )
        )
    }

    if (serial <= 0 || progress.value >= .999f) return
    val p = progress.value
    val intensity = when {
        purchaseCount >= 100 -> 1f
        purchaseCount >= 25 -> .82f
        purchaseCount >= 10 -> .68f
        else -> .52f
    }

    Canvas(modifier) {
        val center = Offset(size.width * .18f, size.height * .50f)
        val min = size.minDimension
        val alpha = (1f - p) * intensity

        drawCircle(
            color = EmpireArtPalette.GoldHot.copy(alpha = alpha * .42f),
            radius = min * (.08f + p * .32f),
            center = center,
            style = Stroke(width = 2.5f + intensity * 2f)
        )
        drawCircle(
            color = Color.White.copy(alpha = alpha * .22f),
            radius = min * (.05f + p * .20f),
            center = center,
            style = Stroke(width = 1.5f)
        )

        if (!reduced) {
            val sparks = if (lowPower) 7 else 13
            repeat(sparks) { i ->
                val angle = i * (2f * PI.toFloat() / sparks) + .18f
                val distance = min * (.07f + p * (.22f + (i % 3) * .025f))
                val point = Offset(
                    center.x + cos(angle) * distance,
                    center.y + sin(angle) * distance
                )
                drawCircle(
                    color = if (i % 4 == 0) Color.White.copy(alpha = alpha) else EmpireArtPalette.Gold.copy(alpha = alpha * .86f),
                    radius = if (i % 4 == 0) 2.7f else 1.8f,
                    center = point
                )
            }
        }
    }
}
