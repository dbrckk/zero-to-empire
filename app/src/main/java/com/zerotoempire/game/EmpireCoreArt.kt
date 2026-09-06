package com.zerotoempire.game

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/**
 * Tier-aware production Power Core renderer.
 *
 * The seven reviewed FLUX masters are the canonical visual progression. Higher
 * world eras intentionally retain the T6 Singularity Crown instead of falling
 * back to procedural placeholder geometry.
 */
@Composable
fun EmpireCoreGlyph(modifier: Modifier = Modifier, eraIndex: Int = 0) {
    val context = LocalContext.current
    val tier = eraIndex.coerceIn(0, 6)
    val coreRes = remember(tier) {
        intArrayOf(
            R.drawable.zte_power_core_t0_final,
            R.drawable.zte_power_core_t1_final,
            R.drawable.zte_power_core_t2_final,
            R.drawable.zte_power_core_t3_final,
            R.drawable.zte_power_core_t4_final,
            R.drawable.zte_power_core_t5_final,
            R.drawable.zte_power_core_t6_final,
        )[tier]
    }
    val core = remember(coreRes) { ImageBitmap.imageResource(context.resources, coreRes) }
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)

    val pulse: Float
    if (reducedMotion || lowPower) {
        pulse = 1f
    } else {
        val infinite = rememberInfiniteTransition(label = "empireCoreRaster")
        val animatedPulse by infinite.animateFloat(
            initialValue = .94f,
            targetValue = 1f,
            animationSpec = infiniteRepeatable(
                animation = tween(1250, easing = FastOutSlowInEasing),
                repeatMode = RepeatMode.Reverse,
            ),
            label = "coreRasterPulse",
        )
        pulse = animatedPulse
    }

    Canvas(modifier) {
        val side = minOf(size.width, size.height) * pulse
        val left = (size.width - side) / 2f
        val top = (size.height - side) / 2f
        val accent = coreAccent(tier)
        drawCircle(
            brush = Brush.radialGradient(
                listOf(accent.copy(alpha = .20f), accent.copy(alpha = .06f), Color.Transparent),
                center = center,
                radius = size.minDimension * .50f,
            ),
            radius = size.minDimension * .50f,
            center = center,
        )
        drawImage(
            image = core,
            srcOffset = IntOffset.Zero,
            srcSize = IntSize(core.width, core.height),
            dstOffset = IntOffset(left.toInt(), top.toInt()),
            dstSize = IntSize(side.toInt().coerceAtLeast(1), side.toInt().coerceAtLeast(1)),
        )
    }
}

private fun coreAccent(era:Int)=when(era){
    0,1->Color(0xFFFFC857);2->Color(0xFF62E8FF);3->Color(0xFF7ED8FF);4->Color(0xFFFF765F);5->Color(0xFFFFD95A);6->Color(0xFF7ADFFF);7->Color(0xFFA685FF);8->Color(0xFFD58CFF);9->Color(0xFFFF66D8);else->Color(0xFFFFE477)}
private fun coreSecondary(era:Int)=when(era){
    0,1->Color(0xFF6EEBFF);2,3->Color(0xFFA38BFF);4->Color(0xFFFFC068);5->Color(0xFFFFF2B0);6->Color(0xFF766BFF);7,8->Color(0xFF60E9FF);9->Color(0xFF8E7CFF);else->Color(0xFFC68BFF)}

private fun DrawScope.drawCoreDepthField(
    c: Offset,
    s: Float,
    rotation: Float,
    fast: Float,
    pulse: Float,
    lowPower: Boolean,
    accent: Color,
    secondary: Color
) {
    drawCircle(
        Brush.radialGradient(
            listOf(Color.Transparent, accent.copy(alpha = .055f * pulse), secondary.copy(alpha = .035f), Color.Transparent),
            c,
            s * .44f
        ),
        s * .44f,
        c
    )

    val orbitCount = if (lowPower) 2 else 3
    repeat(orbitCount) { orbit ->
        val rx = s * (.29f + orbit * .052f)
        val ry = s * (.12f + orbit * .027f)
        val direction = if (orbit % 2 == 0) 1f else -1f
        val phase = rotation * direction + orbit * 61f
        val orbitColor = if (orbit % 2 == 0) accent else secondary
        drawArc(
            orbitColor.copy(alpha = .16f + orbit * .035f),
            phase,
            205f,
            false,
            Offset(c.x - rx, c.y - ry),
            Size(rx * 2f, ry * 2f),
            style = Stroke(s * (.007f + orbit * .0015f))
        )
        drawArc(
            Color.White.copy(alpha = .075f * pulse),
            phase + 184f,
            72f,
            false,
            Offset(c.x - rx, c.y - ry),
            Size(rx * 2f, ry * 2f),
            style = Stroke(s * .0045f)
        )
    }

    val sheenRadius = s * .205f
    val sheenAngle = Math.toRadians((fast * .72f - 36f).toDouble())
    val sheenCenter = Offset(
        c.x + cos(sheenAngle).toFloat() * s * .035f,
        c.y + sin(sheenAngle).toFloat() * s * .025f
    )
    drawArc(
        Color.White.copy(alpha = .17f * pulse),
        -58f + fast * .16f,
        82f,
        false,
        Offset(sheenCenter.x - sheenRadius, sheenCenter.y - sheenRadius),
        Size(sheenRadius * 2f, sheenRadius * 2f),
        style = Stroke(s * .009f)
    )

    if (!lowPower) {
        repeat(6) { i ->
            val angle = Math.toRadians((fast * .55f + i * 60f).toDouble())
            val rx = s * if (i % 2 == 0) .405f else .365f
            val ry = s * if (i % 2 == 0) .145f else .19f
            val p = Offset(c.x + cos(angle).toFloat() * rx, c.y + sin(angle).toFloat() * ry)
            drawCircle(
                if (i % 2 == 0) Color.White.copy(alpha = .60f) else secondary.copy(alpha = .62f),
                s * if (i % 3 == 0) .008f else .0055f,
                p
            )
        }
    }
}

