package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import androidx.compose.runtime.Stable
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import kotlin.random.Random

/** Transient presentation events. They never alter economy state. */
sealed interface JuiceEvent {
    data class CashBurst(val amount: Double, val x: Float = .5f, val y: Float = .5f) : JuiceEvent
    data class PurchasePop(val businessId: Int) : JuiceEvent
    data class Milestone(val businessId: Int, val level: Int) : JuiceEvent
    data class PrestigeBurst(val points: Int) : JuiceEvent
}

data class SparkParticle(
    val id: Long,
    val angle: Float,
    val distance: Float,
    val size: Float
)

object ParticleFactory {
    fun burst(count: Int = 14): List<SparkParticle> = List(count.coerceIn(4, 40)) {
        SparkParticle(
            id = System.nanoTime() + it,
            angle = Random.nextFloat() * 360f,
            distance = 35f + Random.nextFloat() * 90f,
            size = 3f + Random.nextFloat() * 7f
        )
    }
}

@Stable
class PressMotion {
    val scale = Animatable(1f)
    suspend fun pulse() = coroutineScope {
        launch { scale.animateTo(.91f, spring(stiffness = Spring.StiffnessHigh)) }
        launch {
            scale.animateTo(1.04f, spring(dampingRatio = .45f, stiffness = Spring.StiffnessMedium))
            scale.animateTo(1f, spring(dampingRatio = .55f))
        }
    }
}

enum class HapticCue { TAP, PURCHASE, MILESTONE, REWARD, PRESTIGE }

interface HapticGateway { fun play(cue: HapticCue) }
interface AudioGateway { fun play(cue: AudioCue) }
enum class AudioCue { TAP, COIN, PURCHASE, MILESTONE, REWARD, PRESTIGE, UI_OPEN }
