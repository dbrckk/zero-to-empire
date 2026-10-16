package com.zerotoempire.game

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp

/** Strictly reviewed modular terrain from FLUX runs 52, 66, 68 and 69, visible in the active city stage. */
@Composable
internal fun ReviewedTerrainLayer(eraIndex: Int, modifier: Modifier = Modifier) {
    val groups = listOf(
        intArrayOf(R.drawable.zte_terrain_00_final, R.drawable.zte_terrain_01_final, R.drawable.zte_terrain_02_final, R.drawable.zte_terrain_03_final),
        intArrayOf(R.drawable.zte_terrain_04_final, R.drawable.zte_terrain_05_final, R.drawable.zte_terrain_06_final, R.drawable.zte_terrain_07_final),
        intArrayOf(R.drawable.zte_terrain_08_final, R.drawable.zte_terrain_09_final, R.drawable.zte_terrain_10_final, R.drawable.zte_terrain_11_final),
        intArrayOf(R.drawable.zte_terrain_12_final, R.drawable.zte_terrain_13_final),
    )
    val group = when { eraIndex <= 1 -> groups[0]; eraIndex <= 3 -> groups[1]; eraIndex <= 5 -> groups[2]; else -> groups[3] }
    // These are physical ground tiles, not an offscreen decoration row.
    // The old absolute 610/654dp offsets clipped almost every tile inside the
    // shipping 620dp stage, even though every resource was technically loaded.
    BoxWithConstraints(modifier.fillMaxSize()) {
        val side = minOf(88.dp, ((maxWidth - 16.dp) / 4f).coerceAtLeast(32.dp))
        val usableWidth = (maxWidth - side - 16.dp).coerceAtLeast(0.dp)
        val groundTop = (maxHeight - side - 16.dp).coerceAtLeast(0.dp)
        group.forEachIndexed { index, resId ->
            val laneFraction = if (group.size <= 1) .5f else index.toFloat() / (group.size - 1)
            val x = 8.dp + usableWidth * laneFraction
            val y = (groundTop - if (index % 2 == 1) 10.dp else 0.dp).coerceAtLeast(0.dp)
            Image(
                painter = painterResource(resId),
                contentDescription = null,
                contentScale = ContentScale.Fit,
                modifier = Modifier.offset(x, y).size(side),
            )
        }
    }
}
