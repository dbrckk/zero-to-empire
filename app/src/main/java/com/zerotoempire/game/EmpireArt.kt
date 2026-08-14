package com.zerotoempire.game

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Rect
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.*
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import kotlin.math.cos
import kotlin.math.sin

/**
 * Scalable procedural art layer used instead of platform emoji.
 * Every asset is vector-like, resolution independent and can later be swapped with authored HD art
 * without touching economy or UI state.
 */
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
fun BusinessArtIcon(id: Int, size: Dp = 54.dp, modifier: Modifier = Modifier) {
    Box(
        modifier = modifier
            .size(size)
            .background(
                Brush.radialGradient(
                    listOf(EmpireColors.SurfaceHigh, EmpireColors.Surface, EmpireColors.Void)
                ),
                RoundedCornerShape(size * .28f)
            )
    ) {
        Canvas(Modifier.matchParentSize()) {
            val glow = when (id) {
                0, 1 -> EmpireArtPalette.Gold
                2, 3 -> EmpireArtPalette.Cyan
                4, 5 -> EmpireArtPalette.Violet
                6, 7 -> EmpireArtPalette.Red
                else -> EmpireArtPalette.Magenta
            }
            drawCircle(glow.copy(alpha = .16f), radius = size.minDimension * .46f)
            drawCircle(
                color = glow.copy(alpha = .42f),
                radius = size.minDimension * .38f,
                style = Stroke(width = size.minDimension * .025f)
            )
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
    val phase by transition.animateFloat(
        initialValue = 0f,
        targetValue = 1f,
        animationSpec = infiniteRepeatable(tween(18_000, easing = LinearEasing)),
        label = "ambientPhase"
    )
    Canvas(modifier) {
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1 -> EmpireArtPalette.Cyan
            2 -> EmpireArtPalette.Cyan
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }
        drawRect(
            Brush.verticalGradient(
                listOf(EmpireColors.Void, EmpireColors.DeepSpace, EmpireColors.Void)
            )
        )
        val w = size.width
        val h = size.height
        repeat(28) { i ->
            val fx = ((i * 47) % 101) / 100f
            val fy = ((i * 73) % 97) / 100f
            val pulse = .35f + .4f * ((i % 5) / 4f)
            drawCircle(
                EmpireArtPalette.White.copy(alpha = pulse),
                radius = if (i % 7 == 0) 2.2f else 1.1f,
                center = Offset(w * fx, h * fy)
            )
        }
        val cx = w * (.18f + phase * .64f)
        drawCircle(
            brush = Brush.radialGradient(
                listOf(accent.copy(alpha = .16f), Color.Transparent),
                center = Offset(cx, h * .28f),
                radius = w * .55f
            ),
            radius = w * .55f,
            center = Offset(cx, h * .28f)
        )
        drawCircle(
            brush = Brush.radialGradient(
                listOf(EmpireArtPalette.Violet.copy(alpha = .10f), Color.Transparent),
                center = Offset(w * .82f, h * .68f),
                radius = w * .48f
            ),
            radius = w * .48f,
            center = Offset(w * .82f, h * .68f)
        )
    }
}

private fun DrawScope.drawStreetStand(c: Color) {
    val s = size.minDimension
    drawRoundRect(c, Offset(s*.25f,s*.46f), Size(s*.5f,s*.28f), CornerRadius(s*.04f))
    drawRect(EmpireArtPalette.Ink, Offset(s*.31f,s*.53f), Size(s*.38f,s*.15f))
    drawLine(c, Offset(s*.28f,s*.42f), Offset(s*.72f,s*.42f), s*.07f)
    drawLine(c, Offset(s*.35f,s*.3f), Offset(s*.65f,s*.3f), s*.055f)
}

private fun DrawScope.drawStore(c: Color) {
    val s = size.minDimension
    drawRoundRect(c.copy(alpha=.9f), Offset(s*.24f,s*.39f), Size(s*.52f,s*.36f), CornerRadius(s*.05f))
    drawRect(EmpireArtPalette.Ink, Offset(s*.32f,s*.51f), Size(s*.36f,s*.24f))
    repeat(3){ i -> drawRect(c, Offset(s*(.29f+i*.15f),s*.31f), Size(s*.11f,s*.1f)) }
}

private fun DrawScope.drawWorkshop(c: Color) {
    val s=size.minDimension
    drawCircle(c, s*.20f, Offset(s*.5f,s*.52f), style=Stroke(s*.09f))
    repeat(6){i-> val a=i*Math.PI.toFloat()/3f; drawLine(c, Offset(s*.5f+cos(a)*s*.2f,s*.52f+sin(a)*s*.2f), Offset(s*.5f+cos(a)*s*.34f,s*.52f+sin(a)*s*.34f), s*.065f)}
    drawCircle(EmpireArtPalette.Ink,s*.07f,Offset(s*.5f,s*.52f))
}

private fun DrawScope.drawFactory(c: Color) {
    val s=size.minDimension
    val p=Path().apply{moveTo(s*.18f,s*.72f);lineTo(s*.18f,s*.5f);lineTo(s*.36f,s*.39f);lineTo(s*.36f,s*.5f);lineTo(s*.55f,s*.39f);lineTo(s*.55f,s*.5f);lineTo(s*.78f,s*.5f);lineTo(s*.78f,s*.72f);close()}
    drawPath(p,c)
    drawRect(EmpireArtPalette.Ink,Offset(s*.27f,s*.58f),Size(s*.12f,s*.09f));drawRect(EmpireArtPalette.Ink,Offset(s*.52f,s*.58f),Size(s*.12f,s*.09f))
    drawRect(c,Offset(s*.66f,s*.23f),Size(s*.08f,s*.28f))
}

private fun DrawScope.drawTech(c: Color) {
    val s=size.minDimension
    drawRoundRect(c,Offset(s*.22f,s*.27f),Size(s*.56f,s*.46f),CornerRadius(s*.09f),style=Stroke(s*.055f))
    repeat(3){i->drawLine(c,Offset(s*(.32f+i*.18f),s*.16f),Offset(s*(.32f+i*.18f),s*.27f),s*.035f);drawLine(c,Offset(s*(.32f+i*.18f),s*.73f),Offset(s*(.32f+i*.18f),s*.84f),s*.035f)}
    drawCircle(c,s*.10f,Offset(s*.5f,s*.5f));drawCircle(EmpireArtPalette.Ink,s*.04f,Offset(s*.5f,s*.5f))
}

private fun DrawScope.drawCity(c: Color) {
    val s=size.minDimension
    val xs=listOf(.20f,.35f,.50f,.64f)
    val hs=listOf(.36f,.50f,.43f,.58f)
    xs.forEachIndexed{i,x-> val h=hs[i]*s;drawRoundRect(c.copy(alpha=.85f),Offset(s*x,s*.75f-h),Size(s*.12f,h),CornerRadius(s*.025f));repeat(3){r->drawCircle(EmpireArtPalette.GoldHot,s*.012f,Offset(s*(x+.035f),s*.69f-h+r*s*.09f));drawCircle(EmpireArtPalette.Cyan,s*.012f,Offset(s*(x+.085f),s*.69f-h+r*s*.09f))}}
}

private fun DrawScope.drawMoon(c: Color) {
    val s=size.minDimension
    drawCircle(c,s*.27f,Offset(s*.48f,s*.5f));drawCircle(EmpireArtPalette.Ink.copy(alpha=.28f),s*.055f,Offset(s*.39f,s*.41f));drawCircle(EmpireArtPalette.Ink.copy(alpha=.22f),s*.035f,Offset(s*.57f,s*.57f));drawArc(EmpireArtPalette.Cyan,-12f,205f,false,Rect(s*.18f,s*.34f,s*.82f,s*.67f),style=Stroke(s*.035f))
}

private fun DrawScope.drawPlanet(c: Color) {
    val s=size.minDimension
    drawCircle(c,s*.25f,Offset(s*.5f,s*.51f));drawArc(EmpireArtPalette.GoldHot,-12f,205f,false,Rect(s*.14f,s*.36f,s*.86f,s*.66f),style=Stroke(s*.045f));drawCircle(EmpireArtPalette.White,s*.018f,Offset(s*.31f,s*.3f))
}

private fun DrawScope.drawDyson(c: Color) {
    val s=size.minDimension
    drawCircle(EmpireArtPalette.GoldHot,s*.12f,Offset(s*.5f,s*.5f));drawCircle(c.copy(alpha=.25f),s*.22f,Offset(s*.5f,s*.5f));drawCircle(c,s*.30f,Offset(s*.5f,s*.5f),style=Stroke(s*.035f));repeat(8){i->val a=i*Math.PI.toFloat()/4f;drawLine(c,Offset(s*.5f+cos(a)*s*.19f,s*.5f+sin(a)*s*.19f),Offset(s*.5f+cos(a)*s*.36f,s*.5f+sin(a)*s*.36f),s*.025f)}
}

private fun DrawScope.drawGalaxy(c: Color) {
    val s=size.minDimension
    drawCircle(EmpireArtPalette.White,s*.045f,Offset(s*.5f,s*.5f));
    repeat(3){ring->drawArc(c.copy(alpha=.9f-ring*.2f),25f+ring*42f,205f,false,Rect(s*(.18f+ring*.06f),s*(.27f+ring*.06f),s*(.82f-ring*.06f),s*(.73f-ring*.06f)),style=Stroke(s*(.045f-ring*.008f)))}
    repeat(8){i->val a=i*.83f;drawCircle(if(i%2==0)EmpireArtPalette.Cyan else EmpireArtPalette.Magenta,s*.018f,Offset(s*.5f+cos(a)*s*(.23f+i*.012f),s*.5f+sin(a)*s*(.16f+i*.009f)))}
}
