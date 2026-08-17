package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

enum class MetaSpriteKind { CASH, GEM, LEGACY, DAILY, MISSION, ACHIEVEMENT, BOOST, EVENT, LOCK, STORE, SHARE }

@Composable
fun MetaSprite(kind: MetaSpriteKind, size: Dp = 42.dp, active: Boolean = true, progress: Float = 1f) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val t = rememberInfiniteTransition(label = "meta-$kind")
    val phaseAnim by t.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 12000 else 7000, easing = LinearEasing)), label = "phase")
    val phase = if (reduced) .18f else phaseAnim
    val accent = when (kind) {
        MetaSpriteKind.CASH -> Color(0xFF6EEB8B)
        MetaSpriteKind.GEM -> Color(0xFFC68BFF)
        MetaSpriteKind.LEGACY -> Color(0xFFFFD66B)
        MetaSpriteKind.DAILY -> Color(0xFFFFC857)
        MetaSpriteKind.MISSION -> Color(0xFF57E7F2)
        MetaSpriteKind.ACHIEVEMENT -> Color(0xFFFFE36E)
        MetaSpriteKind.BOOST -> Color(0xFFFF8C5A)
        MetaSpriteKind.EVENT -> Color(0xFFFF68D8)
        MetaSpriteKind.LOCK -> Color(0xFF7C8799)
        MetaSpriteKind.STORE -> Color(0xFF62B4FF)
        MetaSpriteKind.SHARE -> Color(0xFF8BE0FF)
    }
    Canvas(Modifier.size(size)) {
        val s = this.size.minDimension
        val c = Offset(s * .5f, s * .5f)
        val alpha = if (active) 1f else .45f
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha = .24f * alpha), Color.Transparent), c, s * .5f), s * .5f, c)
        drawCircle(EmpireColors.SurfaceHigh.copy(alpha = .96f), s * .39f, c)
        drawCircle(accent.copy(alpha = .80f * alpha), s * .39f, c, style = Stroke(s * .035f))
        drawMetaGlyph(kind, c, s, accent.copy(alpha = alpha), progress.coerceIn(0f, 1f))
        if (active && kind !in setOf(MetaSpriteKind.LOCK, MetaSpriteKind.CASH)) {
            val count = if (lowPower) 2 else 4
            repeat(count) { i ->
                val a = phase * 2f * PI.toFloat() + i * 2f * PI.toFloat() / count
                drawCircle(Color.White.copy(alpha = .72f), s * .018f, Offset(c.x + cos(a) * s * .44f, c.y + sin(a) * s * .44f))
            }
        }
    }
}

