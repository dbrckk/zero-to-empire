package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.RepeatMode
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
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/**
 * High-detail, resolution-independent business sprites.
 * Every asset is built from several material/emissive/detail layers and evolves by level.
 */
@Composable
fun PremiumBusinessSprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val motion = rememberInfiniteTransition(label = "premiumSprite$id")
    val phase by motion.animateFloat(
        0f, 1f,
        infiniteRepeatable(tween(6200 + id * 170, easing = LinearEasing)),
        label = "phase"
    )
    val breathe by motion.animateFloat(
        .82f, 1f,
        infiniteRepeatable(tween(1650 + id * 80), RepeatMode.Reverse),
        label = "breathe"
    )

    val accent = spriteAccent(id)
    val stage = spriteStage(level)

    Box(
        modifier = modifier
            .size(iconSize)
            .background(
                Brush.radialGradient(
                    0f to accent.copy(alpha = .20f + stage * .025f),
                    .42f to EmpireColors.SurfaceHigh,
                    1f to EmpireColors.Void
                ),
                RoundedCornerShape(iconSize * .28f)
            )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val center = Offset(s * .5f, s * .5f)

            // Atmospheric/material layers.
            drawCircle(accent.copy(alpha = (.08f + stage * .025f) * breathe), s * .47f, center)
            drawCircle(accent.copy(alpha = .24f + stage * .04f), s * .405f, center, style = Stroke(s * .018f))
            drawCircle(Color.White.copy(alpha = .055f), s * .365f, center, style = Stroke(s * .008f))
            drawSpriteFloor(accent)

            // Level-based prestige shell.
            if (stage >= 1) drawOrbitRing(accent, phase, .42f, .017f, 3)
            if (stage >= 2) drawOrbitRing(EmpireArtPalette.GoldHot, 1f - phase, .465f, .012f, 5)
            if (stage >= 3) drawPrestigeSpokes(accent, phase)
            if (stage >= 4) drawCrownArc(accent, phase)
            if (stage >= 5) drawAscendantHalo(accent, breathe)

            when (id.coerceIn(0, 9)) {
                0 -> premiumStreetStand(accent, stage)
                1 -> premiumCornerShop(accent, stage)
                2 -> premiumWorkshop(accent, stage, phase)
                3 -> premiumFactory(accent, stage, phase)
                4 -> premiumTechCompany(accent, stage, phase)
                5 -> premiumMegacity(accent, stage, phase)
                6 -> premiumMoonColony(accent, stage, phase)
                7 -> premiumMarsEmpire(accent, stage, phase)
                8 -> premiumDysonNetwork(accent, stage, phase)
                else -> premiumGalacticExchange(accent, stage, phase)
            }

            // Specular highlight unifies all sprites.
            drawArc(
                Color.White.copy(alpha = .20f),
                205f, 58f, false,
                Offset(s * .18f, s * .17f), Size(s * .64f, s * .64f),
                style = Stroke(s * .010f)
            )
        }
    }
}

private fun spriteAccent(id: Int): Color = when (id) {
    0 -> Color(0xFFFFC85A)
    1 -> Color(0xFFFFA95A)
    2 -> Color(0xFF66E7F5)
    3 -> Color(0xFF54C7FF)
    4 -> Color(0xFF9C8CFF)
    5 -> Color(0xFFC077FF)
    6 -> Color(0xFFE6F4FF)
    7 -> Color(0xFFFF6F68)
    8 -> Color(0xFFFFDF72)
    else -> Color(0xFFFF71D8)
}

private fun spriteStage(level: Int): Int = when {
    level >= 1000 -> 5
    level >= 500 -> 4
    level >= 250 -> 3
    level >= 100 -> 2
    level >= 25 -> 1
    else -> 0
}

private fun DrawScope.drawSpriteFloor(accent: Color) {
    val s = size.minDimension
    drawOval(
        Brush.radialGradient(listOf(accent.copy(alpha = .18f), Color.Transparent)),
        Offset(s * .17f, s * .72f), Size(s * .66f, s * .14f)
    )
    drawLine(accent.copy(alpha = .30f), Offset(s * .23f, s * .78f), Offset(s * .77f, s * .78f), s * .010f)
}

private fun DrawScope.drawOrbitRing(color: Color, phase: Float, radius: Float, stroke: Float, nodes: Int) {
    val s = size.minDimension
    val c = Offset(s * .5f, s * .5f)
    drawCircle(color.copy(alpha = .35f), s * radius, c, style = Stroke(s * stroke))
    repeat(nodes) { i ->
        val a = phase * PI.toFloat() * 2f + i * PI.toFloat() * 2f / nodes
        val p = Offset(c.x + cos(a) * s * radius, c.y + sin(a) * s * radius)
        drawCircle(Color.White.copy(alpha = .75f), s * .011f, p)
        drawCircle(color.copy(alpha = .28f), s * .025f, p)
    }
}

