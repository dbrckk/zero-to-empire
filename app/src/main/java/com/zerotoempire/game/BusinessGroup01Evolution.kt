package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
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

/** Extra structural layers that make each progression tier visibly change silhouette. */
@Composable
fun BusinessGroup01Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
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
            reveal.animateTo(0f, tween(760))
        } else if (reducedMotion && reveal.value != 0f) {
            reveal.snapTo(0f)
        }
    }

    if (stage == 0) return

    val accent = when (id) {
        0 -> Color(0xFF78F56A)
        1 -> Color(0xFF58BFFF)
        2 -> Color(0xFFFF9A43)
        else -> Color(0xFFB76CFF)
    }
    val secondary = when (id) {
        0 -> Color(0xFFFFE87A)
        1 -> Color(0xFFB8F1FF)
        2 -> Color(0xFFFFD073)
        else -> Color(0xFFFF72D8)
    }

    Canvas(modifier.size(iconSize)) {
        val s = size.minDimension
        val center = Offset(s * .5f, s * .5f)

        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(Color.White.copy(alpha = .07f), accent.copy(alpha = .09f), Color.Transparent),
                    center = Offset(s * .42f, s * .36f),
                    radius = s * .47f
                ),
                radius = s * .455f,
                center = center
            )
            drawArc(
                secondary.copy(alpha = .24f),
                214f,
                50f,
                false,
                Offset(s * .10f, s * .10f),
                Size(s * .80f, s * .80f),
                style = Stroke(s * .005f)
            )
        }
        if (stage >= 6) {
            drawArc(
                accent.copy(alpha = .30f),
                20f,
                112f,
                false,
                Offset(s * .08f, s * .08f),
                Size(s * .84f, s * .84f),
                style = Stroke(s * .006f)
            )
            drawArc(
                Color.White.copy(alpha = .18f),
                198f,
                68f,
                false,
                Offset(s * .125f, s * .125f),
                Size(s * .75f, s * .75f),
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
                drawCircle(Color.Black.copy(alpha = .32f), s * .014f, node)
                drawCircle(if (i % 2 == 0) secondary else accent, s * .007f, node)
            }
        }

        when (id) {
            0 -> {
                val green = Color(0xFF78F56A)
                if (stage >= 1) {
                    drawLine(green.copy(alpha = .8f), Offset(s * .14f, s * .76f), Offset(s * .86f, s * .76f), s * .012f)
                    drawCircle(green.copy(alpha = .75f), s * .018f, Offset(s * .17f, s * .75f))
                    drawCircle(green.copy(alpha = .75f), s * .018f, Offset(s * .83f, s * .75f))
                }
                if (stage >= 2) {
                    drawRoundRect(Color(0xFF385A31), Offset(s * .12f, s * .52f), Size(s * .10f, s * .18f), CornerRadius(s * .015f))
                    drawRoundRect(Color(0xFF385A31), Offset(s * .78f, s * .52f), Size(s * .10f, s * .18f), CornerRadius(s * .015f))
                }
                if (stage >= 3) {
                    drawLine(Color(0xFFFFD66B), Offset(s * .17f, s * .20f), Offset(s * .83f, s * .20f), s * .012f)
                    repeat(5) { i -> drawCircle(Color(0xFFFFEAA0), s * .009f, Offset(s * (.22f + i * .14f), s * .20f)) }
                }
                if (stage >= 4) {
                    drawRoundRect(green.copy(alpha = .25f), Offset(s * .08f, s * .34f), Size(s * .12f, s * .38f), CornerRadius(s * .025f), style = Stroke(s * .012f))
                    drawRoundRect(green.copy(alpha = .25f), Offset(s * .80f, s * .34f), Size(s * .12f, s * .38f), CornerRadius(s * .025f), style = Stroke(s * .012f))
                }
                if (stage >= 5) {
                    drawLine(green.copy(alpha = .62f), Offset(s * .24f, s * .14f), Offset(s * .24f, s * .33f), s * .009f)
                    drawLine(green.copy(alpha = .62f), Offset(s * .76f, s * .14f), Offset(s * .76f, s * .33f), s * .009f)
                }
                if (stage >= 6) {
                    repeat(3) { i -> drawCircle(Color(0xFFFFE87A).copy(alpha = .62f), s * (.30f + i * .055f), Offset(s * .5f, s * .5f), style = Stroke(s * .008f)) }
                }
                if (stage >= 7) drawCircle(Color(0xFFFFE87A).copy(alpha = .82f), s * .455f, Offset(s * .5f, s * .5f), style = Stroke(s * .016f))
            }

            1 -> {
                val blue = Color(0xFF58BFFF)
                if (stage >= 1) drawRoundRect(blue.copy(alpha = .25f), Offset(s * .15f, s * .27f), Size(s * .70f, s * .50f), CornerRadius(s * .035f), style = Stroke(s * .012f))
                if (stage >= 2) {
                    drawRoundRect(Color(0xFF28445E), Offset(s * .24f, s * .19f), Size(s * .52f, s * .09f), CornerRadius(s * .02f))
                    repeat(4) { i -> drawCircle(blue, s * .009f, Offset(s * (.34f + i * .11f), s * .235f)) }
                }
                if (stage >= 3) {
                    drawLine(blue.copy(alpha = .8f), Offset(s * .12f, s * .74f), Offset(s * .88f, s * .74f), s * .012f)
                    drawCircle(Color.White.copy(alpha = .85f), s * .015f, Offset(s * .15f, s * .74f))
                    drawCircle(Color.White.copy(alpha = .85f), s * .015f, Offset(s * .85f, s * .74f))
                }
                if (stage >= 4) {
                    drawRoundRect(blue.copy(alpha = .18f), Offset(s * .09f, s * .38f), Size(s * .10f, s * .31f), CornerRadius(s * .015f))
                    drawRoundRect(blue.copy(alpha = .18f), Offset(s * .81f, s * .38f), Size(s * .10f, s * .31f), CornerRadius(s * .015f))
                }
                if (stage >= 5) {
                    drawLine(blue.copy(alpha = .70f), Offset(s * .20f, s * .16f), Offset(s * .32f, s * .26f), s * .009f)
                    drawLine(blue.copy(alpha = .70f), Offset(s * .80f, s * .16f), Offset(s * .68f, s * .26f), s * .009f)
                }
                if (stage >= 6) {
                    repeat(3) { i -> drawCircle(Color(0xFFB8F1FF).copy(alpha = .58f), s * (.30f + i * .055f), Offset(s * .5f, s * .5f), style = Stroke(s * .008f)) }
                }
                if (stage >= 7) drawCircle(Color(0xFFB8F1FF).copy(alpha = .84f), s * .455f, Offset(s * .5f, s * .5f), style = Stroke(s * .015f))
            }

            2 -> {
                val orange = Color(0xFFFF9A43)
                if (stage >= 1) drawRoundRect(Color(0xFF343A40), Offset(s * .11f, s * .51f), Size(s * .10f, s * .22f), CornerRadius(s * .012f))
                if (stage >= 2) drawRoundRect(Color(0xFF4A5058), Offset(s * .72f, s * .25f), Size(s * .09f, s * .26f), CornerRadius(s * .012f))
                if (stage >= 3) {
                    repeat(3) { i -> drawCircle(orange.copy(alpha = .7f), s * .026f, Offset(s * (.26f + i * .24f), s * .77f), style = Stroke(s * .010f)) }
                    drawLine(orange.copy(alpha = .75f), Offset(s * .15f, s * .78f), Offset(s * .85f, s * .78f), s * .011f)
                }
                if (stage >= 4) {
                    drawRoundRect(orange.copy(alpha = .20f), Offset(s * .08f, s * .30f), Size(s * .12f, s * .44f), CornerRadius(s * .018f), style = Stroke(s * .012f))
                    drawRoundRect(orange.copy(alpha = .20f), Offset(s * .80f, s * .30f), Size(s * .12f, s * .44f), CornerRadius(s * .018f), style = Stroke(s * .012f))
                }
                if (stage >= 5) {
                    drawLine(orange.copy(alpha = .65f), Offset(s * .20f, s * .20f), Offset(s * .20f, s * .37f), s * .009f)
                    drawLine(orange.copy(alpha = .65f), Offset(s * .84f, s * .20f), Offset(s * .84f, s * .37f), s * .009f)
                }
                if (stage >= 6) {
                    repeat(3) { i -> drawCircle(Color(0xFFFFD073).copy(alpha = .60f), s * (.30f + i * .055f), Offset(s * .5f, s * .5f), style = Stroke(s * .008f)) }
                }
                if (stage >= 7) drawCircle(Color(0xFFFFD073).copy(alpha = .84f), s * .455f, Offset(s * .5f, s * .5f), style = Stroke(s * .016f))
            }

            3 -> {
                val violet = Color(0xFFB76CFF)
                if (stage >= 1) {
                    drawRoundRect(Color(0xFF444855), Offset(s * .09f, s * .48f), Size(s * .12f, s * .27f), CornerRadius(s * .018f))
                    drawRoundRect(Color(0xFF444855), Offset(s * .79f, s * .48f), Size(s * .12f, s * .27f), CornerRadius(s * .018f))
                }
                if (stage >= 2) repeat(2) { i -> drawRoundRect(Color(0xFF626879), Offset(s * (.17f + i * .58f), s * .23f), Size(s * .07f, s * .28f), CornerRadius(s * .010f)) }
                if (stage >= 3) {
                    drawLine(violet.copy(alpha = .8f), Offset(s * .10f, s * .77f), Offset(s * .90f, s * .77f), s * .013f)
                    repeat(5) { i -> drawCircle(Color(0xFFFF72D8), s * .010f, Offset(s * (.25f + i * .125f), s * .77f)) }
                }
                if (stage >= 4) {
                    drawRoundRect(violet.copy(alpha = .20f), Offset(s * .07f, s * .32f), Size(s * .10f, s * .42f), CornerRadius(s * .018f), style = Stroke(s * .012f))
                    drawRoundRect(violet.copy(alpha = .20f), Offset(s * .83f, s * .32f), Size(s * .10f, s * .42f), CornerRadius(s * .018f), style = Stroke(s * .012f))
                }
                if (stage >= 5) {
                    drawLine(Color(0xFFFF72D8).copy(alpha = .68f), Offset(s * .22f, s * .18f), Offset(s * .31f, s * .31f), s * .009f)
                    drawLine(Color(0xFFFF72D8).copy(alpha = .68f), Offset(s * .78f, s * .18f), Offset(s * .69f, s * .31f), s * .009f)
                }
                if (stage >= 6) {
                    repeat(3) { i -> drawCircle(Color(0xFFFF72D8).copy(alpha = .56f), s * (.30f + i * .055f), Offset(s * .5f, s * .5f), style = Stroke(s * .008f)) }
                }
                if (stage >= 7) drawCircle(Color(0xFFFF72D8).copy(alpha = .82f), s * .46f, Offset(s * .5f, s * .5f), style = Stroke(s * .016f))
            }
        }

        val revealIntensity = reveal.value.coerceIn(0f, 1f)
        if (revealIntensity > 0f) {
            val travel = 1f - revealIntensity
            val ringRadius = s * (.30f + .18f * travel)

            // A short materialization beat makes a tier unlock read as a true transformation,
            // without creating another permanent animation loop.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .18f * revealIntensity),
                        accent.copy(alpha = .14f * revealIntensity),
                        Color.Transparent
                    ),
                    center = center,
                    radius = s * .48f
                ),
                radius = s * (.34f + .10f * travel),
                center = center
            )
            drawCircle(
                color = secondary.copy(alpha = .74f * revealIntensity),
                radius = ringRadius,
                center = center,
                style = Stroke(width = s * (.010f + .008f * revealIntensity))
            )
            drawCircle(
                color = Color.White.copy(alpha = .42f * revealIntensity),
                radius = s * (.25f + .14f * travel),
                center = center,
                style = Stroke(width = s * .005f)
            )

            val rayCount = 8 + stage.coerceAtMost(4) * 2
            repeat(rayCount) { i ->
                val angle = 2f * PI.toFloat() * i / rayCount - PI.toFloat() / 2f
                val inner = s * (.28f + .04f * travel)
                val outer = s * (.36f + .12f * travel)
                drawLine(
                    color = if (i % 2 == 0) accent else secondary,
                    start = Offset(center.x + cos(angle) * inner, center.y + sin(angle) * inner),
                    end = Offset(center.x + cos(angle) * outer, center.y + sin(angle) * outer),
                    strokeWidth = s * .007f,
                    alpha = .58f * revealIntensity
                )
            }
        }
    }
}
