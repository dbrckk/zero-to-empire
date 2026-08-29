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
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
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
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun PowerCoreTrailField(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = if (reduced) {
        .18f
    } else {
        val transition = rememberInfiniteTransition(label = "coreTrails")
        val animated by transition.animateFloat(
            0f,
            1f,
            infiniteRepeatable(tween(if (lowPower) 4200 else 2600, easing = LinearEasing)),
            label = "trailPhase"
        )
        animated
    }
    Canvas(modifier) {
        val c = Offset(size.width / 2f, size.height / 2f)
        val r = size.minDimension * .34f
        val trailCount = if (lowPower) 9 else 18
        repeat(trailCount) { i ->
            val p = (phase + i / trailCount.toFloat()) % 1f
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
    val phase = if (reduced) {
        .22f
    } else {
        val transition = rememberInfiniteTransition(label = "celebration-$accentName")
        val animated by transition.animateFloat(
            0f,
            1f,
            infiniteRepeatable(tween(if (lowPower) 5200 else 3200, easing = LinearEasing)),
            label = "celebrationPhase"
        )
        animated
    }
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
    AnimatedVisibility(
        visible = visible,
        enter = fadeIn(tween(180)),
        exit = fadeOut(tween(520)),
        modifier = modifier
    ) {
        val context = LocalContext.current
        val reduced = MotionQuality.reducedMotion(context)
        val lowPower = MotionQuality.lowPowerMode(context)
        val era = EmpireEras.catalog.getOrElse(eraIndex.coerceAtLeast(0)) { EmpireEras.catalog.last() }
        val phase = if (reduced || lowPower) {
            .48f
        } else {
            val transition = rememberInfiniteTransition(label = "eraTransition")
            val animated by transition.animateFloat(
                0f,
                1f,
                infiniteRepeatable(tween(1250, easing = LinearEasing)),
                label = "eraPhase"
            )
            animated
        }
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1, 2 -> EmpireArtPalette.Cyan
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }

        Box(
            Modifier.fillMaxSize().background(EmpireColors.Void),
            contentAlignment = Alignment.Center
        ) {
            EraVistaAAA(era.index, Modifier.fillMaxSize())
            Box(
                Modifier.fillMaxSize().background(
                    Brush.verticalGradient(
                        listOf(
                            EmpireColors.Void.copy(alpha = .34f),
                            EmpireColors.DeepSpace.copy(alpha = .48f),
                            EmpireColors.Void.copy(alpha = .94f)
                        )
                    )
                )
            )
            Canvas(Modifier.fillMaxSize()) {
                val c = Offset(size.width / 2f, size.height * .43f)
                val min = size.minDimension
                repeat(if (lowPower) 2 else 4) { i ->
                    val p = (phase + i * .16f) % 1f
                    drawCircle(
                        accent.copy(alpha = (1f - p) * .42f),
                        min * (.10f + p * .52f),
                        c,
                        style = Stroke(2.5f + i)
                    )
                }
                val particleCount = if (lowPower) 14 else 34
                repeat(particleCount) { i ->
                    val a = i * (Math.PI * 2.0 / particleCount).toFloat() + phase * .7f
                    val spread = min * (.18f + ((i * 17) % 100) / 100f * .34f)
                    drawCircle(
                        color = if (i % 4 == 0) Color.White.copy(alpha = .78f) else accent.copy(alpha = .64f),
                        radius = if (i % 6 == 0) 3.2f else 1.8f,
                        center = Offset(c.x + cos(a) * spread, c.y + sin(a) * spread)
                    )
                }
            }

            Surface(
                color = EmpireColors.DeepSpace.copy(alpha = .84f),
                shape = RoundedCornerShape(28.dp),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 26.dp)
                    .border(1.dp, accent.copy(alpha = .48f), RoundedCornerShape(28.dp))
            ) {
                Column(
                    Modifier.padding(horizontal = 24.dp, vertical = 22.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        "ERA ${era.index + 1} OF ${EmpireEras.catalog.size}",
                        color = accent,
                        fontSize = 10.sp,
                        fontWeight = FontWeight.Black,
                        letterSpacing = 2.1.sp
                    )
                    Spacer(Modifier.height(5.dp))
                    Text(
                        era.icon,
                        color = Color.White,
                        fontSize = 38.sp,
                        fontWeight = FontWeight.Black
                    )
                    Spacer(Modifier.height(4.dp))
                    Text(
                        era.name,
                        color = Color.White,
                        fontSize = 28.sp,
                        fontWeight = FontWeight.Black,
                        textAlign = TextAlign.Center
                    )
                    Spacer(Modifier.height(7.dp))
                    Text(
                        era.subtitle,
                        color = EmpireColors.TextSecondary,
                        fontSize = 13.sp,
                        fontWeight = FontWeight.Bold,
                        textAlign = TextAlign.Center,
                        lineHeight = 18.sp
                    )
                    Spacer(Modifier.height(13.dp))
                    Text(
                        "NEW ECONOMIC HORIZON UNLOCKED",
                        color = accent,
                        fontSize = 9.sp,
                        fontWeight = FontWeight.Black,
                        letterSpacing = 1.4.sp
                    )
                }
            }
        }
    }
}
