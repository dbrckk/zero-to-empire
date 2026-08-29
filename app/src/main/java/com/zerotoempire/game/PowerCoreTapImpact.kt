package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
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
import kotlin.math.cos
import kotlin.math.sin

/**
 * Short-lived, tap-triggered VFX for the Power Core.
 *
 * Unlike the ambient core aura this owns no infinite animation clock: work is
 * performed only after a successful tap. Reduced-motion users keep the existing
 * haptic/number feedback without this burst, while low-power mode uses fewer
 * particles and a shorter animation.
 */
@Composable
fun PowerCoreTapImpact(serial: Int, eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val progress = remember { Animatable(1f) }

    LaunchedEffect(serial, reducedMotion, lowPower) {
        if (serial <= 0 || reducedMotion) {
            progress.snapTo(1f)
            return@LaunchedEffect
        }
        progress.snapTo(0f)
        progress.animateTo(
            targetValue = 1f,
            animationSpec = tween(
                durationMillis = if (lowPower) 260 else 380,
                easing = FastOutSlowInEasing
            )
        )
    }

    if (serial <= 0 || reducedMotion || progress.value >= .999f) return

    val accent = when (eraIndex) {
        in 0..2 -> EmpireColors.Gold
        in 3..5 -> EmpireColors.Cyan
        in 6..8 -> EmpireColors.Violet
        else -> EmpireColors.GoldBright
    }
    val p = progress.value
    val alpha = (1f - p).coerceIn(0f, 1f)

    Canvas(modifier) {
        val center = Offset(size.width / 2f, size.height / 2f)
        val min = size.minDimension
        val primaryRadius = min * (.22f + .30f * p)
        val secondaryRadius = min * (.16f + .22f * p)

        drawCircle(
            color = accent.copy(alpha = alpha * .78f),
            radius = primaryRadius,
            center = center,
            style = Stroke(width = min * (.018f - .010f * p).coerceAtLeast(.004f))
        )
        if (!lowPower) {
            drawCircle(
                color = Color.White.copy(alpha = alpha * .34f),
                radius = secondaryRadius,
                center = center,
                style = Stroke(width = min * .005f)
            )
        }

        val sparkCount = if (lowPower) 6 else 14
        repeat(sparkCount) { index ->
            val angle = index * (Math.PI * 2.0 / sparkCount) + serial * .37
            val startRadius = min * (.20f + .08f * p)
            val endRadius = min * (.29f + .24f * p) * if (index % 3 == 0) 1.08f else 1f
            val start = Offset(
                center.x + cos(angle).toFloat() * startRadius,
                center.y + sin(angle).toFloat() * startRadius
            )
            val end = Offset(
                center.x + cos(angle).toFloat() * endRadius,
                center.y + sin(angle).toFloat() * endRadius
            )
            drawLine(
                color = if (index % 2 == 0) accent.copy(alpha = alpha * .72f) else Color.White.copy(alpha = alpha * .44f),
                start = start,
                end = end,
                strokeWidth = min * if (index % 3 == 0) .010f else .006f
            )
        }
    }
}
