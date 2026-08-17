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
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun EndgameBusinessSprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val motion = rememberInfiniteTransition(label = "endgameBusiness$id")
    val phase by motion.animateFloat(0f, 1f, infiniteRepeatable(tween(7600 + (id-10)*540, easing = LinearEasing)), label = "phase")
    val accent = when (id) {
        10 -> Color(0xFF67E8FF)
        11 -> Color(0xFFC692FF)
        12 -> Color(0xFFFF72D5)
        else -> Color(0xFFFFE27C)
    }
    val stage = when {
        level >= 1000 -> 5
        level >= 500 -> 4
        level >= 250 -> 3
        level >= 100 -> 2
        level >= 25 -> 1
        else -> 0
    }

    Box(modifier.size(iconSize).background(
        Brush.radialGradient(listOf(accent.copy(alpha=.22f), EmpireColors.SurfaceHigh, EmpireColors.Void)),
        RoundedCornerShape(iconSize * .30f)
    )) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val c = Offset(s*.5f,s*.5f)
            drawCircle(accent.copy(alpha=.12f + stage*.025f),s*.46f,c)
            drawCircle(accent.copy(alpha=.52f),s*.39f,c,style=Stroke(s*.015f))
            repeat(stage.coerceAtLeast(1)) { ring ->
                val r = s*(.31f+ring*.035f)
                drawArc(accent.copy(alpha=.24f),phase*360f*(if(ring%2==0)1 else -1)+ring*28f,210f,false,Offset(c.x-r,c.y-r),Size(r*2,r*2),style=Stroke(s*.009f))
            }
            when (id) {
                10 -> { // Intergalactic Gateway
                    repeat(3){r->drawCircle(if(r==1)Color.White.copy(alpha=.55f) else accent.copy(alpha=.78f-r*.16f),s*(.13f+r*.07f),c,style=Stroke(s*(.028f-r*.005f)))}
                    repeat(6){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/3f;val p=Offset(c.x+cos(a)*s*.27f,c.y+sin(a)*s*.27f);drawCircle(Color.White,s*.018f,p);drawLine(accent.copy(alpha=.55f),c,p,s*.008f)}
                }
                11 -> { // Cosmic Foundry
                    val core=Path().apply{moveTo(s*.50f,s*.22f);lineTo(s*.70f,s*.37f);lineTo(s*.64f,s*.67f);lineTo(s*.50f,s*.78f);lineTo(s*.36f,s*.67f);lineTo(s*.30f,s*.37f);close()}
                    drawPath(core,Brush.radialGradient(listOf(Color.White.copy(alpha=.75f),accent.copy(alpha=.65f),EmpireArtPalette.Steel),c,s*.30f))
                    drawPath(core,accent,style=Stroke(s*.020f))
                    repeat(4){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/2f;drawLine(accent.copy(alpha=.65f),Offset(c.x+cos(a)*s*.22f,c.y+sin(a)*s*.22f),Offset(c.x+cos(a)*s*.34f,c.y+sin(a)*s*.34f),s*.018f)}
                }
                12 -> { // Reality Engine
                    repeat(3){ring->val rx=s*(.16f+ring*.07f);val ry=rx*(.48f+ring*.08f);drawArc(accent.copy(alpha=.78f-ring*.15f),phase*360f*(if(ring%2==0)1 else -1)+ring*55f,245f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(s*(.026f-ring*.004f)))}
                    drawCircle(Color.White,s*.036f,c)
                    repeat(8){i->val a=i*PI.toFloat()/4f+phase*PI.toFloat();drawCircle(if(i%2==0)EmpireArtPalette.Cyan else accent,s*.014f,Offset(c.x+cos(a)*s*.29f,c.y+sin(a)*s*.17f))}
                }
                else -> { // Transcendent Nexus
                    drawCircle(Brush.radialGradient(listOf(Color.White,accent.copy(alpha=.65f),Color.Transparent),c,s*.19f),s*.19f,c)
                    repeat(7){i->val a=-PI.toFloat()/2f+(i-3)*.22f;drawLine(accent.copy(alpha=.72f),Offset(c.x+cos(a)*s*.17f,c.y+sin(a)*s*.17f),Offset(c.x+cos(a)*s*(.30f+(i%2)*.07f),c.y+sin(a)*s*(.30f+(i%2)*.07f)),s*.016f)}
                    drawCircle(Color.White.copy(alpha=.38f),s*.33f,c,style=Stroke(s*.008f))
                }
            }
            if(stage>=4) drawCircle(Color.White.copy(alpha=.20f),s*.47f,c,style=Stroke(s*.008f))
        }
    }
}
