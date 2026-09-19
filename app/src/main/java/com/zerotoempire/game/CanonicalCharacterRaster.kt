package com.zerotoempire.game

/**
 * Source-reviewed character roles backed by authored production sprites.
 *
 * Every authored sheet uses the same 4x4 atlas contract (256px cells on a
 * 1024px canvas). Runtime callers must render one frame at a time rather than
 * displaying the whole atlas as a static image.
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

internal const val REVIEWED_CHARACTER_ATLAS_SIDE = 1024
internal const val REVIEWED_CHARACTER_CELL_SIDE = 256
internal const val REVIEWED_CHARACTER_COLUMNS = 4
internal const val REVIEWED_CHARACTER_ROWS = 4

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

internal fun reviewedCharacterRasterRes(
    role: ReviewedCharacterRole,
    action: ReviewedCharacterAction,
): Int = when (role) {
    ReviewedCharacterRole.OPERATOR -> when (action) {
        ReviewedCharacterAction.IDLE -> R.drawable.zte_chr_op_idle_final
        ReviewedCharacterAction.WALK -> R.drawable.zte_chr_op_walk_final
        ReviewedCharacterAction.WORK -> R.drawable.zte_chr_op_work_final
        ReviewedCharacterAction.CARRY -> R.drawable.zte_chr_op_carry_final
        ReviewedCharacterAction.REPAIR -> R.drawable.zte_chr_op_repair_final
        ReviewedCharacterAction.CELEBRATE -> R.drawable.zte_chr_op_celeb_final
    }
    ReviewedCharacterRole.TECHNICIAN -> when (action) {
        ReviewedCharacterAction.IDLE -> R.drawable.zte_chr_tech_idle_final
        ReviewedCharacterAction.WALK -> R.drawable.zte_chr_tech_walk_final
        ReviewedCharacterAction.WORK -> R.drawable.zte_chr_tech_work_final
        ReviewedCharacterAction.CARRY -> R.drawable.zte_chr_tech_carry_final
        ReviewedCharacterAction.REPAIR -> R.drawable.zte_chr_tech_repair_final
        ReviewedCharacterAction.CELEBRATE -> R.drawable.zte_chr_tech_celeb_final
    }
    ReviewedCharacterRole.LOGISTICS -> when (action) {
        ReviewedCharacterAction.IDLE -> R.drawable.zte_chr_log_idle_final
        ReviewedCharacterAction.WALK -> R.drawable.zte_chr_log_walk_final
        ReviewedCharacterAction.WORK -> R.drawable.zte_chr_log_work_final
        ReviewedCharacterAction.CARRY -> R.drawable.zte_chr_log_carry_final
        ReviewedCharacterAction.REPAIR -> R.drawable.zte_chr_log_repair_final
        ReviewedCharacterAction.CELEBRATE -> R.drawable.zte_chr_log_celeb_final
    }
    ReviewedCharacterRole.ENGINEER -> when (action) {
        ReviewedCharacterAction.IDLE -> R.drawable.zte_chr_eng_idle_final
        ReviewedCharacterAction.WALK -> R.drawable.zte_chr_eng_walk_final
        ReviewedCharacterAction.WORK -> R.drawable.zte_chr_eng_work_final
        ReviewedCharacterAction.CARRY -> R.drawable.zte_chr_eng_carry_final
        ReviewedCharacterAction.REPAIR -> R.drawable.zte_chr_eng_repair_final
        ReviewedCharacterAction.CELEBRATE -> R.drawable.zte_chr_eng_celeb_final
    }
}

internal fun reviewedCharacterIdleRasterRes(role: ReviewedCharacterRole): Int =
    reviewedCharacterRasterRes(role, ReviewedCharacterAction.IDLE)
