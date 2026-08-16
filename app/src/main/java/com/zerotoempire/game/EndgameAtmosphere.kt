package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Transparent cinematic overlay reserved for post-Galactic eras. */
@Composable
fun EndgameAtmosphere(eraIndex: Int, modifier: Modifier = Modifier) {
    if (eraIndex < 7) return
    val transition = rememberInfiniteTransition(label = "endgameAtmosphere")
    val phase by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(24_000, easing = LinearEasing)), label = "phase")
    val fast by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(8_500, easing = LinearEasing)), label = "fast")

    Canvas(modifier) {
        val w = size.width
        val h = size.height
        val center = Offset(w * .5f, h * .43f)
        val primary = when (eraIndex) {
            7 -> Color(0xFF6DE7FF)
            8 -> Color(0xFFC58CFF)
            9 -> Color(0xFFFF74DD)
            else -> Color(0xFFFFE59A)
        }
        val secondary = when (eraIndex) {
            7 -> Color(0xFF527BFF)
            8 -> Color(0xFFFF68B7)
            9 -> Color(0xFF77FFF1)
            else -> Color.White
        }

        // Large moving nebulae kept subtle so HUD remains readable.
        val driftX = w * (.18f + phase * .64f)
        drawCircle(
            Brush.radialGradient(listOf(primary.copy(alpha = .11f), Color.Transparent), Offset(driftX, h * .22f), w * .38f),
            w * .38f,
            Offset(driftX, h * .22f)
        )
        drawCircle(
            Brush.radialGradient(listOf(secondary.copy(alpha = .07f), Color.Transparent), Offset(w - driftX * .45f, h * .72f), w * .31f),
            w * .31f,
            Offset(w - driftX * .45f, h * .72f)
        )

        when (eraIndex) {
            7 -> {
                // Intergalactic transit lattice.
                repeat(5) { ring ->
                    val r = size.minDimension * (.13f + ring * .075f)
                    drawCircle(primary.copy(alpha = .08f + ring * .014f), r, center, style = Stroke(1.3f + ring * .25f))
                }
                repeat(18) { i ->
                    val a = fast * PI.toFloat() * 2f + i * PI.toFloat() * 2f / 18f
                    val r = size.minDimension * (.18f + (i % 6) * .038f)
                    val p = Offset(center.x + cos(a) * r, center.y + sin(a) * r * .58f)
                    drawCircle(if (i % 3 == 0) secondary else primary, 1.4f + i % 3, p, alpha = .48f)
                }
            }
            8 -> {
                // Cosmic filaments / universe-scale web.
                repeat(22) { i ->
                    val x1 = w * (((i * 37) % 101) / 100f)
                    val y1 = h * (((i * 53) % 97) / 100f)
                    val x2 = w * ((((i + 5) * 61) % 101) / 100f)
                    val y2 = h * ((((i + 3) * 43) % 97) / 100f)
                    drawLine(primary.copy(alpha = .075f), Offset(x1, y1), Offset(x2, y2), 1f)
                    drawCircle(secondary.copy(alpha = .33f), 1.7f, Offset(x1, y1))
                }
            }
            9 -> {
                // Reality Engine: impossible geometric rings and phase gates.
                repeat(4) { i ->
                    val p = (phase + i * .25f) % 1f
                    val r = size.minDimension * (.10f + p * .38f)
                    drawCircle(primary.copy(alpha = (1f - p) * .16f), r, center, style = Stroke(1.5f + (1f-p) * 2.5f))
                }
                repeat(6) { i ->
                    val y = h * (.20f + i * .11f)
                    val offset = sin((fast + i * .13f) * PI.toFloat() * 2f) * w * .09f
                    drawLine(secondary.copy(alpha = .09f), Offset(w*.18f + offset,y), Offset(w*.82f-offset,y), 1.2f)
                }
            }
            else -> {
                // Transcendent: minimal white-gold singularity and lensing arcs.
                drawCircle(
                    Brush.radialGradient(listOf(Color.White.copy(alpha=.22f), primary.copy(alpha=.08f), Color.Transparent), center, size.minDimension*.24f),
                    size.minDimension*.24f,
                    center
                )
                repeat(5) { i ->
                    val pad = size.minDimension * (.08f + i * .035f)
                    drawArc(
                        if(i%2==0) primary.copy(alpha=.15f) else secondary.copy(alpha=.10f),
                        startAngle = -30f + phase*60f + i*22f,
                        sweepAngle = 110f + i*13f,
                        useCenter = false,
                        topLeft = Offset(center.x-pad, center.y-pad*.55f),
                        size = Size(pad*2f,pad*1.1f),
                        style = Stroke(1.1f+i*.25f)
                    )
                }
            }
        }
    }
}