private fun DrawScope.drawPrestigeSpokes(color: Color, phase: Float) {
    val s = size.minDimension
    val c = Offset(s * .5f, s * .5f)
    repeat(8) { i ->
        val a = phase * PI.toFloat() * .35f + i * PI.toFloat() / 4f
        drawLine(
            color.copy(alpha = .44f),
            Offset(c.x + cos(a) * s * .39f, c.y + sin(a) * s * .39f),
            Offset(c.x + cos(a) * s * .48f, c.y + sin(a) * s * .48f),
            s * .009f
        )
    }
}

private fun DrawScope.drawCrownArc(color: Color, phase: Float) {
    val s = size.minDimension
    drawArc(
        EmpireArtPalette.GoldHot.copy(alpha = .66f),
        -40f + phase * 18f, 245f, false,
        Offset(s * .075f, s * .075f), Size(s * .85f, s * .85f), style = Stroke(s * .014f)
    )
    drawArc(
        color.copy(alpha = .42f),
        155f - phase * 14f, 165f, false,
        Offset(s * .11f, s * .11f), Size(s * .78f, s * .78f), style = Stroke(s * .010f)
    )
}

private fun DrawScope.drawAscendantHalo(color: Color, breathe: Float) {
    val s = size.minDimension
    drawCircle(
        Brush.radialGradient(listOf(Color.White.copy(alpha = .12f * breathe), color.copy(alpha = .08f), Color.Transparent)),
        s * .51f,
        Offset(s * .5f, s * .5f)
    )
}

private fun DrawScope.premiumStreetStand(c: Color, stage: Int) {
    val s = size.minDimension
    val roof = Path().apply {
        moveTo(s * .22f, s * .38f); lineTo(s * .31f, s * .27f); lineTo(s * .69f, s * .27f); lineTo(s * .78f, s * .38f); close()
    }
    drawPath(roof, Brush.verticalGradient(listOf(EmpireArtPalette.GoldHot, c)))
    drawRoundRect(EmpireArtPalette.Steel, Offset(s * .25f, s * .40f), Size(s * .50f, s * .31f), CornerRadius(s * .035f))
    drawRoundRect(c.copy(alpha = .85f), Offset(s * .28f, s * .44f), Size(s * .44f, s * .08f), CornerRadius(s * .018f))
    drawRect(EmpireArtPalette.Ink, Offset(s * .31f, s * .55f), Size(s * .38f, s * .13f))
    repeat(4) { i -> drawCircle(Color.White.copy(alpha = .8f), s * .010f, Offset(s * (.35f + i * .10f), s * .48f)) }
    if (stage >= 2) {
        drawLine(c, Offset(s * .22f, s * .73f), Offset(s * .78f, s * .73f), s * .018f)
        drawCircle(c, s * .026f, Offset(s * .24f, s * .72f)); drawCircle(c, s * .026f, Offset(s * .76f, s * .72f))
    }
}

private fun DrawScope.premiumCornerShop(c: Color, stage: Int) {
    val s = size.minDimension
    drawRoundRect(EmpireArtPalette.SteelBright, Offset(s * .22f, s * .34f), Size(s * .56f, s * .40f), CornerRadius(s * .04f))
    drawRect(EmpireArtPalette.Ink, Offset(s * .29f, s * .48f), Size(s * .42f, s * .24f))
    repeat(4) { i ->
        val x = s * (.245f + i * .135f)
        drawRoundRect(if (i % 2 == 0) c else EmpireArtPalette.GoldHot, Offset(x, s * .29f), Size(s * .105f, s * .12f), CornerRadius(s * .015f))
    }
    drawLine(c, Offset(s * .34f, s * .57f), Offset(s * .66f, s * .57f), s * .012f)
    if (stage >= 1) drawRoundRect(c.copy(alpha = .30f), Offset(s * .29f, s * .19f), Size(s * .42f, s * .07f), CornerRadius(s * .02f))
}

