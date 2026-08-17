package androidx.compose.foundation.layout

import androidx.compose.ui.Modifier

/** Compatibility shim for the Compose version pinned by the project. */
fun Modifier.matchParentSize(): Modifier = fillMaxSize()
