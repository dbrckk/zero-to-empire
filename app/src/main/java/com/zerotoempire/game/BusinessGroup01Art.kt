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
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Final art pass for Group 01: Street Stand, Corner Shop, Workshop, Factory. */
@Composable
fun BusinessGroup01Sprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val transition = if (reduced) null else rememberInfiniteTransition(label = "group01-$id")
    val phase = if (transition == null) .18f else {
        val phaseAnimated by transition.animateFloat(
            0f, 1f,
            infiniteRepeatable(tween(if (lowPower) 9000 else 5600 + id * 380, easing = LinearEasing)),
            label = "phase"
        )
        phaseAnimated
    }
    val breathe = if (reduced) .92f else .88f + .10f * ((sin(phase * PI.toFloat() * 2f - PI.toFloat() / 2f) + 1f) * .5f)
    val stage = group01Stage(level)
    val accent = group01Accent(id)

    Box(
        modifier = modifier
            .size(iconSize)
            .background(
                Brush.radialGradient(
                    0f to accent.copy(alpha = .23f + stage * .02f),
                    .45f to EmpireColors.SurfaceHigh,
                    1f to EmpireColors.Void
                ), RoundedCornerShape(iconSize * .27f)
            )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val c = Offset(s * .5f, s * .52f)
            drawOval(
                Brush.radialGradient(listOf(accent.copy(alpha = .25f), Color.Transparent), Offset(c.x, s * .77f), s * .39f),
                Offset(s * .12f, s * .68f), Size(s * .76f, s * .22f)
            )
            drawCircle(accent.copy(alpha = .09f * breathe), s * .46f, c)
            drawCircle(accent.copy(alpha = .32f), s * .42f, c, style = Stroke(s * .012f))

            when (id.coerceIn(0, 3)) {
                0 -> drawStreetStandAAA(stage, phase, breathe)
                1 -> drawCornerShopAAA(stage, phase, breathe)
                2 -> drawWorkshopAAA(stage, phase, breathe)
                else -> drawFactoryAAA(stage, phase, breathe, lowPower)
            }

            if (stage >= 1) drawGroupProgressionRing(accent, phase, .435f, 3)
            if (stage >= 2) drawGroupProgressionRing(Color.White, 1f - phase, .475f, 5)
            if (stage >= 3) drawGroupSpokes(accent, phase, if (lowPower) 4 else 8)
            if (stage >= 4) drawGroupCrown(accent, phase)
            if (stage >= 5) drawGroupMastery(accent, breathe, lowPower)
        }
    }
}

private fun group01Stage(level: Int) = when {
    level >= 1000 -> 5
    level >= 500 -> 4
    level >= 250 -> 3
    level >= 100 -> 2
    level >= 25 -> 1
    else -> 0
}

private fun group01Accent(id: Int): Color = when (id) {
    0 -> Color(0xFF78F56A)
    1 -> Color(0xFF58BFFF)
    2 -> Color(0xFFFF9A43)
    else -> Color(0xFFB76CFF)
}

