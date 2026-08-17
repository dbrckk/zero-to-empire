package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp

@Composable
fun BusinessGroup02Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val stage = when { level >= 1000 -> 5; level >= 500 -> 4; level >= 250 -> 3; level >= 100 -> 2; level >= 25 -> 1; else -> 0 }
    if (stage == 0) return
    val accent = when (id) { 4 -> Color(0xFF8C7CFF); 5 -> Color(0xFFB861FF); 6 -> Color(0xFF9FE8FF); else -> Color(0xFFFF6C5F) }
    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        when (id) {
            4 -> {
                if (stage >= 1) { drawRect(accent.copy(.38f), Offset(s*.14f,s*.46f), Size(s*.10f,s*.24f)); drawRect(accent.copy(.38f), Offset(s*.76f,s*.46f), Size(s*.10f,s*.24f)) }
                if (stage >= 2) drawCircle(Color(0xFF6EEAFF).copy(.55f), s*.19f, Offset(s*.5f,s*.50f), style = Stroke(s*.010f))
                if (stage >= 3) repeat(4){i->drawLine(accent.copy(.55f),Offset(s*(.28f+i*.15f),s*.30f),Offset(s*(.28f+i*.15f),s*.18f),s*.010f)}
                if (stage >= 4) drawArc(Color.White.copy(.55f), 195f, 150f, false, Offset(s*.10f,s*.10f), Size(s*.80f,s*.80f), style=Stroke(s*.014f))
                if (stage >= 5) drawCircle(Color(0xFFFFE79B).copy(.18f), s*.40f, Offset(s*.5f,s*.5f))
            }
            5 -> {
                if (stage >= 1) repeat(2){i->drawRect(accent.copy(.35f),Offset(s*(if(i==0).10f else .82f),s*.47f),Size(s*.08f,s*.27f))}
                if (stage >= 2) drawLine(Color(0xFF59E8FF).copy(.70f),Offset(s*.14f,s*.74f),Offset(s*.86f,s*.74f),s*.014f)
                if (stage >= 3) repeat(3){i->drawCircle(Color(0xFF59E8FF).copy(.45f),s*.045f,Offset(s*(.30f+i*.20f),s*.24f))}
                if (stage >= 4) drawArc(accent.copy(.55f),185f,170f,false,Offset(s*.08f,s*.10f),Size(s*.84f,s*.72f),style=Stroke(s*.012f))
                if (stage >= 5) drawCircle(accent.copy(.16f),s*.42f,Offset(s*.5f,s*.50f))
            }
            6 -> {
                if(stage>=1){drawCircle(accent.copy(.32f),s*.095f,Offset(s*.18f,s*.58f));drawCircle(accent.copy(.32f),s*.095f,Offset(s*.82f,s*.58f))}
                if(stage>=2) drawLine(Color.White.copy(.50f),Offset(s*.16f,s*.67f),Offset(s*.84f,s*.67f),s*.012f)
                if(stage>=3) repeat(3){i->drawCircle(accent.copy(.55f),s*.016f,Offset(s*(.32f+i*.18f),s*.29f))}
                if(stage>=4) drawArc(accent.copy(.65f),200f,145f,false,Offset(s*.10f,s*.12f),Size(s*.80f,s*.72f),style=Stroke(s*.014f))
                if(stage>=5) drawCircle(Color.White.copy(.13f),s*.40f,Offset(s*.5f,s*.52f))
            }
            7 -> {
                if(stage>=1){drawRect(accent.copy(.40f),Offset(s*.12f,s*.48f),Size(s*.10f,s*.22f));drawRect(accent.copy(.40f),Offset(s*.78f,s*.48f),Size(s*.10f,s*.22f))}
                if(stage>=2) drawLine(Color(0xFFFFC85A).copy(.75f),Offset(s*.15f,s*.74f),Offset(s*.85f,s*.74f),s*.014f)
                if(stage>=3) repeat(4){i->drawCircle(accent.copy(.65f),s*.013f,Offset(s*(.29f+i*.14f),s*.30f))}
                if(stage>=4) drawArc(Color(0xFFFFC85A).copy(.60f),200f,150f,false,Offset(s*.09f,s*.10f),Size(s*.82f,s*.80f),style=Stroke(s*.014f))
                if(stage>=5) drawCircle(Color(0xFFFFC85A).copy(.14f),s*.42f,Offset(s*.5f,s*.50f))
            }
        }
    }
}
