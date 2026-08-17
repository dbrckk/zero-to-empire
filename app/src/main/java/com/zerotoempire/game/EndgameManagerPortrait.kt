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

@Composable
fun EndgameManagerPortrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val transition = rememberInfiniteTransition(label = "endgameManager$businessId")
    val animated by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 15000 else 9000, easing = LinearEasing)), label = "phase")
    val phase = if (reduced) .31f else animated
    val accent = when (businessId) {
        10 -> Color(0xFF67E8FF)
        11 -> Color(0xFFC692FF)
        12 -> Color(0xFFFF72D5)
        else -> Color(0xFFFFE27C)
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
            drawCircle(accent.copy(alpha=.12f),s*.47f,center)
            drawCircle(accent.copy(alpha=.58f),s*.425f,center,style=Stroke(s*.017f))
            drawCircle(Color.White.copy(alpha=.13f),s*.455f,center,style=Stroke(s*.007f))

            repeat(if(lowPower) 2 else 4) { i ->
                val count = if(lowPower) 2 else 4
                val a = phase * 2f * PI.toFloat() + i * 2f * PI.toFloat() / count
                drawCircle(accent.copy(alpha=.7f),s*.012f,Offset(center.x+cos(a)*s*.39f,center.y+sin(a)*s*.39f))
            }

            drawCircle(skin,s*.165f,Offset(s*.5f,s*.375f))
            drawArc(hair,190f,160f,true,Offset(s*.325f,s*.18f),Size(s*.35f,s*.30f))
            drawCircle(EmpireArtPalette.Ink,s*.014f,Offset(s*.445f,s*.375f))
            drawCircle(EmpireArtPalette.Ink,s*.014f,Offset(s*.555f,s*.375f))
            drawLine(accent.copy(alpha=.8f),Offset(s*.445f,s*.47f),Offset(s*.555f,s*.47f),s*.014f)

            val torso = Path().apply {
                moveTo(s*.21f,s*.84f)
                quadraticTo(s*.27f,s*.58f,s*.5f,s*.57f)
                quadraticTo(s*.73f,s*.58f,s*.79f,s*.84f)
                close()
            }
            drawPath(torso,Color(0xFF1A2940))
            drawPath(torso,accent.copy(alpha=.8f),style=Stroke(s*.022f))
            drawLine(Color.White.copy(alpha=.25f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.80f),s*.010f)

            when (businessId) {
                10 -> {
                    drawArc(accent,195f,150f,false,Offset(s*.355f,s*.295f),Size(s*.29f,s*.16f),style=Stroke(s*.024f))
                    drawCircle(Color.White.copy(alpha=.7f),s*.012f,Offset(s*.61f,s*.34f))
                    drawArc(accent.copy(alpha=.65f),205f,125f,false,Offset(s*.28f,s*.61f),Size(s*.44f,s*.18f),style=Stroke(s*.015f))
                    repeat(3){i->drawCircle(Color.White.copy(alpha=.65f),s*.010f,Offset(s*(.35f+i*.13f),s*.70f))}
                }
                11 -> {
                    repeat(3){i->val x=s*(.40f+i*.10f);drawLine(accent,Offset(x,s*.205f),Offset(x+s*(i-1)*.025f,s*.14f),s*.016f)}
                    drawRoundRect(accent.copy(alpha=.32f),Offset(s*.39f,s*.66f),Size(s*.22f,s*.10f),style=Stroke(s*.018f))
                    drawCircle(Color.White.copy(alpha=.75f),s*.022f,Offset(s*.5f,s*.71f))
                }
                12 -> {
                    drawArc(accent,165f,205f,false,Offset(s*.34f,s*.285f),Size(s*.32f,s*.19f),style=Stroke(s*.022f))
                    drawLine(accent.copy(alpha=.7f),Offset(s*.31f,s*.64f),Offset(s*.69f,s*.79f),s*.016f)
                    drawLine(Color.White.copy(alpha=.28f),Offset(s*.33f,s*.77f),Offset(s*.67f,s*.64f),s*.010f)
                    drawCircle(accent,s*.026f,Offset(s*.64f,s*.70f))
                }
                else -> {
                    drawArc(accent.copy(alpha=.82f),205f,130f,false,Offset(s*.31f,s*.16f),Size(s*.38f,s*.22f),style=Stroke(s*.020f))
                    repeat(5){i->val a=(-.5f+i*.25f)*PI.toFloat();drawLine(accent.copy(alpha=.72f),Offset(s*.5f+cos(a)*s*.17f,s*.27f+sin(a)*s*.07f),Offset(s*.5f+cos(a)*s*.25f,s*.20f+sin(a)*s*.10f),s*.012f)}
                    drawCircle(Color.White.copy(alpha=.8f),s*.020f,Offset(s*.5f,s*.69f))
                    drawCircle(accent.copy(alpha=.45f),s*.055f,Offset(s*.5f,s*.69f),style=Stroke(s*.012f))
                }
            }
        }
    }
}