private fun DrawScope.drawStreetStandAAA(stage: Int, phase: Float, breathe: Float) {
    val s = size.minDimension
    val woodDark = Color(0xFF4A2C20)
    val wood = Color(0xFF7A4B31)
    val cream = Color(0xFFFFE6B0)
    val green = group01Accent(0)
    drawRoundRect(woodDark, Offset(s*.20f,s*.49f), Size(s*.60f,s*.24f), CornerRadius(s*.04f))
    drawRoundRect(wood, Offset(s*.24f,s*.52f), Size(s*.52f,s*.15f), CornerRadius(s*.025f))
    drawCircle(Color(0xFF1A1412), s*.065f, Offset(s*.29f,s*.73f)); drawCircle(Color(0xFF1A1412),s*.065f,Offset(s*.71f,s*.73f))
    drawCircle(wood, s*.040f, Offset(s*.29f,s*.73f)); drawCircle(wood,s*.040f,Offset(s*.71f,s*.73f))
    val canopy = Path().apply { moveTo(s*.15f,s*.42f); lineTo(s*.25f,s*.26f); lineTo(s*.75f,s*.26f); lineTo(s*.85f,s*.42f); close() }
    drawPath(canopy, Color(0xFFE34B3F))
    repeat(5) { i ->
        val x = .22f + i*.12f
        val strip = Path().apply { moveTo(s*x,s*.27f); lineTo(s*(x+.075f),s*.27f); lineTo(s*(x+.12f),s*.42f); lineTo(s*(x+.045f),s*.42f); close() }
        drawPath(strip, cream.copy(alpha=.95f))
    }
    drawLine(green,Offset(s*.17f,s*.43f),Offset(s*.83f,s*.43f),s*.015f)
    repeat(4) { i ->
        val x=s*(.34f+i*.105f)
        drawCircle(Color(0xFFFFB64D),s*.024f,Offset(x,s*.58f))
        drawCircle(Color.White.copy(alpha=.6f),s*.006f,Offset(x-s*.007f,s*.57f))
    }
    val flicker = .65f + .25f*sin(phase*PI.toFloat()*2f)
    listOf(.22f,.78f).forEach { x ->
        drawCircle(Color(0xFFFFC65A).copy(alpha=flicker),s*.045f,Offset(s*x,s*.47f))
        drawCircle(Color.White.copy(alpha=.9f),s*.012f,Offset(s*x,s*.47f))
    }
    if(stage>=1) drawRoundRect(green.copy(alpha=.65f),Offset(s*.31f,s*.18f),Size(s*.38f,s*.065f),CornerRadius(s*.018f))
    if(stage>=2) repeat(3){i->drawCircle(green.copy(alpha=.8f),s*.012f,Offset(s*(.36f+i*.14f),s*.34f))}
    if(stage>=3) drawLine(Color(0xFFFFD66B),Offset(s*.23f,s*.66f),Offset(s*.77f,s*.66f),s*.012f)
    if(stage>=4) drawCircle(green.copy(alpha=.18f*breathe),s*.34f,Offset(s*.5f,s*.5f))
    if(stage>=5) repeat(5){i->drawCircle(Color(0xFFFFE78A),s*.011f,Offset(s*(.30f+i*.10f),s*.22f))}
}

private fun DrawScope.drawCornerShopAAA(stage: Int, phase: Float, breathe: Float) {
    val s=size.minDimension
    val blue=group01Accent(1)
    val navy=Color(0xFF18324C)
    val glass=Color(0xFF8FE5FF)
    val warm=Color(0xFFFFB85C)
    drawRoundRect(Color(0xFF24394D),Offset(s*.20f,s*.33f),Size(s*.60f,s*.42f),CornerRadius(s*.035f))
    drawRoundRect(Color(0xFF31516E),Offset(s*.23f,s*.36f),Size(s*.54f,s*.35f),CornerRadius(s*.025f))
    drawRoundRect(navy,Offset(s*.27f,s*.49f),Size(s*.46f,s*.20f),CornerRadius(s*.015f))
    drawRect(glass.copy(alpha=.45f),Offset(s*.29f,s*.51f),Size(s*.18f,s*.16f)); drawRect(glass.copy(alpha=.45f),Offset(s*.53f,s*.51f),Size(s*.18f,s*.16f))
    drawLine(warm.copy(alpha=.85f),Offset(s*.50f,s*.51f),Offset(s*.50f,s*.67f),s*.012f)
    repeat(6){i->
        val x=.22f+i*.095f
        drawRoundRect(if(i%2==0) blue else Color.White.copy(alpha=.9f),Offset(s*x,s*.40f),Size(s*.09f,s*.08f),CornerRadius(s*.012f))
    }
    drawRoundRect(Color(0xFF0E1C2A),Offset(s*.30f,s*.24f),Size(s*.40f,s*.10f),CornerRadius(s*.022f))
    drawRoundRect(blue.copy(alpha=.75f),Offset(s*.32f,s*.255f),Size(s*.36f,s*.065f),CornerRadius(s*.018f))
    val neon=.55f+.35f*breathe
    listOf(.17f,.83f).forEach{x->
        drawLine(Color(0xFF6B7D8E),Offset(s*x,s*.43f),Offset(s*x,s*.74f),s*.012f)
        drawCircle(warm.copy(alpha=neon),s*.035f,Offset(s*x,s*.42f)); drawCircle(Color.White,s*.010f,Offset(s*x,s*.42f))
    }
    if(stage>=1) drawCircle(blue.copy(alpha=.16f*breathe),s*.30f,Offset(s*.5f,s*.50f))
    if(stage>=2) repeat(4){i->drawCircle(blue,s*.010f,Offset(s*(.33f+i*.11f),s*.30f))}
    if(stage>=3) drawArc(blue.copy(alpha=.6f),195f+phase*15f,150f,false,Offset(s*.18f,s*.17f),Size(s*.64f,s*.64f),style=Stroke(s*.014f))
    if(stage>=4) drawLine(Color.White.copy(alpha=.45f),Offset(s*.26f,s*.70f),Offset(s*.74f,s*.70f),s*.009f)
    if(stage>=5) repeat(6){i->drawCircle(Color(0xFFB8F1FF),s*.009f,Offset(s*(.27f+i*.09f),s*.21f))}
}

