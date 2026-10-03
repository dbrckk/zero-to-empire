package com.zerotoempire.game

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.delay

/**
 * Debug-only semantic review surface for all authored character atlases.
 *
 * This activity is declared only by src/debug/AndroidManifest.xml and therefore
 * cannot ship in release builds.
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
    LaunchedEffect(Unit) {
        while (true) {
            delay(100)
            worldFrame = (worldFrame + 1) % 240
        }
    }

    MaterialTheme {
        Surface(Modifier.fillMaxSize()) {
            LazyColumn(
                modifier = Modifier.padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(14.dp),
            ) {
                items(ReviewedCharacterRole.entries) { role ->
                    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        Text(role.name, style = MaterialTheme.typography.titleLarge)
                        ReviewedCharacterAction.entries.chunked(3).forEach { actions ->
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
        Text("$frameCount frames", style = MaterialTheme.typography.labelSmall)
    }
}
