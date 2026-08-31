package com.zerotoempire.game

import java.io.File
import org.junit.Assert.assertTrue
import org.junit.Test

class RuntimePerformanceInvariantTest {
    @Test
    fun endgameAtmosphereDoesNoWorkBeforeLateGame() {
        val source = source("EndgameAtmosphere.kt")
        val earlyReturn = source.indexOf("if (eraIndex < 7) return")
        val animationClock = source.indexOf("rememberInfiniteTransition(label")
        val canvas = source.indexOf("Canvas(modifier)")

        assertTrue(earlyReturn >= 0)
        assertTrue(animationClock > earlyReturn)
        assertTrue(canvas > earlyReturn)
    }

    @Test
    fun powerCoreKeepsReducedMotionOutsideInfiniteClock() {
        val source = source("EmpireCoreArt.kt")
        val reducedBranch = source.indexOf("if (reducedMotion)")
        val animationClock = source.indexOf("rememberInfiniteTransition(label")

        assertTrue(reducedBranch >= 0)
        assertTrue(animationClock > reducedBranch)
    }

    @Test
    fun batterySaverDisablesDecorativeParticles() {
        val source = source("MotionQuality.kt")
        assertTrue(source.contains("fun reducedMotion(context: Context): Boolean = !animationsEnabled(context) || lowPowerMode(context)"))
        assertTrue(source.contains("reducedMotion(context) -> 0"))
    }

    @Test
    fun transientEraImpactLeavesCompositionClockWhenFinished() {
        val source = source("CinematicRuntimeTransition.kt")
        assertTrue(source.contains("phase < CINEMATIC_TRANSITION_END"))
        assertTrue(source.contains("if (shouldRenderCinematicTransition(reducedMotion, phase.value))"))
    }

    private fun source(name: String): String {
        val moduleRelative = File("src/main/java/com/zerotoempire/game/$name")
        val repoRelative = File("app/src/main/java/com/zerotoempire/game/$name")
        val file = when {
            moduleRelative.isFile -> moduleRelative
            repoRelative.isFile -> repoRelative
            else -> error("Unable to locate production source $name")
        }
        return file.readText()
    }
}
