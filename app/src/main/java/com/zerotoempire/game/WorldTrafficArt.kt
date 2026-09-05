package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize

/** Reviewed FLUX static assets used as physical scenery in the city stage. */
private val worldTrafficSprites = intArrayOf(
    R.drawable.zte_vehicle_00_final, R.drawable.zte_vehicle_01_final,
    R.drawable.zte_vehicle_02_final, R.drawable.zte_vehicle_03_final,
    R.drawable.zte_vehicle_04_final, R.drawable.zte_vehicle_05_final,
    R.drawable.zte_vehicle_06_final, R.drawable.zte_vehicle_07_final,
    R.drawable.zte_vehicle_08_final, R.drawable.zte_vehicle_10_final,
)

private val worldPropSprites = intArrayOf(
    R.drawable.zte_prop_02_b_final, R.drawable.zte_prop_04_a_final,
    R.drawable.zte_prop_05_b_final, R.drawable.zte_prop_06_a_final,
    R.drawable.zte_prop_06_b_final, R.drawable.zte_prop_07_a_final,
    R.drawable.zte_prop_07_b_final, R.drawable.zte_prop_08_a_final,
    R.drawable.zte_prop_08_b_final, R.drawable.zte_prop_09_a_final,
    R.drawable.zte_prop_09_b_final, R.drawable.zte_prop_10_a_final,
    R.drawable.zte_prop_10_b_final, R.drawable.zte_prop_11_a_final,
    R.drawable.zte_prop_11_b_final, R.drawable.zte_prop_12_a_final,
    R.drawable.zte_prop_12_b_final, R.drawable.zte_prop_13_a_final,
)

@Composable
internal fun ReviewedWorldTraffic(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val vehicles = remember { worldTrafficSprites.map { ImageBitmap.imageResource(context.resources, it) } }
    val props = remember { worldPropSprites.map { ImageBitmap.imageResource(context.resources, it) } }
    Box(modifier) {
        Canvas(Modifier.fillMaxSize()) {
            val vehiclePlacements = listOf(
                Triple(.45f,.37f,.090f), Triple(.54f,.43f,.105f), Triple(.43f,.50f,.112f),
                Triple(.58f,.58f,.125f), Triple(.39f,.66f,.132f), Triple(.63f,.73f,.145f),
                Triple(.34f,.79f,.090f), Triple(.69f,.84f,.150f), Triple(.46f,.89f,.158f),
                Triple(.57f,.94f,.090f),
            )
            vehiclePlacements.forEachIndexed { i, (x,y,w) -> drawSprite(vehicles[i], x,y,w,.72f,true) }

            // Props stay off the cargo avenue and scale with depth. They provide machinery,
            // utility and district detail without becoming UI decoration.
            val propPlacements = listOf(
                Triple(.12f,.38f,.085f), Triple(.83f,.40f,.080f), Triple(.16f,.48f,.095f),
                Triple(.82f,.51f,.100f), Triple(.13f,.59f,.110f), Triple(.86f,.61f,.105f),
                Triple(.18f,.69f,.120f), Triple(.82f,.71f,.125f), Triple(.12f,.78f,.130f),
                Triple(.88f,.80f,.130f), Triple(.20f,.86f,.140f), Triple(.80f,.87f,.145f),
                Triple(.10f,.91f,.135f), Triple(.90f,.92f,.135f), Triple(.25f,.94f,.125f),
                Triple(.75f,.95f,.125f), Triple(.31f,.84f,.105f), Triple(.71f,.76f,.105f),
            )
            propPlacements.forEachIndexed { i, (x,y,w) -> drawSprite(props[i], x,y,w,.78f,false) }
        }
    }
}

private fun DrawScope.drawSprite(image: ImageBitmap, xFraction: Float, yFraction: Float, widthFraction: Float, pivot: Float, shadow: Boolean) {
    val targetWidth=(size.width*widthFraction).toInt().coerceAtLeast(1)
    val targetHeight=(targetWidth*(image.height.toFloat()/image.width.toFloat())).toInt().coerceAtLeast(1)
    val x=(size.width*xFraction-targetWidth/2f).toInt()
    val y=(size.height*yFraction-targetHeight*pivot).toInt()
    if(shadow) drawOval(Color.Black.copy(alpha=.28f),Offset(x+targetWidth*.12f,y+targetHeight*.73f),Size(targetWidth*.76f,targetHeight*.14f))
    drawImage(image=image,srcOffset=IntOffset.Zero,srcSize=IntSize(image.width,image.height),dstOffset=IntOffset(x,y),dstSize=IntSize(targetWidth,targetHeight))
}
