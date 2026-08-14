package com.zerotoempire.game

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.*
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import kotlin.math.cos
import kotlin.math.sin

object EmpireArtPalette {
    val Ink = Color(0xFF07101E)
    val Steel = Color(0xFF1A2C45)
    val SteelBright = Color(0xFF3A587A)
    val Gold = Color(0xFFFFC857)
    val GoldHot = Color(0xFFFFE6A1)
    val Cyan = Color(0xFF57E7F2)
    val Violet = Color(0xFFA58BFF)
    val Magenta = Color(0xFFFF6ED6)
    val Red = Color(0xFFFF6D68)
    val White = Color(0xFFF6FBFF)
}

@Composable
fun BusinessArtIcon(id: Int, level: Int = 0, iconSize: Dp = 54.dp, modifier: Modifier = Modifier) {
    val transition = rememberInfiniteTransition(label = "businessArt$id")
    val pulse by transition.animateFloat(
        initialValue = .82f,
        targetValue = 1f,
        animationSpec = infiniteRepeatable(tween(1800 + id * 90), RepeatMode.Reverse),
        label = "pulse"
    )
    Box(
        modifier = modifier.size(iconSize).background(
            Brush.radialGradient(listOf(EmpireColors.SurfaceHigh, EmpireColors.Surface, EmpireColors.Void)),
            RoundedCornerShape(iconSize * .28f)
        )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val glow = when (id) {
                0, 1 -> EmpireArtPalette.Gold
                2, 3 -> EmpireArtPalette.Cyan
                4, 5 -> EmpireArtPalette.Violet
                6, 7 -> EmpireArtPalette.Red
                else -> EmpireArtPalette.Magenta
            }
            val tier = when {
                level >= 500 -> 4
                level >= 100 -> 3
                level >= 50 -> 2
                level >= 10 -> 1
                else -> 0
            }
            drawCircle(glow.copy(alpha = (.12f + tier * .035f) * pulse), radius = s * (.42f + tier * .018f))
            drawCircle(glow.copy(alpha = .34f + tier * .08f), radius = s * .38f, style = Stroke(s * (.022f + tier * .004f)))
            if (tier >= 1) drawCircle(EmpireArtPalette.White.copy(alpha = .16f * pulse), s * .46f, style = Stroke(s * .012f))
            if (tier >= 2) {
                repeat(4) { i ->
                    val a = (i * Math.PI / 2.0).toFloat()
                    drawCircle(glow.copy(alpha = .72f), s * .022f, Offset(s*.5f + cos(a)*s*.44f, s*.5f + sin(a)*s*.44f))
                }
            }
            if (tier >= 3) {
                drawArc(EmpireArtPalette.GoldHot.copy(alpha = .55f), -35f, 250f, false, Offset(s*.08f,s*.08f), Size(s*.84f,s*.84f), style = Stroke(s*.015f))
            }
            if (tier >= 4) {
                repeat(8) { i ->
                    val a = (i * Math.PI / 4.0).toFloat()
                    drawLine(glow.copy(alpha=.65f), Offset(s*.5f+cos(a)*s*.39f,s*.5f+sin(a)*s*.39f), Offset(s*.5f+cos(a)*s*.49f,s*.5f+sin(a)*s*.49f), s*.012f)
                }
            }
            when (id) {
                0 -> drawStreetStand(glow)
                1 -> drawStore(glow)
                2 -> drawWorkshop(glow)
                3 -> drawFactory(glow)
                4 -> drawTech(glow)
                5 -> drawCity(glow)
                6 -> drawMoon(glow)
                7 -> drawPlanet(glow)
                8 -> drawDyson(glow)
                else -> drawGalaxy(glow)
            }
        }
    }
}

