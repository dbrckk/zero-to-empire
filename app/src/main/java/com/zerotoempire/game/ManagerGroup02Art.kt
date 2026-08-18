package com.zerotoempire.game

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.*
import androidx.compose.ui.graphics.*
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.*

/** Expansion class: tech, city, lunar and Mars executives. */
@Composable
fun ManagerGroup02Portrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase: Float = if (reduced) {
        .27f
    } else {
        val t = rememberInfiniteTransition(label="manager-g2-$businessId")
        val animated by t.animateFloat(0f,1f,infiniteRepeatable(tween(if(lowPower) 15000 else 9000,easing=LinearEasing)),label="phase")
        animated
    }
    val id=businessId.coerceIn(4,7)
    val accent=when(id){4->Color(0xFF43E6FF);5->Color(0xFF4FA8FF);6->Color(0xFFEAF6FF);else->Color(0xFFFF654F)}
    val skin=when(id){4->Color(0xFFD49A74);5->Color(0xFF9C664A);6->Color(0xFFF0C7A3);else->Color(0xFFB87854)}
    val hair=when(id){4->Color(0xFF151A28);5->Color(0xFF303744);6->Color(0xFFD8DCE5);else->Color(0xFF3D2018)}
    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.27f),EmpireColors.SurfaceHigh,EmpireColors.Void)),RoundedCornerShape(portraitSize*.31f))){
        Canvas(Modifier.fillMaxSize()){
            val s=size.minDimension;val c=Offset(s*.5f,s*.5f)
            drawCircle(accent.copy(alpha=.12f),s*.47f,c);drawCircle(accent.copy(alpha=.63f),s*.425f,c,style=Stroke(s*.017f))
            repeat(if(lowPower)2 else 5){i->val a=phase*2*PI.toFloat()+i*2*PI.toFloat()/(if(lowPower)2 else 5);drawCircle(accent.copy(alpha=.72f),s*.009f,Offset(c.x+cos(a)*s*.395f,c.y+sin(a)*s*.395f))}
            val torso=Path().apply{moveTo(s*.16f,s*.88f);quadraticTo(s*.23f,s*.59f,s*.5f,s*.56f);quadraticTo(s*.77f,s*.59f,s*.84f,s*.88f);close()}
            drawPath(torso,when(id){4->Color(0xFF102A3D);5->Color(0xFF172C45);6->Color(0xFFCBD7E2);else->Color(0xFF3A1D1A)});drawPath(torso,accent.copy(alpha=.72f),style=Stroke(s*.019f))
            drawRoundRect(skin,Offset(s*.455f,s*.49f),Size(s*.09f,s*.14f));drawCircle(skin,s*.164f,Offset(s*.5f,s*.36f));drawArc(hair,188f,166f,true,Offset(s*.325f,s*.155f),Size(s*.35f,s*.31f))
            drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.445f,s*.36f));drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.555f,s*.36f));drawLine(Color(0xFF75413A),Offset(s*.466f,s*.438f),Offset(s*.534f,s*.438f),s*.008f)
            when(id){
                4->{ drawLine(accent,Offset(s*.39f,s*.345f),Offset(s*.48f,s*.345f),s*.013f);drawLine(accent,Offset(s*.52f,s*.345f),Offset(s*.61f,s*.345f),s*.013f);drawLine(accent,Offset(s*.48f,s*.345f),Offset(s*.52f,s*.345f),s*.007f);drawRoundRect(accent.copy(alpha=.16f),Offset(s*.24f,s*.63f),Size(s*.22f,s*.13f),CornerRadius(s*.018f));drawRoundRect(accent.copy(alpha=.9f),Offset(s*.24f,s*.63f),Size(s*.22f,s*.13f),CornerRadius(s*.018f),style=Stroke(s*.010f));drawLine(Color.White.copy(alpha=.75f),Offset(s*.27f,s*.69f),Offset(s*.42f,s*.69f),s*.007f) }
                5->{ drawLine(accent,Offset(s*.29f,s*.64f),Offset(s*.42f,s*.77f),s*.015f);drawLine(accent,Offset(s*.42f,s*.77f),Offset(s*.52f,s*.64f),s*.015f);drawRect(accent.copy(alpha=.25f),Offset(s*.60f,s*.62f),Size(s*.12f,s*.15f));repeat(3){i->drawLine(Color.White.copy(alpha=.55f),Offset(s*(.62f+i*.035f),s*.65f),Offset(s*(.62f+i*.035f),s*.74f),s*.006f)} }
                6->{ drawArc(accent,190f,160f,false,Offset(s*.31f,s*.23f),Size(s*.38f,s*.29f),style=Stroke(s*.018f));drawCircle(Color.White.copy(alpha=.12f),s*.20f,Offset(s*.5f,s*.36f),style=Stroke(s*.010f));drawCircle(EmpireArtPalette.Cyan,s*.022f,Offset(s*.67f,s*.69f));drawLine(EmpireArtPalette.Cyan,Offset(s*.60f,s*.69f),Offset(s*.73f,s*.69f),s*.009f) }
                else->{ drawLine(accent,Offset(s*.31f,s*.61f),Offset(s*.42f,s*.76f),s*.022f);drawLine(accent,Offset(s*.69f,s*.61f),Offset(s*.58f,s*.76f),s*.022f);drawCircle(EmpireArtPalette.GoldHot,s*.022f,Offset(s*.5f,s*.68f));drawCircle(accent.copy(alpha=.30f),s*.055f,Offset(s*.68f,s*.69f),style=Stroke(s*.013f));drawLine(accent,Offset(s*.65f,s*.69f),Offset(s*.71f,s*.69f),s*.008f) }
            }
        }
    }
}