private fun DrawScope.drawCoreEraGeometry(era:Int,c:Offset,s:Float,rotation:Float,fast:Float,pulse:Float,lowPower:Boolean,accent:Color,secondary:Color){
    when {
        era<=1 -> {
            drawCircle(EmpireArtPalette.Ink,s*.16f,c)
            drawCircle(accent,s*.115f,c,style=Stroke(s*.024f))
            drawLine(accent,Offset(c.x,c.y-s*.075f),Offset(c.x,c.y+s*.075f),s*.022f)
            drawLine(accent,Offset(c.x-s*.05f,c.y-s*.05f),Offset(c.x+s*.05f,c.y-s*.05f),s*.022f)
        }
        era<=3 -> {
            drawCircle(Color(0xFF10192A),s*.15f,c)
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,Color.Transparent),c,s*.12f),s*.12f,c)
            repeat(4){i->val a=Math.toRadians((rotation+i*90f).toDouble());drawLine(accent,Offset(c.x+cos(a).toFloat()*s*.13f,c.y+sin(a).toFloat()*s*.13f),Offset(c.x+cos(a).toFloat()*s*.23f,c.y+sin(a).toFloat()*s*.23f),s*.014f)}
        }
        era<=5 -> {
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,Color(0xFFFF8B2F),Color.Transparent),c,s*.18f),s*.18f,c)
            repeat(if(lowPower)6 else 12){i->val a=Math.toRadians((fast+i*(360f/(if(lowPower)6 else 12))).toDouble());val p=Offset(c.x+cos(a).toFloat()*s*.25f,c.y+sin(a).toFloat()*s*.25f);drawCircle(accent,s*.012f,p)}
        }
        era<=7 -> {
            drawCircle(Color(0xFF0C1020),s*.145f,c)
            repeat(3){r->drawCircle(if(r%2==0)accent else secondary,s*(.12f+r*.055f),c,style=Stroke(s*(.024f-r*.004f)))}
            drawCircle(Brush.radialGradient(listOf(Color.White,secondary,Color.Transparent),c,s*.09f),s*.09f,c)
        }
        era<=9 -> {
            repeat(4){r->val rx=s*(.10f+r*.045f);val ry=rx*(.50f+r*.08f);drawArc(if(r%2==0)accent else secondary,rotation*(if(r%2==0)1f else -1f)+r*41f,250f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(s*(.023f-r*.003f)))}
            drawCircle(Color.White,s*.035f,c)
            if(era>=9){val d=Path().apply{moveTo(c.x,c.y-s*.27f);lineTo(c.x+s*.27f,c.y);lineTo(c.x,c.y+s*.27f);lineTo(c.x-s*.27f,c.y);close()};drawPath(d,accent.copy(alpha=.30f),style=Stroke(s*.008f))}
        }
        else -> {
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,secondary.copy(alpha=.55f),Color.Transparent),c,s*.20f),s*.20f*pulse,c)
            repeat(if(lowPower)6 else 12){i->val a=fast*PI.toFloat()/180f+i*2f*PI.toFloat()/(if(lowPower)6 else 12);val inner=s*.18f;val outer=s*(.30f+(i%3)*.035f);drawLine(if(i%2==0)accent else secondary,Offset(c.x+cos(a)*inner,c.y+sin(a)*inner),Offset(c.x+cos(a)*outer,c.y+sin(a)*outer),s*.011f)}
            drawCircle(Color.White.copy(alpha=.34f),s*.36f,c,style=Stroke(s*.008f))
        }
    }
}
