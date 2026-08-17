package com.zerotoempire.game

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
    val accent: String,
    val businessId: Int? = null,
    val businessLevel: Int? = null
)

object Celebrations {
    fun milestone(business: Business): MajorCelebration = MajorCelebration(
        title = "POWER SPIKE ×${GameEconomy.milestoneMultiplier(business.level).toInt()}",
        subtitle = "${business.name} reached level ${business.level}",
        icon = business.emoji,
        accent = "MILESTONE",
        businessId = business.id,
        businessLevel = business.level
    )

    fun era(era: EmpireEra): MajorCelebration = MajorCelebration(
        title = era.name,
        subtitle = era.subtitle,
        icon = era.icon,
        accent = "NEW ERA"
    )
}

/** Compatibility facade backed exclusively by the premium SoundPool engine. */
class GameAudioEngine {
    fun tap() = GameSfxBus.play(PremiumSfxCue.TAP)
    fun purchase() = GameSfxBus.play(PremiumSfxCue.PURCHASE)
    fun reward() = GameSfxBus.play(PremiumSfxCue.REWARD)
    fun milestone() = GameSfxBus.play(PremiumSfxCue.MILESTONE)
    fun prestige() = GameSfxBus.play(PremiumSfxCue.PRESTIGE)
    fun release() = Unit
}
