package com.zerotoempire.game

import android.content.Intent
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
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
        modifier = Modifier.heightIn(min = 48.dp),
        shape = RoundedCornerShape(50),
        color = EmpireColors.SurfaceHigh
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 10.dp, vertical = 5.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            MetaSprite(MetaSpriteKind.SHARE, size = 24.dp)
            Spacer(Modifier.width(6.dp))
            Text("SHARE MILESTONE", color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Black)
        }
    }
}