@Composable
fun EmpireAmbientBackdrop(eraIndex: Int, modifier: Modifier = Modifier) {
    val transition = rememberInfiniteTransition(label = "empireAmbient")
    val phase by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(18_000, easing = LinearEasing)), label = "ambientPhase")
    Canvas(modifier) {
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1, 2 -> EmpireArtPalette.Cyan
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }
        drawRect(Brush.verticalGradient(listOf(EmpireColors.Void, EmpireColors.DeepSpace, EmpireColors.Void)))
        repeat(34) { i ->
            val x = size.width * (((i * 47) % 101) / 100f)
            val y = size.height * (((i * 73) % 97) / 100f)
            drawCircle(EmpireArtPalette.White.copy(alpha = .28f + .12f * (i % 5)), if (i % 7 == 0) 2.2f else 1.1f, Offset(x, y))
        }
        val cx = size.width * (.18f + phase * .64f)
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha = .16f), Color.Transparent), Offset(cx, size.height * .28f), size.width * .55f), size.width * .55f, Offset(cx, size.height * .28f))
        drawCircle(Brush.radialGradient(listOf(EmpireArtPalette.Violet.copy(alpha = .10f), Color.Transparent), Offset(size.width * .82f, size.height * .68f), size.width * .48f), size.width * .48f, Offset(size.width * .82f, size.height * .68f))
    }
}

private fun DrawScope.arc(color: Color, left: Float, top: Float, right: Float, bottom: Float, start: Float, sweep: Float, stroke: Float) {
    drawArc(color, start, sweep, false, Offset(left, top), Size(right-left, bottom-top), style = Stroke(stroke))
}

