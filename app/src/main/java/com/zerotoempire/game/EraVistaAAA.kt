package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
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
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun EraVistaAAA(eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val transition = rememberInfiniteTransition(label = "eraVistaAAA")
    val driftAnim by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 26000 else 16000, easing = LinearEasing)), label = "drift")
    val drift = if (reduced) .22f else driftAnim
    Canvas(modifier) {
        val w=size.width; val h=size.height
        drawRect(Brush.verticalGradient(listOf(EmpireColors.DeepSpace,EmpireColors.Void)))
        drawStarfield(w,h,if(lowPower)18 else 32,drift)
        when(eraIndex.coerceIn(0,10)) {
            0 -> drawStreetEra(w,h,drift)
            1 -> drawIndustrialEra(w,h,drift)
            2 -> drawDigitalEra(w,h,drift)
            3 -> drawMegacityEra(w,h,drift)
            4 -> drawLunarEra(w,h,drift)
            5 -> drawMarsEra(w,h,drift)
            6 -> drawDysonEra(w,h,drift,lowPower)
            7 -> drawGalacticEra(w,h,drift,lowPower)
            8 -> drawIntergalacticEra(w,h,drift,lowPower)
            9 -> drawRealityEra(w,h,drift,lowPower)
            else -> drawTranscendentEra(w,h,drift,lowPower)
        }
    }
}