private fun DrawScope.premiumWorkshop(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    val center = Offset(s * .5f, s * .51f)
    drawCircle(EmpireArtPalette.SteelBright, s * .27f, center)
    drawCircle(c, s * .20f, center, style = Stroke(s * .065f))
    repeat(8) { i ->
        val a = phase * PI.toFloat() * .6f + i * PI.toFloat() / 4f
        drawLine(c, Offset(center.x + cos(a) * s * .21f, center.y + sin(a) * s * .21f), Offset(center.x + cos(a) * s * .31f, center.y + sin(a) * s * .31f), s * .045f)
    }
    drawCircle(EmpireArtPalette.Ink, s * .075f, center)
    drawCircle(Color.White.copy(alpha = .6f), s * .018f, Offset(s * .47f, s * .46f))
    if (stage >= 3) repeat(3) { i -> drawCircle(EmpireArtPalette.GoldHot, s * .014f, Offset(s * (.34f + i * .16f), s * .73f)) }
}

private fun DrawScope.premiumFactory(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    val body = Path().apply {
        moveTo(s*.17f,s*.72f); lineTo(s*.17f,s*.49f); lineTo(s*.34f,s*.37f); lineTo(s*.34f,s*.49f); lineTo(s*.52f,s*.37f); lineTo(s*.52f,s*.49f); lineTo(s*.79f,s*.49f); lineTo(s*.79f,s*.72f); close()
    }
    drawPath(body, Brush.verticalGradient(listOf(EmpireArtPalette.SteelBright, EmpireArtPalette.Steel)))
    drawPath(body, c.copy(alpha=.65f), style = Stroke(s*.018f))
    drawRect(EmpireArtPalette.SteelBright, Offset(s*.66f,s*.20f), Size(s*.085f,s*.30f))
    repeat(3){i-> drawRoundRect(c.copy(alpha=.82f), Offset(s*(.25f+i*.16f),s*.56f), Size(s*.09f,s*.09f), CornerRadius(s*.012f)) }
    val smokeY = s * (.16f - .035f * sin(phase * PI.toFloat()*2f))
    drawCircle(Color.White.copy(alpha=.10f), s*.055f, Offset(s*.70f, smokeY))
    if(stage>=2) drawLine(EmpireArtPalette.GoldHot,Offset(s*.20f,s*.74f),Offset(s*.77f,s*.74f),s*.016f)
}

private fun DrawScope.premiumTechCompany(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    drawRoundRect(EmpireArtPalette.Steel, Offset(s*.21f,s*.26f), Size(s*.58f,s*.48f), CornerRadius(s*.09f))
    drawRoundRect(c.copy(alpha=.25f), Offset(s*.25f,s*.30f), Size(s*.50f,s*.40f), CornerRadius(s*.07f))
    drawCircle(c, s*.115f, Offset(s*.5f,s*.5f), style=Stroke(s*.030f))
    drawCircle(Color.White.copy(alpha=.85f), s*.035f, Offset(s*.5f,s*.5f))
    repeat(8){i->
        val a=i*PI.toFloat()/4f+phase*PI.toFloat()*.25f
        drawLine(c.copy(alpha=.7f),Offset(s*.5f+cos(a)*s*.14f,s*.5f+sin(a)*s*.14f),Offset(s*.5f+cos(a)*s*.25f,s*.5f+sin(a)*s*.25f),s*.015f)
    }
    if(stage>=3) repeat(4){i->drawCircle(EmpireArtPalette.Magenta,s*.015f,Offset(s*(.31f+i*.125f),s*.66f))}
}

private fun DrawScope.premiumMegacity(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    val xs = listOf(.18f,.29f,.40f,.53f,.65f,.74f)
    val hs = listOf(.28f,.44f,.36f,.53f,.40f,.31f)
    xs.forEachIndexed { i,x ->
        val h = s * hs[i]
        val w = s * if(i==3) .12f else .095f
        drawRoundRect(Brush.verticalGradient(listOf(c.copy(alpha=.72f),EmpireArtPalette.Steel)),Offset(s*x,s*.75f-h),Size(w,h),CornerRadius(s*.018f))
        repeat(3){r->
            val glow = if((r+i)%2==0) EmpireArtPalette.Cyan else EmpireArtPalette.GoldHot
            drawCircle(glow.copy(alpha=.65f),s*.008f,Offset(s*(x+.03f),s*.70f-h+r*s*.075f))
        }
    }
    drawLine(c.copy(alpha=.45f),Offset(s*.16f,s*.75f),Offset(s*.84f,s*.75f),s*.012f)
    if(stage>=2){
        val x=s*(.30f+.40f*phase)
        drawLine(EmpireArtPalette.Cyan.copy(alpha=.7f),Offset(x,s*.20f),Offset(x,s*.72f),s*.008f)
    }
}

