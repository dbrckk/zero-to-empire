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
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** First executive class: grounded entrepreneurs with strong profession silhouettes. */
@Composable
fun ManagerGroup01Portrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase: Float = if (reduced) {
        .18f
    } else {
        val transition = rememberInfiniteTransition(label = "manager-g1-$businessId")
        val animated by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 12000 else 7600, easing = LinearEasing)), label = "phase")
        animated
    }
    val accent = when (businessId) {
        0 -> Color(0xFF69E08A)
        1 -> Color(0xFF56BFFF)
        2 -> Color(0xFFFFA54D)
        else -> Color(0xFFC28BFF)
    }
    val skin = listOf(Color(0xFFB87550), Color(0xFFE5B38B), Color(0xFFF0C39B), Color(0xFF8C593F))[businessId.coerceIn(0,3)]
    val hair = listOf(Color(0xFF1B1720), Color(0xFF493126), Color(0xFF6C452D), Color(0xFF181B22))[businessId.coerceIn(0,3)]

    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.30f), EmpireColors.SurfaceHigh, EmpireColors.Void)), RoundedCornerShape(portraitSize*.31f))) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension; val c = Offset(s*.5f,s*.5f)
            drawCircle(accent.copy(alpha=.13f),s*.47f,c)
            drawCircle(accent.copy(alpha=.62f),s*.425f,c,style=Stroke(s*.017f))
            drawArc(Color.White.copy(alpha=.16f),205f,70f,false,Offset(s*.09f,s*.09f),Size(s*.82f,s*.82f),style=Stroke(s*.008f))
            val orbiters = if (lowPower) 2 else 4
            repeat(orbiters){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/orbiters;drawCircle(accent.copy(alpha=.72f),s*.010f,Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f))}
            val torso=Path().apply{moveTo(s*.17f,s*.88f);quadraticTo(s*.25f,s*.59f,s*.5f,s*.57f);quadraticTo(s*.75f,s*.59f,s*.83f,s*.88f);close()}
            drawPath(torso,when(businessId){0->Color(0xFF17352A);1->Color(0xFF173047);2->Color(0xFF3A271B);else->Color(0xFF272037)})
            drawPath(torso,accent.copy(alpha=.75f),style=Stroke(s*.019f))
            drawLine(Color.White.copy(alpha=.18f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.83f),s*.008f)
            drawRoundRect(skin,Offset(s*.455f,s*.50f),Size(s*.09f,s*.13f))
            drawCircle(skin,s*.166f,Offset(s*.5f,s*.365f))
            drawArc(hair,188f,166f,true,Offset(s*.325f,s*.16f),Size(s*.35f,s*.31f))
            drawCircle(EmpireArtPalette.Ink,s*.012f,Offset(s*.445f,s*.365f));drawCircle(EmpireArtPalette.Ink,s*.012f,Offset(s*.555f,s*.365f))
            drawLine(Color(0xFF7A4138),Offset(s*.465f,s*.445f),Offset(s*.535f,s*.445f),s*.009f)
            when(businessId){
                0 -> { val cap=Path().apply{moveTo(s*.34f,s*.245f);quadraticTo(s*.5f,s*.12f,s*.66f,s*.245f);lineTo(s*.62f,s*.275f);lineTo(s*.37f,s*.275f);close()};drawPath(cap,Color(0xFF143C2B));drawPath(cap,accent,style=Stroke(s*.014f));drawLine(accent,Offset(s*.55f,s*.245f),Offset(s*.70f,s*.275f),s*.018f);drawCircle(EmpireArtPalette.GoldHot,s*.013f,Offset(s*.655f,s*.39f));drawRoundRect(accent.copy(alpha=.30f),Offset(s*.28f,s*.67f),Size(s*.16f,s*.09f),style=Stroke(s*.014f)) }
                1 -> { drawLine(accent,Offset(s*.395f,s*.35f),Offset(s*.475f,s*.35f),s*.014f);drawLine(accent,Offset(s*.525f,s*.35f),Offset(s*.605f,s*.35f),s*.014f);drawLine(accent,Offset(s*.475f,s*.35f),Offset(s*.525f,s*.35f),s*.009f);drawLine(accent,Offset(s*.5f,s*.59f),Offset(s*.47f,s*.76f),s*.022f);drawLine(accent,Offset(s*.5f,s*.59f),Offset(s*.53f,s*.76f),s*.022f);drawRoundRect(accent.copy(alpha=.28f),Offset(s*.62f,s*.65f),Size(s*.10f,s*.07f),style=Stroke(s*.012f)) }
                2 -> { drawArc(accent,190f,160f,false,Offset(s*.345f,s*.30f),Size(s*.31f,s*.13f),style=Stroke(s*.020f));drawCircle(Color.White.copy(alpha=.7f),s*.010f,Offset(s*.43f,s*.355f));drawCircle(Color.White.copy(alpha=.7f),s*.010f,Offset(s*.57f,s*.355f));drawLine(accent,Offset(s*.32f,s*.61f),Offset(s*.43f,s*.73f),s*.018f);drawLine(accent,Offset(s*.68f,s*.61f),Offset(s*.57f,s*.73f),s*.018f);drawCircle(EmpireArtPalette.GoldHot,s*.020f,Offset(s*.67f,s*.70f)) }
                else -> { val helmet=Path().apply{moveTo(s*.34f,s*.26f);quadraticTo(s*.38f,s*.14f,s*.5f,s*.14f);quadraticTo(s*.62f,s*.14f,s*.66f,s*.26f);lineTo(s*.69f,s*.28f);lineTo(s*.31f,s*.28f);close()};drawPath(helmet,Color(0xFF2C2338));drawPath(helmet,accent,style=Stroke(s*.016f));drawLine(EmpireArtPalette.GoldHot,Offset(s*.5f,s*.145f),Offset(s*.5f,s*.265f),s*.016f);drawRoundRect(accent.copy(alpha=.26f),Offset(s*.61f,s*.65f),Size(s*.11f,s*.10f),style=Stroke(s*.014f));repeat(3){i->drawCircle(Color.White.copy(alpha=.65f),s*.007f,Offset(s*(.635f+i*.03f),s*.70f))} }
            }
        }
    }
}
