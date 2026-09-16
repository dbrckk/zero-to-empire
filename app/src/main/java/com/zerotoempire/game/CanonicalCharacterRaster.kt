package com.zerotoempire.game

/**
 * Source-reviewed character roles backed by authored production sprites.
 *
 * Runtime raster bindings remain intentionally limited to assets that have
 * completed the production pipeline. Action semantics below are documented by
 * the character-sheet factory and do not imply that every action sheet is
 * ready for runtime rendering.
 */
internal enum class ReviewedCharacterRole {
    OPERATOR,
    TECHNICIAN,
    LOGISTICS,
    ENGINEER,
}

internal enum class ReviewedCharacterAction {
    IDLE,
    WALK,
    WORK,
    CARRY,
    REPAIR,
    CELEBRATE,
}

internal fun reviewedCharacterFrameCount(action: ReviewedCharacterAction): Int = when (action) {
    ReviewedCharacterAction.IDLE -> 6
    ReviewedCharacterAction.WALK -> 8
    ReviewedCharacterAction.WORK -> 10
    ReviewedCharacterAction.CARRY -> 8
    ReviewedCharacterAction.REPAIR -> 10
    ReviewedCharacterAction.CELEBRATE -> 8
}

internal fun reviewedCharacterActionLoopsAmbiently(action: ReviewedCharacterAction): Boolean = when (action) {
    ReviewedCharacterAction.IDLE,
    ReviewedCharacterAction.WALK,
    ReviewedCharacterAction.WORK -> true
    ReviewedCharacterAction.CARRY,
    ReviewedCharacterAction.REPAIR,
    ReviewedCharacterAction.CELEBRATE -> false
}

internal fun reviewedCharacterIdleRasterRes(role: ReviewedCharacterRole): Int = when (role) {
    ReviewedCharacterRole.OPERATOR -> R.drawable.zte_chr_op_idle_final
    ReviewedCharacterRole.TECHNICIAN -> R.drawable.zte_chr_tech_idle_final
    ReviewedCharacterRole.LOGISTICS -> R.drawable.zte_chr_log_idle_final
    ReviewedCharacterRole.ENGINEER -> R.drawable.zte_chr_eng_idle_final
}