private fun DrawScope.premiumMoonColony(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    drawCircle(Color(0xFFDCE8F0),s*.265f,Offset(s*.48f,s*.50f))
    drawCircle(Color(0xFF8293A6).copy(alpha=.28f),s*.060f,Offset(s*.39f,s*.42f))
    drawCircle(Color(0xFF8293A6).copy(alpha=.22f),s*.040f,Offset(s*.57f,s*.57f))
    drawArc(c,205f,145f,false,Offset(s*.17f,s*.35f),Size(s*.65f,s*.30f),style=Stroke(s*.028f))
    repeat(3){i->drawCircle(EmpireArtPalette.Cyan,s*.020f,Offset(s*(.35f+i*.13f),s*.64f))}
    val shuttleX=s*(.25f+.50f*phase)
    drawLine(EmpireArtPalette.GoldHot,Offset(shuttleX,s*.26f),Offset(shuttleX+s*.055f,s*.245f),s*.018f)
    if(stage>=4) drawCircle(c.copy(alpha=.20f),s*.35f,Offset(s*.48f,s*.50f),style=Stroke(s*.012f))
}

private fun DrawScope.premiumMarsEmpire(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    drawCircle(Color(0xFFD96054),s*.255f,Offset(s*.50f,s*.51f))
    drawCircle(Color(0xFF772E31).copy(alpha=.32f),s*.055f,Offset(s*.41f,s*.45f))
    drawArc(EmpireArtPalette.GoldHot,198f,168f,false,Offset(s*.14f,s*.35f),Size(s*.72f,s*.32f),style=Stroke(s*.030f))
    repeat(4){i->
        val a=phase*PI.toFloat()*2f+i*PI.toFloat()/2f
        drawCircle(c,s*.018f,Offset(s*.5f+cos(a)*s*.34f,s*.5f+sin(a)*s*.15f))
    }
    if(stage>=2){
        drawLine(c,Offset(s*.36f,s*.70f),Offset(s*.36f,s*.55f),s*.014f)
        drawLine(c,Offset(s*.64f,s*.70f),Offset(s*.64f,s*.55f),s*.014f)
    }
}

private fun DrawScope.premiumDysonNetwork(c: Color, stage: Int, phase: Float) {
    val s=size.minDimension
    val center=Offset(s*.5f,s*.5f)
    drawCircle(Brush.radialGradient(listOf(Color.White,EmpireArtPalette.GoldHot,Color(0xFFFF8B3D).copy(alpha=.2f))),s*.15f,center)
    drawCircle(c.copy(alpha=.18f),s*.23f,center)
    repeat(3){ring->
        drawCircle(c.copy(alpha=.65f-ring*.12f),s*(.26f+ring*.06f),center,style=Stroke(s*(.020f-ring*.003f)))
    }
    repeat(12){i->
        val a=phase*PI.toFloat()*2f+i*PI.toFloat()/6f
        val r=s*(.27f+(i%3)*.06f)
        val p=Offset(center.x+cos(a)*r,center.y+sin(a)*r)
        drawRoundRect(if(i%2==0)c else EmpireArtPalette.GoldHot,Offset(p.x-s*.018f,p.y-s*.010f),Size(s*.036f,s*.020f),CornerRadius(s*.006f))
    }
    if(stage>=5) drawCircle(Color.White.copy(alpha=.35f),s*.41f,center,style=Stroke(s*.008f))
}

private fun DrawScope.premiumGalacticExchange(c: Color, stage: Int, phase: Float) {
    val s=size.minDimension
    val center=Offset(s*.5f,s*.51f)
    drawCircle(Color.White,s*.035f,center)
    repeat(4){arm->
        val start=arm*PI.toFloat()/2f+phase*PI.toFloat()*2f
        repeat(13){j->
            val r=s*(.035f+j*.021f)
            val a=start+j*.23f
            val color=when(j%3){0->EmpireArtPalette.Cyan;1->c;else->EmpireArtPalette.Violet}
            drawCircle(color.copy(alpha=.82f-j*.025f),s*(.012f+j*.0006f),Offset(center.x+cos(a)*r,center.y+sin(a)*r*.62f))
        }
    }
    drawCircle(c.copy(alpha=.28f),s*.31f,center,style=Stroke(s*.018f))
    if(stage>=2) drawCircle(EmpireArtPalette.GoldHot.copy(alpha=.45f),s*.38f,center,style=Stroke(s*.010f))
    if(stage>=4) repeat(6){i->
        val a=i*PI.toFloat()/3f-phase*PI.toFloat()
        drawCircle(Color.White.copy(alpha=.9f),s*.012f,Offset(center.x+cos(a)*s*.42f,center.y+sin(a)*s*.22f))
    }
}
