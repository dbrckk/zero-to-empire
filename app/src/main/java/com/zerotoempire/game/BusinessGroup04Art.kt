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
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Final business tier: reality-scale machinery and transcendent infrastructure. */
@Composable
fun BusinessGroup04Sprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase: Float
    val pulse = .90f
    if (reduced) {
        phase = .21f
    } else {
        val motion = rememberInfiniteTransition(label = "group04-$id")
        val phaseAnim by motion.animateFloat(0f,1f,infiniteRepeatable(tween(if(lowPower)14000 else 8200,easing=LinearEasing)),label="phase")
        phase = phaseAnim
    }
    val stage=when{level>=1000->5;level>=500->4;level>=250->3;level>=100->2;level>=25->1;else->0}
    val accent=if(id==12) Color(0xFFFF68D8) else Color(0xFFFFE36E)

    Box(modifier.size(iconSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.24f),EmpireColors.SurfaceHigh,EmpireColors.Void)),RoundedCornerShape(iconSize*.28f))){
        Canvas(Modifier.fillMaxSize()){
            val s=size.minDimension;val c=Offset(s*.5f,s*.51f)
            drawCircle(accent.copy(alpha=.10f*pulse),s*.47f,c)
            drawCircle(accent.copy(alpha=.32f),s*.42f,c,style=Stroke(s*.010f))
            if(id==12) drawRealityEngineFinal(stage,phase,pulse,lowPower) else drawTranscendentNexusFinal(stage,phase,pulse,lowPower)
            if(stage>=1) drawCircle(accent.copy(alpha=.34f),s*.45f,c,style=Stroke(s*.008f))
            if(stage>=2) repeat(if(lowPower)4 else 8){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/4f;drawCircle(Color.White.copy(alpha=.80f),s*.008f,Offset(c.x+cos(a)*s*.45f,c.y+sin(a)*s*.45f))}
            if(stage>=3) drawArc(Color.White.copy(alpha=.38f),phase*360f,245f,false,Offset(s*.035f,s*.035f),Size(s*.93f,s*.93f),style=Stroke(s*.008f))
            if(stage>=4) drawArc(accent.copy(alpha=.55f),180f-phase*270f,150f,false,Offset(s*.07f,s*.07f),Size(s*.86f,s*.86f),style=Stroke(s*.012f))
            if(stage>=5){drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.16f*pulse),accent.copy(alpha=.08f),Color.Transparent),c,s*.52f),s*.52f,c);repeat(if(lowPower)6 else 12){i->val a=i*2f*PI.toFloat()/(if(lowPower)6 else 12);drawCircle(Color.White,s*.006f,Offset(c.x+cos(a)*s*.49f,c.y+sin(a)*s*.49f))}}
        }
    }
}

private fun DrawScope.drawRealityEngineFinal(stage:Int,phase:Float,pulse:Float,lowPower:Boolean){
    val s=size.minDimension;val c=Offset(s*.5f,s*.51f);val pink=Color(0xFFFF68D8);val cyan=Color(0xFF6EEBFF)
    repeat(4){r->val rx=s*(.12f+r*.055f);val ry=rx*(.48f+r*.08f);drawArc(if(r%2==0)pink.copy(alpha=.82f-r*.12f) else cyan.copy(alpha=.72f-r*.10f),phase*360f*(if(r%2==0)1 else -1)+r*47f,255f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(s*(.024f-r*.003f)))}
    drawCircle(Brush.radialGradient(listOf(Color.White,pink.copy(alpha=.82f),Color.Transparent),c,s*.105f),s*.105f,c)
    val nodes=if(lowPower)5 else 10;repeat(nodes){i->val a=-phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes;drawCircle(if(i%2==0)cyan else pink,s*.010f,Offset(c.x+cos(a)*s*.31f,c.y+sin(a)*s*.19f))}
    if(stage>=2){val diamond=Path().apply{moveTo(c.x,s*.13f);lineTo(s*.79f,c.y);lineTo(c.x,s*.87f);lineTo(s*.21f,c.y);close()};drawPath(diamond,pink.copy(alpha=.30f),style=Stroke(s*.009f))}
    if(stage>=4) repeat(4){i->val a=i*PI.toFloat()/2f+phase;drawLine(color=pink.copy(alpha=.40f),start=c,end=Offset(c.x+cos(a)*s*.37f,c.y+sin(a)*s*.37f),strokeWidth=s*.006f)}
}

private fun DrawScope.drawTranscendentNexusFinal(stage:Int,phase:Float,pulse:Float,lowPower:Boolean){
    val s=size.minDimension;val c=Offset(s*.5f,s*.51f);val gold=Color(0xFFFFE36E);val violet=Color(0xFFC68BFF)
    drawCircle(Brush.radialGradient(listOf(Color.White,gold.copy(alpha=.86f),violet.copy(alpha=.34f),Color.Transparent),c,s*.18f),s*.18f,c)
    repeat(3){r->drawCircle(if(r%2==0)gold.copy(alpha=.72f-r*.15f) else violet.copy(alpha=.58f),s*(.22f+r*.065f),c,style=Stroke(s*(.020f-r*.004f)))}
    val rays=if(lowPower)6 else 12;repeat(rays){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/rays;val inner=s*.20f;val outer=s*(.32f+(i%3)*.045f);drawLine(color=if(i%2==0)gold else violet,start=Offset(c.x+cos(a)*inner,c.y+sin(a)*inner),end=Offset(c.x+cos(a)*outer,c.y+sin(a)*outer),strokeWidth=s*.012f)}
    if(stage>=2) repeat(6){i->val a=-phase*PI.toFloat()+i*PI.toFloat()/3f;drawCircle(Color.White.copy(alpha=.88f),s*.009f,Offset(c.x+cos(a)*s*.37f,c.y+sin(a)*s*.23f))}
    if(stage>=3) drawCircle(gold.copy(alpha=.12f*pulse),s*.39f,c)
    if(stage>=4) drawArc(violet.copy(alpha=.55f),-30f+phase*40f,300f,false,Offset(s*.09f,s*.09f),Size(s*.82f,s*.82f),style=Stroke(s*.011f))
}
