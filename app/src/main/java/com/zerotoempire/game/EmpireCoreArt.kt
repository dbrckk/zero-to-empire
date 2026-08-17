package com.zerotoempire.game

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
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
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun EmpireCoreGlyph(modifier: Modifier = Modifier) {
    val vm: GameViewModel = viewModel()
    val state by vm.state.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val era = state.empireLevel.coerceIn(0, 10)

    val rotation: Float
    val fastRotation: Float
    val pulse: Float
    if (reducedMotion) {
        rotation = 0f; fastRotation = 0f; pulse = .94f
    } else {
        val infinite = rememberInfiniteTransition(label = "empireCore")
        val r by infinite.animateFloat(0f,360f,infiniteRepeatable(tween(if(lowPower)18_000 else 12_000,easing=LinearEasing)),label="coreRotation")
        val fr by infinite.animateFloat(0f,360f,infiniteRepeatable(tween(if(lowPower)8_000 else 4_800,easing=LinearEasing)),label="trailRotation")
        val p by infinite.animateFloat(.82f,1f,infiniteRepeatable(tween(if(lowPower)2_100 else 1_400,easing=FastOutSlowInEasing),RepeatMode.Reverse),label="corePulse")
        rotation=r; fastRotation=fr; pulse=p
    }

    val accent = coreAccent(era)
    val secondary = coreSecondary(era)
    val intensity = (3 + era).coerceAtMost(if(lowPower)7 else 13)
    val trailPoints = if(lowPower) 2 else 5

    Canvas(modifier) {
        val s=size.minDimension; val center=Offset(size.width/2f,size.height/2f)
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha=.20f*pulse),secondary.copy(alpha=.08f),Color.Transparent),center,s*.52f),s*.52f,center)

        repeat(intensity){i->
            val angle=Math.toRadians((fastRotation+i*(360f/intensity)).toDouble())
            val radius=s*(.31f+(i%4)*.04f)
            repeat(trailPoints){trail->
                val back=angle-trail*.072
                val alpha=(.30f-trail*.05f).coerceAtLeast(.05f)
                drawCircle(if(i%2==0)accent.copy(alpha=alpha) else secondary.copy(alpha=alpha),s*(.013f-trail*.0014f).coerceAtLeast(.006f),Offset(center.x+cos(back).toFloat()*radius,center.y+sin(back).toFloat()*radius))
            }
        }

        drawCoreEraGeometry(era,center,s,rotation,fastRotation,pulse,lowPower,accent,secondary)

        repeat((2+era/3).coerceAtMost(if(lowPower)3 else 5)){ring->
            val radius=s*(.22f+ring*.065f)
            drawCircle(if(ring%2==0)accent.copy(alpha=.58f) else secondary.copy(alpha=.48f),radius,center,style=Stroke(s*(.012f-ring*.001f)))
            val nodes=(if(lowPower)3 else 5)+ring*2
            repeat(nodes){i->
                val angle=Math.toRadians((rotation*(if(ring%2==0)1 else -1)+i*(360f/nodes)).toDouble())
                drawCircle(if(i%2==0)Color.White else accent,s*.013f,Offset(center.x+cos(angle).toFloat()*radius,center.y+sin(angle).toFloat()*radius))
            }
        }

        if(era>=4 && !lowPower) repeat((era-1).coerceAtMost(10)){i->
            val a=Math.toRadians((rotation*-1.25f+i*(360f/(era-1).coerceAtLeast(1))).toDouble())
            drawLine(accent.copy(alpha=.20f),Offset(center.x+cos(a).toFloat()*s*.18f,center.y+sin(a).toFloat()*s*.18f),Offset(center.x+cos(a).toFloat()*s*.49f,center.y+sin(a).toFloat()*s*.49f),s*.006f)
        }
    }
}

private fun coreAccent(era:Int)=when(era){
    0,1->Color(0xFFFFC857);2->Color(0xFF62E8FF);3->Color(0xFF7ED8FF);4->Color(0xFFFF765F);5->Color(0xFFFFD95A);6->Color(0xFF7ADFFF);7->Color(0xFFA685FF);8->Color(0xFFD58CFF);9->Color(0xFFFF66D8);else->Color(0xFFFFE477)}
