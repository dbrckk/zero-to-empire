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
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Final art pass for Group 02: Tech Company, Megacity, Moon Colony, Mars Empire. */
@Composable
fun BusinessGroup02Sprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val motion = rememberInfiniteTransition(label = "group02-$id")
    val phaseAnimated by motion.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 9800 else 6100 + id * 280, easing = LinearEasing)), label = "phase")
    val breatheAnimated by motion.animateFloat(.84f, 1f, infiniteRepeatable(tween(if (lowPower) 2900 else 1750 + id * 110), RepeatMode.Reverse), label = "breathe")
    val phase = if (reduced) .22f else phaseAnimated
    val breathe = if (reduced) .92f else breatheAnimated
    val stage = group02Stage(level)
    val accent = group02Accent(id)

    Box(modifier.size(iconSize).background(Brush.radialGradient(0f to accent.copy(alpha=.23f+stage*.02f), .46f to EmpireColors.SurfaceHigh, 1f to EmpireColors.Void), RoundedCornerShape(iconSize*.27f))) {
        Canvas(Modifier.fillMaxSize()) {
            val s=size.minDimension
            val c=Offset(s*.5f,s*.52f)
            drawOval(Brush.radialGradient(listOf(accent.copy(alpha=.24f),Color.Transparent),Offset(c.x,s*.78f),s*.40f),Offset(s*.10f,s*.69f),Size(s*.80f,s*.22f))
            drawCircle(accent.copy(alpha=.08f*breathe),s*.47f,c)
            drawCircle(accent.copy(alpha=.30f),s*.42f,c,style=Stroke(s*.012f))
            when(id.coerceIn(4,7)) {
                4 -> drawTechCompanyAAA(stage,phase,breathe)
                5 -> drawMegacityAAA(stage,phase,breathe,lowPower)
                6 -> drawMoonColonyAAA(stage,phase,breathe,lowPower)
                else -> drawMarsEmpireAAA(stage,phase,breathe,lowPower)
            }
            if(stage>=1) drawGroup02Ring(accent,phase,.435f,3)
            if(stage>=2) drawGroup02Ring(Color.White,1f-phase,.475f,5)
            if(stage>=3) drawGroup02Spokes(accent,phase,if(lowPower)4 else 8)
            if(stage>=4) drawGroup02Crown(accent,phase)
            if(stage>=5) drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.12f*breathe),accent.copy(alpha=.08f),Color.Transparent)),s*.52f,c)
        }
    }
}

private fun group02Stage(level:Int)=when{level>=1000->5;level>=500->4;level>=250->3;level>=100->2;level>=25->1;else->0}
private fun group02Accent(id:Int)=when(id){4->Color(0xFF8C7CFF);5->Color(0xFFB861FF);6->Color(0xFF9FE8FF);else->Color(0xFFFF6C5F)}

private fun DrawScope.drawTechCompanyAAA(stage:Int,phase:Float,breathe:Float){
    val s=size.minDimension; val purple=group02Accent(4); val cyan=Color(0xFF6EEAFF); val steel=Color(0xFF303849)
    drawRoundRect(steel,Offset(s*.20f,s*.31f),Size(s*.60f,s*.44f),CornerRadius(s*.06f))
    drawRoundRect(Color(0xFF151B28),Offset(s*.24f,s*.35f),Size(s*.52f,s*.36f),CornerRadius(s*.05f))
    repeat(4){i-> val x=.29f+i*.13f; drawRoundRect(if(i%2==0)purple.copy(alpha=.65f) else cyan.copy(alpha=.55f),Offset(s*x,s*.40f),Size(s*.085f,s*.21f),CornerRadius(s*.014f))}
    drawCircle(purple,s*.105f,Offset(s*.5f,s*.48f),style=Stroke(s*.026f)); drawCircle(Color.White,s*.024f,Offset(s*.5f,s*.48f))
    repeat(if(stage>=3)10 else 6){i->val a=phase*2f*PI.toFloat()/1f+i*2f*PI.toFloat()/(if(stage>=3)10 else 6);drawLine(cyan.copy(alpha=.65f),Offset(s*.5f+cos(a)*s*.13f,s*.48f+sin(a)*s*.13f),Offset(s*.5f+cos(a)*s*.22f,s*.48f+sin(a)*s*.22f),s*.010f)}
    if(stage>=1) drawRoundRect(purple.copy(alpha=.45f*breathe),Offset(s*.31f,s*.22f),Size(s*.38f,s*.06f),CornerRadius(s*.018f))
    if(stage>=2) repeat(3){i->drawCircle(cyan,s*.012f,Offset(s*(.36f+i*.14f),s*.67f))}
    if(stage>=4) drawArc(Color.White.copy(alpha=.45f),200f+phase*15f,140f,false,Offset(s*.16f,s*.15f),Size(s*.68f,s*.68f),style=Stroke(s*.012f))
    if(stage>=5) repeat(5){i->drawCircle(Color(0xFFFFE79B),s*.009f,Offset(s*(.30f+i*.10f),s*.20f))}
}

