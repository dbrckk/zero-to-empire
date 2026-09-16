package com.zerotoempire.game

/**
 * Source-reviewed character roles backed by authored production sprites.
 *
 * This first runtime contract intentionally exposes only IDLE art. The wider
 * CHR catalogue also contains WALK/WORK/CARRY/REPAIR/CELEB poses, but those
 * are not treated as animation frames until their timing/transition semantics
 * are explicitly reviewed.
 */
internal enum class ReviewedCharacterRole {
    OPERATOR,
    TECHNICIAN,
    LOGISTICS,
    ENGINEER,
}

internal fun reviewedCharacterIdleRasterRes(role: ReviewedCharacterRole): Int = when (role) {
    ReviewedCharacterRole.OPERATOR -> R.drawable.zte_chr_op_idle_final
    ReviewedCharacterRole.TECHNICIAN -> R.drawable.zte_chr_tech_idle_final
    ReviewedCharacterRole.LOGISTICS -> R.drawable.zte_chr_log_idle_final
    ReviewedCharacterRole.ENGINEER -> R.drawable.zte_chr_eng_idle_final
}
