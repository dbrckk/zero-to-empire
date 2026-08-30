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
fun BusinessGroup03Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
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
    val reveal = remember(id) { Animatable(0f) }
    val previousStage = remember(id) { intArrayOf(stage) }

    LaunchedEffect(stage, reducedMotion) {
        val prior = previousStage[0]
        previousStage[0] = stage
        if (stage > prior && !reducedMotion) {
            reveal.snapTo(1f)
            reveal.animateTo(0f, tween(980))
        } else if (reducedMotion && reveal.value != 0f) {
            reveal.snapTo(0f)
        }
    }

    if (stage == 0) return

    val accent = when (id) {
        8 -> Color(0xFFFFD45A)
        9 -> Color(0xFF5BE6FF)
        10 -> Color(0xFF9F7CFF)
        else -> Color(0xFFFF65D7)
    }
    val secondary = when (id) {
        8 -> Color(0xFFFFF2B0)
        9 -> Color(0xFF8C88FF)
        10 -> Color(0xFF6EEBFF)
        else -> Color(0xFFFFC85A)
    }

    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        val c = Offset(s * .5f, s * .52f)

        if (stage >= 1) {
            drawCircle(accent.copy(alpha = .32f), s * .36f, c, style = Stroke(s * .008f))
            drawCircle(secondary.copy(alpha = .58f), s * .010f, Offset(s * .22f, s * .72f))
            drawCircle(secondary.copy(alpha = .58f), s * .010f, Offset(s * .78f, s * .72f))
        }
        if (stage >= 2) {
            drawArc(secondary.copy(alpha = .48f), 195f, 150f, false, Offset(s * .13f, s * .15f), Size(s * .74f, s * .70f), style = Stroke(s * .009f))
        }
        if (stage >= 3) {
            repeat(4) { i ->
                val x = s * (.29f + i * .14f)
                drawLine(accent.copy(alpha = .45f), Offset(x, s * .68f), Offset(x, s * .34f), s * .005f)
            }
        }
        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(Color.White.copy(alpha = .08f), accent.copy(alpha = .12f), Color.Transparent),
                    center = Offset(s * .42f, s * .37f),
                    radius = s * .50f
                ),
                radius = s * .45f,
                center = c
            )
            drawCircle(accent.copy(alpha = .12f), s * .42f, c)
            drawCircle(secondary.copy(alpha = .36f), s * .43f, c, style = Stroke(s * .008f))
            drawArc(Color.White.copy(alpha = .18f), 208f, 58f, false, Offset(s * .12f, s * .14f), Size(s * .76f, s * .72f), style = Stroke(s * .004f))
        }
        if (stage >= 5) {
            repeat(6) { i ->
                drawCircle(secondary.copy(alpha = .72f), s * .007f, Offset(s * (.25f + i * .10f), s * .18f))
            }
            drawArc(secondary.copy(alpha = .24f), 24f, 112f, false, Offset(s * .095f, s * .115f), Size(s * .81f, s * .77f), style = Stroke(s * .005f))
        }
        if (stage >= 6) {
            drawArc(accent.copy(alpha = .68f), -35f, 250f, false, Offset(s * .07f, s * .07f), Size(s * .86f, s * .86f), style = Stroke(s * .012f))
            drawArc(secondary.copy(alpha = .42f), 165f, 170f, false, Offset(s * .11f, s * .11f), Size(s * .78f, s * .78f), style = Stroke(s * .007f))
            repeat(6) { i ->
                val angle = i * 2f * PI.toFloat() / 6f - PI.toFloat() / 2f
                val node = Offset(c.x + cos(angle) * s * .405f, c.y + sin(angle) * s * .405f)
                drawCircle(Color.Black.copy(alpha = .32f), s * .013f, node)
                drawCircle(if (i % 2 == 0) secondary else accent, s * .0065f, node)
            }
        }
        if (stage >= 7) {
            drawCircle(Color.White.copy(alpha = .10f), s * .48f, c)
            drawCircle(accent.copy(alpha = .24f), s * .475f, c, style = Stroke(s * .018f))
            drawCircle(secondary.copy(alpha = .78f), s * .462f, c, style = Stroke(s * .008f))
            repeat(10) { i ->
                val angle = i * 2f * PI.toFloat() / 10f - PI.toFloat() / 2f
                val node = Offset(c.x + cos(angle) * s * .468f, c.y + sin(angle) * s * .468f)
                drawCircle(Color.Black.copy(alpha = .38f), s * .014f, node)
                drawCircle(if (i % 2 == 0) Color.White.copy(alpha = .92f) else secondary, s * .0065f, node)
            }
        }

        val revealIntensity = reveal.value.coerceIn(0f, 1f)
        if (revealIntensity > 0f) {
            val travel = 1f - revealIntensity
            val gravityRadius = s * (.22f + .25f * travel)

            // Megastructure tiers arrive with a slower, heavier convergence beat: a dense
            // gravity well, two pressure fronts and massive radial braces instead of sparks.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .14f * revealIntensity),
                        accent.copy(alpha = .17f * revealIntensity),
                        secondary.copy(alpha = .07f * revealIntensity),
                        Color.Transparent
                    ),
                    center = c,
                    radius = s * .50f
                ),
                radius = s * (.31f + .12f * travel),
                center = c
            )
            drawCircle(
                color = accent.copy(alpha = .70f * revealIntensity),
                radius = gravityRadius,
                center = c,
                style = Stroke(width = s * (.010f + .008f * revealIntensity))
            )
            drawCircle(
                color = secondary.copy(alpha = .48f * revealIntensity),
                radius = gravityRadius + s * .055f,
                center = c,
                style = Stroke(width = s * .006f)
            )

            val braceCount = 8
            repeat(braceCount) { i ->
                val angle = i * 2f * PI.toFloat() / braceCount + id * .13f
                val inner = s * (.17f + .05f * travel)
                val outer = s * (.34f + .11f * travel)
                drawLine(
                    color = if (i % 2 == 0) accent else secondary,
                    start = Offset(c.x + cos(angle) * inner, c.y + sin(angle) * inner),
                    end = Offset(c.x + cos(angle) * outer, c.y + sin(angle) * outer),
                    strokeWidth = s * if (i % 2 == 0) .010f else .006f,
                    alpha = (.30f + .55f * revealIntensity).coerceAtMost(1f)
                )
            }

            repeat(4) { i ->
                val angle = i * PI.toFloat() / 2f + PI.toFloat() / 4f
                val nodeRadius = s * (.37f + .08f * travel)
                val node = Offset(c.x + cos(angle) * nodeRadius, c.y + sin(angle) * nodeRadius)
                drawCircle(Color.Black.copy(alpha = .34f * revealIntensity), s * .016f, node)
                drawCircle(secondary.copy(alpha = .82f * revealIntensity), s * .0075f, node)
            }
        }
    }
}
