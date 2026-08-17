package com.zerotoempire.game

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.material3.Text
import androidx.compose.ui.unit.sp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun PowerCoreTrailField(modifier: Modifier = Modifier) {
    val transition = rememberInfiniteTransition(label = "coreTrails")
    val phase by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(2600, easing = LinearEasing)), label = "trailPhase")
    Canvas(modifier) {
        val c = Offset(size.width / 2f, size.height / 2f)
        val r = size.minDimension * .34f
        repeat(18) { i ->
            val p = (phase + i / 18f) % 1f
            val a = p * (Math.PI * 2.0).toFloat() + i * .31f
            val rr = r * (.55f + .45f * p)
            val pos = Offset(c.x + cos(a) * rr, c.y + sin(a) * rr)
            val alpha = (1f - p) * .8f
            drawCircle(
                color = if (i % 3 == 0) EmpireArtPalette.Cyan.copy(alpha = alpha) else EmpireArtPalette.Gold.copy(alpha = alpha),
                radius = 1.5f + (1f - p) * 4f,
                center = pos
            )
        }
        repeat(3) { ring ->
            drawCircle(
                color = EmpireArtPalette.Gold.copy(alpha = .18f - ring * .035f),
                radius = r * (.72f + ring * .18f),
                center = c,
                style = Stroke(2f + ring)
            )
        }
    }
}

/** Full-screen celebration field used by milestone, reward and prestige overlays. */
@Composable
fun CelebrationVfx(accentName: String, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val transition = rememberInfiniteTransition(label = "celebration-$accentName")
    val animated by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 5200 else 3200, easing = LinearEasing)), label = "celebrationPhase")
    val phase = if (reduced) .22f else animated
    val accent = when (accentName.uppercase()) {
        "PRESTIGE", "ASCENSION" -> EmpireArtPalette.Violet
        "REWARDED", "REWARD" -> EmpireArtPalette.Cyan
        "MILESTONE" -> EmpireArtPalette.GoldHot
        "UNLOCK" -> EmpireArtPalette.Magenta
        else -> EmpireArtPalette.Gold
    }
    Canvas(modifier) {
        val c = Offset(size.width / 2f, size.height / 2f)
        val min = size.minDimension
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha = .24f), Color.Transparent), c, min * .62f), min * .62f, c)
        repeat(4) { ring ->
            val p = (phase + ring * .18f) % 1f
            drawCircle(accent.copy(alpha = (1f - p) * .34f), min * (.12f + p * .48f), c, style = Stroke(2f + ring))
        }
        val rays = if (lowPower) 12 else 24
        repeat(rays) { i ->
            val a = i * (2f * PI.toFloat() / rays) + phase * .35f
            val inner = min * .16f
            val outer = min * (.34f + (i % 4) * .035f)
            drawLine(
                color = if (i % 3 == 0) Color.White.copy(alpha = .42f) else accent.copy(alpha = .40f),
                start = Offset(c.x + cos(a) * inner, c.y + sin(a) * inner),
                end = Offset(c.x + cos(a) * outer, c.y + sin(a) * outer),
                strokeWidth = if (i % 3 == 0) 2.6f else 1.4f
            )
        }
        val sparks = if (lowPower) 18 else 42
        repeat(sparks) { i ->
            val a = i * 2f * PI.toFloat() / sparks + phase * 2f
            val wave = ((i * 37) % 100) / 100f
            val r = min * (.22f + .35f * wave)
            drawCircle(
                color = if (i % 5 == 0) Color.White.copy(alpha = .85f) else accent.copy(alpha = .72f),
                radius = if (i % 7 == 0) 3.2f else 1.7f,
                center = Offset(c.x + cos(a) * r, c.y + sin(a) * r)
            )
        }
    }
}

@Composable
fun EraTransitionOverlay(eraIndex: Int, visible: Boolean, modifier: Modifier = Modifier) {
    AnimatedVisibility(visible = visible, enter = fadeIn(tween(180)), exit = fadeOut(tween(520)), modifier = modifier) {
        val transition = rememberInfiniteTransition(label = "eraTransition")
        val phase by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(1200, easing = LinearEasing)), label = "eraPhase")
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1, 2 -> EmpireArtPalette.Cyan
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }
        Box(
            Modifier.fillMaxSize().background(
                Brush.radialGradient(listOf(accent.copy(alpha = .55f), EmpireColors.Void.copy(alpha = .94f)), radius = 1400f)
            ),
            contentAlignment = Alignment.Center
        ) {
            Canvas(Modifier.fillMaxSize()) {
                val c = Offset(size.width / 2f, size.height / 2f)
                repeat(4) { i ->
                    drawCircle(accent.copy(alpha = .45f - i * .08f), size.minDimension * (.12f + phase * .55f + i * .08f), c, style = Stroke(3f + i))
                }
                repeat(36) { i ->
                    val a = i * (Math.PI * 2.0 / 36.0).toFloat()
                    val d = size.minDimension * (.12f + phase * .62f)
                    drawCircle(accent.copy(alpha = (1f - phase) * .85f), 2f + (i % 4), Offset(c.x + cos(a) * d, c.y + sin(a) * d))
                }
            }
            Text("ERA ASCENDED", color = Color.White, fontSize = 28.sp, fontWeight = FontWeight.Black)
        }
    }
}