private fun DrawScope.drawStarfield(w:Float,h:Float,count:Int,drift:Float){repeat(count){i->val x=w*((i*37%101)/100f);val y=h*((i*61%97)/100f);val r=if(i%7==0)2.1f else 1f;drawCircle(Color.White.copy(alpha=.24f+(i%4)*.12f),r,Offset((x+w*.03f*drift*(i%3)).mod(w),y))}}
private fun DrawScope.drawStreetEra(w:Float,h:Float,d:Float){val gold=EmpireArtPalette.Gold;val base=h*.82f;drawCircle(gold.copy(alpha=.12f),h*.30f,Offset(w*.24f,h*.36f));repeat(7){i->val bw=w*.09f;val bh=h*(.18f+(i%4)*.045f);drawRoundRect(Color(0xFF182536),Offset(w*(.04f+i*.135f),base-bh),Size(bw,bh));repeat(2){j->drawCircle(gold.copy(alpha=.75f),1.8f,Offset(w*(.07f+i*.135f),base-bh*.55f+j*12f))}};drawLine(gold.copy(alpha=.45f),Offset(0f,base),Offset(w,base),2.5f)}
private fun DrawScope.drawIndustrialEra(w:Float,h:Float,d:Float){val orange=Color(0xFFFF9B55);val base=h*.84f;repeat(5){i->val x=w*(.08f+i*.19f);val bh=h*(.26f+(i%3)*.07f);drawRect(Color(0xFF222B35),Offset(x,base-bh),Size(w*.13f,bh));drawRect(orange.copy(alpha=.5f),Offset(x+w*.025f,base-bh*.72f),Size(w*.08f,h*.028f));drawRect(Color(0xFF333B45),Offset(x+w*.045f,base-bh-h*.16f),Size(w*.035f,h*.16f));drawCircle(orange.copy(alpha=.12f),h*.09f,Offset(x+w*.063f,base-bh-h*.18f-d*h*.02f))};drawLine(orange.copy(alpha=.5f),Offset(0f,base),Offset(w,base),3f)}
private fun DrawScope.drawDigitalEra(w:Float,h:Float,d:Float){val cyan=EmpireArtPalette.Cyan;repeat(9){i->val x=w*(.06f+i*.105f);val bh=h*(.20f+(i%5)*.055f);drawRect(Color(0xFF10243A),Offset(x,h*.79f-bh),Size(w*.075f,bh));drawLine(cyan.copy(alpha=.42f),Offset(x+w*.012f,h*.76f-bh),Offset(x+w*.06f,h*.76f-bh),2f)};repeat(5){i->val y=h*(.2f+i*.105f);drawLine(cyan.copy(alpha=.18f),Offset(0f,y),Offset(w,y+w*.01f*d),1f)};drawCircle(cyan.copy(alpha=.12f),h*.24f,Offset(w*(.25f+.45f*d),h*.34f))}
private fun DrawScope.drawMegacityEra(w:Float,h:Float,d:Float){val violet=EmpireArtPalette.Violet;val base=h*.84f;repeat(12){i->val x=w*(.02f+i*.082f);val bh=h*(.20f+(i*7%6)*.07f);drawRect(Color(0xFF151D31),Offset(x,base-bh),Size(w*.062f,bh));repeat(3){j->drawCircle(if((i+j)%2==0)violet else EmpireArtPalette.Cyan,1.5f,Offset(x+w*.031f,base-bh+h*(.05f+j*.065f)))}};drawArc(violet.copy(alpha=.42f),190f,160f,false,Offset(w*.17f,h*.18f),Size(w*.66f,h*.54f),style=Stroke(3f))}
private fun DrawScope.drawLunarEra(w:Float,h:Float,d:Float){val cyan=Color(0xFFEAF6FF);drawCircle(Color(0xFFB9C8D7),h*.23f,Offset(w*.73f,h*.36f));drawCircle(Color(0xFF8C99A8),h*.045f,Offset(w*.68f,h*.30f));val base=h*.82f;drawArc(cyan.copy(alpha=.55f),180f,180f,false,Offset(w*.10f,h*.46f),Size(w*.35f,h*.31f),style=Stroke(3f));repeat(5){i->drawLine(Color(0xFF9FB0C0),Offset(w*(.16f+i*.055f),h*.62f),Offset(w*(.16f+i*.055f),base),2f)};drawLine(cyan.copy(alpha=.5f),Offset(0f,base),Offset(w,base),2f)}
private fun DrawScope.drawMarsEra(w:Float,h:Float,d:Float){val red=EmpireArtPalette.Red;drawCircle(Color(0xFFB34235),h*.24f,Offset(w*.76f,h*.37f));drawCircle(Color(0xFF7A2E28),h*.05f,Offset(w*.68f,h*.32f));val base=h*.83f;repeat(4){i->val x=w*(.10f+i*.19f);drawRoundRect(Color(0xFF3B2929),Offset(x,h*.57f),Size(w*.13f,h*.18f));drawArc(red,180f,180f,false,Offset(x-w*.01f,h*.48f),Size(w*.15f,h*.18f),style=Stroke(3f));drawCircle(red.copy(alpha=.7f),2f,Offset(x+w*.065f,h*.64f))};drawLine(red.copy(alpha=.4f),Offset(0f,base),Offset(w,base),3f)}
private fun DrawScope.drawDysonEra(w:Float,h:Float,d:Float,low:Boolean){val gold=EmpireArtPalette.GoldHot;val c=Offset(w*.5f,h*.45f);drawCircle(Brush.radialGradient(listOf(Color.White,gold,Color.Transparent),c,h*.22f),h*.22f,c);repeat(if(low)3 else 5){r->drawCircle(gold.copy(alpha=.68f-r*.1f),h*(.24f+r*.035f),c,style=Stroke(2.5f))};repeat(if(low)6 else 12){i->val a=d*2f*PI.toFloat()+i*2f*PI.toFloat()/(if(low)6 else 12);drawCircle(Color.White,2.2f,Offset(c.x+cos(a)*w*.32f,c.y+sin(a)*h*.25f))}}
private fun DrawScope.drawGalacticEra(w:Float,h:Float,d:Float,low:Boolean){val violet=EmpireArtPalette.Violet;val c=Offset(w*.5f,h*.46f);repeat(if(low)3 else 6){i->drawArc(violet.copy(alpha=.18f+i*.07f),d*360f+i*35f,210f,false,Offset(c.x-w*(.15f+i*.035f),c.y-h*(.10f+i*.025f)),Size(w*(.30f+i*.07f),h*(.20f+i*.05f)),style=Stroke(2f))};drawCircle(Color.White,h*.045f,c);repeat(if(low)4 else 9){i->val a=i*2f*PI.toFloat()/(if(low)4 else 9)-d;drawCircle(if(i%2==0)EmpireArtPalette.Cyan else violet,2.4f,Offset(c.x+cos(a)*w*.37f,c.y+sin(a)*h*.27f))}}
private fun DrawScope.drawIntergalacticEra(w:Float,h:Float,d:Float,low:Boolean){val cyan=EmpireArtPalette.Cyan;val mag=EmpireArtPalette.Magenta;val c=Offset(w*.5f,h*.45f);drawCircle(cyan.copy(alpha=.10f),h*.27f,c);drawCircle(cyan,h*.20f,c,style=Stroke(3.5f));drawCircle(mag,h*.13f,c,style=Stroke(2.5f));repeat(if(low)4 else 8){i->val a=d*2f*PI.toFloat()+i*PI.toFloat()/4f;drawLine(Offset(c.x+cos(a)*w*.12f,c.y+sin(a)*h*.09f),Offset(c.x+cos(a)*w*.32f,c.y+sin(a)*h*.25f),2f,if(i%2==0)cyan else mag)};drawCircle(Color.White,h*.045f,c)}
private fun DrawScope.drawRealityEra(w:Float,h:Float,d:Float,low:Boolean){val pink=Color(0xFFFF68D8);val cyan=Color(0xFF6EEBFF);val c=Offset(w*.5f,h*.45f);repeat(4){r->val rx=w*(.12f+r*.06f);val ry=h*(.08f+r*.035f);drawArc(if(r%2==0)pink else cyan,d*360f*(if(r%2==0)1 else -1)+r*45f,255f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(3f-r*.3f))};drawCircle(Color.White,h*.055f,c);val p=Path().apply{moveTo(c.x,h*.12f);lineTo(w*.78f,c.y);lineTo(c.x,h*.78f);lineTo(w*.22f,c.y);close()};drawPath(p,pink.copy(alpha=.24f),style=Stroke(2f))}
private fun DrawScope.drawTranscendentEra(w:Float,h:Float,d:Float,low:Boolean){val gold=Color(0xFFFFE36E);val violet=Color(0xFFC68BFF);val c=Offset(w*.5f,h*.45f);drawCircle(Brush.radialGradient(listOf(Color.White,gold.copy(alpha=.9f),violet.copy(alpha=.25f),Color.Transparent),c,h*.26f),h*.26f,c);repeat(3){r->drawCircle(if(r%2==0)gold else violet,h*(.15f+r*.07f),c,style=Stroke(3f-r*.45f))};repeat(if(low)6 else 12){i->val a=d*2f*PI.toFloat()+i*2f*PI.toFloat()/(if(low)6 else 12);drawLine(Offset(c.x+cos(a)*w*.11f,c.y+sin(a)*h*.08f),Offset(c.x+cos(a)*w*.34f,c.y+sin(a)*h*.27f),2.4f,if(i%2==0)gold else violet)};drawCircle(Color.White,h*.05f,c)}
