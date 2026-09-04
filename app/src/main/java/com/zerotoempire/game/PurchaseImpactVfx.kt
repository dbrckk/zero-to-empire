package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

private const val WarmPulseFrameSize = 128
private const val WarmPulseColumns = 4
private const val WarmPulseFrameCount = 8
private const val WarmPulsePeakFrame = 4
private const val ConstructionDustPeakFrame = 3

/**
 * Short-lived feedback for successful asset purchases.
 * FX-06 provides the authored warm energy pulse while Canvas sparks preserve
 * scale-dependent punch without adding idle animation cost.
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
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_06_final).asImageBitmap()
    }
    val dustSheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_07_final).asImageBitmap()
    }
    val steamSheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_04_final).asImageBitmap()
    }
    val progress = remember { Animatable(1f) }

    LaunchedEffect(serial, reduced, lowPower) {
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
        val frame = when {
            reduced -> WarmPulsePeakFrame
            lowPower -> ((p * 4f).toInt().coerceIn(0, 3) * 2).coerceAtMost(WarmPulseFrameCount - 1)
            else -> (p * WarmPulseFrameCount).toInt().coerceIn(0, WarmPulseFrameCount - 1)
        }
        val pulseSize = (min * (.34f + intensity * .16f)).toInt().coerceAtLeast(1)
        val pulseOffset = IntOffset(
            x = (center.x - pulseSize / 2f).toInt(),
            y = (center.y - pulseSize / 2f).toInt()
        )

        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (frame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = pulseOffset,
            dstSize = IntSize(pulseSize, pulseSize),
            alpha = if (reduced) intensity * .72f else intensity
        )

        val dustFrame = when {
            reduced -> ConstructionDustPeakFrame
            lowPower -> ((p * 4f).toInt().coerceIn(0, 3) * 2).coerceAtMost(WarmPulseFrameCount - 1)
            else -> (p * WarmPulseFrameCount).toInt().coerceIn(0, WarmPulseFrameCount - 1)
        }
        val dustSize = (min * (.42f + intensity * .14f)).toInt().coerceAtLeast(1)
        drawImage(
            image = dustSheet,
            srcOffset = IntOffset(
                x = (dustFrame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (dustFrame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = IntOffset(
                x = (center.x - dustSize / 2f).toInt(),
                y = (center.y - dustSize * .36f).toInt()
            ),
            dstSize = IntSize(dustSize, dustSize),
            alpha = if (reduced) intensity * .48f else intensity * .76f
        )

        val steamFrame = when {
            reduced -> 3
            lowPower -> ((p * 4f).toInt().coerceIn(0, 3) * 2).coerceAtMost(WarmPulseFrameCount - 1)
            else -> (p * WarmPulseFrameCount).toInt().coerceIn(0, WarmPulseFrameCount - 1)
        }
        val steamSize = (min * (.30f + intensity * .10f)).toInt().coerceAtLeast(1)
        drawImage(
            image = steamSheet,
            srcOffset = IntOffset(
                x = (steamFrame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (steamFrame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = IntOffset(
                x = (center.x + min * .08f - steamSize / 2f).toInt(),
                y = (center.y - steamSize * .72f).toInt()
            ),
            dstSize = IntSize(steamSize, steamSize),
            alpha = if (reduced) intensity * .28f else (1f - p) * intensity * .48f
        )

        if (!reduced) {
            drawCircle(
                color = EmpireArtPalette.GoldHot.copy(alpha = alpha * .24f),
                radius = min * (.08f + p * .32f),
                center = center,
                style = Stroke(width = 2f + intensity * 1.5f)
            )

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
