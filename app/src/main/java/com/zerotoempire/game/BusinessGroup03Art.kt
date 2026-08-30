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

/** AAA art pass for Group 03: Dyson Network, Galactic Exchange, Intergalactic Gateway, Cosmic Foundry. */
@Composable
fun BusinessGroup03Sprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val motion = if (reduced) null else rememberInfiniteTransition(label = "group03-$id")
    val phase = if (motion == null) .24f else {
        val phaseAnim by motion.animateFloat(
            0f, 1f,
            infiniteRepeatable(tween(if (lowPower) 12_000 else 7_400 + id * 220, easing = LinearEasing)),
            label = "phase"
        )
        phaseAnim
    }
    val pulse = if (reduced) .90f else .86f + .08f * ((sin(phase * 2f * PI.toFloat() - PI.toFloat() / 2f) + 1f) * .5f)
    val stage = group03Stage(level)
    val accent = group03Accent(id)

    Box(
        modifier = modifier
            .size(iconSize)
            .background(
                Brush.radialGradient(
                    0f to accent.copy(alpha = .25f + stage * .018f),
                    .48f to EmpireColors.SurfaceHigh,
                    1f to EmpireColors.Void
                ),
                RoundedCornerShape(iconSize * .27f)
            )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val c = Offset(s * .5f, s * .52f)
            drawCircle(Brush.radialGradient(listOf(accent.copy(alpha=.18f*pulse), Color.Transparent), c, s*.46f), s*.46f, c)
            drawCircle(accent.copy(alpha=.32f), s*.41f, c, style=Stroke(s*.011f))
            val starCount = if (lowPower) 10 else 20
            repeat(starCount) { i ->
                val a = i * 2f * PI.toFloat() / starCount
                val r = s * (.34f + (i % 3) * .045f)
                drawCircle(Color.White.copy(alpha=.18f + (i%4)*.06f), if(i%5==0)s*.009f else s*.005f, Offset(c.x+cos(a)*r,c.y+sin(a)*r))
            }
            when (id.coerceIn(8, 11)) {
                8 -> drawDysonNetworkAAA(stage, phase, pulse, lowPower)
                9 -> drawGalacticExchangeAAA(stage, phase, pulse, lowPower)
                10 -> drawIntergalacticGatewayAAA(stage, phase, pulse, lowPower)
                else -> drawCosmicFoundryAAA(stage, phase, pulse, lowPower)
            }
            if (stage >= 1) drawGroup03Ring(accent, phase, .435f, if(lowPower)3 else 5)
            if (stage >= 2) drawGroup03Ring(Color.White, 1f-phase, .475f, if(lowPower)4 else 7)
            if (stage >= 3) drawGroup03Spokes(accent, phase, if(lowPower)6 else 12)
            if (stage >= 4) drawGroup03Crown(accent, phase)
            if (stage >= 5) drawGroup03Mastery(accent, pulse, lowPower)
        }
    }
}

private fun group03Stage(level:Int)=when{level>=1000->5;level>=500->4;level>=250->3;level>=100->2;level>=25->1;else->0}
private fun group03Accent(id:Int)=when(id){8->Color(0xFFFFD45A);9->Color(0xFF5BE6FF);10->Color(0xFF9F7CFF);else->Color(0xFFFF65D7)}

private fun DrawScope.drawDysonNetworkAAA(stage:Int, phase:Float, pulse:Float, lowPower:Boolean){
    val s=size.minDimension; val c=Offset(s*.5f,s*.50f); val gold=group03Accent(8); val white=Color(0xFFFFF3C2)
    drawCircle(Brush.radialGradient(listOf(Color.White,Color(0xFFFFEE9A),Color(0xFFFFB42F),Color.Transparent),c,s*.18f),s*.18f,c)
    drawCircle(gold.copy(alpha=.55f),s*.25f,c,style=Stroke(s*.018f))
    drawCircle(white.copy(alpha=.35f),s*.31f,c,style=Stroke(s*.010f))
    val panels=if(lowPower)8 else 16
    repeat(panels){i-> val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/panels; val p=Offset(c.x+cos(a)*s*.31f,c.y+sin(a)*s*.31f); drawRoundRect(gold.copy(alpha=.78f),Offset(p.x-s*.028f,p.y-s*.014f),Size(s*.056f,s*.028f),CornerRadius(s*.006f))}
    if(stage>=1) drawCircle(gold.copy(alpha=.28f*pulse),s*.36f,c,style=Stroke(s*.014f))
    if(stage>=2) repeat(if(lowPower)4 else 8){i->val a=-phase*2f*PI.toFloat()+i*PI.toFloat()/4f;val p=Offset(c.x+cos(a)*s*.38f,c.y+sin(a)*s*.20f);drawCircle(white,s*.010f,p)}
    if(stage>=3) repeat(6){i->val a=i*PI.toFloat()/3f;drawLine(gold.copy(alpha=.45f),Offset(c.x+cos(a)*s*.18f,c.y+sin(a)*s*.18f),Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f),s*.007f)}
    if(stage>=4) drawArc(white.copy(alpha=.55f),-20f+phase*25f,260f,false,Offset(s*.10f,s*.10f),Size(s*.80f,s*.80f),style=Stroke(s*.012f))
    if(stage>=5) drawCircle(gold.copy(alpha=.16f*pulse),s*.43f,c)
}

