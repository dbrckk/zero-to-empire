package com.zerotoempire.game

import android.media.AudioManager
import android.media.ToneGenerator

data class EmpireEra(
    val index: Int,
    val name: String,
    val subtitle: String,
    val icon: String,
    val requiredLifetimeCash: Double
)

object EmpireEras {
    val catalog = listOf(
        EmpireEra(0, "SCRAPPY START", "Turn pocket change into momentum.", "◌", 0.0),
        EmpireEra(1, "LOCAL HUSTLE", "Own the block. Then the city.", "◆", 1_000.0),
        EmpireEra(2, "INDUSTRIAL AGE", "Scale machines, factories and capital.", "⚙", 1_000_000.0),
        EmpireEra(3, "MEGACITY", "Your economy shapes entire cities.", "▦", 1_000_000_000.0),
        EmpireEra(4, "PLANETARY", "Earth is no longer the limit.", "◉", 1_000_000_000_000.0),
        EmpireEra(5, "STELLAR", "Harness stars as infrastructure.", "✦", 1_000_000_000_000_000.0),
        EmpireEra(6, "GALACTIC", "Markets now span the galaxy.", "✧", 1_000_000_000_000_000_000.0),
        EmpireEra(7, "INTERGALACTIC", "Trade routes bridge entire galaxy clusters.", "◇", 1e21),
        EmpireEra(8, "COSMIC", "Civilizations become nodes in your economy.", "◎", 1e24),
        EmpireEra(9, "REALITY ENGINE", "Matter, energy and information become one market.", "⬡", 1e27),
        EmpireEra(10, "TRANSCENDENT", "Your empire operates beyond conventional scale.", "✺", 1e30)
    )

    fun current(lifetimeCash: Double): EmpireEra {
        val safe = if (lifetimeCash.isFinite()) lifetimeCash.coerceAtLeast(0.0) else Double.MAX_VALUE
        return catalog.last { safe >= it.requiredLifetimeCash }
    }

    fun next(lifetimeCash: Double): EmpireEra? {
        val safe = if (lifetimeCash.isFinite()) lifetimeCash.coerceAtLeast(0.0) else Double.MAX_VALUE
        return catalog.firstOrNull { safe < it.requiredLifetimeCash }
    }
}

data class MajorCelebration(
    val title: String,
    val subtitle: String,
    val icon: String,
    val accent: String
)

object Celebrations {
    fun milestone(business: Business): MajorCelebration = MajorCelebration(
        title = "POWER SPIKE ×${GameEconomy.milestoneMultiplier(business.level).toInt()}",
        subtitle = "${business.name} reached level ${business.level}",
        icon = business.emoji,
        accent = "MILESTONE"
    )

    fun era(era: EmpireEra): MajorCelebration = MajorCelebration(
        title = era.name,
        subtitle = era.subtitle,
        icon = era.icon,
        accent = "NEW ERA"
    )
}

/** Lightweight fallback audio retained for compatibility. */
class GameAudioEngine {
    private val tone = ToneGenerator(AudioManager.STREAM_MUSIC, 36)

    fun tap() = tone.startTone(ToneGenerator.TONE_PROP_BEEP, 28)
    fun purchase() = tone.startTone(ToneGenerator.TONE_PROP_ACK, 45)
    fun reward() = tone.startTone(ToneGenerator.TONE_PROP_PROMPT, 90)
    fun milestone() = tone.startTone(ToneGenerator.TONE_CDMA_ALERT_CALL_GUARD, 170)
    fun prestige() = tone.startTone(ToneGenerator.TONE_CDMA_ABBR_ALERT, 260)
    fun release() = tone.release()
}
