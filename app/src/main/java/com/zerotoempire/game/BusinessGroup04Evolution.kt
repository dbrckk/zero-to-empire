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
fun BusinessGroup04Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
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
            reveal.animateTo(0f, tween(1120))
        } else if (reducedMotion && reveal.value != 0f) {
            reveal.snapTo(0f)
        }
    }

    if (stage == 0) return

    val accent = if (id == 12) Color(0xFFFF68D8) else Color(0xFFFFE36E)
    val secondary = if (id == 12) Color(0xFF6EEBFF) else Color(0xFFC68BFF)

    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        val c = Offset(s * .5f, s * .51f)

        if (stage >= 1) {
            drawCircle(accent.copy(alpha = .30f), s * .35f, c, style = Stroke(s * .008f))
            drawCircle(secondary.copy(alpha = .68f), s * .008f, Offset(s * .23f, s * .71f))
            drawCircle(secondary.copy(alpha = .68f), s * .008f, Offset(s * .77f, s * .71f))
        }
        if (stage >= 2) {
            drawArc(
                secondary.copy(alpha = .50f),
                205f,
                130f,
                false,
                Offset(s * .15f, s * .14f),
                Size(s * .70f, s * .72f),
                style = Stroke(s * .009f)
            )
        }
        if (stage >= 3) {
            repeat(4) { i ->
                val x = s * (.30f + i * .13f)
                drawLine(accent.copy(alpha = .48f), Offset(x, s * .69f), Offset(x, s * .31f), s * .005f)
            }
        }
        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .05f),
                        accent.copy(alpha = .10f),
                        secondary.copy(alpha = .04f),
                        Color.Transparent
                    ),
                    center = c,
                    radius = s * .47f
                ),
                radius = s * .47f,
                center = c
            )
            drawCircle(secondary.copy(alpha = .40f), s * .43f, c, style = Stroke(s * .008f))
            drawCircle(accent.copy(alpha = .18f), s * .395f, c, style = Stroke(s * .005f))
        }
        if (stage >= 5) {
            repeat(6) { i ->
                val a = -PI.toFloat() * .82f + i * PI.toFloat() * .164f
                val radius = s * .405f
                val p = Offset(c.x + cos(a) * radius, c.y + sin(a) * radius)
                drawCircle(Color.White.copy(alpha = .82f), s * .007f, p)
                drawCircle(secondary.copy(alpha = .32f), s * .014f, p, style = Stroke(s * .004f))
            }
        }
        if (stage >= 6) {
            drawArc(
                accent.copy(alpha = .72f),
                -30f,
                255f,
                false,
                Offset(s * .065f, s * .065f),
                Size(s * .87f, s * .87f),
                style = Stroke(s * .012f)
            )
            drawArc(
                secondary.copy(alpha = .48f),
                160f,
                175f,
                false,
                Offset(s * .105f, s * .105f),
                Size(s * .79f, s * .79f),
                style = Stroke(s * .007f)
            )
            repeat(8) { i ->
                val a = i * 2f * PI.toFloat() / 8f + .18f
                val r = if (i % 2 == 0) s * .445f else s * .418f
                val p = Offset(c.x + cos(a) * r, c.y + sin(a) * r)
                drawCircle(
                    color = if (i % 2 == 0) accent else secondary,
                    radius = if (i % 2 == 0) s * .008f else s * .006f,
                    center = p,
                    alpha = .86f
                )
            }
        }
        if (stage >= 7) {
            drawCircle(Color.White.copy(alpha = .08f), s * .49f, c)
            drawCircle(Color.White.copy(alpha = .86f), s * .475f, c, style = Stroke(s * .010f))
            drawCircle(accent.copy(alpha = .34f), s * .458f, c, style = Stroke(s * .0045f))

            repeat(12) { i ->
                val a = -PI.toFloat() / 2f + i * 2f * PI.toFloat() / 12f
                val inner = s * .462f
                val outer = s * if (i % 3 == 0) .515f else .495f
                val start = Offset(c.x + cos(a) * inner, c.y + sin(a) * inner)
                val end = Offset(c.x + cos(a) * outer, c.y + sin(a) * outer)
                drawLine(
                    color = if (i % 2 == 0) accent else secondary,
                    start = start,
                    end = end,
                    strokeWidth = if (i % 3 == 0) s * .009f else s * .005f,
                    alpha = if (i % 3 == 0) .88f else .62f
                )
                drawCircle(
                    color = if (i % 2 == 0) Color.White else secondary,
                    radius = if (i % 3 == 0) s * .007f else s * .005f,
                    center = end,
                    alpha = .90f
                )
            }
        }

        val revealIntensity = reveal.value.coerceIn(0f, 1f)
        if (revealIntensity > 0f) {
            val travel = 1f - revealIntensity
            val waveRadius = s * (.18f + .34f * travel)

            // Endgame tiers arrive as a controlled singularity release rather than a generic
            // particle burst, keeping the final businesses visually distinct and premium.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .20f * revealIntensity),
                        accent.copy(alpha = .18f * revealIntensity),
                        secondary.copy(alpha = .10f * revealIntensity),
                        Color.Transparent
                    ),
                    center = c,
                    radius = s * .52f
                ),
                radius = s * (.26f + .20f * travel),
                center = c
            )
            drawCircle(
                color = Color.White.copy(alpha = .72f * revealIntensity),
                radius = waveRadius,
                center = c,
                style = Stroke(width = s * (.010f + .010f * revealIntensity))
            )
            drawCircle(
                color = accent.copy(alpha = .62f * revealIntensity),
                radius = waveRadius + s * .045f,
                center = c,
                style = Stroke(width = s * .006f)
            )
            drawCircle(
                color = secondary.copy(alpha = .38f * revealIntensity),
                radius = waveRadius + s * .080f,
                center = c,
                style = Stroke(width = s * .004f)
            )

            val rayCount = 12
            repeat(rayCount) { i ->
                val angle = -PI.toFloat() / 2f + i * 2f * PI.toFloat() / rayCount + id * .09f
                val inner = s * (.12f + .07f * travel)
                val outer = s * (.31f + .18f * travel)
                drawLine(
                    color = when (i % 3) {
                        0 -> Color.White
                        1 -> accent
                        else -> secondary
                    },
                    start = Offset(c.x + cos(angle) * inner, c.y + sin(angle) * inner),
                    end = Offset(c.x + cos(angle) * outer, c.y + sin(angle) * outer),
                    strokeWidth = s * if (i % 3 == 0) .008f else .005f,
                    alpha = (.22f + .66f * revealIntensity).coerceAtMost(1f)
                )
            }

            repeat(6) { i ->
                val angle = i * PI.toFloat() / 3f + PI.toFloat() / 6f
                val nodeRadius = s * (.30f + .17f * travel)
                val node = Offset(c.x + cos(angle) * nodeRadius, c.y + sin(angle) * nodeRadius)
                drawCircle(Color.Black.copy(alpha = .28f * revealIntensity), s * .017f, node)
                drawCircle(Color.White.copy(alpha = .92f * revealIntensity), s * .0065f, node)
            }
        }
    }
}
