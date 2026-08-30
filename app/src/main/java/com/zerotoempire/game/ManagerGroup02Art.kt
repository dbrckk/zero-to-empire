package com.zerotoempire.game

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
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = .27f
    val id=businessId.coerceIn(4,7)
    val accent=when(id){4->Color(0xFF43E6FF);5->Color(0xFF4FA8FF);6->Color(0xFFEAF6FF);else->Color(0xFFFF654F)}
    val secondary=when(id){4->Color(0xFF8CFFDC);5->Color(0xFF6FE3FF);6->Color(0xFF78DFFF);else->Color(0xFFFFB34D)}
    val skin=when(id){4->Color(0xFFD49A74);5->Color(0xFF9C664A);6->Color(0xFFF0C7A3);else->Color(0xFFB87854)}
    val hair=when(id){4->Color(0xFF151A28);5->Color(0xFF303744);6->Color(0xFFD8DCE5);else->Color(0xFF3D2018)}
    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.27f),EmpireColors.SurfaceHigh,EmpireColors.Void)),RoundedCornerShape(portraitSize*.31f))){
        Canvas(Modifier.fillMaxSize()){
            val s=size.minDimension;val c=Offset(s*.5f,s*.5f)
            drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.08f),accent.copy(alpha=.11f),Color.Transparent),Offset(s*.42f,s*.30f),s*.45f),s*.47f,c)
            drawCircle(accent.copy(alpha=.63f),s*.425f,c,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.16f),s*.455f,c,style=Stroke(s*.006f))
            drawArc(Color.White.copy(alpha=.20f),205f,72f,false,Offset(s*.085f,s*.085f),Size(s*.83f,s*.83f),style=Stroke(s*.007f))
            val nodeCount=if(lowPower)2 else 5
            repeat(nodeCount){i->val a=phase*2*PI.toFloat()+i*2*PI.toFloat()/nodeCount;val p=Offset(c.x+cos(a)*s*.395f,c.y+sin(a)*s*.395f);drawCircle(Color.Black.copy(alpha=.34f),s*.015f,p);drawCircle(if(i%2==0)accent else secondary,s*.009f,p)}
            val torso=Path().apply{moveTo(s*.16f,s*.88f);quadraticTo(s*.23f,s*.59f,s*.5f,s*.56f);quadraticTo(s*.77f,s*.59f,s*.84f,s*.88f);close()}
            val torsoBase=when(id){4->Color(0xFF102A3D);5->Color(0xFF172C45);6->Color(0xFFCBD7E2);else->Color(0xFF3A1D1A)}
            drawPath(torso,Brush.linearGradient(listOf(torsoBase,Color(0xFF10141D)),Offset(s*.28f,s*.58f),Offset(s*.72f,s*.86f)))
            drawPath(torso,accent.copy(alpha=.76f),style=Stroke(s*.019f))
            drawLine(Color.White.copy(alpha=.20f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.82f),s*.008f)
            drawLine(secondary.copy(alpha=.25f),Offset(s*.29f,s*.67f),Offset(s*.40f,s*.80f),s*.006f)
            drawRoundRect(skin,Offset(s*.455f,s*.49f),Size(s*.09f,s*.14f))
            drawCircle(accent.copy(alpha=.11f),s*.177f,Offset(s*.5f,s*.36f))
            drawCircle(skin,s*.164f,Offset(s*.5f,s*.36f))
            drawArc(hair,188f,166f,true,Offset(s*.325f,s*.155f),Size(s*.35f,s*.31f))
            drawArc(Color.White.copy(alpha=.10f),205f,72f,false,Offset(s*.35f,s*.21f),Size(s*.30f,s*.29f),style=Stroke(s*.006f))
            drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.445f,s*.36f));drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.555f,s*.36f))
            drawCircle(Color.White.copy(alpha=.70f),s*.004f,Offset(s*.441f,s*.356f));drawCircle(Color.White.copy(alpha=.70f),s*.004f,Offset(s*.551f,s*.356f))
            drawLine(Color(0xFF75413A),Offset(s*.466f,s*.438f),Offset(s*.534f,s*.438f),s*.008f)
            when(id){
                4->{ drawLine(accent,Offset(s*.39f,s*.345f),Offset(s*.48f,s*.345f),s*.013f);drawLine(accent,Offset(s*.52f,s*.345f),Offset(s*.61f,s*.345f),s*.013f);drawLine(secondary,Offset(s*.48f,s*.345f),Offset(s*.52f,s*.345f),s*.007f);drawRoundRect(accent.copy(alpha=.13f),Offset(s*.24f,s*.63f),Size(s*.22f,s*.13f),CornerRadius(s*.018f));drawRoundRect(accent.copy(alpha=.86f),Offset(s*.24f,s*.63f),Size(s*.22f,s*.13f),CornerRadius(s*.018f),style=Stroke(s*.010f));drawLine(Color.White.copy(alpha=.78f),Offset(s*.27f,s*.69f),Offset(s*.42f,s*.69f),s*.007f);drawCircle(secondary.copy(alpha=.8f),s*.008f,Offset(s*.405f,s*.655f)) }
                5->{ drawLine(accent,Offset(s*.29f,s*.64f),Offset(s*.42f,s*.77f),s*.015f);drawLine(secondary,Offset(s*.42f,s*.77f),Offset(s*.52f,s*.64f),s*.015f);drawRect(accent.copy(alpha=.20f),Offset(s*.60f,s*.62f),Size(s*.12f,s*.15f));drawRect(secondary.copy(alpha=.38f),Offset(s*.60f,s*.62f),Size(s*.12f,s*.15f),style=Stroke(s*.009f));repeat(3){i->drawLine(Color.White.copy(alpha=.62f),Offset(s*(.62f+i*.035f),s*.65f),Offset(s*(.62f+i*.035f),s*.74f),s*.006f)} }
                6->{ drawArc(accent,190f,160f,false,Offset(s*.31f,s*.23f),Size(s*.38f,s*.29f),style=Stroke(s*.018f));drawCircle(secondary.copy(alpha=.14f),s*.205f,Offset(s*.5f,s*.36f),style=Stroke(s*.009f));drawCircle(EmpireArtPalette.Cyan,s*.022f,Offset(s*.67f,s*.69f));drawCircle(secondary.copy(alpha=.22f),s*.052f,Offset(s*.67f,s*.69f));drawLine(EmpireArtPalette.Cyan,Offset(s*.60f,s*.69f),Offset(s*.73f,s*.69f),s*.009f) }
                else->{ drawLine(accent,Offset(s*.31f,s*.61f),Offset(s*.42f,s*.76f),s*.022f);drawLine(secondary,Offset(s*.69f,s*.61f),Offset(s*.58f,s*.76f),s*.022f);drawCircle(accent.copy(alpha=.18f),s*.052f,Offset(s*.5f,s*.68f));drawCircle(EmpireArtPalette.GoldHot,s*.022f,Offset(s*.5f,s*.68f));drawCircle(accent.copy(alpha=.30f),s*.055f,Offset(s*.68f,s*.69f),style=Stroke(s*.013f));drawLine(secondary,Offset(s*.65f,s*.69f),Offset(s*.71f,s*.69f),s*.008f) }
            }
        }
    }
}
