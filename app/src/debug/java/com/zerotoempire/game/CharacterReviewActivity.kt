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
import androidx.compose.material3.darkColorScheme
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
import androidx.compose.ui.Alignment
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
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
    var daylightStage by remember { mutableStateOf(false) }
    var inspectedRole by remember { mutableStateOf<ReviewedCharacterRole?>(null) }
    var inspectedAction by remember { mutableStateOf(ReviewedCharacterAction.WALK) }
    LaunchedEffect(playing) {
        while (playing) {
            delay(100L)
            worldFrame = (worldFrame + 1) % 1680
        }
    }

    // The review gallery must show the authored colors against a calibrated
    // dark game-like backdrop, not generic light Material defaults. This lives
    // only in the isolated debug review activity, never the shipped game UI.
    MaterialTheme(
        colorScheme = darkColorScheme(
            primary = Color(0xFF79D8E9),
            onPrimary = Color(0xFF102430),
            secondary = Color(0xFFFFC081),
            surface = Color(0xFF142333),
            onSurface = Color(0xFFF0F6FA),
            surfaceVariant = Color(0xFF1E3142),
            onSurfaceVariant = Color(0xFFC5D5E1),
            background = Color(0xFF0B1520),
            onBackground = Color(0xFFE9F3F9),
        ),
    ) {
        Surface(
            modifier = Modifier.fillMaxSize(),
            color = MaterialTheme.colorScheme.background,
        ) {
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
                            "Production city stage: real vista, roads, terrain, machines, traffic " +
                                "and character layer (35–46 dp), without interactive businesses. " +
                                "Only this isolated APK substitutes candidate atlases. " +
                                "Pause and step control the entire scene; this is not approval.",
                            style = MaterialTheme.typography.bodySmall,
                        )
                        OutlinedButton(onClick = { daylightStage = !daylightStage }) {
                            Text(if (daylightStage) "Normal city lighting" else "Daylight contrast wash")
                        }
                        Text(
                            if (daylightStage) "DAYLIGHT WASH · QA SIMULATION" else "PRODUCTION CITY LIGHTING",
                            style = MaterialTheme.typography.labelMedium,
                        )
                        Text(
                            "Choisissez un métier et une animation : la scène emploie les vrais " +
                                "calques de la ville, mais sans les panneaux économiques interactifs. " +
                                "Le mode clair est une simulation QA, pas une météo du jeu.",
                            style = MaterialTheme.typography.bodySmall,
                        )
                        OutlinedButton(onClick = { inspectedRole = null }) {
                            Text("Tous les métiers")
                        }
                        ReviewedCharacterRole.entries.chunked(2).forEach { roleRow ->
                            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                                roleRow.forEach { role ->
                                    OutlinedButton(
                                        modifier = Modifier.weight(1f),
                                        onClick = { inspectedRole = role },
                                    ) {
                                        Text(
                                            role.name,
                                            style = MaterialTheme.typography.labelSmall,
                                        )
                                    }
                                }
                            }
                        }
                        if (inspectedRole != null) {
                            val selectedRole = requireNotNull(inspectedRole)
                            Text(
                                "${selectedRole.name} · ${inspectedAction.name}",
                                style = MaterialTheme.typography.labelMedium,
                            )
                            Text(
                                "STAGE FRAME: $worldFrame",
                                style = MaterialTheme.typography.labelSmall,
                            )
                            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                                OutlinedButton(onClick = { playing = !playing }) {
                                    Text(if (playing) "Pause stage" else "Play stage")
                                }
                                OutlinedButton(onClick = {
                                    playing = false
                                    worldFrame = (worldFrame + 1) % 1680
                                }) { Text("Stage +1") }
                            }
                            // This full-body preview must be above the six selector
                            // buttons. On narrow Android viewports the former
                            // bottom placement clipped both actors at the waist.
                            Text(
                                "${selectedRole.name} · REAL GAME SIZE · NIGHT / DAY",
                                style = MaterialTheme.typography.labelMedium,
                            )
                            val context = LocalContext.current
                            val actionAtlas = remember(selectedRole, inspectedAction) {
                                ImageBitmap.imageResource(
                                    context.resources,
                                    reviewedCharacterRasterRes(
                                        selectedRole,
                                        inspectedAction,
                                    ),
                                )
                            }
                            val actionFrame = worldFrame % reviewedCharacterFrameCount(
                                inspectedAction,
                            )
                            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                                listOf(
                                    Triple("NIGHT · 42 dp", Color(0xFF101B24), 42.dp),
                                    Triple("DAY · 39 dp", Color(0xFFBACCD6), 39.dp),
                                ).forEach { (label, ground, side) ->
                                    Column(
                                        modifier = Modifier
                                            .weight(1f)
                                            .background(ground)
                                            .padding(vertical = 8.dp),
                                        horizontalAlignment = Alignment.CenterHorizontally,
                                        verticalArrangement = Arrangement.spacedBy(6.dp),
                                    ) {
                                        Text(
                                            label,
                                            color = if (ground == Color(0xFF101B24)) {
                                                Color.White
                                            } else {
                                                Color(0xFF172B37)
                                            },
                                            style = MaterialTheme.typography.labelSmall,
                                        )
                                        CharacterAtlasFrame(
                                            atlas = actionAtlas,
                                            frame = actionFrame,
                                            edgeSeparation = Color(0xFF8AD9EE),
                                            modifier = Modifier.size(side),
                                        )
                                    }
                                }
                            }
                            // At 320dp widths, two labeled buttons per row
                            // remain touchable; no hidden horizontal scrolling.
                            ReviewedCharacterAction.entries.chunked(2).forEach { rowActions ->
                                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                                    rowActions.forEach { action ->
                                        OutlinedButton(
                                            modifier = Modifier.weight(1f),
                                            onClick = { inspectedAction = action },
                                        ) {
                                            Text(
                                                action.name,
                                                style = MaterialTheme.typography.labelSmall,
                                            )
                                        }
                                    }
                                }
                            }
                        }
                        // Reuse the actual production city stage: its skyline,
                        // road, terrain, machines, traffic and character renderer
                        // are identical. Only its clock and role selection are
                        // overridden inside this isolated preview. No shipping
                        // runtime drawable or save file is modified.
                        Box(
                            Modifier
                                .fillMaxWidth()
                                .height(620.dp)
                                .semantics { contentDescription = "REVIEW GAMEPLAY STAGE" },
                        ) {
                            AscendantCityStage(
                                eraIndex = 0,
                                modifier = Modifier.fillMaxSize(),
                                reviewWorldFrame = worldFrame,
                                reviewRoleFilter = inspectedRole,
                                reviewActionOverride = if (inspectedRole != null) inspectedAction else null,
                            )
                            if (daylightStage) {
                                // Contrast stress test, not a claim that the
                                // production city currently supports day/night.
                                Box(
                                    Modifier.fillMaxSize()
                                        .background(Color(0x44DBEAF2)),
                                )
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
        Text("${worldFrame % frameCount + 1}/$frameCount", style = MaterialTheme.typography.labelSmall)
    }
}
