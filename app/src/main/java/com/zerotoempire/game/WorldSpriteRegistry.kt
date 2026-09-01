package com.zerotoempire.game

/**
 * Runtime-facing contract for progressively replacing procedural business art with authored assets.
 *
 * The existing progression art has visual stage thresholds at levels 10, 25, 50, 100, 250, 500
 * and a mastery stage at 1000. The authored pipeline intentionally keeps seven base masters (T0–T6):
 * level 1000 reuses T6 and adds a separate mastery layer rather than requiring an eighth full master.
 *
 * No economy, save, purchase, unlock or monetization behavior belongs in this registry.
 */
internal data class WorldSpriteSpec(
    val businessId: Int,
    val tier: Int,
    val sourceMasterPath: String,
    val runtimeDrawableName: String? = null,
    val frameWidth: Int = 512,
    val frameHeight: Int = 512,
    val frameCount: Int = 1,
    val fps: Int = 0,
    val pivotX: Float = .50f,
    val pivotY: Float = .88f,
    val hasMasteryLayer: Boolean = false
)

internal object WorldSpriteRegistry {
    /** Mirrors the existing evolution thresholds while collapsing the level-1000 mastery state onto T6. */
    fun tierForLevel(level: Int): Int = when {
        level >= 500 -> 6
        level >= 250 -> 5
        level >= 100 -> 4
        level >= 50 -> 3
        level >= 25 -> 2
        level >= 10 -> 1
        else -> 0
    }

    fun masteryForLevel(level: Int): Boolean = level >= 1000

    /**
     * Source masters currently authored for the Era 1 vertical slice.
     * runtimeDrawableName stays null until an optimized Android raster/vector export is committed.
     * Callers must fall back to BusinessArtIcon whenever it is null.
     */
    fun specFor(businessId: Int, level: Int): WorldSpriteSpec? {
        val tier = tierForLevel(level)
        val mastery = masteryForLevel(level)
        val source = when (businessId to tier) {
            0 to 0 -> "art/source/era01/street_stand/t0/zte_business_00_t0_master.svg"
            0 to 1 -> "art/source/era01/street_stand/t1/zte_business_00_t1_master.svg"
            0 to 2 -> "art/source/era01/street_stand/t2/zte_business_00_t2_master.svg"
            1 to 0 -> "art/source/era01/corner_shop/t0/zte_business_01_t0_master.svg"
            1 to 1 -> "art/source/era01/corner_shop/t1/zte_business_01_t1_master.svg"
            2 to 0 -> "art/source/era01/furnace_stall/t0/zte_business_02_t0_master.svg"
            3 to 0 -> "art/source/era01/assembly_hub/t0/zte_business_03_t0_master.svg"
            else -> return null
        }
        return WorldSpriteSpec(
            businessId = businessId,
            tier = tier,
            sourceMasterPath = source,
            runtimeDrawableName = null,
            hasMasteryLayer = mastery
        )
    }
}
