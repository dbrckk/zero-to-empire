package com.zerotoempire.game

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.delay

/**
 * The debug build exposes this surface as a separate launcher icon. It is
 * entirely absent from the release source set and does not approve assets.
 */
class CharacterReviewActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { CharacterReviewGallery() }
    }
}

@Composable
private fun CharacterReviewGallery() {
    var worldFrame by remember { mutableIntStateOf(0) }
    var playing by remember { mutableStateOf(true) }
    LaunchedEffect(playing) {
        while (playing) {
            delay(100L)
            worldFrame = (worldFrame + 1) % 1680
        }
    }

    MaterialTheme {
        Surface(Modifier.fillMaxSize()) {
            LazyColumn(
                modifier = Modifier.padding(horizontal = 12.dp, vertical = 14.dp),
                verticalArrangement = Arrangement.spacedBy(14.dp),
            ) {
                item {
                    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        Text("ZERO → EMPIRE · Animation QA",
                            style = MaterialTheme.typography.titleLarge)
                        Text(
                            "Visualisation uniquement : une animation correcte dans cette galerie " +
                                "ne signifie pas que le sprite est approuvé pour la production.",
                            style = MaterialTheme.typography.bodySmall,
                        )
                        Row(horizontalArrangement = Arrangement.spacedBy(7.dp)) {
                            Button(onClick = { playing = !playing }) {
                                Text(if (playing) "Pause" else "Lecture")
                            }
                            OutlinedButton(onClick = {
                                playing = false
                                worldFrame = Math.floorMod(worldFrame - 1, 1680)
                            }) { Text("−1") }
                            OutlinedButton(onClick = {
                                playing = false
                                worldFrame = (worldFrame + 1) % 1680
                            }) { Text("+1") }
                        }
                        Text(
                            "Image : $worldFrame · 10 FPS · testez aussi le jeu réel",
                            style = MaterialTheme.typography.labelMedium,
                        )
                    }
                }
                items(ReviewedCharacterRole.entries) { role ->
                    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        Text(role.name, style = MaterialTheme.typography.titleMedium)
                        // A 320dp phone cannot fit three 96dp thumbnails
                        // plus labels, spacers and horizontal padding.
                        BoxWithConstraints(Modifier.fillMaxWidth()) {
                            val columns = if (maxWidth < 400.dp) 2 else 3
                            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                                ReviewedCharacterAction.entries.chunked(columns).forEach { actions ->
                                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                                        actions.forEach { action ->
                                            ReviewCell(role, action, worldFrame)
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                item {
                    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        Text(
                            "STAGE-SCALE CHARACTER LAYER",
                            style = MaterialTheme.typography.titleMedium,
                        )
                        Text(
                            "Exact city character renderer and positions at gameplay sizes " +
                                "(35–46 dp). This debug comparison does not approve any sprite. " +
                                "Pause and single-step above also control this layer.",
                            style = MaterialTheme.typography.bodySmall,
                        )
                        // Only the real city character composable is used here.
                        // CI injects review-only textures into the isolated APK,
                        // never the shipped production masters.
                        Box(
                            Modifier
                                .fillMaxWidth()
                                .height(620.dp)
                                .background(
                                    Brush.verticalGradient(
                                        listOf(Color(0xFF07101C), Color(0xFF101B24), Color(0xFF080D13))
                                    )
                                ),
                        ) {
                            ReviewedCharacterLayer(
                                eraIndex = 0,
                                worldFrame = worldFrame,
                                reducedMotion = false,
                                modifier = Modifier.fillMaxSize(),
                            )
                        }
                    }
                }
            }
        }
    }
}

@Composable
private fun ReviewCell(
    role: ReviewedCharacterRole,
    action: ReviewedCharacterAction,
    worldFrame: Int,
) {
    val context = LocalContext.current
    val atlas = remember(role, action) {
        ImageBitmap.imageResource(context.resources, reviewedCharacterRasterRes(role, action))
    }
    val frameCount = reviewedCharacterFrameCount(action)
    Column(
        modifier = Modifier
            .background(MaterialTheme.colorScheme.surfaceVariant)
            .padding(6.dp),
    ) {
        CharacterAtlasFrame(
            atlas = atlas,
            frame = worldFrame % frameCount,
            modifier = Modifier.size(96.dp),
        )
        Text(action.name, style = MaterialTheme.typography.labelSmall)
        Text("${worldFrame % frameCount + 1}/$frameCount", style = MaterialTheme.typography.labelSmall)
    }
}