private fun DrawScope.drawGalacticExchangeAAA(stage:Int, phase:Float, pulse:Float, lowPower:Boolean){
    val s=size.minDimension; val c=Offset(s*.5f,s*.52f); val cyan=group03Accent(9); val violet=Color(0xFF7D78FF)
    drawOval(Color(0xFF182238),Offset(s*.18f,s*.57f),Size(s*.64f,s*.18f))
    repeat(3){r->drawOval(if(r%2==0)cyan.copy(alpha=.55f) else violet.copy(alpha=.45f),Offset(s*(.22f+r*.04f),s*(.36f+r*.055f)),Size(s*(.56f-r*.08f),s*(.27f-r*.05f)),style=Stroke(s*.015f))}
    drawRoundRect(Color(0xFF26334D),Offset(s*.38f,s*.33f),Size(s*.24f,s*.32f),CornerRadius(s*.035f))
    drawRoundRect(cyan.copy(alpha=.55f),Offset(s*.42f,s*.38f),Size(s*.16f,s*.19f),CornerRadius(s*.020f))
    val traderCount = if(lowPower)4 else 9
    repeat(traderCount){i->val a=phase*2*PI+i*2*PI/traderCount;val x=c.x+cos(a).toFloat()*s*.34f;val y=c.y+sin(a).toFloat()*s*.13f;drawCircle(if(i%2==0)cyan else Color(0xFFFFD36A),s*.009f,Offset(x,y))}
    if(stage>=1) drawArc(cyan.copy(alpha=.55f),180f+phase*35f,170f,false,Offset(s*.13f,s*.17f),Size(s*.74f,s*.64f),style=Stroke(s*.010f))
    if(stage>=2) repeat(4){i->drawLine(violet.copy(alpha=.45f),Offset(s*(.29f+i*.14f),s*.68f),Offset(s*(.34f+i*.10f),s*.42f),s*.006f)}
    if(stage>=3) drawCircle(cyan.copy(alpha=.11f*pulse),s*.34f,c)
    if(stage>=4) repeat(3){i->drawCircle(Color.White.copy(alpha=.8f),s*.009f,Offset(s*(.38f+i*.12f),s*.28f))}
    if(stage>=5) drawArc(Color.White.copy(alpha=.52f),-30f+phase*20f,280f,false,Offset(s*.08f,s*.08f),Size(s*.84f,s*.84f),style=Stroke(s*.012f))
}

private fun DrawScope.drawIntergalacticGatewayAAA(stage:Int, phase:Float, pulse:Float, lowPower:Boolean){
    val s=size.minDimension; val c=Offset(s*.5f,s*.51f); val violet=group03Accent(10); val cyan=Color(0xFF6EEBFF)
    drawCircle(Color(0xFF121629),s*.25f,c)
    drawCircle(violet.copy(alpha=.75f),s*.25f,c,style=Stroke(s*.045f))
    drawCircle(cyan.copy(alpha=.55f),s*.18f,c,style=Stroke(s*.020f))
    val aperture=s*(.11f+.015f*pulse);drawCircle(Brush.radialGradient(listOf(Color.White,violet,Color.Transparent),c,aperture),aperture,c)
    repeat(if(lowPower)4 else 8){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/4f; val inner=Offset(c.x+cos(a)*s*.27f,c.y+sin(a)*s*.27f); val outer=Offset(c.x+cos(a)*s*.38f,c.y+sin(a)*s*.38f);drawLine(if(i%2==0)violet else cyan,inner,outer,s*.018f)}
    if(stage>=1) drawCircle(violet.copy(alpha=.25f),s*.34f,c,style=Stroke(s*.012f))
    if(stage>=2) repeat(if(lowPower)3 else 6){i->val a=-phase*2f*PI.toFloat()+i*PI.toFloat()/3f;drawCircle(Color.White.copy(alpha=.82f),s*.010f,Offset(c.x+cos(a)*s*.36f,c.y+sin(a)*s*.20f))}
    if(stage>=3) drawArc(cyan.copy(alpha=.55f),195f+phase*22f,150f,false,Offset(s*.10f,s*.12f),Size(s*.80f,s*.76f),style=Stroke(s*.012f))
    if(stage>=4) drawCircle(violet.copy(alpha=.13f*pulse),s*.42f,c)
    if(stage>=5) repeat(5){i->drawCircle(Color.White,s*.008f,Offset(s*(.30f+i*.10f),s*.18f))}
}