private fun DrawScope.drawMetaGlyph(kind: MetaSpriteKind, c: Offset, s: Float, accent: Color, progress: Float) {
    when (kind) {
        MetaSpriteKind.CASH -> {
            drawRoundRect(accent.copy(alpha=.22f), Offset(s*.28f,s*.34f), Size(s*.44f,s*.31f))
            drawRoundRect(accent, Offset(s*.28f,s*.34f), Size(s*.44f,s*.31f), style=Stroke(s*.025f))
            drawCircle(accent,s*.055f,c)
            drawLine(Color.White,Offset(s*.47f,s*.43f),Offset(s*.54f,s*.43f),s*.018f)
            drawLine(Color.White,Offset(s*.46f,s*.57f),Offset(s*.53f,s*.57f),s*.018f)
        }
        MetaSpriteKind.GEM -> {
            val p=Path().apply{moveTo(c.x,s*.24f);lineTo(s*.72f,s*.42f);lineTo(s*.62f,s*.72f);lineTo(s*.38f,s*.72f);lineTo(s*.28f,s*.42f);close()}
            drawPath(p,Brush.verticalGradient(listOf(Color.White,accent,accent.copy(alpha=.45f))))
            drawLine(Color.White.copy(alpha=.7f),Offset(c.x,s*.25f),Offset(c.x,s*.69f),s*.014f)
            drawLine(Color.White.copy(alpha=.45f),Offset(s*.29f,s*.42f),Offset(s*.71f,s*.42f),s*.012f)
        }
        MetaSpriteKind.LEGACY -> {
            drawCircle(accent.copy(alpha=.22f),s*.22f,c)
            drawCircle(accent,s*.20f,c,style=Stroke(s*.032f))
            repeat(6){i->val a=i*PI.toFloat()/3f;drawLine(Offset(c.x+cos(a)*s*.11f,c.y+sin(a)*s*.11f),Offset(c.x+cos(a)*s*.27f,c.y+sin(a)*s*.27f),s*.026f,accent)}
            drawCircle(Color.White,s*.055f,c)
        }
        MetaSpriteKind.DAILY -> {
            drawRoundRect(accent.copy(alpha=.16f),Offset(s*.28f,s*.28f),Size(s*.44f,s*.44f))
            drawRoundRect(accent,Offset(s*.28f,s*.28f),Size(s*.44f,s*.44f),style=Stroke(s*.025f))
            drawLine(accent,Offset(s*.28f,s*.40f),Offset(s*.72f,s*.40f),s*.02f)
            drawCircle(Color.White,s*.06f,Offset(c.x,s*.56f))
        }
        MetaSpriteKind.MISSION -> {
            val p=Path().apply{moveTo(s*.30f,s*.66f);lineTo(s*.30f,s*.31f);lineTo(s*.68f,s*.31f);lineTo(s*.68f,s*.66f);close()}
            drawPath(p,accent.copy(alpha=.18f));drawPath(p,accent,style=Stroke(s*.024f))
            drawLine(accent,Offset(s*.37f,s*.43f),Offset(s*.61f,s*.43f),s*.017f)
            drawLine(accent,Offset(s*.37f,s*.53f),Offset(s*(.37f+.24f*progress),s*.53f),s*.017f)
        }
        MetaSpriteKind.ACHIEVEMENT -> {
            val star=Path().apply{for(i in 0 until 10){val a=-PI/2+i*PI/5;val r=if(i%2==0)s*.24 else s*.105;val x=c.x+(cos(a)*r).toFloat();val y=c.y+(sin(a)*r).toFloat();if(i==0)moveTo(x,y)else lineTo(x,y)};close()}
            drawPath(star,Brush.radialGradient(listOf(Color.White,accent),c,s*.28f))
        }
        MetaSpriteKind.BOOST -> {
            val bolt=Path().apply{moveTo(s*.53f,s*.22f);lineTo(s*.34f,s*.51f);lineTo(s*.48f,s*.51f);lineTo(s*.41f,s*.78f);lineTo(s*.68f,s*.43f);lineTo(s*.54f,s*.43f);close()}
            drawPath(bolt,accent);drawPath(bolt,Color.White.copy(alpha=.5f),style=Stroke(s*.012f))
        }
        MetaSpriteKind.EVENT -> {
            drawCircle(accent.copy(alpha=.18f),s*.23f,c)
            repeat(8){i->val a=i*PI.toFloat()/4f;drawLine(Offset(c.x+cos(a)*s*.14f,c.y+sin(a)*s*.14f),Offset(c.x+cos(a)*s*.29f,c.y+sin(a)*s*.29f),s*.018f,accent)}
            drawCircle(Color.White,s*.055f,c)
        }
        MetaSpriteKind.LOCK -> {
            drawRoundRect(accent.copy(alpha=.20f),Offset(s*.31f,s*.43f),Size(s*.38f,s*.31f))
            drawRoundRect(accent,Offset(s*.31f,s*.43f),Size(s*.38f,s*.31f),style=Stroke(s*.025f))
            drawArc(accent,195f,150f,false,Offset(s*.37f,s*.25f),Size(s*.26f,s*.30f),style=Stroke(s*.035f))
            drawCircle(Color.White.copy(alpha=.8f),s*.028f,Offset(c.x,s*.58f))
        }
        MetaSpriteKind.STORE -> {
            drawRoundRect(accent.copy(alpha=.18f),Offset(s*.27f,s*.38f),Size(s*.46f,s*.34f))
            drawRoundRect(accent,Offset(s*.27f,s*.38f),Size(s*.46f,s*.34f),style=Stroke(s*.025f))
            drawArc(accent,200f,140f,false,Offset(s*.37f,s*.25f),Size(s*.26f,s*.27f),style=Stroke(s*.025f))
            drawCircle(Color.White,s*.035f,Offset(c.x,s*.55f))
        }
        MetaSpriteKind.SHARE -> {
            val pts=listOf(Offset(s*.34f,s*.50f),Offset(s*.64f,s*.32f),Offset(s*.64f,s*.68f))
            drawLine(accent,pts[0],pts[1],s*.023f);drawLine(accent,pts[0],pts[2],s*.023f)
            pts.forEach{drawCircle(accent,s*.065f,it);drawCircle(Color.White.copy(alpha=.75f),s*.024f,it)}
        }
    }
}

@Composable
fun NavSprite(tab: GameTab, selected: Boolean, size: Dp = 26.dp) {
    val kind = when (tab) {
        GameTab.EMPIRE -> MetaSpriteKind.LEGACY
        GameTab.MANAGERS -> MetaSpriteKind.MISSION
        GameTab.UPGRADES -> MetaSpriteKind.GEM
        GameTab.GOALS -> MetaSpriteKind.ACHIEVEMENT
    }
    MetaSprite(kind, size, active = selected)
}