private fun DrawScope.drawMegacityAAA(stage:Int,phase:Float,breathe:Float,lowPower:Boolean){
    val s=size.minDimension; val violet=group02Accent(5); val cyan=Color(0xFF59E8FF)
    val xs=listOf(.16f,.27f,.38f,.50f,.62f,.73f); val hs=listOf(.27f,.40f,.33f,.50f,.39f,.29f)
    xs.forEachIndexed{i,x->val h=s*(hs[i]+stage*.012f);val w=s*if(i==3).12f else .095f;drawRoundRect(Brush.verticalGradient(listOf(violet.copy(alpha=.80f),Color(0xFF242838))),Offset(s*x,s*.76f-h),Size(w,h),CornerRadius(s*.016f));repeat(if(lowPower)2 else 4){r->drawCircle(if((i+r)%2==0)cyan else Color(0xFFFFD46A),s*.007f,Offset(s*(x+.03f),s*.71f-h+r*s*.055f))}}
    drawLine(violet.copy(alpha=.70f),Offset(s*.17f,s*.77f),Offset(s*.83f,s*.77f),s*.013f)
    if(stage>=1) drawArc(cyan.copy(alpha=.45f),190f+phase*12f,160f,false,Offset(s*.14f,s*.14f),Size(s*.72f,s*.72f),style=Stroke(s*.010f))
    if(stage>=2) repeat(if(lowPower)3 else 6){i->val a=phase*2*PI+i*2*PI/(if(lowPower)3 else 6);drawCircle(violet.copy(alpha=.8f),s*.010f,Offset(s*.5f+cos(a).toFloat()*s*.33f,s*.50f+sin(a).toFloat()*s*.10f))}
    if(stage>=3) drawRoundRect(Color.White.copy(alpha=.10f*breathe),Offset(s*.28f,s*.18f),Size(s*.44f,s*.055f),CornerRadius(s*.018f))
    if(stage>=4) repeat(3){i->drawLine(cyan.copy(alpha=.50f),Offset(s*(.29f+i*.19f),s*.66f),Offset(s*(.29f+i*.19f),s*.28f),s*.006f)}
    if(stage>=5) drawCircle(violet.copy(alpha=.14f*breathe),s*.36f,Offset(s*.5f,s*.49f))
}

private fun DrawScope.drawMoonColonyAAA(stage:Int,phase:Float,breathe:Float,lowPower:Boolean){
    val s=size.minDimension; val ice=group02Accent(6); val steel=Color(0xFF8AA5B7); val dark=Color(0xFF202A35)
    drawOval(Color(0xFF68737A),Offset(s*.15f,s*.68f),Size(s*.70f,s*.12f)); drawOval(Color.White.copy(alpha=.10f),Offset(s*.23f,s*.70f),Size(s*.17f,s*.04f))
    listOf(.28f,.50f,.72f).forEachIndexed{i,x->val r=s*(.115f+i*.012f);drawCircle(dark,r,Offset(s*x,s*.56f));drawCircle(ice.copy(alpha=.35f),r*.84f,Offset(s*x,s*.56f));drawArc(Color.White.copy(alpha=.50f),205f,90f,false,Offset(s*x-r*.78f,s*.56f-r*.78f),Size(r*1.56f,r*1.56f),style=Stroke(s*.008f))}
    drawLine(steel,Offset(s*.34f,s*.62f),Offset(s*.44f,s*.62f),s*.018f); drawLine(steel,Offset(s*.56f,s*.62f),Offset(s*.66f,s*.62f),s*.018f)
    val dishA=phase*2f*PI.toFloat(); val dishC=Offset(s*.51f,s*.35f);drawLine(steel,dishC,Offset(dishC.x+cos(dishA)*s*.08f,dishC.y+sin(dishA)*s*.04f),s*.010f);drawArc(ice.copy(alpha=.75f),210f+phase*20f,120f,false,Offset(s*.44f,s*.28f),Size(s*.14f,s*.10f),style=Stroke(s*.012f))
    if(stage>=1) repeat(3){i->drawCircle(ice.copy(alpha=.55f*breathe),s*.013f,Offset(s*(.32f+i*.18f),s*.45f))}
    if(stage>=2) drawArc(Color.White.copy(alpha=.36f),185f+phase*15f,170f,false,Offset(s*.13f,s*.16f),Size(s*.74f,s*.62f),style=Stroke(s*.010f))
    if(stage>=3) repeat(if(lowPower)2 else 4){i->drawCircle(Color(0xFFE9FBFF),s*.009f,Offset(s*(.28f+i*.14f),s*.74f))}
    if(stage>=4) drawCircle(ice.copy(alpha=.12f*breathe),s*.35f,Offset(s*.5f,s*.53f))
    if(stage>=5) repeat(5){i->drawCircle(Color.White.copy(alpha=.85f),s*.008f,Offset(s*(.30f+i*.10f),s*.20f))}
}