private fun DrawScope.drawCosmicFoundryAAA(stage:Int, phase:Float, pulse:Float, lowPower:Boolean){
    val s=size.minDimension; val c=Offset(s*.5f,s*.52f); val magenta=group03Accent(11); val gold=Color(0xFFFFC85A)
    val body=Path().apply{moveTo(s*.20f,s*.70f);lineTo(s*.26f,s*.40f);lineTo(s*.38f,s*.32f);lineTo(s*.50f,s*.20f);lineTo(s*.62f,s*.32f);lineTo(s*.74f,s*.40f);lineTo(s*.80f,s*.70f);close()}
    drawPath(body,Brush.verticalGradient(listOf(Color(0xFF452550),Color(0xFF171527))))
    drawPath(body,magenta.copy(alpha=.68f),style=Stroke(s*.014f))
    drawCircle(Brush.radialGradient(listOf(Color.White,gold,magenta.copy(alpha=.45f),Color.Transparent),c,s*.15f),s*.15f,c)
    repeat(if(lowPower)3 else 6){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/3f;val p=Offset(c.x+cos(a)*s*.23f,c.y+sin(a)*s*.15f);drawCircle(if(i%2==0)gold else magenta,s*.014f,p)}
    if(stage>=1) repeat(3){i->drawRoundRect(magenta.copy(alpha=.55f),Offset(s*(.30f+i*.16f),s*.58f),Size(s*.075f,s*.12f),CornerRadius(s*.012f))}
    if(stage>=2) drawArc(gold.copy(alpha=.52f),205f+phase*18f,130f,false,Offset(s*.15f,s*.13f),Size(s*.70f,s*.70f),style=Stroke(s*.012f))
    if(stage>=3) repeat(4){i->drawLine(magenta.copy(alpha=.55f),Offset(s*.50f,s*.22f),Offset(s*(.23f+i*.18f),s*.76f),s*.007f)}
    if(stage>=4) drawCircle(magenta.copy(alpha=.14f*pulse),s*.38f,c)
    if(stage>=5) repeat(7){i->drawCircle(Color.White.copy(alpha=.8f),s*.007f,Offset(s*(.27f+i*.075f),s*.16f))}
}

private fun DrawScope.drawGroup03Ring(color:Color,phase:Float,radius:Float,nodes:Int){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);drawCircle(color.copy(alpha=.26f),s*radius,c,style=Stroke(s*.008f));repeat(nodes){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes;drawCircle(color.copy(alpha=.86f),s*.009f,Offset(c.x+cos(a)*s*radius,c.y+sin(a)*s*radius))}}
private fun DrawScope.drawGroup03Spokes(color:Color,phase:Float,count:Int){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);repeat(count){i->val a=phase*PI.toFloat()*.28f+i*2f*PI.toFloat()/count;drawLine(color.copy(alpha=.30f),Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f),Offset(c.x+cos(a)*s*.49f,c.y+sin(a)*s*.49f),s*.006f)}}
private fun DrawScope.drawGroup03Crown(color:Color,phase:Float){val s=size.minDimension;drawArc(Color(0xFFFFE48A).copy(alpha=.62f),-45f+phase*18f,250f,false,Offset(s*.07f,s*.07f),Size(s*.86f,s*.86f),style=Stroke(s*.011f));drawArc(color.copy(alpha=.42f),165f-phase*15f,170f,false,Offset(s*.11f,s*.11f),Size(s*.78f,s*.78f),style=Stroke(s*.008f))}
private fun DrawScope.drawGroup03Mastery(color:Color,pulse:Float,lowPower:Boolean){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.13f*pulse),color.copy(alpha=.10f),Color.Transparent),c,s*.52f),s*.52f,c);repeat(if(lowPower)5 else 10){i->val a=i*2f*PI.toFloat()/(if(lowPower)5 else 10);drawCircle(Color.White.copy(alpha=.75f),s*.006f,Offset(c.x+cos(a)*s*.46f,c.y+sin(a)*s*.46f))}}
