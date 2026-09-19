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

/** Semantically reviewed FLUX machine masters, including run 68 stragglers, visible as era-specific production machinery. */
@Composable
internal fun ReviewedMachineLayer(eraIndex: Int, modifier: Modifier = Modifier) {
    val groups = listOf(
        intArrayOf(R.drawable.zte_machine_00_0_final, R.drawable.zte_machine_00_1_final, R.drawable.zte_machine_01_0_final, R.drawable.zte_machine_01_1_final),
        intArrayOf(R.drawable.zte_machine_02_0_final, R.drawable.zte_machine_02_1_final, R.drawable.zte_machine_03_0_final, R.drawable.zte_machine_03_1_final),
        intArrayOf(R.drawable.zte_machine_04_1_final, R.drawable.zte_machine_05_0_final, R.drawable.zte_machine_05_1_final, R.drawable.zte_machine_06_0_final, R.drawable.zte_machine_06_1_final),
        intArrayOf(R.drawable.zte_machine_07_0_final, R.drawable.zte_machine_07_1_final, R.drawable.zte_machine_08_0_final, R.drawable.zte_machine_08_1_final),
        intArrayOf(R.drawable.zte_machine_09_0_final, R.drawable.zte_machine_09_1_final, R.drawable.zte_machine_10_0_final),
        intArrayOf(R.drawable.zte_machine_10_1_final, R.drawable.zte_machine_11_0_final, R.drawable.zte_machine_11_1_final, R.drawable.zte_machine_12_1_final),
        intArrayOf(R.drawable.zte_machine_12_0_final, R.drawable.zte_machine_13_0_final, R.drawable.zte_machine_13_1_final),
    )
    val ids = groups[eraIndex.coerceIn(0, groups.lastIndex)]
    val x = listOf(18.dp, 94.dp, 188.dp, 270.dp)
    val y = listOf(280.dp, 360.dp, 430.dp, 500.dp)
    Box(modifier.fillMaxSize()) {
        ids.forEachIndexed { index, resId ->
            Image(
                painter = painterResource(resId),
                contentDescription = null,
                contentScale = ContentScale.Fit,
                modifier = Modifier.offset(x[index], y[index]).size(if (eraIndex >= 4) 54.dp else 48.dp),
            )
        }
    }
}
