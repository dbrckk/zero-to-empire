package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun OnboardingStepArt(step: Int) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val transition = rememberInfiniteTransition(label = "onboarding-art")
    val phaseAnim by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 12000 else 7000, easing = LinearEasing)), label = "phase")
    val phase = if (reduced) .2f else phaseAnim
    Canvas(Modifier.size(220.dp)) {
        val s = size.minDimension
        val c = Offset(s * .5f, s * .5f)
        val accents = listOf(EmpireColors.Gold, EmpireColors.Cyan, Color(0xFFFF9B55), EmpireColors.Violet, Color(0xFFFFE36E))
        val accent = accents[step.coerceIn(0, 4)]
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha = .23f), Color.Transparent), c, s * .5f), s * .5f, c)
        drawCircle(EmpireColors.SurfaceHigh.copy(alpha = .78f), s * .36f, c)
        drawCircle(accent.copy(alpha = .72f), s * .36f, c, style = Stroke(s * .012f))
        when (step.coerceIn(0, 4)) {
            0 -> {
                drawCircle(accent.copy(alpha=.25f),s*.18f,c)
                drawCircle(accent,s*.12f,c,style=Stroke(s*.025f))
                drawCircle(Color.White,s*.045f,c)
                repeat(if(lowPower)4 else 8){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/4f;drawLine(Offset(c.x+cos(a)*s*.15f,c.y+sin(a)*s*.15f),Offset(c.x+cos(a)*s*.28f,c.y+sin(a)*s*.28f),s*.012f,accent)}
            }
            1 -> {
                val base=s*.68f
                repeat(3){i->val x=s*(.28f+i*.18f);val h=s*(.22f+i*.06f);drawRoundRect(Color(0xFF17263A),Offset(x-s*.06f,base-h),Size(s*.12f,h));drawLine(accent,Offset(x-s*.04f,base-h+s*.05f),Offset(x+s*.04f,base-h+s*.05f),s*.012f)}
                drawLine(accent.copy(alpha=.65f),Offset(s*.22f,base),Offset(s*.78f,base),s*.018f)
            }
            2 -> {
                repeat(4){r->drawCircle(accent.copy(alpha=.72f-r*.12f),s*(.10f+r*.055f),c,style=Stroke(s*(.020f-r*.002f)))}
                repeat(if(lowPower)4 else 8){i->val a=-phase*2f*PI.toFloat()+i*PI.toFloat()/4f;drawCircle(Color.White,s*.012f,Offset(c.x+cos(a)*s*.29f,c.y+sin(a)*s*.29f))}
                drawCircle(Color.White,s*.045f,c)
            }
            3 -> {
                drawCircle(Color(0xFFD9AE86),s*.105f,Offset(c.x,c.y-s*.08f))
                drawArc(Color(0xFF18243A),185f,170f,true,Offset(c.x-s*.115f,c.y-s*.205f),Size(s*.23f,s*.18f))
                val torso=Path().apply{moveTo(s*.32f,s*.69f);quadraticTo(s*.36f,s*.52f,c.x,s*.52f);quadraticTo(s*.64f,s*.52f,s*.68f,s*.69f);close()};drawPath(torso,Color(0xFF1A3150));drawPath(torso,accent,style=Stroke(s*.016f))
                repeat(if(lowPower)3 else 6){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/3f;drawCircle(accent,s*.012f,Offset(c.x+cos(a)*s*.28f,c.y+sin(a)*s*.28f))}
            }
            4 -> {
                val diamond=Path().apply{moveTo(c.x,s*.22f);lineTo(s*.75f,c.y);lineTo(c.x,s*.78f);lineTo(s*.25f,c.y);close()};drawPath(diamond,accent.copy(alpha=.15f));drawPath(diamond,accent,style=Stroke(s*.020f))
                drawCircle(Brush.radialGradient(listOf(Color.White,accent,Color.Transparent),c,s*.16f),s*.16f,c)
                repeat(if(lowPower)4 else 8){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/4f;drawCircle(if(i%2==0)EmpireColors.Cyan else accent,s*.014f,Offset(c.x+cos(a)*s*.31f,c.y+sin(a)*s*.22f))}
            }
        }
    }
}

@Composable
fun CelebrationBusinessSprite(businessId: Int, level: Int, size: androidx.compose.ui.unit.Dp = 116.dp) {
    when (businessId) {
        in 0..3 -> { BusinessGroup01Sprite(businessId, level, size); BusinessGroup01Evolution(businessId, level, size) }
        in 4..7 -> { BusinessGroup02Sprite(businessId, level, size); BusinessGroup02Evolution(businessId, level, size) }
        in 8..11 -> BusinessGroup03Sprite(businessId, level, size)
        in 12..13 -> BusinessGroup04Sprite(businessId, level, size)
    }
}
