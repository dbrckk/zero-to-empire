package com.zerotoempire.game

import androidx.compose.animation.AnimatedContentTransitionScope
import androidx.compose.animation.ContentTransform
import androidx.compose.animation.EnterTransition
import androidx.compose.animation.ExitTransition
import androidx.compose.foundation.layout.Box
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier

/**
 * Package-local animation shims used by the compact game UI.
 *
 * Compose exposes scope-specific AnimatedVisibility overloads (RowScope/ColumnScope)
 * which can become ambiguous inside deeply nested compact composables. Keeping a
 * package-local entry point gives Kotlin one deterministic overload while preserving
 * the public call sites. State-change emphasis is still handled by the card's
 * Animatable pulse and haptics.
 */
@Composable
fun AnimatedVisibility(
    visible: Boolean,
    enter: EnterTransition = EnterTransition.None,
    exit: ExitTransition = ExitTransition.None,
    modifier: Modifier = Modifier,
    content: @Composable () -> Unit
) {
    if (visible) Box(modifier = modifier) { content() }
}

/**
 * Deterministic compact-state content switch for manager badges/details.
 * The transition specification remains accepted so existing call sites stay clear
 * and can be upgraded to richer motion later without another API migration.
 */
@Composable
fun <T> AnimatedContent(
    targetState: T,
    transitionSpec: AnimatedContentTransitionScope<T>.() -> ContentTransform,
    label: String = "",
    content: @Composable (T) -> Unit
) {
    content(targetState)
}
