package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun ManagerPortrait(businessId: Int, size: Dp = 58.dp) {
    val accent = when (businessId) {
        0, 1 -> EmpireArtPalette.Gold
        2, 3 -> EmpireArtPalette.Cyan
        4, 5 -> EmpireArtPalette.Violet
        6, 7 -> EmpireArtPalette.Red
        else -> EmpireArtPalette.Magenta
    }
    Box(
        Modifier.size(size).background(
            Brush.radialGradient(listOf(accent.copy(alpha = .28f), EmpireColors.SurfaceHigh, EmpireColors.Void)),
            RoundedCornerShape(size * .32f)
        )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = this.size.minDimension
            drawCircle(accent.copy(alpha = .18f), s * .46f)
            drawCircle(accent.copy(alpha = .55f), s * .42f, style = Stroke(s * .018f))

            val skin = when (businessId % 5) {
                0 -> Color(0xFFE8B98A)
                1 -> Color(0xFFB97A56)
                2 -> Color(0xFFF1C7A0)
                3 -> Color(0xFF8E5A3C)
                else -> Color(0xFFD59A73)
            }
            val hair = when (businessId % 4) {
                0 -> Color(0xFF17191F)
                1 -> Color(0xFF5A3828)
                2 -> Color(0xFFD8C29B)
                else -> Color(0xFF2D2437)
            }

            drawCircle(skin, s * .17f, Offset(s * .5f, s * .38f))
            drawArc(
                color = hair,
                startAngle = 185f,
                sweepAngle = 170f,
                useCenter = true,
                topLeft = Offset(s * .32f, s * .18f),
                size = Size(s * .36f, s * .34f)
            )
            drawCircle(EmpireArtPalette.Ink, s * .015f, Offset(s * .445f, s * .38f))
            drawCircle(EmpireArtPalette.Ink, s * .015f, Offset(s * .555f, s * .38f))
            drawLine(accent, Offset(s * .43f, s * .48f), Offset(s * .57f, s * .48f), s * .018f)

            val torso = Path().apply {
                moveTo(s * .24f, s * .82f)
                quadraticTo(s * .28f, s * .58f, s * .5f, s * .57f)
                quadraticTo(s * .72f, s * .58f, s * .76f, s * .82f)
                close()
            }
            drawPath(torso, EmpireArtPalette.Steel)
            drawPath(torso, accent.copy(alpha = .7f), style = Stroke(s * .025f))
            drawLine(accent, Offset(s * .5f, s * .58f), Offset(s * .5f, s * .78f), s * .02f)

            when (businessId) {
                2, 3 -> {
                    drawCircle(accent, s * .035f, Offset(s * .35f, s * .69f))
                    drawLine(accent, Offset(s * .32f, s * .69f), Offset(s * .38f, s * .69f), s * .012f)
                }
                4, 5 -> {
                    drawRect(accent.copy(alpha = .8f), Offset(s * .31f, s * .65f), Size(s * .11f, s * .07f))
                    drawCircle(EmpireArtPalette.GoldHot, s * .012f, Offset(s * .365f, s * .685f))
                }
                6, 7, 8, 9 -> {
                    drawArc(accent, 190f, 160f, false, Offset(s * .28f, s * .6f), Size(s * .44f, s * .22f), style = Stroke(s * .02f))
                }
            }
        }
    }
}

