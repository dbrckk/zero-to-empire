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
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Transparent cinematic layer reserved for post-galactic progression. */
@Composable
fun EndgameEraAmbient(eraIndex: Int, modifier: Modifier = Modifier) {
    if (eraIndex < 7) return
    val motion = rememberInfiniteTransition(label = "endgameEra$eraIndex")
    val phase by motion.animateFloat(0f, 1f, infiniteRepeatable(tween(24_000, easing = LinearEasing)), label = "phase")
    val pulse by motion.animateFloat(.55f, 1f, infiniteRepeatable(tween(2600)), label = "pulse")

    Canvas(modifier) {
        val w = size.width
        val h = size.height
        val center = Offset(w * .5f, h * .42f)
        val accent = when (eraIndex) {
            7 -> Color(0xFF66E6FF)
            8 -> Color(0xFFC28CFF)
            9 -> Color(0xFFFF6ACF)
            else -> Color(0xFFFFE37A)
        }

        drawRect(Brush.radialGradient(listOf(accent.copy(alpha=.09f*pulse), Color.Transparent), center, w*.82f))

        when (eraIndex) {
            7 -> { // intergalactic bridge network
                repeat(6) { arm ->
                    val a0 = arm * PI.toFloat() / 3f + phase * PI.toFloat() * .28f
                    repeat(12) { j ->
                        val r1 = w * (.07f + j * .027f)
                        val r2 = r1 + w * .022f
                        val a = a0 + j * .07f
                        val p1 = Offset(center.x + cos(a) * r1, center.y + sin(a) * r1 * .42f)
                        val p2 = Offset(center.x + cos(a+.08f) * r2, center.y + sin(a+.08f) * r2 * .42f)
                        drawLine(accent.copy(alpha=.17f), p1, p2, 1.4f)
                        if (j % 3 == 0) drawCircle(Color.White.copy(alpha=.35f), 1.6f, p1)
                    }
                }
            }
            8 -> { // cosmic lattice / void geometry
                repeat(5) { ring ->
                    val r = w * (.12f + ring * .075f)
                    drawCircle(accent.copy(alpha=.10f + ring*.018f), r, center, style=Stroke(1.2f))
                }
                repeat(10) { i ->
                    val a = phase * 2f * PI.toFloat() + i * PI.toFloat() / 5f
                    val p = Offset(center.x + cos(a) * w*.34f, center.y + sin(a) * w*.17f)
                    drawCircle(Color.White.copy(alpha=.30f), 2f, p)
                }
            }
            9 -> { // reality engine: rotating impossible machinery
                repeat(3) { ring ->
                    val r = w * (.16f + ring*.08f)
                    drawArc(accent.copy(alpha=.17f+ring*.025f), phase*360f*(if(ring%2==0)1 else -1), 235f, false,
                        Offset(center.x-r, center.y-r*.48f), Size(r*2f,r*.96f), style=Stroke(2f+ring))
                }
                repeat(8) { i ->
                    val a = phase * PI.toFloat()*2f + i*PI.toFloat()/4f
                    val p1 = Offset(center.x+cos(a)*w*.13f, center.y+sin(a)*w*.07f)
                    val p2 = Offset(center.x+cos(a)*w*.31f, center.y+sin(a)*w*.16f)
                    drawLine(Color.White.copy(alpha=.14f),p1,p2,1.3f)
                }
            }
            else -> { // transcendent: luminous horizon / fractal crown
                repeat(7) { i ->
                    val a = -PI.toFloat()/2f + (i-3)*.17f
                    val inner = w*.12f
                    val outer = w*(.32f + (i%2)*.05f)
                    drawLine(accent.copy(alpha=.14f*pulse),
                        Offset(center.x+cos(a)*inner,center.y+sin(a)*inner),
                        Offset(center.x+cos(a)*outer,center.y+sin(a)*outer),2f)
                }
                val crown = Path().apply {
                    moveTo(w*.28f,h*.31f); lineTo(w*.38f,h*.19f); lineTo(w*.46f,h*.29f); lineTo(w*.52f,h*.15f); lineTo(w*.60f,h*.29f); lineTo(w*.70f,h*.19f); lineTo(w*.76f,h*.31f)
                }
                drawPath(crown, accent.copy(alpha=.18f*pulse), style=Stroke(2.2f))
                drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.10f*pulse),accent.copy(alpha=.08f),Color.Transparent),center,w*.25f),w*.25f,center)
            }
        }
    }
}
