package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
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
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = .18f
    val accent = when (businessId) {
        0 -> Color(0xFF69E08A)
        1 -> Color(0xFF56BFFF)
        2 -> Color(0xFFFFA54D)
        else -> Color(0xFFC28BFF)
    }
    val secondary = when (businessId) {
        0 -> Color(0xFFFFD166)
        1 -> Color(0xFF8CEBFF)
        2 -> Color(0xFFFFD27A)
        else -> Color(0xFF71D8FF)
    }
    val skin = listOf(Color(0xFFB87550), Color(0xFFE5B38B), Color(0xFFF0C39B), Color(0xFF8C593F))[businessId.coerceIn(0,3)]
    val hair = listOf(Color(0xFF1B1720), Color(0xFF493126), Color(0xFF6C452D), Color(0xFF181B22))[businessId.coerceIn(0,3)]

    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.30f), EmpireColors.SurfaceHigh, EmpireColors.Void)), RoundedCornerShape(portraitSize*.31f))) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension; val c = Offset(s*.5f,s*.5f)
            drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.08f),accent.copy(alpha=.12f),Color.Transparent),Offset(s*.42f,s*.31f),s*.43f),s*.47f,c)
            drawCircle(accent.copy(alpha=.62f),s*.425f,c,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.13f),s*.452f,c,style=Stroke(s*.005f))
            drawArc(Color.White.copy(alpha=.20f),205f,70f,false,Offset(s*.09f,s*.09f),Size(s*.82f,s*.82f),style=Stroke(s*.008f))
            drawLine(accent.copy(alpha=.72f),Offset(s*.12f,s*.20f),Offset(s*.12f,s*.32f),s*.010f)
            drawLine(accent.copy(alpha=.72f),Offset(s*.12f,s*.20f),Offset(s*.24f,s*.20f),s*.010f)
            drawLine(secondary.copy(alpha=.48f),Offset(s*.76f,s*.80f),Offset(s*.88f,s*.80f),s*.008f)
            drawCircle(accent.copy(alpha=.9f),s*.012f,Offset(s*.84f,s*.24f))
            val orbiters = if (lowPower) 2 else 4
            repeat(orbiters){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/orbiters;val p=Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f);drawCircle(Color.Black.copy(alpha=.34f),s*.016f,p);drawCircle(if(i%2==0)accent else secondary,s*.009f,p)}
            val torso=Path().apply{moveTo(s*.17f,s*.88f);quadraticTo(s*.25f,s*.59f,s*.5f,s*.57f);quadraticTo(s*.75f,s*.59f,s*.83f,s*.88f);close()}
            val torsoBase=when(businessId){0->Color(0xFF17352A);1->Color(0xFF173047);2->Color(0xFF3A271B);else->Color(0xFF272037)}
            drawPath(torso,Brush.linearGradient(listOf(torsoBase.copy(alpha=.92f),Color(0xFF10141E)),Offset(s*.28f,s*.58f),Offset(s*.72f,s*.86f)))
            drawPath(torso,accent.copy(alpha=.75f),style=Stroke(s*.019f))
            drawLine(Color.White.copy(alpha=.22f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.83f),s*.008f)
            drawLine(secondary.copy(alpha=.22f),Offset(s*.29f,s*.67f),Offset(s*.40f,s*.80f),s*.006f)
            drawRoundRect(skin,Offset(s*.455f,s*.50f),Size(s*.09f,s*.13f))
            drawCircle(accent.copy(alpha=.12f),s*.178f,Offset(s*.5f,s*.365f))
            drawCircle(skin,s*.166f,Offset(s*.5f,s*.365f))
            drawArc(hair,188f,166f,true,Offset(s*.325f,s*.16f),Size(s*.35f,s*.31f))
            drawArc(Color.White.copy(alpha=.11f),205f,72f,false,Offset(s*.35f,s*.215f),Size(s*.30f,s*.29f),style=Stroke(s*.006f))
            drawCircle(EmpireArtPalette.Ink,s*.012f,Offset(s*.445f,s*.365f));drawCircle(EmpireArtPalette.Ink,s*.012f,Offset(s*.555f,s*.365f))
            drawCircle(Color.White.copy(alpha=.68f),s*.004f,Offset(s*.441f,s*.361f));drawCircle(Color.White.copy(alpha=.68f),s*.004f,Offset(s*.551f,s*.361f))
            drawLine(Color(0xFF7A4138),Offset(s*.465f,s*.445f),Offset(s*.535f,s*.445f),s*.009f)
            when(businessId){
                0 -> { val cap=Path().apply{moveTo(s*.34f,s*.245f);quadraticTo(s*.5f,s*.12f,s*.66f,s*.245f);lineTo(s*.62f,s*.275f);lineTo(s*.37f,s*.275f);close()};drawPath(cap,Brush.linearGradient(listOf(Color(0xFF1D5A3C),Color(0xFF10291F)),Offset(s*.4f,s*.14f),Offset(s*.6f,s*.28f)));drawPath(cap,accent,style=Stroke(s*.014f));drawLine(secondary.copy(alpha=.8f),Offset(s*.55f,s*.245f),Offset(s*.70f,s*.275f),s*.018f);drawCircle(EmpireArtPalette.GoldHot,s*.013f,Offset(s*.655f,s*.39f));drawRoundRect(accent.copy(alpha=.18f),Offset(s*.28f,s*.67f),Size(s*.16f,s*.09f));drawRoundRect(accent.copy(alpha=.45f),Offset(s*.28f,s*.67f),Size(s*.16f,s*.09f),style=Stroke(s*.014f));drawLine(secondary.copy(alpha=.65f),Offset(s*.30f,s*.71f),Offset(s*.41f,s*.71f),s*.006f) }
                1 -> { drawLine(accent,Offset(s*.395f,s*.35f),Offset(s*.475f,s*.35f),s*.014f);drawLine(accent,Offset(s*.525f,s*.35f),Offset(s*.605f,s*.35f),s*.014f);drawLine(secondary,Offset(s*.475f,s*.35f),Offset(s*.525f,s*.35f),s*.007f);drawLine(accent,Offset(s*.5f,s*.59f),Offset(s*.47f,s*.76f),s*.022f);drawLine(accent,Offset(s*.5f,s*.59f),Offset(s*.53f,s*.76f),s*.022f);drawRoundRect(accent.copy(alpha=.15f),Offset(s*.62f,s*.65f),Size(s*.10f,s*.07f));drawRoundRect(secondary.copy(alpha=.55f),Offset(s*.62f,s*.65f),Size(s*.10f,s*.07f),style=Stroke(s*.010f));drawCircle(Color.White.copy(alpha=.75f),s*.006f,Offset(s*.67f,s*.685f)) }
                2 -> { drawArc(accent,190f,160f,false,Offset(s*.345f,s*.30f),Size(s*.31f,s*.13f),style=Stroke(s*.020f));drawArc(secondary.copy(alpha=.48f),200f,140f,false,Offset(s*.36f,s*.315f),Size(s*.28f,s*.10f),style=Stroke(s*.006f));drawCircle(Color.White.copy(alpha=.78f),s*.010f,Offset(s*.43f,s*.355f));drawCircle(Color.White.copy(alpha=.78f),s*.010f,Offset(s*.57f,s*.355f));drawLine(accent,Offset(s*.32f,s*.61f),Offset(s*.43f,s*.73f),s*.018f);drawLine(accent,Offset(s*.68f,s*.61f),Offset(s*.57f,s*.73f),s*.018f);drawCircle(accent.copy(alpha=.20f),s*.052f,Offset(s*.67f,s*.70f));drawCircle(EmpireArtPalette.GoldHot,s*.020f,Offset(s*.67f,s*.70f)) }
                else -> { val helmet=Path().apply{moveTo(s*.34f,s*.26f);quadraticTo(s*.38f,s*.14f,s*.5f,s*.14f);quadraticTo(s*.62f,s*.14f,s*.66f,s*.26f);lineTo(s*.69f,s*.28f);lineTo(s*.31f,s*.28f);close()};drawPath(helmet,Brush.linearGradient(listOf(Color(0xFF44345C),Color(0xFF211A2C)),Offset(s*.4f,s*.14f),Offset(s*.6f,s*.28f)));drawPath(helmet,accent,style=Stroke(s*.016f));drawLine(EmpireArtPalette.GoldHot,Offset(s*.5f,s*.145f),Offset(s*.5f,s*.265f),s*.016f);drawLine(secondary.copy(alpha=.55f),Offset(s*.38f,s*.225f),Offset(s*.62f,s*.225f),s*.006f);drawRoundRect(accent.copy(alpha=.16f),Offset(s*.61f,s*.65f),Size(s*.11f,s*.10f));drawRoundRect(accent.copy(alpha=.48f),Offset(s*.61f,s*.65f),Size(s*.11f,s*.10f),style=Stroke(s*.014f));repeat(3){i->drawCircle(Color.White.copy(alpha=.72f),s*.007f,Offset(s*(.635f+i*.03f),s*.70f))} }
            }
        }
    }
}
