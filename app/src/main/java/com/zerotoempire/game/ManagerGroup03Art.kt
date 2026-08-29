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

/** Megastructure executives: stellar engineering and galactic finance. */
@Composable
fun ManagerGroup03Portrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase: Float = if (reduced || lowPower) {
        .32f
    } else {
        val transition = rememberInfiniteTransition(label = "manager-g3-$businessId")
        val animated by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(8800, easing = LinearEasing)), label = "phase")
        animated
    }
    val sol = businessId == 8
    val accent = if (sol) Color(0xFFFFD75E) else Color(0xFFB86CFF)
    val secondary = if (sol) Color(0xFFFF8E46) else Color(0xFF55D9FF)
    val skin = if (sol) Color(0xFFD5A077) else Color(0xFFB57A59)
    val hair = if (sol) Color(0xFFE4D8C5) else Color(0xFF171A23)

    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.29f), EmpireColors.SurfaceHigh, EmpireColors.Void)), RoundedCornerShape(portraitSize*.31f))) {
        Canvas(Modifier.fillMaxSize()) {
            val s=size.minDimension; val c=Offset(s*.5f,s*.5f)
            drawCircle(accent.copy(alpha=.13f),s*.47f,c)
            drawCircle(accent.copy(alpha=.66f),s*.425f,c,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.22f),s*.455f,c,style=Stroke(s*.007f))
            val nodes=if(lowPower)3 else 7
            repeat(nodes){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes;drawCircle(if(i%2==0)accent else secondary,s*.010f,Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f))}
            val torso=Path().apply{moveTo(s*.15f,s*.88f);quadraticTo(s*.23f,s*.58f,s*.5f,s*.56f);quadraticTo(s*.77f,s*.58f,s*.85f,s*.88f);close()}
            drawPath(torso, if(sol) Color(0xFF302716) else Color(0xFF20162E))
            drawPath(torso,accent.copy(alpha=.78f),style=Stroke(s*.019f))
            drawRoundRect(skin,Offset(s*.455f,s*.49f),Size(s*.09f,s*.14f))
            drawCircle(skin,s*.165f,Offset(s*.5f,s*.36f))
            drawArc(hair,188f,166f,true,Offset(s*.325f,s*.155f),Size(s*.35f,s*.31f))
            drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.445f,s*.36f));drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.555f,s*.36f))
            drawLine(Color(0xFF75413A),Offset(s*.466f,s*.438f),Offset(s*.534f,s*.438f),s*.008f)
            if(sol){
                drawArc(accent,205f,130f,false,Offset(s*.31f,s*.17f),Size(s*.38f,s*.22f),style=Stroke(s*.018f))
                repeat(5){i->val a=(-.48f+i*.24f)*PI.toFloat();drawLine(accent.copy(alpha=.78f),Offset(s*.5f+cos(a)*s*.17f,s*.25f+sin(a)*s*.06f),Offset(s*.5f+cos(a)*s*.24f,s*.18f+sin(a)*s*.09f),s*.010f)}
                drawCircle(EmpireArtPalette.GoldHot,s*.025f,Offset(s*.66f,s*.69f))
                drawCircle(accent.copy(alpha=.55f),s*.064f,Offset(s*.66f,s*.69f),style=Stroke(s*.012f))
                repeat(4){i->val a=i*PI.toFloat()/2f+phase;drawLine(accent,Offset(s*.66f+cos(a)*s*.045f,s*.69f+sin(a)*s*.045f),Offset(s*.66f+cos(a)*s*.085f,s*.69f+sin(a)*s*.085f),s*.008f)}
            }else{
                drawLine(accent,Offset(s*.39f,s*.345f),Offset(s*.48f,s*.345f),s*.013f);drawLine(accent,Offset(s*.52f,s*.345f),Offset(s*.61f,s*.345f),s*.013f);drawLine(secondary,Offset(s*.48f,s*.345f),Offset(s*.52f,s*.345f),s*.007f)
                val graph=Path().apply{moveTo(s*.25f,s*.74f);lineTo(s*.32f,s*.69f);lineTo(s*.39f,s*.72f);lineTo(s*.47f,s*.63f)}
                drawPath(graph,secondary,style=Stroke(s*.014f))
                drawArc(accent.copy(alpha=.7f),190f,160f,false,Offset(s*.57f,s*.62f),Size(s*.17f,s*.12f),style=Stroke(s*.012f))
                drawCircle(Color.White.copy(alpha=.8f),s*.010f,Offset(s*.655f,s*.68f))
            }
        }
    }
}
