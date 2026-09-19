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
import kotlin.math.min

/** Semantically reviewed FLUX assets used as physical scenery in the active city stage. */
private val worldTrafficSprites = intArrayOf(
    R.drawable.zte_vehicle_00_final, R.drawable.zte_vehicle_01_final,
    R.drawable.zte_vehicle_02_final, R.drawable.zte_vehicle_03_final,
    R.drawable.zte_vehicle_04_final, R.drawable.zte_vehicle_05_final,
    R.drawable.zte_vehicle_06_final, R.drawable.zte_vehicle_07_final,
    R.drawable.zte_vehicle_08_final, R.drawable.zte_vehicle_09_final,
    R.drawable.zte_vehicle_10_final,
    R.drawable.zte_vehicle_11_final, R.drawable.zte_vehicle_12_final,
    R.drawable.zte_vehicle_13_final, R.drawable.zte_vehicle_14_final,
    R.drawable.zte_vehicle_15_final, R.drawable.zte_vehicle_16_final,
    R.drawable.zte_vehicle_17_final,
)

private val worldPropSprites = intArrayOf(
    R.drawable.zte_prop_02_b_final, R.drawable.zte_prop_04_a_final,
    R.drawable.zte_prop_05_a_final, R.drawable.zte_prop_05_b_final,
    R.drawable.zte_prop_06_a_final, R.drawable.zte_prop_06_b_final,
    R.drawable.zte_prop_07_a_final, R.drawable.zte_prop_07_b_final,
    R.drawable.zte_prop_08_a_final, R.drawable.zte_prop_08_b_final,
    R.drawable.zte_prop_09_a_final, R.drawable.zte_prop_09_b_final,
    R.drawable.zte_prop_10_a_final, R.drawable.zte_prop_10_b_final,
    R.drawable.zte_prop_11_a_final, R.drawable.zte_prop_11_b_final,
    R.drawable.zte_prop_12_a_final, R.drawable.zte_prop_12_b_final,
    R.drawable.zte_prop_13_a_final, R.drawable.zte_prop_13_b_final,
    R.drawable.zte_prop_00_a_final, R.drawable.zte_prop_00_b_final,
    R.drawable.zte_prop_01_a_final, R.drawable.zte_prop_01_b_final,
    R.drawable.zte_prop_02_a_final, R.drawable.zte_prop_03_a_final,
    R.drawable.zte_prop_03_b_final, R.drawable.zte_prop_04_b_final,
)

private data class TrafficPlacement(
    val x: Float,
    val y: Float,
    val width: Float,
    val travelX: Float,
    val travelY: Float,
    val phaseFrames: Int,
)

private val vehiclePlacements = listOf(
    TrafficPlacement(.45f,.37f,.090f, .06f,.035f, 0),
    TrafficPlacement(.54f,.43f,.105f,-.05f,.040f,17),
    TrafficPlacement(.43f,.50f,.112f, .07f,.050f,31),
    TrafficPlacement(.58f,.58f,.125f,-.08f,.055f,49),
    TrafficPlacement(.39f,.66f,.132f, .09f,.060f,68),
    TrafficPlacement(.63f,.73f,.145f,-.10f,.065f,83),
    TrafficPlacement(.34f,.79f,.090f, .08f,.055f,101),
    TrafficPlacement(.69f,.84f,.150f,-.07f,.050f,119),
    TrafficPlacement(.46f,.89f,.158f, .05f,.035f,137),
    TrafficPlacement(.57f,.94f,.090f,-.04f,.030f,151),
    TrafficPlacement(.51f,.33f,.088f, .03f,.020f,11),
    TrafficPlacement(.61f,.48f,.100f,-.04f,.025f,39),
    TrafficPlacement(.36f,.56f,.108f, .04f,.030f,57),
    TrafficPlacement(.66f,.68f,.118f,-.05f,.035f,76),
    TrafficPlacement(.49f,.81f,.126f, .05f,.035f,94),
    TrafficPlacement(.73f,.55f,.112f,-.03f,.020f,123),
    TrafficPlacement(.28f,.62f,.104f, .03f,.020f,142),
    TrafficPlacement(.78f,.63f,.110f,-.03f,.020f,158),
)

