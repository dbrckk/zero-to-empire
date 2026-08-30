package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun BusinessGroup02Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val stage = when {
        level >= 1000 -> 7
        level >= 500 -> 6
        level >= 250 -> 5
        level >= 100 -> 4
        level >= 50 -> 3
        level >= 25 -> 2
        level >= 10 -> 1
        else -> 0
    }

    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val reveal = remember(id) { Animatable(0f) }
    val previousStage = remember(id) { intArrayOf(stage) }

    LaunchedEffect(stage, reducedMotion, lowPower) {
        val prior = previousStage[0]
        previousStage[0] = stage
        if (stage > prior && !reducedMotion) {
            reveal.snapTo(1f)
            reveal.animateTo(0f, tween(if (lowPower) 520 else 820))
        } else if (reducedMotion && reveal.value != 0f) {
            reveal.snapTo(0f)
        }
    }

    if (stage == 0) return

    val accent = when (id) {
        4 -> Color(0xFF8C7CFF)
        5 -> Color(0xFFB861FF)
        6 -> Color(0xFF9FE8FF)
        else -> Color(0xFFFF6C5F)
    }
    val secondary = when (id) {
        4 -> Color(0xFF6EEAFF)
        5 -> Color(0xFF59E8FF)
        6 -> Color.White
        else -> Color(0xFFFFC85A)
    }

    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        val center = Offset(s * .5f, s * .5f)

        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(Color.White.copy(alpha = .08f), accent.copy(alpha = .10f), Color.Transparent),
                    center = Offset(s * .43f, s * .37f),
                    radius = s * .48f
                ),
                radius = s * .46f,
                center = center
            )
            drawArc(
                secondary.copy(alpha = .28f),
                212f,
                54f,
                false,
                Offset(s * .095f, s * .095f),
                Size(s * .81f, s * .81f),
                style = Stroke(s * .006f)
            )
        }
        if (stage >= 6) {
            drawArc(
                accent.copy(alpha = .34f),
                18f,
                118f,
                false,
                Offset(s * .075f, s * .075f),
                Size(s * .85f, s * .85f),
                style = Stroke(s * .006f)
            )
            drawArc(
                Color.White.copy(alpha = .22f),
                198f,
                72f,
                false,
                Offset(s * .12f, s * .12f),
                Size(s * .76f, s * .76f),
                style = Stroke(s * .004f)
            )
        }
        if (stage >= 7) {
            repeat(8) { i ->
                val angle = i * 2f * PI.toFloat() / 8f - PI.toFloat() / 2f
                val node = Offset(
                    center.x + cos(angle) * s * .445f,
                    center.y + sin(angle) * s * .445f
                )
                drawCircle(Color.Black.copy(alpha = .34f), s * .014f, node)
                drawCircle(if (i % 2 == 0) secondary else accent, s * .007f, node)
            }
        }

        when (id) {
            4 -> {
                if (stage >= 1) {
                    drawRect(accent.copy(.30f), Offset(s * .15f, s * .50f), Size(s * .08f, s * .20f))
                    drawRect(accent.copy(.30f), Offset(s * .77f, s * .50f), Size(s * .08f, s * .20f))
                }
                if (stage >= 2) drawCircle(secondary.copy(.48f), s * .18f, center, style = Stroke(s * .010f))
                if (stage >= 3) repeat(4) { i ->
                    val x = s * (.29f + i * .14f)
                    drawLine(accent.copy(.52f), Offset(x, s * .31f), Offset(x, s * .19f), s * .009f)
                }
                if (stage >= 4) drawArc(Color.White.copy(.50f), 195f, 150f, false, Offset(s * .11f, s * .11f), Size(s * .78f, s * .78f), style = Stroke(s * .013f))
                if (stage >= 5) repeat(6) { i ->
                    val x = s * (.25f + i * .10f)
                    drawCircle(secondary.copy(.68f), s * .010f, Offset(x, s * .75f))
                }
                if (stage >= 6) {
                    drawLine(secondary.copy(.62f), Offset(s * .18f, s * .24f), Offset(s * .82f, s * .24f), s * .008f)
                    drawCircle(accent.copy(.18f), s * .40f, center)
                }
                if (stage >= 7) {
                    drawCircle(Color(0xFFFFE79B).copy(.22f), s * .46f, center)
                    drawCircle(Color(0xFFFFE79B).copy(.78f), s * .45f, center, style = Stroke(s * .010f))
                }
            }

            5 -> {
                if (stage >= 1) repeat(2) { i ->
                    drawRect(accent.copy(.30f), Offset(s * if (i == 0) .11f else .81f, s * .49f), Size(s * .08f, s * .24f))
                }
                if (stage >= 2) drawLine(secondary.copy(.66f), Offset(s * .14f, s * .74f), Offset(s * .86f, s * .74f), s * .013f)
                if (stage >= 3) repeat(3) { i ->
                    drawCircle(secondary.copy(.50f), s * .040f, Offset(s * (.30f + i * .20f), s * .24f))
                }
                if (stage >= 4) drawArc(accent.copy(.56f), 185f, 170f, false, Offset(s * .08f, s * .10f), Size(s * .84f, s * .72f), style = Stroke(s * .012f))
                if (stage >= 5) repeat(4) { i ->
                    val x = s * (.24f + i * .17f)
                    drawLine(secondary.copy(.42f), Offset(x, s * .67f), Offset(x, s * .31f), s * .006f)
                }
                if (stage >= 6) {
                    drawCircle(accent.copy(.16f), s * .42f, center)
                    drawCircle(secondary.copy(.42f), s * .39f, center, style = Stroke(s * .008f))
                }
                if (stage >= 7) {
                    drawArc(Color(0xFFFFD76A).copy(.72f), -30f, 240f, false, Offset(s * .07f, s * .07f), Size(s * .86f, s * .86f), style = Stroke(s * .013f))
                    repeat(5) { i -> drawCircle(Color(0xFFFFD76A), s * .008f, Offset(s * (.30f + i * .10f), s * .18f)) }
                }
            }

            6 -> {
                if (stage >= 1) {
                    drawCircle(accent.copy(.30f), s * .09f, Offset(s * .18f, s * .58f))
                    drawCircle(accent.copy(.30f), s * .09f, Offset(s * .82f, s * .58f))
                }
                if (stage >= 2) drawLine(Color.White.copy(.46f), Offset(s * .16f, s * .67f), Offset(s * .84f, s * .67f), s * .011f)
                if (stage >= 3) repeat(3) { i -> drawCircle(accent.copy(.58f), s * .015f, Offset(s * (.32f + i * .18f), s * .29f)) }
                if (stage >= 4) drawArc(accent.copy(.62f), 200f, 145f, false, Offset(s * .10f, s * .12f), Size(s * .80f, s * .72f), style = Stroke(s * .013f))
                if (stage >= 5) repeat(4) { i ->
                    drawLine(accent.copy(.38f), Offset(s * (.29f + i * .14f), s * .61f), Offset(s * (.29f + i * .14f), s * .37f), s * .006f)
                }
                if (stage >= 6) {
                    drawCircle(Color.White.copy(.13f), s * .40f, center)
                    drawCircle(accent.copy(.44f), s * .44f, center, style = Stroke(s * .008f))
                }
                if (stage >= 7) {
                    drawArc(Color.White.copy(.72f), 20f, 250f, false, Offset(s * .06f, s * .06f), Size(s * .88f, s * .88f), style = Stroke(s * .012f))
                    repeat(6) { i -> drawCircle(Color.White.copy(.90f), s * .007f, Offset(s * (.25f + i * .10f), s * .18f)) }
                }
            }

            7 -> {
                if (stage >= 1) {
                    drawRect(accent.copy(.36f), Offset(s * .12f, s * .49f), Size(s * .10f, s * .21f))
                    drawRect(accent.copy(.36f), Offset(s * .78f, s * .49f), Size(s * .10f, s * .21f))
                }
                if (stage >= 2) drawLine(secondary.copy(.72f), Offset(s * .15f, s * .74f), Offset(s * .85f, s * .74f), s * .013f)
                if (stage >= 3) repeat(4) { i -> drawCircle(accent.copy(.66f), s * .012f, Offset(s * (.29f + i * .14f), s * .30f)) }
                if (stage >= 4) drawArc(secondary.copy(.58f), 200f, 150f, false, Offset(s * .09f, s * .10f), Size(s * .82f, s * .80f), style = Stroke(s * .013f))
                if (stage >= 5) repeat(3) { i ->
                    drawLine(secondary.copy(.42f), Offset(s * (.34f + i * .16f), s * .64f), Offset(s * (.34f + i * .16f), s * .34f), s * .006f)
                }
                if (stage >= 6) {
                    drawCircle(secondary.copy(.14f), s * .42f, center)
                    drawCircle(accent.copy(.45f), s * .44f, center, style = Stroke(s * .009f))
                }
                if (stage >= 7) {
                    drawArc(secondary.copy(.78f), -25f, 250f, false, Offset(s * .06f, s * .06f), Size(s * .88f, s * .88f), style = Stroke(s * .013f))
                    repeat(5) { i -> drawCircle(secondary, s * .008f, Offset(s * (.30f + i * .10f), s * .18f)) }
                }
            }
        }

        val revealIntensity = reveal.value.coerceIn(0f, 1f)
        if (revealIntensity > 0f) {
            val travel = 1f - revealIntensity
            val sweepRadius = s * (.31f + .16f * travel)

            // Expansion tiers assemble like powered machinery: a core ignition, segmented
            // pressure rings and short orthogonal energy rails. This is transient only.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .16f * revealIntensity),
                        secondary.copy(alpha = .13f * revealIntensity),
                        Color.Transparent
                    ),
                    center = center,
                    radius = s * .48f
                ),
                radius = s * (.33f + .11f * travel),
                center = center
            )
            drawCircle(
                color = accent.copy(alpha = .78f * revealIntensity),
                radius = sweepRadius,
                center = center,
                style = Stroke(s * (.010f + .006f * revealIntensity))
            )
            drawArc(
                color = secondary.copy(alpha = .68f * revealIntensity),
                startAngle = -34f + 28f * travel,
                sweepAngle = 68f,
                useCenter = false,
                topLeft = Offset(center.x - sweepRadius * 1.08f, center.y - sweepRadius * 1.08f),
                size = Size(sweepRadius * 2.16f, sweepRadius * 2.16f),
                style = Stroke(s * .008f)
            )
            drawArc(
                color = Color.White.copy(alpha = .46f * revealIntensity),
                startAngle = 146f + 22f * travel,
                sweepAngle = 54f,
                useCenter = false,
                topLeft = Offset(center.x - sweepRadius * .88f, center.y - sweepRadius * .88f),
                size = Size(sweepRadius * 1.76f, sweepRadius * 1.76f),
                style = Stroke(s * .005f)
            )

            val railLength = s * (.10f + .09f * travel)
            val railOffset = s * (.28f + .10f * travel)
            val railWidth = s * (.008f + .004f * revealIntensity)
            drawLine(accent.copy(alpha = .66f * revealIntensity), Offset(center.x - railOffset, center.y), Offset(center.x - railOffset - railLength, center.y), railWidth)
            drawLine(accent.copy(alpha = .66f * revealIntensity), Offset(center.x + railOffset, center.y), Offset(center.x + railOffset + railLength, center.y), railWidth)
            drawLine(secondary.copy(alpha = .62f * revealIntensity), Offset(center.x, center.y - railOffset), Offset(center.x, center.y - railOffset - railLength), railWidth)
            drawLine(secondary.copy(alpha = .62f * revealIntensity), Offset(center.x, center.y + railOffset), Offset(center.x, center.y + railOffset + railLength), railWidth)

            if (!lowPower) {
                repeat(4) { i ->
                    val angle = i * PI.toFloat() / 2f + PI.toFloat() / 4f
                    val nodeRadius = s * (.35f + .10f * travel)
                    val node = Offset(
                        center.x + cos(angle) * nodeRadius,
                        center.y + sin(angle) * nodeRadius
                    )
                    drawCircle(Color.Black.copy(alpha = .25f * revealIntensity), s * .018f, node)
                    drawCircle(if (i % 2 == 0) secondary else accent, s * .009f, node, alpha = .82f * revealIntensity)
                }
            }
        }
    }
}