private fun DrawScope.drawStreetStand(c: Color) { val s=size.minDimension; drawRoundRect(c,Offset(s*.25f,s*.46f),Size(s*.5f,s*.28f),CornerRadius(s*.04f)); drawRect(EmpireArtPalette.Ink,Offset(s*.31f,s*.53f),Size(s*.38f,s*.15f)); drawLine(c,Offset(s*.28f,s*.42f),Offset(s*.72f,s*.42f),s*.07f); drawLine(c,Offset(s*.35f,s*.3f),Offset(s*.65f,s*.3f),s*.055f) }
private fun DrawScope.drawStore(c: Color) { val s=size.minDimension; drawRoundRect(c.copy(alpha=.9f),Offset(s*.24f,s*.39f),Size(s*.52f,s*.36f),CornerRadius(s*.05f)); drawRect(EmpireArtPalette.Ink,Offset(s*.32f,s*.51f),Size(s*.36f,s*.24f)); repeat(3){i->drawRect(c,Offset(s*(.29f+i*.15f),s*.31f),Size(s*.11f,s*.1f))} }
private fun DrawScope.drawWorkshop(c: Color) { val s=size.minDimension; drawCircle(c,s*.20f,Offset(s*.5f,s*.52f),style=Stroke(s*.09f)); repeat(6){i->val a=i*Math.PI.toFloat()/3f;drawLine(c,Offset(s*.5f+cos(a)*s*.2f,s*.52f+sin(a)*s*.2f),Offset(s*.5f+cos(a)*s*.34f,s*.52f+sin(a)*s*.34f),s*.065f)};drawCircle(EmpireArtPalette.Ink,s*.07f,Offset(s*.5f,s*.52f)) }
private fun DrawScope.drawFactory(c: Color) { val s=size.minDimension; val p=Path().apply{moveTo(s*.18f,s*.72f);lineTo(s*.18f,s*.5f);lineTo(s*.36f,s*.39f);lineTo(s*.36f,s*.5f);lineTo(s*.55f,s*.39f);lineTo(s*.55f,s*.5f);lineTo(s*.78f,s*.5f);lineTo(s*.78f,s*.72f);close()};drawPath(p,c);drawRect(EmpireArtPalette.Ink,Offset(s*.27f,s*.58f),Size(s*.12f,s*.09f));drawRect(EmpireArtPalette.Ink,Offset(s*.52f,s*.58f),Size(s*.12f,s*.09f));drawRect(c,Offset(s*.66f,s*.23f),Size(s*.08f,s*.28f)) }
private fun DrawScope.drawTech(c: Color) { val s=size.minDimension; drawRoundRect(c,Offset(s*.22f,s*.27f),Size(s*.56f,s*.46f),CornerRadius(s*.09f),style=Stroke(s*.055f));repeat(3){i->drawLine(c,Offset(s*(.32f+i*.18f),s*.16f),Offset(s*(.32f+i*.18f),s*.27f),s*.035f);drawLine(c,Offset(s*(.32f+i*.18f),s*.73f),Offset(s*(.32f+i*.18f),s*.84f),s*.035f)};drawCircle(c,s*.10f,Offset(s*.5f,s*.5f));drawCircle(EmpireArtPalette.Ink,s*.04f,Offset(s*.5f,s*.5f)) }
private fun DrawScope.drawCity(c: Color) { val s=size.minDimension; val xs=listOf(.20f,.35f,.50f,.64f);val hs=listOf(.36f,.50f,.43f,.58f);xs.forEachIndexed{i,x->val h=hs[i]*s;drawRoundRect(c.copy(alpha=.85f),Offset(s*x,s*.75f-h),Size(s*.12f,h),CornerRadius(s*.025f));repeat(3){r->drawCircle(EmpireArtPalette.GoldHot,s*.012f,Offset(s*(x+.035f),s*.69f-h+r*s*.09f));drawCircle(EmpireArtPalette.Cyan,s*.012f,Offset(s*(x+.085f),s*.69f-h+r*s*.09f))}} }
private fun DrawScope.drawMoon(c: Color) { val s=size.minDimension; drawCircle(c,s*.27f,Offset(s*.48f,s*.5f));drawCircle(EmpireArtPalette.Ink.copy(alpha=.28f),s*.055f,Offset(s*.39f,s*.41f));drawCircle(EmpireArtPalette.Ink.copy(alpha=.22f),s*.035f,Offset(s*.57f,s*.57f));arc(EmpireArtPalette.Cyan,s*.18f,s*.34f,s*.82f,s*.67f,-12f,205f,s*.035f) }
private fun DrawScope.drawPlanet(c: Color) { val s=size.minDimension; drawCircle(c,s*.25f,Offset(s*.5f,s*.51f));arc(EmpireArtPalette.GoldHot,s*.14f,s*.36f,s*.86f,s*.66f,-12f,205f,s*.045f);drawCircle(EmpireArtPalette.White,s*.018f,Offset(s*.31f,s*.3f)) }
private fun DrawScope.drawDyson(c: Color) { val s=size.minDimension; drawCircle(EmpireArtPalette.GoldHot,s*.12f,Offset(s*.5f,s*.5f));drawCircle(c.copy(alpha=.25f),s*.22f,Offset(s*.5f,s*.5f));drawCircle(c,s*.30f,Offset(s*.5f,s*.5f),style=Stroke(s*.035f));repeat(8){i->val a=i*Math.PI.toFloat()/4f;drawLine(c,Offset(s*.5f+cos(a)*s*.19f,s*.5f+sin(a)*s*.19f),Offset(s*.5f+cos(a)*s*.36f,s*.5f+sin(a)*s*.36f),s*.025f)} }
private fun DrawScope.drawGalaxy(c: Color) { val s=size.minDimension; drawCircle(EmpireArtPalette.White,s*.045f,Offset(s*.5f,s*.5f));repeat(3){ring->arc(c.copy(alpha=.9f-ring*.2f),s*(.18f+ring*.06f),s*(.27f+ring*.06f),s*(.82f-ring*.06f),s*(.73f-ring*.06f),25f+ring*42f,205f,s*(.045f-ring*.008f))};repeat(8){i->val a=i*.83f;drawCircle(if(i%2==0)EmpireArtPalette.Cyan else EmpireArtPalette.Magenta,s*.018f,Offset(s*.5f+cos(a)*s*(.23f+i*.012f),s*.5f+sin(a)*s*(.16f+i*.009f)))} }