private val propPlacements = listOf(
    Triple(.12f,.38f,.085f), Triple(.83f,.40f,.080f), Triple(.17f,.43f,.088f),
    Triple(.16f,.48f,.095f), Triple(.82f,.51f,.100f), Triple(.13f,.59f,.110f),
    Triple(.86f,.61f,.105f), Triple(.18f,.69f,.120f), Triple(.82f,.71f,.125f),
    Triple(.12f,.78f,.130f), Triple(.88f,.80f,.130f), Triple(.20f,.86f,.140f),
    Triple(.80f,.87f,.145f), Triple(.10f,.91f,.135f), Triple(.90f,.92f,.135f),
    Triple(.25f,.94f,.125f), Triple(.75f,.95f,.125f), Triple(.31f,.84f,.105f),
    Triple(.71f,.76f,.105f), Triple(.91f,.68f,.110f), Triple(.08f,.47f,.078f),
    Triple(.92f,.48f,.078f), Triple(.07f,.56f,.082f), Triple(.93f,.58f,.082f),
    Triple(.09f,.66f,.088f), Triple(.91f,.74f,.090f), Triple(.14f,.73f,.086f),
    Triple(.86f,.45f,.082f),
)

@Composable
internal fun ReviewedWorldTraffic(
    worldFrame: Int,
    reducedMotion: Boolean,
    modifier: Modifier = Modifier,
) {
    val context = LocalContext.current
    val vehicles = remember { worldTrafficSprites.map { ImageBitmap.imageResource(context.resources, it) } }
    val props = remember { worldPropSprites.map { ImageBitmap.imageResource(context.resources, it) } }

    Box(modifier) {
        Canvas(Modifier.fillMaxSize()) {
            vehiclePlacements.forEachIndexed { i, placement ->
                val sample = trafficSample(
                    placement = placement,
                    worldFrame = worldFrame,
                    reducedMotion = reducedMotion,
                )
                drawSprite(
                    image = vehicles[i],
                    xFraction = sample.x,
                    yFraction = sample.y,
                    widthFraction = placement.width,
                    pivot = .72f,
                    shadow = true,
                    alpha = sample.alpha,
                )
            }

            // Props stay still: motion belongs to actors/traffic and remains visually legible.
            propPlacements.forEachIndexed { i, (x,y,w) ->
                drawSprite(props[i], x,y,w,.78f,false,1f)
            }
        }
    }
}

internal data class AmbientTrafficMotion(
    val deltaX: Float,
    val deltaY: Float,
    val alpha: Float,
)

internal fun ambientTrafficMotion(
    worldFrame: Int,
    phaseFrames: Int,
    travelX: Float,
    travelY: Float,
    reducedMotion: Boolean,
): AmbientTrafficMotion {
    if (reducedMotion || (travelX == 0f && travelY == 0f)) {
        return AmbientTrafficMotion(0f, 0f, .92f)
    }

    val cycleFrames = 180
    val normalizedFrame = Math.floorMod(worldFrame + phaseFrames, cycleFrames)
    val cycle = normalizedFrame.toFloat() / cycleFrames
    val centered = cycle - .5f
    val edgeFade = (min(cycle, 1f - cycle) * 10f).coerceIn(.25f, 1f)

    return AmbientTrafficMotion(
        deltaX = travelX * centered,
        deltaY = travelY * centered,
        alpha = .48f + edgeFade * .50f,
    )
}

private data class TrafficSample(
    val x: Float,
    val y: Float,
    val alpha: Float,
)

private fun trafficSample(
    placement: TrafficPlacement,
    worldFrame: Int,
    reducedMotion: Boolean,
): TrafficSample {
    val motion = ambientTrafficMotion(
        worldFrame = worldFrame,
        phaseFrames = placement.phaseFrames,
        travelX = placement.travelX,
        travelY = placement.travelY,
        reducedMotion = reducedMotion,
    )
    return TrafficSample(
        x = placement.x + motion.deltaX,
        y = placement.y + motion.deltaY,
        alpha = motion.alpha,
    )
}

private fun DrawScope.drawSprite(
    image: ImageBitmap,
    xFraction: Float,
    yFraction: Float,
    widthFraction: Float,
    pivot: Float,
    shadow: Boolean,
    alpha: Float,
) {
    val targetWidth=(size.width*widthFraction).toInt().coerceAtLeast(1)
    val targetHeight=(targetWidth*(image.height.toFloat()/image.width.toFloat())).toInt().coerceAtLeast(1)
    val x=(size.width*xFraction-targetWidth/2f).toInt()
    val y=(size.height*yFraction-targetHeight*pivot).toInt()
    if(shadow) {
        drawOval(
            Color.Black.copy(alpha=.28f * alpha),
            Offset(x+targetWidth*.12f,y+targetHeight*.73f),
            Size(targetWidth*.76f,targetHeight*.14f),
        )
    }
    drawImage(
        image=image,
        srcOffset=IntOffset.Zero,
        srcSize=IntSize(image.width,image.height),
        dstOffset=IntOffset(x,y),
        dstSize=IntSize(targetWidth,targetHeight),
        alpha=alpha,
    )
}
