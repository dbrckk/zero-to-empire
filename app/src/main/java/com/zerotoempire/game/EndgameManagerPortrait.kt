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

@Composable
fun EndgameManagerPortrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = .31f
    val accent = when (businessId) {
        10 -> Color(0xFF67E8FF)
        11 -> Color(0xFFC692FF)
        12 -> Color(0xFFFF72D5)
        else -> Color(0xFFFFE27C)
    }
    val secondary = when (businessId) {
        10 -> Color(0xFF7D8CFF)
        11 -> Color(0xFF62E7FF)
        12 -> Color(0xFFFFB45C)
        else -> Color(0xFFC98BFF)
    }
    val skin = when (businessId) {
        10 -> Color(0xFFB97957)
        11 -> Color(0xFFE9B98B)
        12 -> Color(0xFF8F5A3C)
        else -> Color(0xFFF0C29B)
    }
    val hair = when (businessId) {
        10 -> Color(0xFF151C29)
        11 -> Color(0xFFEEE5D6)
        12 -> Color(0xFF2A163A)
        else -> Color(0xFFB98A55)
    }

    Box(
        Modifier.size(portraitSize).background(
            Brush.radialGradient(listOf(accent.copy(alpha=.32f), EmpireColors.SurfaceHigh, EmpireColors.Void)),
            RoundedCornerShape(portraitSize * .32f)
        )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val center = Offset(s*.5f,s*.5f)

            // Static executive-grade lighting: depth and hierarchy without another animation clock.
            drawCircle(
                Brush.radialGradient(
                    listOf(Color.White.copy(alpha=.10f), accent.copy(alpha=.11f), secondary.copy(alpha=.045f), Color.Transparent),
                    center = Offset(s*.43f, s*.31f),
                    radius = s*.50f
                ),
                s*.47f,
                center
            )
            drawCircle(accent.copy(alpha=.58f),s*.425f,center,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.18f),s*.455f,center,style=Stroke(s*.007f))
            drawArc(Color.White.copy(alpha=.24f),205f,72f,false,Offset(s*.075f,s*.075f),Size(s*.85f,s*.85f),style=Stroke(s*.007f))
            drawArc(accent.copy(alpha=.30f),18f,104f,false,Offset(s*.095f,s*.095f),Size(s*.81f,s*.81f),style=Stroke(s*.005f))

            val orbitCount = if(lowPower) 2 else 4
            repeat(orbitCount) { i ->
                val a = phase * 2f * PI.toFloat() + i * 2f * PI.toFloat() / orbitCount
                val p = Offset(center.x+cos(a)*s*.39f,center.y+sin(a)*s*.39f)
                drawCircle(Color.Black.copy(alpha=.42f),s*.018f,p)
                drawCircle(if(i%2==0) accent else secondary,s*.010f,p)
            }

            // Face receives a soft rim and highlight so it remains readable inside the dense endgame frame.
            drawCircle(accent.copy(alpha=.16f),s*.178f,Offset(s*.5f,s*.375f))
            drawCircle(skin,s*.165f,Offset(s*.5f,s*.375f))
            drawArc(hair,190f,160f,true,Offset(s*.325f,s*.18f),Size(s*.35f,s*.30f))
            drawArc(Color.White.copy(alpha=.13f),205f,75f,false,Offset(s*.352f,s*.225f),Size(s*.296f,s*.285f),style=Stroke(s*.007f))
            drawCircle(EmpireArtPalette.Ink,s*.014f,Offset(s*.445f,s*.375f))
            drawCircle(EmpireArtPalette.Ink,s*.014f,Offset(s*.555f,s*.375f))
            drawCircle(Color.White.copy(alpha=.72f),s*.0045f,Offset(s*.441f,s*.371f))
            drawCircle(Color.White.copy(alpha=.72f),s*.0045f,Offset(s*.551f,s*.371f))
            drawLine(accent.copy(alpha=.8f),Offset(s*.445f,s*.47f),Offset(s*.555f,s*.47f),s*.014f)

            val torso = Path().apply {
                moveTo(s*.21f,s*.84f)
                quadraticTo(s*.27f,s*.58f,s*.5f,s*.57f)
                quadraticTo(s*.73f,s*.58f,s*.79f,s*.84f)
                close()
            }
            drawPath(torso,Brush.linearGradient(listOf(Color(0xFF263B59),Color(0xFF111B2D)),Offset(s*.28f,s*.58f),Offset(s*.72f,s*.84f)))
            drawPath(torso,accent.copy(alpha=.8f),style=Stroke(s*.022f))
            drawLine(Color.White.copy(alpha=.25f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.80f),s*.010f)
            drawLine(secondary.copy(alpha=.30f),Offset(s*.31f,s*.68f),Offset(s*.42f,s*.80f),s*.007f)

            when (businessId) {
                10 -> {
                    drawArc(accent,195f,150f,false,Offset(s*.355f,s*.295f),Size(s*.29f,s*.16f),style=Stroke(s*.024f))
                    drawArc(secondary.copy(alpha=.55f),204f,132f,false,Offset(s*.37f,s*.31f),Size(s*.26f,s*.13f),style=Stroke(s*.007f))
                    drawCircle(Color.White.copy(alpha=.82f),s*.012f,Offset(s*.61f,s*.34f))
                    drawArc(accent.copy(alpha=.65f),205f,125f,false,Offset(s*.28f,s*.61f),Size(s*.44f,s*.18f),style=Stroke(s*.015f))
                    repeat(3){i->
                        val p=Offset(s*(.35f+i*.13f),s*.70f)
                        drawCircle(accent.copy(alpha=.22f),s*.022f,p)
                        drawCircle(Color.White.copy(alpha=.72f),s*.010f,p)
                    }
                }
                11 -> {
                    repeat(3){i->val x=s*(.40f+i*.10f);drawLine(accent,Offset(x,s*.205f),Offset(x+s*(i-1)*.025f,s*.14f),s*.016f)}
                    drawLine(secondary.copy(alpha=.55f),Offset(s*.36f,s*.25f),Offset(s*.64f,s*.25f),s*.006f)
                    drawRoundRect(accent.copy(alpha=.18f),Offset(s*.39f,s*.66f),Size(s*.22f,s*.10f))
                    drawRoundRect(accent.copy(alpha=.55f),Offset(s*.39f,s*.66f),Size(s*.22f,s*.10f),style=Stroke(s*.018f))
                    drawCircle(secondary.copy(alpha=.28f),s*.052f,Offset(s*.5f,s*.71f))
                    drawCircle(Color.White.copy(alpha=.84f),s*.022f,Offset(s*.5f,s*.71f))
                }
                12 -> {
                    drawArc(accent,165f,205f,false,Offset(s*.34f,s*.285f),Size(s*.32f,s*.19f),style=Stroke(s*.022f))
                    drawArc(secondary.copy(alpha=.48f),185f,160f,false,Offset(s*.365f,s*.31f),Size(s*.27f,s*.14f),style=Stroke(s*.007f))
                    drawLine(accent.copy(alpha=.7f),Offset(s*.31f,s*.64f),Offset(s*.69f,s*.79f),s*.016f)
                    drawLine(Color.White.copy(alpha=.28f),Offset(s*.33f,s*.77f),Offset(s*.67f,s*.64f),s*.010f)
                    drawCircle(secondary.copy(alpha=.24f),s*.060f,Offset(s*.64f,s*.70f))
                    drawCircle(accent,s*.026f,Offset(s*.64f,s*.70f))
                }
                else -> {
                    drawArc(accent.copy(alpha=.82f),205f,130f,false,Offset(s*.31f,s*.16f),Size(s*.38f,s*.22f),style=Stroke(s*.020f))
                    repeat(5){i->val a=(-.5f+i*.25f)*PI.toFloat();drawLine(accent.copy(alpha=.72f),Offset(s*.5f+cos(a)*s*.17f,s*.27f+sin(a)*s*.07f),Offset(s*.5f+cos(a)*s*.25f,s*.20f+sin(a)*s*.10f),s*.012f)}
                    drawCircle(secondary.copy(alpha=.18f),s*.082f,Offset(s*.5f,s*.69f))
                    drawCircle(Color.White.copy(alpha=.86f),s*.020f,Offset(s*.5f,s*.69f))
                    drawCircle(accent.copy(alpha=.55f),s*.055f,Offset(s*.5f,s*.69f),style=Stroke(s*.012f))
                }
            }
        }
    }
}
