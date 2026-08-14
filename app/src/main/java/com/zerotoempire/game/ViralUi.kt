package com.zerotoempire.game

import android.content.Intent
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun ViralShareChip(state: GameState) {
    val milestone = ViralMilestones.latestUnlocked(state.lifetimeCash) ?: return
    val context = LocalContext.current

    Surface(
        onClick = {
            val text = buildString {
                append(milestone.headline)
                append("\n")
                append(milestone.body)
                append("\n\nZERO → EMPIRE")
            }
            val intent = Intent(Intent.ACTION_SEND).apply {
                type = "text/plain"
                putExtra(Intent.EXTRA_TEXT, text)
            }
            context.startActivity(Intent.createChooser(intent, "Share your empire"))
        },
        shape = RoundedCornerShape(50),
        color = EmpireColors.SurfaceHigh
    ) {
        Text(
            text = "↗ SHARE MILESTONE",
            modifier = Modifier.padding(horizontal = 12.dp, vertical = 7.dp),
            color = EmpireColors.Cyan,
            fontSize = 9.sp,
            fontWeight = FontWeight.Black
        )
    }
}