@Composable
fun EraVista(eraIndex: Int, modifier: Modifier = Modifier) {
    val transition = rememberInfiniteTransition(label = "eraVista")
    val drift by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(20_000, easing = LinearEasing)), label = "drift")
    Canvas(modifier) {
        val w = size.width
        val h = size.height
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1 -> EmpireArtPalette.Cyan
            2 -> Color(0xFFFF9B55)
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }
        drawRect(Brush.verticalGradient(listOf(EmpireColors.DeepSpace, EmpireColors.Void)))
        repeat(22) { i ->
            val x = w * (((i * 37) % 101) / 100f)
            val y = h * (((i * 61) % 83) / 100f) * .65f
            drawCircle(EmpireArtPalette.White.copy(alpha = .25f + (i % 4) * .12f), if (i % 6 == 0) 2f else 1f, Offset(x, y))
        }
        drawCircle(
            Brush.radialGradient(listOf(accent.copy(alpha = .22f), Color.Transparent), center = Offset(w * (.25f + .5f * drift), h * .4f), radius = w * .45f),
            w * .45f,
            Offset(w * (.25f + .5f * drift), h * .4f)
        )

        when (eraIndex) {
            0, 1 -> {
                repeat(9) { i ->
                    val bw = w * (.055f + (i % 3) * .015f)
                    val bh = h * (.16f + (i % 5) * .07f)
                    val x = w * (.03f + i * .105f)
                    drawRect(EmpireArtPalette.Steel, Offset(x, h - bh), Size(bw, bh))
                    repeat(3) { r -> drawCircle(accent.copy(alpha = .7f), 1.7f, Offset(x + bw * .5f, h - bh + 14f + r * 13f)) }
                }
            }
            2 -> {
                repeat(6) { i ->
                    val x = w * (.06f + i * .16f)
                    drawRect(EmpireArtPalette.Steel, Offset(x, h * .55f), Size(w * .11f, h * .35f))
                    drawRect(accent.copy(alpha = .8f), Offset(x + w * .025f, h * .49f), Size(w * .035f, h * .14f))
                }
            }
            3 -> {
                repeat(12) { i ->
                    val x = w * (.02f + i * .082f)
                    val bh = h * (.25f + (i % 5) * .1f)
                    drawRect(EmpireArtPalette.SteelBright.copy(alpha = .8f), Offset(x, h - bh), Size(w * .055f, bh))
                    drawLine(accent, Offset(x + w * .027f, h - bh), Offset(x + w * .027f, h), 2f)
                }
            }
            4 -> {
                drawCircle(accent, h * .28f, Offset(w * .72f, h * .72f))
                drawArc(EmpireArtPalette.GoldHot, 200f, 155f, false, Offset(w * .47f, h * .48f), Size(w * .5f, h * .25f), style = Stroke(4f))
            }
            5 -> {
                drawCircle(EmpireArtPalette.GoldHot, h * .12f, Offset(w * .55f, h * .55f))
                repeat(3) { ring -> drawCircle(accent.copy(alpha = .5f - ring * .1f), h * (.18f + ring * .08f), Offset(w * .55f, h * .55f), style = Stroke(3f)) }
            }
            else -> {
                repeat(4) { arm ->
                    val start = arm * PI.toFloat() / 2f + drift * PI.toFloat() * 2f
                    repeat(18) { j ->
                        val r = j / 18f * h * .42f
                        val a = start + j * .18f
                        drawCircle(if (j % 3 == 0) EmpireArtPalette.Cyan else accent, 1.5f + j * .05f, Offset(w * .5f + cos(a) * r, h * .55f + sin(a) * r * .55f))
                    }
                }
            }
        }
        drawRect(Brush.verticalGradient(listOf(Color.Transparent, EmpireColors.Void.copy(alpha = .75f))), topLeft = Offset(0f, h * .55f), size = Size(w, h * .45f))
    }
}

@Composable
fun CelebrationVfx(accent: String, modifier: Modifier = Modifier) {
    val transition = rememberInfiniteTransition(label = "celebrationVfx")
    val phase by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(1600, easing = LinearEasing)), label = "phase")
    Canvas(modifier) {
        val c = when (accent) {
            "PRESTIGE" -> EmpireArtPalette.Violet
            "NEW ERA", "ERA" -> EmpireArtPalette.GoldHot
            "REWARDED" -> EmpireArtPalette.Cyan
            else -> EmpireArtPalette.Gold
        }
        val center = Offset(size.width / 2f, size.height / 2f)
        val maxR = size.minDimension * .48f
        repeat(4) { i ->
            val p = (phase + i * .25f) % 1f
            drawCircle(c.copy(alpha = (1f - p) * .34f), maxR * p, center, style = Stroke(2f + (1f - p) * 5f))
        }
        repeat(40) { i ->
            val a = i / 40f * PI.toFloat() * 2f + phase * PI.toFloat() * 1.5f
            val r = maxR * (.18f + ((i * 17) % 100) / 100f * .82f) * phase.coerceAtLeast(.18f)
            val p = Offset(center.x + cos(a) * r, center.y + sin(a) * r)
            drawCircle(if (i % 4 == 0) EmpireArtPalette.White else c, 1.5f + (i % 5) * .5f, p)
        }
        drawCircle(Brush.radialGradient(listOf(c.copy(alpha = .22f), Color.Transparent), center = center, radius = maxR), maxR, center)
    }
}