private fun coreSecondary(era:Int)=when(era){
    0,1->Color(0xFF6EEBFF);2,3->Color(0xFFA38BFF);4->Color(0xFFFFC068);5->Color(0xFFFFF2B0);6->Color(0xFF766BFF);7,8->Color(0xFF60E9FF);9->Color(0xFF8E7CFF);else->Color(0xFFC68BFF)}

private fun DrawScope.drawCoreEraGeometry(era:Int,c:Offset,s:Float,rotation:Float,fast:Float,pulse:Float,lowPower:Boolean,accent:Color,secondary:Color){
    when {
        era<=1 -> {
            drawCircle(EmpireArtPalette.Ink,s*.16f,c)
            drawCircle(accent,s*.115f,c,style=Stroke(s*.024f))
            drawLine(accent,Offset(c.x,c.y-s*.075f),Offset(c.x,c.y+s*.075f),s*.022f)
            drawLine(accent,Offset(c.x-s*.05f,c.y-s*.05f),Offset(c.x+s*.05f,c.y-s*.05f),s*.022f)
        }
        era<=3 -> {
            drawCircle(Color(0xFF10192A),s*.15f,c)
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,Color.Transparent),c,s*.12f),s*.12f,c)
            repeat(4){i->val a=Math.toRadians((rotation+i*90f).toDouble());drawLine(accent,Offset(c.x+cos(a).toFloat()*s*.13f,c.y+sin(a).toFloat()*s*.13f),Offset(c.x+cos(a).toFloat()*s*.23f,c.y+sin(a).toFloat()*s*.23f),s*.014f)}
        }
        era<=5 -> {
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,Color(0xFFFF8B2F),Color.Transparent),c,s*.18f),s*.18f,c)
            repeat(if(lowPower)6 else 12){i->val a=Math.toRadians((fast+i*(360f/(if(lowPower)6 else 12))).toDouble());val p=Offset(c.x+cos(a).toFloat()*s*.25f,c.y+sin(a).toFloat()*s*.25f);drawCircle(accent,s*.012f,p)}
        }
        era<=7 -> {
            drawCircle(Color(0xFF0C1020),s*.145f,c)
            repeat(3){r->drawCircle(if(r%2==0)accent else secondary,s*(.12f+r*.055f),c,style=Stroke(s*(.024f-r*.004f)))}
            drawCircle(Brush.radialGradient(listOf(Color.White,secondary,Color.Transparent),c,s*.09f),s*.09f,c)
        }
        era<=9 -> {
            repeat(4){r->val rx=s*(.10f+r*.045f);val ry=rx*(.50f+r*.08f);drawArc(if(r%2==0)accent else secondary,rotation*(if(r%2==0)1f else -1f)+r*41f,250f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(s*(.023f-r*.003f)))}
            drawCircle(Color.White,s*.035f,c)
            if(era>=9){val d=Path().apply{moveTo(c.x,c.y-s*.27f);lineTo(c.x+s*.27f,c.y);lineTo(c.x,c.y+s*.27f);lineTo(c.x-s*.27f,c.y);close()};drawPath(d,accent.copy(alpha=.30f),style=Stroke(s*.008f))}
        }
        else -> {
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,secondary.copy(alpha=.55f),Color.Transparent),c,s*.20f),s*.20f*pulse,c)
            repeat(if(lowPower)6 else 12){i->val a=fast*PI.toFloat()/180f+i*2f*PI.toFloat()/(if(lowPower)6 else 12);val inner=s*.18f;val outer=s*(.30f+(i%3)*.035f);drawLine(if(i%2==0)accent else secondary,Offset(c.x+cos(a)*inner,c.y+sin(a)*inner),Offset(c.x+cos(a)*outer,c.y+sin(a)*outer),s*.011f)}
            drawCircle(Color.White.copy(alpha=.34f),s*.36f,c,style=Stroke(s*.008f))
        }
    }
}