private fun DrawScope.drawWorkshopAAA(stage:Int,phase:Float,breathe:Float){
    val s=size.minDimension
    val orange=group01Accent(2)
    val steel=Color(0xFF41474D)
    val dark=Color(0xFF20252A)
    val hot=Color(0xFFFFD073)
    val roof=Path().apply{moveTo(s*.18f,s*.48f);lineTo(s*.31f,s*.30f);lineTo(s*.62f,s*.30f);lineTo(s*.75f,s*.43f);lineTo(s*.82f,s*.43f);lineTo(s*.82f,s*.73f);lineTo(s*.18f,s*.73f);close()}
    drawPath(roof,Brush.verticalGradient(listOf(steel,dark)))
    drawPath(roof,orange.copy(alpha=.55f),style=Stroke(s*.014f))
    drawRoundRect(dark,Offset(s*.29f,s*.50f),Size(s*.28f,s*.19f),CornerRadius(s*.015f))
    drawRoundRect(orange.copy(alpha=.42f),Offset(s*.31f,s*.52f),Size(s*.24f,s*.15f),CornerRadius(s*.012f))
    drawRect(steel,Offset(s*.63f,s*.21f),Size(s*.08f,s*.26f))
    drawRect(Color(0xFF1B1B1B),Offset(s*.62f,s*.19f),Size(s*.10f,s*.035f))
    val fire=.55f+.35f*sin(phase*PI.toFloat()*2f)
    drawCircle(orange.copy(alpha=fire),s*.055f,Offset(s*.43f,s*.60f));drawCircle(hot.copy(alpha=.9f),s*.018f,Offset(s*.43f,s*.60f))
    val center=Offset(s*.65f,s*.61f)
    drawCircle(steel,s*.09f,center);drawCircle(orange,s*.057f,center,style=Stroke(s*.026f))
    repeat(8){i->val a=phase*PI.toFloat()*2f+i*PI.toFloat()/4f;drawLine(orange,Offset(center.x+cos(a)*s*.066f,center.y+sin(a)*s*.066f),Offset(center.x+cos(a)*s*.105f,center.y+sin(a)*s*.105f),s*.022f)}
    if(stage>=1) repeat(3){i->drawCircle(hot,s*.009f,Offset(s*(.29f+i*.10f),s*.39f))}
    if(stage>=2) drawLine(orange,Offset(s*.21f,s*.75f),Offset(s*.79f,s*.75f),s*.013f)
    if(stage>=3) repeat(4){i->drawCircle(orange.copy(alpha=.65f*breathe),s*.016f,Offset(s*(.31f+i*.12f),s*.78f))}
    if(stage>=4) drawArc(hot.copy(alpha=.6f),215f+phase*20f,110f,false,Offset(s*.19f,s*.18f),Size(s*.62f,s*.62f),style=Stroke(s*.014f))
    if(stage>=5) repeat(5){i->drawCircle(Color.White.copy(alpha=.8f),s*.008f,Offset(s*(.30f+i*.10f),s*.25f))}
}

