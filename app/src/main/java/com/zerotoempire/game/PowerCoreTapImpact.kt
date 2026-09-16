package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import kotlin.math.cos
import kotlin.math.sin

/**
 * Short-lived, tap-triggered VFX for the Power Core.
 *
 * The authored semantic sprites now carry the visual identity. Runtime Canvas
 * work is deliberately limited to lightweight motion accents around them.
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
    val fade = (1f - p).coerceIn(0f, 1f)

    Box(modifier) {
        CanonicalFxSprite(
            effect = CanonicalFx.RING_PULSE,
            progress = p,
            modifier = Modifier.fillMaxSize(),
            alpha = .98f,
            startScale = .48f,
            endScale = 1.12f,
        )
        if (!lowPower) {
            CanonicalFxSprite(
                effect = CanonicalFx.SPARK,
                progress = p,
                modifier = Modifier.fillMaxSize(),
                alpha = .76f,
                startScale = .28f,
                endScale = .88f,
            )
        }

        Canvas(Modifier.fillMaxSize()) {
            val center = Offset(size.width / 2f, size.height / 2f)
            val min = size.minDimension
            val sparkCount = if (lowPower) 4 else 8

            repeat(sparkCount) { index ->
                val angle = index * (Math.PI * 2.0 / sparkCount) + serial * .37
                val startRadius = min * (.21f + .08f * p)
                val endRadius = min * (.27f + .19f * p) * if (index % 3 == 0) 1.08f else 1f
                val start = Offset(
                    center.x + cos(angle).toFloat() * startRadius,
                    center.y + sin(angle).toFloat() * startRadius
                )
                val end = Offset(
                    center.x + cos(angle).toFloat() * endRadius,
                    center.y + sin(angle).toFloat() * endRadius
                )
                drawLine(
                    color = if (index % 2 == 0) {
                        accent.copy(alpha = fade * .42f)
                    } else {
                        Color.White.copy(alpha = fade * .28f)
                    },
                    start = start,
                    end = end,
                    strokeWidth = min * if (index % 3 == 0) .007f else .004f
                )
            }
        }
    }
}