private fun DrawScope.drawMarsEmpireAAA(stage:Int,phase:Float,breathe:Float,lowPower:Boolean){
    val s=size.minDimension; val red=group02Accent(7); val gold=Color(0xFFFFC85A); val dark=Color(0xFF3A2321)
    drawOval(Color(0xFF6E352E),Offset(s*.12f,s*.70f),Size(s*.76f,s*.12f))
    val palace=Path().apply{moveTo(s*.20f,s*.71f);lineTo(s*.20f,s*.45f);lineTo(s*.34f,s*.34f);lineTo(s*.42f,s*.42f);lineTo(s*.50f,s*.27f);lineTo(s*.58f,s*.42f);lineTo(s*.66f,s*.34f);lineTo(s*.80f,s*.45f);lineTo(s*.80f,s*.71f);close()}
    drawPath(palace,Brush.verticalGradient(listOf(red.copy(alpha=.85f),dark)));drawPath(palace,gold.copy(alpha=.60f),style=Stroke(s*.012f))
    drawCircle(gold.copy(alpha=.70f*breathe),s*.055f,Offset(s*.5f,s*.47f));drawCircle(Color.White,s*.014f,Offset(s*.5f,s*.47f))
    repeat(4){i->drawRoundRect(Color(0xFF1F1515),Offset(s*(.28f+i*.13f),s*.56f),Size(s*.07f,s*.11f),CornerRadius(s*.012f))}
    repeat(if(lowPower)2 else 4){i->val a=phase*2*PI+i*2*PI/(if(lowPower)2 else 4);drawCircle(red.copy(alpha=.75f),s*.010f,Offset(s*.5f+cos(a).toFloat()*s*.30f,s*.50f+sin(a).toFloat()*s*.13f))}
    if(stage>=1) drawLine(gold,Offset(s*.24f,s*.73f),Offset(s*.76f,s*.73f),s*.012f)
    if(stage>=2) repeat(3){i->drawCircle(red,s*.012f,Offset(s*(.36f+i*.14f),s*.33f))}
    if(stage>=3) drawArc(red.copy(alpha=.55f),200f+phase*18f,140f,false,Offset(s*.16f,s*.15f),Size(s*.68f,s*.68f),style=Stroke(s*.012f))
    if(stage>=4) drawCircle(gold.copy(alpha=.12f*breathe),s*.35f,Offset(s*.5f,s*.50f))
    if(stage>=5) repeat(5){i->drawCircle(gold,s*.009f,Offset(s*(.30f+i*.10f),s*.19f))}
}

private fun DrawScope.drawGroup02Ring(color:Color,phase:Float,radius:Float,nodes:Int){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);drawCircle(color.copy(alpha=.28f),s*radius,c,style=Stroke(s*.009f));repeat(nodes){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes;drawCircle(color.copy(alpha=.82f),s*.010f,Offset(c.x+cos(a)*s*radius,c.y+sin(a)*s*radius))}}
private fun DrawScope.drawGroup02Spokes(color:Color,phase:Float,count:Int){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);repeat(count){i->val a=phase*PI.toFloat()*.35f+i*2f*PI.toFloat()/count;drawLine(color.copy(alpha=.35f),Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f),Offset(c.x+cos(a)*s*.48f,c.y+sin(a)*s*.48f),s*.007f)}}
private fun DrawScope.drawGroup02Crown(color:Color,phase:Float){val s=size.minDimension;drawArc(Color(0xFFFFD76A).copy(alpha=.65f),-35f+phase*16f,240f,false,Offset(s*.08f,s*.08f),Size(s*.84f,s*.84f),style=Stroke(s*.012f));drawArc(color.copy(alpha=.40f),160f-phase*12f,160f,false,Offset(s*.12f,s*.12f),Size(s*.76f,s*.76f),style=Stroke(s*.009f))}
