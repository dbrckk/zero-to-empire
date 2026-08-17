package com.zerotoempire.game

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun EmpireCoreGlyph(modifier: Modifier = Modifier) {
    val vm: GameViewModel = viewModel()
    val state by vm.state.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)

    val rotation: Float
    val fastRotation: Float
    val pulse: Float
    if (reducedMotion) {
        rotation = 0f
        fastRotation = 0f
        pulse = .94f
    } else {
        val infinite = rememberInfiniteTransition(label = "empireCore")
        val r by infinite.animateFloat(
            initialValue = 0f,
            targetValue = 360f,
            animationSpec = infiniteRepeatable(tween(if (lowPower) 18_000 else 12_000, easing = LinearEasing)),
            label = "coreRotation"
        )
        val fr by infinite.animateFloat(
            initialValue = 0f,
            targetValue = 360f,
            animationSpec = infiniteRepeatable(tween(if (lowPower) 8_000 else 4_800, easing = LinearEasing)),
            label = "trailRotation"
        )
        val p by infinite.animateFloat(
            initialValue = .82f,
            targetValue = 1f,
            animationSpec = infiniteRepeatable(tween(if (lowPower) 2_100 else 1_400, easing = FastOutSlowInEasing), RepeatMode.Reverse),
            label = "corePulse"
        )
        rotation = r
        fastRotation = fr
        pulse = p
    }

    val intensity = (1 + state.empireLevel).coerceIn(1, if (lowPower) 5 else 8)
    val trailPoints = if (lowPower) 3 else 5

    Canvas(modifier) {
        val s = size.minDimension
        val center = Offset(size.width / 2f, size.height / 2f)

        repeat(intensity + 3) { i ->
            val angle = Math.toRadians((fastRotation + i * (360f / (intensity + 3))).toDouble())
            val radius = s * (.34f + (i % 3) * .045f)
            val head = Offset(center.x + cos(angle).toFloat() * radius, center.y + sin(angle).toFloat() * radius)
            repeat(trailPoints) { trail ->
                val backAngle = angle - trail * .075
                val alpha = (.34f - trail * .055f).coerceAtLeast(.05f)
                drawCircle(
                    color = if (i % 2 == 0) EmpireArtPalette.Cyan.copy(alpha = alpha) else EmpireArtPalette.Violet.copy(alpha = alpha),
                    radius = s * (.014f - trail * .0015f).coerceAtLeast(.006f),
                    center = Offset(center.x + cos(backAngle).toFloat() * radius, center.y + sin(backAngle).toFloat() * radius)
                )
            }
            drawCircle(EmpireArtPalette.White.copy(alpha = .88f), s * .012f, head)
        }

        drawCircle(
            brush = Brush.radialGradient(listOf(EmpireArtPalette.White, EmpireArtPalette.GoldHot, EmpireArtPalette.Gold, Color.Transparent), center, s * .39f),
            radius = s * .39f * pulse,
            center = center
        )
        drawCircle(EmpireArtPalette.Ink, radius = s * .17f, center = center)
        drawCircle(EmpireArtPalette.GoldHot, radius = s * .12f, center = center, style = Stroke(s * .025f))

        repeat(3) { ring ->
            val radius = s * (.23f + ring * .07f)
            drawCircle(
                color = if (ring % 2 == 0) EmpireArtPalette.Cyan.copy(alpha = .72f) else EmpireArtPalette.Violet.copy(alpha = .72f),
                radius = radius,
                center = center,
                style = Stroke(s * .012f)
            )
            val nodes = if (lowPower) 3 + ring else 4 + ring * 2
            repeat(nodes) { i ->
                val angle = Math.toRadians((rotation * (if (ring % 2 == 0) 1 else -1) + i * (360f / nodes)).toDouble())
                drawCircle(
                    color = if (ring % 2 == 0) EmpireArtPalette.White else EmpireArtPalette.GoldHot,
                    radius = s * .018f,
                    center = Offset(center.x + cos(angle).toFloat() * radius, center.y + sin(angle).toFloat() * radius)
                )
            }
        }

        if (state.empireLevel >= 4 && !lowPower) {
            repeat(6) { i ->
                val a = Math.toRadians((rotation * -1.4f + i * 60f).toDouble())
                drawLine(
                    color = EmpireArtPalette.GoldHot.copy(alpha = .28f),
                    start = Offset(center.x + cos(a).toFloat() * s * .18f, center.y + sin(a).toFloat() * s * .18f),
                    end = Offset(center.x + cos(a).toFloat() * s * .48f, center.y + sin(a).toFloat() * s * .48f),
                    strokeWidth = s * .008f
                )
            }
        }

        drawLine(EmpireArtPalette.GoldHot, Offset(center.x, center.y - s*.085f), Offset(center.x, center.y + s*.085f), s*.024f)
        drawLine(EmpireArtPalette.GoldHot, Offset(center.x - s*.055f, center.y - s*.055f), Offset(center.x + s*.055f, center.y - s*.055f), s*.024f)
    }
}
