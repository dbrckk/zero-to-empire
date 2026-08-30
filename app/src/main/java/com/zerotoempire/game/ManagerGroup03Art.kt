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

/** Megastructure executives: stellar engineering and galactic finance. */
@Composable
fun ManagerGroup03Portrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = .32f
    val sol = businessId == 8
    val accent = if (sol) Color(0xFFFFD75E) else Color(0xFFB86CFF)
    val secondary = if (sol) Color(0xFFFF8E46) else Color(0xFF55D9FF)
    val skin = if (sol) Color(0xFFD5A077) else Color(0xFFB57A59)
    val hair = if (sol) Color(0xFFE4D8C5) else Color(0xFF171A23)

    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.29f), EmpireColors.SurfaceHigh, EmpireColors.Void)), RoundedCornerShape(portraitSize*.31f))) {
        Canvas(Modifier.fillMaxSize()) {
            val s=size.minDimension
            val c=Offset(s*.5f,s*.5f)

            // Cinematic lens depth stays completely static; the existing portrait path remains cheap in lists.
            drawCircle(
                Brush.radialGradient(
                    listOf(Color.White.copy(alpha=.10f), accent.copy(alpha=.10f), secondary.copy(alpha=.045f), Color.Transparent),
                    center = Offset(s*.42f,s*.29f),
                    radius = s*.49f
                ),
                s*.47f,
                c
            )
            drawCircle(accent.copy(alpha=.66f),s*.425f,c,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.24f),s*.455f,c,style=Stroke(s*.007f))
            drawArc(Color.White.copy(alpha=.22f),205f,70f,false,Offset(s*.08f,s*.08f),Size(s*.84f,s*.84f),style=Stroke(s*.007f))
            drawArc(secondary.copy(alpha=.24f),18f,100f,false,Offset(s*.105f,s*.105f),Size(s*.79f,s*.79f),style=Stroke(s*.005f))

            val nodes=if(lowPower)3 else 7
            repeat(nodes){i->
                val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes
                val p=Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f)
                drawCircle(Color.Black.copy(alpha=.42f),s*.016f,p)
                drawCircle(if(i%2==0)accent else secondary,s*.009f,p)
            }

            val torso=Path().apply{moveTo(s*.15f,s*.88f);quadraticTo(s*.23f,s*.58f,s*.5f,s*.56f);quadraticTo(s*.77f,s*.58f,s*.85f,s*.88f);close()}
            drawPath(
                torso,
                Brush.linearGradient(
                    if(sol) listOf(Color(0xFF4A3816),Color(0xFF211B12)) else listOf(Color(0xFF38214B),Color(0xFF181222)),
                    Offset(s*.26f,s*.58f),
                    Offset(s*.74f,s*.88f)
                )
            )
            drawPath(torso,accent.copy(alpha=.82f),style=Stroke(s*.019f))
            drawLine(Color.White.copy(alpha=.18f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.83f),s*.007f)
            drawLine(secondary.copy(alpha=.28f),Offset(s*.30f,s*.67f),Offset(s*.41f,s*.80f),s*.006f)

            drawRoundRect(skin,Offset(s*.455f,s*.49f),Size(s*.09f,s*.14f))
            drawCircle(accent.copy(alpha=.14f),s*.176f,Offset(s*.5f,s*.36f))
            drawCircle(skin,s*.165f,Offset(s*.5f,s*.36f))
            drawArc(hair,188f,166f,true,Offset(s*.325f,s*.155f),Size(s*.35f,s*.31f))
            drawArc(Color.White.copy(alpha=.13f),205f,74f,false,Offset(s*.35f,s*.205f),Size(s*.30f,s*.29f),style=Stroke(s*.006f))
            drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.445f,s*.36f));drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.555f,s*.36f))
            drawCircle(Color.White.copy(alpha=.70f),s*.004f,Offset(s*.442f,s*.357f));drawCircle(Color.White.copy(alpha=.70f),s*.004f,Offset(s*.552f,s*.357f))
            drawLine(Color(0xFF75413A),Offset(s*.466f,s*.438f),Offset(s*.534f,s*.438f),s*.008f)

            if(sol){
                drawArc(accent,205f,130f,false,Offset(s*.31f,s*.17f),Size(s*.38f,s*.22f),style=Stroke(s*.018f))
                drawArc(secondary.copy(alpha=.42f),212f,112f,false,Offset(s*.335f,s*.195f),Size(s*.33f,s*.17f),style=Stroke(s*.006f))
                repeat(5){i->val a=(-.48f+i*.24f)*PI.toFloat();drawLine(accent.copy(alpha=.78f),Offset(s*.5f+cos(a)*s*.17f,s*.25f+sin(a)*s*.06f),Offset(s*.5f+cos(a)*s*.24f,s*.18f+sin(a)*s*.09f),s*.010f)}
                val core=Offset(s*.66f,s*.69f)
                drawCircle(secondary.copy(alpha=.18f),s*.080f,core)
                drawCircle(EmpireArtPalette.GoldHot,s*.025f,core)
                drawCircle(accent.copy(alpha=.60f),s*.064f,core,style=Stroke(s*.012f))
                repeat(4){i->val a=i*PI.toFloat()/2f+phase;drawLine(accent,Offset(core.x+cos(a)*s*.045f,core.y+sin(a)*s*.045f),Offset(core.x+cos(a)*s*.085f,core.y+sin(a)*s*.085f),s*.008f)}
                if(!lowPower){
                    repeat(3){i->drawCircle(Color.White.copy(alpha=.70f),s*.006f,Offset(s*(.28f+i*.055f),s*.615f))}
                }
            }else{
                drawLine(accent,Offset(s*.39f,s*.345f),Offset(s*.48f,s*.345f),s*.013f);drawLine(accent,Offset(s*.52f,s*.345f),Offset(s*.61f,s*.345f),s*.013f);drawLine(secondary,Offset(s*.48f,s*.345f),Offset(s*.52f,s*.345f),s*.007f)
                drawLine(Color.White.copy(alpha=.20f),Offset(s*.40f,s*.327f),Offset(s*.47f,s*.327f),s*.004f)
                val graph=Path().apply{moveTo(s*.25f,s*.74f);lineTo(s*.32f,s*.69f);lineTo(s*.39f,s*.72f);lineTo(s*.47f,s*.63f)}
                drawPath(graph,secondary,style=Stroke(s*.014f))
                drawPath(graph,Color.White.copy(alpha=.16f),style=Stroke(s*.004f))
                drawArc(accent.copy(alpha=.72f),190f,160f,false,Offset(s*.57f,s*.62f),Size(s*.17f,s*.12f),style=Stroke(s*.012f))
                drawCircle(secondary.copy(alpha=.20f),s*.032f,Offset(s*.655f,s*.68f))
                drawCircle(Color.White.copy(alpha=.84f),s*.010f,Offset(s*.655f,s*.68f))
                if(!lowPower){
                    repeat(3){i->drawLine(accent.copy(alpha=.40f),Offset(s*(.58f+i*.045f),s*.77f),Offset(s*(.60f+i*.045f),s*.73f),s*.005f)}
                }
            }
        }
    }
}
