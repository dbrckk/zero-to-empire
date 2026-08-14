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
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun EmpireCoreGlyph(modifier: Modifier = Modifier) {
    val infinite = rememberInfiniteTransition(label = "empireCore")
    val rotation by infinite.animateFloat(
        initialValue = 0f,
        targetValue = 360f,
        animationSpec = infiniteRepeatable(tween(12_000, easing = LinearEasing)),
        label = "coreRotation"
    )
    val pulse by infinite.animateFloat(
        initialValue = .82f,
        targetValue = 1f,
        animationSpec = infiniteRepeatable(tween(1_400, easing = FastOutSlowInEasing), RepeatMode.Reverse),
        label = "corePulse"
    )

    Canvas(modifier) {
        val s = size.minDimension
        val center = Offset(size.width / 2f, size.height / 2f)
        drawCircle(
            brush = Brush.radialGradient(
                listOf(EmpireArtPalette.White, EmpireArtPalette.GoldHot, EmpireArtPalette.Gold, Color.Transparent),
                center = center,
                radius = s * .39f
            ),
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
            repeat(4 + ring * 2) { i ->
                val angle = Math.toRadians((rotation * (if (ring % 2 == 0) 1 else -1) + i * (360f / (4 + ring * 2))).toDouble())
                drawCircle(
                    color = if (ring % 2 == 0) EmpireArtPalette.White else EmpireArtPalette.GoldHot,
                    radius = s * .018f,
                    center = Offset(
                        center.x + cos(angle).toFloat() * radius,
                        center.y + sin(angle).toFloat() * radius
                    )
                )
            }
        }
        drawLine(EmpireArtPalette.GoldHot, Offset(center.x, center.y - s*.085f), Offset(center.x, center.y + s*.085f), s*.024f)
        drawLine(EmpireArtPalette.GoldHot, Offset(center.x - s*.055f, center.y - s*.055f), Offset(center.x + s*.055f, center.y - s*.055f), s*.024f)
    }
}