private fun DrawScope.drawFactoryAAA(stage:Int,phase:Float,breathe:Float,lowPower:Boolean){
    val s=size.minDimension
    val violet=group01Accent(3)
    val steel=Color(0xFF333642)
    val steel2=Color(0xFF555B6B)
    val magenta=Color(0xFFFF72D8)
    drawRoundRect(steel,Offset(s*.16f,s*.46f),Size(s*.68f,s*.30f),CornerRadius(s*.025f))
    drawRoundRect(steel2,Offset(s*.24f,s*.37f),Size(s*.45f,s*.23f),CornerRadius(s*.018f))
    drawRoundRect(Color(0xFF242631),Offset(s*.33f,s*.30f),Size(s*.28f,s*.15f),CornerRadius(s*.015f))
    drawLine(violet,Offset(s*.18f,s*.72f),Offset(s*.82f,s*.72f),s*.015f)
    val stacks=if(lowPower) 3 else 4
    repeat(stacks){i->
        val x=.24f+i*.15f
        val h=.22f+(i%2)*.05f
        drawRoundRect(steel2,Offset(s*x,s*(.42f-h)),Size(s*.075f,s*h),CornerRadius(s*.012f))
        drawRect(violet.copy(alpha=.75f),Offset(s*(x-.005f),s*(.42f-h)),Size(s*.085f,s*.035f))
        val smokeOffset=.025f*sin((phase+i*.17f)*PI.toFloat()*2f)
        drawCircle(Color(0xFFC8B8FF).copy(alpha=.10f),s*.045f,Offset(s*(x+.038f+smokeOffset),s*(.36f-h)))
    }
    repeat(4){i->
        drawRoundRect(violet.copy(alpha=.75f),Offset(s*(.24f+i*.13f),s*.57f),Size(s*.085f,s*.085f),CornerRadius(s*.010f))
        drawCircle(magenta.copy(alpha=.6f*breathe),s*.010f,Offset(s*(.282f+i*.13f),s*.612f))
    }
    drawRoundRect(Color(0xFF171821),Offset(s*.66f,s*.52f),Size(s*.12f,s*.15f),CornerRadius(s*.012f))
    repeat(3){i->drawLine(violet.copy(alpha=.55f),Offset(s*.67f,s*(.55f+i*.035f)),Offset(s*.77f,s*(.55f+i*.035f)),s*.009f)}
    if(stage>=1) drawCircle(violet.copy(alpha=.12f*breathe),s*.32f,Offset(s*.5f,s*.52f))
    if(stage>=2) repeat(5){i->drawCircle(magenta,s*.008f,Offset(s*(.28f+i*.10f),s*.69f))}
    if(stage>=3) drawArc(violet.copy(alpha=.55f),185f+phase*25f,165f,false,Offset(s*.13f,s*.14f),Size(s*.74f,s*.70f),style=Stroke(s*.014f))
    if(stage>=4) repeat(if(lowPower)3 else 6){i->val a=i*PI.toFloat()/3f+phase;drawLine(violet.copy(alpha=.32f),Offset(s*.5f+cos(a)*s*.28f,s*.5f+sin(a)*s*.20f),Offset(s*.5f+cos(a)*s*.42f,s*.5f+sin(a)*s*.30f),s*.010f)}
    if(stage>=5) drawCircle(Color.White.copy(alpha=.12f*breathe),s*.40f,Offset(s*.5f,s*.5f),style=Stroke(s*.018f))
}

private fun DrawScope.drawGroupProgressionRing(color:Color,phase:Float,radius:Float,nodes:Int){
    val s=size.minDimension;val c=Offset(s*.5f,s*.5f)
    drawCircle(color.copy(alpha=.30f),s*radius,c,style=Stroke(s*.010f))
    repeat(nodes){i->val a=phase*PI.toFloat()*2f+i*PI.toFloat()*2f/nodes;val p=Offset(c.x+cos(a)*s*radius,c.y+sin(a)*s*radius);drawCircle(color.copy(alpha=.75f),s*.010f,p)}
}
private fun DrawScope.drawGroupSpokes(color:Color,phase:Float,count:Int){
    val s=size.minDimension;val c=Offset(s*.5f,s*.5f);repeat(count){i->val a=phase*PI.toFloat()*.5f+i*PI.toFloat()*2f/count;drawLine(color.copy(alpha=.34f),Offset(c.x+cos(a)*s*.38f,c.y+sin(a)*s*.38f),Offset(c.x+cos(a)*s*.47f,c.y+sin(a)*s*.47f),s*.008f)}
}
private fun DrawScope.drawGroupCrown(color:Color,phase:Float){
    val s=size.minDimension;drawArc(Color(0xFFFFE07A).copy(alpha=.65f),-30f+phase*20f,230f,false,Offset(s*.07f,s*.07f),Size(s*.86f,s*.86f),style=Stroke(s*.014f));drawArc(color.copy(alpha=.48f),160f-phase*16f,145f,false,Offset(s*.11f,s*.11f),Size(s*.78f,s*.78f),style=Stroke(s*.009f))
}
private fun DrawScope.drawGroupMastery(color:Color,breathe:Float,lowPower:Boolean){
    val s=size.minDimension;drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.13f*breathe),color.copy(alpha=.08f),Color.Transparent)),s*.50f,Offset(s*.5f,s*.5f));repeat(if(lowPower)4 else 8){i->val a=i*PI.toFloat()/4f;drawCircle(Color.White.copy(alpha=.65f),s*.007f,Offset(s*.5f+cos(a)*s*.46f,s*.5f+sin(a)*s*.46f))}
}
