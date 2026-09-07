package com.zerotoempire.game

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp

/** Strictly reviewed modular terrain from FLUX runs 52 and 66, visible in the active city stage. */
@Composable
internal fun ReviewedTerrainLayer(eraIndex: Int, modifier: Modifier = Modifier) {
    val groups = listOf(
        intArrayOf(R.drawable.zte_terrain_00_final, R.drawable.zte_terrain_01_final, R.drawable.zte_terrain_02_final, R.drawable.zte_terrain_03_final),
        intArrayOf(R.drawable.zte_terrain_04_final, R.drawable.zte_terrain_06_final),
        intArrayOf(R.drawable.zte_terrain_08_final, R.drawable.zte_terrain_10_final, R.drawable.zte_terrain_11_final),
        intArrayOf(R.drawable.zte_terrain_12_final, R.drawable.zte_terrain_13_final),
    )
    val group = when { eraIndex <= 1 -> groups[0]; eraIndex <= 3 -> groups[1]; eraIndex <= 5 -> groups[2]; else -> groups[3] }
    Box(modifier.fillMaxSize()) {
        group.forEachIndexed { index, resId ->
            Image(
                painter = painterResource(resId),
                contentDescription = null,
                contentScale = ContentScale.Fit,
                modifier = Modifier.offset((14 + index * 82).dp, (610 + (index % 2) * 44).dp).size(92.dp),
            )
        }
    }
}
