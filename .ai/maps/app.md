This file is a merged representation of a subset of the codebase, containing specifically included files and files not matching ignore patterns, combined into a single document by Repomix.
The content has been processed where content has been compressed (code blocks are separated by ⋮---- delimiter).

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: **/*.{py,js,mjs,cjs,ts,tsx,jsx,java,kt,kts,gd,groovy,gradle,toml,json,yaml,yml,sql,sh}
- Files matching these patterns are excluded: .ai/**, **/node_modules/**, **/.gradle/**, **/build/**, **/dist/**, **/.venv/**, **/__pycache__/**, **/.pytest_cache/**, **/.git/**, **/coverage/**, **/*.lock, **/*.min.js, **/*.map, assets/**, art/**, art_sources/**, marketing/**, colab/**, kaggle/**, discovery-cache.json, health-snapshot.json, history.json
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Content has been compressed - code blocks are separated by ⋮---- delimiter
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
src/
  debug/
    java/
      com/
        zerotoempire/
          game/
            SmokeSeedReceiver.kt
  main/
    java/
      com/
        zerotoempire/
          game/
            AdaptiveMusic.kt
            AdMobInterstitialGateway.kt
            AdMobRewardedGateway.kt
            Analytics.kt
            AscendantCityWorld.kt
            AscensionAdvisor.kt
            BillingDiagnostics.kt
            BillingFailurePolicy.kt
            BulkPurchase.kt
            BulkQuoteDock.kt
            BusinessGroup01Art.kt
            BusinessGroup01Evolution.kt
            BusinessGroup02Art.kt
            BusinessGroup02Evolution.kt
            BusinessGroup03Art.kt
            BusinessGroup03Evolution.kt
            BusinessGroup04Art.kt
            BusinessGroup04Evolution.kt
            CanonicalBusinessRaster.kt
            CanonicalBusinessTier.kt
            CanonicalCharacterRaster.kt
            CanonicalFxRaster.kt
            CanonicalFxSprite.kt
            Challenges.kt
            ChallengeUi.kt
            CinematicArt.kt
            CinematicRuntimeTransition.kt
            CommerceUi.kt
            ContentUnlocks.kt
            DrawScopeCompat.kt
            DroneThruster.kt
            DynastyProgression.kt
            EconomyMath.kt
            ElectricArc.kt
            EmpireArt.kt
            EmpireArtCompat.kt
            EmpireCoreArt.kt
            EmpireNumberFormat.kt
            EndgameAtmosphere.kt
            EndgameBusinessSprites.kt
            EndgameManagerPortrait.kt
            EndgameProgression.kt
            EraVistaAAA.kt
            EraVistaCinematicOverlay.kt
            FoundryWorldMotion.kt
            FullScreenAdActivityPolicy.kt
            GameEconomy.kt
            GameEngine.kt
            GameFeel.kt
            GameRepository.kt
            GameTheme.kt
            GameViewModel.kt
            GrowthRuntime.kt
            GrowthTelemetry.kt
            HologramScanSweep.kt
            IdentitySystems.kt
            IdentityUi.kt
            IncomePickupSparkle.kt
            IndustrialBusinessFx.kt
            InterstitialController.kt
            InterstitialPolicy.kt
            LateGame.kt
            LiveOps.kt
            MainActivity.kt
            ManagerGroup01Art.kt
            ManagerGroup02Art.kt
            ManagerGroup03Art.kt
            Managers.kt
            MasteryCrownShimmer.kt
            MetaSpriteArt.kt
            Monetization.kt
            MotionQuality.kt
            OfflineProgress.kt
            OnboardingArt.kt
            OrbitalIonTrail.kt
            PhaseDistortion.kt
            PlayBillingGateway.kt
            PowerCoreTapImpact.kt
            PremiumGameFeel.kt
            PremiumGameFeelOverlay.kt
            PremiumGameFeelV2.kt
            PremiumGameUiV2.kt
            PremiumGoalsCenter.kt
            PremiumMotion.kt
            PremiumSfx.kt
            PremiumSprites.kt
            PremiumUiCompat.kt
            PrivacyConsentManager.kt
            PrivacyPolicy.kt
            ProgressionSystems.kt
            PurchaseCreditLedger.kt
            PurchaseImpactVfx.kt
            PurchaseRecovery.kt
            Retention.kt
            ReviewedCharacterLayer.kt
            ReviewedMachineLayer.kt
            ReviewedTerrainLayer.kt
            RewardedController.kt
            RewardRequestGate.kt
            SfxRuntime.kt
            SingularityLensPulse.kt
            StellarFlare.kt
            UpgradeConstructionFlash.kt
            UpgradeProgression.kt
            UpgradeTreeScreen.kt
            UpgradeTreeUi.kt
            ViralSystems.kt
            ViralUi.kt
            WorldBusinessVisual.kt
            WorldMoneyFormat.kt
            WorldSpriteRegistry.kt
            WorldTrafficArt.kt
  test/
    java/
      com/
        zerotoempire/
          game/
            AmbientTrafficMotionTest.kt
            BillingDiagnosticsTest.kt
            BillingFailurePolicyTest.kt
            BulkPurchaseTest.kt
            CanonicalBusinessRasterTest.kt
            CanonicalBusinessTierTest.kt
            CanonicalCharacterRasterTest.kt
            CanonicalFxRasterTest.kt
            ChallengeRotationTest.kt
            CinematicRuntimeTransitionPolicyTest.kt
            ContentUnlocksTest.kt
            DynastyProgressionTest.kt
            EconomyInvariantTest.kt
            EconomyMathBoundaryTest.kt
            EconomySafetyTest.kt
            EconomyTest.kt
            EmpireNumberFormatTest.kt
            EndgameContentTest.kt
            EndgameProgressionTest.kt
            IdentitySystemsTest.kt
            InterstitialPolicyTest.kt
            LateGameTest.kt
            LongCampaignInvariantTest.kt
            NumericStabilityTest.kt
            OfflineAutomationTest.kt
            OfflineProgressBoundaryTest.kt
            OfflineProgressLifecycleTest.kt
            OfflineTemporalTest.kt
            PlayableFlowTest.kt
            PlayBillingGatewayInvariantTest.kt
            PreDeviceSmokeInvariantTest.kt
            PrestigeCycleTest.kt
            PrestigeResetTest.kt
            ProgressionCycleTest.kt
            PurchaseCreditLedgerTest.kt
            PurchaseRecoveryTest.kt
            ReviewedTerrainLayerTest.kt
            RewardRequestGateTest.kt
            RuntimePerformanceInvariantTest.kt
            StoreProductResolverTest.kt
            UpgradeProgressionTest.kt
            WeeklyChallengeTest.kt
build.gradle.kts
```

# Files

## File: src/debug/java/com/zerotoempire/game/SmokeSeedReceiver.kt
```kotlin
package com.zerotoempire.game

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.runBlocking

/** Debug-only state seeder used by the emulator functional smoke. */
class SmokeSeedReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action != ACTION_SEED) return
        val requestedCash = intent.getLongExtra(EXTRA_CASH, DEFAULT_CASH).toDouble()
            .coerceIn(0.0, EconomyMath.MAX_VALUE)

        runBlocking(Dispatchers.IO) {
            val repository = GameRepository(context.applicationContext)
            val save = repository.load()
            val seededCash = maxOf(save.state.cash, requestedCash)
            repository.save(
                s = save.state.copy(
                    cash = seededCash,
                    lifetimeCash = maxOf(save.state.lifetimeCash, seededCash)
                ),
                m = save.meta.copy(onboardingCompleted = true),
                creditedPurchaseTokens = save.creditedPurchaseTokens
            )
        }
    }

    companion object {
        const val ACTION_SEED = "com.zerotoempire.game.DEBUG_SMOKE_SEED"
        const val EXTRA_CASH = "cash"
        const val DEFAULT_CASH = 3_000L
    }
}
```

## File: src/main/java/com/zerotoempire/game/AdaptiveMusic.kt
```kotlin
package com.zerotoempire.game

import android.content.Context
import android.media.AudioAttributes
import android.media.AudioFocusRequest
import android.media.AudioFormat
import android.media.AudioManager
import android.media.AudioTrack
import java.util.concurrent.atomic.AtomicBoolean
import kotlin.concurrent.thread
import kotlin.math.PI
import kotlin.math.sin

/** Resource-free adaptive soundtrack synthesized at runtime. */
class AdaptiveMusicEngine(context: Context) {
    private val running = AtomicBoolean(false)
    private val foreground = AtomicBoolean(true)
    private val hasAudioFocus = AtomicBoolean(false)
    @Volatile private var intensity = 0
    @Volatile private var volume = .18f
    @Volatile private var focusVolumeMultiplier = 1f
    private var worker: Thread? = null

    private val audioAttributes = AudioAttributes.Builder()
        .setUsage(AudioAttributes.USAGE_GAME)
        .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
        .build()

    private val audioManager = context.applicationContext.getSystemService(Context.AUDIO_SERVICE) as AudioManager
    private val focusRequest = AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN)
        .setAudioAttributes(audioAttributes)
        .setOnAudioFocusChangeListener { change ->
            when (change) {
                AudioManager.AUDIOFOCUS_GAIN -> {
                    focusVolumeMultiplier = 1f
                    hasAudioFocus.set(true)
                    if (running.get() && foreground.get()) runCatching { track.play() }
                }
                AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK -> {
                    // Keep rendering and playing, but make room for short system/navigation audio.
                    // This avoids flushing the stream for every notification and resumes seamlessly.
                    focusVolumeMultiplier = .25f
                }
                AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> {
                    // Preserve the short queued buffer so a temporary interruption resumes cleanly.
                    // The render loop sleeps while focus is absent, so no additional audio is queued.
                    focusVolumeMultiplier = 1f
                    hasAudioFocus.set(false)
                    runCatching { track.pause() }
                }
                AudioManager.AUDIOFOCUS_LOSS -> {
                    focusVolumeMultiplier = 1f
                    hasAudioFocus.set(false)
                    runCatching { track.pause() }
                    runCatching { track.flush() }
                }
            }
        }
        .build()

    private val sampleRate = 22_050
    private val bufferSize = AudioTrack.getMinBufferSize(
        sampleRate,
        AudioFormat.CHANNEL_OUT_STEREO,
        AudioFormat.ENCODING_PCM_16BIT
    ).coerceAtLeast(4096)

    private val track = AudioTrack.Builder()
        .setAudioAttributes(audioAttributes)
        .setAudioFormat(
            AudioFormat.Builder()
                .setSampleRate(sampleRate)
                .setEncoding(AudioFormat.ENCODING_PCM_16BIT)
                .setChannelMask(AudioFormat.CHANNEL_OUT_STEREO)
                .build()
        )
        .setBufferSizeInBytes(bufferSize * 2)
        .setTransferMode(AudioTrack.MODE_STREAM)
        .build()

    fun start() {
        if (!running.compareAndSet(false, true)) return
        foreground.set(true)
        requestAudioFocusAndPlay()
        worker = thread(name = "EmpireAdaptiveMusic", isDaemon = true) { renderLoop() }
    }

    fun resumePlayback() {
        if (!running.get()) return
        foreground.set(true)
        requestAudioFocusAndPlay()
    }

    fun pausePlayback() {
        if (!running.get()) return
        foreground.set(false)
        focusVolumeMultiplier = 1f
        hasAudioFocus.set(false)
        runCatching { track.pause() }
        runCatching { track.flush() }
        runCatching { audioManager.abandonAudioFocusRequest(focusRequest) }
    }

    fun setEmpireLevel(level: Int) { intensity = level.coerceIn(0, 10) }
    fun setVolume(value: Float) { volume = value.coerceIn(0f, .35f) }

    fun release() {
        foreground.set(false)
        focusVolumeMultiplier = 1f
        hasAudioFocus.set(false)
        running.set(false)
        runCatching { audioManager.abandonAudioFocusRequest(focusRequest) }
        worker?.join(250)
        worker = null
        runCatching { track.pause() }
        runCatching { track.flush() }
        track.release()
    }

    private fun requestAudioFocusAndPlay() {
        val granted = runCatching { audioManager.requestAudioFocus(focusRequest) }
            .getOrDefault(AudioManager.AUDIOFOCUS_REQUEST_FAILED) == AudioManager.AUDIOFOCUS_REQUEST_GRANTED
        focusVolumeMultiplier = 1f
        hasAudioFocus.set(granted)
        if (granted && foreground.get()) runCatching { track.play() }
    }

    private fun renderLoop() {
        val frames = (bufferSize / 4).coerceAtLeast(512)
        val pcm = ShortArray(frames * 2)
        var sampleCursor = 0L
        while (running.get()) {
            if (!foreground.get() || !hasAudioFocus.get()) {
                try { Thread.sleep(50) } catch (_: InterruptedException) { Thread.currentThread().interrupt() }
                continue
            }
            val tier = intensity
            val root = when (tier) {
                0, 1 -> 55.0
                2, 3 -> 65.41
                4, 5 -> 73.42
                6, 7 -> 82.41
                else -> 98.0
            }
            val bpm = 68.0 + tier * 2.2
            for (frame in 0 until frames) {
                val t = sampleCursor.toDouble() / sampleRate
                val beat = (t * bpm / 60.0) % 4.0
                val pulse = if (beat % 1.0 < .12) (1.0 - (beat % 1.0) / .12) else 0.0
                val pad = sin(2 * PI * root * t) * .32 +
                    sin(2 * PI * root * 1.5 * t) * .18 +
                    sin(2 * PI * root * 2.0 * t) * .10
                val shimmer = if (tier >= 4) sin(2 * PI * root * 4.0 * t) * .06 else 0.0
                val drive = if (tier >= 7) sin(2 * PI * root * .5 * t) * pulse * .22 else pulse * .08
                val effectiveVolume = volume.toDouble() * focusVolumeMultiplier
                val amp = effectiveVolume * (pad + shimmer + drive)
                val left = (amp * 26_000.0).coerceIn(-32767.0, 32767.0).toInt().toShort()
                val rightPhase = sin(2 * PI * root * 1.0025 * t) * .03 * effectiveVolume
                val right = ((amp + rightPhase) * 26_000.0).coerceIn(-32767.0, 32767.0).toInt().toShort()
                pcm[frame * 2] = left
                pcm[frame * 2 + 1] = right
                sampleCursor++
            }
            if (foreground.get() && hasAudioFocus.get()) {
                track.write(pcm, 0, pcm.size, AudioTrack.WRITE_BLOCKING)
            }
        }
    }
}

object GameMusicBus {
    @Volatile private var engine: AdaptiveMusicEngine? = null

    @Synchronized
    fun attach(engine: AdaptiveMusicEngine) {
        this.engine?.release()
        this.engine = engine
        engine.start()
    }

    fun resume() = engine?.resumePlayback() ?: Unit
    fun pause() = engine?.pausePlayback() ?: Unit
    fun setEmpireLevel(level: Int) = engine?.setEmpireLevel(level) ?: Unit
    fun setVolume(volume: Float) = engine?.setVolume(volume) ?: Unit

    @Synchronized
    fun detach(expected: AdaptiveMusicEngine) {
        if (engine !== expected) return
        engine?.release()
        engine = null
    }

    @Synchronized
    fun detach() {
        engine?.release()
        engine = null
    }
}
```

## File: src/main/java/com/zerotoempire/game/AdMobInterstitialGateway.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import com.google.android.gms.ads.AdError
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.FullScreenContentCallback
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback

class AdMobInterstitialGateway(private val context: Context) {
    @Volatile private var ad: InterstitialAd? = null
    @Volatile private var loading = false
    @Volatile private var enabled = false
    @Volatile private var requestGeneration = 0L

    fun setEnabled(value: Boolean) {
        if (enabled == value) return
        enabled = value
        if (!value) {
            requestGeneration += 1L
            ad = null
            loading = false
        }
    }

    fun preload() {
        if (!enabled || loading || ad != null || BuildConfig.INTERSTITIAL_AD_UNIT_ID.isBlank()) return
        loading = true
        val generation = requestGeneration
        InterstitialAd.load(
            context,
            BuildConfig.INTERSTITIAL_AD_UNIT_ID,
            AdRequest.Builder().build(),
            object : InterstitialAdLoadCallback() {
                override fun onAdLoaded(interstitialAd: InterstitialAd) {
                    if (!enabled || generation != requestGeneration) return
                    loading = false
                    ad = interstitialAd
                }

                override fun onAdFailedToLoad(error: LoadAdError) {
                    if (generation != requestGeneration) return
                    loading = false
                    ad = null
                }
            }
        )
    }

    fun isReady(): Boolean = enabled && ad != null

    fun show(
        activity: Activity,
        onShown: () -> Unit = {},
        onClosed: () -> Unit = {}
    ) {
        if (!enabled || !activity.canHostFullScreenAd()) {
            onClosed()
            return
        }
        val current = ad ?: run {
            preload()
            onClosed()
            return
        }
        ad = null
        current.fullScreenContentCallback = object : FullScreenContentCallback() {
            override fun onAdShowedFullScreenContent() {
                onShown()
            }

            override fun onAdDismissedFullScreenContent() {
                preload()
                onClosed()
            }

            override fun onAdFailedToShowFullScreenContent(adError: AdError) {
                preload()
                onClosed()
            }
        }
        runCatching { current.show(activity) }
            .onFailure {
                preload()
                onClosed()
            }
    }
}
```

## File: src/main/java/com/zerotoempire/game/AdMobRewardedGateway.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.FullScreenContentCallback
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.MobileAds
import com.google.android.gms.ads.rewarded.RewardedAd
import com.google.android.gms.ads.rewarded.RewardedAdLoadCallback

class AdMobRewardedGateway(private val context: Context) : RewardedAdGateway {
    @Volatile private var rewardedAd: RewardedAd? = null
    @Volatile private var loading = false
    @Volatile private var mobileAdsReady = false
    @Volatile private var initializing = false
    @Volatile private var enabled = false
    @Volatile private var requestGeneration = 0L

    @Synchronized
    override fun setEnabled(enabled: Boolean) {
        if (this.enabled == enabled) return
        this.enabled = enabled
        if (!enabled) {
            requestGeneration += 1L
            rewardedAd = null
            loading = false
        }
    }

    /**
     * Preload is intentionally the first point that may initialize the ads SDK.
     * CommerceRoot only enables this gateway after the privacy gate allows ad requests.
     */
    @Synchronized
    override fun preload() {
        if (!enabled || loading || rewardedAd != null || BuildConfig.REWARDED_AD_UNIT_ID.isBlank()) return
        if (!mobileAdsReady) {
            if (initializing) return
            initializing = true
            val generation = requestGeneration
            MobileAds.initialize(context) {
                synchronized(this) {
                    initializing = false
                    mobileAdsReady = true
                }
                if (enabled && generation == requestGeneration) preload()
            }
            return
        }

        loading = true
        val generation = requestGeneration
        RewardedAd.load(
            context,
            BuildConfig.REWARDED_AD_UNIT_ID,
            AdRequest.Builder().build(),
            object : RewardedAdLoadCallback() {
                override fun onAdLoaded(ad: RewardedAd) {
                    if (!enabled || generation != requestGeneration) return
                    loading = false
                    rewardedAd = ad
                }

                override fun onAdFailedToLoad(error: LoadAdError) {
                    if (generation != requestGeneration) return
                    loading = false
                    rewardedAd = null
                }
            }
        )
    }

    override fun isReady(): Boolean = enabled && rewardedAd != null

    override fun show(
        activity: Activity,
        placement: RewardPlacement,
        onReward: () -> Unit,
        onClosed: () -> Unit
    ) {
        if (!enabled || !activity.canHostFullScreenAd()) {
            onClosed()
            return
        }
        val ad = rewardedAd ?: run {
            preload()
            onClosed()
            return
        }
        rewardedAd = null
        var rewarded = false
        var closed = false
        fun closeOnce() {
            if (closed) return
            closed = true
            preload()
            onClosed()
        }
        ad.fullScreenContentCallback = object : FullScreenContentCallback() {
            override fun onAdDismissedFullScreenContent() = closeOnce()

            override fun onAdFailedToShowFullScreenContent(adError: com.google.android.gms.ads.AdError) = closeOnce()
        }
        runCatching {
            ad.show(activity) {
                if (!rewarded) {
                    rewarded = true
                    onReward()
                }
            }
        }.onFailure { closeOnce() }
    }
}
```

## File: src/main/java/com/zerotoempire/game/Analytics.kt
```kotlin
package com.zerotoempire.game

/** Small analytics boundary: no vendor SDK leaks into gameplay code. */
interface GameAnalytics {
    fun track(event: GameEvent)
}

sealed interface GameEvent {
    data class SessionStarted(val returningPlayer: Boolean) : GameEvent
    data class BusinessPurchased(val businessId: Int, val newLevel: Int) : GameEvent
    data class ManagerHired(val businessId: Int) : GameEvent
    data class PrestigeUsed(val pointsEarned: Int, val runSeconds: Long) : GameEvent
    data class RewardedAdCompleted(val placement: RewardPlacement) : GameEvent
    data class MissionClaimed(val missionId: String) : GameEvent
    data class TutorialStep(val step: Int) : GameEvent
}

object NoOpAnalytics : GameAnalytics {
    override fun track(event: GameEvent) = Unit
}
```

## File: src/main/java/com/zerotoempire/game/AscendantCityWorld.kt
```kotlin
package com.zerotoempire.game

import android.provider.Settings
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

/** World-first Empire surface defined by AAA_WORLD_SPRITE_BIBLE.md.
 * Economy and save behavior remain delegated to the existing GameViewModel.
 */
@Composable
internal fun AscendantCityEmpireWorld(vm: GameViewModel, state: GameState, buyMode: BuyMode) {
    val visible = remember(state.businesses, state.lifetimeCash) { ContentUnlocks.visibleBusinesses(state) }
    val era = EmpireEras.current(state.lifetimeCash)
    LazyColumn(modifier = Modifier.fillMaxSize(), verticalArrangement = Arrangement.spacedBy(10.dp)) {
        item { AscendantCompactHud(state) }
        item {
            Box(Modifier.fillMaxWidth().height(620.dp)) {
                AscendantCityStage(era.index, Modifier.fillMaxSize())
                Row(Modifier.fillMaxWidth().padding(horizontal = 12.dp, vertical = 14.dp), horizontalArrangement = Arrangement.SpaceBetween) {
                    EraChip(era.index + 1, era.name)
                    Surface(color = EmpireColors.DeepSpace.copy(alpha = .82f), shape = RoundedCornerShape(14.dp)) {
                        Text("${visible.size}/14 DISTRICTS", Modifier.padding(horizontal = 10.dp, vertical = 7.dp), color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Black)
                    }
                }
                visible.take(4).getOrNull(0)?.let { AscendantHeroLot(vm, it, state, buyMode, Modifier.align(Alignment.TopStart).padding(start = 14.dp, top = 142.dp), false) }
                visible.take(4).getOrNull(1)?.let { AscendantHeroLot(vm, it, state, buyMode, Modifier.align(Alignment.TopEnd).padding(end = 14.dp, top = 238.dp), true) }
                visible.take(4).getOrNull(2)?.let { AscendantHeroLot(vm, it, state, buyMode, Modifier.align(Alignment.TopStart).padding(start = 14.dp, top = 334.dp), false) }
                visible.take(4).getOrNull(3)?.let { AscendantHeroLot(vm, it, state, buyMode, Modifier.align(Alignment.TopEnd).padding(end = 14.dp, top = 430.dp), true) }
                AscendantCorePlaza(state = state, tap = vm::tap, modifier = Modifier.align(Alignment.BottomCenter).padding(bottom = 12.dp))
            }
        }
        item { PurchaseModeRailWorld(vm, buyMode) }
        item { Text("DISTRICT NETWORK", Modifier.padding(horizontal = 16.dp, vertical = 4.dp), color = EmpireColors.TextSecondary, fontSize = 10.sp, fontWeight = FontWeight.Black, letterSpacing = 1.5.sp) }
        visible.drop(4).forEach { business -> item(key = business.id) { AscendantWorldLot(vm, business, state, buyMode, business.id) } }
        item { Spacer(Modifier.height(22.dp)) }
    }
}

@Composable
private fun AscendantCompactHud(state: GameState) {
    Surface(color = EmpireColors.Surface.copy(alpha = .94f), shape = RoundedCornerShape(0.dp)) {
        Row(Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 10.dp), verticalAlignment = Alignment.CenterVertically) {
            Column(Modifier.weight(1f)) {
                Text("CAPITAL", color = EmpireColors.TextSecondary, fontSize = 8.sp, fontWeight = FontWeight.Bold, letterSpacing = 1.2.sp)
                Text(moneyV2(state.cash), color = EmpireColors.TextPrimary, fontSize = 24.sp, fontWeight = FontWeight.Black)
            }
            HudChip("+${moneyV2(state.incomePerSecond)}/s", EmpireColors.Success); Spacer(Modifier.width(6.dp)); HudChip("◆ ${state.gems}", EmpireColors.Violet); Spacer(Modifier.width(6.dp)); HudChip("×${String.format("%.1f", state.boostMultiplier)}", EmpireColors.Gold)
        }
    }
}

@Composable private fun HudChip(text: String, accent: Color) { Surface(color = accent.copy(alpha = .11f), shape = RoundedCornerShape(12.dp), modifier = Modifier.border(1.dp, accent.copy(alpha = .25f), RoundedCornerShape(12.dp))) { Text(text, Modifier.padding(horizontal = 8.dp, vertical = 7.dp), color = accent, fontSize = 10.sp, fontWeight = FontWeight.Black) } }
@Composable private fun EraChip(number: Int, name: String) { Surface(color = EmpireColors.DeepSpace.copy(alpha = .88f), shape = RoundedCornerShape(15.dp), modifier = Modifier.border(1.dp, EmpireColors.Gold.copy(alpha = .25f), RoundedCornerShape(15.dp))) { Column(Modifier.padding(horizontal = 11.dp, vertical = 7.dp)) { Text("ERA $number", color = EmpireColors.Gold, fontSize = 8.sp, fontWeight = FontWeight.Black, letterSpacing = 1.2.sp); Text(name.uppercase(), color = EmpireColors.TextPrimary, fontSize = 11.sp, fontWeight = FontWeight.Black) } } }

@Composable
private fun AscendantCityStage(eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    var ambientFrame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        if (reducedMotion) {
            ambientFrame = 0
        } else {
            while (true) {
                delay(100)
                ambientFrame = (ambientFrame + 1) % 10_000
            }
        }
    }

    Box(modifier.background(Brush.verticalGradient(listOf(Color(0xFF07101C), Color(0xFF101B24), Color(0xFF080D13))))) {
        EraVistaAAA(eraIndex, Modifier.fillMaxSize())
        Canvas(Modifier.fillMaxSize()) {
            val w=size.width; val h=size.height
            repeat(7){i-> val bw=w*(.065f+(i%3)*.018f); val bh=h*(.07f+(i%4)*.024f); val x=w*(.03f+i*.145f); val y=h*.31f-bh; drawRect(Color(0xB510171D),Offset(x,y),Size(bw,bh)); drawRect(EmpireColors.Gold.copy(alpha=.12f),Offset(x+bw*.18f,y+bh*.28f),Size(bw*.12f,3f)); drawRect(EmpireColors.Cyan.copy(alpha=.10f),Offset(x+bw*.54f,y+bh*.48f),Size(bw*.16f,3f)) }
            val ground=Path().apply{moveTo(0f,h*.30f);lineTo(w,h*.17f);lineTo(w,h);lineTo(0f,h);close()}; drawPath(ground,Color(0xE5141B20)); drawLine(Color.White.copy(alpha=.06f),Offset(0f,h*.30f),Offset(w,h*.17f),2f)
            val road=Path().apply{moveTo(w*.36f,h*.30f);lineTo(w*.57f,h*.26f);lineTo(w*.88f,h);lineTo(w*.18f,h);close()}; drawPath(road,Color(0xFF1B2227)); drawLine(Color.White.copy(alpha=.05f),Offset(w*.37f,h*.31f),Offset(w*.20f,h),2f); drawLine(Color.White.copy(alpha=.05f),Offset(w*.56f,h*.28f),Offset(w*.86f,h),2f); drawLine(EmpireColors.Gold.copy(alpha=.34f),Offset(w*.47f,h*.31f),Offset(w*.53f,h*.95f),3f)
            repeat(4){i->val y=h*(.42f+i*.145f);drawLine(EmpireColors.Cyan.copy(alpha=.20f),Offset(w*.10f,y),Offset(w*.50f,h*.91f),2f);drawLine(EmpireColors.Cyan.copy(alpha=.15f),Offset(w*.90f,y-h*.025f),Offset(w*.50f,h*.91f),2f)}
            repeat(3){i->val y=h*(.39f+i*.19f);drawLine(Color(0xFF6F5B3C).copy(alpha=.24f),Offset(0f,y),Offset(w*.22f,y-h*.025f),5f);drawCircle(EmpireColors.Gold.copy(alpha=.18f),6f,Offset(w*.22f,y-h*.025f))}
            repeat(4){i->val y=h*(.34f+i*.155f);val left=i%2==0;val x=if(left)w*.035f else w*.595f;val pad=Path().apply{moveTo(x,y+h*.035f);lineTo(x+w*.25f,y);lineTo(x+w*.39f,y+h*.045f);lineTo(x+w*.13f,y+h*.083f);close()};drawPath(pad,Color(0xE5263034));drawPath(pad,EmpireColors.Cyan.copy(alpha=.12f),style=Stroke(2f));drawLine(EmpireColors.Gold.copy(alpha=.18f),Offset(x+w*.06f,y+h*.056f),Offset(x+w*.31f,y+h*.02f),3f)}
            drawRect(Color(0xFF0E151A),Offset(0f,h*.90f),Size(w*.16f,h*.10f));drawRect(Color(0xFF0E151A),Offset(w*.86f,h*.88f),Size(w*.14f,h*.12f))
        }
        ReviewedTerrainLayer(eraIndex, Modifier.fillMaxSize())
        ReviewedMachineLayer(eraIndex, Modifier.fillMaxSize())
        ReviewedCharacterLayer(
            eraIndex = eraIndex,
            worldFrame = ambientFrame,
            reducedMotion = reducedMotion,
            modifier = Modifier.fillMaxSize(),
        )
        ReviewedWorldTraffic(
            worldFrame = ambientFrame,
            reducedMotion = reducedMotion,
            modifier = Modifier.fillMaxSize(),
        )
        Box(Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(Color.Transparent,Color.Transparent,EmpireColors.Void.copy(alpha=.24f)))))
    }
}

@Composable
private fun AscendantHeroLot(vm: GameViewModel,business: Business,state: GameState,mode: BuyMode,modifier: Modifier,alignRight: Boolean){
 val quote=vm.bulkQuote(business.id,mode);val affordable=quote.count>0&&state.cash>=quote.cost;val income=state.businessIncome(business)*state.permanentIncomeMultiplier*state.boostMultiplier*state.eventMultiplier;val accent=if(affordable)EmpireColors.Gold else EmpireColors.Cyan
 Column(modifier.width(178.dp).clickable(enabled=affordable,role=Role.Button){vm.buyBulk(business.id,mode)},horizontalAlignment=if(alignRight)Alignment.End else Alignment.Start){Box(Modifier.fillMaxWidth().height(92.dp),contentAlignment=if(alignRight)Alignment.CenterEnd else Alignment.CenterStart){Canvas(Modifier.fillMaxSize()){val baseY=size.height*.76f;val left=if(alignRight)size.width*.18f else 0f;drawOval(Color.Black.copy(alpha=.34f),Offset(left,baseY),Size(size.width*.76f,size.height*.18f));drawLine(accent.copy(alpha=.22f),Offset(left+8f,baseY+8f),Offset(left+size.width*.65f,baseY+2f),3f)};WorldBusinessVisual(business.id,business.level,88.dp)};Surface(color=EmpireColors.DeepSpace.copy(alpha=.84f),shape=RoundedCornerShape(12.dp),modifier=Modifier.border(1.dp,accent.copy(alpha=.28f),RoundedCornerShape(12.dp))){Row(Modifier.padding(horizontal=8.dp,vertical=6.dp),verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(business.name,color=EmpireColors.TextPrimary,fontSize=10.sp,fontWeight=FontWeight.Black,maxLines=1,overflow=TextOverflow.Ellipsis);Text("LV ${business.level} • ${moneyV2(income)}/s",color=EmpireColors.Cyan,fontSize=8.sp,fontWeight=FontWeight.Bold)};Spacer(Modifier.width(5.dp));Column(horizontalAlignment=Alignment.End){Text(if(quote.count>0)"+${quote.count}" else "—",color=if(affordable)EmpireColors.GoldBright else EmpireColors.TextSecondary,fontSize=9.sp,fontWeight=FontWeight.Black);Text(if(quote.count>0)moneyV2(quote.cost) else "LOCKED",color=EmpireColors.TextSecondary,fontSize=7.sp,fontWeight=FontWeight.Bold)}}}}
}

@Composable private fun AscendantWorldLot(vm:GameViewModel,business:Business,state:GameState,mode:BuyMode,row:Int){val quote=vm.bulkQuote(business.id,mode);val affordable=quote.count>0&&state.cash>=quote.cost;val income=state.businessIncome(business)*state.permanentIncomeMultiplier*state.boostMultiplier*state.eventMultiplier;val alignRight=row%2!=0;Row(Modifier.fillMaxWidth().padding(horizontal=14.dp),horizontalArrangement=if(alignRight)Arrangement.End else Arrangement.Start,verticalAlignment=Alignment.CenterVertically){Surface(color=EmpireColors.Surface.copy(alpha=.94f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth(.96f).border(1.dp,if(affordable)EmpireColors.Gold.copy(alpha=.38f) else Color.White.copy(alpha=.07f),RoundedCornerShape(18.dp)).clickable(enabled=affordable,role=Role.Button){vm.buyBulk(business.id,mode)}){Row(Modifier.padding(horizontal=10.dp,vertical=9.dp),verticalAlignment=Alignment.CenterVertically){Box(Modifier.size(68.dp),contentAlignment=Alignment.Center){WorldBusinessVisual(business.id,business.level,66.dp)};Spacer(Modifier.width(9.dp));Column(Modifier.weight(1f)){Text(business.name,color=EmpireColors.TextPrimary,fontSize=15.sp,fontWeight=FontWeight.Black,maxLines=1,overflow=TextOverflow.Ellipsis);Text("LV ${business.level} • ${moneyV2(income)}/s",color=EmpireColors.Cyan,fontSize=9.sp,fontWeight=FontWeight.Bold)};Column(horizontalAlignment=Alignment.End){Text(if(quote.count>0)"+${quote.count}" else "—",color=if(affordable)EmpireColors.GoldBright else EmpireColors.TextSecondary,fontSize=11.sp,fontWeight=FontWeight.Black);Text(if(quote.count>0)moneyV2(quote.cost) else "LOCKED",color=EmpireColors.TextSecondary,fontSize=8.sp,fontWeight=FontWeight.Bold)}}}}}

@Composable
private fun AscendantCorePlaza(state:GameState,tap:()->Unit,modifier:Modifier=Modifier){
 val context=LocalContext.current
 val cyanPulseSheet=remember{ImageBitmap.imageResource(context.resources,R.drawable.zte_fx_05_final)}
 val pulseSheet=remember{ImageBitmap.imageResource(context.resources,R.drawable.zte_fx_06_final)}
 val coreSprites=remember{listOf(
  ImageBitmap.imageResource(context.resources,R.drawable.zte_power_core_t0_final),
  ImageBitmap.imageResource(context.resources,R.drawable.zte_power_core_t1_final),
  ImageBitmap.imageResource(context.resources,R.drawable.zte_power_core_t2_final),
  ImageBitmap.imageResource(context.resources,R.drawable.zte_power_core_t3_final),
  ImageBitmap.imageResource(context.resources,R.drawable.zte_power_core_t4_final),
  ImageBitmap.imageResource(context.resources,R.drawable.zte_power_core_t5_final),
  ImageBitmap.imageResource(context.resources,R.drawable.zte_power_core_t6_final),
 )}
 val coreIndex=EmpireEras.current(state.lifetimeCash).index.coerceIn(0,6)
 val coreSprite=coreSprites[coreIndex]
 val motionEnabled=remember(context){Settings.Global.getFloat(context.contentResolver,Settings.Global.ANIMATOR_DURATION_SCALE,1f)>0f}
 var cyanFrame by remember{mutableIntStateOf(0)};var pulseToken by remember{mutableIntStateOf(0)};var pulseFrame by remember{mutableIntStateOf(-1)}
 LaunchedEffect(motionEnabled){if(!motionEnabled){cyanFrame=3}else{while(true){for(frame in 0 until 8){cyanFrame=frame;delay(110)};delay(440)}}}
 LaunchedEffect(pulseToken){if(pulseToken==0)return@LaunchedEffect;if(!motionEnabled){pulseFrame=3;delay(80)}else{for(frame in 0 until 8){pulseFrame=frame;delay(42)}};pulseFrame=-1}
 Box(modifier.fillMaxWidth().height(118.dp),contentAlignment=Alignment.Center){
  Box(Modifier.size(118.dp).background(Brush.radialGradient(listOf(EmpireColors.Gold.copy(alpha=.22f),EmpireColors.Cyan.copy(alpha=.08f),Color.Transparent)),CircleShape))
  Canvas(Modifier.size(110.dp)){val frame=cyanFrame.coerceIn(0,7);val side=minOf(size.width,size.height).toInt();drawImage(image=cyanPulseSheet,srcOffset=IntOffset((frame%4)*128,(frame/4)*128),srcSize=IntSize(128,128),dstOffset=IntOffset(((size.width-side)/2f).toInt(),((size.height-side)/2f).toInt()),dstSize=IntSize(side,side))}
  Surface(color=EmpireColors.DeepSpace.copy(alpha=.42f),shape=CircleShape,modifier=Modifier.size(98.dp).border(2.dp,EmpireColors.Gold.copy(alpha=.48f),CircleShape).clickable(role=Role.Button){pulseToken+=1;tap()}){
   Box(contentAlignment=Alignment.Center){Canvas(Modifier.size(88.dp)){val side=minOf(size.width,size.height).toInt();drawImage(image=coreSprite,srcOffset=IntOffset.Zero,srcSize=IntSize(coreSprite.width,coreSprite.height),dstOffset=IntOffset(((size.width-side)/2f).toInt(),((size.height-side)/2f).toInt()),dstSize=IntSize(side,side))}}
  }
  if(pulseFrame>=0){Canvas(Modifier.size(118.dp)){val frame=pulseFrame.coerceIn(0,7);val side=minOf(size.width,size.height).toInt();drawImage(image=pulseSheet,srcOffset=IntOffset((frame%4)*128,(frame/4)*128),srcSize=IntSize(128,128),dstOffset=IntOffset(((size.width-side)/2f).toInt(),((size.height-side)/2f).toInt()),dstSize=IntSize(side,side))}}
  Surface(color=EmpireColors.DeepSpace.copy(alpha=.90f),shape=RoundedCornerShape(10.dp),modifier=Modifier.align(Alignment.BottomCenter)){Text("POWER CORE  +${moneyV2(state.tapValue)}",Modifier.padding(horizontal=9.dp,vertical=5.dp),color=EmpireColors.GoldBright,fontSize=9.sp,fontWeight=FontWeight.Black)}
 }
}

@Composable private fun PurchaseModeRailWorld(vm:GameViewModel,selected:BuyMode){val modes=listOf(BuyMode.X1 to "×1",BuyMode.X10 to "×10",BuyMode.X25 to "×25",BuyMode.MILESTONE to "NEXT",BuyMode.MAX to "MAX");Row(Modifier.fillMaxWidth().padding(horizontal=14.dp),horizontalArrangement=Arrangement.spacedBy(5.dp)){modes.forEach{(mode,label)->val active=mode==selected;Surface(color=if(active)EmpireColors.Violet else EmpireColors.Surface,shape=RoundedCornerShape(12.dp),modifier=Modifier.weight(1f).height(42.dp).clickable{vm.setBuyMode(mode)}){Box(contentAlignment=Alignment.Center){Text(label,color=if(active)Color.White else EmpireColors.TextSecondary,fontSize=9.sp,fontWeight=FontWeight.Black)}}}}}
```

## File: src/main/java/com/zerotoempire/game/AscensionAdvisor.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import java.util.Locale

@Composable
fun AscensionAdvisor(state: GameState, modifier: Modifier = Modifier) {
    val total = Progression.prestigeReward(state.lifetimeCash)
    val gain = (total - state.prestigePoints).coerceAtLeast(0)
    if (gain <= 0) return

    val after = state.copy(prestigePoints = total)
    val beforePower = state.prestigeMultiplier * state.legacyMasteryMultiplier
    val afterPower = after.prestigeMultiplier * after.legacyMasteryMultiplier
    val improvement = ((afterPower / beforePower) - 1.0).coerceAtLeast(0.0)
    val recommended = LateGame.recommendedPrestige(state.prestigePoints, state.lifetimeCash)

    Surface(
        modifier = modifier.fillMaxWidth(),
        color = EmpireColors.Violet.copy(alpha = if (recommended) .22f else .12f),
        shape = RoundedCornerShape(16.dp),
        shadowElevation = if (recommended) 10.dp else 3.dp
    ) {
        Row(
            Modifier.padding(horizontal = 12.dp, vertical = 9.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Column(Modifier.weight(1f)) {
                Text(
                    if (recommended) "ASCENSION READY" else "ASCENSION CHARGING",
                    color = if (recommended) EmpireColors.Gold else EmpireColors.TextSecondary,
                    fontWeight = FontWeight.Black,
                    fontSize = 10.sp
                )
                Text(
                    "+$gain LEGACY  •  +${String.format(Locale.US, "%.0f", improvement * 100)}% permanent power",
                    color = EmpireColors.TextPrimary,
                    fontWeight = FontWeight.Bold,
                    fontSize = 10.sp
                )
            }
            Spacer(Modifier.width(10.dp))
            Text(
                "×${String.format(Locale.US, "%.2f", beforePower)} → ×${String.format(Locale.US, "%.2f", afterPower)}",
                color = EmpireColors.Cyan,
                fontWeight = FontWeight.Black,
                fontSize = 10.sp
            )
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/BillingDiagnostics.kt
```kotlin
package com.zerotoempire.game

import android.util.Log
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.atomic.AtomicInteger

enum class BillingOperation { CONNECT, PURCHASE_UPDATE, PRODUCT_LOOKUP, LAUNCH, RESTORE, ACKNOWLEDGE, CONSUME, RECOVER_CONSUMABLE }

data class BillingDiagnostic(
    val operation: BillingOperation,
    val responseCode: Int,
    val failureKind: BillingFailureKind
) {
    fun toLogLine(): String = "operation=$operation responseCode=$responseCode category=$failureKind"
}

data class BillingDiagnosticCount(val diagnostic: BillingDiagnostic, val count: Int)

data class BillingDiagnosticSummary(val counts: List<BillingDiagnosticCount>) {
    fun toSupportText(): String = if (counts.isEmpty()) {
        "No Google Play Billing errors recorded during this app session."
    } else {
        buildString {
            appendLine("Google Play Billing errors for this app session:")
            counts.forEach { entry -> appendLine("${entry.diagnostic.toLogLine()} count=${entry.count}") }
        }.trimEnd()
    }
}

fun interface BillingDiagnostics {
    fun record(diagnostic: BillingDiagnostic)
    fun snapshot(): BillingDiagnosticSummary = BillingDiagnosticSummary(emptyList())
}

object NoOpBillingDiagnostics : BillingDiagnostics {
    override fun record(diagnostic: BillingDiagnostic) = Unit
}

class InMemoryBillingDiagnostics : BillingDiagnostics {
    private val counts = ConcurrentHashMap<BillingDiagnostic, AtomicInteger>()

    override fun record(diagnostic: BillingDiagnostic) {
        counts.computeIfAbsent(diagnostic) { AtomicInteger() }.incrementAndGet()
    }

    override fun snapshot(): BillingDiagnosticSummary = BillingDiagnosticSummary(
        counts.entries
            .map { BillingDiagnosticCount(it.key, it.value.get()) }
            .sortedWith(compareBy({ it.diagnostic.operation.name }, { it.diagnostic.failureKind.name }, { it.diagnostic.responseCode }))
    )
}

object LocalBillingDiagnostics : BillingDiagnostics {
    private val counter = InMemoryBillingDiagnostics()

    override fun record(diagnostic: BillingDiagnostic) {
        counter.record(diagnostic)
        // Deliberately excludes purchase tokens, order IDs, product IDs and debug messages.
        Log.w("ZeroEmpireBilling", diagnostic.toLogLine())
    }

    override fun snapshot(): BillingDiagnosticSummary = counter.snapshot()
}
```

## File: src/main/java/com/zerotoempire/game/BillingFailurePolicy.kt
```kotlin
package com.zerotoempire.game

enum class BillingFailureKind { SERVICE_DISCONNECTED, SERVICE_UNAVAILABLE, NETWORK_ERROR, OTHER }

data class BillingFailure(val message: String, val shouldReconnect: Boolean)

/** User-facing Billing failures. A retry means reconnecting the client, never replaying a purchase. */
object BillingFailurePolicy {
    fun resolve(kind: BillingFailureKind, detail: String, fallback: String): BillingFailure = when (kind) {
        BillingFailureKind.SERVICE_DISCONNECTED -> BillingFailure(
            "Google Play disconnected. Reopen the store and try again.",
            shouldReconnect = true
        )
        BillingFailureKind.SERVICE_UNAVAILABLE -> BillingFailure(
            "Google Play is temporarily unavailable. Try again shortly.",
            shouldReconnect = true
        )
        BillingFailureKind.NETWORK_ERROR -> BillingFailure(
            "Network error while contacting Google Play. Check your connection and try again.",
            shouldReconnect = true
        )
        BillingFailureKind.OTHER -> BillingFailure(detail.ifBlank { fallback }, shouldReconnect = false)
    }
}
```

## File: src/main/java/com/zerotoempire/game/BulkPurchase.kt
```kotlin
package com.zerotoempire.game

import kotlin.math.floor
import kotlin.math.ln

enum class BuyMode(val fixedCount: Int?) {
    X1(1), X10(10), X25(25), MILESTONE(null), MAX(null)
}

data class BulkQuote(val count: Int, val totalCost: Double) {
    val valid: Boolean get() = count > 0 && totalCost.isFinite() && totalCost >= 0.0
}

object BulkPurchase {
    private const val GROWTH = 1.15
    private const val MAX_SAFE_LEVELS = 1_000_000
    private val milestones = listOf(10, 25, 50, 100, 250, 500, 1000)

    fun cost(business: Business, count: Int): Double =
        EconomyMath.geometricCost(business.baseCost, business.level, count)

    fun affordableCount(business: Business, cash: Double): Int {
        val available = EconomyMath.finite(cash)
        val first = business.nextCost
        if (available < first) return 0
        if (first >= EconomyMath.MAX_VALUE) return 1

        val inside = 1.0 + available * (GROWTH - 1.0) / first
        if (!inside.isFinite()) return MAX_SAFE_LEVELS
        return floor(ln(inside) / ln(GROWTH)).toInt().coerceIn(1, MAX_SAFE_LEVELS)
    }

    fun levelsToNextMilestone(business: Business): Int {
        val next = milestones.firstOrNull { it > business.level }
            ?: if (business.level <= Int.MAX_VALUE - 1000) (((business.level / 1000) + 1) * 1000) else Int.MAX_VALUE
        return (next - business.level).coerceAtLeast(1)
    }

    fun quote(business: Business, cash: Double, mode: BuyMode): BulkQuote {
        val available = EconomyMath.finite(cash)
        val requested = when (mode) {
            BuyMode.MILESTONE -> levelsToNextMilestone(business)
            BuyMode.MAX -> affordableCount(business, available)
            else -> mode.fixedCount ?: 1
        }
        if (requested <= 0) return BulkQuote(0, 0.0)

        val total = cost(business, requested)
        if (total <= available * (1.0 + 1e-12)) return BulkQuote(requested, total)
        if (mode == BuyMode.MILESTONE) return BulkQuote(0, total)

        // The logarithmic estimate can overshoot near floating-point boundaries.
        // Correct it with a bounded binary search instead of decrementing potentially
        // hundreds of thousands of levels one by one.
        var low = 0
        var high = requested
        while (low < high) {
            val mid = low + (high - low + 1) / 2
            if (cost(business, mid) <= available) low = mid else high = mid - 1
        }
        return BulkQuote(low, cost(business, low))
    }

    fun crossedMilestones(fromLevel: Int, toLevel: Int): List<Int> =
        if (toLevel <= fromLevel) emptyList() else milestones.filter { it > fromLevel && it <= toLevel }
}
```

## File: src/main/java/com/zerotoempire/game/BulkQuoteDock.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.stateDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import java.util.Locale
import kotlin.math.abs

@Composable
fun BulkQuoteDock(vm: GameViewModel, modifier: Modifier = Modifier) {
    val state by vm.state.collectAsStateWithLifecycle()
    val mode by vm.buyMode.collectAsStateWithLifecycle()
    val candidates = state.businesses.mapNotNull { business ->
        val quote = vm.bulkQuote(business.id, mode)
        if (!quote.valid) null else Triple(business, quote, quote.totalCost <= state.cash)
    }
    if (candidates.isEmpty()) return

    Surface(
        color = EmpireColors.Void.copy(alpha = .93f),
        shape = RoundedCornerShape(18.dp),
        shadowElevation = 12.dp,
        modifier = modifier.fillMaxWidth()
    ) {
        Column(Modifier.padding(10.dp)) {
            val label = when (mode) {
                BuyMode.X1 -> "×1"
                BuyMode.X10 -> "×10"
                BuyMode.X25 -> "×25"
                BuyMode.MILESTONE -> "MILESTONE"
                BuyMode.MAX -> "MAX"
            }
            Text(
                "BULK PURCHASE • $label",
                color = EmpireColors.Gold,
                fontWeight = FontWeight.Black,
                fontSize = 10.sp,
                modifier = Modifier.semantics {
                    contentDescription = "Bulk purchase"
                    stateDescription = "$label mode selected"
                }
            )
            Spacer(Modifier.height(7.dp))
            Row(
                Modifier.horizontalScroll(rememberScrollState()),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                candidates.forEach { (business, quote, affordable) ->
                    val affordability = if (affordable) "Available" else "Not enough cash"
                    Button(
                        onClick = { vm.buyBulk(business.id, mode) },
                        enabled = affordable,
                        modifier = Modifier
                            .heightIn(min = 48.dp)
                            .semantics {
                                contentDescription = "Buy ${quote.count} levels of ${business.name} for ${compactMoney(quote.totalCost)} using $label mode"
                                stateDescription = affordability
                            },
                        shape = RoundedCornerShape(14.dp)
                    ) {
                        Column {
                            Text(business.name, fontWeight = FontWeight.Black, fontSize = 10.sp)
                            Text("+${quote.count} LV • ${compactMoney(quote.totalCost)}", fontSize = 9.sp)
                        }
                    }
                }
            }
        }
    }
}

private fun compactMoney(value: Double): String {
    val v = abs(value)
    val units = listOf(1e18 to "Qi", 1e15 to "Q", 1e12 to "T", 1e9 to "B", 1e6 to "M", 1e3 to "K")
    val u = units.firstOrNull { v >= it.first }
    return if (u != null) "$${String.format(Locale.US, "%.2f", value / u.first)}${u.second}"
    else "$${String.format(Locale.US, "%.0f", value)}"
}
```

## File: src/main/java/com/zerotoempire/game/BusinessGroup01Art.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Final art pass for Group 01: Street Stand, Corner Shop, Workshop, Factory. */
@Composable
fun BusinessGroup01Sprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val transition = if (reduced) null else rememberInfiniteTransition(label = "group01-$id")
    val phase = if (transition == null) .18f else {
        val phaseAnimated by transition.animateFloat(
            0f, 1f,
            infiniteRepeatable(tween(if (lowPower) 9000 else 5600 + id * 380, easing = LinearEasing)),
            label = "phase"
        )
        phaseAnimated
    }
    val breathe = if (reduced) .92f else .88f + .10f * ((sin(phase * PI.toFloat() * 2f - PI.toFloat() / 2f) + 1f) * .5f)
    val stage = group01Stage(level)
    val accent = group01Accent(id)

    Box(
        modifier = modifier
            .size(iconSize)
            .background(
                Brush.radialGradient(
                    0f to accent.copy(alpha = .23f + stage * .02f),
                    .45f to EmpireColors.SurfaceHigh,
                    1f to EmpireColors.Void
                ), RoundedCornerShape(iconSize * .27f)
            )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val c = Offset(s * .5f, s * .52f)
            drawOval(
                Brush.radialGradient(listOf(accent.copy(alpha = .25f), Color.Transparent), Offset(c.x, s * .77f), s * .39f),
                Offset(s * .12f, s * .68f), Size(s * .76f, s * .22f)
            )
            drawCircle(accent.copy(alpha = .09f * breathe), s * .46f, c)
            drawCircle(accent.copy(alpha = .32f), s * .42f, c, style = Stroke(s * .012f))

            when (id.coerceIn(0, 3)) {
                0 -> drawStreetStandAAA(stage, phase, breathe)
                1 -> drawCornerShopAAA(stage, phase, breathe)
                2 -> drawWorkshopAAA(stage, phase, breathe)
                else -> drawFactoryAAA(stage, phase, breathe, lowPower)
            }

            if (stage >= 1) drawGroupProgressionRing(accent, phase, .435f, 3)
            if (stage >= 2) drawGroupProgressionRing(Color.White, 1f - phase, .475f, 5)
            if (stage >= 3) drawGroupSpokes(accent, phase, if (lowPower) 4 else 8)
            if (stage >= 4) drawGroupCrown(accent, phase)
            if (stage >= 5) drawGroupMastery(accent, breathe, lowPower)
        }
    }
}

private fun group01Stage(level: Int) = when {
    level >= 1000 -> 5
    level >= 500 -> 4
    level >= 250 -> 3
    level >= 100 -> 2
    level >= 25 -> 1
    else -> 0
}

private fun group01Accent(id: Int): Color = when (id) {
    0 -> Color(0xFF78F56A)
    1 -> Color(0xFF58BFFF)
    2 -> Color(0xFFFF9A43)
    else -> Color(0xFFB76CFF)
}

private fun DrawScope.drawStreetStandAAA(stage: Int, phase: Float, breathe: Float) {
    val s = size.minDimension
    val woodDark = Color(0xFF4A2C20)
    val wood = Color(0xFF7A4B31)
    val cream = Color(0xFFFFE6B0)
    val green = group01Accent(0)
    drawRoundRect(woodDark, Offset(s*.20f,s*.49f), Size(s*.60f,s*.24f), CornerRadius(s*.04f))
    drawRoundRect(wood, Offset(s*.24f,s*.52f), Size(s*.52f,s*.15f), CornerRadius(s*.025f))
    drawCircle(Color(0xFF1A1412), s*.065f, Offset(s*.29f,s*.73f)); drawCircle(Color(0xFF1A1412),s*.065f,Offset(s*.71f,s*.73f))
    drawCircle(wood, s*.040f, Offset(s*.29f,s*.73f)); drawCircle(wood,s*.040f,Offset(s*.71f,s*.73f))
    val canopy = Path().apply { moveTo(s*.15f,s*.42f); lineTo(s*.25f,s*.26f); lineTo(s*.75f,s*.26f); lineTo(s*.85f,s*.42f); close() }
    drawPath(canopy, Color(0xFFE34B3F))
    repeat(5) { i ->
        val x = .22f + i*.12f
        val strip = Path().apply { moveTo(s*x,s*.27f); lineTo(s*(x+.075f),s*.27f); lineTo(s*(x+.12f),s*.42f); lineTo(s*(x+.045f),s*.42f); close() }
        drawPath(strip, cream.copy(alpha=.95f))
    }
    drawLine(green,Offset(s*.17f,s*.43f),Offset(s*.83f,s*.43f),s*.015f)
    repeat(4) { i ->
        val x=s*(.34f+i*.105f)
        drawCircle(Color(0xFFFFB64D),s*.024f,Offset(x,s*.58f))
        drawCircle(Color.White.copy(alpha=.6f),s*.006f,Offset(x-s*.007f,s*.57f))
    }
    val flicker = .65f + .25f*sin(phase*PI.toFloat()*2f)
    listOf(.22f,.78f).forEach { x ->
        drawCircle(Color(0xFFFFC65A).copy(alpha=flicker),s*.045f,Offset(s*x,s*.47f))
        drawCircle(Color.White.copy(alpha=.9f),s*.012f,Offset(s*x,s*.47f))
    }
    if(stage>=1) drawRoundRect(green.copy(alpha=.65f),Offset(s*.31f,s*.18f),Size(s*.38f,s*.065f),CornerRadius(s*.018f))
    if(stage>=2) repeat(3){i->drawCircle(green.copy(alpha=.8f),s*.012f,Offset(s*(.36f+i*.14f),s*.34f))}
    if(stage>=3) drawLine(Color(0xFFFFD66B),Offset(s*.23f,s*.66f),Offset(s*.77f,s*.66f),s*.012f)
    if(stage>=4) drawCircle(green.copy(alpha=.18f*breathe),s*.34f,Offset(s*.5f,s*.5f))
    if(stage>=5) repeat(5){i->drawCircle(Color(0xFFFFE78A),s*.011f,Offset(s*(.30f+i*.10f),s*.22f))}
}

private fun DrawScope.drawCornerShopAAA(stage: Int, phase: Float, breathe: Float) {
    val s=size.minDimension
    val blue=group01Accent(1)
    val navy=Color(0xFF18324C)
    val glass=Color(0xFF8FE5FF)
    val warm=Color(0xFFFFB85C)
    drawRoundRect(Color(0xFF24394D),Offset(s*.20f,s*.33f),Size(s*.60f,s*.42f),CornerRadius(s*.035f))
    drawRoundRect(Color(0xFF31516E),Offset(s*.23f,s*.36f),Size(s*.54f,s*.35f),CornerRadius(s*.025f))
    drawRoundRect(navy,Offset(s*.27f,s*.49f),Size(s*.46f,s*.20f),CornerRadius(s*.015f))
    drawRect(glass.copy(alpha=.45f),Offset(s*.29f,s*.51f),Size(s*.18f,s*.16f)); drawRect(glass.copy(alpha=.45f),Offset(s*.53f,s*.51f),Size(s*.18f,s*.16f))
    drawLine(warm.copy(alpha=.85f),Offset(s*.50f,s*.51f),Offset(s*.50f,s*.67f),s*.012f)
    repeat(6){i->
        val x=.22f+i*.095f
        drawRoundRect(if(i%2==0) blue else Color.White.copy(alpha=.9f),Offset(s*x,s*.40f),Size(s*.09f,s*.08f),CornerRadius(s*.012f))
    }
    drawRoundRect(Color(0xFF0E1C2A),Offset(s*.30f,s*.24f),Size(s*.40f,s*.10f),CornerRadius(s*.022f))
    drawRoundRect(blue.copy(alpha=.75f),Offset(s*.32f,s*.255f),Size(s*.36f,s*.065f),CornerRadius(s*.018f))
    val neon=.55f+.35f*breathe
    listOf(.17f,.83f).forEach{x->
        drawLine(Color(0xFF6B7D8E),Offset(s*x,s*.43f),Offset(s*x,s*.74f),s*.012f)
        drawCircle(warm.copy(alpha=neon),s*.035f,Offset(s*x,s*.42f)); drawCircle(Color.White,s*.010f,Offset(s*x,s*.42f))
    }
    if(stage>=1) drawCircle(blue.copy(alpha=.16f*breathe),s*.30f,Offset(s*.5f,s*.50f))
    if(stage>=2) repeat(4){i->drawCircle(blue,s*.010f,Offset(s*(.33f+i*.11f),s*.30f))}
    if(stage>=3) drawArc(blue.copy(alpha=.6f),195f+phase*15f,150f,false,Offset(s*.18f,s*.17f),Size(s*.64f,s*.64f),style=Stroke(s*.014f))
    if(stage>=4) drawLine(Color.White.copy(alpha=.45f),Offset(s*.26f,s*.70f),Offset(s*.74f,s*.70f),s*.009f)
    if(stage>=5) repeat(6){i->drawCircle(Color(0xFFB8F1FF),s*.009f,Offset(s*(.27f+i*.09f),s*.21f))}
}

private fun DrawScope.drawWorkshopAAA(stage:Int,phase:Float,breathe:Float){
    val s=size.minDimension
    val orange=group01Accent(2)
    val steel=Color(0xFF41474D)
    val dark=Color(0xFF20252A)
    val hot=Color(0xFFFFD073)
    val roof=Path().apply{moveTo(s*.18f,s*.48f);lineTo(s*.31f,s*.30f);lineTo(s*.62f,s*.30f);lineTo(s*.75f,s*.43f);lineTo(s*.82f,s*.43f);lineTo(s*.82f,s*.73f);lineTo(s*.18f,s*.73f);close()}
    drawPath(roof,Brush.verticalGradient(listOf(steel,dark)))
    drawPath(roof,orange.copy(alpha=.55f),style=Stroke(s*.014f))
    drawRoundRect(dark,Offset(s*.29f,s*.50f),Size(s*.28f,s*.19f),CornerRadius(s*.015f))
    drawRoundRect(orange.copy(alpha=.42f),Offset(s*.31f,s*.52f),Size(s*.24f,s*.15f),CornerRadius(s*.012f))
    drawRect(steel,Offset(s*.63f,s*.21f),Size(s*.08f,s*.26f))
    drawRect(Color(0xFF1B1B1B),Offset(s*.62f,s*.19f),Size(s*.10f,s*.035f))
    val fire=.55f+.35f*sin(phase*PI.toFloat()*2f)
    drawCircle(orange.copy(alpha=fire),s*.055f,Offset(s*.43f,s*.60f));drawCircle(hot.copy(alpha=.9f),s*.018f,Offset(s*.43f,s*.60f))
    val center=Offset(s*.65f,s*.61f)
    drawCircle(steel,s*.09f,center);drawCircle(orange,s*.057f,center,style=Stroke(s*.026f))
    repeat(8){i->val a=phase*PI.toFloat()*2f+i*PI.toFloat()/4f;drawLine(orange,Offset(center.x+cos(a)*s*.066f,center.y+sin(a)*s*.066f),Offset(center.x+cos(a)*s*.105f,center.y+sin(a)*s*.105f),s*.022f)}
    if(stage>=1) repeat(3){i->drawCircle(hot,s*.009f,Offset(s*(.29f+i*.10f),s*.39f))}
    if(stage>=2) drawLine(orange,Offset(s*.21f,s*.75f),Offset(s*.79f,s*.75f),s*.013f)
    if(stage>=3) repeat(4){i->drawCircle(orange.copy(alpha=.65f*breathe),s*.016f,Offset(s*(.31f+i*.12f),s*.78f))}
    if(stage>=4) drawArc(hot.copy(alpha=.6f),215f+phase*20f,110f,false,Offset(s*.19f,s*.18f),Size(s*.62f,s*.62f),style=Stroke(s*.014f))
    if(stage>=5) repeat(5){i->drawCircle(Color.White.copy(alpha=.8f),s*.008f,Offset(s*(.30f+i*.10f),s*.25f))}
}

private fun DrawScope.drawFactoryAAA(stage:Int,phase:Float,breathe:Float,lowPower:Boolean){
    val s=size.minDimension
    val violet=group01Accent(3)
    val steel=Color(0xFF333642)
    val steel2=Color(0xFF555B6B)
    val magenta=Color(0xFFFF72D8)
    drawRoundRect(steel,Offset(s*.16f,s*.46f),Size(s*.68f,s*.30f),CornerRadius(s*.025f))
    drawRoundRect(steel2,Offset(s*.24f,s*.37f),Size(s*.45f,s*.23f),CornerRadius(s*.018f))
    drawRoundRect(Color(0xFF242631),Offset(s*.33f,s*.30f),Size(s*.28f,s*.15f),CornerRadius(s*.015f))
    drawLine(violet,Offset(s*.18f,s*.72f),Offset(s*.82f,s*.72f),s*.015f)
    val stacks=if(lowPower) 3 else 4
    repeat(stacks){i->
        val x=.24f+i*.15f
        val h=.22f+(i%2)*.05f
        drawRoundRect(steel2,Offset(s*x,s*(.42f-h)),Size(s*.075f,s*h),CornerRadius(s*.012f))
        drawRect(violet.copy(alpha=.75f),Offset(s*(x-.005f),s*(.42f-h)),Size(s*.085f,s*.035f))
        val smokeOffset=.025f*sin((phase+i*.17f)*PI.toFloat()*2f)
        drawCircle(Color(0xFFC8B8FF).copy(alpha=.10f),s*.045f,Offset(s*(x+.038f+smokeOffset),s*(.36f-h)))
    }
    repeat(4){i->
        drawRoundRect(violet.copy(alpha=.75f),Offset(s*(.24f+i*.13f),s*.57f),Size(s*.085f,s*.085f),CornerRadius(s*.010f))
        drawCircle(magenta.copy(alpha=.6f*breathe),s*.010f,Offset(s*(.282f+i*.13f),s*.612f))
    }
    drawRoundRect(Color(0xFF171821),Offset(s*.66f,s*.52f),Size(s*.12f,s*.15f),CornerRadius(s*.012f))
    repeat(3){i->drawLine(violet.copy(alpha=.55f),Offset(s*.67f,s*(.55f+i*.035f)),Offset(s*.77f,s*(.55f+i*.035f)),s*.009f)}
    if(stage>=1) drawCircle(violet.copy(alpha=.12f*breathe),s*.32f,Offset(s*.5f,s*.52f))
    if(stage>=2) repeat(5){i->drawCircle(magenta,s*.008f,Offset(s*(.28f+i*.10f),s*.69f))}
    if(stage>=3) drawArc(violet.copy(alpha=.55f),185f+phase*25f,165f,false,Offset(s*.13f,s*.14f),Size(s*.74f,s*.70f),style=Stroke(s*.014f))
    if(stage>=4) repeat(if(lowPower)3 else 6){i->val a=i*PI.toFloat()/3f+phase;drawLine(violet.copy(alpha=.32f),Offset(s*.5f+cos(a)*s*.28f,s*.5f+sin(a)*s*.20f),Offset(s*.5f+cos(a)*s*.42f,s*.5f+sin(a)*s*.30f),s*.010f)}
    if(stage>=5) drawCircle(Color.White.copy(alpha=.12f*breathe),s*.40f,Offset(s*.5f,s*.5f),style=Stroke(s*.018f))
}

private fun DrawScope.drawGroupProgressionRing(color:Color,phase:Float,radius:Float,nodes:Int){
    val s=size.minDimension;val c=Offset(s*.5f,s*.5f)
    drawCircle(color.copy(alpha=.30f),s*radius,c,style=Stroke(s*.010f))
    repeat(nodes){i->val a=phase*PI.toFloat()*2f+i*PI.toFloat()*2f/nodes;val p=Offset(c.x+cos(a)*s*radius,c.y+sin(a)*s*radius);drawCircle(color.copy(alpha=.75f),s*.010f,p)}
}
private fun DrawScope.drawGroupSpokes(color:Color,phase:Float,count:Int){
    val s=size.minDimension;val c=Offset(s*.5f,s*.5f);repeat(count){i->val a=phase*PI.toFloat()*.5f+i*PI.toFloat()*2f/count;drawLine(color.copy(alpha=.34f),Offset(c.x+cos(a)*s*.38f,c.y+sin(a)*s*.38f),Offset(c.x+cos(a)*s*.47f,c.y+sin(a)*s*.47f),s*.008f)}
}
private fun DrawScope.drawGroupCrown(color:Color,phase:Float){
    val s=size.minDimension;drawArc(Color(0xFFFFE07A).copy(alpha=.65f),-30f+phase*20f,230f,false,Offset(s*.07f,s*.07f),Size(s*.86f,s*.86f),style=Stroke(s*.014f));drawArc(color.copy(alpha=.48f),160f-phase*16f,145f,false,Offset(s*.11f,s*.11f),Size(s*.78f,s*.78f),style=Stroke(s*.009f))
}
private fun DrawScope.drawGroupMastery(color:Color,breathe:Float,lowPower:Boolean){
    val s=size.minDimension;drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.13f*breathe),color.copy(alpha=.08f),Color.Transparent)),s*.50f,Offset(s*.5f,s*.5f));repeat(if(lowPower)4 else 8){i->val a=i*PI.toFloat()/4f;drawCircle(Color.White.copy(alpha=.65f),s*.007f,Offset(s*.5f+cos(a)*s*.46f,s*.5f+sin(a)*s*.46f))}
}
```

## File: src/main/java/com/zerotoempire/game/BusinessGroup01Evolution.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Extra structural layers that make each progression tier visibly change silhouette. */
@Composable
fun BusinessGroup01Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val stage = when {
        level >= 1000 -> 7
        level >= 500 -> 6
        level >= 250 -> 5
        level >= 100 -> 4
        level >= 50 -> 3
        level >= 25 -> 2
        level >= 10 -> 1
        else -> 0
    }

    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val reveal = remember(id) { Animatable(0f) }
    val previousStage = remember(id) { intArrayOf(stage) }

    LaunchedEffect(stage, reducedMotion) {
        val prior = previousStage[0]
        previousStage[0] = stage
        if (stage > prior && !reducedMotion) {
            reveal.snapTo(1f)
            reveal.animateTo(0f, tween(760))
        } else if (reducedMotion && reveal.value != 0f) {
            reveal.snapTo(0f)
        }
    }

    if (stage == 0) return

    val accent = when (id) {
        0 -> Color(0xFF78F56A)
        1 -> Color(0xFF58BFFF)
        2 -> Color(0xFFFF9A43)
        else -> Color(0xFFB76CFF)
    }
    val secondary = when (id) {
        0 -> Color(0xFFFFE87A)
        1 -> Color(0xFFB8F1FF)
        2 -> Color(0xFFFFD073)
        else -> Color(0xFFFF72D8)
    }

    Canvas(modifier.size(iconSize)) {
        val s = size.minDimension
        val center = Offset(s * .5f, s * .5f)

        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(Color.White.copy(alpha = .07f), accent.copy(alpha = .09f), Color.Transparent),
                    center = Offset(s * .42f, s * .36f),
                    radius = s * .47f
                ),
                radius = s * .455f,
                center = center
            )
            drawArc(
                secondary.copy(alpha = .24f),
                214f,
                50f,
                false,
                Offset(s * .10f, s * .10f),
                Size(s * .80f, s * .80f),
                style = Stroke(s * .005f)
            )
        }
        if (stage >= 6) {
            drawArc(
                accent.copy(alpha = .30f),
                20f,
                112f,
                false,
                Offset(s * .08f, s * .08f),
                Size(s * .84f, s * .84f),
                style = Stroke(s * .006f)
            )
            drawArc(
                Color.White.copy(alpha = .18f),
                198f,
                68f,
                false,
                Offset(s * .125f, s * .125f),
                Size(s * .75f, s * .75f),
                style = Stroke(s * .004f)
            )
        }
        if (stage >= 7) {
            repeat(8) { i ->
                val angle = i * 2f * PI.toFloat() / 8f - PI.toFloat() / 2f
                val node = Offset(
                    center.x + cos(angle) * s * .445f,
                    center.y + sin(angle) * s * .445f
                )
                drawCircle(Color.Black.copy(alpha = .32f), s * .014f, node)
                drawCircle(if (i % 2 == 0) secondary else accent, s * .007f, node)
            }
        }

        when (id) {
            0 -> {
                val green = Color(0xFF78F56A)
                if (stage >= 1) {
                    drawLine(green.copy(alpha = .8f), Offset(s * .14f, s * .76f), Offset(s * .86f, s * .76f), s * .012f)
                    drawCircle(green.copy(alpha = .75f), s * .018f, Offset(s * .17f, s * .75f))
                    drawCircle(green.copy(alpha = .75f), s * .018f, Offset(s * .83f, s * .75f))
                }
                if (stage >= 2) {
                    drawRoundRect(Color(0xFF385A31), Offset(s * .12f, s * .52f), Size(s * .10f, s * .18f), CornerRadius(s * .015f))
                    drawRoundRect(Color(0xFF385A31), Offset(s * .78f, s * .52f), Size(s * .10f, s * .18f), CornerRadius(s * .015f))
                }
                if (stage >= 3) {
                    drawLine(Color(0xFFFFD66B), Offset(s * .17f, s * .20f), Offset(s * .83f, s * .20f), s * .012f)
                    repeat(5) { i -> drawCircle(Color(0xFFFFEAA0), s * .009f, Offset(s * (.22f + i * .14f), s * .20f)) }
                }
                if (stage >= 4) {
                    drawRoundRect(green.copy(alpha = .25f), Offset(s * .08f, s * .34f), Size(s * .12f, s * .38f), CornerRadius(s * .025f), style = Stroke(s * .012f))
                    drawRoundRect(green.copy(alpha = .25f), Offset(s * .80f, s * .34f), Size(s * .12f, s * .38f), CornerRadius(s * .025f), style = Stroke(s * .012f))
                }
                if (stage >= 5) {
                    drawLine(green.copy(alpha = .62f), Offset(s * .24f, s * .14f), Offset(s * .24f, s * .33f), s * .009f)
                    drawLine(green.copy(alpha = .62f), Offset(s * .76f, s * .14f), Offset(s * .76f, s * .33f), s * .009f)
                }
                if (stage >= 6) {
                    repeat(3) { i -> drawCircle(Color(0xFFFFE87A).copy(alpha = .62f), s * (.30f + i * .055f), Offset(s * .5f, s * .5f), style = Stroke(s * .008f)) }
                }
                if (stage >= 7) drawCircle(Color(0xFFFFE87A).copy(alpha = .82f), s * .455f, Offset(s * .5f, s * .5f), style = Stroke(s * .016f))
            }

            1 -> {
                val blue = Color(0xFF58BFFF)
                if (stage >= 1) drawRoundRect(blue.copy(alpha = .25f), Offset(s * .15f, s * .27f), Size(s * .70f, s * .50f), CornerRadius(s * .035f), style = Stroke(s * .012f))
                if (stage >= 2) {
                    drawRoundRect(Color(0xFF28445E), Offset(s * .24f, s * .19f), Size(s * .52f, s * .09f), CornerRadius(s * .02f))
                    repeat(4) { i -> drawCircle(blue, s * .009f, Offset(s * (.34f + i * .11f), s * .235f)) }
                }
                if (stage >= 3) {
                    drawLine(blue.copy(alpha = .8f), Offset(s * .12f, s * .74f), Offset(s * .88f, s * .74f), s * .012f)
                    drawCircle(Color.White.copy(alpha = .85f), s * .015f, Offset(s * .15f, s * .74f))
                    drawCircle(Color.White.copy(alpha = .85f), s * .015f, Offset(s * .85f, s * .74f))
                }
                if (stage >= 4) {
                    drawRoundRect(blue.copy(alpha = .18f), Offset(s * .09f, s * .38f), Size(s * .10f, s * .31f), CornerRadius(s * .015f))
                    drawRoundRect(blue.copy(alpha = .18f), Offset(s * .81f, s * .38f), Size(s * .10f, s * .31f), CornerRadius(s * .015f))
                }
                if (stage >= 5) {
                    drawLine(blue.copy(alpha = .70f), Offset(s * .20f, s * .16f), Offset(s * .32f, s * .26f), s * .009f)
                    drawLine(blue.copy(alpha = .70f), Offset(s * .80f, s * .16f), Offset(s * .68f, s * .26f), s * .009f)
                }
                if (stage >= 6) {
                    repeat(3) { i -> drawCircle(Color(0xFFB8F1FF).copy(alpha = .58f), s * (.30f + i * .055f), Offset(s * .5f, s * .5f), style = Stroke(s * .008f)) }
                }
                if (stage >= 7) drawCircle(Color(0xFFB8F1FF).copy(alpha = .84f), s * .455f, Offset(s * .5f, s * .5f), style = Stroke(s * .015f))
            }

            2 -> {
                val orange = Color(0xFFFF9A43)
                if (stage >= 1) drawRoundRect(Color(0xFF343A40), Offset(s * .11f, s * .51f), Size(s * .10f, s * .22f), CornerRadius(s * .012f))
                if (stage >= 2) drawRoundRect(Color(0xFF4A5058), Offset(s * .72f, s * .25f), Size(s * .09f, s * .26f), CornerRadius(s * .012f))
                if (stage >= 3) {
                    repeat(3) { i -> drawCircle(orange.copy(alpha = .7f), s * .026f, Offset(s * (.26f + i * .24f), s * .77f), style = Stroke(s * .010f)) }
                    drawLine(orange.copy(alpha = .75f), Offset(s * .15f, s * .78f), Offset(s * .85f, s * .78f), s * .011f)
                }
                if (stage >= 4) {
                    drawRoundRect(orange.copy(alpha = .20f), Offset(s * .08f, s * .30f), Size(s * .12f, s * .44f), CornerRadius(s * .018f), style = Stroke(s * .012f))
                    drawRoundRect(orange.copy(alpha = .20f), Offset(s * .80f, s * .30f), Size(s * .12f, s * .44f), CornerRadius(s * .018f), style = Stroke(s * .012f))
                }
                if (stage >= 5) {
                    drawLine(orange.copy(alpha = .65f), Offset(s * .20f, s * .20f), Offset(s * .20f, s * .37f), s * .009f)
                    drawLine(orange.copy(alpha = .65f), Offset(s * .84f, s * .20f), Offset(s * .84f, s * .37f), s * .009f)
                }
                if (stage >= 6) {
                    repeat(3) { i -> drawCircle(Color(0xFFFFD073).copy(alpha = .60f), s * (.30f + i * .055f), Offset(s * .5f, s * .5f), style = Stroke(s * .008f)) }
                }
                if (stage >= 7) drawCircle(Color(0xFFFFD073).copy(alpha = .84f), s * .455f, Offset(s * .5f, s * .5f), style = Stroke(s * .016f))
            }

            3 -> {
                val violet = Color(0xFFB76CFF)
                if (stage >= 1) {
                    drawRoundRect(Color(0xFF444855), Offset(s * .09f, s * .48f), Size(s * .12f, s * .27f), CornerRadius(s * .018f))
                    drawRoundRect(Color(0xFF444855), Offset(s * .79f, s * .48f), Size(s * .12f, s * .27f), CornerRadius(s * .018f))
                }
                if (stage >= 2) repeat(2) { i -> drawRoundRect(Color(0xFF626879), Offset(s * (.17f + i * .58f), s * .23f), Size(s * .07f, s * .28f), CornerRadius(s * .010f)) }
                if (stage >= 3) {
                    drawLine(violet.copy(alpha = .8f), Offset(s * .10f, s * .77f), Offset(s * .90f, s * .77f), s * .013f)
                    repeat(5) { i -> drawCircle(Color(0xFFFF72D8), s * .010f, Offset(s * (.25f + i * .125f), s * .77f)) }
                }
                if (stage >= 4) {
                    drawRoundRect(violet.copy(alpha = .20f), Offset(s * .07f, s * .32f), Size(s * .10f, s * .42f), CornerRadius(s * .018f), style = Stroke(s * .012f))
                    drawRoundRect(violet.copy(alpha = .20f), Offset(s * .83f, s * .32f), Size(s * .10f, s * .42f), CornerRadius(s * .018f), style = Stroke(s * .012f))
                }
                if (stage >= 5) {
                    drawLine(Color(0xFFFF72D8).copy(alpha = .68f), Offset(s * .22f, s * .18f), Offset(s * .31f, s * .31f), s * .009f)
                    drawLine(Color(0xFFFF72D8).copy(alpha = .68f), Offset(s * .78f, s * .18f), Offset(s * .69f, s * .31f), s * .009f)
                }
                if (stage >= 6) {
                    repeat(3) { i -> drawCircle(Color(0xFFFF72D8).copy(alpha = .56f), s * (.30f + i * .055f), Offset(s * .5f, s * .5f), style = Stroke(s * .008f)) }
                }
                if (stage >= 7) drawCircle(Color(0xFFFF72D8).copy(alpha = .82f), s * .46f, Offset(s * .5f, s * .5f), style = Stroke(s * .016f))
            }
        }

        val revealIntensity = reveal.value.coerceIn(0f, 1f)
        if (revealIntensity > 0f) {
            val travel = 1f - revealIntensity
            val ringRadius = s * (.30f + .18f * travel)

            // A short materialization beat makes a tier unlock read as a true transformation,
            // without creating another permanent animation loop.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .18f * revealIntensity),
                        accent.copy(alpha = .14f * revealIntensity),
                        Color.Transparent
                    ),
                    center = center,
                    radius = s * .48f
                ),
                radius = s * (.34f + .10f * travel),
                center = center
            )
            drawCircle(
                color = secondary.copy(alpha = .74f * revealIntensity),
                radius = ringRadius,
                center = center,
                style = Stroke(width = s * (.010f + .008f * revealIntensity))
            )
            drawCircle(
                color = Color.White.copy(alpha = .42f * revealIntensity),
                radius = s * (.25f + .14f * travel),
                center = center,
                style = Stroke(width = s * .005f)
            )

            val rayCount = 8 + stage.coerceAtMost(4) * 2
            repeat(rayCount) { i ->
                val angle = 2f * PI.toFloat() * i / rayCount - PI.toFloat() / 2f
                val inner = s * (.28f + .04f * travel)
                val outer = s * (.36f + .12f * travel)
                drawLine(
                    color = if (i % 2 == 0) accent else secondary,
                    start = Offset(center.x + cos(angle) * inner, center.y + sin(angle) * inner),
                    end = Offset(center.x + cos(angle) * outer, center.y + sin(angle) * outer),
                    strokeWidth = s * .007f,
                    alpha = .58f * revealIntensity
                )
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/BusinessGroup02Art.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Final art pass for Group 02: Tech Company, Megacity, Moon Colony, Mars Empire. */
@Composable
fun BusinessGroup02Sprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val motion = if (reduced) null else rememberInfiniteTransition(label = "group02-$id")
    val phase = if (motion == null) .22f else {
        val phaseAnimated by motion.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 9800 else 6100 + id * 280, easing = LinearEasing)), label = "phase")
        phaseAnimated
    }
    val breathe = if (reduced) .94f else .92f + .04f * sin(phase * 2f * PI.toFloat())
    val stage = group02Stage(level)
    val accent = group02Accent(id)

    Box(modifier.size(iconSize).background(Brush.radialGradient(0f to accent.copy(alpha=.23f+stage*.02f), .46f to EmpireColors.SurfaceHigh, 1f to EmpireColors.Void), RoundedCornerShape(iconSize*.27f))) {
        Canvas(Modifier.fillMaxSize()) {
            val s=size.minDimension
            val c=Offset(s*.5f,s*.52f)
            drawOval(Brush.radialGradient(listOf(accent.copy(alpha=.24f),Color.Transparent),Offset(c.x,s*.78f),s*.40f),Offset(s*.10f,s*.69f),Size(s*.80f,s*.22f))
            drawCircle(accent.copy(alpha=.08f*breathe),s*.47f,c)
            drawCircle(accent.copy(alpha=.30f),s*.42f,c,style=Stroke(s*.012f))
            when(id.coerceIn(4,7)) {
                4 -> drawTechCompanyAAA(stage,phase,breathe)
                5 -> drawMegacityAAA(stage,phase,breathe,lowPower)
                6 -> drawMoonColonyAAA(stage,phase,breathe,lowPower)
                else -> drawMarsEmpireAAA(stage,phase,breathe,lowPower)
            }
            if(stage>=1) drawGroup02Ring(accent,phase,.435f,3)
            if(stage>=2) drawGroup02Ring(Color.White,1f-phase,.475f,5)
            if(stage>=3) drawGroup02Spokes(accent,phase,if(lowPower)4 else 8)
            if(stage>=4) drawGroup02Crown(accent,phase)
            if(stage>=5) drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.12f*breathe),accent.copy(alpha=.08f),Color.Transparent)),s*.52f,c)
        }
    }
}

private fun group02Stage(level:Int)=when{level>=1000->5;level>=500->4;level>=250->3;level>=100->2;level>=25->1;else->0}
private fun group02Accent(id:Int)=when(id){4->Color(0xFF8C7CFF);5->Color(0xFFB861FF);6->Color(0xFF9FE8FF);else->Color(0xFFFF6C5F)}

private fun DrawScope.drawTechCompanyAAA(stage:Int,phase:Float,breathe:Float){
    val s=size.minDimension; val purple=group02Accent(4); val cyan=Color(0xFF6EEAFF); val steel=Color(0xFF303849)
    drawRoundRect(steel,Offset(s*.20f,s*.31f),Size(s*.60f,s*.44f),CornerRadius(s*.06f))
    drawRoundRect(Color(0xFF151B28),Offset(s*.24f,s*.35f),Size(s*.52f,s*.36f),CornerRadius(s*.05f))
    repeat(4){i-> val x=.29f+i*.13f; drawRoundRect(if(i%2==0)purple.copy(alpha=.65f) else cyan.copy(alpha=.55f),Offset(s*x,s*.40f),Size(s*.085f,s*.21f),CornerRadius(s*.014f))}
    drawCircle(purple,s*.105f,Offset(s*.5f,s*.48f),style=Stroke(s*.026f)); drawCircle(Color.White,s*.024f,Offset(s*.5f,s*.48f))
    repeat(if(stage>=3)10 else 6){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/(if(stage>=3)10 else 6);drawLine(cyan.copy(alpha=.65f),Offset(s*.5f+cos(a)*s*.13f,s*.48f+sin(a)*s*.13f),Offset(s*.5f+cos(a)*s*.22f,s*.48f+sin(a)*s*.22f),s*.010f)}
    if(stage>=1) drawRoundRect(purple.copy(alpha=.45f*breathe),Offset(s*.31f,s*.22f),Size(s*.38f,s*.06f),CornerRadius(s*.018f))
    if(stage>=2) repeat(3){i->drawCircle(cyan,s*.012f,Offset(s*(.36f+i*.14f),s*.67f))}
    if(stage>=4) drawArc(Color.White.copy(alpha=.45f),200f+phase*15f,140f,false,Offset(s*.16f,s*.15f),Size(s*.68f,s*.68f),style=Stroke(s*.012f))
    if(stage>=5) repeat(5){i->drawCircle(Color(0xFFFFE79B),s*.009f,Offset(s*(.30f+i*.10f),s*.20f))}
}

private fun DrawScope.drawMegacityAAA(stage:Int,phase:Float,breathe:Float,lowPower:Boolean){
    val s=size.minDimension; val violet=group02Accent(5); val cyan=Color(0xFF59E8FF)
    val xs=listOf(.16f,.27f,.38f,.50f,.62f,.73f); val hs=listOf(.27f,.40f,.33f,.50f,.39f,.29f)
    xs.forEachIndexed{i,x->val h=s*(hs[i]+stage*.012f);val w=s*if(i==3).12f else .095f;drawRoundRect(Brush.verticalGradient(listOf(violet.copy(alpha=.80f),Color(0xFF242838))),Offset(s*x,s*.76f-h),Size(w,h),CornerRadius(s*.016f));repeat(if(lowPower)2 else 4){r->drawCircle(if((i+r)%2==0)cyan else Color(0xFFFFD46A),s*.007f,Offset(s*(x+.03f),s*.71f-h+r*s*.055f))}}
    drawLine(violet.copy(alpha=.70f),Offset(s*.17f,s*.77f),Offset(s*.83f,s*.77f),s*.013f)
    if(stage>=1) drawArc(cyan.copy(alpha=.45f),190f+phase*12f,160f,false,Offset(s*.14f,s*.14f),Size(s*.72f,s*.72f),style=Stroke(s*.010f))
    val orbiters = if(lowPower)3 else 6
    if(stage>=2) repeat(orbiters){i->val a=phase*2*PI+i*2*PI/orbiters;drawCircle(violet.copy(alpha=.8f),s*.010f,Offset(s*.5f+cos(a).toFloat()*s*.33f,s*.50f+sin(a).toFloat()*s*.10f))}
    if(stage>=3) drawRoundRect(Color.White.copy(alpha=.10f*breathe),Offset(s*.28f,s*.18f),Size(s*.44f,s*.055f),CornerRadius(s*.018f))
    if(stage>=4) repeat(3){i->drawLine(cyan.copy(alpha=.50f),Offset(s*(.29f+i*.19f),s*.66f),Offset(s*(.29f+i*.19f),s*.28f),s*.006f)}
    if(stage>=5) drawCircle(violet.copy(alpha=.14f*breathe),s*.36f,Offset(s*.5f,s*.49f))
}

private fun DrawScope.drawMoonColonyAAA(stage:Int,phase:Float,breathe:Float,lowPower:Boolean){
    val s=size.minDimension; val ice=group02Accent(6); val steel=Color(0xFF8AA5B7); val dark=Color(0xFF202A35)
    drawOval(Color(0xFF68737A),Offset(s*.15f,s*.68f),Size(s*.70f,s*.12f)); drawOval(Color.White.copy(alpha=.10f),Offset(s*.23f,s*.70f),Size(s*.17f,s*.04f))
    listOf(.28f,.50f,.72f).forEachIndexed{i,x->val r=s*(.115f+i*.012f);drawCircle(dark,r,Offset(s*x,s*.56f));drawCircle(ice.copy(alpha=.35f),r*.84f,Offset(s*x,s*.56f));drawArc(Color.White.copy(alpha=.50f),205f,90f,false,Offset(s*x-r*.78f,s*.56f-r*.78f),Size(r*1.56f,r*1.56f),style=Stroke(s*.008f))}
    drawLine(steel,Offset(s*.34f,s*.62f),Offset(s*.44f,s*.62f),s*.018f); drawLine(steel,Offset(s*.56f,s*.62f),Offset(s*.66f,s*.62f),s*.018f)
    val dishA=phase*2f*PI.toFloat(); val dishC=Offset(s*.51f,s*.35f);drawLine(steel,dishC,Offset(dishC.x+cos(dishA)*s*.08f,dishC.y+sin(dishA)*s*.04f),s*.010f);drawArc(ice.copy(alpha=.75f),210f+phase*20f,120f,false,Offset(s*.44f,s*.28f),Size(s*.14f,s*.10f),style=Stroke(s*.012f))
    if(stage>=1) repeat(3){i->drawCircle(ice.copy(alpha=.55f*breathe),s*.013f,Offset(s*(.32f+i*.18f),s*.45f))}
    if(stage>=2) drawArc(Color.White.copy(alpha=.36f),185f+phase*15f,170f,false,Offset(s*.13f,s*.16f),Size(s*.74f,s*.62f),style=Stroke(s*.010f))
    if(stage>=3) repeat(if(lowPower)2 else 4){i->drawCircle(Color(0xFFE9FBFF),s*.009f,Offset(s*(.28f+i*.14f),s*.74f))}
    if(stage>=4) drawCircle(ice.copy(alpha=.12f*breathe),s*.35f,Offset(s*.5f,s*.53f))
    if(stage>=5) repeat(5){i->drawCircle(Color.White.copy(alpha=.85f),s*.008f,Offset(s*(.30f+i*.10f),s*.20f))}
}

private fun DrawScope.drawMarsEmpireAAA(stage:Int,phase:Float,breathe:Float,lowPower:Boolean){
    val s=size.minDimension; val red=group02Accent(7); val gold=Color(0xFFFFC85A); val dark=Color(0xFF3A2321)
    drawOval(Color(0xFF6E352E),Offset(s*.12f,s*.70f),Size(s*.76f,s*.12f))
    val palace=Path().apply{moveTo(s*.20f,s*.71f);lineTo(s*.20f,s*.45f);lineTo(s*.34f,s*.34f);lineTo(s*.42f,s*.42f);lineTo(s*.50f,s*.27f);lineTo(s*.58f,s*.42f);lineTo(s*.66f,s*.34f);lineTo(s*.80f,s*.45f);lineTo(s*.80f,s*.71f);close()}
    drawPath(palace,Brush.verticalGradient(listOf(red.copy(alpha=.85f),dark)));drawPath(palace,gold.copy(alpha=.60f),style=Stroke(s*.012f))
    drawCircle(gold.copy(alpha=.70f*breathe),s*.055f,Offset(s*.5f,s*.47f));drawCircle(Color.White,s*.014f,Offset(s*.5f,s*.47f))
    repeat(4){i->drawRoundRect(Color(0xFF1F1515),Offset(s*(.28f+i*.13f),s*.56f),Size(s*.07f,s*.11f),CornerRadius(s*.012f))}
    val patrolCount = if(lowPower)2 else 4
    repeat(patrolCount){i->val a=phase*2*PI+i*2*PI/patrolCount;drawCircle(red.copy(alpha=.75f),s*.010f,Offset(s*.5f+cos(a).toFloat()*s*.30f,s*.50f+sin(a).toFloat()*s*.13f))}
    if(stage>=1) drawLine(gold,Offset(s*.24f,s*.73f),Offset(s*.76f,s*.73f),s*.012f)
    if(stage>=2) repeat(3){i->drawCircle(red,s*.012f,Offset(s*(.36f+i*.14f),s*.33f))}
    if(stage>=3) drawArc(red.copy(alpha=.55f),200f+phase*18f,140f,false,Offset(s*.16f,s*.15f),Size(s*.68f,s*.68f),style=Stroke(s*.012f))
    if(stage>=4) drawCircle(gold.copy(alpha=.12f*breathe),s*.35f,Offset(s*.5f,s*.50f))
    if(stage>=5) repeat(5){i->drawCircle(gold,s*.009f,Offset(s*(.30f+i*.10f),s*.19f))}
}

private fun DrawScope.drawGroup02Ring(color:Color,phase:Float,radius:Float,nodes:Int){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);drawCircle(color.copy(alpha=.28f),s*radius,c,style=Stroke(s*.009f));repeat(nodes){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes;drawCircle(color.copy(alpha=.82f),s*.010f,Offset(c.x+cos(a)*s*radius,c.y+sin(a)*s*radius))}}
private fun DrawScope.drawGroup02Spokes(color:Color,phase:Float,count:Int){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);repeat(count){i->val a=phase*PI.toFloat()*.35f+i*2f*PI.toFloat()/count;drawLine(color.copy(alpha=.35f),Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f),Offset(c.x+cos(a)*s*.48f,c.y+sin(a)*s*.48f),s*.007f)}}
private fun DrawScope.drawGroup02Crown(color:Color,phase:Float){val s=size.minDimension;drawArc(Color(0xFFFFD76A).copy(alpha=.65f),-35f+phase*16f,240f,false,Offset(s*.08f,s*.08f),Size(s*.84f,s*.84f),style=Stroke(s*.012f));drawArc(color.copy(alpha=.40f),160f-phase*12f,160f,false,Offset(s*.12f,s*.12f),Size(s*.76f,s*.76f),style=Stroke(s*.009f))}
```

## File: src/main/java/com/zerotoempire/game/BusinessGroup02Evolution.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun BusinessGroup02Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val stage = when {
        level >= 1000 -> 7
        level >= 500 -> 6
        level >= 250 -> 5
        level >= 100 -> 4
        level >= 50 -> 3
        level >= 25 -> 2
        level >= 10 -> 1
        else -> 0
    }

    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val reveal = remember(id) { Animatable(0f) }
    val previousStage = remember(id) { intArrayOf(stage) }

    LaunchedEffect(stage, reducedMotion, lowPower) {
        val prior = previousStage[0]
        previousStage[0] = stage
        if (stage > prior && !reducedMotion) {
            reveal.snapTo(1f)
            reveal.animateTo(0f, tween(if (lowPower) 520 else 820))
        } else if (reducedMotion && reveal.value != 0f) {
            reveal.snapTo(0f)
        }
    }

    if (stage == 0) return

    val accent = when (id) {
        4 -> Color(0xFF8C7CFF)
        5 -> Color(0xFFB861FF)
        6 -> Color(0xFF9FE8FF)
        else -> Color(0xFFFF6C5F)
    }
    val secondary = when (id) {
        4 -> Color(0xFF6EEAFF)
        5 -> Color(0xFF59E8FF)
        6 -> Color.White
        else -> Color(0xFFFFC85A)
    }

    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        val center = Offset(s * .5f, s * .5f)

        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(Color.White.copy(alpha = .08f), accent.copy(alpha = .10f), Color.Transparent),
                    center = Offset(s * .43f, s * .37f),
                    radius = s * .48f
                ),
                radius = s * .46f,
                center = center
            )
            drawArc(
                secondary.copy(alpha = .28f),
                212f,
                54f,
                false,
                Offset(s * .095f, s * .095f),
                Size(s * .81f, s * .81f),
                style = Stroke(s * .006f)
            )
        }
        if (stage >= 6) {
            drawArc(
                accent.copy(alpha = .34f),
                18f,
                118f,
                false,
                Offset(s * .075f, s * .075f),
                Size(s * .85f, s * .85f),
                style = Stroke(s * .006f)
            )
            drawArc(
                Color.White.copy(alpha = .22f),
                198f,
                72f,
                false,
                Offset(s * .12f, s * .12f),
                Size(s * .76f, s * .76f),
                style = Stroke(s * .004f)
            )
        }
        if (stage >= 7) {
            repeat(8) { i ->
                val angle = i * 2f * PI.toFloat() / 8f - PI.toFloat() / 2f
                val node = Offset(
                    center.x + cos(angle) * s * .445f,
                    center.y + sin(angle) * s * .445f
                )
                drawCircle(Color.Black.copy(alpha = .34f), s * .014f, node)
                drawCircle(if (i % 2 == 0) secondary else accent, s * .007f, node)
            }
        }

        when (id) {
            4 -> {
                if (stage >= 1) {
                    drawRect(accent.copy(.30f), Offset(s * .15f, s * .50f), Size(s * .08f, s * .20f))
                    drawRect(accent.copy(.30f), Offset(s * .77f, s * .50f), Size(s * .08f, s * .20f))
                }
                if (stage >= 2) drawCircle(secondary.copy(.48f), s * .18f, center, style = Stroke(s * .010f))
                if (stage >= 3) repeat(4) { i ->
                    val x = s * (.29f + i * .14f)
                    drawLine(accent.copy(.52f), Offset(x, s * .31f), Offset(x, s * .19f), s * .009f)
                }
                if (stage >= 4) drawArc(Color.White.copy(.50f), 195f, 150f, false, Offset(s * .11f, s * .11f), Size(s * .78f, s * .78f), style = Stroke(s * .013f))
                if (stage >= 5) repeat(6) { i ->
                    val x = s * (.25f + i * .10f)
                    drawCircle(secondary.copy(.68f), s * .010f, Offset(x, s * .75f))
                }
                if (stage >= 6) {
                    drawLine(secondary.copy(.62f), Offset(s * .18f, s * .24f), Offset(s * .82f, s * .24f), s * .008f)
                    drawCircle(accent.copy(.18f), s * .40f, center)
                }
                if (stage >= 7) {
                    drawCircle(Color(0xFFFFE79B).copy(.22f), s * .46f, center)
                    drawCircle(Color(0xFFFFE79B).copy(.78f), s * .45f, center, style = Stroke(s * .010f))
                }
            }

            5 -> {
                if (stage >= 1) repeat(2) { i ->
                    drawRect(accent.copy(.30f), Offset(s * if (i == 0) .11f else .81f, s * .49f), Size(s * .08f, s * .24f))
                }
                if (stage >= 2) drawLine(secondary.copy(.66f), Offset(s * .14f, s * .74f), Offset(s * .86f, s * .74f), s * .013f)
                if (stage >= 3) repeat(3) { i ->
                    drawCircle(secondary.copy(.50f), s * .040f, Offset(s * (.30f + i * .20f), s * .24f))
                }
                if (stage >= 4) drawArc(accent.copy(.56f), 185f, 170f, false, Offset(s * .08f, s * .10f), Size(s * .84f, s * .72f), style = Stroke(s * .012f))
                if (stage >= 5) repeat(4) { i ->
                    val x = s * (.24f + i * .17f)
                    drawLine(secondary.copy(.42f), Offset(x, s * .67f), Offset(x, s * .31f), s * .006f)
                }
                if (stage >= 6) {
                    drawCircle(accent.copy(.16f), s * .42f, center)
                    drawCircle(secondary.copy(.42f), s * .39f, center, style = Stroke(s * .008f))
                }
                if (stage >= 7) {
                    drawArc(Color(0xFFFFD76A).copy(.72f), -30f, 240f, false, Offset(s * .07f, s * .07f), Size(s * .86f, s * .86f), style = Stroke(s * .013f))
                    repeat(5) { i -> drawCircle(Color(0xFFFFD76A), s * .008f, Offset(s * (.30f + i * .10f), s * .18f)) }
                }
            }

            6 -> {
                if (stage >= 1) {
                    drawCircle(accent.copy(.30f), s * .09f, Offset(s * .18f, s * .58f))
                    drawCircle(accent.copy(.30f), s * .09f, Offset(s * .82f, s * .58f))
                }
                if (stage >= 2) drawLine(Color.White.copy(.46f), Offset(s * .16f, s * .67f), Offset(s * .84f, s * .67f), s * .011f)
                if (stage >= 3) repeat(3) { i -> drawCircle(accent.copy(.58f), s * .015f, Offset(s * (.32f + i * .18f), s * .29f)) }
                if (stage >= 4) drawArc(accent.copy(.62f), 200f, 145f, false, Offset(s * .10f, s * .12f), Size(s * .80f, s * .72f), style = Stroke(s * .013f))
                if (stage >= 5) repeat(4) { i ->
                    drawLine(accent.copy(.38f), Offset(s * (.29f + i * .14f), s * .61f), Offset(s * (.29f + i * .14f), s * .37f), s * .006f)
                }
                if (stage >= 6) {
                    drawCircle(Color.White.copy(.13f), s * .40f, center)
                    drawCircle(accent.copy(.44f), s * .44f, center, style = Stroke(s * .008f))
                }
                if (stage >= 7) {
                    drawArc(Color.White.copy(.72f), 20f, 250f, false, Offset(s * .06f, s * .06f), Size(s * .88f, s * .88f), style = Stroke(s * .012f))
                    repeat(6) { i -> drawCircle(Color.White.copy(.90f), s * .007f, Offset(s * (.25f + i * .10f), s * .18f)) }
                }
            }

            7 -> {
                if (stage >= 1) {
                    drawRect(accent.copy(.36f), Offset(s * .12f, s * .49f), Size(s * .10f, s * .21f))
                    drawRect(accent.copy(.36f), Offset(s * .78f, s * .49f), Size(s * .10f, s * .21f))
                }
                if (stage >= 2) drawLine(secondary.copy(.72f), Offset(s * .15f, s * .74f), Offset(s * .85f, s * .74f), s * .013f)
                if (stage >= 3) repeat(4) { i -> drawCircle(accent.copy(.66f), s * .012f, Offset(s * (.29f + i * .14f), s * .30f)) }
                if (stage >= 4) drawArc(secondary.copy(.58f), 200f, 150f, false, Offset(s * .09f, s * .10f), Size(s * .82f, s * .80f), style = Stroke(s * .013f))
                if (stage >= 5) repeat(3) { i ->
                    drawLine(secondary.copy(.42f), Offset(s * (.34f + i * .16f), s * .64f), Offset(s * (.34f + i * .16f), s * .34f), s * .006f)
                }
                if (stage >= 6) {
                    drawCircle(secondary.copy(.14f), s * .42f, center)
                    drawCircle(accent.copy(.45f), s * .44f, center, style = Stroke(s * .009f))
                }
                if (stage >= 7) {
                    drawArc(secondary.copy(.78f), -25f, 250f, false, Offset(s * .06f, s * .06f), Size(s * .88f, s * .88f), style = Stroke(s * .013f))
                    repeat(5) { i -> drawCircle(secondary, s * .008f, Offset(s * (.30f + i * .10f), s * .18f)) }
                }
            }
        }

        val revealIntensity = reveal.value.coerceIn(0f, 1f)
        if (revealIntensity > 0f) {
            val travel = 1f - revealIntensity
            val sweepRadius = s * (.31f + .16f * travel)

            // Expansion tiers assemble like powered machinery: a core ignition, segmented
            // pressure rings and short orthogonal energy rails. This is transient only.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .16f * revealIntensity),
                        secondary.copy(alpha = .13f * revealIntensity),
                        Color.Transparent
                    ),
                    center = center,
                    radius = s * .48f
                ),
                radius = s * (.33f + .11f * travel),
                center = center
            )
            drawCircle(
                color = accent.copy(alpha = .78f * revealIntensity),
                radius = sweepRadius,
                center = center,
                style = Stroke(s * (.010f + .006f * revealIntensity))
            )
            drawArc(
                color = secondary.copy(alpha = .68f * revealIntensity),
                startAngle = -34f + 28f * travel,
                sweepAngle = 68f,
                useCenter = false,
                topLeft = Offset(center.x - sweepRadius * 1.08f, center.y - sweepRadius * 1.08f),
                size = Size(sweepRadius * 2.16f, sweepRadius * 2.16f),
                style = Stroke(s * .008f)
            )
            drawArc(
                color = Color.White.copy(alpha = .46f * revealIntensity),
                startAngle = 146f + 22f * travel,
                sweepAngle = 54f,
                useCenter = false,
                topLeft = Offset(center.x - sweepRadius * .88f, center.y - sweepRadius * .88f),
                size = Size(sweepRadius * 1.76f, sweepRadius * 1.76f),
                style = Stroke(s * .005f)
            )

            val railLength = s * (.10f + .09f * travel)
            val railOffset = s * (.28f + .10f * travel)
            val railWidth = s * (.008f + .004f * revealIntensity)
            drawLine(accent.copy(alpha = .66f * revealIntensity), Offset(center.x - railOffset, center.y), Offset(center.x - railOffset - railLength, center.y), railWidth)
            drawLine(accent.copy(alpha = .66f * revealIntensity), Offset(center.x + railOffset, center.y), Offset(center.x + railOffset + railLength, center.y), railWidth)
            drawLine(secondary.copy(alpha = .62f * revealIntensity), Offset(center.x, center.y - railOffset), Offset(center.x, center.y - railOffset - railLength), railWidth)
            drawLine(secondary.copy(alpha = .62f * revealIntensity), Offset(center.x, center.y + railOffset), Offset(center.x, center.y + railOffset + railLength), railWidth)

            if (!lowPower) {
                repeat(4) { i ->
                    val angle = i * PI.toFloat() / 2f + PI.toFloat() / 4f
                    val nodeRadius = s * (.35f + .10f * travel)
                    val node = Offset(
                        center.x + cos(angle) * nodeRadius,
                        center.y + sin(angle) * nodeRadius
                    )
                    drawCircle(Color.Black.copy(alpha = .25f * revealIntensity), s * .018f, node)
                    drawCircle(if (i % 2 == 0) secondary else accent, s * .009f, node, alpha = .82f * revealIntensity)
                }
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/BusinessGroup03Art.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** AAA art pass for Group 03: Dyson Network, Galactic Exchange, Intergalactic Gateway, Cosmic Foundry. */
@Composable
fun BusinessGroup03Sprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val motion = if (reduced) null else rememberInfiniteTransition(label = "group03-$id")
    val phase = if (motion == null) .24f else {
        val phaseAnim by motion.animateFloat(
            0f, 1f,
            infiniteRepeatable(tween(if (lowPower) 12_000 else 7_400 + id * 220, easing = LinearEasing)),
            label = "phase"
        )
        phaseAnim
    }
    val pulse = if (reduced) .90f else .86f + .08f * ((sin(phase * 2f * PI.toFloat() - PI.toFloat() / 2f) + 1f) * .5f)
    val stage = group03Stage(level)
    val accent = group03Accent(id)

    Box(
        modifier = modifier
            .size(iconSize)
            .background(
                Brush.radialGradient(
                    0f to accent.copy(alpha = .25f + stage * .018f),
                    .48f to EmpireColors.SurfaceHigh,
                    1f to EmpireColors.Void
                ),
                RoundedCornerShape(iconSize * .27f)
            )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val c = Offset(s * .5f, s * .52f)
            drawCircle(Brush.radialGradient(listOf(accent.copy(alpha=.18f*pulse), Color.Transparent), c, s*.46f), s*.46f, c)
            drawCircle(accent.copy(alpha=.32f), s*.41f, c, style=Stroke(s*.011f))
            val starCount = if (lowPower) 10 else 20
            repeat(starCount) { i ->
                val a = i * 2f * PI.toFloat() / starCount
                val r = s * (.34f + (i % 3) * .045f)
                drawCircle(Color.White.copy(alpha=.18f + (i%4)*.06f), if(i%5==0)s*.009f else s*.005f, Offset(c.x+cos(a)*r,c.y+sin(a)*r))
            }
            when (id.coerceIn(8, 11)) {
                8 -> drawDysonNetworkAAA(stage, phase, pulse, lowPower)
                9 -> drawGalacticExchangeAAA(stage, phase, pulse, lowPower)
                10 -> drawIntergalacticGatewayAAA(stage, phase, pulse, lowPower)
                else -> drawCosmicFoundryAAA(stage, phase, pulse, lowPower)
            }
            if (stage >= 1) drawGroup03Ring(accent, phase, .435f, if(lowPower)3 else 5)
            if (stage >= 2) drawGroup03Ring(Color.White, 1f-phase, .475f, if(lowPower)4 else 7)
            if (stage >= 3) drawGroup03Spokes(accent, phase, if(lowPower)6 else 12)
            if (stage >= 4) drawGroup03Crown(accent, phase)
            if (stage >= 5) drawGroup03Mastery(accent, pulse, lowPower)
        }
    }
}

private fun group03Stage(level:Int)=when{level>=1000->5;level>=500->4;level>=250->3;level>=100->2;level>=25->1;else->0}
private fun group03Accent(id:Int)=when(id){8->Color(0xFFFFD45A);9->Color(0xFF5BE6FF);10->Color(0xFF9F7CFF);else->Color(0xFFFF65D7)}

private fun DrawScope.drawDysonNetworkAAA(stage:Int, phase:Float, pulse:Float, lowPower:Boolean){
    val s=size.minDimension; val c=Offset(s*.5f,s*.50f); val gold=group03Accent(8); val white=Color(0xFFFFF3C2)
    drawCircle(Brush.radialGradient(listOf(Color.White,Color(0xFFFFEE9A),Color(0xFFFFB42F),Color.Transparent),c,s*.18f),s*.18f,c)
    drawCircle(gold.copy(alpha=.55f),s*.25f,c,style=Stroke(s*.018f))
    drawCircle(white.copy(alpha=.35f),s*.31f,c,style=Stroke(s*.010f))
    val panels=if(lowPower)8 else 16
    repeat(panels){i-> val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/panels; val p=Offset(c.x+cos(a)*s*.31f,c.y+sin(a)*s*.31f); drawRoundRect(gold.copy(alpha=.78f),Offset(p.x-s*.028f,p.y-s*.014f),Size(s*.056f,s*.028f),CornerRadius(s*.006f))}
    if(stage>=1) drawCircle(gold.copy(alpha=.28f*pulse),s*.36f,c,style=Stroke(s*.014f))
    if(stage>=2) repeat(if(lowPower)4 else 8){i->val a=-phase*2f*PI.toFloat()+i*PI.toFloat()/4f;val p=Offset(c.x+cos(a)*s*.38f,c.y+sin(a)*s*.20f);drawCircle(white,s*.010f,p)}
    if(stage>=3) repeat(6){i->val a=i*PI.toFloat()/3f;drawLine(gold.copy(alpha=.45f),Offset(c.x+cos(a)*s*.18f,c.y+sin(a)*s*.18f),Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f),s*.007f)}
    if(stage>=4) drawArc(white.copy(alpha=.55f),-20f+phase*25f,260f,false,Offset(s*.10f,s*.10f),Size(s*.80f,s*.80f),style=Stroke(s*.012f))
    if(stage>=5) drawCircle(gold.copy(alpha=.16f*pulse),s*.43f,c)
}

private fun DrawScope.drawGalacticExchangeAAA(stage:Int, phase:Float, pulse:Float, lowPower:Boolean){
    val s=size.minDimension; val c=Offset(s*.5f,s*.52f); val cyan=group03Accent(9); val violet=Color(0xFF7D78FF)
    drawOval(Color(0xFF182238),Offset(s*.18f,s*.57f),Size(s*.64f,s*.18f))
    repeat(3){r->drawOval(if(r%2==0)cyan.copy(alpha=.55f) else violet.copy(alpha=.45f),Offset(s*(.22f+r*.04f),s*(.36f+r*.055f)),Size(s*(.56f-r*.08f),s*(.27f-r*.05f)),style=Stroke(s*.015f))}
    drawRoundRect(Color(0xFF26334D),Offset(s*.38f,s*.33f),Size(s*.24f,s*.32f),CornerRadius(s*.035f))
    drawRoundRect(cyan.copy(alpha=.55f),Offset(s*.42f,s*.38f),Size(s*.16f,s*.19f),CornerRadius(s*.020f))
    val traderCount = if(lowPower)4 else 9
    repeat(traderCount){i->val a=phase*2*PI+i*2*PI/traderCount;val x=c.x+cos(a).toFloat()*s*.34f;val y=c.y+sin(a).toFloat()*s*.13f;drawCircle(if(i%2==0)cyan else Color(0xFFFFD36A),s*.009f,Offset(x,y))}
    if(stage>=1) drawArc(cyan.copy(alpha=.55f),180f+phase*35f,170f,false,Offset(s*.13f,s*.17f),Size(s*.74f,s*.64f),style=Stroke(s*.010f))
    if(stage>=2) repeat(4){i->drawLine(violet.copy(alpha=.45f),Offset(s*(.29f+i*.14f),s*.68f),Offset(s*(.34f+i*.10f),s*.42f),s*.006f)}
    if(stage>=3) drawCircle(cyan.copy(alpha=.11f*pulse),s*.34f,c)
    if(stage>=4) repeat(3){i->drawCircle(Color.White.copy(alpha=.8f),s*.009f,Offset(s*(.38f+i*.12f),s*.28f))}
    if(stage>=5) drawArc(Color.White.copy(alpha=.52f),-30f+phase*20f,280f,false,Offset(s*.08f,s*.08f),Size(s*.84f,s*.84f),style=Stroke(s*.012f))
}

private fun DrawScope.drawIntergalacticGatewayAAA(stage:Int, phase:Float, pulse:Float, lowPower:Boolean){
    val s=size.minDimension; val c=Offset(s*.5f,s*.51f); val violet=group03Accent(10); val cyan=Color(0xFF6EEBFF)
    drawCircle(Color(0xFF121629),s*.25f,c)
    drawCircle(violet.copy(alpha=.75f),s*.25f,c,style=Stroke(s*.045f))
    drawCircle(cyan.copy(alpha=.55f),s*.18f,c,style=Stroke(s*.020f))
    val aperture=s*(.11f+.015f*pulse);drawCircle(Brush.radialGradient(listOf(Color.White,violet,Color.Transparent),c,aperture),aperture,c)
    repeat(if(lowPower)4 else 8){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/4f; val inner=Offset(c.x+cos(a)*s*.27f,c.y+sin(a)*s*.27f); val outer=Offset(c.x+cos(a)*s*.38f,c.y+sin(a)*s*.38f);drawLine(if(i%2==0)violet else cyan,inner,outer,s*.018f)}
    if(stage>=1) drawCircle(violet.copy(alpha=.25f),s*.34f,c,style=Stroke(s*.012f))
    if(stage>=2) repeat(if(lowPower)3 else 6){i->val a=-phase*2f*PI.toFloat()+i*PI.toFloat()/3f;drawCircle(Color.White.copy(alpha=.82f),s*.010f,Offset(c.x+cos(a)*s*.36f,c.y+sin(a)*s*.20f))}
    if(stage>=3) drawArc(cyan.copy(alpha=.55f),195f+phase*22f,150f,false,Offset(s*.10f,s*.12f),Size(s*.80f,s*.76f),style=Stroke(s*.012f))
    if(stage>=4) drawCircle(violet.copy(alpha=.13f*pulse),s*.42f,c)
    if(stage>=5) repeat(5){i->drawCircle(Color.White,s*.008f,Offset(s*(.30f+i*.10f),s*.18f))}
}

private fun DrawScope.drawCosmicFoundryAAA(stage:Int, phase:Float, pulse:Float, lowPower:Boolean){
    val s=size.minDimension; val c=Offset(s*.5f,s*.52f); val magenta=group03Accent(11); val gold=Color(0xFFFFC85A)
    val body=Path().apply{moveTo(s*.20f,s*.70f);lineTo(s*.26f,s*.40f);lineTo(s*.38f,s*.32f);lineTo(s*.50f,s*.20f);lineTo(s*.62f,s*.32f);lineTo(s*.74f,s*.40f);lineTo(s*.80f,s*.70f);close()}
    drawPath(body,Brush.verticalGradient(listOf(Color(0xFF452550),Color(0xFF171527))))
    drawPath(body,magenta.copy(alpha=.68f),style=Stroke(s*.014f))
    drawCircle(Brush.radialGradient(listOf(Color.White,gold,magenta.copy(alpha=.45f),Color.Transparent),c,s*.15f),s*.15f,c)
    repeat(if(lowPower)3 else 6){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/3f;val p=Offset(c.x+cos(a)*s*.23f,c.y+sin(a)*s*.15f);drawCircle(if(i%2==0)gold else magenta,s*.014f,p)}
    if(stage>=1) repeat(3){i->drawRoundRect(magenta.copy(alpha=.55f),Offset(s*(.30f+i*.16f),s*.58f),Size(s*.075f,s*.12f),CornerRadius(s*.012f))}
    if(stage>=2) drawArc(gold.copy(alpha=.52f),205f+phase*18f,130f,false,Offset(s*.15f,s*.13f),Size(s*.70f,s*.70f),style=Stroke(s*.012f))
    if(stage>=3) repeat(4){i->drawLine(magenta.copy(alpha=.55f),Offset(s*.50f,s*.22f),Offset(s*(.23f+i*.18f),s*.76f),s*.007f)}
    if(stage>=4) drawCircle(magenta.copy(alpha=.14f*pulse),s*.38f,c)
    if(stage>=5) repeat(7){i->drawCircle(Color.White.copy(alpha=.8f),s*.007f,Offset(s*(.27f+i*.075f),s*.16f))}
}

private fun DrawScope.drawGroup03Ring(color:Color,phase:Float,radius:Float,nodes:Int){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);drawCircle(color.copy(alpha=.26f),s*radius,c,style=Stroke(s*.008f));repeat(nodes){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes;drawCircle(color.copy(alpha=.86f),s*.009f,Offset(c.x+cos(a)*s*radius,c.y+sin(a)*s*radius))}}
private fun DrawScope.drawGroup03Spokes(color:Color,phase:Float,count:Int){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);repeat(count){i->val a=phase*PI.toFloat()*.28f+i*2f*PI.toFloat()/count;drawLine(color.copy(alpha=.30f),Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f),Offset(c.x+cos(a)*s*.49f,c.y+sin(a)*s*.49f),s*.006f)}}
private fun DrawScope.drawGroup03Crown(color:Color,phase:Float){val s=size.minDimension;drawArc(Color(0xFFFFE48A).copy(alpha=.62f),-45f+phase*18f,250f,false,Offset(s*.07f,s*.07f),Size(s*.86f,s*.86f),style=Stroke(s*.011f));drawArc(color.copy(alpha=.42f),165f-phase*15f,170f,false,Offset(s*.11f,s*.11f),Size(s*.78f,s*.78f),style=Stroke(s*.008f))}
private fun DrawScope.drawGroup03Mastery(color:Color,pulse:Float,lowPower:Boolean){val s=size.minDimension;val c=Offset(s*.5f,s*.52f);drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.13f*pulse),color.copy(alpha=.10f),Color.Transparent),c,s*.52f),s*.52f,c);repeat(if(lowPower)5 else 10){i->val a=i*2f*PI.toFloat()/(if(lowPower)5 else 10);drawCircle(Color.White.copy(alpha=.75f),s*.006f,Offset(c.x+cos(a)*s*.46f,c.y+sin(a)*s*.46f))}}
```

## File: src/main/java/com/zerotoempire/game/BusinessGroup03Evolution.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun BusinessGroup03Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val stage = when {
        level >= 1000 -> 7
        level >= 500 -> 6
        level >= 250 -> 5
        level >= 100 -> 4
        level >= 50 -> 3
        level >= 25 -> 2
        level >= 10 -> 1
        else -> 0
    }

    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val reveal = remember(id) { Animatable(0f) }
    val previousStage = remember(id) { intArrayOf(stage) }

    LaunchedEffect(stage, reducedMotion) {
        val prior = previousStage[0]
        previousStage[0] = stage
        if (stage > prior && !reducedMotion) {
            reveal.snapTo(1f)
            reveal.animateTo(0f, tween(980))
        } else if (reducedMotion && reveal.value != 0f) {
            reveal.snapTo(0f)
        }
    }

    if (stage == 0) return

    val accent = when (id) {
        8 -> Color(0xFFFFD45A)
        9 -> Color(0xFF5BE6FF)
        10 -> Color(0xFF9F7CFF)
        else -> Color(0xFFFF65D7)
    }
    val secondary = when (id) {
        8 -> Color(0xFFFFF2B0)
        9 -> Color(0xFF8C88FF)
        10 -> Color(0xFF6EEBFF)
        else -> Color(0xFFFFC85A)
    }

    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        val c = Offset(s * .5f, s * .52f)

        if (stage >= 1) {
            drawCircle(accent.copy(alpha = .32f), s * .36f, c, style = Stroke(s * .008f))
            drawCircle(secondary.copy(alpha = .58f), s * .010f, Offset(s * .22f, s * .72f))
            drawCircle(secondary.copy(alpha = .58f), s * .010f, Offset(s * .78f, s * .72f))
        }
        if (stage >= 2) {
            drawArc(secondary.copy(alpha = .48f), 195f, 150f, false, Offset(s * .13f, s * .15f), Size(s * .74f, s * .70f), style = Stroke(s * .009f))
        }
        if (stage >= 3) {
            repeat(4) { i ->
                val x = s * (.29f + i * .14f)
                drawLine(accent.copy(alpha = .45f), Offset(x, s * .68f), Offset(x, s * .34f), s * .005f)
            }
        }
        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(Color.White.copy(alpha = .08f), accent.copy(alpha = .12f), Color.Transparent),
                    center = Offset(s * .42f, s * .37f),
                    radius = s * .50f
                ),
                radius = s * .45f,
                center = c
            )
            drawCircle(accent.copy(alpha = .12f), s * .42f, c)
            drawCircle(secondary.copy(alpha = .36f), s * .43f, c, style = Stroke(s * .008f))
            drawArc(Color.White.copy(alpha = .18f), 208f, 58f, false, Offset(s * .12f, s * .14f), Size(s * .76f, s * .72f), style = Stroke(s * .004f))
        }
        if (stage >= 5) {
            repeat(6) { i ->
                drawCircle(secondary.copy(alpha = .72f), s * .007f, Offset(s * (.25f + i * .10f), s * .18f))
            }
            drawArc(secondary.copy(alpha = .24f), 24f, 112f, false, Offset(s * .095f, s * .115f), Size(s * .81f, s * .77f), style = Stroke(s * .005f))
        }
        if (stage >= 6) {
            drawArc(accent.copy(alpha = .68f), -35f, 250f, false, Offset(s * .07f, s * .07f), Size(s * .86f, s * .86f), style = Stroke(s * .012f))
            drawArc(secondary.copy(alpha = .42f), 165f, 170f, false, Offset(s * .11f, s * .11f), Size(s * .78f, s * .78f), style = Stroke(s * .007f))
            repeat(6) { i ->
                val angle = i * 2f * PI.toFloat() / 6f - PI.toFloat() / 2f
                val node = Offset(c.x + cos(angle) * s * .405f, c.y + sin(angle) * s * .405f)
                drawCircle(Color.Black.copy(alpha = .32f), s * .013f, node)
                drawCircle(if (i % 2 == 0) secondary else accent, s * .0065f, node)
            }
        }
        if (stage >= 7) {
            drawCircle(Color.White.copy(alpha = .10f), s * .48f, c)
            drawCircle(accent.copy(alpha = .24f), s * .475f, c, style = Stroke(s * .018f))
            drawCircle(secondary.copy(alpha = .78f), s * .462f, c, style = Stroke(s * .008f))
            repeat(10) { i ->
                val angle = i * 2f * PI.toFloat() / 10f - PI.toFloat() / 2f
                val node = Offset(c.x + cos(angle) * s * .468f, c.y + sin(angle) * s * .468f)
                drawCircle(Color.Black.copy(alpha = .38f), s * .014f, node)
                drawCircle(if (i % 2 == 0) Color.White.copy(alpha = .92f) else secondary, s * .0065f, node)
            }
        }

        val revealIntensity = reveal.value.coerceIn(0f, 1f)
        if (revealIntensity > 0f) {
            val travel = 1f - revealIntensity
            val gravityRadius = s * (.22f + .25f * travel)

            // Megastructure tiers arrive with a slower, heavier convergence beat: a dense
            // gravity well, two pressure fronts and massive radial braces instead of sparks.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .14f * revealIntensity),
                        accent.copy(alpha = .17f * revealIntensity),
                        secondary.copy(alpha = .07f * revealIntensity),
                        Color.Transparent
                    ),
                    center = c,
                    radius = s * .50f
                ),
                radius = s * (.31f + .12f * travel),
                center = c
            )
            drawCircle(
                color = accent.copy(alpha = .70f * revealIntensity),
                radius = gravityRadius,
                center = c,
                style = Stroke(width = s * (.010f + .008f * revealIntensity))
            )
            drawCircle(
                color = secondary.copy(alpha = .48f * revealIntensity),
                radius = gravityRadius + s * .055f,
                center = c,
                style = Stroke(width = s * .006f)
            )

            val braceCount = 8
            repeat(braceCount) { i ->
                val angle = i * 2f * PI.toFloat() / braceCount + id * .13f
                val inner = s * (.17f + .05f * travel)
                val outer = s * (.34f + .11f * travel)
                drawLine(
                    color = if (i % 2 == 0) accent else secondary,
                    start = Offset(c.x + cos(angle) * inner, c.y + sin(angle) * inner),
                    end = Offset(c.x + cos(angle) * outer, c.y + sin(angle) * outer),
                    strokeWidth = s * if (i % 2 == 0) .010f else .006f,
                    alpha = (.30f + .55f * revealIntensity).coerceAtMost(1f)
                )
            }

            repeat(4) { i ->
                val angle = i * PI.toFloat() / 2f + PI.toFloat() / 4f
                val nodeRadius = s * (.37f + .08f * travel)
                val node = Offset(c.x + cos(angle) * nodeRadius, c.y + sin(angle) * nodeRadius)
                drawCircle(Color.Black.copy(alpha = .34f * revealIntensity), s * .016f, node)
                drawCircle(secondary.copy(alpha = .82f * revealIntensity), s * .0075f, node)
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/BusinessGroup04Art.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Final business tier: reality-scale machinery and transcendent infrastructure. */
@Composable
fun BusinessGroup04Sprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase: Float
    if (reduced) {
        phase = .21f
    } else {
        val motion = rememberInfiniteTransition(label = "group04-$id")
        val phaseAnim by motion.animateFloat(0f,1f,infiniteRepeatable(tween(if(lowPower)14000 else 8200,easing=LinearEasing)),label="phase")
        phase = phaseAnim
    }
    val pulse = if (reduced) .90f else .87f + .08f * ((sin(phase * 2f * PI.toFloat() - PI.toFloat() / 2f) + 1f) * .5f)
    val stage=when{level>=1000->5;level>=500->4;level>=250->3;level>=100->2;level>=25->1;else->0}
    val accent=if(id==12) Color(0xFFFF68D8) else Color(0xFFFFE36E)

    Box(modifier.size(iconSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.24f),EmpireColors.SurfaceHigh,EmpireColors.Void)),RoundedCornerShape(iconSize*.28f))){
        Canvas(Modifier.fillMaxSize()){
            val s=size.minDimension;val c=Offset(s*.5f,s*.51f)
            drawCircle(accent.copy(alpha=.10f*pulse),s*.47f,c)
            drawCircle(accent.copy(alpha=.32f),s*.42f,c,style=Stroke(s*.010f))
            if(id==12) drawRealityEngineFinal(stage,phase,pulse,lowPower) else drawTranscendentNexusFinal(stage,phase,pulse,lowPower)
            if(stage>=1) drawCircle(accent.copy(alpha=.34f),s*.45f,c,style=Stroke(s*.008f))
            if(stage>=2) repeat(if(lowPower)4 else 8){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/4f;drawCircle(Color.White.copy(alpha=.80f),s*.008f,Offset(c.x+cos(a)*s*.45f,c.y+sin(a)*s*.45f))}
            if(stage>=3) drawArc(Color.White.copy(alpha=.38f),phase*360f,245f,false,Offset(s*.035f,s*.035f),Size(s*.93f,s*.93f),style=Stroke(s*.008f))
            if(stage>=4) drawArc(accent.copy(alpha=.55f),180f-phase*270f,150f,false,Offset(s*.07f,s*.07f),Size(s*.86f,s*.86f),style=Stroke(s*.012f))
            if(stage>=5){drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.16f*pulse),accent.copy(alpha=.08f),Color.Transparent),c,s*.52f),s*.52f,c);repeat(if(lowPower)6 else 12){i->val a=i*2f*PI.toFloat()/(if(lowPower)6 else 12);drawCircle(Color.White,s*.006f,Offset(c.x+cos(a)*s*.49f,c.y+sin(a)*s*.49f))}}
        }
    }
}

private fun DrawScope.drawRealityEngineFinal(stage:Int,phase:Float,pulse:Float,lowPower:Boolean){
    val s=size.minDimension;val c=Offset(s*.5f,s*.51f);val pink=Color(0xFFFF68D8);val cyan=Color(0xFF6EEBFF)
    repeat(4){r->val rx=s*(.12f+r*.055f);val ry=rx*(.48f+r*.08f);drawArc(if(r%2==0)pink.copy(alpha=.82f-r*.12f) else cyan.copy(alpha=.72f-r*.10f),phase*360f*(if(r%2==0)1 else -1)+r*47f,255f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(s*(.024f-r*.003f)))}
    drawCircle(Brush.radialGradient(listOf(Color.White,pink.copy(alpha=.82f),Color.Transparent),c,s*.105f),s*.105f,c)
    val nodes=if(lowPower)5 else 10;repeat(nodes){i->val a=-phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes;drawCircle(if(i%2==0)cyan else pink,s*.010f,Offset(c.x+cos(a)*s*.31f,c.y+sin(a)*s*.19f))}
    if(stage>=2){val diamond=Path().apply{moveTo(c.x,s*.13f);lineTo(s*.79f,c.y);lineTo(c.x,s*.87f);lineTo(s*.21f,c.y);close()};drawPath(diamond,pink.copy(alpha=.30f),style=Stroke(s*.009f))}
    if(stage>=4) repeat(4){i->val a=i*PI.toFloat()/2f+phase;drawLine(color=pink.copy(alpha=.40f),start=c,end=Offset(c.x+cos(a)*s*.37f,c.y+sin(a)*s*.37f),strokeWidth=s*.006f)}
}

private fun DrawScope.drawTranscendentNexusFinal(stage:Int,phase:Float,pulse:Float,lowPower:Boolean){
    val s=size.minDimension;val c=Offset(s*.5f,s*.51f);val gold=Color(0xFFFFE36E);val violet=Color(0xFFC68BFF)
    drawCircle(Brush.radialGradient(listOf(Color.White,gold.copy(alpha=.86f),violet.copy(alpha=.34f),Color.Transparent),c,s*.18f),s*.18f,c)
    repeat(3){r->drawCircle(if(r%2==0)gold.copy(alpha=.72f-r*.15f) else violet.copy(alpha=.58f),s*(.22f+r*.065f),c,style=Stroke(s*(.020f-r*.004f)))}
    val rays=if(lowPower)6 else 12;repeat(rays){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/rays;val inner=s*.20f;val outer=s*(.32f+(i%3)*.045f);drawLine(color=if(i%2==0)gold else violet,start=Offset(c.x+cos(a)*inner,c.y+sin(a)*inner),end=Offset(c.x+cos(a)*outer,c.y+sin(a)*outer),strokeWidth=s*.012f)}
    if(stage>=2) repeat(6){i->val a=-phase*PI.toFloat()+i*PI.toFloat()/3f;drawCircle(Color.White.copy(alpha=.88f),s*.009f,Offset(c.x+cos(a)*s*.37f,c.y+sin(a)*s*.23f))}
    if(stage>=3) drawCircle(gold.copy(alpha=.12f*pulse),s*.39f,c)
    if(stage>=4) drawArc(violet.copy(alpha=.55f),-30f+phase*40f,300f,false,Offset(s*.09f,s*.09f),Size(s*.82f,s*.82f),style=Stroke(s*.011f))
}
```

## File: src/main/java/com/zerotoempire/game/BusinessGroup04Evolution.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun BusinessGroup04Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val stage = when {
        level >= 1000 -> 7
        level >= 500 -> 6
        level >= 250 -> 5
        level >= 100 -> 4
        level >= 50 -> 3
        level >= 25 -> 2
        level >= 10 -> 1
        else -> 0
    }

    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val reveal = remember(id) { Animatable(0f) }
    val previousStage = remember(id) { intArrayOf(stage) }

    LaunchedEffect(stage, reducedMotion) {
        val prior = previousStage[0]
        previousStage[0] = stage
        if (stage > prior && !reducedMotion) {
            reveal.snapTo(1f)
            reveal.animateTo(0f, tween(1120))
        } else if (reducedMotion && reveal.value != 0f) {
            reveal.snapTo(0f)
        }
    }

    if (stage == 0) return

    val accent = if (id == 12) Color(0xFFFF68D8) else Color(0xFFFFE36E)
    val secondary = if (id == 12) Color(0xFF6EEBFF) else Color(0xFFC68BFF)

    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        val c = Offset(s * .5f, s * .51f)

        if (stage >= 1) {
            drawCircle(accent.copy(alpha = .30f), s * .35f, c, style = Stroke(s * .008f))
            drawCircle(secondary.copy(alpha = .68f), s * .008f, Offset(s * .23f, s * .71f))
            drawCircle(secondary.copy(alpha = .68f), s * .008f, Offset(s * .77f, s * .71f))
        }
        if (stage >= 2) {
            drawArc(
                secondary.copy(alpha = .50f),
                205f,
                130f,
                false,
                Offset(s * .15f, s * .14f),
                Size(s * .70f, s * .72f),
                style = Stroke(s * .009f)
            )
        }
        if (stage >= 3) {
            repeat(4) { i ->
                val x = s * (.30f + i * .13f)
                drawLine(accent.copy(alpha = .48f), Offset(x, s * .69f), Offset(x, s * .31f), s * .005f)
            }
        }
        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .05f),
                        accent.copy(alpha = .10f),
                        secondary.copy(alpha = .04f),
                        Color.Transparent
                    ),
                    center = c,
                    radius = s * .47f
                ),
                radius = s * .47f,
                center = c
            )
            drawCircle(secondary.copy(alpha = .40f), s * .43f, c, style = Stroke(s * .008f))
            drawCircle(accent.copy(alpha = .18f), s * .395f, c, style = Stroke(s * .005f))
        }
        if (stage >= 5) {
            repeat(6) { i ->
                val a = -PI.toFloat() * .82f + i * PI.toFloat() * .164f
                val radius = s * .405f
                val p = Offset(c.x + cos(a) * radius, c.y + sin(a) * radius)
                drawCircle(Color.White.copy(alpha = .82f), s * .007f, p)
                drawCircle(secondary.copy(alpha = .32f), s * .014f, p, style = Stroke(s * .004f))
            }
        }
        if (stage >= 6) {
            drawArc(
                accent.copy(alpha = .72f),
                -30f,
                255f,
                false,
                Offset(s * .065f, s * .065f),
                Size(s * .87f, s * .87f),
                style = Stroke(s * .012f)
            )
            drawArc(
                secondary.copy(alpha = .48f),
                160f,
                175f,
                false,
                Offset(s * .105f, s * .105f),
                Size(s * .79f, s * .79f),
                style = Stroke(s * .007f)
            )
            repeat(8) { i ->
                val a = i * 2f * PI.toFloat() / 8f + .18f
                val r = if (i % 2 == 0) s * .445f else s * .418f
                val p = Offset(c.x + cos(a) * r, c.y + sin(a) * r)
                drawCircle(
                    color = if (i % 2 == 0) accent else secondary,
                    radius = if (i % 2 == 0) s * .008f else s * .006f,
                    center = p,
                    alpha = .86f
                )
            }
        }
        if (stage >= 7) {
            drawCircle(Color.White.copy(alpha = .08f), s * .49f, c)
            drawCircle(Color.White.copy(alpha = .86f), s * .475f, c, style = Stroke(s * .010f))
            drawCircle(accent.copy(alpha = .34f), s * .458f, c, style = Stroke(s * .0045f))

            repeat(12) { i ->
                val a = -PI.toFloat() / 2f + i * 2f * PI.toFloat() / 12f
                val inner = s * .462f
                val outer = s * if (i % 3 == 0) .515f else .495f
                val start = Offset(c.x + cos(a) * inner, c.y + sin(a) * inner)
                val end = Offset(c.x + cos(a) * outer, c.y + sin(a) * outer)
                drawLine(
                    color = if (i % 2 == 0) accent else secondary,
                    start = start,
                    end = end,
                    strokeWidth = if (i % 3 == 0) s * .009f else s * .005f,
                    alpha = if (i % 3 == 0) .88f else .62f
                )
                drawCircle(
                    color = if (i % 2 == 0) Color.White else secondary,
                    radius = if (i % 3 == 0) s * .007f else s * .005f,
                    center = end,
                    alpha = .90f
                )
            }
        }

        val revealIntensity = reveal.value.coerceIn(0f, 1f)
        if (revealIntensity > 0f) {
            val travel = 1f - revealIntensity
            val waveRadius = s * (.18f + .34f * travel)

            // Endgame tiers arrive as a controlled singularity release rather than a generic
            // particle burst, keeping the final businesses visually distinct and premium.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .20f * revealIntensity),
                        accent.copy(alpha = .18f * revealIntensity),
                        secondary.copy(alpha = .10f * revealIntensity),
                        Color.Transparent
                    ),
                    center = c,
                    radius = s * .52f
                ),
                radius = s * (.26f + .20f * travel),
                center = c
            )
            drawCircle(
                color = Color.White.copy(alpha = .72f * revealIntensity),
                radius = waveRadius,
                center = c,
                style = Stroke(width = s * (.010f + .010f * revealIntensity))
            )
            drawCircle(
                color = accent.copy(alpha = .62f * revealIntensity),
                radius = waveRadius + s * .045f,
                center = c,
                style = Stroke(width = s * .006f)
            )
            drawCircle(
                color = secondary.copy(alpha = .38f * revealIntensity),
                radius = waveRadius + s * .080f,
                center = c,
                style = Stroke(width = s * .004f)
            )

            val rayCount = 12
            repeat(rayCount) { i ->
                val angle = -PI.toFloat() / 2f + i * 2f * PI.toFloat() / rayCount + id * .09f
                val inner = s * (.12f + .07f * travel)
                val outer = s * (.31f + .18f * travel)
                drawLine(
                    color = when (i % 3) {
                        0 -> Color.White
                        1 -> accent
                        else -> secondary
                    },
                    start = Offset(c.x + cos(angle) * inner, c.y + sin(angle) * inner),
                    end = Offset(c.x + cos(angle) * outer, c.y + sin(angle) * outer),
                    strokeWidth = s * if (i % 3 == 0) .008f else .005f,
                    alpha = (.22f + .66f * revealIntensity).coerceAtMost(1f)
                )
            }

            repeat(6) { i ->
                val angle = i * PI.toFloat() / 3f + PI.toFloat() / 6f
                val nodeRadius = s * (.30f + .17f * travel)
                val node = Offset(c.x + cos(angle) * nodeRadius, c.y + sin(angle) * nodeRadius)
                drawCircle(Color.Black.copy(alpha = .28f * revealIntensity), s * .017f, node)
                drawCircle(Color.White.copy(alpha = .92f * revealIntensity), s * .0065f, node)
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/CanonicalBusinessRaster.kt
```kotlin
package com.zerotoempire.game

/**
 * Compile-time binding for the complete authored business catalog.
 *
 * Each business 0..13 owns seven production rasters (T0..T6). Keeping the
 * opaque drawable names behind this resolver gives gameplay one canonical
 * level-to-tier contract while making missing packaged art a compile error.
 */
private val canonicalBusinessRasters = arrayOf(
    intArrayOf(
        R.drawable.zte_business_00_t0_final,
        R.drawable.zte_business_00_t1_final,
        R.drawable.zte_business_00_t2_final,
        R.drawable.zte_business_00_t3_final,
        R.drawable.zte_business_00_t4_final,
        R.drawable.zte_business_00_t5_final,
        R.drawable.zte_business_00_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_01_t0_final,
        R.drawable.zte_business_01_t1_final,
        R.drawable.zte_business_01_t2_final,
        R.drawable.zte_business_01_t3_final,
        R.drawable.zte_business_01_t4_final,
        R.drawable.zte_business_01_t5_final,
        R.drawable.zte_business_01_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_02_t0_final,
        R.drawable.zte_business_02_t1_final,
        R.drawable.zte_business_02_t2_final,
        R.drawable.zte_business_02_t3_final,
        R.drawable.zte_business_02_t4_final,
        R.drawable.zte_business_02_t5_final,
        R.drawable.zte_business_02_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_03_t0_final,
        R.drawable.zte_business_03_t1_final,
        R.drawable.zte_business_03_t2_final,
        R.drawable.zte_business_03_t3_final,
        R.drawable.zte_business_03_t4_final,
        R.drawable.zte_business_03_t5_final,
        R.drawable.zte_business_03_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_04_t0_final,
        R.drawable.zte_business_04_t1_final,
        R.drawable.zte_business_04_t2_final,
        R.drawable.zte_business_04_t3_final,
        R.drawable.zte_business_04_t4_final,
        R.drawable.zte_business_04_t5_final,
        R.drawable.zte_business_04_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_05_t0_final,
        R.drawable.zte_business_05_t1_final,
        R.drawable.zte_business_05_t2_final,
        R.drawable.zte_business_05_t3_final,
        R.drawable.zte_business_05_t4_final,
        R.drawable.zte_business_05_t5_final,
        R.drawable.zte_business_05_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_06_t0_final,
        R.drawable.zte_business_06_t1_final,
        R.drawable.zte_business_06_t2_final,
        R.drawable.zte_business_06_t3_final,
        R.drawable.zte_business_06_t4_final,
        R.drawable.zte_business_06_t5_final,
        R.drawable.zte_business_06_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_07_t0_final,
        R.drawable.zte_business_07_t1_final,
        R.drawable.zte_business_07_t2_final,
        R.drawable.zte_business_07_t3_final,
        R.drawable.zte_business_07_t4_final,
        R.drawable.zte_business_07_t5_final,
        R.drawable.zte_business_07_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_08_t0_final,
        R.drawable.zte_business_08_t1_final,
        R.drawable.zte_business_08_t2_final,
        R.drawable.zte_business_08_t3_final,
        R.drawable.zte_business_08_t4_final,
        R.drawable.zte_business_08_t5_final,
        R.drawable.zte_business_08_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_09_t0_final,
        R.drawable.zte_business_09_t1_final,
        R.drawable.zte_business_09_t2_final,
        R.drawable.zte_business_09_t3_final,
        R.drawable.zte_business_09_t4_final,
        R.drawable.zte_business_09_t5_final,
        R.drawable.zte_business_09_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_10_t0_final,
        R.drawable.zte_business_10_t1_final,
        R.drawable.zte_business_10_t2_final,
        R.drawable.zte_business_10_t3_final,
        R.drawable.zte_business_10_t4_final,
        R.drawable.zte_business_10_t5_final,
        R.drawable.zte_business_10_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_11_t0_final,
        R.drawable.zte_business_11_t1_final,
        R.drawable.zte_business_11_t2_final,
        R.drawable.zte_business_11_t3_final,
        R.drawable.zte_business_11_t4_final,
        R.drawable.zte_business_11_t5_final,
        R.drawable.zte_business_11_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_12_t0_final,
        R.drawable.zte_business_12_t1_final,
        R.drawable.zte_business_12_t2_final,
        R.drawable.zte_business_12_t3_final,
        R.drawable.zte_business_12_t4_final,
        R.drawable.zte_business_12_t5_final,
        R.drawable.zte_business_12_t6_final,
    ),
    intArrayOf(
        R.drawable.zte_business_13_t0_final,
        R.drawable.zte_business_13_t1_final,
        R.drawable.zte_business_13_t2_final,
        R.drawable.zte_business_13_t3_final,
        R.drawable.zte_business_13_t4_final,
        R.drawable.zte_business_13_t5_final,
        R.drawable.zte_business_13_t6_final,
    ),
)

internal fun canonicalBusinessRasterRes(businessId: Int, level: Int): Int? {
    val tier = canonicalBusinessTier(level)
    return canonicalBusinessRasters.getOrNull(businessId)?.get(tier)
}
```

## File: src/main/java/com/zerotoempire/game/CanonicalBusinessTier.kt
```kotlin
package com.zerotoempire.game

/**
 * Maps the eight gameplay progression milestones used by business evolution
 * (0, 10, 25, 50, 100, 250, 500, 1000) onto the seven canonical raster tiers
 * T0..T6.
 *
 * The final two gameplay milestones intentionally share T6. This preserves a
 * monotonic visual progression without inventing a non-canonical T7 asset.
 */
internal fun canonicalBusinessTier(level: Int): Int = when {
    level >= 500 -> 6
    level >= 250 -> 5
    level >= 100 -> 4
    level >= 50 -> 3
    level >= 25 -> 2
    level >= 10 -> 1
    else -> 0
}
```

## File: src/main/java/com/zerotoempire/game/CanonicalCharacterRaster.kt
```kotlin
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
```

## File: src/main/java/com/zerotoempire/game/CanonicalFxRaster.kt
```kotlin
package com.zerotoempire.game

/**
 * Semantic contract for authored production VFX whose generation prompts are
 * documented in tools/sprites/hf_sprite_factory.py.
 *
 * Gameplay code uses effect meaning while this resolver owns the opaque
 * production asset ids. Do not add a semantic alias without a documented source.
 */
internal enum class CanonicalFx {
    WELDING_SPARK_BURST,
    SMALL_FURNACE_FLAME,
    LARGE_PLASMA_FLAME,
    INDUSTRIAL_SMOKE_PUFF,
    STEAM_VENT,
    CYAN_ENERGY_PULSE,
    WARM_ENERGY_PULSE,
    CONSTRUCTION_DUST_BURST,
    UPGRADE_CONSTRUCTION_FLASH,
    INCOME_PICKUP_SPARKLE,
    ELECTRIC_ARC,
    HOLOGRAM_SCAN_SWEEP,
    DRONE_THRUSTER,
    PHASE_DISTORTION,
    ORBITAL_ION_TRAIL,
    STELLAR_FLARE,
    SINGULARITY_LENS_PULSE,
    MASTERY_CROWN_SHIMMER,
}

internal fun canonicalFxRasterRes(effect: CanonicalFx): Int = when (effect) {
    CanonicalFx.WELDING_SPARK_BURST -> R.drawable.zte_fx_00_final
    CanonicalFx.SMALL_FURNACE_FLAME -> R.drawable.zte_fx_01_final
    CanonicalFx.LARGE_PLASMA_FLAME -> R.drawable.zte_fx_02_final
    CanonicalFx.INDUSTRIAL_SMOKE_PUFF -> R.drawable.zte_fx_03_final
    CanonicalFx.STEAM_VENT -> R.drawable.zte_fx_04_final
    CanonicalFx.CYAN_ENERGY_PULSE -> R.drawable.zte_fx_05_final
    CanonicalFx.WARM_ENERGY_PULSE -> R.drawable.zte_fx_06_final
    CanonicalFx.CONSTRUCTION_DUST_BURST -> R.drawable.zte_fx_07_final
    CanonicalFx.UPGRADE_CONSTRUCTION_FLASH -> R.drawable.zte_fx_08_final
    CanonicalFx.INCOME_PICKUP_SPARKLE -> R.drawable.zte_fx_09_final
    CanonicalFx.ELECTRIC_ARC -> R.drawable.zte_fx_10_final
    CanonicalFx.HOLOGRAM_SCAN_SWEEP -> R.drawable.zte_fx_11_final
    CanonicalFx.DRONE_THRUSTER -> R.drawable.zte_fx_12_final
    CanonicalFx.PHASE_DISTORTION -> R.drawable.zte_fx_13_final
    CanonicalFx.ORBITAL_ION_TRAIL -> R.drawable.zte_fx_14_final
    CanonicalFx.STELLAR_FLARE -> R.drawable.zte_fx_15_final
    CanonicalFx.SINGULARITY_LENS_PULSE -> R.drawable.zte_fx_16_final
    CanonicalFx.MASTERY_CROWN_SHIMMER -> R.drawable.zte_fx_17_final
}

internal fun powerCorePulseFx(eraIndex: Int): CanonicalFx? = when (eraIndex) {
    in 0..2 -> CanonicalFx.WARM_ENERGY_PULSE
    in 3..5 -> CanonicalFx.CYAN_ENERGY_PULSE
    in 6..8 -> null
    else -> CanonicalFx.WARM_ENERGY_PULSE
}
```

## File: src/main/java/com/zerotoempire/game/CanonicalFxSprite.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.FilterQuality
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlin.math.roundToInt

private const val FX_COLUMNS = 4
private const val FX_ROWS = 2
private const val FX_FRAME_COUNT = FX_COLUMNS * FX_ROWS

internal fun canonicalFxFrameIndex(progress: Float): Int =
    (progress.coerceIn(0f, 1f) * FX_FRAME_COUNT)
        .toInt()
        .coerceIn(0, FX_FRAME_COUNT - 1)

/**
 * Sprite-first renderer for authored 4x2 production VFX sheets.
 *
 * Only one 128x128 source cell is drawn at a time; the sheet itself is never
 * exposed as a single UI image. Runtime drawing may still be layered around the
 * authored frame for motion accents, but does not replace its visual identity.
 */
@Composable
internal fun CanonicalFxSprite(
    effect: CanonicalFx,
    progress: Float,
    modifier: Modifier = Modifier,
    alpha: Float = 1f,
    startScale: Float = .55f,
    endScale: Float = 1.10f,
) {
    val context = LocalContext.current
    val sheet = remember(effect) {
        BitmapFactory.decodeResource(context.resources, canonicalFxRasterRes(effect)).asImageBitmap()
    }
    val p = progress.coerceIn(0f, 1f)
    val scale = startScale + (endScale - startScale) * p
    val frameIndex = canonicalFxFrameIndex(p)
    val frameWidth = sheet.width / FX_COLUMNS
    val frameHeight = sheet.height / FX_ROWS
    val sourceOffset = IntOffset(
        x = (frameIndex % FX_COLUMNS) * frameWidth,
        y = (frameIndex / FX_COLUMNS) * frameHeight,
    )

    Canvas(
        modifier = modifier.graphicsLayer {
            scaleX = scale
            scaleY = scale
        }
    ) {
        val side = size.minDimension.roundToInt().coerceAtLeast(1)
        val destinationOffset = IntOffset(
            x = ((size.width - side) / 2f).roundToInt(),
            y = ((size.height - side) / 2f).roundToInt(),
        )
        drawImage(
            image = sheet,
            srcOffset = sourceOffset,
            srcSize = IntSize(frameWidth, frameHeight),
            dstOffset = destinationOffset,
            dstSize = IntSize(side, side),
            alpha = (alpha * (1f - p)).coerceIn(0f, 1f),
            filterQuality = FilterQuality.High,
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/Challenges.kt
```kotlin
package com.zerotoempire.game

import java.time.LocalDate
import java.time.temporal.WeekFields
import kotlin.math.min

enum class ChallengeMetric { TAPS, PURCHASES, LIFETIME_CASH, PRESTIGES }

data class TimedChallenge(
    val id: String,
    val title: String,
    val description: String,
    val metric: ChallengeMetric,
    val target: Double,
    val rewardGems: Int,
    val progress: Double,
    val claimed: Boolean
) {
    val completed: Boolean get() = progress >= target
    val fraction: Float get() = min(1.0, progress / target).toFloat()
}

object ChallengeRotation {
    fun weeklyKey(date: LocalDate = LocalDate.now()): String {
        val wf = WeekFields.ISO
        return "${date.get(wf.weekBasedYear())}-W${date.get(wf.weekOfWeekBasedYear())}"
    }

    fun current(state: GameState, meta: PlayerMeta, date: LocalDate = LocalDate.now()): List<TimedChallenge> {
        val key = weeklyKey(date)
        val baselineReady = meta.challengeWeekKey == key
        fun claimed(suffix: String) = "$key:$suffix" in meta.claimedChallengeIds
        val weeklyTaps = if (baselineReady) (meta.totalTaps - meta.challengeWeekTapBase).coerceAtLeast(0L).toDouble() else 0.0
        val weeklyPurchases = if (baselineReady) (meta.totalPurchases - meta.challengeWeekPurchaseBase).coerceAtLeast(0L).toDouble() else 0.0
        val weeklyPrestiges = if (baselineReady) (meta.prestigeCount - meta.challengeWeekPrestigeBase).coerceAtLeast(0).toDouble() else 0.0
        return listOf(
            TimedChallenge("$key:tap", "Tap Storm", "Generate capital manually 500 times this week.", ChallengeMetric.TAPS, 500.0, 20, weeklyTaps, claimed("tap")),
            TimedChallenge("$key:scale", "Scale Up", "Purchase 150 business levels this week.", ChallengeMetric.PURCHASES, 150.0, 30, weeklyPurchases, claimed("scale")),
            TimedChallenge("$key:wealth", "Capital Surge", "Reach 10M lifetime cash in the current run.", ChallengeMetric.LIFETIME_CASH, 10_000_000.0, 40, state.lifetimeCash, claimed("wealth")),
            TimedChallenge("$key:ascend", "Legacy Run", "Complete 2 ascensions this week.", ChallengeMetric.PRESTIGES, 2.0, 50, weeklyPrestiges, claimed("ascend"))
        )
    }
}

object ChallengeOrdering {
    fun forCommandCenter(challenges: List<TimedChallenge>): List<TimedChallenge> =
        challenges.sortedBy { challenge ->
            when {
                challenge.completed && !challenge.claimed -> 0
                !challenge.completed -> 1
                else -> 2
            }
        }
}

object BalanceGuard {
    fun recommendedPrestigeWindowSeconds(lifetimeCash: Double): Long = when {
        lifetimeCash < 1e6 -> 900L
        lifetimeCash < 1e9 -> 1_800L
        lifetimeCash < 1e12 -> 3_600L
        lifetimeCash < 1e15 -> 7_200L
        else -> 10_800L
    }

    fun economyHealth(state: GameState): Double {
        if (state.incomePerSecond <= 0.0) return 0.0
        val nextAffordable = state.businesses.minOfOrNull { it.nextCost } ?: return 0.0
        return (state.incomePerSecond / nextAffordable).coerceIn(0.0, 1.0)
    }
}
```

## File: src/main/java/com/zerotoempire/game/ChallengeUi.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import java.time.LocalDate

/** Goals command module: permanent Dynasty campaign rank + rotating weekly challenges. */
@Composable
fun ChallengeDock(vm: GameViewModel, modifier: Modifier = Modifier) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val currentWeek = ChallengeRotation.weeklyKey()
    LaunchedEffect(currentWeek, meta.challengeWeekKey) {
        if (meta.challengeWeekKey != currentWeek) vm.ensureChallengeWeek()
    }
    val challenges = remember(state, meta, currentWeek) { ChallengeRotation.current(state, meta) }
    val dynasty = remember(state.prestigePoints, meta) { DynastyProgression.status(state, meta) }
    val completed = challenges.count { it.completed }
    val unclaimed = challenges.count { it.completed && !it.claimed }
    var open by remember { mutableStateOf(false) }

    Column(modifier, verticalArrangement = Arrangement.spacedBy(9.dp)) {
        Surface(
            color = EmpireColors.Violet.copy(alpha = .10f),
            shape = RoundedCornerShape(22.dp),
            modifier = Modifier
                .fillMaxWidth()
                .border(1.dp, EmpireColors.Violet.copy(alpha = .22f), RoundedCornerShape(22.dp))
        ) {
            Column(Modifier.padding(15.dp)) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    MetaSprite(MetaSpriteKind.ACHIEVEMENT, 42.dp, active = true, progress = dynasty.progress)
                    Spacer(Modifier.width(11.dp))
                    Column(Modifier.weight(1f)) {
                        Text("DYNASTY RANK ${dynasty.rank.level}", color = EmpireColors.Violet, fontSize = 10.sp, fontWeight = FontWeight.Black, letterSpacing = 1.3.sp)
                        Text(dynasty.rank.title.uppercase(), color = EmpireColors.TextPrimary, fontSize = 17.sp, fontWeight = FontWeight.Black)
                        Text(
                            if (dynasty.next == null) "APEX DYNASTY • MAXIMUM RANK" else "Next: Rank ${dynasty.next.level} • ${dynasty.next.title}",
                            color = EmpireColors.TextSecondary,
                            fontSize = 9.sp
                        )
                    }
                    Text("${dynasty.rank.level}/${DynastyProgression.MAX_RANK}", color = EmpireColors.Gold, fontSize = 11.sp, fontWeight = FontWeight.Black)
                }
                Spacer(Modifier.height(10.dp))
                LinearProgressIndicator(
                    progress = { dynasty.progress },
                    modifier = Modifier.fillMaxWidth().height(5.dp),
                    color = EmpireColors.Violet,
                    trackColor = EmpireColors.SurfaceHigh
                )
                Spacer(Modifier.height(6.dp))
                Text(
                    "Permanent renown grows through ascensions, eras, purchases, taps and streaks.",
                    color = Color.White.copy(alpha = .48f),
                    fontSize = 9.sp
                )
            }
        }

        FilledTonalButton(
            onClick = { open = true },
            modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
            shape = RoundedCornerShape(16.dp),
            contentPadding = PaddingValues(horizontal = 14.dp, vertical = 11.dp)
        ) {
            MetaSprite(MetaSpriteKind.MISSION, 25.dp, active = unclaimed > 0)
            Spacer(Modifier.width(8.dp))
            Column(Modifier.weight(1f)) {
                Text("WEEKLY COMMAND", fontSize = 10.sp, fontWeight = FontWeight.Black)
                Text("$completed/${challenges.size} objectives complete", color = EmpireColors.TextSecondary, fontSize = 9.sp)
            }
            Text(if (unclaimed > 0) "$unclaimed CLAIM" else "OPEN", color = if (unclaimed > 0) EmpireColors.Gold else EmpireColors.Cyan, fontSize = 10.sp, fontWeight = FontWeight.Black)
        }
    }

    if (open) {
        ChallengeDialog(
            challenges = challenges,
            onClaim = { vm.claimChallenge(it) },
            onDismiss = { open = false }
        )
    }
}

@Composable
private fun ChallengeDialog(
    challenges: List<TimedChallenge>,
    onClaim: (String) -> Boolean,
    onDismiss: () -> Unit
) {
    val haptics = LocalHapticFeedback.current
    val orderedChallenges = remember(challenges) { ChallengeOrdering.forCommandCenter(challenges) }

    AlertDialog(
        onDismissRequest = onDismiss,
        containerColor = EmpireColors.SurfaceHigh,
        title = {
            Column {
                Text("WEEKLY COMMAND", color = EmpireColors.Gold, fontWeight = FontWeight.Black)
                Text(ChallengeRotation.weeklyKey(LocalDate.now()), color = EmpireColors.TextSecondary, fontSize = 10.sp)
            }
        },
        text = {
            LazyColumn(
                modifier = Modifier.heightIn(max = 440.dp),
                verticalArrangement = Arrangement.spacedBy(9.dp)
            ) {
                items(orderedChallenges, key = { it.id }) { challenge ->
                    Surface(color = EmpireColors.Surface, shape = RoundedCornerShape(14.dp)) {
                        Column(Modifier.fillMaxWidth().padding(12.dp)) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Column(Modifier.weight(1f)) {
                                    Text(challenge.title, color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black)
                                    Text(challenge.description, color = EmpireColors.TextSecondary, fontSize = 10.sp)
                                }
                                Spacer(Modifier.width(8.dp))
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    MetaSprite(MetaSpriteKind.GEM, 20.dp)
                                    Text("${challenge.rewardGems}", color = EmpireColors.Violet, fontWeight = FontWeight.Black, fontSize = 11.sp)
                                }
                            }
                            Spacer(Modifier.height(8.dp))
                            LinearProgressIndicator(
                                progress = { challenge.fraction },
                                modifier = Modifier.fillMaxWidth().height(4.dp),
                                color = if (challenge.completed) EmpireColors.Success else EmpireColors.Cyan,
                                trackColor = EmpireColors.SurfaceHigh
                            )
                            Spacer(Modifier.height(6.dp))
                            val progressText = when (challenge.metric) {
                                ChallengeMetric.LIFETIME_CASH -> "${EmpireNumberFormat.money(challenge.progress)} / ${EmpireNumberFormat.money(challenge.target)}"
                                else -> "${challenge.progress.toLong()} / ${challenge.target.toLong()}"
                            }
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Text(progressText, color = EmpireColors.TextSecondary, fontSize = 9.sp, modifier = Modifier.weight(1f))
                                Spacer(Modifier.width(8.dp))
                                Button(
                                    onClick = { if (onClaim(challenge.id)) haptics.performHapticFeedback(HapticFeedbackType.LongPress) },
                                    enabled = challenge.completed && !challenge.claimed,
                                    contentPadding = PaddingValues(horizontal = 12.dp, vertical = 6.dp),
                                    modifier = Modifier.heightIn(min = 48.dp)
                                ) {
                                    Text(
                                        when {
                                            challenge.claimed -> "DONE"
                                            challenge.completed -> "CLAIM"
                                            else -> "IN PROGRESS"
                                        },
                                        fontSize = 9.sp,
                                        fontWeight = FontWeight.Black
                                    )
                                }
                            }
                        }
                    }
                }
            }
        },
        confirmButton = {
            TextButton(
                onClick = onDismiss,
                modifier = Modifier.heightIn(min = 48.dp)
            ) { Text("CLOSE") }
        }
    )
}
```

## File: src/main/java/com/zerotoempire/game/CinematicArt.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

@Composable
fun ManagerPortrait(businessId: Int, size: Dp = 58.dp) {
    val accent = when (businessId.coerceAtLeast(0)) {
        0 -> Color(0xFF69E08A)
        1 -> Color(0xFF56BFFF)
        2 -> Color(0xFFFFA54D)
        3 -> Color(0xFFC28BFF)
        4 -> Color(0xFF43E6FF)
        5 -> Color(0xFF4FA8FF)
        6 -> Color(0xFFEAF6FF)
        7 -> Color(0xFFFF654F)
        8 -> Color(0xFFFFD45A)
        9 -> Color(0xFF5BE6FF)
        10 -> Color(0xFF9F7CFF)
        11 -> Color(0xFFFF65D7)
        12 -> Color(0xFFFF68D8)
        else -> Color(0xFFFFE36E)
    }
    val secondary = when (businessId.coerceAtLeast(0)) {
        0 -> Color(0xFFFFD166)
        1 -> Color(0xFF8CEBFF)
        2 -> Color(0xFFFFD27A)
        3 -> Color(0xFF71D8FF)
        4 -> Color(0xFF8CFFDC)
        5 -> Color(0xFF6FE3FF)
        6 -> Color(0xFF78DFFF)
        7 -> Color(0xFFFFB34D)
        8 -> Color(0xFFFFF2B0)
        9 -> Color(0xFF8C88FF)
        10 -> Color(0xFF6EEBFF)
        11 -> Color(0xFFFFC85A)
        12 -> Color(0xFF6EEBFF)
        else -> Color(0xFFC68BFF)
    }
    val tier = when {
        businessId >= 12 -> 4
        businessId >= 8 -> 3
        businessId >= 4 -> 2
        else -> 1
    }

    Box(modifier = Modifier.size(size), contentAlignment = Alignment.Center) {
        when {
            businessId in 0..3 -> ManagerGroup01Portrait(businessId = businessId, portraitSize = size)
            businessId in 4..7 -> ManagerGroup02Portrait(businessId = businessId, portraitSize = size)
            businessId in 8..9 -> ManagerGroup03Portrait(businessId = businessId, portraitSize = size)
            else -> EndgameManagerPortrait(businessId = businessId, portraitSize = size)
        }

        Canvas(Modifier.size(size)) {
            val s = this.size.minDimension
            val c = Offset(this.size.width * .5f, this.size.height * .5f)

            // Dual-tone static lens treatment keeps each executive tied to the visual language
            // of its business without introducing another animation clock in scrolling lists.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.Transparent,
                        secondary.copy(alpha = .035f),
                        accent.copy(alpha = .060f),
                        Color.Black.copy(alpha = .22f)
                    ),
                    center = Offset(c.x - s * .07f, c.y - s * .09f),
                    radius = s * .52f
                ),
                radius = s * .488f,
                center = c
            )
            drawCircle(
                color = Color.Black.copy(alpha = .30f),
                radius = s * .486f,
                center = c,
                style = Stroke(width = s * .026f)
            )
            drawCircle(
                color = accent.copy(alpha = .78f),
                radius = s * .470f,
                center = c,
                style = Stroke(width = s * .010f)
            )
            drawCircle(
                color = secondary.copy(alpha = .24f),
                radius = s * .458f,
                center = c,
                style = Stroke(width = s * .0045f)
            )
            drawCircle(
                color = Color.White.copy(alpha = .10f),
                radius = s * .448f,
                center = c,
                style = Stroke(width = s * .004f)
            )
            drawArc(
                color = Color.White.copy(alpha = .50f),
                startAngle = 208f,
                sweepAngle = 76f,
                useCenter = false,
                topLeft = Offset(s * .052f, s * .052f),
                size = Size(s * .896f, s * .896f),
                style = Stroke(width = s * .009f)
            )
            drawArc(
                color = accent.copy(alpha = .42f),
                startAngle = 18f,
                sweepAngle = 112f,
                useCenter = false,
                topLeft = Offset(s * .074f, s * .074f),
                size = Size(s * .852f, s * .852f),
                style = Stroke(width = s * .006f)
            )
            drawArc(
                color = secondary.copy(alpha = .32f),
                startAngle = 132f,
                sweepAngle = 52f + tier * 7f,
                useCenter = false,
                topLeft = Offset(s * .092f, s * .092f),
                size = Size(s * .816f, s * .816f),
                style = Stroke(width = s * .0045f)
            )
            drawArc(
                color = Color.White.copy(alpha = .16f),
                startAngle = 298f,
                sweepAngle = 34f,
                useCenter = false,
                topLeft = Offset(s * .105f, s * .105f),
                size = Size(s * .790f, s * .790f),
                style = Stroke(width = s * .004f)
            )

            // Machined notches alternate both identity colors so silhouettes stay readable while
            // higher tiers feel denser and more premium at the same physical portrait size.
            val notch = s * .035f
            val inset = s * .095f
            listOf(
                Offset(inset, inset) to Offset(inset + notch, inset),
                Offset(s - inset, inset) to Offset(s - inset - notch, inset),
                Offset(inset, s - inset) to Offset(inset + notch, s - inset),
                Offset(s - inset, s - inset) to Offset(s - inset - notch, s - inset)
            ).forEachIndexed { index, (start, end) ->
                drawLine(
                    color = if (index % 2 == 0) accent.copy(alpha = .62f) else secondary.copy(alpha = .58f),
                    start = start,
                    end = end,
                    strokeWidth = s * .006f
                )
            }

            val crest = Offset(c.x, s * .075f)
            drawCircle(Color.Black.copy(alpha = .52f), s * .018f, crest)
            drawCircle(secondary.copy(alpha = .82f), s * .010f, crest)
            drawCircle(Color.White.copy(alpha = .72f), s * .0035f, Offset(crest.x - s * .003f, crest.y - s * .003f))

            val markerCount = tier + 1
            val markerSpacing = s * .060f
            val markerStart = c.x - (markerCount - 1) * markerSpacing * .5f
            repeat(markerCount) { index ->
                val markerCenter = Offset(markerStart + index * markerSpacing, s * .925f)
                drawCircle(Color.Black.copy(alpha = .58f), s * .016f, markerCenter)
                drawCircle(
                    color = when {
                        index == markerCount - 1 -> Color.White.copy(alpha = .96f)
                        index % 2 == 0 -> accent.copy(alpha = .84f)
                        else -> secondary.copy(alpha = .82f)
                    },
                    radius = s * .010f,
                    center = markerCenter
                )
            }
        }
    }
}

@Composable
fun EraVista(eraIndex: Int, modifier: Modifier = Modifier) {
    Box(modifier = modifier) {
        EraVistaAAA(eraIndex = eraIndex, modifier = Modifier.fillMaxSize())
        EraVistaCinematicOverlay(eraIndex = eraIndex, modifier = Modifier.fillMaxSize())
    }
}
```

## File: src/main/java/com/zerotoempire/game/CinematicRuntimeTransition.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalConfiguration
import androidx.compose.ui.platform.LocalContext
import kotlin.math.min

private const val CINEMATIC_TRANSITION_END = .985f

internal fun cinematicTransitionDurationMillis(compactScreen: Boolean): Int =
    if (compactScreen) 472 else 552

internal fun shouldRenderCinematicTransition(reducedMotion: Boolean, phase: Float): Boolean =
    !reducedMotion && phase < CINEMATIC_TRANSITION_END

/**
 * Lightweight full-screen punctuation for major era changes.
 * It owns no gameplay state, consumes no input, and is completely disabled
 * when reduced-motion / battery-saver policy is active.
 */
@Composable
fun CinematicRuntimeTransitionOverlay(
    eraIndex: Int,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val configuration = LocalConfiguration.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val compactScreen = configuration.screenWidthDp < 360
    val phase = remember { Animatable(1f) }
    var previousEra by remember { mutableIntStateOf(eraIndex) }

    // Size/configuration changes should not cancel an era impact already in flight.
    // The next era change naturally samples the current compact-screen policy.
    LaunchedEffect(eraIndex, reducedMotion) {
        val advanced = eraIndex > previousEra
        previousEra = eraIndex
        if (!advanced || reducedMotion) {
            phase.snapTo(1f)
            return@LaunchedEffect
        }
        phase.snapTo(0f)
        // The final 1.5% is visually negligible; ending there also removes
        // the otherwise invisible animation tail from the composition clock.
        phase.animateTo(
            CINEMATIC_TRANSITION_END,
            animationSpec = tween(durationMillis = cinematicTransitionDurationMillis(compactScreen))
        )
    }

    if (shouldRenderCinematicTransition(reducedMotion, phase.value)) {
        val progress = phase.value.coerceIn(0f, 1f)
        val impact = (1f - progress).coerceIn(0f, 1f)
        val cyan = Color(0xFF63E7FF)
        val gold = Color(0xFFFFD166)

        Canvas(modifier.fillMaxSize()) {
            val shortest = min(size.width, size.height)
            val center = Offset(size.width * .5f, size.height * .46f)
            val ringRadius = shortest * (.10f + .72f * progress)
            val edgeWidth = shortest * .012f

            drawRect(Color.White.copy(alpha = .16f * impact))
            drawRect(cyan.copy(alpha = .09f * impact))

            drawCircle(
                color = gold.copy(alpha = .70f * impact),
                radius = ringRadius,
                center = center,
                style = Stroke(width = edgeWidth * (1.15f - .55f * progress))
            )
            if (!compactScreen) {
                drawCircle(
                    color = cyan.copy(alpha = .48f * impact),
                    radius = ringRadius * 1.18f,
                    center = center,
                    style = Stroke(width = edgeWidth * .48f)
                )
            }

            val sweepY = size.height * (-.08f + 1.16f * progress)
            drawLine(
                color = Color.White.copy(alpha = .28f * impact),
                start = Offset(0f, sweepY),
                end = Offset(size.width, sweepY),
                strokeWidth = edgeWidth * .65f
            )
            if (!compactScreen) {
                drawLine(
                    color = cyan.copy(alpha = .34f * impact),
                    start = Offset(0f, sweepY + edgeWidth * 1.8f),
                    end = Offset(size.width, sweepY + edgeWidth * 1.8f),
                    strokeWidth = edgeWidth * .28f
                )

                val cornerLength = shortest * (.10f + .05f * impact)
                val inset = shortest * .035f
                val cornerAlpha = .55f * impact
                drawLine(gold.copy(alpha = cornerAlpha), Offset(inset, inset), Offset(inset + cornerLength, inset), edgeWidth * .32f)
                drawLine(gold.copy(alpha = cornerAlpha), Offset(inset, inset), Offset(inset, inset + cornerLength), edgeWidth * .32f)
                drawLine(cyan.copy(alpha = cornerAlpha), Offset(size.width - inset, size.height - inset), Offset(size.width - inset - cornerLength, size.height - inset), edgeWidth * .32f)
                drawLine(cyan.copy(alpha = cornerAlpha), Offset(size.width - inset, size.height - inset), Offset(size.width - inset, size.height - inset - cornerLength), edgeWidth * .32f)
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/CommerceUi.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import android.content.ContextWrapper
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun CommerceRoot(vm: GameViewModel = viewModel()) {
    val context = LocalContext.current
    val activity = remember(context) { context.findActivity() }
    val lifecycleOwner = LocalLifecycleOwner.current
    val meta by vm.meta.collectAsStateWithLifecycle()
    val billing = remember(context) { PlayBillingGateway(context.applicationContext) }
    val rewarded = remember(context) { AdMobRewardedGateway(context.applicationContext) }
    val consent = remember(activity) { activity?.let(::PrivacyConsentManager) }
    var showStore by remember { mutableStateOf(false) }
    var showPrivacyPolicy by remember { mutableStateOf(false) }
    var owned by remember { mutableStateOf<Set<StoreProduct>>(emptySet()) }
    var purchaseInFlight by remember { mutableStateOf<StoreProduct?>(null) }
    var pendingPurchases by remember { mutableStateOf<Set<StoreProduct>>(emptySet()) }
    var status by remember { mutableStateOf<String?>(null) }
    var adsAllowed by remember { mutableStateOf(false) }
    var privacyOptionsRequired by remember { mutableStateOf(false) }

    DisposableEffect(billing, activity) {
        billing.connect()
        if (activity != null && consent != null) consent.gather { canRequestAds, _ -> adsAllowed = canRequestAds; rewarded.setEnabled(canRequestAds); privacyOptionsRequired = consent.isPrivacyOptionsRequired(); if (canRequestAds) rewarded.preload() }
        billing.restore { result -> val restored = result.products; if (result is RestoreResult.Success) owned = restored.filterNot { it.consumable }.toSet() else owned = owned + restored.filterNot { it.consumable }; if (purchaseInFlight == null) pendingPurchases = result.pendingProducts; vm.applyEntitlements(restored, authoritativePermanentEntitlements = result is RestoreResult.Success) }
        onDispose { rewarded.setEnabled(false); billing.disconnect() }
    }
    DisposableEffect(lifecycleOwner, billing) {
        var leftForeground = false
        val observer = LifecycleEventObserver { _, event ->
            when (event) {
                Lifecycle.Event.ON_STOP -> leftForeground = true
                Lifecycle.Event.ON_RESUME -> if (leftForeground) {
                    leftForeground = false
                    billing.restore { result ->
                        val restored = result.products
                        if (result is RestoreResult.Success) owned = restored.filterNot { it.consumable }.toSet() else owned = owned + restored.filterNot { it.consumable }
                        if (purchaseInFlight == null) pendingPurchases = result.pendingProducts
                        vm.applyEntitlements(restored, authoritativePermanentEntitlements = result is RestoreResult.Success)
                    }
                }
                else -> Unit
            }
        }
        lifecycleOwner.lifecycle.addObserver(observer); onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }
    Box(Modifier.fillMaxSize()) {
        EmpireRoot(vm)
        if (activity != null) {
            Row(modifier = Modifier.align(Alignment.BottomCenter).padding(start = 16.dp, end = 16.dp, bottom = 86.dp).fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp), verticalAlignment = Alignment.CenterVertically) {
                FilledTonalButton(onClick = { showStore = true }, modifier = Modifier.weight(1f).heightIn(min = 48.dp), shape = RoundedCornerShape(16.dp), contentPadding = PaddingValues(vertical = 9.dp)) { MetaSprite(MetaSpriteKind.STORE, 23.dp); Spacer(Modifier.width(5.dp)); Text("STORE", fontSize = 9.sp, fontWeight = FontWeight.Black) }
                FilledTonalButton(onClick = vm::requestProfitBoostAd, enabled = adsAllowed, modifier = Modifier.weight(1f).heightIn(min = 48.dp), shape = RoundedCornerShape(16.dp), contentPadding = PaddingValues(vertical = 9.dp)) { MetaSprite(MetaSpriteKind.BOOST, 23.dp, active = adsAllowed); Spacer(Modifier.width(5.dp)); Text("×2 BOOST", fontSize = 9.sp, fontWeight = FontWeight.Black) }
                if (privacyOptionsRequired && consent != null) TextButton(onClick = { consent.showPrivacyOptions { error -> adsAllowed = consent.canRequestAds(); rewarded.setEnabled(adsAllowed); privacyOptionsRequired = consent.isPrivacyOptionsRequired(); if (adsAllowed) rewarded.preload(); if (error != null) status = error } }, modifier = Modifier.weight(.8f).heightIn(min = 48.dp)) { Text("PRIVACY", fontSize = 8.sp) }
            }
        }
    }
    status?.let { message -> AlertDialog(onDismissRequest = { status = null }, confirmButton = { TextButton(onClick = { status = null }, modifier = Modifier.heightIn(min = 48.dp)) { Text("OK") } }, text = { Text(message) }) }
    if (showStore && activity != null) StoreDialog(
        owned = owned + buildSet { if (meta.adsRemoved) add(StoreProduct.REMOVE_ADS); if (meta.starterPackOwned) add(StoreProduct.STARTER_PACK) },
        purchaseInFlight = purchaseInFlight,
        pendingPurchases = pendingPurchases,
        onDismiss = { showStore = false },
        onPrivacyPolicy = { showPrivacyPolicy = true },
        onDiagnostics = if (BuildConfig.DEBUG) {
            { status = LocalBillingDiagnostics.snapshot().toSupportText() }
        } else null,
        onRestore = { billing.restore { result ->
            val restored = result.products
            if (result is RestoreResult.Success) owned = restored.filterNot { it.consumable }.toSet() else owned = owned + restored.filterNot { it.consumable }
            if (purchaseInFlight == null) pendingPurchases = result.pendingProducts
            vm.applyEntitlements(restored, authoritativePermanentEntitlements = result is RestoreResult.Success)
            status = when (result) {
                is RestoreResult.Success -> when {
                    restored.isNotEmpty() -> "Purchases restored."
                    result.pendingProducts.isNotEmpty() -> "Payment is still pending Google Play confirmation."
                    else -> "No purchases found."
                }
                is RestoreResult.Failed -> if (restored.isEmpty()) result.reason else "${result.reason} Some purchases were restored."
            }
        } },
        onPurchase = { product ->
            if (purchaseInFlight != null) return@StoreDialog
            purchaseInFlight = product
            pendingPurchases = pendingPurchases - product
            billing.purchase(activity, product) { result ->
                when (result) {
                    is PurchaseResult.Success -> {
                        purchaseInFlight = null
                        pendingPurchases = pendingPurchases - result.product
                        if (!result.product.consumable) owned = owned + result.product
                        vm.applyPurchase(result.product, result.transactionId)
                        status = "Purchase completed."
                    }
                    PurchaseResult.Cancelled -> {
                        purchaseInFlight = null
                        pendingPurchases = pendingPurchases - product
                    }
                    PurchaseResult.Pending -> {
                        purchaseInFlight = null
                        pendingPurchases = pendingPurchases + product
                        status = "Purchase pending. You can close the Store; the reward will unlock after Google Play confirms payment."
                    }
                    is PurchaseResult.Failed -> {
                        purchaseInFlight = null
                        pendingPurchases = pendingPurchases - product
                        status = result.reason
                    }
                }
            }
        }
    )
    if (showPrivacyPolicy) PrivacyPolicyDialog(onDismiss = { showPrivacyPolicy = false })
}

@Composable
private fun StoreDialog(
    owned: Set<StoreProduct>,
    purchaseInFlight: StoreProduct?,
    pendingPurchases: Set<StoreProduct>,
    onDismiss: () -> Unit,
    onPrivacyPolicy: () -> Unit,
    onDiagnostics: (() -> Unit)?,
    onRestore: () -> Unit,
    onPurchase: (StoreProduct) -> Unit
) {
    AlertDialog(
        onDismissRequest = onDismiss,
        containerColor = EmpireColors.SurfaceHigh,
        title = {
            Row(verticalAlignment = Alignment.CenterVertically) {
                MetaSprite(MetaSpriteKind.STORE, 34.dp)
                Spacer(Modifier.width(8.dp))
                Text("EMPIRE STORE", color = EmpireColors.Gold, fontWeight = FontWeight.Black)
            }
        },
        text = {
            Column(
                modifier = Modifier.heightIn(max = 480.dp).verticalScroll(rememberScrollState()),
                verticalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                Text("Purchases are handled by Google Play. Prices and final confirmation are shown by Google Play.", color = EmpireColors.TextSecondary, fontSize = 11.sp)
                if (pendingPurchases.isNotEmpty()) {
                    Text(
                        "PAYMENT PENDING — Google Play has not confirmed this transaction yet. You can safely close and reopen the Store.",
                        color = EmpireColors.Gold,
                        fontSize = 11.sp,
                        fontWeight = FontWeight.Bold
                    )
                }
                StoreRow("REMOVE ADS", "Lifetime removal of non-rewarded advertising. Reward videos remain optional.", StoreProduct.REMOVE_ADS in owned, purchaseInFlight, pendingPurchases, StoreProduct.REMOVE_ADS, MetaSpriteKind.LEGACY) { onPurchase(StoreProduct.REMOVE_ADS) }
                StoreRow("STARTER PACK", "250 gems + 30 min ×2 income. One-time purchase.", StoreProduct.STARTER_PACK in owned, purchaseInFlight, pendingPurchases, StoreProduct.STARTER_PACK, MetaSpriteKind.BOOST) { onPurchase(StoreProduct.STARTER_PACK) }
                StoreRow("120 GEMS", "Consumable gem pack.", false, purchaseInFlight, pendingPurchases, StoreProduct.GEM_PACK_SMALL, MetaSpriteKind.GEM) { onPurchase(StoreProduct.GEM_PACK_SMALL) }
                StoreRow("650 GEMS", "Consumable gem pack.", false, purchaseInFlight, pendingPurchases, StoreProduct.GEM_PACK_MEDIUM, MetaSpriteKind.GEM) { onPurchase(StoreProduct.GEM_PACK_MEDIUM) }
                OutlinedButton(onClick = onRestore, enabled = purchaseInFlight == null, modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)) { Text("RESTORE PURCHASES") }
                TextButton(onClick = onPrivacyPolicy, modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)) { Text("PRIVACY POLICY") }
                if (onDiagnostics != null) {
                    TextButton(onClick = onDiagnostics, modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)) { Text("BILLING DIAGNOSTICS") }
                }
            }
        },
        confirmButton = {
            TextButton(onClick = onDismiss, modifier = Modifier.heightIn(min = 48.dp)) { Text("CLOSE") }
        }
    )
}

@Composable
private fun StoreRow(
    title: String,
    subtitle: String,
    owned: Boolean,
    purchaseInFlight: StoreProduct?,
    pendingPurchases: Set<StoreProduct>,
    product: StoreProduct,
    kind: MetaSpriteKind,
    purchase: () -> Unit
) {
    val pending = product in pendingPurchases
    val processing = purchaseInFlight == product && !pending
    val enabled = !owned && purchaseInFlight == null && !pending
    Surface(color = EmpireColors.Surface, shape = RoundedCornerShape(14.dp)) {
        Row(Modifier.fillMaxWidth().padding(12.dp), verticalAlignment = Alignment.CenterVertically) {
            MetaSprite(kind, 38.dp, active = !owned)
            Spacer(Modifier.width(10.dp))
            Column(Modifier.weight(1f)) {
                Text(title, color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black)
                Text(subtitle, color = EmpireColors.TextSecondary, fontSize = 10.sp)
            }
            Spacer(Modifier.width(8.dp))
            Button(
                onClick = purchase,
                enabled = enabled,
                modifier = Modifier
                    .heightIn(min = 48.dp)
                    .semantics { contentDescription = when { owned -> "$title owned"; pending -> "$title payment pending Google Play confirmation"; processing -> "$title purchase processing"; else -> "Buy $title" } }
            ) {
                Text(when { owned -> "OWNED"; pending -> "PENDING"; processing -> "PROCESSING…"; else -> "BUY" }, fontSize = 10.sp)
            }
        }
    }
}

private tailrec fun Context.findActivity(): Activity? = when (this) {
    is Activity -> this
    is ContextWrapper -> baseContext.findActivity()
    else -> null
}
```

## File: src/main/java/com/zerotoempire/game/ContentUnlocks.kt
```kotlin
package com.zerotoempire.game

/**
 * Presentation unlocks are deliberately separate from GameState persistence/economy.
 * Existing saves retain every business; the UI simply reveals higher tiers as the empire grows.
 */
object ContentUnlocks {
    private val businessThresholds = mapOf(
        0 to 0.0,
        1 to 40.0,
        2 to 500.0,
        3 to 6_000.0,
        4 to 120_000.0,
        5 to 3_000_000.0,
        6 to 180_000_000.0,
        7 to 18_000_000_000.0,
        8 to 2_500_000_000_000.0,
        9 to 650_000_000_000_000.0,
        10 to 500_000_000_000_000_000.0,
        11 to 2.0e21,
        12 to 8.0e24,
        13 to 3.0e28
    )

    fun thresholdForBusiness(id: Int): Double = businessThresholds[id] ?: Double.POSITIVE_INFINITY

    fun isBusinessVisible(id: Int, lifetimeCash: Double): Boolean =
        lifetimeCash >= thresholdForBusiness(id)

    fun visibleBusinesses(state: GameState): List<Business> =
        state.businesses.filter { isBusinessVisible(it.id, state.lifetimeCash) }

    /**
     * Keeps the manager screen useful on phones by putting the next actionable hires first.
     * This is presentation-only: costs, manager effects, unlock thresholds and saved state are untouched.
     */
    fun visibleManagers(state: GameState): List<Manager> =
        Managers.catalog
            .asSequence()
            .filter { isBusinessVisible(it.businessId, state.lifetimeCash) }
            .sortedWith(
                compareBy<Manager> {
                    when {
                        it.businessId in state.hiredManagerIds -> 2
                        state.cash >= it.cost -> 0
                        else -> 1
                    }
                }.thenBy { it.businessId }
            )
            .toList()

    fun nextHiddenBusiness(state: GameState): Business? =
        state.businesses.firstOrNull { !isBusinessVisible(it.id, state.lifetimeCash) }

    fun progressToNextUnlock(state: GameState): Float {
        val next = nextHiddenBusiness(state) ?: return 1f
        val threshold = thresholdForBusiness(next.id)
        if (!threshold.isFinite() || threshold <= 0.0) return 0f
        val previousThreshold = thresholdForBusiness((next.id - 1).coerceAtLeast(0))
        val span = (threshold - previousThreshold).coerceAtLeast(1.0)
        return ((state.lifetimeCash - previousThreshold) / span).toFloat().coerceIn(0f, 1f)
    }
}
```

## File: src/main/java/com/zerotoempire/game/DrawScopeCompat.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.DrawScope

/**
 * Explicit premium-art overload for start/end/width/color ordering.
 * Keeps the procedural art sources concise while delegating to Compose's canonical API.
 */
fun DrawScope.drawLine(start: Offset, end: Offset, strokeWidth: Float, color: Color) {
    drawLine(color = color, start = start, end = end, strokeWidth = strokeWidth)
}
```

## File: src/main/java/com/zerotoempire/game/DroneThruster.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val ThrusterFrameSize = 128
private const val ThrusterColumns = 4
private const val ThrusterFrameCount = 8

/** Galactic Exchange propulsion accent, frozen on frame zero under reduced motion. */
@Composable
internal fun DroneThruster(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_12_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }
    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) while (true) {
            delay(125)
            frame = (frame + 1) % ThrusterFrameCount
        }
    }
    Canvas(modifier) {
        val effectSize = size.minDimension * .48f
        val destination = Offset((size.width - effectSize) * .5f, size.height * .40f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset((frame % ThrusterColumns) * ThrusterFrameSize, (frame / ThrusterColumns) * ThrusterFrameSize),
            srcSize = IntSize(ThrusterFrameSize, ThrusterFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .70f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/DynastyProgression.kt
```kotlin
package com.zerotoempire.game

import kotlin.math.ln
import kotlin.math.sqrt

/**
 * Long-horizon campaign progression built only from already-persisted player data.
 * It therefore works with every existing save without migrations.
 *
 * Dynasty is intentionally cosmetic/status progression for now: it gives the
 * player a months-long ladder without destabilising the tuned economy.
 */
data class DynastyRank(
    val level: Int,
    val title: String,
    val renownRequired: Double
)

data class DynastyStatus(
    val rank: DynastyRank,
    val next: DynastyRank?,
    val renown: Double,
    val progress: Float
)

object DynastyProgression {
    const val MAX_RANK = 60

    private val titles = listOf(
        "Street Spark", "Local Operator", "District Builder", "City Founder",
        "Industrial Architect", "Market Baron", "National Power", "Global Magnate",
        "Orbital Pioneer", "Planetary Governor", "Stellar Director", "System Sovereign",
        "Galactic Regent", "Cluster Chancellor", "Cosmic Architect", "Reality Broker",
        "Transcendent Founder", "Eternal Strategist", "Infinite Industrialist", "Empire Ascendant"
    )

    val ranks: List<DynastyRank> = (1..MAX_RANK).map { level ->
        DynastyRank(
            level = level,
            title = titleFor(level),
            renownRequired = threshold(level)
        )
    }

    /** Persistent campaign score. Every source survives ordinary ascensions. */
    fun renown(state: GameState, meta: PlayerMeta): Double {
        val legacy = sqrt(state.prestigePoints.coerceAtLeast(0).toDouble()) * 34.0
        val ascensions = sqrt(meta.prestigeCount.coerceAtLeast(0).toDouble()) * 38.0
        val purchases = ln(1.0 + meta.totalPurchases.coerceAtLeast(0).toDouble()) * 18.0
        val taps = ln(1.0 + meta.totalTaps.coerceAtLeast(0).toDouble()) * 7.0
        val eras = meta.highestEraSeen.coerceAtLeast(0) * 72.0
        val streak = sqrt(meta.streakDays.coerceAtLeast(0).toDouble()) * 9.0
        return (legacy + ascensions + purchases + taps + eras + streak).coerceAtLeast(0.0)
    }

    fun status(state: GameState, meta: PlayerMeta): DynastyStatus {
        val score = renown(state, meta)
        val current = ranks.lastOrNull { score >= it.renownRequired } ?: ranks.first()
        val next = ranks.getOrNull(current.level)
        val progress = if (next == null) 1f else {
            val span = (next.renownRequired - current.renownRequired).coerceAtLeast(1.0)
            ((score - current.renownRequired) / span).toFloat().coerceIn(0f, 1f)
        }
        return DynastyStatus(current, next, score, progress)
    }

    private fun threshold(level: Int): Double {
        if (level <= 1) return 0.0
        val n = level - 1.0
        return 32.0 * n * n + 16.0 * n * n * n / MAX_RANK
    }

    private fun titleFor(level: Int): String {
        val index = ((level - 1) * titles.size / MAX_RANK).coerceIn(0, titles.lastIndex)
        return titles[index]
    }
}
```

## File: src/main/java/com/zerotoempire/game/EconomyMath.kt
```kotlin
package com.zerotoempire.game

import kotlin.math.exp
import kotlin.math.ln

/** Numerical guardrails for extremely mature saves. */
object EconomyMath {
    const val MAX_VALUE: Double = 1e300
    private const val COST_GROWTH = 1.15
    private val lnGrowth = ln(COST_GROWTH)
    private val lnMax = ln(MAX_VALUE)

    fun finite(value: Double): Double = when {
        value.isNaN() || value <= 0.0 -> 0.0
        value.isInfinite() || value > MAX_VALUE -> MAX_VALUE
        else -> value
    }

    fun safeAdd(a: Double, b: Double): Double {
        val left = finite(a)
        val right = finite(b)
        if (left >= MAX_VALUE - right) return MAX_VALUE
        return left + right
    }

    fun growthCost(baseCost: Double, level: Int): Double {
        if (baseCost <= 0.0 || !baseCost.isFinite()) return MAX_VALUE
        val safeLevel = level.coerceAtLeast(0)
        if (safeLevel == 0) return baseCost.coerceAtMost(MAX_VALUE)
        val exponent = ln(baseCost) + safeLevel * lnGrowth
        if (!exponent.isFinite() || exponent >= lnMax) return MAX_VALUE
        return exp(exponent).coerceAtMost(MAX_VALUE)
    }

    fun geometricCost(baseCost: Double, startLevel: Int, count: Int): Double {
        if (count <= 0) return 0.0
        val first = growthCost(baseCost, startLevel)
        if (first >= MAX_VALUE) return MAX_VALUE
        if (count == 1) return first
        val growthExponent = count.toDouble() * lnGrowth
        if (!growthExponent.isFinite() || growthExponent >= lnMax) return MAX_VALUE
        val factor = exp(growthExponent)
        if (!factor.isFinite()) return MAX_VALUE
        val total = first * (factor - 1.0) / (COST_GROWTH - 1.0)
        return finite(total)
    }
}
```

## File: src/main/java/com/zerotoempire/game/ElectricArc.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val ArcFrameSize = 128
private const val ArcColumns = 4
private const val ArcFrameCount = 8

/** Mars Empire power arc, frozen on frame zero under reduced motion. */
@Composable
internal fun ElectricArc(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_10_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }
    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) while (true) {
            delay(125)
            frame = (frame + 1) % ArcFrameCount
        }
    }
    Canvas(modifier) {
        val effectSize = size.minDimension * .58f
        val destination = Offset((size.width - effectSize) * .5f, (size.height - effectSize) * .5f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset((frame % ArcColumns) * ArcFrameSize, (frame / ArcColumns) * ArcFrameSize),
            srcSize = IntSize(ArcFrameSize, ArcFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .66f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/EmpireArt.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.*
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import kotlin.math.cos
import kotlin.math.sin

object EmpireArtPalette {
    val Ink = Color(0xFF07101E)
    val Steel = Color(0xFF1A2C45)
    val SteelBright = Color(0xFF3A587A)
    val Gold = Color(0xFFFFC857)
    val GoldHot = Color(0xFFFFE6A1)
    val Cyan = Color(0xFF57E7F2)
    val Violet = Color(0xFFA58BFF)
    val Magenta = Color(0xFFFF6ED6)
    val Red = Color(0xFFFF6D68)
    val White = Color(0xFFF6FBFF)
}

@Composable
fun BusinessArtIcon(id: Int, level: Int = 0, iconSize: Dp = 54.dp, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val pulse: Float = if (reducedMotion || lowPower) {
        1f
    } else {
        val transition = rememberInfiniteTransition(label = "businessArt$id")
        val animated by transition.animateFloat(
            initialValue = .82f,
            targetValue = 1f,
            animationSpec = infiniteRepeatable(tween(1800 + id * 90), RepeatMode.Reverse),
            label = "pulse"
        )
        animated
    }

    Box(
        modifier = modifier.size(iconSize).background(
            Brush.radialGradient(listOf(EmpireColors.SurfaceHigh, EmpireColors.Surface, EmpireColors.Void)),
            RoundedCornerShape(iconSize * .28f)
        )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val glow = when (id) {
                0, 1 -> EmpireArtPalette.Gold
                2, 3 -> EmpireArtPalette.Cyan
                4, 5 -> EmpireArtPalette.Violet
                6, 7 -> EmpireArtPalette.Red
                else -> EmpireArtPalette.Magenta
            }
            val tier = when {
                level >= 1000 -> 7
                level >= 500 -> 6
                level >= 250 -> 5
                level >= 100 -> 4
                level >= 50 -> 3
                level >= 25 -> 2
                level >= 10 -> 1
                else -> 0
            }
            val motionScale = if (lowPower) .72f else 1f
            drawCircle(
                glow.copy(alpha = ((.11f + tier * .025f) * pulse * motionScale).coerceAtMost(.34f)),
                radius = s * (.41f + tier * .010f)
            )
            drawCircle(
                glow.copy(alpha = (.30f + tier * .055f).coerceAtMost(.72f)),
                radius = s * .38f,
                style = Stroke(s * (.020f + tier * .0028f))
            )
            if (tier >= 1) {
                drawCircle(EmpireArtPalette.White.copy(alpha = .14f * pulse), s * .445f, style = Stroke(s * .010f))
            }
            if (tier >= 2) {
                repeat(if (lowPower) 2 else 4) { i ->
                    val count = if (lowPower) 2 else 4
                    val a = (i * Math.PI * 2.0 / count).toFloat()
                    drawCircle(glow.copy(alpha = .70f), s * .021f, Offset(s*.5f + cos(a)*s*.43f, s*.5f + sin(a)*s*.43f))
                }
            }
            if (tier >= 3) {
                drawArc(EmpireArtPalette.GoldHot.copy(alpha = .48f), -35f, 235f, false, Offset(s*.09f,s*.09f), Size(s*.82f,s*.82f), style = Stroke(s*.013f))
            }
            if (tier >= 4) {
                val spokes = if (lowPower) 4 else 8
                repeat(spokes) { i ->
                    val a = (i * Math.PI * 2.0 / spokes).toFloat()
                    drawLine(glow.copy(alpha=.58f), Offset(s*.5f+cos(a)*s*.39f,s*.5f+sin(a)*s*.39f), Offset(s*.5f+cos(a)*s*.48f,s*.5f+sin(a)*s*.48f), s*.010f)
                }
            }
            if (tier >= 5) {
                drawCircle(EmpireColors.Cyan.copy(alpha = .24f * pulse), s * .49f, style = Stroke(s * .009f))
                drawCircle(EmpireColors.GoldBright.copy(alpha = .18f), s * .455f, style = Stroke(s * .006f))
            }
            if (tier >= 6) {
                drawArc(EmpireColors.Violet.copy(alpha = .52f), 145f, 165f, false, Offset(s*.055f,s*.055f), Size(s*.89f,s*.89f), style = Stroke(s*.012f))
                drawArc(EmpireColors.GoldBright.copy(alpha = .60f), -32f, 118f, false, Offset(s*.045f,s*.045f), Size(s*.91f,s*.91f), style = Stroke(s*.014f))
            }
            if (tier >= 7) {
                val rays = if (lowPower) 6 else 12
                repeat(rays) { i ->
                    val a = (i * Math.PI * 2.0 / rays).toFloat()
                    val inner = s * .455f
                    val outer = s * if (i % 2 == 0) .515f else .49f
                    drawLine(
                        if (i % 2 == 0) EmpireColors.GoldBright.copy(alpha=.72f) else EmpireColors.Cyan.copy(alpha=.58f),
                        Offset(s*.5f+cos(a)*inner,s*.5f+sin(a)*inner),
                        Offset(s*.5f+cos(a)*outer,s*.5f+sin(a)*outer),
                        s*.008f
                    )
                }
                drawCircle(Color.White.copy(alpha = .10f * pulse), s * .505f)
            }
            when (id) {
                0 -> drawStreetStand(glow)
                1 -> drawStore(glow)
                2 -> drawWorkshop(glow)
                3 -> drawFactory(glow)
                4 -> drawTech(glow)
                5 -> drawCity(glow)
                6 -> drawMoon(glow)
                7 -> drawPlanet(glow)
                8 -> drawDyson(glow)
                else -> drawGalaxy(glow)
            }
        }
    }
}

@Composable
fun EmpireAmbientBackdrop(eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase: Float = if (reducedMotion || lowPower) {
        .5f
    } else {
        val transition = rememberInfiniteTransition(label = "empireAmbient")
        val animated by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(18_000, easing = LinearEasing)), label = "ambientPhase")
        animated
    }
    Canvas(modifier) {
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1, 2 -> EmpireArtPalette.Cyan
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }
        drawRect(Brush.verticalGradient(listOf(EmpireColors.Void, EmpireColors.DeepSpace, EmpireColors.Void)))
        val starCount = if (lowPower) 18 else 34
        repeat(starCount) { i ->
            val x = size.width * (((i * 47) % 101) / 100f)
            val y = size.height * (((i * 73) % 97) / 100f)
            drawCircle(EmpireArtPalette.White.copy(alpha = .28f + .12f * (i % 5)), if (i % 7 == 0) 2.2f else 1.1f, Offset(x, y))
        }
        val cx = size.width * (.18f + phase * .64f)
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha = .16f), Color.Transparent), Offset(cx, size.height * .28f), size.width * .55f), size.width * .55f, Offset(cx, size.height * .28f))
        drawCircle(Brush.radialGradient(listOf(EmpireArtPalette.Violet.copy(alpha = .10f), Color.Transparent), Offset(size.width * .82f, size.height * .68f), size.width * .48f), size.width * .48f, Offset(size.width * .82f, size.height * .68f))
    }
}

private fun DrawScope.arc(color: Color, left: Float, top: Float, right: Float, bottom: Float, start: Float, sweep: Float, stroke: Float) {
    drawArc(color, start, sweep, false, Offset(left, top), Size(right-left, bottom-top), style = Stroke(stroke))
}

private fun DrawScope.drawStreetStand(c: Color) { val s=size.minDimension; drawRoundRect(c,Offset(s*.25f,s*.46f),Size(s*.5f,s*.28f),CornerRadius(s*.04f)); drawRect(EmpireArtPalette.Ink,Offset(s*.31f,s*.53f),Size(s*.38f,s*.15f)); drawLine(c,Offset(s*.28f,s*.42f),Offset(s*.72f,s*.42f),s*.07f); drawLine(c,Offset(s*.35f,s*.3f),Offset(s*.65f,s*.3f),s*.055f) }
private fun DrawScope.drawStore(c: Color) { val s=size.minDimension; drawRoundRect(c.copy(alpha=.9f),Offset(s*.24f,s*.39f),Size(s*.52f,s*.36f),CornerRadius(s*.05f)); drawRect(EmpireArtPalette.Ink,Offset(s*.32f,s*.51f),Size(s*.36f,s*.24f)); repeat(3){i->drawRect(c,Offset(s*(.29f+i*.15f),s*.31f),Size(s*.11f,s*.1f))} }
private fun DrawScope.drawWorkshop(c: Color) { val s=size.minDimension; drawCircle(c,s*.20f,Offset(s*.5f,s*.52f),style=Stroke(s*.09f)); repeat(6){i->val a=i*Math.PI.toFloat()/3f;drawLine(c,Offset(s*.5f+cos(a)*s*.2f,s*.52f+sin(a)*s*.2f),Offset(s*.5f+cos(a)*s*.34f,s*.52f+sin(a)*s*.34f),s*.065f)};drawCircle(EmpireArtPalette.Ink,s*.07f,Offset(s*.5f,s*.52f)) }
private fun DrawScope.drawFactory(c: Color) { val s=size.minDimension; val p=Path().apply{moveTo(s*.18f,s*.72f);lineTo(s*.18f,s*.5f);lineTo(s*.36f,s*.39f);lineTo(s*.36f,s*.5f);lineTo(s*.55f,s*.39f);lineTo(s*.55f,s*.5f);lineTo(s*.78f,s*.5f);lineTo(s*.78f,s*.72f);close()};drawPath(p,c);drawRect(EmpireArtPalette.Ink,Offset(s*.27f,s*.58f),Size(s*.12f,s*.09f));drawRect(EmpireArtPalette.Ink,Offset(s*.52f,s*.58f),Size(s*.12f,s*.09f));drawRect(c,Offset(s*.66f,s*.23f),Size(s*.08f,s*.28f)) }
private fun DrawScope.drawTech(c: Color) { val s=size.minDimension; drawRoundRect(c,Offset(s*.22f,s*.27f),Size(s*.56f,s*.46f),CornerRadius(s*.09f),style=Stroke(s*.055f));repeat(3){i->drawLine(c,Offset(s*(.32f+i*.18f),s*.16f),Offset(s*(.32f+i*.18f),s*.27f),s*.035f);drawLine(c,Offset(s*(.32f+i*.18f),s*.73f),Offset(s*(.32f+i*.18f),s*.84f),s*.035f)};drawCircle(c,s*.10f,Offset(s*.5f,s*.5f));drawCircle(EmpireArtPalette.Ink,s*.04f,Offset(s*.5f,s*.5f)) }
private fun DrawScope.drawCity(c: Color) { val s=size.minDimension; val xs=listOf(.20f,.35f,.50f,.64f);val hs=listOf(.36f,.50f,.43f,.58f);xs.forEachIndexed{i,x->val h=hs[i]*s;drawRoundRect(c.copy(alpha=.85f),Offset(s*x,s*.75f-h),Size(s*.12f,h),CornerRadius(s*.025f));repeat(3){r->drawCircle(EmpireArtPalette.GoldHot,s*.012f,Offset(s*(x+.035f),s*.69f-h+r*s*.09f));drawCircle(EmpireArtPalette.Cyan,s*.012f,Offset(s*(x+.085f),s*.69f-h+r*s*.09f))}} }
private fun DrawScope.drawMoon(c: Color) { val s=size.minDimension; drawCircle(c,s*.27f,Offset(s*.48f,s*.5f));drawCircle(EmpireArtPalette.Ink.copy(alpha=.28f),s*.055f,Offset(s*.39f,s*.41f));drawCircle(EmpireArtPalette.Ink.copy(alpha=.22f),s*.035f,Offset(s*.57f,s*.57f));arc(EmpireArtPalette.Cyan,s*.18f,s*.34f,s*.82f,s*.67f,-12f,205f,s*.035f) }
private fun DrawScope.drawPlanet(c: Color) { val s=size.minDimension; drawCircle(c,s*.25f,Offset(s*.5f,s*.51f));arc(EmpireArtPalette.GoldHot,s*.14f,s*.36f,s*.86f,s*.66f,-12f,205f,s*.045f);drawCircle(EmpireArtPalette.White,s*.018f,Offset(s*.31f,s*.3f)) }
private fun DrawScope.drawDyson(c: Color) { val s=size.minDimension; drawCircle(EmpireArtPalette.GoldHot,s*.12f,Offset(s*.5f,s*.5f));drawCircle(c.copy(alpha=.25f),s*.22f,Offset(s*.5f,s*.5f));drawCircle(c,s*.30f,Offset(s*.5f,s*.5f),style=Stroke(s*.035f));repeat(8){i->val a=i*Math.PI.toFloat()/4f;drawLine(c,Offset(s*.5f+cos(a)*s*.19f,s*.5f+sin(a)*s*.19f),Offset(s*.5f+cos(a)*s*.36f,s*.5f+sin(a)*s*.36f),s*.025f)} }
private fun DrawScope.drawGalaxy(c: Color) { val s=size.minDimension; drawCircle(EmpireArtPalette.White,s*.045f,Offset(s*.5f,s*.5f));repeat(3){ring->arc(c.copy(alpha=.9f-ring*.2f),s*(.18f+ring*.06f),s*(.27f+ring*.06f),s*(.82f-ring*.06f),s*(.73f-ring*.06f),25f+ring*42f,205f,s*(.045f-ring*.008f))};repeat(8){i->val a=i*.83f;drawCircle(if(i%2==0)EmpireArtPalette.Cyan else EmpireArtPalette.Magenta,s*.018f,Offset(s*.5f+cos(a)*s*(.23f+i*.012f),s*.5f+sin(a)*s*(.16f+i*.009f)))} }
```

## File: src/main/java/com/zerotoempire/game/EmpireArtCompat.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.material3.Text
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.flow.distinctUntilChanged
import kotlinx.coroutines.flow.map
import java.util.Locale
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.min
import kotlin.math.sin

private data class BusinessArtUiState(
    val level: Int,
    val quoteCount: Int,
    val quoteCost: Double,
    val affordable: Boolean
)

private fun businessArtUiState(state: GameState, id: Int, buyMode: BuyMode): BusinessArtUiState {
    val business = state.businesses.firstOrNull { it.id == id }
    val level = business?.level ?: 0
    if (business == null || buyMode == BuyMode.X1) {
        return BusinessArtUiState(level, 0, 0.0, false)
    }
    val quote = BulkPurchase.quote(business, state.cash, buyMode)
    return BusinessArtUiState(
        level = level,
        quoteCount = quote.count,
        quoteCost = quote.totalCost,
        affordable = quote.valid && quote.totalCost <= state.cash
    )
}

@Composable
fun BusinessArtIcon(id: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val vm: GameViewModel = viewModel()
    val buyMode by vm.buyMode.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)

    // Cash changes several times per second. In X1 mode none of that cash data is rendered
    // inside the sprite, so emit only when this business level changes. In bulk modes the
    // quote is part of the visible icon and therefore remains live.
    val uiFlow = remember(vm, id, buyMode) {
        vm.state.map { state -> businessArtUiState(state, id, buyMode) }.distinctUntilChanged()
    }
    val initialUi = remember(vm, id, buyMode) { businessArtUiState(vm.state.value, id, buyMode) }
    val ui by uiFlow.collectAsStateWithLifecycle(initialValue = initialUi)

    val level = ui.level
    val burst = remember(id) { Animatable(0f) }
    val previousLevel = remember(id) { intArrayOf(level) }

    LaunchedEffect(level, reducedMotion, lowPower) {
        val delta = level - previousLevel[0]
        previousLevel[0] = level
        if (delta > 0 && !reducedMotion) {
            burst.snapTo(min(1f, .28f + delta / 25f))
            burst.animateTo(0f, tween(if (lowPower) 420 else 650))
        } else if (reducedMotion && burst.value != 0f) {
            burst.snapTo(0f)
        }
    }

    Column(modifier = modifier, horizontalAlignment = Alignment.CenterHorizontally) {
        Box(contentAlignment = Alignment.Center) {
            if (burst.value > 0f) {
                Canvas(Modifier.size(iconSize + 26.dp)) {
                    val center = Offset(size.width / 2f, size.height / 2f)
                    val intensity = burst.value.coerceIn(0f, 1f)
                    val travel = 1f - intensity
                    val group = when (id) {
                        in 0..3 -> 0
                        in 4..7 -> 1
                        in 8..11 -> 2
                        else -> 3
                    }
                    val primary = when (group) {
                        0 -> EmpireColors.GoldBright
                        1 -> EmpireColors.Cyan
                        2 -> Color(0xFFB48CFF)
                        else -> Color.White
                    }
                    val secondary = when (group) {
                        0 -> EmpireColors.Cyan
                        1 -> Color(0xFF9A7CFF)
                        2 -> Color(0xFFFFD86A)
                        else -> Color(0xFFFF68D8)
                    }
                    val baseRays = when (group) {
                        0 -> 8
                        1 -> 10
                        2 -> 6
                        else -> 12
                    }
                    val extraRays = if (lowPower) 0 else (intensity * when (group) {
                        0 -> 16
                        1 -> 10
                        2 -> 6
                        else -> 8
                    }).toInt()
                    val rays = baseRays + extraRays
                    val radius = size.minDimension * (.32f + .18f * travel)

                    // The same purchase event now speaks the visual language of each era:
                    // energetic early-game sparks, engineered expansion locks, heavy
                    // megastructure pressure spokes, then a cleaner endgame singularity flash.
                    drawCircle(
                        color = primary,
                        radius = size.minDimension * (.16f + .06f * intensity),
                        center = center,
                        alpha = .10f * intensity
                    )
                    drawCircle(
                        color = secondary,
                        radius = size.minDimension * (.21f + .25f * travel),
                        center = center,
                        alpha = .32f * intensity,
                        style = Stroke(width = 1.4f + 2.2f * intensity)
                    )
                    drawCircle(
                        color = primary,
                        radius = size.minDimension * (.27f + .24f * travel),
                        center = center,
                        alpha = .20f * intensity,
                        style = Stroke(width = .9f + 1.5f * intensity)
                    )

                    if (group == 1) {
                        repeat(4) { i ->
                            val a = i * PI.toFloat() / 2f
                            val inner = size.minDimension * (.22f + .08f * travel)
                            val outer = size.minDimension * (.34f + .11f * travel)
                            val side = size.minDimension * .045f
                            val joint = Offset(
                                center.x + cos(a).toFloat() * outer,
                                center.y + sin(a).toFloat() * outer
                            )
                            drawLine(
                                color = primary,
                                start = Offset(center.x + cos(a).toFloat() * inner, center.y + sin(a).toFloat() * inner),
                                end = joint,
                                strokeWidth = 1.4f + intensity * 2.4f,
                                alpha = .72f * intensity
                            )
                            drawLine(
                                color = secondary,
                                start = Offset(joint.x + cos(a + PI.toFloat() / 2f) * side, joint.y + sin(a + PI.toFloat() / 2f) * side),
                                end = Offset(joint.x - cos(a + PI.toFloat() / 2f) * side, joint.y - sin(a + PI.toFloat() / 2f) * side),
                                strokeWidth = 1.1f + intensity * 1.7f,
                                alpha = .60f * intensity
                            )
                        }
                    }

                    repeat(rays) { i ->
                        val a = 2.0 * PI * i / rays + id * .17
                        val startScale = when (group) {
                            2 -> .40f
                            3 -> .58f
                            else -> .48f
                        }
                        val start = Offset(center.x + cos(a).toFloat() * radius * startScale, center.y + sin(a).toFloat() * radius * startScale)
                        val end = Offset(center.x + cos(a).toFloat() * radius, center.y + sin(a).toFloat() * radius)
                        drawLine(
                            color = when {
                                group == 3 && i % 3 == 0 -> Color.White
                                i % 2 == 0 -> primary
                                else -> secondary
                            },
                            start = start,
                            end = end,
                            strokeWidth = when (group) {
                                2 -> 2.2f + intensity * if (i % 2 == 0) 4.0f else 2.0f
                                3 -> 1.1f + intensity * 2.0f
                                else -> 1.5f + intensity * 3f
                            },
                            alpha = intensity
                        )
                    }

                    val sparkCount = if (lowPower) {
                        when (group) {
                            2, 3 -> 4
                            else -> 6
                        }
                    } else {
                        when (group) {
                            0 -> 12
                            1 -> 10
                            2 -> 6
                            else -> 8
                        }
                    }
                    repeat(sparkCount) { i ->
                        val a = 2.0 * PI * i / sparkCount + id * .31
                        val stagger = .72f + (i % 4) * .08f
                        val sparkRadius = size.minDimension * (.20f + .34f * travel * stagger)
                        val p = Offset(
                            center.x + cos(a).toFloat() * sparkRadius,
                            center.y + sin(a).toFloat() * sparkRadius
                        )
                        drawCircle(
                            color = when {
                                group == 3 && i % 3 == 0 -> Color.White
                                i % 3 == 0 -> primary
                                else -> secondary
                            },
                            radius = when (group) {
                                2 -> 1.4f + intensity * if (i % 2 == 0) 2.5f else 1.3f
                                3 -> 1.0f + intensity * 1.4f
                                else -> 1.2f + intensity * if (i % 3 == 0) 2.2f else 1.5f
                            },
                            center = p,
                            alpha = (.35f + .65f * intensity).coerceAtMost(1f)
                        )
                    }
                }
            }

            when {
                id in 0..3 -> {
                    BusinessGroup01Sprite(id, level, iconSize)
                    BusinessGroup01Evolution(id, level, iconSize)
                }
                id in 4..7 -> {
                    BusinessGroup02Sprite(id, level, iconSize)
                    BusinessGroup02Evolution(id, level, iconSize)
                }
                id in 8..11 -> {
                    BusinessGroup03Sprite(id, level, iconSize)
                    BusinessGroup03Evolution(id, level, iconSize)
                }
                id in 12..13 -> {
                    BusinessGroup04Sprite(id, level, iconSize)
                    BusinessGroup04Evolution(id, level, iconSize)
                }
                else -> PremiumBusinessSprite(id, level, iconSize)
            }

            // Early and mid-game assets now receive the same material finish as late-game
            // machinery without adding another animation clock. These marks are deliberately
            // sparse and level-gated so the base silhouettes remain readable at phone size.
            if (id in 0..7 && level >= 25) {
                Canvas(Modifier.size(iconSize)) {
                    val s = size.minDimension
                    val center = Offset(size.width / 2f, size.height / 2f)
                    val tier = when {
                        level >= 1000 -> 5
                        level >= 500 -> 4
                        level >= 250 -> 3
                        level >= 100 -> 2
                        else -> 1
                    }
                    val accent = when (id) {
                        0 -> Color(0xFF78F56A)
                        1 -> Color(0xFF58BFFF)
                        2 -> Color(0xFFFF9A43)
                        3 -> Color(0xFFB76CFF)
                        4 -> Color(0xFF67E8FF)
                        5 -> Color(0xFFFFD166)
                        6 -> Color(0xFFFF776D)
                        else -> Color(0xFFA98BFF)
                    }

                    drawCircle(
                        color = accent.copy(alpha = .20f + tier * .025f),
                        radius = s * .455f,
                        center = center,
                        style = Stroke(width = s * .0065f)
                    )
                    drawLine(
                        color = Color.White.copy(alpha = .18f + tier * .025f),
                        start = Offset(s * .25f, s * .20f),
                        end = Offset(s * .46f, s * .11f),
                        strokeWidth = s * .008f
                    )
                    drawLine(
                        color = accent.copy(alpha = .24f),
                        start = Offset(s * .54f, s * .89f),
                        end = Offset(s * .75f, s * .80f),
                        strokeWidth = s * .006f
                    )

                    if (tier >= 2) {
                        val nodeCount = if (lowPower) 2 else 4
                        repeat(nodeCount) { i ->
                            val a = (2.0 * PI * i / nodeCount) + id * .23
                            drawCircle(
                                color = if (i % 2 == 0) accent else Color.White,
                                radius = s * .009f,
                                center = Offset(
                                    center.x + cos(a).toFloat() * s * .445f,
                                    center.y + sin(a).toFloat() * s * .445f
                                ),
                                alpha = .58f
                            )
                        }
                    }
                    if (tier >= 4 && !lowPower) {
                        repeat(3) { i ->
                            drawCircle(
                                color = Color.White,
                                radius = s * .0055f,
                                center = Offset(s * (.39f + i * .11f), s * .105f),
                                alpha = .72f
                            )
                        }
                    }
                }
            }

            if (buyMode != BuyMode.X1) {
                Text(
                    text = if (ui.quoteCount > 0) "×${ui.quoteCount}" else "—",
                    color = if (ui.affordable) EmpireColors.GoldBright else EmpireColors.TextSecondary,
                    fontSize = 8.sp,
                    fontWeight = FontWeight.Black,
                    modifier = Modifier.align(Alignment.TopEnd).offset(x = 8.dp, y = (-4).dp)
                )
            }
        }

        if (buyMode != BuyMode.X1) {
            Text(
                text = if (ui.quoteCount > 0) compactMoney(ui.quoteCost) else "LOCKED",
                color = if (ui.affordable) EmpireColors.Success else EmpireColors.TextSecondary,
                fontSize = 7.sp,
                fontWeight = FontWeight.Bold,
                maxLines = 1
            )
        }
    }
}

private fun compactMoney(value: Double): String {
    if (!value.isFinite()) return "∞"
    val units = listOf(1e30 to "No", 1e27 to "Oc", 1e24 to "Sp", 1e21 to "Sx", 1e18 to "Qi", 1e15 to "Q", 1e12 to "T", 1e9 to "B", 1e6 to "M", 1e3 to "K")
    val unit = units.firstOrNull { value >= it.first }
    return if (unit == null) "$${String.format(Locale.US, "%.0f", value)}"
    else "$${String.format(Locale.US, "%.1f", value / unit.first)}${unit.second}"
}
```

## File: src/main/java/com/zerotoempire/game/EmpireCoreArt.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/**
 * Tier-aware production Power Core renderer.
 *
 * The seven reviewed FLUX masters are the canonical visual progression. Higher
 * world eras intentionally retain the T6 Singularity Crown instead of falling
 * back to procedural placeholder geometry.
 */
@Composable
fun EmpireCoreGlyph(modifier: Modifier = Modifier, eraIndex: Int = 0) {
    val context = LocalContext.current
    val tier = eraIndex.coerceIn(0, 6)
    val coreRes = remember(tier) {
        intArrayOf(
            R.drawable.zte_power_core_t0_final,
            R.drawable.zte_power_core_t1_final,
            R.drawable.zte_power_core_t2_final,
            R.drawable.zte_power_core_t3_final,
            R.drawable.zte_power_core_t4_final,
            R.drawable.zte_power_core_t5_final,
            R.drawable.zte_power_core_t6_final,
        )[tier]
    }
    val core = remember(coreRes) { ImageBitmap.imageResource(context.resources, coreRes) }
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)

    // Keep accessibility / power-saving paths completely outside the infinite
    // animation clock. This avoids allocating a perpetual transition when the
    // renderer is required to remain static.
    val pulse: Float
    if (reducedMotion) {
        pulse = 1f
    } else if (lowPower) {
        pulse = 1f
    } else {
        val infinite = rememberInfiniteTransition(label = "empireCoreRaster")
        val animatedPulse by infinite.animateFloat(
            initialValue = .94f,
            targetValue = 1f,
            animationSpec = infiniteRepeatable(
                animation = tween(1250, easing = FastOutSlowInEasing),
                repeatMode = RepeatMode.Reverse,
            ),
            label = "coreRasterPulse",
        )
        pulse = animatedPulse
    }

    Canvas(modifier) {
        val side = minOf(size.width, size.height) * pulse
        val left = (size.width - side) / 2f
        val top = (size.height - side) / 2f
        val accent = coreAccent(tier)
        drawCircle(
            brush = Brush.radialGradient(
                listOf(accent.copy(alpha = .20f), accent.copy(alpha = .06f), Color.Transparent),
                center = center,
                radius = size.minDimension * .50f,
            ),
            radius = size.minDimension * .50f,
            center = center,
        )
        drawImage(
            image = core,
            srcOffset = IntOffset.Zero,
            srcSize = IntSize(core.width, core.height),
            dstOffset = IntOffset(left.toInt(), top.toInt()),
            dstSize = IntSize(side.toInt().coerceAtLeast(1), side.toInt().coerceAtLeast(1)),
        )
    }
}

private fun coreAccent(era:Int)=when(era){
    0,1->Color(0xFFFFC857);2->Color(0xFF62E8FF);3->Color(0xFF7ED8FF);4->Color(0xFFFF765F);5->Color(0xFFFFD95A);6->Color(0xFF7ADFFF);7->Color(0xFFA685FF);8->Color(0xFFD58CFF);9->Color(0xFFFF66D8);else->Color(0xFFFFE477)}
private fun coreSecondary(era:Int)=when(era){
    0,1->Color(0xFF6EEBFF);2,3->Color(0xFFA38BFF);4->Color(0xFFFFC068);5->Color(0xFFFFF2B0);6->Color(0xFF766BFF);7,8->Color(0xFF60E9FF);9->Color(0xFF8E7CFF);else->Color(0xFFC68BFF)}

private fun DrawScope.drawCoreDepthField(
    c: Offset,
    s: Float,
    rotation: Float,
    fast: Float,
    pulse: Float,
    lowPower: Boolean,
    accent: Color,
    secondary: Color
) {
    drawCircle(
        Brush.radialGradient(
            listOf(Color.Transparent, accent.copy(alpha = .055f * pulse), secondary.copy(alpha = .035f), Color.Transparent),
            c,
            s * .44f
        ),
        s * .44f,
        c
    )

    val orbitCount = if (lowPower) 2 else 3
    repeat(orbitCount) { orbit ->
        val rx = s * (.29f + orbit * .052f)
        val ry = s * (.12f + orbit * .027f)
        val direction = if (orbit % 2 == 0) 1f else -1f
        val phase = rotation * direction + orbit * 61f
        val orbitColor = if (orbit % 2 == 0) accent else secondary
        drawArc(
            orbitColor.copy(alpha = .16f + orbit * .035f),
            phase,
            205f,
            false,
            Offset(c.x - rx, c.y - ry),
            Size(rx * 2f, ry * 2f),
            style = Stroke(s * (.007f + orbit * .0015f))
        )
        drawArc(
            Color.White.copy(alpha = .075f * pulse),
            phase + 184f,
            72f,
            false,
            Offset(c.x - rx, c.y - ry),
            Size(rx * 2f, ry * 2f),
            style = Stroke(s * .0045f)
        )
    }

    val sheenRadius = s * .205f
    val sheenAngle = Math.toRadians((fast * .72f - 36f).toDouble())
    val sheenCenter = Offset(
        c.x + cos(sheenAngle).toFloat() * s * .035f,
        c.y + sin(sheenAngle).toFloat() * s * .025f
    )
    drawArc(
        Color.White.copy(alpha = .17f * pulse),
        -58f + fast * .16f,
        82f,
        false,
        Offset(sheenCenter.x - sheenRadius, sheenCenter.y - sheenRadius),
        Size(sheenRadius * 2f, sheenRadius * 2f),
        style = Stroke(s * .009f)
    )

    if (!lowPower) {
        repeat(6) { i ->
            val angle = Math.toRadians((fast * .55f + i * 60f).toDouble())
            val rx = s * if (i % 2 == 0) .405f else .365f
            val ry = s * if (i % 2 == 0) .145f else .19f
            val p = Offset(c.x + cos(angle).toFloat() * rx, c.y + sin(angle).toFloat() * ry)
            drawCircle(
                if (i % 2 == 0) Color.White.copy(alpha = .60f) else secondary.copy(alpha = .62f),
                s * if (i % 3 == 0) .008f else .0055f,
                p
            )
        }
    }
}

private fun DrawScope.drawCoreEraGeometry(era:Int,c:Offset,s:Float,rotation:Float,fast:Float,pulse:Float,lowPower:Boolean,accent:Color,secondary:Color){
    when {
        era<=1 -> {
            drawCircle(EmpireArtPalette.Ink,s*.16f,c)
            drawCircle(accent,s*.115f,c,style=Stroke(s*.024f))
            drawLine(accent,Offset(c.x,c.y-s*.075f),Offset(c.x,c.y+s*.075f),s*.022f)
            drawLine(accent,Offset(c.x-s*.05f,c.y-s*.05f),Offset(c.x+s*.05f,c.y-s*.05f),s*.022f)
        }
        era<=3 -> {
            drawCircle(Color(0xFF10192A),s*.15f,c)
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,Color.Transparent),c,s*.12f),s*.12f,c)
            repeat(4){i->val a=Math.toRadians((rotation+i*90f).toDouble());drawLine(accent,Offset(c.x+cos(a).toFloat()*s*.13f,c.y+sin(a).toFloat()*s*.13f),Offset(c.x+cos(a).toFloat()*s*.23f,c.y+sin(a).toFloat()*s*.23f),s*.014f)}
        }
        era<=5 -> {
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,Color(0xFFFF8B2F),Color.Transparent),c,s*.18f),s*.18f,c)
            repeat(if(lowPower)6 else 12){i->val a=Math.toRadians((fast+i*(360f/(if(lowPower)6 else 12))).toDouble());val p=Offset(c.x+cos(a).toFloat()*s*.25f,c.y+sin(a).toFloat()*s*.25f);drawCircle(accent,s*.012f,p)}
        }
        era<=7 -> {
            drawCircle(Color(0xFF0C1020),s*.145f,c)
            repeat(3){r->drawCircle(if(r%2==0)accent else secondary,s*(.12f+r*.055f),c,style=Stroke(s*(.024f-r*.004f)))}
            drawCircle(Brush.radialGradient(listOf(Color.White,secondary,Color.Transparent),c,s*.09f),s*.09f,c)
        }
        era<=9 -> {
            repeat(4){r->val rx=s*(.10f+r*.045f);val ry=rx*(.50f+r*.08f);drawArc(if(r%2==0)accent else secondary,rotation*(if(r%2==0)1f else -1f)+r*41f,250f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(s*(.023f-r*.003f)))}
            drawCircle(Color.White,s*.035f,c)
            if(era>=9){val d=Path().apply{moveTo(c.x,c.y-s*.27f);lineTo(c.x+s*.27f,c.y);lineTo(c.x,c.y+s*.27f);lineTo(c.x-s*.27f,c.y);close()};drawPath(d,accent.copy(alpha=.30f),style=Stroke(s*.008f))}
        }
        else -> {
            drawCircle(Brush.radialGradient(listOf(Color.White,accent,secondary.copy(alpha=.55f),Color.Transparent),c,s*.20f),s*.20f*pulse,c)
            repeat(if(lowPower)6 else 12){i->val a=fast*PI.toFloat()/180f+i*2f*PI.toFloat()/(if(lowPower)6 else 12);val inner=s*.18f;val outer=s*(.30f+(i%3)*.035f);drawLine(if(i%2==0)accent else secondary,Offset(c.x+cos(a)*inner,c.y+sin(a)*inner),Offset(c.x+cos(a)*outer,c.y+sin(a)*outer),s*.011f)}
            drawCircle(Color.White.copy(alpha=.34f),s*.36f,c,style=Stroke(s*.008f))
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/EmpireNumberFormat.kt
```kotlin
package com.zerotoempire.game

import java.util.Locale
import kotlin.math.abs

object EmpireNumberFormat {
    private data class UnitDef(val value: Double, val suffix: String)

    private val units = listOf(
        UnitDef(1e33, "Dc"),
        UnitDef(1e30, "No"),
        UnitDef(1e27, "Oc"),
        UnitDef(1e24, "Sp"),
        UnitDef(1e21, "Sx"),
        UnitDef(1e18, "Qi"),
        UnitDef(1e15, "Qa"),
        UnitDef(1e12, "T"),
        UnitDef(1e9, "B"),
        UnitDef(1e6, "M"),
        UnitDef(1e3, "K")
    )

    fun compact(value: Double, currency: Boolean = false): String {
        if (value.isNaN()) return if (currency) "$0" else "0"
        if (value == Double.POSITIVE_INFINITY) return if (currency) "$∞" else "∞"
        if (value == Double.NEGATIVE_INFINITY) return if (currency) "-$∞" else "-∞"

        val magnitude = abs(value)
        val unit = units.firstOrNull { magnitude >= it.value }
        val body = if (unit == null) {
            when {
                magnitude >= 100.0 -> String.format(Locale.US, "%.0f", value)
                magnitude >= 10.0 -> String.format(Locale.US, "%.1f", value)
                else -> String.format(Locale.US, "%.2f", value)
            }
        } else {
            val scaled = value / unit.value
            val decimals = when {
                abs(scaled) >= 100 -> 0
                abs(scaled) >= 10 -> 1
                else -> 2
            }
            String.format(Locale.US, "%.${decimals}f%s", scaled, unit.suffix)
        }
        return if (currency) "$${body}" else body
    }

    fun money(value: Double): String = compact(value, currency = true)
}
```

## File: src/main/java/com/zerotoempire/game/EndgameAtmosphere.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Transparent cinematic overlay reserved for post-Galactic eras. */
@Composable
fun EndgameAtmosphere(eraIndex: Int, modifier: Modifier = Modifier) {
    if (eraIndex < 7) return
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)

    val phase: Float
    val fast: Float
    if (reduced) {
        phase = .38f
        fast = .22f
    } else {
        val transition = rememberInfiniteTransition(label = "endgameAtmosphere")
        val phaseAnimated by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 34_000 else 24_000, easing = LinearEasing)), label = "phase")
        val fastAnimated by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 14_000 else 8_500, easing = LinearEasing)), label = "fast")
        phase = phaseAnimated
        fast = fastAnimated
    }

    Canvas(modifier) {
        val w = size.width
        val h = size.height
        val center = Offset(w * .5f, h * .43f)
        val primary = when (eraIndex) {
            7 -> Color(0xFF6DE7FF)
            8 -> Color(0xFFC58CFF)
            9 -> Color(0xFFFF74DD)
            else -> Color(0xFFFFE59A)
        }
        val secondary = when (eraIndex) {
            7 -> Color(0xFF527BFF)
            8 -> Color(0xFFFF68B7)
            9 -> Color(0xFF77FFF1)
            else -> Color.White
        }

        val driftX = w * (.18f + phase * .64f)
        drawCircle(Brush.radialGradient(listOf(primary.copy(alpha = .11f), Color.Transparent), Offset(driftX, h * .22f), w * .38f), w * .38f, Offset(driftX, h * .22f))
        drawCircle(Brush.radialGradient(listOf(secondary.copy(alpha = .07f), Color.Transparent), Offset(w - driftX * .45f, h * .72f), w * .31f), w * .31f, Offset(w - driftX * .45f, h * .72f))

        when (eraIndex) {
            7 -> {
                repeat(if (lowPower) 3 else 5) { ring ->
                    val r = size.minDimension * (.13f + ring * .075f)
                    drawCircle(primary.copy(alpha = .08f + ring * .014f), r, center, style = Stroke(1.3f + ring * .25f))
                }
                val particleCount = MotionQuality.particleBudget(context, 18)
                repeat(particleCount) { i ->
                    val count = particleCount.coerceAtLeast(1)
                    val a = fast * PI.toFloat() * 2f + i * PI.toFloat() * 2f / count
                    val r = size.minDimension * (.18f + (i % 6) * .038f)
                    val p = Offset(center.x + cos(a) * r, center.y + sin(a) * r * .58f)
                    drawCircle(if (i % 3 == 0) secondary else primary, 1.4f + i % 3, p, alpha = .48f)
                }
            }
            8 -> repeat(MotionQuality.particleBudget(context, 22)) { i ->
                val x1 = w * (((i * 37) % 101) / 100f); val y1 = h * (((i * 53) % 97) / 100f)
                val x2 = w * ((((i + 5) * 61) % 101) / 100f); val y2 = h * ((((i + 3) * 43) % 97) / 100f)
                drawLine(primary.copy(alpha = .075f), Offset(x1, y1), Offset(x2, y2), 1f)
                drawCircle(secondary.copy(alpha = .33f), 1.7f, Offset(x1, y1))
            }
            9 -> {
                repeat(if (lowPower) 2 else 4) { i ->
                    val p = (phase + i * .25f) % 1f
                    val r = size.minDimension * (.10f + p * .38f)
                    drawCircle(primary.copy(alpha = (1f - p) * .16f), r, center, style = Stroke(1.5f + (1f-p) * 2.5f))
                }
                repeat(if (lowPower) 3 else 6) { i ->
                    val y = h * (.20f + i * .11f)
                    val offset = sin((fast + i * .13f) * PI.toFloat() * 2f) * w * .09f
                    drawLine(secondary.copy(alpha = .09f), Offset(w*.18f + offset,y), Offset(w*.82f-offset,y), 1.2f)
                }
            }
            else -> {
                drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.22f), primary.copy(alpha=.08f), Color.Transparent), center, size.minDimension*.24f), size.minDimension*.24f, center)
                repeat(if (lowPower) 3 else 5) { i ->
                    val pad = size.minDimension * (.08f + i * .035f)
                    drawArc(if(i%2==0) primary.copy(alpha=.15f) else secondary.copy(alpha=.10f), -30f + phase*60f + i*22f, 110f + i*13f, false, Offset(center.x-pad, center.y-pad*.55f), Size(pad*2f,pad*1.1f), style = Stroke(1.1f+i*.25f))
                }
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/EndgameBusinessSprites.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun EndgameBusinessSprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val motion = rememberInfiniteTransition(label = "endgameBusiness$id")
    val phase by motion.animateFloat(0f, 1f, infiniteRepeatable(tween(7600 + (id-10)*540, easing = LinearEasing)), label = "phase")
    val accent = when (id) {
        10 -> Color(0xFF67E8FF)
        11 -> Color(0xFFC692FF)
        12 -> Color(0xFFFF72D5)
        else -> Color(0xFFFFE27C)
    }
    val stage = when {
        level >= 1000 -> 5
        level >= 500 -> 4
        level >= 250 -> 3
        level >= 100 -> 2
        level >= 25 -> 1
        else -> 0
    }

    Box(modifier.size(iconSize).background(
        Brush.radialGradient(listOf(accent.copy(alpha=.22f), EmpireColors.SurfaceHigh, EmpireColors.Void)),
        RoundedCornerShape(iconSize * .30f)
    )) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val c = Offset(s*.5f,s*.5f)
            drawCircle(accent.copy(alpha=.12f + stage*.025f),s*.46f,c)
            drawCircle(accent.copy(alpha=.52f),s*.39f,c,style=Stroke(s*.015f))
            repeat(stage.coerceAtLeast(1)) { ring ->
                val r = s*(.31f+ring*.035f)
                drawArc(accent.copy(alpha=.24f),phase*360f*(if(ring%2==0)1 else -1)+ring*28f,210f,false,Offset(c.x-r,c.y-r),Size(r*2,r*2),style=Stroke(s*.009f))
            }
            when (id) {
                10 -> { // Intergalactic Gateway
                    repeat(3){r->drawCircle(if(r==1)Color.White.copy(alpha=.55f) else accent.copy(alpha=.78f-r*.16f),s*(.13f+r*.07f),c,style=Stroke(s*(.028f-r*.005f)))}
                    repeat(6){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/3f;val p=Offset(c.x+cos(a)*s*.27f,c.y+sin(a)*s*.27f);drawCircle(Color.White,s*.018f,p);drawLine(accent.copy(alpha=.55f),c,p,s*.008f)}
                }
                11 -> { // Cosmic Foundry
                    val core=Path().apply{moveTo(s*.50f,s*.22f);lineTo(s*.70f,s*.37f);lineTo(s*.64f,s*.67f);lineTo(s*.50f,s*.78f);lineTo(s*.36f,s*.67f);lineTo(s*.30f,s*.37f);close()}
                    drawPath(core,Brush.radialGradient(listOf(Color.White.copy(alpha=.75f),accent.copy(alpha=.65f),EmpireArtPalette.Steel),c,s*.30f))
                    drawPath(core,accent,style=Stroke(s*.020f))
                    repeat(4){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/2f;drawLine(accent.copy(alpha=.65f),Offset(c.x+cos(a)*s*.22f,c.y+sin(a)*s*.22f),Offset(c.x+cos(a)*s*.34f,c.y+sin(a)*s*.34f),s*.018f)}
                }
                12 -> { // Reality Engine
                    repeat(3){ring->val rx=s*(.16f+ring*.07f);val ry=rx*(.48f+ring*.08f);drawArc(accent.copy(alpha=.78f-ring*.15f),phase*360f*(if(ring%2==0)1 else -1)+ring*55f,245f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(s*(.026f-ring*.004f)))}
                    drawCircle(Color.White,s*.036f,c)
                    repeat(8){i->val a=i*PI.toFloat()/4f+phase*PI.toFloat();drawCircle(if(i%2==0)EmpireArtPalette.Cyan else accent,s*.014f,Offset(c.x+cos(a)*s*.29f,c.y+sin(a)*s*.17f))}
                }
                else -> { // Transcendent Nexus
                    drawCircle(Brush.radialGradient(listOf(Color.White,accent.copy(alpha=.65f),Color.Transparent),c,s*.19f),s*.19f,c)
                    repeat(7){i->val a=-PI.toFloat()/2f+(i-3)*.22f;drawLine(accent.copy(alpha=.72f),Offset(c.x+cos(a)*s*.17f,c.y+sin(a)*s*.17f),Offset(c.x+cos(a)*s*(.30f+(i%2)*.07f),c.y+sin(a)*s*(.30f+(i%2)*.07f)),s*.016f)}
                    drawCircle(Color.White.copy(alpha=.38f),s*.33f,c,style=Stroke(s*.008f))
                }
            }
            if(stage>=4) drawCircle(Color.White.copy(alpha=.20f),s*.47f,c,style=Stroke(s*.008f))
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/EndgameManagerPortrait.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun EndgameManagerPortrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = .31f
    val accent = when (businessId) {
        10 -> Color(0xFF67E8FF)
        11 -> Color(0xFFC692FF)
        12 -> Color(0xFFFF72D5)
        else -> Color(0xFFFFE27C)
    }
    val secondary = when (businessId) {
        10 -> Color(0xFF7D8CFF)
        11 -> Color(0xFF62E7FF)
        12 -> Color(0xFFFFB45C)
        else -> Color(0xFFC98BFF)
    }
    val skin = when (businessId) {
        10 -> Color(0xFFB97957)
        11 -> Color(0xFFE9B98B)
        12 -> Color(0xFF8F5A3C)
        else -> Color(0xFFF0C29B)
    }
    val hair = when (businessId) {
        10 -> Color(0xFF151C29)
        11 -> Color(0xFFEEE5D6)
        12 -> Color(0xFF2A163A)
        else -> Color(0xFFB98A55)
    }

    Box(
        Modifier.size(portraitSize).background(
            Brush.radialGradient(listOf(accent.copy(alpha=.32f), EmpireColors.SurfaceHigh, EmpireColors.Void)),
            RoundedCornerShape(portraitSize * .32f)
        )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val center = Offset(s*.5f,s*.5f)

            // Static executive-grade lighting: depth and hierarchy without another animation clock.
            drawCircle(
                Brush.radialGradient(
                    listOf(Color.White.copy(alpha=.10f), accent.copy(alpha=.11f), secondary.copy(alpha=.045f), Color.Transparent),
                    center = Offset(s*.43f, s*.31f),
                    radius = s*.50f
                ),
                s*.47f,
                center
            )
            drawCircle(accent.copy(alpha=.58f),s*.425f,center,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.18f),s*.455f,center,style=Stroke(s*.007f))
            drawArc(Color.White.copy(alpha=.24f),205f,72f,false,Offset(s*.075f,s*.075f),Size(s*.85f,s*.85f),style=Stroke(s*.007f))
            drawArc(accent.copy(alpha=.30f),18f,104f,false,Offset(s*.095f,s*.095f),Size(s*.81f,s*.81f),style=Stroke(s*.005f))

            val orbitCount = if(lowPower) 2 else 4
            repeat(orbitCount) { i ->
                val a = phase * 2f * PI.toFloat() + i * 2f * PI.toFloat() / orbitCount
                val p = Offset(center.x+cos(a)*s*.39f,center.y+sin(a)*s*.39f)
                drawCircle(Color.Black.copy(alpha=.42f),s*.018f,p)
                drawCircle(if(i%2==0) accent else secondary,s*.010f,p)
            }

            // Face receives a soft rim and highlight so it remains readable inside the dense endgame frame.
            drawCircle(accent.copy(alpha=.16f),s*.178f,Offset(s*.5f,s*.375f))
            drawCircle(skin,s*.165f,Offset(s*.5f,s*.375f))
            drawArc(hair,190f,160f,true,Offset(s*.325f,s*.18f),Size(s*.35f,s*.30f))
            drawArc(Color.White.copy(alpha=.13f),205f,75f,false,Offset(s*.352f,s*.225f),Size(s*.296f,s*.285f),style=Stroke(s*.007f))
            drawCircle(EmpireArtPalette.Ink,s*.014f,Offset(s*.445f,s*.375f))
            drawCircle(EmpireArtPalette.Ink,s*.014f,Offset(s*.555f,s*.375f))
            drawCircle(Color.White.copy(alpha=.72f),s*.0045f,Offset(s*.441f,s*.371f))
            drawCircle(Color.White.copy(alpha=.72f),s*.0045f,Offset(s*.551f,s*.371f))
            drawLine(accent.copy(alpha=.8f),Offset(s*.445f,s*.47f),Offset(s*.555f,s*.47f),s*.014f)

            val torso = Path().apply {
                moveTo(s*.21f,s*.84f)
                quadraticTo(s*.27f,s*.58f,s*.5f,s*.57f)
                quadraticTo(s*.73f,s*.58f,s*.79f,s*.84f)
                close()
            }
            drawPath(torso,Brush.linearGradient(listOf(Color(0xFF263B59),Color(0xFF111B2D)),Offset(s*.28f,s*.58f),Offset(s*.72f,s*.84f)))
            drawPath(torso,accent.copy(alpha=.8f),style=Stroke(s*.022f))
            drawLine(Color.White.copy(alpha=.25f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.80f),s*.010f)
            drawLine(secondary.copy(alpha=.30f),Offset(s*.31f,s*.68f),Offset(s*.42f,s*.80f),s*.007f)

            when (businessId) {
                10 -> {
                    drawArc(accent,195f,150f,false,Offset(s*.355f,s*.295f),Size(s*.29f,s*.16f),style=Stroke(s*.024f))
                    drawArc(secondary.copy(alpha=.55f),204f,132f,false,Offset(s*.37f,s*.31f),Size(s*.26f,s*.13f),style=Stroke(s*.007f))
                    drawCircle(Color.White.copy(alpha=.82f),s*.012f,Offset(s*.61f,s*.34f))
                    drawArc(accent.copy(alpha=.65f),205f,125f,false,Offset(s*.28f,s*.61f),Size(s*.44f,s*.18f),style=Stroke(s*.015f))
                    repeat(3){i->
                        val p=Offset(s*(.35f+i*.13f),s*.70f)
                        drawCircle(accent.copy(alpha=.22f),s*.022f,p)
                        drawCircle(Color.White.copy(alpha=.72f),s*.010f,p)
                    }
                }
                11 -> {
                    repeat(3){i->val x=s*(.40f+i*.10f);drawLine(accent,Offset(x,s*.205f),Offset(x+s*(i-1)*.025f,s*.14f),s*.016f)}
                    drawLine(secondary.copy(alpha=.55f),Offset(s*.36f,s*.25f),Offset(s*.64f,s*.25f),s*.006f)
                    drawRoundRect(accent.copy(alpha=.18f),Offset(s*.39f,s*.66f),Size(s*.22f,s*.10f))
                    drawRoundRect(accent.copy(alpha=.55f),Offset(s*.39f,s*.66f),Size(s*.22f,s*.10f),style=Stroke(s*.018f))
                    drawCircle(secondary.copy(alpha=.28f),s*.052f,Offset(s*.5f,s*.71f))
                    drawCircle(Color.White.copy(alpha=.84f),s*.022f,Offset(s*.5f,s*.71f))
                }
                12 -> {
                    drawArc(accent,165f,205f,false,Offset(s*.34f,s*.285f),Size(s*.32f,s*.19f),style=Stroke(s*.022f))
                    drawArc(secondary.copy(alpha=.48f),185f,160f,false,Offset(s*.365f,s*.31f),Size(s*.27f,s*.14f),style=Stroke(s*.007f))
                    drawLine(accent.copy(alpha=.7f),Offset(s*.31f,s*.64f),Offset(s*.69f,s*.79f),s*.016f)
                    drawLine(Color.White.copy(alpha=.28f),Offset(s*.33f,s*.77f),Offset(s*.67f,s*.64f),s*.010f)
                    drawCircle(secondary.copy(alpha=.24f),s*.060f,Offset(s*.64f,s*.70f))
                    drawCircle(accent,s*.026f,Offset(s*.64f,s*.70f))
                }
                else -> {
                    drawArc(accent.copy(alpha=.82f),205f,130f,false,Offset(s*.31f,s*.16f),Size(s*.38f,s*.22f),style=Stroke(s*.020f))
                    repeat(5){i->val a=(-.5f+i*.25f)*PI.toFloat();drawLine(accent.copy(alpha=.72f),Offset(s*.5f+cos(a)*s*.17f,s*.27f+sin(a)*s*.07f),Offset(s*.5f+cos(a)*s*.25f,s*.20f+sin(a)*s*.10f),s*.012f)}
                    drawCircle(secondary.copy(alpha=.18f),s*.082f,Offset(s*.5f,s*.69f))
                    drawCircle(Color.White.copy(alpha=.86f),s*.020f,Offset(s*.5f,s*.69f))
                    drawCircle(accent.copy(alpha=.55f),s*.055f,Offset(s*.5f,s*.69f),style=Stroke(s*.012f))
                }
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/EndgameProgression.kt
```kotlin
package com.zerotoempire.game

import kotlin.math.ln
import kotlin.math.max
import kotlin.math.pow

/**
 * Progression beyond the Galactic era. This layer deliberately uses logarithmic
 * growth so mature saves keep gaining power without making Double values explode.
 */
object EndgameProgression {
    private const val START = 1e18

    fun transcendenceLevel(lifetimeCash: Double): Int {
        if (!lifetimeCash.isFinite() || lifetimeCash < START) return 0
        val decades = ln(max(START, lifetimeCash) / START) / ln(10.0)
        return (decades / 3.0).toInt().coerceAtLeast(0)
    }

    fun transcendenceMultiplier(lifetimeCash: Double): Double {
        if (lifetimeCash < START || !lifetimeCash.isFinite()) return 1.0
        val decades = (ln(lifetimeCash / START) / ln(10.0)).coerceAtLeast(0.0)
        return 1.0 + 0.11 * decades.pow(0.82)
    }

    fun title(lifetimeCash: Double): String = when (transcendenceLevel(lifetimeCash)) {
        0 -> "GALACTIC"
        1 -> "INTERGALACTIC"
        2 -> "COSMIC"
        3 -> "REALITY ENGINE"
        else -> "TRANSCENDENT"
    }
}
```

## File: src/main/java/com/zerotoempire/game/EraVistaAAA.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun EraVistaAAA(eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val drift = if (!reduced) {
        val transition = rememberInfiniteTransition(label = "eraVistaAAA")
        val driftAnim by transition.animateFloat(
            0f,
            1f,
            infiniteRepeatable(tween(if (lowPower) 26000 else 16000, easing = LinearEasing)),
            label = "drift"
        )
        driftAnim
    } else .22f

    Canvas(modifier) {
        val w = size.width
        val h = size.height
        val era = eraIndex.coerceIn(0, 10)
        drawRect(Brush.verticalGradient(listOf(EmpireColors.DeepSpace, EmpireColors.Void)))
        drawStarfield(w, h, if (lowPower) 18 else 32, drift)
        drawAtmosphericDepth(w, h, era, drift, lowPower)
        when (era) {
            0 -> drawStreetEra(w, h, drift)
            1 -> drawIndustrialEra(w, h, drift)
            2 -> drawDigitalEra(w, h, drift)
            3 -> drawMegacityEra(w, h, drift)
            4 -> drawLunarEra(w, h, drift)
            5 -> drawMarsEra(w, h, drift)
            6 -> drawDysonEra(w, h, drift, lowPower)
            7 -> drawGalacticEra(w, h, drift, lowPower)
            8 -> drawIntergalacticEra(w, h, drift, lowPower)
            9 -> drawRealityEra(w, h, drift, lowPower)
            else -> drawTranscendentEra(w, h, drift, lowPower)
        }
        if (!reduced) drawAmbientTraffic(w, h, era, drift, lowPower)
    }
}

private fun DrawScope.drawAtmosphericDepth(w: Float, h: Float, era: Int, drift: Float, lowPower: Boolean) {
    val accent = when (era) {
        0 -> EmpireArtPalette.Gold
        1 -> Color(0xFFFF9B55)
        2, 4 -> EmpireArtPalette.Cyan
        3 -> EmpireArtPalette.Violet
        5 -> EmpireArtPalette.Red
        6 -> EmpireArtPalette.GoldHot
        7 -> EmpireArtPalette.Violet
        8 -> EmpireArtPalette.Cyan
        9 -> Color(0xFFFF68D8)
        else -> Color(0xFFFFE36E)
    }
    val secondary = when {
        era <= 1 -> Color(0xFF6EEBFF)
        era <= 5 -> EmpireArtPalette.Violet
        era <= 8 -> EmpireArtPalette.Cyan
        else -> Color(0xFFC68BFF)
    }
    val farX = w * (.18f + drift * .22f)
    val nearX = w * (.82f - drift * .14f)
    drawCircle(
        Brush.radialGradient(
            listOf(accent.copy(alpha = if (lowPower) .055f else .085f), Color.Transparent),
            Offset(farX, h * .25f),
            w * .42f
        ),
        w * .42f,
        Offset(farX, h * .25f)
    )
    if (!lowPower) {
        drawCircle(
            Brush.radialGradient(
                listOf(secondary.copy(alpha = .055f), Color.Transparent),
                Offset(nearX, h * .54f),
                w * .34f
            ),
            w * .34f,
            Offset(nearX, h * .54f)
        )
    }
    drawRect(
        Brush.verticalGradient(
            listOf(Color.Transparent, accent.copy(alpha = if (lowPower) .035f else .055f), Color.Transparent),
            startY = h * .54f,
            endY = h * .94f
        ),
        topLeft = Offset(0f, h * .50f),
        size = Size(w, h * .48f)
    )
    val horizonY = h * (.78f + sin(drift * 2f * PI.toFloat()) * .008f)
    drawLine(accent.copy(alpha = if (lowPower) .10f else .16f), Offset(0f, horizonY), Offset(w, horizonY), if (lowPower) 1f else 1.5f)
    if (era >= 6 && !lowPower) {
        drawArc(
            secondary.copy(alpha = .12f),
            198f,
            144f,
            false,
            Offset(w * .12f, h * .20f),
            Size(w * .76f, h * .52f),
            style = Stroke(1.4f)
        )
    }
}

private fun DrawScope.drawAmbientTraffic(w: Float, h: Float, era: Int, drift: Float, lowPower: Boolean) {
    val count = if (lowPower) 2 else when {
        era <= 1 -> 3
        era <= 5 -> 5
        else -> 7
    }
    val accent = when (era) {
        0 -> EmpireArtPalette.Gold
        1 -> Color(0xFFFF9B55)
        2, 4 -> EmpireArtPalette.Cyan
        3 -> EmpireArtPalette.Violet
        5 -> EmpireArtPalette.Red
        6 -> EmpireArtPalette.GoldHot
        7 -> EmpireArtPalette.Violet
        8 -> EmpireArtPalette.Cyan
        9 -> Color(0xFFFF68D8)
        else -> Color(0xFFFFE36E)
    }
    repeat(count) { i ->
        val lane = .18f + (i % 4) * .115f
        val speed = .55f + (i % 3) * .22f
        val phase = (drift * speed + i * .173f) % 1f
        val reverse = i % 2 == 1
        val x = if (reverse) w * (1.08f - phase * 1.16f) else w * (-.08f + phase * 1.16f)
        val y = h * lane + sin((phase + i) * PI.toFloat() * 2f) * h * if (era >= 6) .035f else .012f
        val trail = w * if (era >= 6) .075f else .04f
        val alpha = if (lowPower) .26f else .42f
        val start = Offset(x + if (reverse) trail else -trail, y)
        val end = Offset(x, y)
        drawLine(accent.copy(alpha = alpha * .48f), start, end, if (era >= 6) 2.1f else 1.4f)
        drawCircle(accent.copy(alpha = alpha), if (era >= 6) 2.6f else 1.9f, end)
        if (!lowPower && era >= 3) {
            drawCircle(Color.White.copy(alpha = alpha * .7f), 1f, end)
        }
    }
}

private fun DrawScope.drawStarfield(w:Float,h:Float,count:Int,drift:Float){repeat(count){i->val x=w*((i*37%101)/100f);val y=h*((i*61%97)/100f);val r=if(i%7==0)2.1f else 1f;drawCircle(Color.White.copy(alpha=.24f+(i%4)*.12f),r,Offset((x+w*.03f*drift*(i%3)).mod(w),y))}}
private fun DrawScope.drawStreetEra(w:Float,h:Float,d:Float){val gold=EmpireArtPalette.Gold;val base=h*.82f;drawCircle(gold.copy(alpha=.12f),h*.30f,Offset(w*.24f,h*.36f));repeat(7){i->val bw=w*.09f;val bh=h*(.18f+(i%4)*.045f);drawRoundRect(Color(0xFF182536),Offset(w*(.04f+i*.135f),base-bh),Size(bw,bh));repeat(2){j->drawCircle(gold.copy(alpha=.75f),1.8f,Offset(w*(.07f+i*.135f),base-bh*.55f+j*12f))}};drawLine(gold.copy(alpha=.45f),Offset(0f,base),Offset(w,base),2.5f)}
private fun DrawScope.drawIndustrialEra(w:Float,h:Float,d:Float){val orange=Color(0xFFFF9B55);val base=h*.84f;repeat(5){i->val x=w*(.08f+i*.19f);val bh=h*(.26f+(i%3)*.07f);drawRect(Color(0xFF222B35),Offset(x,base-bh),Size(w*.13f,bh));drawRect(orange.copy(alpha=.5f),Offset(x+w*.025f,base-bh*.72f),Size(w*.08f,h*.028f));drawRect(Color(0xFF333B45),Offset(x+w*.045f,base-bh-h*.16f),Size(w*.035f,h*.16f));drawCircle(orange.copy(alpha=.12f),h*.09f,Offset(x+w*.063f,base-bh-h*.18f-d*h*.02f))};drawLine(orange.copy(alpha=.5f),Offset(0f,base),Offset(w,base),3f)}
private fun DrawScope.drawDigitalEra(w:Float,h:Float,d:Float){val cyan=EmpireArtPalette.Cyan;repeat(9){i->val x=w*(.06f+i*.105f);val bh=h*(.20f+(i%5)*.055f);drawRect(Color(0xFF10243A),Offset(x,h*.79f-bh),Size(w*.075f,bh));drawLine(cyan.copy(alpha=.42f),Offset(x+w*.012f,h*.76f-bh),Offset(x+w*.06f,h*.76f-bh),2f)};repeat(5){i->val y=h*(.2f+i*.105f);drawLine(cyan.copy(alpha=.18f),Offset(0f,y),Offset(w,y+w*.01f*d),1f)};drawCircle(cyan.copy(alpha=.12f),h*.24f,Offset(w*(.25f+.45f*d),h*.34f))}
private fun DrawScope.drawMegacityEra(w:Float,h:Float,d:Float){val violet=EmpireArtPalette.Violet;val base=h*.84f;repeat(12){i->val x=w*(.02f+i*.082f);val bh=h*(.20f+(i*7%6)*.07f);drawRect(Color(0xFF151D31),Offset(x,base-bh),Size(w*.062f,bh));repeat(3){j->drawCircle(if((i+j)%2==0)violet else EmpireArtPalette.Cyan,1.5f,Offset(x+w*.031f,base-bh+h*(.05f+j*.065f)))}};drawArc(violet.copy(alpha=.42f),190f,160f,false,Offset(w*.17f,h*.18f),Size(w*.66f,h*.54f),style=Stroke(3f))}
private fun DrawScope.drawLunarEra(w:Float,h:Float,d:Float){val cyan=Color(0xFFEAF6FF);drawCircle(Color(0xFFB9C8D7),h*.23f,Offset(w*.73f,h*.36f));drawCircle(Color(0xFF8C99A8),h*.045f,Offset(w*.68f,h*.30f));val base=h*.82f;drawArc(cyan.copy(alpha=.55f),180f,180f,false,Offset(w*.10f,h*.46f),Size(w*.35f,h*.31f),style=Stroke(3f));repeat(5){i->drawLine(Color(0xFF9FB0C0),Offset(w*(.16f+i*.055f),h*.62f),Offset(w*(.16f+i*.055f),base),2f)};drawLine(cyan.copy(alpha=.5f),Offset(0f,base),Offset(w,base),2f)}
private fun DrawScope.drawMarsEra(w:Float,h:Float,d:Float){val red=EmpireArtPalette.Red;drawCircle(Color(0xFFB34235),h*.24f,Offset(w*.76f,h*.37f));drawCircle(Color(0xFF7A2E28),h*.05f,Offset(w*.68f,h*.32f));val base=h*.83f;repeat(4){i->val x=w*(.10f+i*.19f);drawRoundRect(Color(0xFF3B2929),Offset(x,h*.57f),Size(w*.13f,h*.18f));drawArc(red,180f,180f,false,Offset(x-w*.01f,h*.48f),Size(w*.15f,h*.18f),style=Stroke(3f));drawCircle(red.copy(alpha=.7f),2f,Offset(x+w*.065f,h*.64f))};drawLine(red.copy(alpha=.4f),Offset(0f,base),Offset(w,base),3f)}
private fun DrawScope.drawDysonEra(w:Float,h:Float,d:Float,low:Boolean){val gold=EmpireArtPalette.GoldHot;val c=Offset(w*.5f,h*.45f);drawCircle(Brush.radialGradient(listOf(Color.White,gold,Color.Transparent),c,h*.22f),h*.22f,c);repeat(if(low)3 else 5){r->drawCircle(gold.copy(alpha=.68f-r*.1f),h*(.24f+r*.035f),c,style=Stroke(2.5f))};repeat(if(low)6 else 12){i->val a=d*2f*PI.toFloat()+i*2f*PI.toFloat()/(if(low)6 else 12);drawCircle(Color.White,2.2f,Offset(c.x+cos(a)*w*.32f,c.y+sin(a)*h*.25f))}}
private fun DrawScope.drawGalacticEra(w:Float,h:Float,d:Float,low:Boolean){val violet=EmpireArtPalette.Violet;val c=Offset(w*.5f,h*.46f);repeat(if(low)3 else 6){i->drawArc(violet.copy(alpha=.18f+i*.07f),d*360f+i*35f,210f,false,Offset(c.x-w*(.15f+i*.035f),c.y-h*(.10f+i*.025f)),Size(w*(.30f+i*.07f),h*(.20f+i*.05f)),style=Stroke(2f))};drawCircle(Color.White,h*.045f,c);repeat(if(low)4 else 9){i->val a=i*2f*PI.toFloat()/(if(low)4 else 9)-d;drawCircle(if(i%2==0)EmpireArtPalette.Cyan else violet,2.4f,Offset(c.x+cos(a)*w*.37f,c.y+sin(a)*h*.27f))}}
private fun DrawScope.drawIntergalacticEra(w:Float,h:Float,d:Float,low:Boolean){val cyan=EmpireArtPalette.Cyan;val mag=EmpireArtPalette.Magenta;val c=Offset(w*.5f,h*.45f);drawCircle(cyan.copy(alpha=.10f),h*.27f,c);drawCircle(cyan,h*.20f,c,style=Stroke(3.5f));drawCircle(mag,h*.13f,c,style=Stroke(2.5f));repeat(if(low)4 else 8){i->val a=d*2f*PI.toFloat()+i*PI.toFloat()/4f;drawLine(color=if(i%2==0)cyan else mag,start=Offset(c.x+cos(a)*w*.12f,c.y+sin(a)*h*.09f),end=Offset(c.x+cos(a)*w*.32f,c.y+sin(a)*h*.25f),strokeWidth=2f)};drawCircle(Color.White,h*.045f,c)}
private fun DrawScope.drawRealityEra(w:Float,h:Float,d:Float,low:Boolean){val pink=Color(0xFFFF68D8);val cyan=Color(0xFF6EEBFF);val c=Offset(w*.5f,h*.45f);repeat(4){r->val rx=w*(.12f+r*.06f);val ry=h*(.08f+r*.035f);drawArc(if(r%2==0)pink else cyan,d*360f*(if(r%2==0)1 else -1)+r*45f,255f,false,Offset(c.x-rx,c.y-ry),Size(rx*2,ry*2),style=Stroke(3f-r*.3f))};drawCircle(Color.White,h*.055f,c);val p=Path().apply{moveTo(c.x,h*.12f);lineTo(w*.78f,c.y);lineTo(c.x,h*.78f);lineTo(w*.22f,c.y);close()};drawPath(p,pink.copy(alpha=.24f),style=Stroke(2f))}
private fun DrawScope.drawTranscendentEra(w:Float,h:Float,d:Float,low:Boolean){val gold=Color(0xFFFFE36E);val violet=Color(0xFFC68BFF);val c=Offset(w*.5f,h*.45f);drawCircle(Brush.radialGradient(listOf(Color.White,gold.copy(alpha=.9f),violet.copy(alpha=.25f),Color.Transparent),c,h*.26f),h*.26f,c);repeat(3){r->drawCircle(if(r%2==0)gold else violet,h*(.15f+r*.07f),c,style=Stroke(3f-r*.45f))};repeat(if(low)6 else 12){i->val a=d*2f*PI.toFloat()+i*2f*PI.toFloat()/(if(low)6 else 12);drawLine(color=if(i%2==0)gold else violet,start=Offset(c.x+cos(a)*w*.11f,c.y+sin(a)*h*.08f),end=Offset(c.x+cos(a)*w*.34f,c.y+sin(a)*h*.27f),strokeWidth=2.4f)};drawCircle(Color.White,h*.05f,c)}
```

## File: src/main/java/com/zerotoempire/game/EraVistaCinematicOverlay.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext

/**
 * Lightweight foreground treatment for EraVista. It deliberately owns no animation state:
 * the vista beneath it already supplies motion, while this layer adds depth and lens framing
 * without another frame clock or persistent allocation stream.
 */
@Composable
fun EraVistaCinematicOverlay(eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val lowPower = MotionQuality.lowPowerMode(context)
    val era = eraIndex.coerceIn(0, 10)
    val accent = when (era) {
        0 -> EmpireArtPalette.Gold
        1 -> Color(0xFFFF9B55)
        2, 4 -> EmpireArtPalette.Cyan
        3 -> EmpireArtPalette.Violet
        5 -> EmpireArtPalette.Red
        6 -> EmpireArtPalette.GoldHot
        7 -> EmpireArtPalette.Violet
        8 -> EmpireArtPalette.Cyan
        9 -> Color(0xFFFF68D8)
        else -> Color(0xFFFFE36E)
    }

    Canvas(modifier.fillMaxSize()) {
        val w = size.width
        val h = size.height
        val center = Offset(w * .5f, h * .45f)

        // Optical vignette: preserves the focal center while giving the vista a camera-like frame.
        drawRect(
            brush = Brush.radialGradient(
                colors = listOf(
                    Color.Transparent,
                    Color.Transparent,
                    Color.Black.copy(alpha = if (lowPower) .24f else .32f)
                ),
                center = center,
                radius = size.maxDimension * .72f
            )
        )

        // Foreground atmospheric falloff separates UI/silhouettes from the distant scene.
        drawRect(
            brush = Brush.verticalGradient(
                colors = listOf(Color.Transparent, Color.Black.copy(alpha = if (lowPower) .12f else .20f)),
                startY = h * .54f,
                endY = h
            ),
            topLeft = Offset(0f, h * .52f),
            size = Size(w, h * .48f)
        )

        // Era-colored horizon bloom. Cheap, static, and visually binds every vista to its era palette.
        drawRect(
            brush = Brush.verticalGradient(
                colors = listOf(
                    Color.Transparent,
                    accent.copy(alpha = if (lowPower) .025f else .055f),
                    Color.Transparent
                ),
                startY = h * .64f,
                endY = h * .91f
            ),
            topLeft = Offset(0f, h * .60f),
            size = Size(w, h * .34f)
        )

        if (!lowPower) {
            // Thin anamorphic edge glints add a premium lens treatment without bloom shaders.
            drawLine(accent.copy(alpha = .15f), Offset(w * .06f, h * .09f), Offset(w * .30f, h * .09f), 1.2f)
            drawLine(accent.copy(alpha = .11f), Offset(w * .70f, h * .91f), Offset(w * .94f, h * .91f), 1.2f)
            if (era >= 6) {
                drawArc(
                    color = accent.copy(alpha = .09f),
                    startAngle = 198f,
                    sweepAngle = 144f,
                    useCenter = false,
                    topLeft = Offset(w * .08f, h * .10f),
                    size = Size(w * .84f, h * .70f),
                    style = Stroke(1.2f)
                )
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/FoundryWorldMotion.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import kotlin.math.abs

/**
 * One shared motion phase for lightweight authored worker, vehicle and machine activity
 * in the Foundry district. Decorative motion stops completely when Android animations
 * are disabled or battery saver is active.
 */
@Composable
internal fun FoundryWorkerTraffic(
    businessId: Int,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val phase = remember { Animatable(.18f) }

    LaunchedEffect(reducedMotion) {
        if (reducedMotion) {
            phase.snapTo(.32f)
        } else {
            phase.snapTo(0f)
            while (true) {
                phase.animateTo(1f, tween(durationMillis = 7200, easing = LinearEasing))
                phase.snapTo(0f)
            }
        }
    }

    BoxWithConstraints(modifier.fillMaxSize()) {
        val widthPx = constraints.maxWidth.toFloat()
        val heightPx = constraints.maxHeight.toFloat()
        val p = phase.value

        // Four transparent raster frames run at ~10 fps from the existing shared district
        // clock. The second worker is two frames out of phase so the crowd does not march
        // in lockstep. Reduced motion remains a deterministic frozen pose.
        val workerFrames = intArrayOf(
            R.drawable.zte_foundry_worker_raster_f0,
            R.drawable.zte_foundry_worker_raster_f1,
            R.drawable.zte_foundry_worker_raster_f2,
            R.drawable.zte_foundry_worker_raster_f3
        )
        val workerFrameIndex = if (reducedMotion) 0 else ((p * 72f).toInt() and 3)
        val secondWorkerFrameIndex = if (reducedMotion) 0 else (((p * 72f).toInt() + 2) and 3)

        Image(
            painter = painterResource(workerFrames[workerFrameIndex]),
            contentDescription = null,
            modifier = Modifier
                .size(34.dp)
                .graphicsLayer {
                    val edgeFade = (minOf(p, 1f - p) * 12f).coerceIn(0f, 1f)
                    translationX = widthPx * (.19f + p * .24f)
                    translationY = heightPx * (.48f + p * .11f)
                    alpha = if (reducedMotion) .76f else (.18f + edgeFade * .74f)
                    scaleX = .92f
                    scaleY = .92f
                }
        )

        Image(
            painter = painterResource(workerFrames[secondWorkerFrameIndex]),
            contentDescription = null,
            modifier = Modifier
                .size(29.dp)
                .graphicsLayer {
                    val q = (p + .52f) % 1f
                    val edgeFade = (minOf(q, 1f - q) * 12f).coerceIn(0f, 1f)
                    translationX = widthPx * (.73f - q * .20f)
                    translationY = heightPx * (.57f + q * .08f)
                    alpha = if (reducedMotion) .62f else (.16f + edgeFade * .66f)
                    scaleX = -.82f
                    scaleY = .82f
                }
        )

        if (businessId == 1 || businessId == 3) {
            Image(
                painter = painterResource(R.drawable.zte_foundry_delivery_v1_runtime),
                contentDescription = null,
                modifier = Modifier
                    .size(46.dp)
                    .graphicsLayer {
                        val r = (p + .24f) % 1f
                        translationX = widthPx * (.08f + r * .58f)
                        translationY = heightPx * (.70f - r * .15f)
                        alpha = if (reducedMotion) .74f else .94f
                        scaleX = .78f
                        scaleY = .78f
                    }
            )
        }

        if (businessId == 2 || businessId == 3) {
            val route = if (reducedMotion) .38f else (p + .63f) % 1f
            val forkliftFrame = if (reducedMotion || route < .32f || route > .70f) {
                R.drawable.zte_foundry_forklift_v1_runtime
            } else {
                R.drawable.zte_foundry_forklift_load_v1_runtime
            }

            Image(
                painter = painterResource(forkliftFrame),
                contentDescription = null,
                modifier = Modifier
                    .size(44.dp)
                    .graphicsLayer {
                        translationX = widthPx * (.34f + route * .24f)
                        translationY = heightPx * (.66f - route * .07f)
                        alpha = if (reducedMotion) .76f else .96f
                        scaleX = if (route < .5f) .74f else -.74f
                        scaleY = .74f
                    }
            )

            // Authored spark/smoke activity gives industrial lots a visible production beat
            // without introducing another animation clock. The overlay freezes to a subtle,
            // readable state in reduced-motion / battery-saver mode.
            Image(
                painter = painterResource(R.drawable.zte_foundry_machine_activity_t0_runtime),
                contentDescription = null,
                modifier = Modifier
                    .size(if (businessId == 2) 45.dp else 39.dp)
                    .graphicsLayer {
                        val cycle = if (reducedMotion) .35f else (p * 3f) % 1f
                        val pulse = 1f - abs(cycle * 2f - 1f)
                        translationX = widthPx * if (businessId == 2) .51f else .57f
                        translationY = heightPx * if (businessId == 2) .34f else .40f
                        alpha = if (reducedMotion) .34f else (.28f + pulse * .64f)
                        val activityScale = if (reducedMotion) .70f else (.66f + pulse * .18f)
                        scaleX = activityScale
                        scaleY = activityScale
                        rotationZ = if (reducedMotion) 0f else (cycle - .5f) * 5f
                    }
            )
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/FullScreenAdActivityPolicy.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity

/** Conservative lifecycle gate shared by full-screen ad surfaces.
 * A finishing/destroyed Activity must never be handed to an ad SDK because
 * configuration changes and background transitions can invalidate it between
 * preload and show.
 */
internal fun Activity.canHostFullScreenAd(): Boolean = !isFinishing && !isDestroyed
```

## File: src/main/java/com/zerotoempire/game/GameEconomy.kt
```kotlin
package com.zerotoempire.game

/**
 * Central deterministic economy rules.
 * Keep balance formulas here so gameplay, offline progress and tests use the same model.
 */
object GameEconomy {
    private val milestones = listOf(
        1000 to 128.0,
        500 to 64.0,
        250 to 32.0,
        100 to 16.0,
        50 to 8.0,
        25 to 4.0,
        10 to 2.0
    )

    fun milestoneMultiplier(level: Int): Double =
        milestones.firstOrNull { (requiredLevel, _) -> level >= requiredLevel }?.second ?: 1.0
}
```

## File: src/main/java/com/zerotoempire/game/GameEngine.kt
```kotlin
package com.zerotoempire.game

import java.time.LocalDate

data class Business(
    val id: Int,
    val name: String,
    val emoji: String,
    val baseCost: Double,
    val baseIncome: Double,
    val level: Int = 0
) {
    val nextCost: Double get() = EconomyMath.growthCost(baseCost, level)
    val rawIncomePerSecond: Double get() = EconomyMath.finite(baseIncome * level.coerceAtLeast(0) * GameEconomy.milestoneMultiplier(level))
    val nextMilestone: Int? get() = listOf(10, 25, 50, 100, 250, 500, 1000).firstOrNull { it > level }
}

data class GameState(
    val cash: Double = 10.0,
    val lifetimeCash: Double = 10.0,
    val prestigePoints: Int = 0,
    val businesses: List<Business> = defaultBusinesses(),
    val hiredManagerIds: Set<Int> = emptySet(),
    val upgradeRanks: Map<String, Int> = emptyMap(),
    val gems: Int = 0,
    val boostEndsAtMillis: Long = 0L
) {
    val prestigeUpgradeRank: Int get() = upgradeRanks["prestige"] ?: 0
    val incomeUpgradeRank: Int get() = upgradeRanks["income"] ?: 0
    val tapUpgradeRank: Int get() = upgradeRanks["tap"] ?: 0
    val prestigeMultiplier: Double get() = EconomyMath.finite(1.0 + prestigePoints.coerceAtLeast(0) * (0.12 * (1.0 + prestigeUpgradeRank * .08)))
    val legacyMasteryMultiplier: Double get() = EconomyMath.finite(LateGame.legacyMasteryMultiplier(prestigePoints))
    val portfolioDepthMultiplier: Double get() = EconomyMath.finite(LateGame.portfolioDepthMultiplier(businesses))
    val transcendenceMultiplier: Double get() = EconomyMath.finite(EndgameProgression.transcendenceMultiplier(lifetimeCash))
    val globalUpgradeMultiplier: Double get() = EconomyMath.finite(1.0 + incomeUpgradeRank * .10)
    val boostMultiplier: Double get() = if (System.currentTimeMillis() < boostEndsAtMillis) 2.0 else 1.0
    val eventMultiplier: Double get() = LiveOps.currentEvent(LocalDate.now())?.incomeMultiplier ?: 1.0

    fun businessIncome(b: Business): Double {
        val manager = Managers.catalog.firstOrNull { it.businessId == b.id && it.businessId in hiredManagerIds }
        return EconomyMath.finite(b.rawIncomePerSecond * (manager?.incomeMultiplier ?: 1.0))
    }

    val permanentIncomeMultiplier: Double
        get() = EconomyMath.finite(prestigeMultiplier * legacyMasteryMultiplier * portfolioDepthMultiplier * transcendenceMultiplier * globalUpgradeMultiplier)

    private val globalIncomeMultiplier: Double
        get() = EconomyMath.finite(permanentIncomeMultiplier * boostMultiplier * eventMultiplier)

    /** All owned businesses generate while the player is active. */
    val incomePerSecond: Double
        get() = EconomyMath.finite(businesses.sumOf(::businessIncome) * globalIncomeMultiplier)

    /** Base automated income before temporary boost/event multipliers. */
    val automatedBaseIncomePerSecond: Double
        get() = EconomyMath.finite(businesses.filter { it.id in hiredManagerIds }.sumOf(::businessIncome) * permanentIncomeMultiplier)

    /** Only manager-operated businesses continue generating while the app is away. */
    val automatedIncomePerSecond: Double
        get() = EconomyMath.finite(automatedBaseIncomePerSecond * boostMultiplier * eventMultiplier)

    val tapValue: Double
        get() = EconomyMath.finite((1.0 + incomePerSecond * .05) * prestigeMultiplier * legacyMasteryMultiplier * transcendenceMultiplier * (1.0 + tapUpgradeRank * .25))
    val empireLevel: Int get() = EmpireEras.current(lifetimeCash).index
}

fun defaultBusinesses() = listOf(
    Business(0, "Street Stand", "☕", 10.0, 1.0),
    Business(1, "Corner Shop", "🏪", 120.0, 8.0),
    Business(2, "Workshop", "🔧", 1_500.0, 70.0),
    Business(3, "Factory", "🏭", 25_000.0, 900.0),
    Business(4, "Tech Company", "💻", 500_000.0, 15_000.0),
    Business(5, "Megacity", "🌆", 15_000_000.0, 400_000.0),
    Business(6, "Moon Colony", "🌕", 800_000_000.0, 18_000_000.0),
    Business(7, "Mars Empire", "🔴", 75_000_000_000.0, 1_200_000_000.0),
    Business(8, "Dyson Network", "☀️", 12_000_000_000_000.0, 160_000_000_000.0),
    Business(9, "Galactic Exchange", "🌌", 4.0e15, 3.5e13),
    Business(10, "Intergalactic Gateway", "◎", 2.0e18, 1.8e16),
    Business(11, "Cosmic Foundry", "◇", 8.0e21, 8.5e19),
    Business(12, "Reality Engine", "✦", 3.0e25, 4.2e23),
    Business(13, "Transcendent Nexus", "✧", 1.2e29, 2.4e27)
)
```

## File: src/main/java/com/zerotoempire/game/GameFeel.kt
```kotlin
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
```

## File: src/main/java/com/zerotoempire/game/GameRepository.kt
```kotlin
package com.zerotoempire.game

import android.content.Context
import androidx.datastore.core.handlers.ReplaceFileCorruptionHandler
import androidx.datastore.preferences.core.*
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.first

private val Context.gameDataStore by preferencesDataStore(
    name = "zero_empire_save_v2",
    corruptionHandler = ReplaceFileCorruptionHandler { emptyPreferences() }
)

class GameRepository(private val context: Context) {
    private object Keys {
        val cash = doublePreferencesKey("cash")
        val lifetime = doublePreferencesKey("lifetime")
        val prestige = intPreferencesKey("prestige")
        val gems = intPreferencesKey("gems")
        val taps = longPreferencesKey("taps")
        val purchases = longPreferencesKey("purchases")
        val prestigeCount = intPreferencesKey("prestige_count")
        val streak = intPreferencesKey("streak")
        val lastDaily = longPreferencesKey("last_daily")
        val lastSeen = longPreferencesKey("last_seen")
        val boostEnd = longPreferencesKey("boost_end")
        val missions = stringSetPreferencesKey("claimed_missions")
        val achievements = stringSetPreferencesKey("claimed_achievements")
        val challenges = stringSetPreferencesKey("claimed_challenges")
        val challengeWeek = stringPreferencesKey("challenge_week")
        val challengeTapBase = longPreferencesKey("challenge_tap_base")
        val challengePurchaseBase = longPreferencesKey("challenge_purchase_base")
        val challengePrestigeBase = intPreferencesKey("challenge_prestige_base")
        val onboarding = booleanPreferencesKey("onboarding_completed")
        val highestEra = intPreferencesKey("highest_era_seen")
        val adsRemoved = booleanPreferencesKey("ads_removed")
        val starterPack = booleanPreferencesKey("starter_pack_owned")
        val creditedPurchaseTokens = stringSetPreferencesKey("credited_purchase_tokens")
        fun level(id: Int) = intPreferencesKey("business_${id}_level")
        fun manager(id: Int) = booleanPreferencesKey("manager_$id")
        fun upgrade(id: String) = intPreferencesKey("upgrade_$id")
    }

    data class Save(val state: GameState, val meta: PlayerMeta, val lastSeenMillis: Long, val creditedPurchaseTokens: Set<String>)

    suspend fun load(): Save {
        val p = context.gameDataStore.data.first()
        val businesses = defaultBusinesses().map { business ->
            business.copy(level = (p[Keys.level(business.id)] ?: 0).coerceAtLeast(0))
        }
        val managers = Managers.catalog.filter { p[Keys.manager(it.businessId)] == true }.map { it.businessId }.toSet()
        val upgrades = Upgrades.catalog.associate { upgrade ->
            upgrade.id to (p[Keys.upgrade(upgrade.id)] ?: 0).coerceIn(0, upgrade.maxRank)
        }
        val rawCash = p[Keys.cash] ?: 10.0
        val rawLifetime = p[Keys.lifetime] ?: 10.0
        val cash = if (rawCash.isFinite() && rawCash >= 0.0) rawCash.coerceAtMost(EconomyMath.MAX_VALUE) else 10.0
        val lifetime = if (rawLifetime.isFinite() && rawLifetime >= 0.0) rawLifetime.coerceIn(10.0, EconomyMath.MAX_VALUE) else maxOf(10.0, cash)
        val gems = (p[Keys.gems] ?: 0).coerceAtLeast(0)
        val taps = (p[Keys.taps] ?: 0L).coerceAtLeast(0L)
        val purchases = (p[Keys.purchases] ?: 0L).coerceAtLeast(0L)
        val prestigeCount = (p[Keys.prestigeCount] ?: 0).coerceAtLeast(0)
        val currentWeek = ChallengeRotation.weeklyKey()
        val storedWeek = p[Keys.challengeWeek] ?: ""
        val sameWeek = storedWeek == currentWeek

        val state = GameState(
            cash = cash,
            lifetimeCash = maxOf(lifetime, cash),
            prestigePoints = (p[Keys.prestige] ?: 0).coerceAtLeast(0),
            businesses = businesses,
            hiredManagerIds = managers,
            upgradeRanks = upgrades,
            gems = gems,
            boostEndsAtMillis = (p[Keys.boostEnd] ?: 0L).coerceAtLeast(0L)
        )
        val meta = PlayerMeta(
            gems = gems,
            totalTaps = taps,
            totalPurchases = purchases,
            prestigeCount = prestigeCount,
            streakDays = (p[Keys.streak] ?: 0).coerceAtLeast(0),
            lastDailyClaimEpochDay = p[Keys.lastDaily] ?: -1L,
            boostEndsAtMillis = state.boostEndsAtMillis,
            claimedMissionIds = p[Keys.missions] ?: emptySet(),
            claimedAchievementIds = p[Keys.achievements] ?: emptySet(),
            claimedChallengeIds = p[Keys.challenges] ?: emptySet(),
            challengeWeekKey = currentWeek,
            challengeWeekTapBase = if (sameWeek) (p[Keys.challengeTapBase] ?: taps).coerceIn(0L, taps) else taps,
            challengeWeekPurchaseBase = if (sameWeek) (p[Keys.challengePurchaseBase] ?: purchases).coerceIn(0L, purchases) else purchases,
            challengeWeekPrestigeBase = if (sameWeek) (p[Keys.challengePrestigeBase] ?: prestigeCount).coerceIn(0, prestigeCount) else prestigeCount,
            onboardingCompleted = p[Keys.onboarding] ?: false,
            highestEraSeen = (p[Keys.highestEra] ?: 0).coerceIn(0, EmpireEras.catalog.lastIndex),
            adsRemoved = p[Keys.adsRemoved] ?: false,
            starterPackOwned = p[Keys.starterPack] ?: false
        )
        return Save(state, meta, (p[Keys.lastSeen] ?: 0L).coerceAtLeast(0L), p[Keys.creditedPurchaseTokens] ?: emptySet())
    }

    suspend fun save(s: GameState, m: PlayerMeta, creditedPurchaseTokens: Set<String> = emptySet(), now: Long = System.currentTimeMillis()) {
        context.gameDataStore.edit { p ->
            p[Keys.cash] = EconomyMath.finite(s.cash)
            p[Keys.lifetime] = EconomyMath.finite(s.lifetimeCash)
            p[Keys.prestige] = s.prestigePoints.coerceAtLeast(0)
            p[Keys.gems] = s.gems.coerceAtLeast(0)
            p[Keys.taps] = m.totalTaps.coerceAtLeast(0L)
            p[Keys.purchases] = m.totalPurchases.coerceAtLeast(0L)
            p[Keys.prestigeCount] = m.prestigeCount.coerceAtLeast(0)
            p[Keys.streak] = m.streakDays.coerceAtLeast(0)
            p[Keys.lastDaily] = m.lastDailyClaimEpochDay
            p[Keys.lastSeen] = now.coerceAtLeast(0L)
            p[Keys.boostEnd] = s.boostEndsAtMillis.coerceAtLeast(0L)
            p[Keys.missions] = m.claimedMissionIds
            p[Keys.achievements] = m.claimedAchievementIds
            p[Keys.challenges] = m.claimedChallengeIds
            p[Keys.challengeWeek] = m.challengeWeekKey
            p[Keys.challengeTapBase] = m.challengeWeekTapBase.coerceAtLeast(0L)
            p[Keys.challengePurchaseBase] = m.challengeWeekPurchaseBase.coerceAtLeast(0L)
            p[Keys.challengePrestigeBase] = m.challengeWeekPrestigeBase.coerceAtLeast(0)
            p[Keys.onboarding] = m.onboardingCompleted
            p[Keys.highestEra] = m.highestEraSeen.coerceIn(0, EmpireEras.catalog.lastIndex)
            p[Keys.adsRemoved] = m.adsRemoved
            p[Keys.starterPack] = m.starterPackOwned
            p[Keys.creditedPurchaseTokens] = creditedPurchaseTokens
            s.businesses.forEach { p[Keys.level(it.id)] = it.level.coerceAtLeast(0) }
            Managers.catalog.forEach { p[Keys.manager(it.businessId)] = it.businessId in s.hiredManagerIds }
            Upgrades.catalog.forEach { upgrade -> p[Keys.upgrade(upgrade.id)] = (s.upgradeRanks[upgrade.id] ?: 0).coerceIn(0, upgrade.maxRank) }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/GameTheme.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.material3.darkColorScheme
import androidx.compose.ui.graphics.Color

object EmpireColors {
    val Void = Color(0xFF050914)
    val DeepSpace = Color(0xFF09152A)
    val Surface = Color(0xFF101D33)
    val SurfaceHigh = Color(0xFF172943)
    val Gold = Color(0xFFFFC857)
    val GoldBright = Color(0xFFFFE08A)
    val Cyan = Color(0xFF48E5E9)
    val Violet = Color(0xFF9B7BFF)
    val Success = Color(0xFF69E7A5)
    val TextPrimary = Color(0xFFF7FAFF)
    val TextSecondary = Color(0xFF9EB0C9)
}

val EmpireColorScheme = darkColorScheme(
    primary = EmpireColors.Gold,
    secondary = EmpireColors.Cyan,
    tertiary = EmpireColors.Violet,
    background = EmpireColors.Void,
    surface = EmpireColors.Surface,
    onPrimary = EmpireColors.Void,
    onBackground = EmpireColors.TextPrimary,
    onSurface = EmpireColors.TextPrimary
)
```

## File: src/main/java/com/zerotoempire/game/GameViewModel.kt
```kotlin
package com.zerotoempire.game

import android.app.Application
import android.os.SystemClock
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharedFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import java.time.LocalDate

class GameViewModel(application: Application) : AndroidViewModel(application) {
    private val repository = GameRepository(application.applicationContext)

    private val _state = MutableStateFlow(GameState())
    val state: StateFlow<GameState> = _state.asStateFlow()
    private val _meta = MutableStateFlow(PlayerMeta())
    val meta: StateFlow<PlayerMeta> = _meta.asStateFlow()
    private val _offlineReward = MutableStateFlow<OfflineReward?>(null)
    val offlineReward: StateFlow<OfflineReward?> = _offlineReward.asStateFlow()
    private val _celebration = MutableStateFlow<MajorCelebration?>(null)
    val celebration: StateFlow<MajorCelebration?> = _celebration.asStateFlow()
    private val _buyMode = MutableStateFlow(BuyMode.X1)
    val buyMode: StateFlow<BuyMode> = _buyMode.asStateFlow()
    private val _rewardedRequests = MutableSharedFlow<RewardPlacement>(extraBufferCapacity = 1)
    val rewardedRequests: SharedFlow<RewardPlacement> = _rewardedRequests.asSharedFlow()

    private var loaded = false
    private var saveJob: Job? = null
    private var saveDirty = false
    @Volatile private var appForeground = true
    @Volatile private var resetTickClock = true
    private var backgroundedAtMillis: Long = 0L
    private val offlineRewardAdGate = RewardRequestGate()
    private val profitBoostAdGate = RewardRequestGate()
    private var purchaseCreditLedger = PurchaseCreditLedger()

    init {
        viewModelScope.launch {
            val save = repository.load()
            purchaseCreditLedger = PurchaseCreditLedger(save.creditedPurchaseTokens)
            var restored = save.state
            val reward = OfflineProgress.calculate(restored, save.lastSeenMillis)
            if (reward.eligible) {
                restored = restored.copy(
                    cash = EconomyMath.safeAdd(restored.cash, reward.cash),
                    lifetimeCash = EconomyMath.safeAdd(restored.lifetimeCash, reward.cash)
                )
                _offlineReward.value = reward
            }
            _state.value = restored
            val eraIndex = EmpireEras.current(restored.lifetimeCash).index
            _meta.value = save.meta.copy(gems = restored.gems, boostEndsAtMillis = restored.boostEndsAtMillis, highestEraSeen = maxOf(save.meta.highestEraSeen, eraIndex))
            loaded = true
            if (appForeground) persistNow()

            launch {
                var previousTickNanos = SystemClock.elapsedRealtimeNanos()
                while (true) {
                    delay(250L)
                    val nowNanos = SystemClock.elapsedRealtimeNanos()
                    if (!appForeground || resetTickClock) {
                        previousTickNanos = nowNanos
                        resetTickClock = false
                        continue
                    }
                    val elapsedSeconds = (nowNanos - previousTickNanos).coerceAtLeast(0L) / 1_000_000_000.0
                    previousTickNanos = nowNanos
                    val s = _state.value
                    val gain = EconomyMath.finite(s.incomePerSecond * elapsedSeconds)
                    if (gain > 0.0) {
                        val updated = s.copy(
                            cash = EconomyMath.safeAdd(s.cash, gain),
                            lifetimeCash = EconomyMath.safeAdd(s.lifetimeCash, gain)
                        )
                        _state.value = updated
                        checkEraUnlock(updated)
                    }
                }
            }
            launch {
                while (true) {
                    delay(30_000L)
                    if (appForeground) {
                        ensureChallengeWeek()
                        persistNow()
                    }
                }
            }
        }
    }

    fun onAppBackgrounded(nowMillis: Long = System.currentTimeMillis()) {
        if (!appForeground) return
        appForeground = false
        resetTickClock = true
        backgroundedAtMillis = nowMillis
        if (loaded) {
            val stateSnapshot = _state.value
            val metaSnapshot = _meta.value
            viewModelScope.launch {
                repository.save(stateSnapshot, metaSnapshot, purchaseCreditLedger.snapshot(), nowMillis)
                // Do not clear saveDirty here: a foreground mutation may have arrived
                // while this background snapshot was being written. The foreground
                // coalescing worker owns that flag and will persist the newer state.
            }
        }
    }

    fun onAppForegrounded(nowMillis: Long = System.currentTimeMillis()) {
        if (appForeground) return
        val startedAt = backgroundedAtMillis
        backgroundedAtMillis = 0L
        appForeground = true
        resetTickClock = true
        if (!loaded || startedAt <= 0L || nowMillis <= startedAt) return

        val reward = OfflineProgress.calculate(_state.value, startedAt, nowMillis)
        if (reward.eligible) {
            val updated = _state.value.copy(
                cash = EconomyMath.safeAdd(_state.value.cash, reward.cash),
                lifetimeCash = EconomyMath.safeAdd(_state.value.lifetimeCash, reward.cash)
            )
            _state.value = updated
            _offlineReward.value = reward
            checkEraUnlock(updated)
            scheduleSave()
        }
    }

    fun setBuyMode(mode: BuyMode) { _buyMode.value = mode }
    fun completeOnboarding() { if (!_meta.value.onboardingCompleted) { _meta.value = _meta.value.copy(onboardingCompleted = true); scheduleSave() } }
    fun dismissCelebration() { _celebration.value = null }
    fun dismissOfflineReward() {
        offlineRewardAdGate.release()
        _offlineReward.value = null
    }
    fun requestDoubleOfflineAd() {
        if (_offlineReward.value?.eligible != true || !offlineRewardAdGate.request()) return
        if (!_rewardedRequests.tryEmit(RewardPlacement.DOUBLE_OFFLINE_EARNINGS)) offlineRewardAdGate.release()
    }
    fun onRewardedUnavailable(placement: RewardPlacement) {
        when (placement) {
            RewardPlacement.DOUBLE_OFFLINE_EARNINGS -> offlineRewardAdGate.release()
            RewardPlacement.PROFIT_BOOST -> profitBoostAdGate.release()
            else -> Unit
        }
    }
    fun requestProfitBoostAd() {
        if (!profitBoostAdGate.request()) return
        if (!_rewardedRequests.tryEmit(RewardPlacement.PROFIT_BOOST)) profitBoostAdGate.release()
    }
    fun canClaimDaily(): Boolean = _meta.value.lastDailyClaimEpochDay != LocalDate.now().toEpochDay()

    fun ensureChallengeWeek() {
        val key = ChallengeRotation.weeklyKey()
        val m = _meta.value
        if (m.challengeWeekKey == key) return
        _meta.value = m.copy(
            challengeWeekKey = key,
            challengeWeekTapBase = m.totalTaps,
            challengeWeekPurchaseBase = m.totalPurchases,
            challengeWeekPrestigeBase = m.prestigeCount
        )
        scheduleSave()
    }

    fun claimDaily(): RewardDay? {
        val today = LocalDate.now().toEpochDay(); val meta = _meta.value
        if (meta.lastDailyClaimEpochDay == today) return null
        val nextStreak = if (meta.lastDailyClaimEpochDay == today - 1) meta.streakDays + 1 else 1
        val reward = LoginCalendar.rewardFor(nextStreak); val s = _state.value
        val boostBase = maxOf(System.currentTimeMillis(), s.boostEndsAtMillis)
        val boostEnd = if (reward.multiplierMinutes > 0) boostBase + reward.multiplierMinutes * 60_000L else s.boostEndsAtMillis
        val newGems = safeGemAdd(s.gems, reward.gems)
        _state.value = s.copy(gems = newGems, boostEndsAtMillis = boostEnd)
        _meta.value = meta.copy(gems = newGems, streakDays = nextStreak, lastDailyClaimEpochDay = today, boostEndsAtMillis = boostEnd)
        scheduleSave(); return reward
    }

    fun missions(): List<Mission> = Progression.missions(_state.value, _meta.value)
    fun achievements(): List<Achievement> = Progression.achievements(_state.value, _meta.value)
    fun challenges(): List<TimedChallenge> { ensureChallengeWeek(); return ChallengeRotation.current(_state.value, _meta.value) }

    fun claimMission(id: String): Boolean { val m=missions().firstOrNull{it.id==id}?:return false; if(!m.completed||m.claimed)return false; val g=safeGemAdd(_state.value.gems,m.rewardGems);_state.value=_state.value.copy(gems=g); _meta.value=_meta.value.copy(gems=g,claimedMissionIds=_meta.value.claimedMissionIds+id); scheduleSave(); return true }
    fun claimAchievement(id: String):Boolean { val a=achievements().firstOrNull{it.id==id}?:return false; if(!a.unlocked||a.claimed)return false; val g=safeGemAdd(_state.value.gems,a.rewardGems);_state.value=_state.value.copy(gems=g); _meta.value=_meta.value.copy(gems=g,claimedAchievementIds=_meta.value.claimedAchievementIds+id); scheduleSave(); return true }
    fun claimChallenge(id: String): Boolean { val c=challenges().firstOrNull{it.id==id}?:return false; if(!c.completed||c.claimed)return false; val g=safeGemAdd(_state.value.gems,c.rewardGems);_state.value=_state.value.copy(gems=g); _meta.value=_meta.value.copy(gems=g,claimedChallengeIds=_meta.value.claimedChallengeIds+id); _celebration.value=MajorCelebration("CHALLENGE COMPLETE","+${c.rewardGems} gems earned","★","WEEKLY"); scheduleSave(); return true }

    fun applyEntitlements(
        products: Set<StoreProduct>,
        authoritativePermanentEntitlements: Boolean = false
    ) {
        val hadStarter = _meta.value.starterPackOwned
        val restoredStarter = StoreProduct.STARTER_PACK in products && !hadStarter
        val hasRemoveAds = PurchaseRecovery.permanentOwned(
            StoreProduct.REMOVE_ADS,
            _meta.value.adsRemoved,
            products,
            authoritativePermanentEntitlements
        )
        val hasStarter = PurchaseRecovery.permanentOwned(
            StoreProduct.STARTER_PACK,
            hadStarter,
            products,
            authoritativePermanentEntitlements
        )
        val recoveredConsumableGems = (if (StoreProduct.GEM_PACK_SMALL in products) 120 else 0) + (if (StoreProduct.GEM_PACK_MEDIUM in products) 650 else 0)
        val restoredStarterGems = if (restoredStarter) 250 else 0
        val totalRecoveredGems = recoveredConsumableGems + restoredStarterGems
        if (totalRecoveredGems > 0) _state.value = _state.value.copy(gems = safeGemAdd(_state.value.gems, totalRecoveredGems))
        _meta.value = _meta.value.copy(gems = _state.value.gems, adsRemoved = hasRemoveAds, starterPackOwned = hasStarter)
        if (restoredStarter) activateProfitBoost(30)
        if (totalRecoveredGems > 0) {
            val detail = if (restoredStarter) "Starter Pack and purchase rewards restored." else "+$totalRecoveredGems gems restored."
            _celebration.value = MajorCelebration("PURCHASE RECOVERED", detail, "◆", "STORE")
        }
        scheduleSave()
    }

    fun applyPurchase(product: StoreProduct, transactionId: String) {
        if (!purchaseCreditLedger.claim(transactionId)) return
        when (product) {
            StoreProduct.REMOVE_ADS -> _meta.value = _meta.value.copy(adsRemoved = true)
            StoreProduct.STARTER_PACK -> if (!_meta.value.starterPackOwned) { _state.value = _state.value.copy(gems = safeGemAdd(_state.value.gems, 250)); _meta.value = _meta.value.copy(gems = _state.value.gems, starterPackOwned = true); activateProfitBoost(30) }
            StoreProduct.GEM_PACK_SMALL -> grantGems(120)
            StoreProduct.GEM_PACK_MEDIUM -> grantGems(650)
        }
        _celebration.value = MajorCelebration("PURCHASE COMPLETE", "Your empire has been upgraded.", "◆", "STORE")
        scheduleSave()
    }

    fun rewardDoubleOffline() {
        if (!offlineRewardAdGate.consume()) return
        val reward = _offlineReward.value ?: return
        if (!reward.eligible) return
        _state.value = _state.value.copy(
            cash = EconomyMath.safeAdd(_state.value.cash, reward.cash),
            lifetimeCash = EconomyMath.safeAdd(_state.value.lifetimeCash, reward.cash)
        )
        _offlineReward.value = null
        _celebration.value = MajorCelebration("OFFLINE PROFITS ×2", "+${EmpireNumberFormat.compact(reward.cash)} bonus cash", "⚡", "REWARDED")
        scheduleSave()
    }
    fun rewardProfitBoost() {
        if (!profitBoostAdGate.consume()) return
        activateProfitBoost(10)
        _celebration.value = MajorCelebration("OVERDRIVE ACTIVE", "All profits doubled for 10 minutes.", "⚡", "REWARDED")
    }

    fun tap() {
        ensureChallengeWeek()
        val s=_state.value
        val u=s.copy(
            cash=EconomyMath.safeAdd(s.cash,s.tapValue),
            lifetimeCash=EconomyMath.safeAdd(s.lifetimeCash,s.tapValue)
        )
        _state.value=u; _meta.value=_meta.value.copy(totalTaps=(_meta.value.totalTaps+1).coerceAtLeast(_meta.value.totalTaps)); checkEraUnlock(u); scheduleSave()
    }

    fun buy(id: Int) { buyBulk(id, _buyMode.value) }
    fun bulkQuote(id: Int, mode: BuyMode = _buyMode.value): BulkQuote { val s = _state.value; val b = s.businesses.firstOrNull { it.id == id } ?: return BulkQuote(0, 0.0); return BulkPurchase.quote(b, s.cash, mode) }

    fun buyBulk(id: Int, mode: BuyMode): BulkQuote {
        ensureChallengeWeek()
        val s = _state.value; val b = s.businesses.firstOrNull { it.id == id } ?: return BulkQuote(0, 0.0)
        val quote = BulkPurchase.quote(b, s.cash, mode); if (!quote.valid || quote.totalCost > s.cash) return BulkQuote(0, 0.0)
        val newLevel = if (b.level > Int.MAX_VALUE - quote.count) Int.MAX_VALUE else b.level + quote.count
        val actualCount = newLevel - b.level
        if (actualCount <= 0) return BulkQuote(0, 0.0)
        val actualCost = if (actualCount == quote.count) quote.totalCost else BulkPurchase.cost(b, actualCount)
        val updatedBusiness = b.copy(level = newLevel)
        _state.value = s.copy(cash = (s.cash - actualCost).coerceAtLeast(0.0), businesses = s.businesses.map { if (it.id == id) updatedBusiness else it })
        _meta.value = _meta.value.copy(totalPurchases = safeLongAdd(_meta.value.totalPurchases, actualCount.toLong()))
        val crossed = BulkPurchase.crossedMilestones(b.level, newLevel)
        if (crossed.isNotEmpty()) _celebration.value = Celebrations.milestone(updatedBusiness.copy(level = crossed.last()))
        else if (actualCount >= 10) _celebration.value = MajorCelebration("MASS EXPANSION", "+$actualCount ${b.name} levels", "▲", "EXPANSION")
        scheduleSave(); return BulkQuote(actualCount, actualCost)
    }

    fun hireManager(businessId:Int):Boolean{val s=_state.value;val m=Managers.catalog.firstOrNull{it.businessId==businessId}?:return false;if(businessId in s.hiredManagerIds||s.cash<m.cost)return false;_state.value=s.copy(cash=s.cash-m.cost,hiredManagerIds=s.hiredManagerIds+businessId);scheduleSave();return true}
    fun buyUpgrade(id:String):Boolean{val s=_state.value;val u=Upgrades.catalog.firstOrNull{it.id==id}?:return false;val r=s.upgradeRanks[id]?:0;if(r>=u.maxRank||s.gems<u.gemCost)return false;_state.value=s.copy(gems=s.gems-u.gemCost,upgradeRanks=s.upgradeRanks+(id to r+1));syncMetaCurrency();scheduleSave();return true}
    fun grantGems(amount:Int){if(amount>0){_state.value=_state.value.copy(gems=safeGemAdd(_state.value.gems,amount));syncMetaCurrency();scheduleSave()}}
    fun activateProfitBoost(){requestProfitBoostAd()}
    fun activateProfitBoost(minutes:Int){if(minutes<=0)return;val s=_state.value;val base=maxOf(System.currentTimeMillis(),s.boostEndsAtMillis);val extension=minutes.toLong()*60_000L;val end=if(base>Long.MAX_VALUE-extension)Long.MAX_VALUE else base+extension;_state.value=s.copy(boostEndsAtMillis=end);_meta.value=_meta.value.copy(boostEndsAtMillis=end);scheduleSave()}
    fun prestige(){
        ensureChallengeWeek()
        val reset = Progression.prestigeReset(_state.value) ?: return
        _state.value = reset
        _meta.value = _meta.value.copy(
            prestigeCount = if (_meta.value.prestigeCount == Int.MAX_VALUE) Int.MAX_VALUE else _meta.value.prestigeCount + 1,
            boostEndsAtMillis = reset.boostEndsAtMillis
        )
        _celebration.value = MajorCelebration("ASCENSION COMPLETE","Legacy power permanently increased.","◇","PRESTIGE")
        scheduleSave()
    }

    private fun checkEraUnlock(s:GameState){val era=EmpireEras.current(s.lifetimeCash);if(era.index>_meta.value.highestEraSeen){_meta.value=_meta.value.copy(highestEraSeen=era.index);_celebration.value=Celebrations.era(era);scheduleSave()}}
    private fun syncMetaCurrency(){_meta.value=_meta.value.copy(gems=_state.value.gems)}
    private fun scheduleSave(){
        if (!loaded) return
        saveDirty = true
        if (saveJob?.isActive == true) return
        saveJob = viewModelScope.launch {
            delay(350L)
            while (appForeground && saveDirty) {
                saveDirty = false
                persistNow()
                if (saveDirty) delay(350L)
            }
        }
    }
    private suspend fun persistNow(){
        if (!loaded) return
        // Clear before taking the snapshot. Mutations that arrive while DataStore writes
        // will set the flag again and force the coalescing worker to perform another pass.
        saveDirty = false
        val stateSnapshot = _state.value
        val metaSnapshot = _meta.value
        repository.save(stateSnapshot, metaSnapshot)
    }
    private fun safeGemAdd(current:Int, amount:Int):Int = if(amount<=0) current else if(current>Int.MAX_VALUE-amount) Int.MAX_VALUE else current+amount
    private fun safeLongAdd(current:Long, amount:Long):Long = if(amount<=0) current else if(current>Long.MAX_VALUE-amount) Long.MAX_VALUE else current+amount
    override fun onCleared(){if(loaded&&appForeground){val s=_state.value;val m=_meta.value;viewModelScope.launch{repository.save(s,m)}};super.onCleared()}
}
```

## File: src/main/java/com/zerotoempire/game/GrowthRuntime.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import android.content.ContextWrapper
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel

/** Runtime shell. Visual atmosphere must stay behind gameplay so it can never
 * obscure or intercept phone UI. Persistent controls live inside the Scaffold. */
@Composable
fun GrowthRuntimeRoot(vm: GameViewModel = viewModel()) {
    val context = LocalContext.current
    val activity = remember(context) { context.findGrowthActivity() }
    val lifecycleOwner = LocalLifecycleOwner.current
    val telemetry = remember(context) { LocalGrowthTelemetry(context.applicationContext) }
    val state = vm.state.collectAsStateWithLifecycle().value
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val celebration = vm.celebration.collectAsStateWithLifecycle().value
    val adsAllowed = PrivacyConsentManager.adsAllowed.collectAsStateWithLifecycle().value
    val eraIndex = EmpireEras.current(state.lifetimeCash).index

    DisposableEffect(lifecycleOwner, vm) {
        val observer = LifecycleEventObserver { _, event ->
            when (event) {
                Lifecycle.Event.ON_START -> vm.onAppForegrounded()
                Lifecycle.Event.ON_STOP -> vm.onAppBackgrounded()
                else -> Unit
            }
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        if (lifecycleOwner.lifecycle.currentState.isAtLeast(Lifecycle.State.STARTED)) vm.onAppForegrounded()
        onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }

    LaunchedEffect(Unit) { telemetry.track(GrowthEvent.SessionStarted) }
    LaunchedEffect(eraIndex) { GameMusicBus.setEmpireLevel(eraIndex) }
    LaunchedEffect(meta.onboardingCompleted) {
        if (meta.onboardingCompleted) telemetry.track(GrowthEvent.OnboardingCompleted)
    }
    LaunchedEffect(state.businesses.sumOf { it.level }) {
        if (state.businesses.any { it.level > 0 }) telemetry.track(GrowthEvent.FirstAssetPurchased)
    }
    LaunchedEffect(state.hiredManagerIds.size) {
        if (state.hiredManagerIds.isNotEmpty()) telemetry.track(GrowthEvent.FirstManagerHired)
    }
    LaunchedEffect(meta.prestigeCount) {
        if (meta.prestigeCount > 0) telemetry.track(GrowthEvent.FirstPrestige)
    }
    LaunchedEffect(celebration?.accent) {
        if (celebration?.accent == "REWARDED") telemetry.track(GrowthEvent.FirstRewardedCompleted)
    }

    SfxRuntime(vm)

    Box(Modifier.fillMaxSize()) {
        // Draw ambience first. CommerceRoot contains every interactive surface.
        EndgameAtmosphere(eraIndex = eraIndex, modifier = Modifier.fillMaxSize())
        CommerceRoot(vm)
        // Purely visual, input-transparent punctuation for major progression changes.
        CinematicRuntimeTransitionOverlay(eraIndex = eraIndex, modifier = Modifier.fillMaxSize())
    }

    if (activity != null) {
        RewardedController(
            activity = activity,
            adsAllowed = adsAllowed,
            vm = vm
        )
        InterstitialController(
            activity = activity,
            adsAllowed = adsAllowed,
            vm = vm,
            telemetry = telemetry
        )
    }
}

private tailrec fun Context.findGrowthActivity(): Activity? = when (this) {
    is Activity -> this
    is ContextWrapper -> baseContext.findGrowthActivity()
    else -> null
}
```

## File: src/main/java/com/zerotoempire/game/GrowthTelemetry.kt
```kotlin
package com.zerotoempire.game

import android.content.Context
import android.util.Log

sealed interface GrowthEvent {
    data object SessionStarted : GrowthEvent
    data object OnboardingCompleted : GrowthEvent
    data object FirstAssetPurchased : GrowthEvent
    data object FirstManagerHired : GrowthEvent
    data object FirstPrestige : GrowthEvent
    data object FirstRewardedCompleted : GrowthEvent
    data object StoreOpened : GrowthEvent
    data class PurchaseCompleted(val productId: String) : GrowthEvent
    data class InterstitialShown(val breakPoint: NaturalBreakPoint) : GrowthEvent
}

interface GrowthTelemetry {
    fun track(event: GrowthEvent)
}

class LocalGrowthTelemetry(context: Context) : GrowthTelemetry {
    private val prefs = context.getSharedPreferences("zero_empire_growth_telemetry", Context.MODE_PRIVATE)

    override fun track(event: GrowthEvent) {
        val key = when (event) {
            GrowthEvent.SessionStarted -> null
            GrowthEvent.OnboardingCompleted -> "onboarding_completed"
            GrowthEvent.FirstAssetPurchased -> "first_asset"
            GrowthEvent.FirstManagerHired -> "first_manager"
            GrowthEvent.FirstPrestige -> "first_prestige"
            GrowthEvent.FirstRewardedCompleted -> "first_rewarded"
            GrowthEvent.StoreOpened -> null
            is GrowthEvent.PurchaseCompleted -> null
            is GrowthEvent.InterstitialShown -> null
        }
        if (key != null && prefs.getBoolean(key, false)) return
        if (key != null) prefs.edit().putBoolean(key, true).apply()
        Log.i("ZeroEmpireGrowth", event.toString())
    }
}
```

## File: src/main/java/com/zerotoempire/game/HologramScanSweep.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val ScanFrameSize = 128
private const val ScanColumns = 4
private const val ScanFrameCount = 8

/** Dyson Network scan volume, frozen on frame zero under reduced motion. */
@Composable
internal fun HologramScanSweep(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_11_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }
    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) while (true) {
            delay(125)
            frame = (frame + 1) % ScanFrameCount
        }
    }
    Canvas(modifier) {
        val effectSize = size.minDimension * .64f
        val destination = Offset((size.width - effectSize) * .5f, (size.height - effectSize) * .5f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset((frame % ScanColumns) * ScanFrameSize, (frame / ScanColumns) * ScanFrameSize),
            srcSize = IntSize(ScanFrameSize, ScanFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .58f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/IdentitySystems.kt
```kotlin
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
```

## File: src/main/java/com/zerotoempire/game/IdentityUi.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.semantics.LiveRegionMode
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.liveRegion
import androidx.compose.ui.semantics.stateDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.delay

/** Identity/gameplay presentation root. Persistent HUD controls live inside the scroll layout. */
@Composable
fun EmpireRoot(vm: GameViewModel = viewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val celebration by vm.celebration.collectAsStateWithLifecycle()
    val eraIndex = EmpireEras.current(state.lifetimeCash).index
    var previousEra by remember { mutableIntStateOf(eraIndex) }
    var eraTransitionVisible by remember { mutableStateOf(false) }

    LaunchedEffect(eraIndex) {
        if (eraIndex > previousEra && meta.onboardingCompleted) {
            eraTransitionVisible = true
            GameSfxBus.play(PremiumSfxCue.PRESTIGE)
            delay(1550)
            eraTransitionVisible = false
        }
        previousEra = eraIndex
    }

    Box(Modifier.fillMaxSize()) {
        PremiumZeroToEmpireApp(vm)
        if (meta.onboardingCompleted) {
            PremiumMilestoneCelebration(state = state, modifier = Modifier.fillMaxSize())
        }
        if (!meta.onboardingCompleted) {
            OnboardingOverlay(
                onTapSound = { GameSfxBus.play(PremiumSfxCue.UI, .85f) },
                onComplete = { GameSfxBus.play(PremiumSfxCue.REWARD); vm.completeOnboarding() }
            )
        }
        celebration?.let { item ->
            CelebrationOverlay(
                item = item,
                onShown = { GameSfxBus.play(if (item.accent == "PRESTIGE") PremiumSfxCue.PRESTIGE else PremiumSfxCue.MILESTONE) },
                onDismiss = vm::dismissCelebration
            )
        }
        EraTransitionOverlay(eraIndex = eraIndex, visible = eraTransitionVisible, modifier = Modifier.fillMaxSize())
    }
}

@Composable
private fun OnboardingOverlay(onTapSound: () -> Unit, onComplete: () -> Unit) {
    var step by remember { mutableIntStateOf(0) }
    val steps = listOf(
        Triple("ZERO", "You start with almost nothing. Tap to create your first capital.", "TAP → EARN"),
        Triple("BUILD", "Buy assets. Every level increases automatic income.", "EARN → INVEST"),
        Triple("SCALE", "Hit power-spike levels to multiply production dramatically.", "10 • 25 • 50 • 100"),
        Triple("AUTOMATE", "Hire managers, stack upgrades and keep earning while offline.", "SYSTEMS → MOMENTUM"),
        Triple("ASCEND", "When growth slows, reset the run for permanent Legacy power.", "RESET → RETURN STRONGER")
    )
    val current = steps[step]
    Box(Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(EmpireColors.Void, EmpireColors.DeepSpace))), contentAlignment = Alignment.Center) {
        Column(
            Modifier
                .fillMaxWidth()
                .padding(28.dp)
                .semantics {
                    stateDescription = "Onboarding step ${step + 1} of ${steps.size}: ${current.first}"
                },
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text("ZERO → EMPIRE", color = EmpireColors.Gold, fontSize = 28.sp, fontWeight = FontWeight.Black)
            Spacer(Modifier.height(12.dp)); OnboardingStepArt(step); Spacer(Modifier.height(8.dp))
            Text(current.first, color = EmpireColors.TextPrimary, fontSize = 36.sp, fontWeight = FontWeight.Black)
            Spacer(Modifier.height(10.dp))
            Text(current.second, color = EmpireColors.TextSecondary, fontSize = 16.sp, textAlign = TextAlign.Center, lineHeight = 23.sp)
            Spacer(Modifier.height(14.dp))
            Surface(shape = RoundedCornerShape(50), color = EmpireColors.SurfaceHigh) { Text(current.third, modifier = Modifier.padding(horizontal = 18.dp, vertical = 9.dp), color = EmpireColors.Cyan, fontWeight = FontWeight.Bold, fontSize = 12.sp) }
            Spacer(Modifier.height(22.dp))
            LinearProgressIndicator(progress = { (step + 1) / steps.size.toFloat() }, modifier = Modifier.fillMaxWidth().height(5.dp), color = EmpireColors.Gold, trackColor = EmpireColors.SurfaceHigh)
            Spacer(Modifier.height(16.dp))
            Button(onClick = { onTapSound(); if (step == steps.lastIndex) onComplete() else step++ }, modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp), shape = RoundedCornerShape(16.dp)) {
                Text(if (step == steps.lastIndex) "BUILD MY EMPIRE" else "CONTINUE", fontWeight = FontWeight.Black)
            }
        }
    }
}

@Composable
private fun CelebrationOverlay(item: MajorCelebration, onShown: () -> Unit, onDismiss: () -> Unit) {
    var visible by remember(item) { mutableStateOf(true) }
    LaunchedEffect(item) { onShown(); delay(2100); visible = false; delay(280); onDismiss() }
    if (!visible) return
    Box(Modifier.fillMaxSize().background(EmpireColors.Void.copy(alpha = .72f)), contentAlignment = Alignment.Center) {
        Surface(
            shape = RoundedCornerShape(28.dp),
            color = EmpireColors.SurfaceHigh,
            shadowElevation = 28.dp,
            modifier = Modifier
                .padding(24.dp)
                .semantics {
                    liveRegion = LiveRegionMode.Assertive
                    contentDescription = "${item.accent}. ${item.title}. ${item.subtitle}"
                }
        ) {
            Column(Modifier.padding(28.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                MetaSprite(MetaSpriteKind.ACHIEVEMENT, 76.dp)
                Spacer(Modifier.height(14.dp))
                Text(item.accent, color = EmpireColors.Gold, fontSize = 12.sp, fontWeight = FontWeight.Black, letterSpacing = 2.sp)
                Text(item.title, color = EmpireColors.TextPrimary, fontSize = 28.sp, fontWeight = FontWeight.Black, textAlign = TextAlign.Center)
                Spacer(Modifier.height(8.dp))
                Text(item.subtitle, color = EmpireColors.TextSecondary, fontSize = 13.sp, textAlign = TextAlign.Center)
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/IncomePickupSparkle.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val IncomeSparkleFrameSize = 128
private const val IncomeSparkleColumns = 4
private const val IncomeSparkleFrameCount = 8

/** Compact income feedback sparkle; reduced motion retains a quiet static glint. */
@Composable
internal fun IncomePickupSparkle(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_09_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }
    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) while (true) {
            delay(125)
            frame = (frame + 1) % IncomeSparkleFrameCount
            if (frame == 0) delay(1_250)
        }
    }
    Canvas(modifier) {
        val effectSize = size.minDimension * .34f
        val destination = Offset(size.width * .60f, size.height * .10f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                (frame % IncomeSparkleColumns) * IncomeSparkleFrameSize,
                (frame / IncomeSparkleColumns) * IncomeSparkleFrameSize
            ),
            srcSize = IntSize(IncomeSparkleFrameSize, IncomeSparkleFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .82f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/IndustrialBusinessFx.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val IndustrialFxFrameSize = 128
private const val IndustrialFxColumns = 4
private const val IndustrialFxFrameCount = 8

private enum class IndustrialFxKind {
    SMALL_FURNACE,
    LARGE_PLASMA,
    SMOKE,
}

@Composable
private fun IndustrialFxLoop(
    kind: IndustrialFxKind,
    modifier: Modifier = Modifier,
) {
    val context = LocalContext.current
    // Read snapshot-backed motion policy directly so Battery Saver / animation
    // changes recompose this loop without requiring the world stage to restart.
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val resource = when (kind) {
        IndustrialFxKind.SMALL_FURNACE -> R.drawable.zte_fx_01_final
        IndustrialFxKind.LARGE_PLASMA -> R.drawable.zte_fx_02_final
        IndustrialFxKind.SMOKE -> R.drawable.zte_fx_03_final
    }
    val sheet: ImageBitmap = remember(resource) {
        BitmapFactory.decodeResource(context.resources, resource).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(kind, reducedMotion, lowPower) {
        frame = when (kind) {
            IndustrialFxKind.SMALL_FURNACE -> 3
            IndustrialFxKind.LARGE_PLASMA -> 4
            IndustrialFxKind.SMOKE -> 3
        }
        if (!reducedMotion) {
            while (true) {
                delay(if (lowPower) 250 else 125)
                frame = (frame + if (lowPower) 2 else 1) % IndustrialFxFrameCount
            }
        }
    }

    Canvas(modifier) {
        val side = when (kind) {
            IndustrialFxKind.SMALL_FURNACE -> size.minDimension * .24f
            IndustrialFxKind.LARGE_PLASMA -> size.minDimension * .34f
            IndustrialFxKind.SMOKE -> size.minDimension * .28f
        }
        val destination = when (kind) {
            IndustrialFxKind.SMALL_FURNACE -> Offset(size.width * .18f, size.height * .49f)
            IndustrialFxKind.LARGE_PLASMA -> Offset(size.width * .34f, size.height * .40f)
            IndustrialFxKind.SMOKE -> Offset(size.width * .56f, size.height * .06f)
        }
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                (frame % IndustrialFxColumns) * IndustrialFxFrameSize,
                (frame / IndustrialFxColumns) * IndustrialFxFrameSize,
            ),
            srcSize = IntSize(IndustrialFxFrameSize, IndustrialFxFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(side.toInt().coerceAtLeast(1), side.toInt().coerceAtLeast(1)),
            alpha = when (kind) {
                IndustrialFxKind.SMALL_FURNACE -> .72f
                IndustrialFxKind.LARGE_PLASMA -> .68f
                IndustrialFxKind.SMOKE -> .46f
            },
        )
    }
}

/**
 * Brings the remaining historical industrial FX into visible gameplay without
 * replacing the authored building identity. Reduced-motion users receive a
 * stable representative frame; battery saver advances at half cadence.
 */
@Composable
internal fun IndustrialBusinessFx(
    businessId: Int,
    tier: Int,
    modifier: Modifier = Modifier,
) {
    when (businessId) {
        2 -> {
            if (tier >= 2) {
                IndustrialFxLoop(IndustrialFxKind.SMALL_FURNACE, modifier)
            }
        }
        3 -> {
            if (tier >= 2) {
                IndustrialFxLoop(IndustrialFxKind.SMOKE, modifier)
            }
            if (tier >= 4) {
                IndustrialFxLoop(IndustrialFxKind.LARGE_PLASMA, modifier)
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/InterstitialController.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import java.time.LocalDate

@Composable
fun InterstitialController(
    activity: Activity,
    adsAllowed: Boolean,
    vm: GameViewModel,
    telemetry: GrowthTelemetry
) {
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val celebration = vm.celebration.collectAsStateWithLifecycle().value
    val gateway = remember(activity) { AdMobInterstitialGateway(activity.applicationContext) }
    val frequency = remember(activity) { InterstitialFrequencyStore(activity.applicationContext) }

    LaunchedEffect(adsAllowed, meta.adsRemoved) {
        val enabled = adsAllowed && !meta.adsRemoved
        gateway.setEnabled(enabled)
        if (enabled) gateway.preload()
    }

    LaunchedEffect(celebration, adsAllowed, meta.adsRemoved, meta.onboardingCompleted) {
        if (!adsAllowed || celebration == null || meta.adsRemoved) return@LaunchedEffect
        val breakPoint = when (celebration.accent) {
            "PRESTIGE" -> NaturalBreakPoint.PRESTIGE
            "NEW ERA", "ERA" -> NaturalBreakPoint.ERA_UNLOCK
            else -> return@LaunchedEffect
        }
        val now = System.currentTimeMillis()
        val today = LocalDate.now().toEpochDay()
        if (!InterstitialPolicy.canShow(
                state = frequency.snapshot(),
                nowMillis = now,
                currentEpochDay = today,
                breakPoint = breakPoint,
                onboardingCompleted = meta.onboardingCompleted,
                adsRemoved = meta.adsRemoved
            )) return@LaunchedEffect
        if (!gateway.isReady()) {
            gateway.preload()
            return@LaunchedEffect
        }
        gateway.show(
            activity = activity,
            onShown = {
                frequency.recordShow(System.currentTimeMillis())
                telemetry.track(GrowthEvent.InterstitialShown(breakPoint))
            }
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/InterstitialPolicy.kt
```kotlin
package com.zerotoempire.game

import android.content.Context
import java.time.LocalDate

enum class NaturalBreakPoint { PRESTIGE, ERA_UNLOCK }

data class InterstitialPolicyState(
    val sessionStartedAtMillis: Long,
    val sessionShows: Int = 0,
    val lastShownAtMillis: Long = 0L,
    val dayEpoch: Long = LocalDate.now().toEpochDay(),
    val dayShows: Int = 0
)

object InterstitialPolicy {
    const val MIN_SESSION_AGE_MS = 12L * 60_000L
    const val MIN_GAP_MS = 8L * 60_000L
    const val MAX_PER_SESSION = 2
    const val MAX_PER_DAY = 4

    fun canShow(
        state: InterstitialPolicyState,
        nowMillis: Long,
        currentEpochDay: Long,
        breakPoint: NaturalBreakPoint,
        onboardingCompleted: Boolean,
        adsRemoved: Boolean
    ): Boolean {
        if (adsRemoved || !onboardingCompleted) return false
        if (breakPoint !in setOf(NaturalBreakPoint.PRESTIGE, NaturalBreakPoint.ERA_UNLOCK)) return false
        if (nowMillis - state.sessionStartedAtMillis < MIN_SESSION_AGE_MS) return false
        if (state.sessionShows >= MAX_PER_SESSION) return false
        val showsToday = if (state.dayEpoch == currentEpochDay) state.dayShows else 0
        if (showsToday >= MAX_PER_DAY) return false
        if (state.lastShownAtMillis > 0 && nowMillis - state.lastShownAtMillis < MIN_GAP_MS) return false
        return true
    }

    fun recordShow(
        state: InterstitialPolicyState,
        nowMillis: Long,
        currentEpochDay: Long
    ): InterstitialPolicyState {
        val sameDay = state.dayEpoch == currentEpochDay
        return state.copy(
            sessionShows = state.sessionShows + 1,
            lastShownAtMillis = nowMillis,
            dayEpoch = currentEpochDay,
            dayShows = if (sameDay) state.dayShows + 1 else 1
        )
    }
}

class InterstitialFrequencyStore(context: Context) {
    private val prefs = context.getSharedPreferences("zero_empire_ad_frequency", Context.MODE_PRIVATE)
    private val sessionStart = System.currentTimeMillis()
    private var sessionShows = 0

    fun snapshot(): InterstitialPolicyState = InterstitialPolicyState(
        sessionStartedAtMillis = sessionStart,
        sessionShows = sessionShows,
        lastShownAtMillis = prefs.getLong("last_shown", 0L),
        dayEpoch = prefs.getLong("day_epoch", LocalDate.now().toEpochDay()),
        dayShows = prefs.getInt("day_shows", 0)
    )

    fun recordShow(nowMillis: Long = System.currentTimeMillis()) {
        val today = LocalDate.now().toEpochDay()
        val updated = InterstitialPolicy.recordShow(snapshot(), nowMillis, today)
        sessionShows = updated.sessionShows
        prefs.edit()
            .putLong("last_shown", updated.lastShownAtMillis)
            .putLong("day_epoch", updated.dayEpoch)
            .putInt("day_shows", updated.dayShows)
            .apply()
    }
}
```

## File: src/main/java/com/zerotoempire/game/LateGame.kt
```kotlin
package com.zerotoempire.game

import kotlin.math.ln
import kotlin.math.max
import kotlin.math.pow
import kotlin.math.sqrt

/** Long-horizon progression helpers. Pure functions keep balancing testable. */
object LateGame {
    /** Softly accelerates mature empires without creating an unbounded exponential runaway. */
    fun legacyMasteryMultiplier(prestigePoints: Int): Double {
        val p = prestigePoints.coerceAtLeast(0).toDouble()
        return 1.0 + 0.08 * sqrt(p) + 0.015 * ln(1.0 + p).pow(2.0)
    }

    /** Additional production from reaching deep business tiers. */
    fun portfolioDepthMultiplier(businesses: List<Business>): Double {
        val tierScore = businesses.sumOf { b ->
            when {
                b.level >= 1000 -> 5
                b.level >= 500 -> 4
                b.level >= 250 -> 3
                b.level >= 100 -> 2
                b.level >= 50 -> 1
                else -> 0
            }
        }
        return 1.0 + tierScore * 0.035
    }

    /** A recommended prestige becomes attractive at ~25%+ permanent improvement. */
    fun prestigeReadiness(currentPoints: Int, lifetimeCash: Double): Double {
        val current = currentPoints.coerceAtLeast(0)
        val total = Progression.prestigeReward(lifetimeCash)
        val gain = (total.toLong() - current.toLong()).coerceAtLeast(0L)
        if (gain == 0L) return 0.0
        return (gain.toDouble() / max(1, current).toDouble()).coerceAtMost(4.0)
    }

    fun recommendedPrestige(currentPoints: Int, lifetimeCash: Double): Boolean =
        prestigeReadiness(currentPoints, lifetimeCash) >= 0.25 ||
            (currentPoints <= 0 && Progression.prestigeReward(lifetimeCash) >= 1)
}
```

## File: src/main/java/com/zerotoempire/game/LiveOps.kt
```kotlin
package com.zerotoempire.game

import java.time.DayOfWeek
import java.time.LocalDate

data class LiveEvent(
    val id: String,
    val name: String,
    val description: String,
    val incomeMultiplier: Double,
    val icon: String
)

object LiveOps {
    fun currentEvent(date: LocalDate = LocalDate.now()): LiveEvent? = when (date.dayOfWeek) {
        DayOfWeek.FRIDAY -> LiveEvent("friday_rush", "Friday Rush", "Global profits are doubled today.", 2.0, "⚡")
        DayOfWeek.SATURDAY -> LiveEvent("golden_saturday", "Golden Saturday", "Build your empire with +50% production.", 1.5, "✨")
        DayOfWeek.SUNDAY -> LiveEvent("legacy_sunday", "Legacy Sunday", "Prestige runs generate faster progress.", 1.35, "👑")
        else -> null
    }
}

data class DailyQuest(
    val id: String,
    val label: String,
    val target: Int,
    val rewardGems: Int
)

object DailyQuests {
    val quests = listOf(
        DailyQuest("tap_daily", "Make 100 power taps", 100, 5),
        DailyQuest("buy_daily", "Buy 30 business levels", 30, 7),
        DailyQuest("boost_daily", "Activate a profit boost", 1, 8)
    )
}
```

## File: src/main/java/com/zerotoempire/game/MainActivity.kt
```kotlin
package com.zerotoempire.game

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.Build
import android.os.Bundle
import android.os.PowerManager
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent

class MainActivity : ComponentActivity() {
    private lateinit var sfxEngine: PremiumSfxEngine
    private lateinit var musicEngine: AdaptiveMusicEngine
    private var motionPolicyReceiverRegistered = false

    private val motionPolicyReceiver = object : BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            if (intent?.action == PowerManager.ACTION_POWER_SAVE_MODE_CHANGED) {
                MotionQuality.refresh(this@MainActivity)
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        MotionQuality.refresh(this)
        registerMotionPolicyReceiver()

        sfxEngine = PremiumSfxEngine(applicationContext)
        musicEngine = AdaptiveMusicEngine(applicationContext)
        GameSfxBus.attach(sfxEngine)
        GameMusicBus.attach(musicEngine)
        setContent { GrowthRuntimeRoot() }
    }

    override fun onStart() {
        super.onStart()
        GameMusicBus.resume()
    }

    override fun onResume() {
        super.onResume()
        // Re-read animator settings after returning from Android Settings or Developer Options.
        MotionQuality.refresh(this)
    }

    override fun onStop() {
        GameMusicBus.pause()
        super.onStop()
    }

    override fun onDestroy() {
        unregisterMotionPolicyReceiver()
        GameMusicBus.detach(musicEngine)
        GameSfxBus.detach(sfxEngine)
        super.onDestroy()
    }

    private fun registerMotionPolicyReceiver() {
        if (motionPolicyReceiverRegistered) return
        val filter = IntentFilter(PowerManager.ACTION_POWER_SAVE_MODE_CHANGED)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            registerReceiver(motionPolicyReceiver, filter, RECEIVER_NOT_EXPORTED)
        } else {
            @Suppress("DEPRECATION")
            registerReceiver(motionPolicyReceiver, filter)
        }
        motionPolicyReceiverRegistered = true
    }

    private fun unregisterMotionPolicyReceiver() {
        if (!motionPolicyReceiverRegistered) return
        unregisterReceiver(motionPolicyReceiver)
        motionPolicyReceiverRegistered = false
    }
}
```

## File: src/main/java/com/zerotoempire/game/ManagerGroup01Art.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** First executive class: grounded entrepreneurs with strong profession silhouettes. */
@Composable
fun ManagerGroup01Portrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = .18f
    val accent = when (businessId) {
        0 -> Color(0xFF69E08A)
        1 -> Color(0xFF56BFFF)
        2 -> Color(0xFFFFA54D)
        else -> Color(0xFFC28BFF)
    }
    val secondary = when (businessId) {
        0 -> Color(0xFFFFD166)
        1 -> Color(0xFF8CEBFF)
        2 -> Color(0xFFFFD27A)
        else -> Color(0xFF71D8FF)
    }
    val skin = listOf(Color(0xFFB87550), Color(0xFFE5B38B), Color(0xFFF0C39B), Color(0xFF8C593F))[businessId.coerceIn(0,3)]
    val hair = listOf(Color(0xFF1B1720), Color(0xFF493126), Color(0xFF6C452D), Color(0xFF181B22))[businessId.coerceIn(0,3)]

    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.30f), EmpireColors.SurfaceHigh, EmpireColors.Void)), RoundedCornerShape(portraitSize*.31f))) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension; val c = Offset(s*.5f,s*.5f)
            drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.08f),accent.copy(alpha=.12f),Color.Transparent),Offset(s*.42f,s*.31f),s*.43f),s*.47f,c)
            drawCircle(accent.copy(alpha=.62f),s*.425f,c,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.13f),s*.452f,c,style=Stroke(s*.005f))
            drawArc(Color.White.copy(alpha=.20f),205f,70f,false,Offset(s*.09f,s*.09f),Size(s*.82f,s*.82f),style=Stroke(s*.008f))
            drawLine(accent.copy(alpha=.72f),Offset(s*.12f,s*.20f),Offset(s*.12f,s*.32f),s*.010f)
            drawLine(accent.copy(alpha=.72f),Offset(s*.12f,s*.20f),Offset(s*.24f,s*.20f),s*.010f)
            drawLine(secondary.copy(alpha=.48f),Offset(s*.76f,s*.80f),Offset(s*.88f,s*.80f),s*.008f)
            drawCircle(accent.copy(alpha=.9f),s*.012f,Offset(s*.84f,s*.24f))
            val orbiters = if (lowPower) 2 else 4
            repeat(orbiters){i->val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/orbiters;val p=Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f);drawCircle(Color.Black.copy(alpha=.34f),s*.016f,p);drawCircle(if(i%2==0)accent else secondary,s*.009f,p)}
            val torso=Path().apply{moveTo(s*.17f,s*.88f);quadraticTo(s*.25f,s*.59f,s*.5f,s*.57f);quadraticTo(s*.75f,s*.59f,s*.83f,s*.88f);close()}
            val torsoBase=when(businessId){0->Color(0xFF17352A);1->Color(0xFF173047);2->Color(0xFF3A271B);else->Color(0xFF272037)}
            drawPath(torso,Brush.linearGradient(listOf(torsoBase.copy(alpha=.92f),Color(0xFF10141E)),Offset(s*.28f,s*.58f),Offset(s*.72f,s*.86f)))
            drawPath(torso,accent.copy(alpha=.75f),style=Stroke(s*.019f))
            drawLine(Color.White.copy(alpha=.22f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.83f),s*.008f)
            drawLine(secondary.copy(alpha=.22f),Offset(s*.29f,s*.67f),Offset(s*.40f,s*.80f),s*.006f)
            drawRoundRect(skin,Offset(s*.455f,s*.50f),Size(s*.09f,s*.13f))
            drawCircle(accent.copy(alpha=.12f),s*.178f,Offset(s*.5f,s*.365f))
            drawCircle(skin,s*.166f,Offset(s*.5f,s*.365f))
            drawArc(hair,188f,166f,true,Offset(s*.325f,s*.16f),Size(s*.35f,s*.31f))
            drawArc(Color.White.copy(alpha=.11f),205f,72f,false,Offset(s*.35f,s*.215f),Size(s*.30f,s*.29f),style=Stroke(s*.006f))
            drawCircle(EmpireArtPalette.Ink,s*.012f,Offset(s*.445f,s*.365f));drawCircle(EmpireArtPalette.Ink,s*.012f,Offset(s*.555f,s*.365f))
            drawCircle(Color.White.copy(alpha=.68f),s*.004f,Offset(s*.441f,s*.361f));drawCircle(Color.White.copy(alpha=.68f),s*.004f,Offset(s*.551f,s*.361f))
            drawLine(Color(0xFF7A4138),Offset(s*.465f,s*.445f),Offset(s*.535f,s*.445f),s*.009f)
            when(businessId){
                0 -> { val cap=Path().apply{moveTo(s*.34f,s*.245f);quadraticTo(s*.5f,s*.12f,s*.66f,s*.245f);lineTo(s*.62f,s*.275f);lineTo(s*.37f,s*.275f);close()};drawPath(cap,Brush.linearGradient(listOf(Color(0xFF1D5A3C),Color(0xFF10291F)),Offset(s*.4f,s*.14f),Offset(s*.6f,s*.28f)));drawPath(cap,accent,style=Stroke(s*.014f));drawLine(secondary.copy(alpha=.8f),Offset(s*.55f,s*.245f),Offset(s*.70f,s*.275f),s*.018f);drawCircle(EmpireArtPalette.GoldHot,s*.013f,Offset(s*.655f,s*.39f));drawRoundRect(accent.copy(alpha=.18f),Offset(s*.28f,s*.67f),Size(s*.16f,s*.09f));drawRoundRect(accent.copy(alpha=.45f),Offset(s*.28f,s*.67f),Size(s*.16f,s*.09f),style=Stroke(s*.014f));drawLine(secondary.copy(alpha=.65f),Offset(s*.30f,s*.71f),Offset(s*.41f,s*.71f),s*.006f) }
                1 -> { drawLine(accent,Offset(s*.395f,s*.35f),Offset(s*.475f,s*.35f),s*.014f);drawLine(accent,Offset(s*.525f,s*.35f),Offset(s*.605f,s*.35f),s*.014f);drawLine(secondary,Offset(s*.475f,s*.35f),Offset(s*.525f,s*.35f),s*.007f);drawLine(accent,Offset(s*.5f,s*.59f),Offset(s*.47f,s*.76f),s*.022f);drawLine(accent,Offset(s*.5f,s*.59f),Offset(s*.53f,s*.76f),s*.022f);drawRoundRect(accent.copy(alpha=.15f),Offset(s*.62f,s*.65f),Size(s*.10f,s*.07f));drawRoundRect(secondary.copy(alpha=.55f),Offset(s*.62f,s*.65f),Size(s*.10f,s*.07f),style=Stroke(s*.010f));drawCircle(Color.White.copy(alpha=.75f),s*.006f,Offset(s*.67f,s*.685f)) }
                2 -> { drawArc(accent,190f,160f,false,Offset(s*.345f,s*.30f),Size(s*.31f,s*.13f),style=Stroke(s*.020f));drawArc(secondary.copy(alpha=.48f),200f,140f,false,Offset(s*.36f,s*.315f),Size(s*.28f,s*.10f),style=Stroke(s*.006f));drawCircle(Color.White.copy(alpha=.78f),s*.010f,Offset(s*.43f,s*.355f));drawCircle(Color.White.copy(alpha=.78f),s*.010f,Offset(s*.57f,s*.355f));drawLine(accent,Offset(s*.32f,s*.61f),Offset(s*.43f,s*.73f),s*.018f);drawLine(accent,Offset(s*.68f,s*.61f),Offset(s*.57f,s*.73f),s*.018f);drawCircle(accent.copy(alpha=.20f),s*.052f,Offset(s*.67f,s*.70f));drawCircle(EmpireArtPalette.GoldHot,s*.020f,Offset(s*.67f,s*.70f)) }
                else -> { val helmet=Path().apply{moveTo(s*.34f,s*.26f);quadraticTo(s*.38f,s*.14f,s*.5f,s*.14f);quadraticTo(s*.62f,s*.14f,s*.66f,s*.26f);lineTo(s*.69f,s*.28f);lineTo(s*.31f,s*.28f);close()};drawPath(helmet,Brush.linearGradient(listOf(Color(0xFF44345C),Color(0xFF211A2C)),Offset(s*.4f,s*.14f),Offset(s*.6f,s*.28f)));drawPath(helmet,accent,style=Stroke(s*.016f));drawLine(EmpireArtPalette.GoldHot,Offset(s*.5f,s*.145f),Offset(s*.5f,s*.265f),s*.016f);drawLine(secondary.copy(alpha=.55f),Offset(s*.38f,s*.225f),Offset(s*.62f,s*.225f),s*.006f);drawRoundRect(accent.copy(alpha=.16f),Offset(s*.61f,s*.65f),Size(s*.11f,s*.10f));drawRoundRect(accent.copy(alpha=.48f),Offset(s*.61f,s*.65f),Size(s*.11f,s*.10f),style=Stroke(s*.014f));repeat(3){i->drawCircle(Color.White.copy(alpha=.72f),s*.007f,Offset(s*(.635f+i*.03f),s*.70f))} }
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/ManagerGroup02Art.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.*
import androidx.compose.ui.graphics.*
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.*

/** Expansion class: tech, city, lunar and Mars executives. */
@Composable
fun ManagerGroup02Portrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = .27f
    val id=businessId.coerceIn(4,7)
    val accent=when(id){4->Color(0xFF43E6FF);5->Color(0xFF4FA8FF);6->Color(0xFFEAF6FF);else->Color(0xFFFF654F)}
    val secondary=when(id){4->Color(0xFF8CFFDC);5->Color(0xFF6FE3FF);6->Color(0xFF78DFFF);else->Color(0xFFFFB34D)}
    val skin=when(id){4->Color(0xFFD49A74);5->Color(0xFF9C664A);6->Color(0xFFF0C7A3);else->Color(0xFFB87854)}
    val hair=when(id){4->Color(0xFF151A28);5->Color(0xFF303744);6->Color(0xFFD8DCE5);else->Color(0xFF3D2018)}
    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.27f),EmpireColors.SurfaceHigh,EmpireColors.Void)),RoundedCornerShape(portraitSize*.31f))){
        Canvas(Modifier.fillMaxSize()){
            val s=size.minDimension;val c=Offset(s*.5f,s*.5f)
            drawCircle(Brush.radialGradient(listOf(Color.White.copy(alpha=.08f),accent.copy(alpha=.11f),Color.Transparent),Offset(s*.42f,s*.30f),s*.45f),s*.47f,c)
            drawCircle(accent.copy(alpha=.63f),s*.425f,c,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.16f),s*.455f,c,style=Stroke(s*.006f))
            drawArc(Color.White.copy(alpha=.20f),205f,72f,false,Offset(s*.085f,s*.085f),Size(s*.83f,s*.83f),style=Stroke(s*.007f))
            val nodeCount=if(lowPower)2 else 5
            repeat(nodeCount){i->val a=phase*2*PI.toFloat()+i*2*PI.toFloat()/nodeCount;val p=Offset(c.x+cos(a)*s*.395f,c.y+sin(a)*s*.395f);drawCircle(Color.Black.copy(alpha=.34f),s*.015f,p);drawCircle(if(i%2==0)accent else secondary,s*.009f,p)}
            val torso=Path().apply{moveTo(s*.16f,s*.88f);quadraticTo(s*.23f,s*.59f,s*.5f,s*.56f);quadraticTo(s*.77f,s*.59f,s*.84f,s*.88f);close()}
            val torsoBase=when(id){4->Color(0xFF102A3D);5->Color(0xFF172C45);6->Color(0xFFCBD7E2);else->Color(0xFF3A1D1A)}
            drawPath(torso,Brush.linearGradient(listOf(torsoBase,Color(0xFF10141D)),Offset(s*.28f,s*.58f),Offset(s*.72f,s*.86f)))
            drawPath(torso,accent.copy(alpha=.76f),style=Stroke(s*.019f))
            drawLine(Color.White.copy(alpha=.20f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.82f),s*.008f)
            drawLine(secondary.copy(alpha=.25f),Offset(s*.29f,s*.67f),Offset(s*.40f,s*.80f),s*.006f)
            drawRoundRect(skin,Offset(s*.455f,s*.49f),Size(s*.09f,s*.14f))
            drawCircle(accent.copy(alpha=.11f),s*.177f,Offset(s*.5f,s*.36f))
            drawCircle(skin,s*.164f,Offset(s*.5f,s*.36f))
            drawArc(hair,188f,166f,true,Offset(s*.325f,s*.155f),Size(s*.35f,s*.31f))
            drawArc(Color.White.copy(alpha=.10f),205f,72f,false,Offset(s*.35f,s*.21f),Size(s*.30f,s*.29f),style=Stroke(s*.006f))
            drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.445f,s*.36f));drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.555f,s*.36f))
            drawCircle(Color.White.copy(alpha=.70f),s*.004f,Offset(s*.441f,s*.356f));drawCircle(Color.White.copy(alpha=.70f),s*.004f,Offset(s*.551f,s*.356f))
            drawLine(Color(0xFF75413A),Offset(s*.466f,s*.438f),Offset(s*.534f,s*.438f),s*.008f)
            when(id){
                4->{ drawLine(accent,Offset(s*.39f,s*.345f),Offset(s*.48f,s*.345f),s*.013f);drawLine(accent,Offset(s*.52f,s*.345f),Offset(s*.61f,s*.345f),s*.013f);drawLine(secondary,Offset(s*.48f,s*.345f),Offset(s*.52f,s*.345f),s*.007f);drawRoundRect(accent.copy(alpha=.13f),Offset(s*.24f,s*.63f),Size(s*.22f,s*.13f),CornerRadius(s*.018f));drawRoundRect(accent.copy(alpha=.86f),Offset(s*.24f,s*.63f),Size(s*.22f,s*.13f),CornerRadius(s*.018f),style=Stroke(s*.010f));drawLine(Color.White.copy(alpha=.78f),Offset(s*.27f,s*.69f),Offset(s*.42f,s*.69f),s*.007f);drawCircle(secondary.copy(alpha=.8f),s*.008f,Offset(s*.405f,s*.655f)) }
                5->{ drawLine(accent,Offset(s*.29f,s*.64f),Offset(s*.42f,s*.77f),s*.015f);drawLine(secondary,Offset(s*.42f,s*.77f),Offset(s*.52f,s*.64f),s*.015f);drawRect(accent.copy(alpha=.20f),Offset(s*.60f,s*.62f),Size(s*.12f,s*.15f));drawRect(secondary.copy(alpha=.38f),Offset(s*.60f,s*.62f),Size(s*.12f,s*.15f),style=Stroke(s*.009f));repeat(3){i->drawLine(Color.White.copy(alpha=.62f),Offset(s*(.62f+i*.035f),s*.65f),Offset(s*(.62f+i*.035f),s*.74f),s*.006f)} }
                6->{ drawArc(accent,190f,160f,false,Offset(s*.31f,s*.23f),Size(s*.38f,s*.29f),style=Stroke(s*.018f));drawCircle(secondary.copy(alpha=.14f),s*.205f,Offset(s*.5f,s*.36f),style=Stroke(s*.009f));drawCircle(EmpireArtPalette.Cyan,s*.022f,Offset(s*.67f,s*.69f));drawCircle(secondary.copy(alpha=.22f),s*.052f,Offset(s*.67f,s*.69f));drawLine(EmpireArtPalette.Cyan,Offset(s*.60f,s*.69f),Offset(s*.73f,s*.69f),s*.009f) }
                else->{ drawLine(accent,Offset(s*.31f,s*.61f),Offset(s*.42f,s*.76f),s*.022f);drawLine(secondary,Offset(s*.69f,s*.61f),Offset(s*.58f,s*.76f),s*.022f);drawCircle(accent.copy(alpha=.18f),s*.052f,Offset(s*.5f,s*.68f));drawCircle(EmpireArtPalette.GoldHot,s*.022f,Offset(s*.5f,s*.68f));drawCircle(accent.copy(alpha=.30f),s*.055f,Offset(s*.68f,s*.69f),style=Stroke(s*.013f));drawLine(secondary,Offset(s*.65f,s*.69f),Offset(s*.71f,s*.69f),s*.008f) }
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/ManagerGroup03Art.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/** Megastructure executives: stellar engineering and galactic finance. */
@Composable
fun ManagerGroup03Portrait(businessId: Int, portraitSize: Dp) {
    val context = LocalContext.current
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = .32f
    val sol = businessId == 8
    val accent = if (sol) Color(0xFFFFD75E) else Color(0xFFB86CFF)
    val secondary = if (sol) Color(0xFFFF8E46) else Color(0xFF55D9FF)
    val skin = if (sol) Color(0xFFD5A077) else Color(0xFFB57A59)
    val hair = if (sol) Color(0xFFE4D8C5) else Color(0xFF171A23)

    Box(Modifier.size(portraitSize).background(Brush.radialGradient(listOf(accent.copy(alpha=.29f), EmpireColors.SurfaceHigh, EmpireColors.Void)), RoundedCornerShape(portraitSize*.31f))) {
        Canvas(Modifier.fillMaxSize()) {
            val s=size.minDimension
            val c=Offset(s*.5f,s*.5f)

            // Cinematic lens depth stays completely static; the existing portrait path remains cheap in lists.
            drawCircle(
                Brush.radialGradient(
                    listOf(Color.White.copy(alpha=.10f), accent.copy(alpha=.10f), secondary.copy(alpha=.045f), Color.Transparent),
                    center = Offset(s*.42f,s*.29f),
                    radius = s*.49f
                ),
                s*.47f,
                c
            )
            drawCircle(accent.copy(alpha=.66f),s*.425f,c,style=Stroke(s*.017f))
            drawCircle(secondary.copy(alpha=.24f),s*.455f,c,style=Stroke(s*.007f))
            drawArc(Color.White.copy(alpha=.22f),205f,70f,false,Offset(s*.08f,s*.08f),Size(s*.84f,s*.84f),style=Stroke(s*.007f))
            drawArc(secondary.copy(alpha=.24f),18f,100f,false,Offset(s*.105f,s*.105f),Size(s*.79f,s*.79f),style=Stroke(s*.005f))

            val nodes=if(lowPower)3 else 7
            repeat(nodes){i->
                val a=phase*2f*PI.toFloat()+i*2f*PI.toFloat()/nodes
                val p=Offset(c.x+cos(a)*s*.39f,c.y+sin(a)*s*.39f)
                drawCircle(Color.Black.copy(alpha=.42f),s*.016f,p)
                drawCircle(if(i%2==0)accent else secondary,s*.009f,p)
            }

            val torso=Path().apply{moveTo(s*.15f,s*.88f);quadraticTo(s*.23f,s*.58f,s*.5f,s*.56f);quadraticTo(s*.77f,s*.58f,s*.85f,s*.88f);close()}
            drawPath(
                torso,
                Brush.linearGradient(
                    if(sol) listOf(Color(0xFF4A3816),Color(0xFF211B12)) else listOf(Color(0xFF38214B),Color(0xFF181222)),
                    Offset(s*.26f,s*.58f),
                    Offset(s*.74f,s*.88f)
                )
            )
            drawPath(torso,accent.copy(alpha=.82f),style=Stroke(s*.019f))
            drawLine(Color.White.copy(alpha=.18f),Offset(s*.5f,s*.59f),Offset(s*.5f,s*.83f),s*.007f)
            drawLine(secondary.copy(alpha=.28f),Offset(s*.30f,s*.67f),Offset(s*.41f,s*.80f),s*.006f)

            drawRoundRect(skin,Offset(s*.455f,s*.49f),Size(s*.09f,s*.14f))
            drawCircle(accent.copy(alpha=.14f),s*.176f,Offset(s*.5f,s*.36f))
            drawCircle(skin,s*.165f,Offset(s*.5f,s*.36f))
            drawArc(hair,188f,166f,true,Offset(s*.325f,s*.155f),Size(s*.35f,s*.31f))
            drawArc(Color.White.copy(alpha=.13f),205f,74f,false,Offset(s*.35f,s*.205f),Size(s*.30f,s*.29f),style=Stroke(s*.006f))
            drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.445f,s*.36f));drawCircle(EmpireArtPalette.Ink,s*.011f,Offset(s*.555f,s*.36f))
            drawCircle(Color.White.copy(alpha=.70f),s*.004f,Offset(s*.442f,s*.357f));drawCircle(Color.White.copy(alpha=.70f),s*.004f,Offset(s*.552f,s*.357f))
            drawLine(Color(0xFF75413A),Offset(s*.466f,s*.438f),Offset(s*.534f,s*.438f),s*.008f)

            if(sol){
                drawArc(accent,205f,130f,false,Offset(s*.31f,s*.17f),Size(s*.38f,s*.22f),style=Stroke(s*.018f))
                drawArc(secondary.copy(alpha=.42f),212f,112f,false,Offset(s*.335f,s*.195f),Size(s*.33f,s*.17f),style=Stroke(s*.006f))
                repeat(5){i->val a=(-.48f+i*.24f)*PI.toFloat();drawLine(accent.copy(alpha=.78f),Offset(s*.5f+cos(a)*s*.17f,s*.25f+sin(a)*s*.06f),Offset(s*.5f+cos(a)*s*.24f,s*.18f+sin(a)*s*.09f),s*.010f)}
                val core=Offset(s*.66f,s*.69f)
                drawCircle(secondary.copy(alpha=.18f),s*.080f,core)
                drawCircle(EmpireArtPalette.GoldHot,s*.025f,core)
                drawCircle(accent.copy(alpha=.60f),s*.064f,core,style=Stroke(s*.012f))
                repeat(4){i->val a=i*PI.toFloat()/2f+phase;drawLine(accent,Offset(core.x+cos(a)*s*.045f,core.y+sin(a)*s*.045f),Offset(core.x+cos(a)*s*.085f,core.y+sin(a)*s*.085f),s*.008f)}
                if(!lowPower){
                    repeat(3){i->drawCircle(Color.White.copy(alpha=.70f),s*.006f,Offset(s*(.28f+i*.055f),s*.615f))}
                }
            }else{
                drawLine(accent,Offset(s*.39f,s*.345f),Offset(s*.48f,s*.345f),s*.013f);drawLine(accent,Offset(s*.52f,s*.345f),Offset(s*.61f,s*.345f),s*.013f);drawLine(secondary,Offset(s*.48f,s*.345f),Offset(s*.52f,s*.345f),s*.007f)
                drawLine(Color.White.copy(alpha=.20f),Offset(s*.40f,s*.327f),Offset(s*.47f,s*.327f),s*.004f)
                val graph=Path().apply{moveTo(s*.25f,s*.74f);lineTo(s*.32f,s*.69f);lineTo(s*.39f,s*.72f);lineTo(s*.47f,s*.63f)}
                drawPath(graph,secondary,style=Stroke(s*.014f))
                drawPath(graph,Color.White.copy(alpha=.16f),style=Stroke(s*.004f))
                drawArc(accent.copy(alpha=.72f),190f,160f,false,Offset(s*.57f,s*.62f),Size(s*.17f,s*.12f),style=Stroke(s*.012f))
                drawCircle(secondary.copy(alpha=.20f),s*.032f,Offset(s*.655f,s*.68f))
                drawCircle(Color.White.copy(alpha=.84f),s*.010f,Offset(s*.655f,s*.68f))
                if(!lowPower){
                    repeat(3){i->drawLine(accent.copy(alpha=.40f),Offset(s*(.58f+i*.045f),s*.77f),Offset(s*(.60f+i*.045f),s*.73f),s*.005f)}
                }
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/Managers.kt
```kotlin
package com.zerotoempire.game

data class Manager(
    val businessId: Int,
    val name: String,
    val title: String,
    val cost: Double,
    val incomeMultiplier: Double = 1.0,
    val hired: Boolean = false
)

object Managers {
    val catalog = listOf(
        Manager(0, "Maya", "Street Hustler", 2_500.0, 1.15),
        Manager(1, "Noah", "Retail Operator", 35_000.0, 1.20),
        Manager(2, "Ava", "Production Chief", 500_000.0, 1.25),
        Manager(3, "Leo", "Factory Director", 8_000_000.0, 1.30),
        Manager(4, "Nova", "Tech Visionary", 180_000_000.0, 1.40),
        Manager(5, "Atlas", "City Architect", 5_000_000_000.0, 1.50),
        Manager(6, "Luna", "Lunar Governor", 300_000_000_000.0, 1.65),
        Manager(7, "Ares", "Martian Chancellor", 25_000_000_000_000.0, 1.80),
        Manager(8, "Sol", "Stellar Engineer", 3.0e15, 2.0),
        Manager(9, "Orion", "Galactic Broker", 4.0e17, 2.25),
        Manager(10, "Vega", "Intergalactic Navigator", 1.2e20, 2.55),
        Manager(11, "Lyra", "Cosmic Fabricator", 5.0e23, 2.90),
        Manager(12, "Axiom", "Reality Systems Architect", 2.0e27, 3.35),
        Manager(13, "Zenith", "Transcendence Director", 8.0e30, 4.00)
    )
}

data class Upgrade(
    val id: String,
    val name: String,
    val description: String,
    val gemCost: Int,
    val maxRank: Int,
    val rank: Int = 0
)

object Upgrades {
    val catalog = listOf(
        Upgrade("tap", "Golden Touch", "+25% tap value per rank", 15, 10),
        Upgrade("income", "Compound Engine", "+10% global income per rank", 25, 20),
        Upgrade("offline", "Deep Automation", "+1 hour offline cap per rank", 20, 8),
        Upgrade("prestige", "Legacy Network", "+8% prestige power per rank", 35, 15)
    )
}
```

## File: src/main/java/com/zerotoempire/game/MasteryCrownShimmer.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val CrownFrameSize = 128
private const val CrownColumns = 4
private const val CrownFrameCount = 8

/** Raster mastery accent. Reduced-motion and battery-saver users receive frame zero. */
@Composable
internal fun MasteryCrownShimmer(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_17_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) {
            while (true) {
                delay(125)
                frame = (frame + 1) % CrownFrameCount
            }
        }
    }

    Canvas(modifier) {
        val crownSize = size.minDimension * .31f
        val destination = Offset(
            x = (size.width - crownSize) * .5f,
            y = size.height * .015f
        )
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % CrownColumns) * CrownFrameSize,
                y = (frame / CrownColumns) * CrownFrameSize
            ),
            srcSize = IntSize(CrownFrameSize, CrownFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(crownSize.toInt(), crownSize.toInt()),
            alpha = .96f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/MetaSpriteArt.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

enum class MetaSpriteKind { CASH, GEM, LEGACY, DAILY, MISSION, ACHIEVEMENT, BOOST, EVENT, LOCK, STORE, SHARE }

@Composable
fun MetaSprite(kind: MetaSpriteKind, size: Dp = 42.dp, active: Boolean = true, progress: Float = 1f) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    // Orbiting pixels are not legible on compact navigation/action icons. Keeping those sprites
    // static removes several always-on transitions, while large reward/status badges retain motion.
    val shouldAnimate = !reduced && !lowPower && active && size >= 32.dp &&
        kind != MetaSpriteKind.LOCK && kind != MetaSpriteKind.CASH
    val phase = if (shouldAnimate) {
        val t = rememberInfiniteTransition(label = "meta-$kind")
        val phaseAnim by t.animateFloat(
            0f,
            1f,
            infiniteRepeatable(tween(if (lowPower) 12000 else 7000, easing = LinearEasing)),
            label = "phase"
        )
        phaseAnim
    } else .18f

    val accent = when (kind) {
        MetaSpriteKind.CASH -> Color(0xFF6EEB8B)
        MetaSpriteKind.GEM -> Color(0xFFC68BFF)
        MetaSpriteKind.LEGACY -> Color(0xFFFFD66B)
        MetaSpriteKind.DAILY -> Color(0xFFFFC857)
        MetaSpriteKind.MISSION -> Color(0xFF57E7F2)
        MetaSpriteKind.ACHIEVEMENT -> Color(0xFFFFE36E)
        MetaSpriteKind.BOOST -> Color(0xFFFF8C5A)
        MetaSpriteKind.EVENT -> Color(0xFFFF68D8)
        MetaSpriteKind.LOCK -> Color(0xFF7C8799)
        MetaSpriteKind.STORE -> Color(0xFF62B4FF)
        MetaSpriteKind.SHARE -> Color(0xFF8BE0FF)
    }
    Canvas(Modifier.size(size)) {
        val s = this.size.minDimension
        val c = Offset(s * .5f, s * .5f)
        val alpha = if (active) 1f else .45f
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha = .24f * alpha), Color.Transparent), c, s * .5f), s * .5f, c)
        drawCircle(EmpireColors.SurfaceHigh.copy(alpha = .96f), s * .39f, c)
        drawCircle(accent.copy(alpha = .80f * alpha), s * .39f, c, style = Stroke(s * .035f))
        drawMetaGlyph(kind, c, s, accent.copy(alpha = alpha), progress.coerceIn(0f, 1f))
        if (shouldAnimate) {
            val count = if (lowPower) 2 else 4
            repeat(count) { i ->
                val a = phase * 2f * PI.toFloat() + i * 2f * PI.toFloat() / count
                drawCircle(Color.White.copy(alpha = .72f), s * .018f, Offset(c.x + cos(a) * s * .44f, c.y + sin(a) * s * .44f))
            }
        }
    }
}

private fun DrawScope.drawMetaGlyph(kind: MetaSpriteKind, c: Offset, s: Float, accent: Color, progress: Float) {
    when (kind) {
        MetaSpriteKind.CASH -> {
            drawRoundRect(accent.copy(alpha=.22f), Offset(s*.28f,s*.34f), Size(s*.44f,s*.31f))
            drawRoundRect(accent, Offset(s*.28f,s*.34f), Size(s*.44f,s*.31f), style=Stroke(s*.025f))
            drawCircle(accent,s*.055f,c)
            drawLine(Color.White,Offset(s*.47f,s*.43f),Offset(s*.54f,s*.43f),s*.018f)
            drawLine(Color.White,Offset(s*.46f,s*.57f),Offset(s*.53f,s*.57f),s*.018f)
        }
        MetaSpriteKind.GEM -> {
            val p=Path().apply{moveTo(c.x,s*.24f);lineTo(s*.72f,s*.42f);lineTo(s*.62f,s*.72f);lineTo(s*.38f,s*.72f);lineTo(s*.28f,s*.42f);close()}
            drawPath(p,Brush.verticalGradient(listOf(Color.White,accent,accent.copy(alpha=.45f))))
            drawLine(Color.White.copy(alpha=.7f),Offset(c.x,s*.25f),Offset(c.x,s*.69f),s*.014f)
            drawLine(Color.White.copy(alpha=.45f),Offset(s*.29f,s*.42f),Offset(s*.71f,s*.42f),s*.012f)
        }
        MetaSpriteKind.LEGACY -> {
            drawCircle(accent.copy(alpha=.22f),s*.22f,c)
            drawCircle(accent,s*.20f,c,style=Stroke(s*.032f))
            repeat(6){i->val a=i*PI.toFloat()/3f;drawLine(color=accent,start=Offset(c.x+cos(a)*s*.11f,c.y+sin(a)*s*.11f),end=Offset(c.x+cos(a)*s*.27f,c.y+sin(a)*s*.27f),strokeWidth=s*.026f)}
            drawCircle(Color.White,s*.055f,c)
        }
        MetaSpriteKind.DAILY -> {
            drawRoundRect(accent.copy(alpha=.16f),Offset(s*.28f,s*.28f),Size(s*.44f,s*.44f))
            drawRoundRect(accent,Offset(s*.28f,s*.28f),Size(s*.44f,s*.44f),style=Stroke(s*.025f))
            drawLine(accent,Offset(s*.28f,s*.40f),Offset(s*.72f,s*.40f),s*.02f)
            drawCircle(Color.White,s*.06f,Offset(c.x,s*.56f))
        }
        MetaSpriteKind.MISSION -> {
            val p=Path().apply{moveTo(s*.30f,s*.66f);lineTo(s*.30f,s*.31f);lineTo(s*.68f,s*.31f);lineTo(s*.68f,s*.66f);close()}
            drawPath(p,accent.copy(alpha=.18f));drawPath(p,accent,style=Stroke(s*.024f))
            drawLine(accent,Offset(s*.37f,s*.43f),Offset(s*.61f,s*.43f),s*.017f)
            drawLine(accent,Offset(s*.37f,s*.53f),Offset(s*(.37f+.24f*progress),s*.53f),s*.017f)
        }
        MetaSpriteKind.ACHIEVEMENT -> {
            val star=Path().apply{for(i in 0 until 10){val a=-PI/2+i*PI/5;val r=if(i%2==0)s*.24 else s*.105;val x=c.x+(cos(a)*r).toFloat();val y=c.y+(sin(a)*r).toFloat();if(i==0)moveTo(x,y)else lineTo(x,y)};close()}
            drawPath(star,Brush.radialGradient(listOf(Color.White,accent),c,s*.28f))
        }
        MetaSpriteKind.BOOST -> {
            val bolt=Path().apply{moveTo(s*.53f,s*.22f);lineTo(s*.34f,s*.51f);lineTo(s*.48f,s*.51f);lineTo(s*.41f,s*.78f);lineTo(s*.68f,s*.43f);lineTo(s*.54f,s*.43f);close()}
            drawPath(bolt,accent);drawPath(bolt,Color.White.copy(alpha=.5f),style=Stroke(s*.012f))
        }
        MetaSpriteKind.EVENT -> {
            drawCircle(accent.copy(alpha=.18f),s*.23f,c)
            repeat(8){i->val a=i*PI.toFloat()/4f;drawLine(color=accent,start=Offset(c.x+cos(a)*s*.14f,c.y+sin(a)*s*.14f),end=Offset(c.x+cos(a)*s*.29f,c.y+sin(a)*s*.29f),strokeWidth=s*.018f)}
            drawCircle(Color.White,s*.055f,c)
        }
        MetaSpriteKind.LOCK -> {
            drawRoundRect(accent.copy(alpha=.20f),Offset(s*.31f,s*.43f),Size(s*.38f,s*.31f))
            drawRoundRect(accent,Offset(s*.31f,s*.43f),Size(s*.38f,s*.31f),style=Stroke(s*.025f))
            drawArc(accent,195f,150f,false,Offset(s*.37f,s*.25f),Size(s*.26f,s*.30f),style=Stroke(s*.035f))
            drawCircle(Color.White.copy(alpha=.8f),s*.028f,Offset(c.x,s*.58f))
        }
        MetaSpriteKind.STORE -> {
            drawRoundRect(accent.copy(alpha=.18f),Offset(s*.27f,s*.38f),Size(s*.46f,s*.34f))
            drawRoundRect(accent,Offset(s*.27f,s*.38f),Size(s*.46f,s*.34f),style=Stroke(s*.025f))
            drawArc(accent,200f,140f,false,Offset(s*.37f,s*.25f),Size(s*.26f,s*.27f),style=Stroke(s*.025f))
            drawCircle(Color.White,s*.035f,Offset(c.x,s*.55f))
        }
        MetaSpriteKind.SHARE -> {
            val pts=listOf(Offset(s*.34f,s*.50f),Offset(s*.64f,s*.32f),Offset(s*.64f,s*.68f))
            drawLine(accent,pts[0],pts[1],s*.023f);drawLine(accent,pts[0],pts[2],s*.023f)
            pts.forEach{drawCircle(accent,s*.065f,it);drawCircle(Color.White.copy(alpha=.75f),s*.024f,it)}
        }
    }
}

@Composable
fun NavSprite(tab: GameTab, selected: Boolean, size: Dp = 26.dp) {
    val kind = when (tab) {
        GameTab.EMPIRE -> MetaSpriteKind.LEGACY
        GameTab.MANAGERS -> MetaSpriteKind.MISSION
        GameTab.UPGRADES -> MetaSpriteKind.GEM
        GameTab.GOALS -> MetaSpriteKind.ACHIEVEMENT
    }
    MetaSprite(kind, size, active = selected)
}
```

## File: src/main/java/com/zerotoempire/game/Monetization.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity

/** Provider-neutral contracts: gameplay code never talks directly to billing or ad SDKs. */
interface RewardedAdGateway {
    /**
     * Lets privacy-aware hosts disable ad work immediately. The default keeps test/fake
     * implementations source-compatible while production gateways can actively invalidate loads.
     */
    fun setEnabled(enabled: Boolean) {}
    fun preload()
    fun isReady(): Boolean
    fun show(activity: Activity, placement: RewardPlacement, onReward: () -> Unit, onClosed: () -> Unit = {})
}

enum class RewardPlacement {
    DOUBLE_OFFLINE_EARNINGS,
    PROFIT_BOOST,
    DAILY_BONUS,
    EVENT_BONUS
}

interface PurchaseGateway {
    fun connect()
    fun disconnect()
    fun purchase(activity: Activity, product: StoreProduct, onResult: (PurchaseResult) -> Unit)
    /**
     * Returns every recovered transaction. This is intentionally a List rather than a Set:
     * multiple interrupted purchases of the same consumable must each be credited exactly once.
     */
    fun restore(onResult: (RestoreResult) -> Unit)
}

enum class StoreProduct(val productId: String, val consumable: Boolean) {
    REMOVE_ADS("remove_ads_lifetime", false),
    STARTER_PACK("starter_pack", false),
    GEM_PACK_SMALL("gems_small", true),
    GEM_PACK_MEDIUM("gems_medium", true)
}

/** A one-time Google Play transaction is accepted only when it identifies one exact catalog SKU. */
object StoreProductResolver {
    fun resolve(productIds: List<String>): StoreProduct? {
        val productId = productIds.distinct().singleOrNull() ?: return null
        return StoreProduct.entries.singleOrNull { it.productId == productId }
    }
}

sealed interface PurchaseResult {
    data class Success(val product: StoreProduct, val transactionId: String) : PurchaseResult
    data object Cancelled : PurchaseResult
    data object Pending : PurchaseResult
    data class Failed(val reason: String) : PurchaseResult
}

sealed interface RestoreResult {
    val products: List<StoreProduct>
    val pendingProducts: Set<StoreProduct>

    data class Success(
        override val products: List<StoreProduct>,
        override val pendingProducts: Set<StoreProduct> = emptySet()
    ) : RestoreResult
    data class Failed(
        val reason: String,
        override val products: List<StoreProduct> = emptyList(),
        override val pendingProducts: Set<StoreProduct> = emptySet()
    ) : RestoreResult
}

data class MonetizationState(
    val adsRemoved: Boolean = false,
    val starterPackOwned: Boolean = false,
    val billingReady: Boolean = false,
    val rewardedReady: Boolean = false
)
```

## File: src/main/java/com/zerotoempire/game/MotionQuality.kt
```kotlin
package com.zerotoempire.game

import android.animation.ValueAnimator
import android.content.Context
import android.os.PowerManager
import androidx.compose.runtime.mutableStateOf

/** Central policy for animation density and accessibility-aware visual load. */
object MotionQuality {
    /*
     * Snapshot-backed system state lets existing composables that call this policy recompose when
     * Android's power/animation settings change, without threading a new flag through the UI tree.
     */
    private val animationsEnabledState = mutableStateOf<Boolean?>(null)
    private val lowPowerModeState = mutableStateOf<Boolean?>(null)

    fun refresh(context: Context) {
        animationsEnabledState.value = ValueAnimator.areAnimatorsEnabled()
        lowPowerModeState.value = queryLowPowerMode(context)
    }

    fun animationsEnabled(context: Context): Boolean =
        animationsEnabledState.value ?: ValueAnimator.areAnimatorsEnabled()

    fun lowPowerMode(context: Context): Boolean =
        lowPowerModeState.value ?: queryLowPowerMode(context)

    private fun queryLowPowerMode(context: Context): Boolean {
        val power = context.getSystemService(Context.POWER_SERVICE) as? PowerManager
        return power?.isPowerSaveMode == true
    }

    /**
     * Decorative motion is disabled when Android animations are disabled or Battery Saver is active.
     * This keeps low-power mode genuinely static instead of running the same infinite transitions slower.
     */
    fun reducedMotion(context: Context): Boolean = !animationsEnabled(context) || lowPowerMode(context)

    fun particleBudget(context: Context, requested: Int): Int = when {
        reducedMotion(context) -> 0
        else -> requested
    }

    fun animationDuration(context: Context, millis: Int): Int = when {
        reducedMotion(context) -> 1
        else -> millis
    }
}
```

## File: src/main/java/com/zerotoempire/game/OfflineProgress.kt
```kotlin
package com.zerotoempire.game

import java.time.Instant
import java.time.ZoneId
import kotlin.math.min

data class OfflineReward(val elapsedSeconds:Long,val paidSeconds:Long,val cash:Double) {
    val eligible:Boolean get()=cash>0.0 && paidSeconds>=30
}

object OfflineProgress {
    fun calculate(
        state: GameState,
        lastSeenMillis: Long,
        nowMillis: Long = System.currentTimeMillis(),
        zoneId: ZoneId = ZoneId.systemDefault()
    ): OfflineReward {
        if (lastSeenMillis <= 0 || nowMillis <= lastSeenMillis) return OfflineReward(0,0,0.0)
        val elapsed = ((nowMillis-lastSeenMillis)/1000L).coerceAtLeast(0)
        val extraHours = (state.upgradeRanks["offline"] ?: 0).coerceIn(0,8)
        val capSeconds = (8L+extraHours)*3600L
        val paid = min(elapsed,capSeconds)
        if (paid <= 0 || state.automatedBaseIncomePerSecond <= 0.0) return OfflineReward(elapsed,paid,0.0)

        val paidEndMillis = lastSeenMillis + paid * 1000L
        var cursor = lastSeenMillis
        var cash = 0.0

        // Integrate only across boundaries that can change the multiplier: local midnight and boost expiry.
        while (cursor < paidEndMillis) {
            val zoned = Instant.ofEpochMilli(cursor).atZone(zoneId)
            val date = zoned.toLocalDate()
            val nextMidnight = date.plusDays(1).atStartOfDay(zoneId).toInstant().toEpochMilli()
            var segmentEnd = min(paidEndMillis, nextMidnight)
            if (state.boostEndsAtMillis > cursor && state.boostEndsAtMillis < segmentEnd) {
                segmentEnd = state.boostEndsAtMillis
            }
            if (segmentEnd <= cursor) segmentEnd = min(paidEndMillis, cursor + 1000L)

            val seconds = (segmentEnd - cursor) / 1000.0
            val boost = if (cursor < state.boostEndsAtMillis) 2.0 else 1.0
            val event = LiveOps.currentEvent(date)?.incomeMultiplier ?: 1.0
            val segmentCash = EconomyMath.finite(state.automatedBaseIncomePerSecond * boost * event * seconds * .75)
            cash = EconomyMath.safeAdd(cash, segmentCash)
            cursor = segmentEnd
        }

        return OfflineReward(elapsed,paid,EconomyMath.finite(cash))
    }
}
```

## File: src/main/java/com/zerotoempire/game/OnboardingArt.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun OnboardingStepArt(step: Int) {
    if (step.coerceIn(0, 4) == 0) {
        Image(
            painter = painterResource(R.drawable.zte_onboarding_00_final),
            contentDescription = null,
            modifier = Modifier.size(220.dp),
            contentScale = ContentScale.Fit,
        )
        return
    }
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase: Float
    if (reduced) {
        phase = .2f
    } else {
        val transition = rememberInfiniteTransition(label = "onboarding-art")
        val phaseAnim by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(if (lowPower) 12000 else 7000, easing = LinearEasing)), label = "phase")
        phase = phaseAnim
    }
    Canvas(Modifier.size(220.dp)) {
        val s = size.minDimension
        val c = Offset(s * .5f, s * .5f)
        val accents = listOf(EmpireColors.Gold, EmpireColors.Cyan, Color(0xFFFF9B55), EmpireColors.Violet, Color(0xFFFFE36E))
        val accent = accents[step.coerceIn(0, 4)]
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha = .23f), Color.Transparent), c, s * .5f), s * .5f, c)
        drawCircle(EmpireColors.SurfaceHigh.copy(alpha = .78f), s * .36f, c)
        drawCircle(accent.copy(alpha = .72f), s * .36f, c, style = Stroke(s * .012f))
        when (step.coerceIn(0, 4)) {
            0 -> {
                drawCircle(accent.copy(alpha=.25f),s*.18f,c)
                drawCircle(accent,s*.12f,c,style=Stroke(s*.025f))
                drawCircle(Color.White,s*.045f,c)
                repeat(if(lowPower)4 else 8){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/4f;drawLine(Offset(c.x+cos(a)*s*.15f,c.y+sin(a)*s*.15f),Offset(c.x+cos(a)*s*.28f,c.y+sin(a)*s*.28f),s*.012f,accent)}
            }
            1 -> {
                val base=s*.68f
                repeat(3){i->val x=s*(.28f+i*.18f);val h=s*(.22f+i*.06f);drawRoundRect(Color(0xFF17263A),Offset(x-s*.06f,base-h),Size(s*.12f,h));drawLine(accent,Offset(x-s*.04f,base-h+s*.05f),Offset(x+s*.04f,base-h+s*.05f),s*.012f)}
                drawLine(accent.copy(alpha=.65f),Offset(s*.22f,base),Offset(s*.78f,base),s*.018f)
            }
            2 -> {
                repeat(4){r->drawCircle(accent.copy(alpha=.72f-r*.12f),s*(.10f+r*.055f),c,style=Stroke(s*(.020f-r*.002f)))}
                repeat(if(lowPower)4 else 8){i->val a=-phase*2f*PI.toFloat()+i*PI.toFloat()/4f;drawCircle(Color.White,s*.012f,Offset(c.x+cos(a)*s*.29f,c.y+sin(a)*s*.29f))}
                drawCircle(Color.White,s*.045f,c)
            }
            3 -> {
                drawCircle(Color(0xFFD9AE86),s*.105f,Offset(c.x,c.y-s*.08f))
                drawArc(Color(0xFF18243A),185f,170f,true,Offset(c.x-s*.115f,c.y-s*.205f),Size(s*.23f,s*.18f))
                val torso=Path().apply{moveTo(s*.32f,s*.69f);quadraticTo(s*.36f,s*.52f,c.x,s*.52f);quadraticTo(s*.64f,s*.52f,s*.68f,s*.69f);close()};drawPath(torso,Color(0xFF1A3150));drawPath(torso,accent,style=Stroke(s*.016f))
                repeat(if(lowPower)3 else 6){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/3f;drawCircle(accent,s*.012f,Offset(c.x+cos(a)*s*.28f,c.y+sin(a)*s*.28f))}
            }
            4 -> {
                val diamond=Path().apply{moveTo(c.x,s*.22f);lineTo(s*.75f,c.y);lineTo(c.x,s*.78f);lineTo(s*.25f,c.y);close()};drawPath(diamond,accent.copy(alpha=.15f));drawPath(diamond,accent,style=Stroke(s*.020f))
                drawCircle(Brush.radialGradient(listOf(Color.White,accent,Color.Transparent),c,s*.16f),s*.16f,c)
                repeat(if(lowPower)4 else 8){i->val a=phase*2f*PI.toFloat()+i*PI.toFloat()/4f;drawCircle(if(i%2==0)EmpireColors.Cyan else accent,s*.014f,Offset(c.x+cos(a)*s*.31f,c.y+sin(a)*s*.22f))}
            }
        }
    }
}

@Composable
fun CelebrationBusinessSprite(businessId: Int, level: Int, size: androidx.compose.ui.unit.Dp = 116.dp) {
    when (businessId) {
        in 0..3 -> { BusinessGroup01Sprite(businessId, level, size); BusinessGroup01Evolution(businessId, level, size) }
        in 4..7 -> { BusinessGroup02Sprite(businessId, level, size); BusinessGroup02Evolution(businessId, level, size) }
        in 8..11 -> BusinessGroup03Sprite(businessId, level, size)
        in 12..13 -> BusinessGroup04Sprite(businessId, level, size)
    }
}
```

## File: src/main/java/com/zerotoempire/game/OrbitalIonTrail.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val IonTrailFrameSize = 128
private const val IonTrailColumns = 4
private const val IonTrailFrameCount = 8

/** Cosmic Foundry orbit accent, frozen on frame zero under reduced motion. */
@Composable
internal fun OrbitalIonTrail(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_14_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) {
            while (true) {
                delay(125)
                frame = (frame + 1) % IonTrailFrameCount
            }
        }
    }

    Canvas(modifier) {
        val effectSize = size.minDimension * .76f
        val destination = Offset((size.width - effectSize) * .5f, size.height * .08f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                (frame % IonTrailColumns) * IonTrailFrameSize,
                (frame / IonTrailColumns) * IonTrailFrameSize
            ),
            srcSize = IntSize(IonTrailFrameSize, IonTrailFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .68f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/PhaseDistortion.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val PhaseFrameSize = 128
private const val PhaseColumns = 4
private const val PhaseFrameCount = 8

/** Intergalactic Gateway phase aperture, frozen on frame zero under reduced motion. */
@Composable
internal fun PhaseDistortion(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_13_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }
    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) while (true) {
            delay(125)
            frame = (frame + 1) % PhaseFrameCount
        }
    }
    Canvas(modifier) {
        val effectSize = size.minDimension * .76f
        val destination = Offset((size.width - effectSize) * .5f, (size.height - effectSize) * .5f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset((frame % PhaseColumns) * PhaseFrameSize, (frame / PhaseColumns) * PhaseFrameSize),
            srcSize = IntSize(PhaseFrameSize, PhaseFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .64f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/PlayBillingGateway.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import com.android.billingclient.api.AcknowledgePurchaseParams
import com.android.billingclient.api.BillingClient
import com.android.billingclient.api.BillingClientStateListener
import com.android.billingclient.api.BillingFlowParams
import com.android.billingclient.api.BillingResult
import com.android.billingclient.api.ConsumeParams
import com.android.billingclient.api.PendingPurchasesParams
import com.android.billingclient.api.ProductDetails
import com.android.billingclient.api.QueryProductDetailsParams
import com.android.billingclient.api.QueryPurchasesParams
import com.android.billingclient.api.Purchase

class PlayBillingGateway(
    private val context: Context,
    private val diagnostics: BillingDiagnostics = if (BuildConfig.DEBUG) LocalBillingDiagnostics else NoOpBillingDiagnostics
) : PurchaseGateway {
    private data class DeferredPurchase(
        val product: StoreProduct,
        val callback: (PurchaseResult) -> Unit
    )

    private var pendingResult: ((PurchaseResult) -> Unit)? = null
    private var pendingProduct: StoreProduct? = null
    private val deferredPurchases = mutableMapOf<String, DeferredPurchase>()
    private val restoreCallbacks = mutableListOf<(RestoreResult) -> Unit>()
    private var connecting = false
    private var restoreInFlight = false
    private var restoreRunId = 0L

    private val billingClient = BillingClient.newBuilder(context)
        .setListener { result, purchases ->
            if (result.responseCode == BillingClient.BillingResponseCode.USER_CANCELED) {
                finishPending(PurchaseResult.Cancelled)
                return@setListener
            }
            if (result.responseCode != BillingClient.BillingResponseCode.OK || purchases == null) {
                finishPending(billingFailure(result, BillingOperation.PURCHASE_UPDATE, "Google Play purchase failed"))
                return@setListener
            }
            if (purchases.isEmpty()) {
                finishPending(PurchaseResult.Failed("Google Play returned no purchase to process"))
                return@setListener
            }

            // A launch callback must only be completed by the product that was actually launched.
            // Updates for older pending transactions may arrive while a different purchase flow is
            // active, so process those independently instead of failing or hijacking the new flow.
            // A token already deferred belongs to an older flow, even if it has the same product ID.
            val target = pendingProduct
            val activePurchase = if (pendingResult != null && target != null) {
                purchases.firstOrNull { target.productId in it.products && it.purchaseToken !in deferredPurchases }
            } else null
            if (activePurchase != null && target != null) {
                processPurchase(activePurchase, target)
            }
            val activeToken = activePurchase?.purchaseToken
            purchases.filter { it.purchaseToken != activeToken }.forEach { processPurchase(it) }
        }
        .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
        .enableAutoServiceReconnection()
        .build()

    override fun connect() {
        if (billingClient.isReady || connecting) return
        connecting = true
        billingClient.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(result: BillingResult) {
                connecting = false
                if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                    if (restoreCallbacks.isNotEmpty()) startRestoreQuery()
                } else {
                    failAllRestores(restoreFailure(result, BillingOperation.CONNECT, "Google Play Billing could not connect"))
                }
            }

            override fun onBillingServiceDisconnected() {
                connecting = false
                restoreInFlight = false
            }
        })
    }

    override fun disconnect() {
        restoreRunId++
        restoreCallbacks.clear()
        restoreInFlight = false
        connecting = false
        // Never retain Activity/UI callbacks beyond the gateway lifecycle.
        clearPending()
        deferredPurchases.clear()
        // End even an in-progress connection so a late setup callback cannot leave BillingClient
        // connected after the owning screen/gateway has already been disposed.
        billingClient.endConnection()
    }

    override fun purchase(activity: Activity, product: StoreProduct, onResult: (PurchaseResult) -> Unit) {
        if (pendingResult != null) {
            onResult(PurchaseResult.Failed("Another Google Play purchase is still being processed"))
            return
        }
        if (!billingClient.isReady) {
            onResult(PurchaseResult.Failed("Google Play Billing is not ready"))
            connect()
            return
        }
        // Reserve the complete query + launch cycle before starting asynchronous product lookup.
        // Without this guard, two rapid taps can both pass the initial check and open competing
        // Google Play flows before either query returns.
        pendingResult = onResult
        pendingProduct = product
        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(listOf(QueryProductDetailsParams.Product.newBuilder().setProductId(product.productId).setProductType(BillingClient.ProductType.INAPP).build()))
            .build()
        billingClient.queryProductDetailsAsync(params) { result, detailsResult ->
            // Ignore a stale lookup that completed after disconnect or another terminal result.
            if (pendingResult !== onResult || pendingProduct != product) return@queryProductDetailsAsync
            if (result.responseCode != BillingClient.BillingResponseCode.OK) {
                completePending(onResult, billingFailure(result, BillingOperation.PRODUCT_LOOKUP, "Google Play product lookup failed"))
                return@queryProductDetailsAsync
            }
            val details = detailsResult.productDetailsList.firstOrNull { it.productId == product.productId }
            if (details == null) {
                completePending(onResult, PurchaseResult.Failed("Product is unavailable in Google Play"))
                return@queryProductDetailsAsync
            }
            launch(activity, details, onResult)
        }
    }

    private fun launch(activity: Activity, details: ProductDetails, onResult: (PurchaseResult) -> Unit) {
        val productParams = BillingFlowParams.ProductDetailsParams.newBuilder().setProductDetails(details).build()
        val flowParams = BillingFlowParams.newBuilder().setProductDetailsParamsList(listOf(productParams)).build()
        val result = billingClient.launchBillingFlow(activity, flowParams)
        if (result.responseCode != BillingClient.BillingResponseCode.OK) {
            completePending(onResult, billingFailure(result, BillingOperation.LAUNCH, "Google Play could not start the purchase"))
        }
    }

    override fun restore(onResult: (RestoreResult) -> Unit) {
        restoreCallbacks += onResult
        if (restoreInFlight) return
        if (!billingClient.isReady) {
            connect()
            return
        }
        startRestoreQuery()
    }

    private fun startRestoreQuery() {
        if (restoreInFlight || restoreCallbacks.isEmpty()) return
        if (!billingClient.isReady) {
            connect()
            return
        }
        restoreInFlight = true
        val runId = ++restoreRunId
        val params = QueryPurchasesParams.newBuilder().setProductType(BillingClient.ProductType.INAPP).build()
        billingClient.queryPurchasesAsync(params) { result, purchases ->
            if (runId != restoreRunId) return@queryPurchasesAsync
            if (result.responseCode != BillingClient.BillingResponseCode.OK) {
                reconnectIfTransient(result)
                finishRestore(runId, RestoreResult.Failed(restoreFailure(result, BillingOperation.RESTORE, "Google Play could not restore purchases")))
                return@queryPurchasesAsync
            }
            val transactions = PurchaseRecovery.distinctTransactions(
                purchases,
                { it.purchaseToken }
            )
            val pendingProducts = transactions
                .filter { it.purchaseState == Purchase.PurchaseState.PENDING }
                .mapNotNull { StoreProductResolver.resolve(it.products) }
                .toSet()
            val purchased = transactions.filter { it.purchaseState == Purchase.PurchaseState.PURCHASED }
            val resolvedPurchases = purchased.mapNotNull { purchase ->
                StoreProductResolver.resolve(purchase.products)?.let { purchase to it }
            }
            val ambiguousPurchases = purchased.size - resolvedPurchases.size
            val permanentOwned = resolvedPurchases.map { it.second }
                .filterNot { it.consumable }
                .distinct()
            resolvedPurchases.filterNot { it.second.consumable }.forEach { (purchase, _) ->
                acknowledge(purchase) { }
            }
            val recoverable = resolvedPurchases.filter { it.second.consumable }
            if (recoverable.isEmpty()) {
                val restoreResult = if (ambiguousPurchases == 0) {
                    RestoreResult.Success(permanentOwned, pendingProducts)
                } else {
                    RestoreResult.Failed(
                        "An ambiguous Google Play transaction was not restored. Contact support if it remains unresolved.",
                        permanentOwned,
                        pendingProducts
                    )
                }
                finishRestore(runId, restoreResult)
                return@queryPurchasesAsync
            }

            val recovered = mutableListOf<StoreProduct>()
            var failedConsumables = 0
            var remaining = recoverable.size
            recoverable.forEach { (purchase, product) ->
                consumeRecovered(purchase) { success ->
                    if (runId != restoreRunId) return@consumeRecovered
                    if (success) recovered += product
                    else failedConsumables++
                    remaining--
                    if (remaining == 0) {
                        val products = permanentOwned + recovered
                        val restoreResult = if (failedConsumables == 0 && ambiguousPurchases == 0) {
                            RestoreResult.Success(products, pendingProducts)
                        } else {
                            val reason = if (ambiguousPurchases > 0) {
                                "An ambiguous Google Play transaction was not restored. Contact support if it remains unresolved."
                            } else {
                                "Some purchases could not be restored. Check your connection and try again."
                            }
                            RestoreResult.Failed(
                                reason,
                                products,
                                pendingProducts
                            )
                        }
                        finishRestore(runId, restoreResult)
                    }
                }
            }
        }
    }

    private fun finishRestore(runId: Long, result: RestoreResult) {
        if (runId != restoreRunId) return
        val callbacks = restoreCallbacks.toList()
        restoreCallbacks.clear()
        restoreInFlight = false
        callbacks.forEachIndexed { index, callback ->
            val products = PurchaseRecovery.deliveryForWaiter(result.products, index)
            callback(when (result) {
                is RestoreResult.Success -> result.copy(products = products)
                is RestoreResult.Failed -> result.copy(products = products)
            })
        }
    }

    private fun failAllRestores(reason: String) {
        restoreRunId++
        val callbacks = restoreCallbacks.toList()
        restoreCallbacks.clear()
        restoreInFlight = false
        callbacks.forEach { it(RestoreResult.Failed(reason)) }
    }

    private fun processPurchase(purchase: Purchase, expectedProduct: StoreProduct? = null) {
        val product = StoreProductResolver.resolve(purchase.products)
        if (product == null || expectedProduct != null && product != expectedProduct) {
            if (expectedProduct != null && pendingResult != null) {
                finishPending(PurchaseResult.Failed("Google Play returned an ambiguous or unexpected product"))
            }
            return
        }

        when (purchase.purchaseState) {
            Purchase.PurchaseState.PENDING -> {
                // A pending transaction can remain unresolved for hours or days. Release the active
                // store slot immediately, but retain this callback by purchase token so a later
                // PURCHASED update can still deliver the entitlement during the same app session.
                val callback = if (expectedProduct != null) pendingResult else null
                if (callback != null) {
                    deferredPurchases[purchase.purchaseToken] = DeferredPurchase(product, callback)
                    clearPending()
                    callback(PurchaseResult.Pending)
                }
            }
            Purchase.PurchaseState.PURCHASED -> {
                val deferred = deferredPurchases[purchase.purchaseToken]?.takeIf { it.product == product }
                val activeCallback = if (expectedProduct != null) pendingResult else null
                when {
                    deferred != null && product.consumable -> consumeDeferred(purchase, product, deferred.callback)
                    deferred != null -> acknowledge(purchase) { result ->
                        val purchaseResult = if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                            PurchaseResult.Success(product, purchase.purchaseToken)
                        } else {
                            billingFailure(result, BillingOperation.ACKNOWLEDGE, "Google Play could not confirm the purchase", record = false)
                        }
                        completeDeferred(purchase.purchaseToken, deferred.callback, purchaseResult)
                    }
                    activeCallback != null && product.consumable -> consume(purchase, product, activeCallback)
                    activeCallback != null -> acknowledge(purchase) { result ->
                        val purchaseResult = if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                            PurchaseResult.Success(product, purchase.purchaseToken)
                        } else {
                            billingFailure(result, BillingOperation.ACKNOWLEDGE, "Google Play could not confirm the purchase", record = false)
                        }
                        completePending(activeCallback, purchaseResult)
                    }
                    product.consumable -> {
                        // No live UI callback exists (for example after process recreation). Keep the
                        // purchase unconsumed so Restore Purchases / next launch can recover it safely.
                    }
                    else -> {
                        // Permanent purchases may complete after process recreation. Restore remains
                        // the entitlement source; acknowledge promptly to prevent automatic refund.
                        acknowledge(purchase) { }
                    }
                }
            }
            else -> {
                if (expectedProduct != null && pendingResult != null) {
                    finishPending(PurchaseResult.Failed("Google Play returned an unsupported purchase state: ${purchase.purchaseState}"))
                }
            }
        }
    }

    private fun clearPending() {
        pendingResult = null
        pendingProduct = null
    }

    private fun finishPending(result: PurchaseResult) {
        val callback = pendingResult ?: return
        clearPending()
        callback(result)
    }

    private fun completePending(callback: (PurchaseResult) -> Unit, result: PurchaseResult) {
        if (pendingResult !== callback) return
        clearPending()
        callback(result)
    }

    private fun completeDeferred(token: String, callback: (PurchaseResult) -> Unit, result: PurchaseResult) {
        val deferred = deferredPurchases[token] ?: return
        if (deferred.callback !== callback) return
        deferredPurchases.remove(token)
        callback(result)
    }

    private fun acknowledge(purchase: Purchase, onResult: (BillingResult) -> Unit) {
        if (purchase.isAcknowledged) {
            onResult(BillingResult.newBuilder().setResponseCode(BillingClient.BillingResponseCode.OK).build())
            return
        }
        val params = AcknowledgePurchaseParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.acknowledgePurchase(params) { result ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) recordFailure(result, BillingOperation.ACKNOWLEDGE)
            onResult(result)
        }
    }

    private fun consume(purchase: Purchase, product: StoreProduct, callback: (PurchaseResult) -> Unit) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ ->
            val purchaseResult = if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                PurchaseResult.Success(product, purchase.purchaseToken)
            } else {
                billingFailure(result, BillingOperation.CONSUME, "Google Play could not consume the purchase")
            }
            completePending(callback, purchaseResult)
        }
    }

    private fun consumeDeferred(purchase: Purchase, product: StoreProduct, callback: (PurchaseResult) -> Unit) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ ->
            val purchaseResult = if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                PurchaseResult.Success(product, purchase.purchaseToken)
            } else {
                billingFailure(result, BillingOperation.CONSUME, "Google Play could not consume the purchase")
            }
            completeDeferred(purchase.purchaseToken, callback, purchaseResult)
        }
    }

    private fun consumeRecovered(purchase: Purchase, done: (Boolean) -> Unit) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) recordFailure(result, BillingOperation.RECOVER_CONSUMABLE)
            reconnectIfTransient(result)
            done(result.responseCode == BillingClient.BillingResponseCode.OK)
        }
    }

    private fun billingFailure(
        result: BillingResult,
        operation: BillingOperation,
        fallback: String,
        record: Boolean = true
    ): PurchaseResult.Failed {
        if (record) recordFailure(result, operation)
        val failure = BillingFailurePolicy.resolve(result.failureKind(), result.debugMessage, fallback)
        if (failure.shouldReconnect) connect()
        return PurchaseResult.Failed(failure.message)
    }

    private fun reconnectIfTransient(result: BillingResult) {
        if (BillingFailurePolicy.resolve(result.failureKind(), result.debugMessage, "").shouldReconnect) connect()
    }

    private fun restoreFailure(result: BillingResult, operation: BillingOperation, fallback: String): String {
        recordFailure(result, operation)
        return BillingFailurePolicy.resolve(result.failureKind(), result.debugMessage, fallback).message
    }

    private fun recordFailure(result: BillingResult, operation: BillingOperation) {
        diagnostics.record(BillingDiagnostic(operation, result.responseCode, result.failureKind()))
    }

    private fun BillingResult.failureKind(): BillingFailureKind = when (responseCode) {
        BillingClient.BillingResponseCode.SERVICE_DISCONNECTED -> BillingFailureKind.SERVICE_DISCONNECTED
        BillingClient.BillingResponseCode.SERVICE_UNAVAILABLE -> BillingFailureKind.SERVICE_UNAVAILABLE
        BillingClient.BillingResponseCode.NETWORK_ERROR -> BillingFailureKind.NETWORK_ERROR
        else -> BillingFailureKind.OTHER
    }
}
```

## File: src/main/java/com/zerotoempire/game/PowerCoreTapImpact.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import kotlin.math.cos
import kotlin.math.sin

/**
 * Short-lived, tap-triggered VFX for the Power Core.
 *
 * Authored semantic sprites carry the primary visual identity whenever a
 * source-verified color match exists. Runtime Canvas drawing is limited to
 * lightweight motion accents and the violet-era fallback, for which no
 * validated authored pulse exists yet.
 */
@Composable
fun PowerCoreTapImpact(serial: Int, eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val progress = remember { Animatable(1f) }

    LaunchedEffect(serial, reducedMotion, lowPower) {
        if (serial <= 0 || reducedMotion) {
            progress.snapTo(1f)
            return@LaunchedEffect
        }
        progress.snapTo(0f)
        progress.animateTo(
            targetValue = 1f,
            animationSpec = tween(
                durationMillis = if (lowPower) 260 else 380,
                easing = FastOutSlowInEasing
            )
        )
    }

    if (serial <= 0 || reducedMotion || progress.value >= .999f) return

    val accent = when (eraIndex) {
        in 0..2 -> EmpireColors.Gold
        in 3..5 -> EmpireColors.Cyan
        in 6..8 -> EmpireColors.Violet
        else -> EmpireColors.GoldBright
    }
    val pulseEffect = powerCorePulseFx(eraIndex)
    val p = progress.value
    val fade = (1f - p).coerceIn(0f, 1f)

    Box(modifier) {
        pulseEffect?.let { effect ->
            CanonicalFxSprite(
                effect = effect,
                progress = p,
                modifier = Modifier.fillMaxSize(),
                alpha = .98f,
                startScale = .48f,
                endScale = 1.12f,
            )
        }
        if (!lowPower) {
            CanonicalFxSprite(
                effect = CanonicalFx.WELDING_SPARK_BURST,
                progress = p,
                modifier = Modifier.fillMaxSize(),
                alpha = .76f,
                startScale = .28f,
                endScale = .88f,
            )
        }

        Canvas(Modifier.fillMaxSize()) {
            val center = Offset(size.width / 2f, size.height / 2f)
            val min = size.minDimension

            if (pulseEffect == null) {
                val primaryRadius = min * (.22f + .30f * p)
                val secondaryRadius = min * (.16f + .22f * p)
                drawCircle(
                    color = accent.copy(alpha = fade * .78f),
                    radius = primaryRadius,
                    center = center,
                    style = Stroke(width = min * (.018f - .010f * p).coerceAtLeast(.004f))
                )
                if (!lowPower) {
                    drawCircle(
                        color = Color.White.copy(alpha = fade * .34f),
                        radius = secondaryRadius,
                        center = center,
                        style = Stroke(width = min * .005f)
                    )
                }
            }

            val sparkCount = if (lowPower) 4 else 8
            repeat(sparkCount) { index ->
                val angle = index * (Math.PI * 2.0 / sparkCount) + serial * .37
                val startRadius = min * (.21f + .08f * p)
                val endRadius = min * (.27f + .19f * p) * if (index % 3 == 0) 1.08f else 1f
                val start = Offset(
                    center.x + cos(angle).toFloat() * startRadius,
                    center.y + sin(angle).toFloat() * startRadius
                )
                val end = Offset(
                    center.x + cos(angle).toFloat() * endRadius,
                    center.y + sin(angle).toFloat() * endRadius
                )
                drawLine(
                    color = if (index % 2 == 0) {
                        accent.copy(alpha = fade * .42f)
                    } else {
                        Color.White.copy(alpha = fade * .28f)
                    },
                    start = start,
                    end = end,
                    strokeWidth = min * if (index % 3 == 0) .007f else .004f
                )
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/PremiumGameFeel.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.delay
import kotlin.math.cos
import kotlin.math.sin

private val premiumMilestones = intArrayOf(10, 25, 50, 100, 250, 500, 1000)

@Composable
fun PremiumProgressionStrip(state: GameState) {
    val next = ContentUnlocks.nextHiddenBusiness(state)
    val era = EmpireEras.current(state.lifetimeCash)
    val unlockProgress = if (next == null) 1f else ContentUnlocks.progressToNextUnlock(state)
    Surface(
        color = EmpireColors.Surface.copy(alpha = .72f),
        shape = RoundedCornerShape(20.dp),
        modifier = Modifier.fillMaxWidth().border(1.dp, EmpireColors.Cyan.copy(alpha = .10f), RoundedCornerShape(20.dp))
    ) {
        Column(Modifier.padding(horizontal = 15.dp, vertical = 12.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text("EMPIRE MOMENTUM", color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Black, letterSpacing = 1.5.sp)
                    Text(if (next == null) "All asset classes revealed" else "Next: ${next.name}", color = EmpireColors.TextPrimary, fontSize = 13.sp, fontWeight = FontWeight.Black)
                }
                Text("ERA ${era.index + 1}/11", color = EmpireColors.Gold, fontSize = 10.sp, fontWeight = FontWeight.Black)
            }
            Spacer(Modifier.height(8.dp))
            LinearProgressIndicator(progress = { unlockProgress.coerceIn(0f, 1f) }, modifier = Modifier.fillMaxWidth().height(4.dp), color = EmpireColors.Cyan, trackColor = EmpireColors.SurfaceHigh)
        }
    }
}

@Composable
fun PremiumMilestoneCelebration(state: GameState, modifier: Modifier = Modifier) {
    val eraIndex = EmpireEras.current(state.lifetimeCash).index
    var knownLevels by remember { mutableStateOf(state.businesses.associate { it.id to it.level }) }
    var knownEra by remember { mutableIntStateOf(eraIndex) }
    var serial by remember { mutableIntStateOf(0) }
    var title by remember { mutableStateOf("") }
    var subtitle by remember { mutableStateOf("") }
    var visible by remember { mutableStateOf(false) }

    LaunchedEffect(state.businesses, eraIndex) {
        val previousLevels = knownLevels
        val previousEra = knownEra
        val hit = state.businesses.firstOrNull { business ->
            val old = previousLevels[business.id] ?: business.level
            business.level > old && premiumMilestones.any { it in (old + 1)..business.level }
        }

        knownLevels = state.businesses.associate { it.id to it.level }
        knownEra = eraIndex

        val holdMillis = when {
            eraIndex > previousEra -> {
                title = "ERA ${eraIndex + 1} UNLOCKED"
                subtitle = "EMPIRE BREAKTHROUGH"
                1_650L
            }
            hit != null -> {
                val old = previousLevels[hit.id] ?: 0
                val reached = premiumMilestones.lastOrNull { it in (old + 1)..hit.level } ?: hit.level
                title = "POWER SPIKE  •  LV $reached"
                subtitle = hit.name.uppercase()
                1_350L
            }
            else -> 0L
        }

        if (holdMillis > 0L) {
            serial++
            val token = serial
            visible = true
            delay(holdMillis)
            if (token == serial) visible = false
        }
    }

    AnimatedVisibility(visible, enter = fadeIn(tween(160)), exit = fadeOut(tween(300)), modifier = modifier) {
        Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            PremiumBurst(serial)
            Surface(
                color = EmpireColors.DeepSpace.copy(alpha = .95f),
                shape = RoundedCornerShape(24.dp),
                modifier = Modifier.padding(34.dp).border(1.dp, EmpireColors.GoldBright.copy(alpha = .65f), RoundedCornerShape(24.dp))
            ) {
                Column(Modifier.padding(horizontal = 26.dp, vertical = 20.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(title, color = EmpireColors.GoldBright, fontSize = 12.sp, fontWeight = FontWeight.Black, letterSpacing = 1.2.sp)
                    Text(subtitle, color = EmpireColors.TextPrimary, fontSize = 20.sp, fontWeight = FontWeight.Black)
                    Text(if (title.startsWith("ERA")) "New empire systems online" else "Production evolved", color = EmpireColors.Cyan, fontSize = 10.sp, fontWeight = FontWeight.Bold)
                }
            }
        }
    }
}

@Composable
private fun PremiumBurst(seed: Int) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val progress = remember(seed) { Animatable(if (reduced) .72f else 0f) }

    LaunchedEffect(seed, reduced) {
        if (reduced) {
            progress.snapTo(.72f)
        } else {
            progress.snapTo(0f)
            progress.animateTo(
                targetValue = 1f,
                animationSpec = tween(durationMillis = 900, easing = FastOutSlowInEasing)
            )
        }
    }

    val p = progress.value
    Canvas(Modifier.fillMaxSize()) {
        val center = Offset(size.width / 2f, size.height / 2f)
        val count = if (lowPower) 10 else 20
        val radius = size.minDimension * (.16f + .34f * p)
        val fade = (1f - p).coerceIn(0f, 1f)

        drawCircle(
            EmpireColors.Gold.copy(alpha = (.20f * fade).coerceAtLeast(if (reduced) .04f else 0f)),
            radius * .72f,
            center,
            style = Stroke(size.minDimension * .008f)
        )
        drawCircle(
            Color.White.copy(alpha = (.13f * fade).coerceAtLeast(if (reduced) .025f else 0f)),
            radius * .52f,
            center,
            style = Stroke(size.minDimension * .004f)
        )

        repeat(count) { i ->
            val angle = i * (Math.PI * 2.0 / count) + seed * .17
            val start = radius * .45f
            val end = radius * (if (i % 3 == 0) 1f else .78f)
            val alpha = (.66f * fade).coerceAtLeast(if (reduced) .07f else 0f)
            val color = if (i % 2 == 0) EmpireColors.GoldBright else EmpireColors.Cyan
            drawLine(
                color.copy(alpha = alpha),
                Offset(center.x + cos(angle).toFloat() * start, center.y + sin(angle).toFloat() * start),
                Offset(center.x + cos(angle).toFloat() * end, center.y + sin(angle).toFloat() * end),
                size.minDimension * .006f
            )

            if (!reduced && !lowPower && i % 2 == 0) {
                val sparkRadius = radius * (.68f + (i % 4) * .055f)
                drawCircle(
                    color = if (i % 4 == 0) Color.White.copy(alpha = alpha * .92f) else color.copy(alpha = alpha * .78f),
                    radius = size.minDimension * if (i % 4 == 0) .008f else .005f,
                    center = Offset(
                        center.x + cos(angle + .08).toFloat() * sparkRadius,
                        center.y + sin(angle + .08).toFloat() * sparkRadius
                    )
                )
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/PremiumGameFeelOverlay.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier

/**
 * Non-blocking V2 feedback layer. It deliberately owns no economy state and
 * simply reacts to the already-sanitized GameState supplied by the main UI.
 */
@Composable
fun PremiumGameFeelOverlay(state: GameState, modifier: Modifier = Modifier) {
    Box(modifier.fillMaxSize()) {
        PremiumMilestoneCelebration(state, Modifier.fillMaxSize())
    }
}
```

## File: src/main/java/com/zerotoempire/game/PremiumGameFeelV2.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.draw.scale
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.ceil
import kotlin.math.cos
import kotlin.math.sin

private val campaignMilestones = listOf(10.0, 120.0, 1_500.0, 25_000.0, 500_000.0, 12_000_000.0, 350_000_000.0, 18_000_000_000.0, 2.5e12, 4e15, 2e18, 8e21, 3e25, 1.2e29, 1e30)

@Composable
fun PremiumCampaignPulse(state: GameState) {
    val current = state.lifetimeCash.coerceAtLeast(0.0)
    val next = campaignMilestones.firstOrNull { it > current } ?: campaignMilestones.last()
    val previous = campaignMilestones.lastOrNull { it <= current } ?: 0.0
    val denominator = (next - previous).coerceAtLeast(1.0)
    val progress = ((current - previous) / denominator).toFloat().coerceIn(0f, 1f)
    val remaining = (next - current).coerceAtLeast(0.0)
    Surface(
        color = EmpireColors.Surface.copy(alpha = .78f),
        shape = RoundedCornerShape(20.dp),
        modifier = Modifier.fillMaxWidth().border(1.dp, EmpireColors.Cyan.copy(alpha = .12f), RoundedCornerShape(20.dp))
    ) {
        Column(Modifier.padding(14.dp)) {
            Row(Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text("NEXT BREAKTHROUGH", color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Black, letterSpacing = 1.4.sp)
                    Text(if (remaining > 0.0) "$${EmpireNumberFormat.compact(remaining)} TO NEXT TIER" else "TRANSCENDENCE RANGE", color = EmpireColors.TextPrimary, fontSize = 13.sp, fontWeight = FontWeight.Black)
                }
                Text("${(progress * 100).toInt()}%", color = EmpireColors.Gold, fontSize = 12.sp, fontWeight = FontWeight.Black)
            }
            Spacer(Modifier.height(9.dp))
            LinearProgressIndicator(progress = { progress }, modifier = Modifier.fillMaxWidth().height(5.dp), color = EmpireColors.Cyan, trackColor = EmpireColors.SurfaceHigh)
        }
    }
}

/**
 * Lightweight hero VFX for the Power Core. The effect stays Canvas-based so
 * the composable count is fixed, and automatically scales down in low-power
 * and reduced-motion modes. Reduced-motion is truly static: no infinite
 * animation clock is created at all.
 */
@Composable
fun PremiumCoreAura(eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val accent = when (eraIndex) {
        in 0..2 -> EmpireColors.Gold
        in 3..5 -> EmpireColors.Cyan
        in 6..8 -> EmpireColors.Violet
        else -> EmpireColors.GoldBright
    }

    var pulse = 1f
    var auraAlpha = .26f
    var phase = 32f
    if (!reducedMotion) {
        val transition = rememberInfiniteTransition(label = "coreAura")
        val masterDurationMs = if (lowPower) 399_000 else 70_200
        val masterAnimated by transition.animateFloat(
            initialValue = 0f,
            targetValue = masterDurationMs.toFloat(),
            animationSpec = infiniteRepeatable(
                tween(masterDurationMs, easing = LinearEasing),
                RepeatMode.Restart
            ),
            label = "coreAuraMaster"
        )
        val pulseHalfCycleMs = if (lowPower) 1_900f else 1_300f
        val pulseCycle = (masterAnimated % (pulseHalfCycleMs * 2f)) / pulseHalfCycleMs
        val pulseFraction = if (pulseCycle <= 1f) pulseCycle else 2f - pulseCycle
        val easedPulse = FastOutSlowInEasing.transform(pulseFraction)
        val pulseMin = if (lowPower) .97f else .94f
        val pulseMax = if (lowPower) 1.025f else 1.045f
        val alphaMin = if (lowPower) .16f else .20f
        val alphaMax = if (lowPower) .30f else .46f
        val phaseCycleMs = if (lowPower) 10_500f else 5_400f
        pulse = pulseMin + (pulseMax - pulseMin) * easedPulse
        auraAlpha = alphaMin + (alphaMax - alphaMin) * easedPulse
        phase = (masterAnimated % phaseCycleMs) / phaseCycleMs * 360f
    }

    Box(modifier, contentAlignment = Alignment.Center) {
        Box(
            Modifier.fillMaxSize().scale(pulse).alpha(auraAlpha).background(
                Brush.radialGradient(
                    listOf(
                        accent.copy(alpha = if (lowPower) .62f else .80f),
                        accent.copy(alpha = if (lowPower) .09f else .14f),
                        Color.Transparent
                    )
                ),
                CircleShape
            )
        )

        Canvas(Modifier.fillMaxSize()) {
            val center = Offset(size.width / 2f, size.height / 2f)
            val min = size.minDimension
            val orbitCount = if (lowPower) 4 else 12
            val phaseRad = Math.toRadians(phase.toDouble())

            drawCircle(
                color = accent.copy(alpha = if (lowPower) .34f else .48f),
                radius = min * .43f,
                center = center,
                style = Stroke(width = min * .006f)
            )
            if (!lowPower) {
                drawCircle(
                    color = Color.White.copy(alpha = .14f),
                    radius = min * .34f,
                    center = center,
                    style = Stroke(width = min * .004f)
                )
            }

            repeat(orbitCount) { index ->
                val angle = phaseRad + index * (Math.PI * 2.0 / orbitCount)
                val radius = min * if (index % 3 == 0) .46f else .405f
                val dot = Offset(
                    x = center.x + cos(angle).toFloat() * radius,
                    y = center.y + sin(angle).toFloat() * radius
                )
                drawCircle(
                    color = if (index % 2 == 0) accent.copy(alpha = .80f) else Color.White.copy(alpha = .52f),
                    radius = min * if (index % 3 == 0) .014f else .009f,
                    center = dot
                )
            }

            if (!lowPower) {
                repeat(4) { index ->
                    val angle = -phaseRad * .72 + index * (Math.PI / 2.0)
                    val inner = min * .25f
                    val outer = min * .38f
                    drawLine(
                        color = accent.copy(alpha = .24f),
                        start = Offset(center.x + cos(angle).toFloat() * inner, center.y + sin(angle).toFloat() * inner),
                        end = Offset(center.x + cos(angle).toFloat() * outer, center.y + sin(angle).toFloat() * outer),
                        strokeWidth = min * .005f
                    )
                }
            }
        }

        Box(Modifier.fillMaxSize().scale(.88f).border(1.dp, accent.copy(alpha = auraAlpha), CircleShape))
        if (!lowPower) {
            Box(Modifier.fillMaxSize().scale(.68f).border(1.dp, Color.White.copy(alpha = auraAlpha * .50f), CircleShape))
        }
    }
}

/**
 * Compact phone-safe status deck. It deliberately uses two rows instead of one
 * crowded rail so values remain readable on narrow devices and never overlap.
 */
@Composable
fun PremiumEmpireSignal(state: GameState) {
    val owned = state.businesses.count { it.level > 0 }
    val automated = state.hiredManagerIds.size
    val era = EmpireEras.current(state.lifetimeCash)
    val now = System.currentTimeMillis()
    val boostLeftMs = (state.boostEndsAtMillis - now).coerceAtLeast(0L)
    val boostLabel = if (boostLeftMs > 0L) {
        val minutes = ceil(boostLeftMs / 60_000.0).toInt().coerceAtLeast(1)
        "×2 ${minutes}M"
    } else "OFF"

    Surface(
        color = EmpireColors.DeepSpace.copy(alpha = .78f),
        shape = RoundedCornerShape(20.dp),
        modifier = Modifier.fillMaxWidth().border(1.dp, Color.White.copy(alpha = .05f), RoundedCornerShape(20.dp))
    ) {
        Column(Modifier.padding(7.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                SignalChip("ERA", "${era.index + 1}/11", Modifier.weight(1f), EmpireColors.Cyan)
                SignalChip("GEMS", state.gems.toString(), Modifier.weight(1f), EmpireColors.Violet)
                SignalChip("BOOST", boostLabel, Modifier.weight(1f), if (boostLeftMs > 0L) EmpireColors.GoldBright else EmpireColors.TextSecondary)
            }
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                SignalChip("ASSETS", "$owned/${state.businesses.size}", Modifier.weight(1f), EmpireColors.Gold)
                SignalChip("AUTO", "$automated/${state.businesses.size}", Modifier.weight(1f), EmpireColors.Success)
            }
        }
    }
}

@Composable
private fun SignalChip(label: String, value: String, modifier: Modifier = Modifier, accent: Color = EmpireColors.TextPrimary) {
    Surface(color = EmpireColors.Surface.copy(alpha = .72f), shape = RoundedCornerShape(13.dp), modifier = modifier) {
        Column(Modifier.padding(horizontal = 5.dp, vertical = 8.dp), horizontalAlignment = Alignment.CenterHorizontally) {
            Text(label, color = EmpireColors.TextSecondary, fontSize = 7.sp, fontWeight = FontWeight.Bold, letterSpacing = .8.sp, maxLines = 1)
            Text(value, color = accent, fontSize = 12.sp, fontWeight = FontWeight.Black, maxLines = 1)
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/PremiumGameUiV2.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.scaleIn
import androidx.compose.animation.scaleOut
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.onClick
import androidx.compose.ui.semantics.role
import androidx.compose.ui.semantics.selected
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

private enum class PremiumTab(val label: String, val glyph: String) {
    EMPIRE("EMPIRE", "◉"), MANAGERS("MANAGERS", "◇"), UPGRADES("UPGRADES", "⬡"), GOALS("GOALS", "★")
}

@Composable
fun PremiumZeroToEmpireApp(vm: GameViewModel) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val buyMode by vm.buyMode.collectAsStateWithLifecycle()
    var tab by remember { mutableStateOf(PremiumTab.EMPIRE) }
    val era = EmpireEras.current(state.lifetimeCash)
    MaterialTheme(colorScheme = EmpireColorScheme) {
        Scaffold(containerColor = EmpireColors.Void, bottomBar = { PremiumNav(tab) { tab = it } }) { padding ->
            Box(Modifier.fillMaxSize().padding(padding)) {
                EmpireAmbientBackdrop(era.index, Modifier.fillMaxSize())
                when (tab) {
                    PremiumTab.EMPIRE -> AscendantCityEmpireWorld(vm, state, buyMode)
                    PremiumTab.MANAGERS -> PremiumManagersTab(vm, state)
                    PremiumTab.UPGRADES -> PremiumUpgradeTreeScreen(vm, state)
                    PremiumTab.GOALS -> PremiumGoalsTab(vm, state, meta)
                }
            }
        }
    }
}

@Composable
private fun PremiumEmpireTab(vm: GameViewModel, state: GameState, buyMode: BuyMode) {
    val visible = remember(state.businesses, state.lifetimeCash) { ContentUnlocks.visibleBusinesses(state) }
    var previousEra by remember { mutableIntStateOf(state.empireLevel) }
    var eraReveal by remember { mutableStateOf(false) }
    LaunchedEffect(state.empireLevel) {
        if (state.empireLevel > previousEra) { previousEra = state.empireLevel; eraReveal = true; delay(1800); eraReveal = false } else previousEra = state.empireLevel
    }
    Box(Modifier.fillMaxSize()) {
        LazyColumn(Modifier.fillMaxSize(), contentPadding = PaddingValues(16.dp,14.dp,16.dp,30.dp), verticalArrangement = Arrangement.spacedBy(13.dp)) {
            item { PremiumTopStatus(state) }; item { PremiumEmpireSignal(state) }; item { CinematicEraHero(state) }; item { PremiumCampaignPulse(state) }; item { PremiumPowerCore(state, vm::tap) }; item { PurchaseModeRail(vm, buyMode) }; item { PremiumSectionTitle("ASSET NETWORK", "${state.businesses.sumOf { it.level }} levels online") }
            items(visible, key = { it.id }) { PremiumBusinessCard(vm, it, state, buyMode) }
            ContentUnlocks.nextHiddenBusiness(state)?.let { item { PremiumLockedAsset(state, it) } }; item { PremiumAscensionCard(vm, state) }
        }
        AnimatedVisibility(eraReveal, enter=fadeIn()+scaleIn(initialScale=.86f), exit=fadeOut()+scaleOut(targetScale=1.08f), modifier=Modifier.align(Alignment.Center)) {
            val era=EmpireEras.current(state.lifetimeCash); Surface(color=EmpireColors.DeepSpace.copy(alpha=.96f),shape=RoundedCornerShape(28.dp),modifier=Modifier.padding(28.dp).border(1.dp,EmpireColors.Gold.copy(alpha=.55f),RoundedCornerShape(28.dp))){Column(Modifier.padding(horizontal=28.dp,vertical=24.dp),horizontalAlignment=Alignment.CenterHorizontally){Text("NEW ERA",color=EmpireColors.Gold,fontSize=11.sp,fontWeight=FontWeight.Black,letterSpacing=2.4.sp);Text(era.name.uppercase(),color=EmpireColors.TextPrimary,fontSize=25.sp,fontWeight=FontWeight.Black);Text("Empire evolution unlocked",color=EmpireColors.Cyan,fontSize=11.sp,fontWeight=FontWeight.Bold)}}
        }
    }
}

@Composable private fun PremiumTopStatus(state: GameState) { Surface(color=EmpireColors.Surface.copy(alpha=.82f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth().border(1.dp,Color.White.copy(alpha=.06f),RoundedCornerShape(22.dp))) { Row(Modifier.padding(horizontal=16.dp,vertical=13.dp),verticalAlignment=Alignment.CenterVertically) { Column(Modifier.weight(1f)) { Text("NET WORTH",color=EmpireColors.TextSecondary,fontSize=10.sp,fontWeight=FontWeight.Bold,letterSpacing=1.4.sp);Text(moneyV2(state.cash),color=EmpireColors.TextPrimary,fontSize=30.sp,fontWeight=FontWeight.Black) }; Column(horizontalAlignment=Alignment.End) { Text("+${moneyV2(state.incomePerSecond)}/S",color=EmpireColors.Success,fontSize=14.sp,fontWeight=FontWeight.Black);Text("LEGACY ×${String.format("%.2f",state.prestigeMultiplier)}",color=EmpireColors.Gold,fontSize=10.sp,fontWeight=FontWeight.Bold) } } } }

@Composable private fun CinematicEraHero(state: GameState) { val era=EmpireEras.current(state.lifetimeCash); Surface(color=Color.Transparent,shape=RoundedCornerShape(28.dp),modifier=Modifier.fillMaxWidth().height(218.dp).border(1.dp,EmpireColors.Cyan.copy(alpha=.16f),RoundedCornerShape(28.dp))) { Box(Modifier.background(Brush.verticalGradient(listOf(EmpireColors.SurfaceHigh.copy(alpha=.72f),EmpireColors.DeepSpace.copy(alpha=.94f),EmpireColors.Void.copy(alpha=.98f))))) { EraVistaAAA(era.index,Modifier.fillMaxSize());Box(Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(Color.Transparent,EmpireColors.Void.copy(alpha=.88f)))));Column(Modifier.align(Alignment.BottomStart).padding(18.dp)) { Text("ERA ${era.index+1}",color=EmpireColors.Cyan,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=1.8.sp);Text(era.name.uppercase(),color=EmpireColors.TextPrimary,fontSize=25.sp,fontWeight=FontWeight.Black);Text("Lifetime capital ${moneyV2(state.lifetimeCash)}",color=EmpireColors.TextSecondary,fontSize=11.sp) } } } }

@Composable private fun PremiumPowerCore(state: GameState,tap:()->Unit) {
    val haptic=LocalHapticFeedback.current;val scope=rememberCoroutineScope();val scale=remember{Animatable(1f)};var pop by remember{mutableStateOf(false)};var lastGain by remember{mutableDoubleStateOf(0.0)};var combo by remember{mutableIntStateOf(0)};var comboToken by remember{mutableIntStateOf(0)};var impactSerial by remember{mutableIntStateOf(0)};val eraIndex=EmpireEras.current(state.lifetimeCash).index
    Surface(color=EmpireColors.Surface.copy(alpha=.70f),shape=RoundedCornerShape(30.dp),modifier=Modifier.fillMaxWidth().border(1.dp,EmpireColors.Gold.copy(alpha=.15f),RoundedCornerShape(30.dp))) { Column(Modifier.padding(vertical=18.dp),horizontalAlignment=Alignment.CenterHorizontally) { Text("POWER CORE",color=EmpireColors.Gold,fontSize=11.sp,fontWeight=FontWeight.Black,letterSpacing=2.sp);Text("Tap to inject capital",color=EmpireColors.TextSecondary,fontSize=10.sp);Spacer(Modifier.height(8.dp));Box(Modifier.height(206.dp).fillMaxWidth(),contentAlignment=Alignment.Center) { PremiumCoreAura(eraIndex, Modifier.size(190.dp));PowerCoreTapImpact(impactSerial,eraIndex,Modifier.size(202.dp));Box(Modifier.size(188.dp).scale(scale.value).background(Brush.radialGradient(listOf(EmpireColors.Gold.copy(alpha=.16f),EmpireColors.Cyan.copy(alpha=.06f),Color.Transparent)),CircleShape).semantics { contentDescription="Power Core, ${moneyV2(state.tapValue)} per tap";role=Role.Button;onClick(label="Inject capital"){tap();true} }.pointerInput(state.tapValue) { detectTapGestures(onPress={scale.animateTo(.93f,spring(stiffness=Spring.StiffnessHigh));if(tryAwaitRelease()){lastGain=state.tapValue;tap();impactSerial++;combo=(combo+1).coerceAtMost(99);comboToken++;haptic.performHapticFeedback(HapticFeedbackType.TextHandleMove);pop=true;scope.launch{scale.animateTo(1.08f,spring(dampingRatio=.38f,stiffness=Spring.StiffnessMedium));scale.animateTo(1f,spring(dampingRatio=.55f))};scope.launch{delay(430);pop=false};val token=comboToken;scope.launch{delay(900);if(token==comboToken)combo=0}}else scale.snapTo(1f)}) },contentAlignment=Alignment.Center) { EmpireCoreGlyph(Modifier.size(166.dp),eraIndex=eraIndex) };if(pop) Text("+${moneyV2(lastGain)}",color=EmpireColors.GoldBright,fontSize=22.sp,fontWeight=FontWeight.Black,modifier=Modifier.align(Alignment.TopCenter));if(combo>=3) Text("CHAIN ×$combo",color=EmpireColors.Cyan,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=1.2.sp,modifier=Modifier.align(Alignment.BottomCenter)) };Text("+${moneyV2(state.tapValue)} PER TAP",color=EmpireColors.TextPrimary,fontSize=13.sp,fontWeight=FontWeight.Black) } }
}

@Composable private fun PurchaseModeRail(vm:GameViewModel,selected:BuyMode){val modes=listOf(BuyMode.X1 to "×1",BuyMode.X10 to "×10",BuyMode.X25 to "×25",BuyMode.MILESTONE to "NEXT",BuyMode.MAX to "MAX");Surface(color=EmpireColors.Surface.copy(alpha=.86f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(6.dp),horizontalArrangement=Arrangement.spacedBy(4.dp)){modes.forEach{(mode,label)->val active=mode==selected;Surface(color=if(active)EmpireColors.Violet.copy(alpha=.90f)else Color.Transparent,shape=RoundedCornerShape(13.dp),modifier=Modifier.weight(1f).height(48.dp).clickable(role=Role.RadioButton){vm.setBuyMode(mode)}.semantics{this.selected=active}){Box(contentAlignment=Alignment.Center){Text(label,color=if(active)Color.White else EmpireColors.TextSecondary,fontSize=10.sp,fontWeight=FontWeight.Black)}}}}}}

@Composable private fun PremiumBusinessCard(vm:GameViewModel,business:Business,state:GameState,mode:BuyMode){
    val quote=vm.bulkQuote(business.id,mode);val affordable=quote.count>0&&state.cash>=quote.cost;val target=business.nextMilestone?:((business.level/1000)+1)*1000;val previous=listOf(0,10,25,50,100,250,500,1000).lastOrNull{it<=business.level}?:0;val progress=((business.level-previous).toFloat()/(target-previous).coerceAtLeast(1)).coerceIn(0f,1f);val borderColor by animateColorAsState(if(affordable)EmpireColors.Gold.copy(alpha=.34f)else Color.White.copy(alpha=.06f),label="assetBorder");val haptic=LocalHapticFeedback.current;val scope=rememberCoroutineScope();val scale=remember{Animatable(1f)};var pulse by remember{mutableStateOf(false)};var purchaseFlash by remember{mutableStateOf(false)};var purchasedCount by remember{mutableIntStateOf(0)};var oldLevel by remember{mutableIntStateOf(business.level)}
    LaunchedEffect(business.level){val crossed=business.level>oldLevel&&listOf(10,25,50,100,250,500,1000).any{it in (oldLevel+1)..business.level};oldLevel=business.level;if(crossed){pulse=true;haptic.performHapticFeedback(HapticFeedbackType.LongPress);delay(900);pulse=false}}
    val buy={if(affordable){purchasedCount=quote.count;purchaseFlash=true;vm.buyBulk(business.id,mode);haptic.performHapticFeedback(if(quote.count>=25)HapticFeedbackType.LongPress else HapticFeedbackType.TextHandleMove);scope.launch{scale.animateTo(.965f,spring(stiffness=Spring.StiffnessHigh));scale.animateTo(1.025f,spring(dampingRatio=.45f,stiffness=Spring.StiffnessMedium));scale.animateTo(1f,spring(dampingRatio=.6f))};scope.launch{delay(360);purchaseFlash=false}}}
    Surface(color=when{pulse->EmpireColors.Gold.copy(alpha=.13f);purchaseFlash->EmpireColors.Cyan.copy(alpha=.11f);else->EmpireColors.Surface.copy(alpha=.94f)},shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth().scale(scale.value).border(if(pulse||purchaseFlash)2.dp else 1.dp,when{pulse->EmpireColors.GoldBright;purchaseFlash->EmpireColors.Cyan;else->borderColor},RoundedCornerShape(22.dp)).clickable(enabled=affordable,onClick=buy)){
        Box{Column(Modifier.padding(14.dp)){if(pulse){Text("POWER SPIKE UNLOCKED",color=EmpireColors.GoldBright,fontSize=9.sp,fontWeight=FontWeight.Black,letterSpacing=1.3.sp);Spacer(Modifier.height(6.dp))};Row(verticalAlignment=Alignment.CenterVertically){BusinessArtIcon(business.id,business.level,64.dp);Spacer(Modifier.width(12.dp));Column(Modifier.weight(1f)){Text(business.name,color=EmpireColors.TextPrimary,fontSize=17.sp,fontWeight=FontWeight.Black,maxLines=1,overflow=TextOverflow.Ellipsis);Text("LEVEL ${business.level}",color=EmpireColors.TextSecondary,fontSize=9.sp,fontWeight=FontWeight.Bold,letterSpacing=1.sp);Text("${moneyV2(state.businessIncome(business)*state.permanentIncomeMultiplier*state.boostMultiplier*state.eventMultiplier)}/S",color=EmpireColors.Cyan,fontSize=12.sp,fontWeight=FontWeight.Black)};Column(horizontalAlignment=Alignment.End){Text(if(quote.count>0)"+${quote.count}" else "—",color=if(affordable)EmpireColors.GoldBright else EmpireColors.TextSecondary,fontSize=14.sp,fontWeight=FontWeight.Black);Text(if(quote.count>0)moneyV2(quote.cost)else "NOT ENOUGH",color=if(affordable)EmpireColors.Gold else EmpireColors.TextSecondary,fontSize=10.sp,fontWeight=FontWeight.Bold)}};Spacer(Modifier.height(11.dp));LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(5.dp),color=if(pulse)EmpireColors.GoldBright else EmpireColors.Gold,trackColor=EmpireColors.SurfaceHigh);Spacer(Modifier.height(6.dp));Row(Modifier.fillMaxWidth()){Text("POWER SPIKE",color=EmpireColors.TextSecondary,fontSize=9.sp,fontWeight=FontWeight.Bold);Spacer(Modifier.weight(1f));Text("LV $target",color=EmpireColors.Gold,fontSize=9.sp,fontWeight=FontWeight.Black)}};AnimatedVisibility(purchaseFlash,enter=fadeIn()+scaleIn(initialScale=.72f),exit=fadeOut()+scaleOut(targetScale=1.18f),modifier=Modifier.align(Alignment.TopEnd).padding(10.dp)){Surface(color=EmpireColors.Cyan.copy(alpha=.92f),shape=RoundedCornerShape(12.dp)){Text("+$purchasedCount LEVEL${if(purchasedCount==1)"" else "S"}",color=EmpireColors.Void,fontSize=10.sp,fontWeight=FontWeight.Black,modifier=Modifier.padding(horizontal=10.dp,vertical=6.dp))}}}
    }
}

@Composable private fun PremiumLockedAsset(state:GameState,next:Business){val threshold=ContentUnlocks.thresholdForBusiness(next.id);val progress=ContentUnlocks.progressToNextUnlock(state);Surface(color=EmpireColors.Surface.copy(alpha=.58f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(16.dp)){Text("NEXT ASSET CLASSIFIED",color=EmpireColors.Violet,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=1.5.sp);Spacer(Modifier.height(4.dp));Text("Unlock at ${moneyV2(threshold)} lifetime capital",color=EmpireColors.TextPrimary,fontSize=13.sp,fontWeight=FontWeight.Bold);Spacer(Modifier.height(9.dp));LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(5.dp),color=EmpireColors.Violet,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun PremiumAscensionCard(vm:GameViewModel,state:GameState){
    val targetPoints=Progression.prestigeReward(state.lifetimeCash)
    val gain=(targetPoints-state.prestigePoints).coerceAtLeast(0)
    var confirmAscension by remember { mutableStateOf(false) }
    Surface(color=EmpireColors.Gold.copy(alpha=.09f),shape=RoundedCornerShape(26.dp),modifier=Modifier.fillMaxWidth().border(1.dp,EmpireColors.Gold.copy(alpha=.20f),RoundedCornerShape(26.dp))){
        Column(Modifier.padding(18.dp)){
            Text("ASCENSION",color=EmpireColors.Gold,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=2.sp)
            Text("Rebuild. Return stronger.",color=EmpireColors.TextPrimary,fontSize=21.sp,fontWeight=FontWeight.Black)
            Text("Current Legacy ×${String.format("%.2f",state.prestigeMultiplier)}  •  Next +$gain points",color=EmpireColors.TextSecondary,fontSize=11.sp)
            Spacer(Modifier.height(12.dp))
            Button(onClick={confirmAscension=true},enabled=gain>0,modifier=Modifier.fillMaxWidth().height(48.dp),shape=RoundedCornerShape(15.dp),colors=ButtonDefaults.buttonColors(containerColor=EmpireColors.Gold,contentColor=EmpireColors.Void)){
                Text(if(gain>0)"ASCEND  +$gain LEGACY" else "BUILD MORE CAPITAL",fontWeight=FontWeight.Black)
            }
        }
    }
    if(confirmAscension&&gain>0){
        AlertDialog(
            onDismissRequest={confirmAscension=false},
            title={Text("CONFIRM ASCENSION",fontWeight=FontWeight.Black)},
            text={Text("Ascension resets cash, lifetime capital, asset levels and managers. Gems, permanent upgrades, Legacy and your active boost are kept. You will gain +$gain Legacy.")},
            confirmButton={TextButton(onClick={confirmAscension=false;vm.prestige()},modifier=Modifier.height(48.dp)){Text("ASCEND +$gain LEGACY",fontWeight=FontWeight.Black)}},
            dismissButton={TextButton(onClick={confirmAscension=false},modifier=Modifier.height(48.dp)){Text("CANCEL",fontWeight=FontWeight.Black)}}
        )
    }
}

@Composable private fun PremiumManagersTab(vm:GameViewModel,state:GameState){val visible=remember(state.hiredManagerIds,state.lifetimeCash,state.cash){ContentUnlocks.visibleManagers(state)};PremiumListShell("EXECUTIVE NETWORK","Managers automate offline production"){items(visible,key={it.businessId}){manager->val hired=manager.businessId in state.hiredManagerIds;val canHire=!hired&&state.cash>=manager.cost;val shortfall=(manager.cost-state.cash).coerceAtLeast(0.0);val cardColor=when{hired->EmpireColors.Cyan.copy(alpha=.10f);canHire->EmpireColors.Gold.copy(alpha=.10f);else->EmpireColors.Surface.copy(alpha=.92f)};val borderColor=when{hired->EmpireColors.Cyan.copy(alpha=.30f);canHire->EmpireColors.Gold.copy(alpha=.40f);else->Color.White.copy(alpha=.06f)};val status=when{hired->"HIRED • AUTOMATING";canHire->"READY TO HIRE";else->"NEED ${moneyV2(shortfall)}"};val statusColor=when{hired->EmpireColors.Cyan;canHire->EmpireColors.GoldBright;else->EmpireColors.TextSecondary};Surface(color=cardColor,shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth().border(1.dp,borderColor,RoundedCornerShape(22.dp))){Row(Modifier.padding(15.dp),verticalAlignment=Alignment.CenterVertically){ManagerPortrait(manager.businessId,62.dp);Spacer(Modifier.width(12.dp));Column(Modifier.weight(1f)){Text(manager.name,color=EmpireColors.TextPrimary,fontSize=17.sp,fontWeight=FontWeight.Black,maxLines=1,overflow=TextOverflow.Ellipsis);Text(manager.title,color=EmpireColors.TextSecondary,fontSize=10.sp,maxLines=1,overflow=TextOverflow.Ellipsis);Spacer(Modifier.height(3.dp));Text("×${manager.incomeMultiplier} production",color=if(hired)EmpireColors.Cyan else EmpireColors.Gold,fontSize=11.sp,fontWeight=FontWeight.Bold);Text(status,color=statusColor,fontSize=9.sp,fontWeight=FontWeight.Black,letterSpacing=.6.sp,maxLines=1,overflow=TextOverflow.Ellipsis)};Spacer(Modifier.width(8.dp));Button(onClick={vm.hireManager(manager.businessId)},enabled=canHire,modifier=Modifier.width(112.dp).height(48.dp),shape=RoundedCornerShape(13.dp),contentPadding=PaddingValues(horizontal=8.dp),colors=ButtonDefaults.buttonColors(containerColor=EmpireColors.Gold,contentColor=EmpireColors.Void)){Text(when{hired->"HIRED";canHire->"HIRE • ${moneyV2(manager.cost)}";else->moneyV2(manager.cost)},fontSize=9.sp,fontWeight=FontWeight.Black,maxLines=1,overflow=TextOverflow.Ellipsis)}}}}}}
@Composable private fun PremiumUpgradesTab(vm:GameViewModel,state:GameState){PremiumListShell("PERMANENT LAB","Permanent systems survive every ascension"){item{Surface(color=EmpireColors.Violet.copy(alpha=.12f),shape=RoundedCornerShape(20.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(16.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.GEM,44.dp);Spacer(Modifier.width(10.dp));Text("${state.gems} GEMS",color=EmpireColors.Violet,fontSize=23.sp,fontWeight=FontWeight.Black)}}};items(Upgrades.catalog,key={it.id}){upgrade->val rank=state.upgradeRanks[upgrade.id]?:0;val maxed=rank>=upgrade.maxRank;val canBuy=!maxed&&state.gems>=upgrade.gemCost;Surface(color=EmpireColors.Surface.copy(alpha=.92f),shape=RoundedCornerShape(21.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(16.dp)){Row(verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(upgrade.name,color=EmpireColors.TextPrimary,fontSize=16.sp,fontWeight=FontWeight.Black);Text(upgrade.description,color=EmpireColors.TextSecondary,fontSize=10.sp)};Text("$rank/${upgrade.maxRank}",color=EmpireColors.Cyan,fontSize=11.sp,fontWeight=FontWeight.Black)};Spacer(Modifier.height(10.dp));Button(onClick={vm.buyUpgrade(upgrade.id)},enabled=canBuy,modifier=Modifier.fillMaxWidth(),shape=RoundedCornerShape(13.dp)){Text(if(maxed)"MAXED" else "UPGRADE  •  ${upgrade.gemCost} GEMS",fontWeight=FontWeight.Black,fontSize=10.sp)}}}};item{Button(onClick=vm::activateProfitBoost,modifier=Modifier.fillMaxWidth().height(50.dp),shape=RoundedCornerShape(16.dp)){Text("⚡ WATCH REWARD  •  ×2 PROFITS",fontWeight=FontWeight.Black)}}}}
@Composable private fun PremiumGoalsTab(vm:GameViewModel,state:GameState,meta:PlayerMeta){PremiumListShell("COMMAND CENTER","Daily, weekly and permanent objectives"){item{val claimable=vm.canClaimDaily();Surface(color=EmpireColors.Gold.copy(alpha=.10f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(16.dp)){Text("DAILY DROP",color=EmpireColors.Gold,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=1.5.sp);Text("${meta.streakDays} day streak",color=EmpireColors.TextPrimary,fontSize=19.sp,fontWeight=FontWeight.Black);Spacer(Modifier.height(10.dp));Button(onClick={vm.claimDaily()},enabled=claimable,modifier=Modifier.fillMaxWidth(),shape=RoundedCornerShape(13.dp)){Text(if(claimable)"CLAIM DAILY REWARD" else "CLAIMED TODAY",fontWeight=FontWeight.Black)}}}};item{ChallengeDock(vm,Modifier.fillMaxWidth())};item{PremiumSectionTitle("MISSIONS","Short-term progression")};items(vm.missions(),key={it.id}){mission->ObjectiveCard(mission.title,"+${mission.rewardGems} gems",mission.fraction,if(mission.claimed)"DONE" else if(mission.completed)"CLAIM" else "${(mission.fraction*100).toInt()}%",mission.completed&&!mission.claimed){vm.claimMission(mission.id)}};item{PremiumSectionTitle("ACHIEVEMENTS","Permanent campaign milestones")};items(vm.achievements(),key={it.id}){a->ObjectiveCard(a.title,a.description,if(a.unlocked)1f else 0f,if(a.claimed)"DONE" else if(a.unlocked)"+${a.rewardGems}" else "LOCKED",a.unlocked&&!a.claimed){vm.claimAchievement(a.id)}}}}
@Composable private fun ObjectiveCard(title:String,subtitle:String,progress:Float,action:String,enabled:Boolean,onClick:()->Unit){Surface(color=EmpireColors.Surface.copy(alpha=.91f),shape=RoundedCornerShape(19.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(14.dp)){Row(verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black,fontSize=14.sp);Text(subtitle,color=EmpireColors.TextSecondary,fontSize=10.sp,maxLines=2,overflow=TextOverflow.Ellipsis)};TextButton(onClick=onClick,enabled=enabled){Text(action,fontWeight=FontWeight.Black,fontSize=10.sp)}};LinearProgressIndicator(progress={progress.coerceIn(0f,1f)},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Cyan,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun PremiumListShell(title:String,subtitle:String,content:androidx.compose.foundation.lazy.LazyListScope.()->Unit){LazyColumn(Modifier.fillMaxSize(),contentPadding=PaddingValues(16.dp,18.dp,16.dp,30.dp),verticalArrangement=Arrangement.spacedBy(12.dp)){item{Column{Text(title,color=EmpireColors.TextPrimary,fontSize=27.sp,fontWeight=FontWeight.Black);Text(subtitle,color=EmpireColors.TextSecondary,fontSize=11.sp)}};content()}}
@Composable private fun PremiumSectionTitle(title:String,subtitle:String){Column{Text(title,color=EmpireColors.TextPrimary,fontSize=15.sp,fontWeight=FontWeight.Black,letterSpacing=1.sp);Text(subtitle,color=EmpireColors.TextSecondary,fontSize=10.sp)}}
@Composable private fun PremiumNav(selected:PremiumTab,onSelect:(PremiumTab)->Unit){NavigationBar(containerColor=EmpireColors.Surface.copy(alpha=.98f),modifier=Modifier.navigationBarsPadding()){PremiumTab.entries.forEach{tab->NavigationBarItem(selected=selected==tab,onClick={onSelect(tab)},icon={Text(tab.glyph,fontSize=17.sp)},label={Text(tab.label,fontSize=8.sp,fontWeight=FontWeight.Black)},alwaysShowLabel=true)}}}

private fun moneyV2(value:Double):String{if(!value.isFinite())return "∞";val v=value.coerceAtLeast(0.0);return when{v>=1e30->String.format("%.2fN",v/1e30);v>=1e27->String.format("%.2fO",v/1e27);v>=1e24->String.format("%.2fSp",v/1e24);v>=1e21->String.format("%.2fSx",v/1e21);v>=1e18->String.format("%.2fQi",v/1e18);v>=1e15->String.format("%.2fQa",v/1e15);v>=1e12->String.format("%.2fT",v/1e12);v>=1e9->String.format("%.2fB",v/1e9);v>=1e6->String.format("%.2fM",v/1e6);v>=1e3->String.format("%.2fK",v/1e3);else->String.format("%.0f",v)}}
```

## File: src/main/java/com/zerotoempire/game/PremiumGoalsCenter.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun PremiumGoalsCenter(
    vm: GameViewModel,
    state: GameState,
    meta: PlayerMeta,
    modifier: Modifier = Modifier
) {
    val missions = vm.missions()
    val achievements = vm.achievements()
    val visibleMissions = missions.sortedBy { mission ->
        when {
            mission.completed && !mission.claimed -> 0
            !mission.claimed -> 1
            else -> 2
        }
    }
    val visibleAchievements = achievements.sortedBy { achievement ->
        when {
            achievement.unlocked && !achievement.claimed -> 0
            !achievement.claimed -> 1
            else -> 2
        }
    }
    val missionDone = missions.count { it.claimed }
    val missionReady = missions.count { it.completed && !it.claimed }
    val achievementDone = achievements.count { it.claimed }
    val achievementReady = achievements.count { it.unlocked && !it.claimed }
    val dynasty = DynastyProgression.status(state, meta)

    LazyColumn(
        modifier.fillMaxSize(),
        contentPadding = PaddingValues(16.dp, 18.dp, 16.dp, 30.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        item {
            Column {
                Text("COMMAND CENTER", color = EmpireColors.TextPrimary, fontSize = 27.sp, fontWeight = FontWeight.Black)
                Text("Daily, weekly and long-term objectives", color = EmpireColors.TextSecondary, fontSize = 11.sp)
            }
        }

        item {
            Surface(
                color = EmpireColors.Cyan.copy(alpha = .08f),
                shape = RoundedCornerShape(24.dp),
                modifier = Modifier.fillMaxWidth().border(1.dp, EmpireColors.Cyan.copy(alpha = .22f), RoundedCornerShape(24.dp))
            ) {
                Column(Modifier.padding(16.dp)) {
                    Text("CAMPAIGN STATUS", color = EmpireColors.Cyan, fontSize = 10.sp, fontWeight = FontWeight.Black, letterSpacing = 1.5.sp)
                    Spacer(Modifier.height(5.dp))
                    Text("Dynasty Rank ${dynasty.rank.level}", color = EmpireColors.TextPrimary, fontSize = 20.sp, fontWeight = FontWeight.Black)
                    Text(dynasty.rank.title, color = EmpireColors.GoldBright, fontSize = 11.sp, fontWeight = FontWeight.Bold)
                    Spacer(Modifier.height(12.dp))
                    LinearProgressIndicator(
                        progress = { dynasty.progress.coerceIn(0f, 1f) },
                        modifier = Modifier.fillMaxWidth().height(6.dp),
                        color = EmpireColors.Cyan,
                        trackColor = EmpireColors.SurfaceHigh
                    )
                    Spacer(Modifier.height(8.dp))
                    Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                        GoalStat("MISSIONS", "$missionDone/${missions.size}", missionReady)
                        GoalStat("ACHIEVEMENTS", "$achievementDone/${achievements.size}", achievementReady)
                        GoalStat("STREAK", "${meta.streakDays}D", 0)
                    }
                }
            }
        }

        item {
            val claimable = vm.canClaimDaily()
            Surface(
                color = EmpireColors.Gold.copy(alpha = .10f),
                shape = RoundedCornerShape(22.dp),
                modifier = Modifier.fillMaxWidth().border(1.dp, EmpireColors.Gold.copy(alpha = .24f), RoundedCornerShape(22.dp))
            ) {
                Column(Modifier.padding(16.dp)) {
                    Text("DAILY DROP", color = EmpireColors.Gold, fontSize = 10.sp, fontWeight = FontWeight.Black, letterSpacing = 1.5.sp)
                    Text("${meta.streakDays} day streak", color = EmpireColors.TextPrimary, fontSize = 20.sp, fontWeight = FontWeight.Black)
                    Text(
                        if (claimable) "Reward ready. Keep the streak alive." else "Today's reward secured.",
                        color = EmpireColors.TextSecondary,
                        fontSize = 10.sp
                    )
                    Spacer(Modifier.height(11.dp))
                    Button(
                        onClick = { vm.claimDaily() },
                        enabled = claimable,
                        modifier = Modifier.fillMaxWidth().height(48.dp),
                        shape = RoundedCornerShape(14.dp)
                    ) {
                        Text(if (claimable) "CLAIM DAILY REWARD" else "CLAIMED TODAY", fontWeight = FontWeight.Black, fontSize = 10.sp)
                    }
                }
            }
        }

        item {
            GoalSectionHeader("WEEKLY OPERATION", "Rotating objective with premium rewards")
        }
        item { ChallengeDock(vm, Modifier.fillMaxWidth()) }

        item {
            GoalSectionHeader("MISSIONS", if (missionReady > 0) "$missionReady reward${if (missionReady == 1) "" else "s"} ready" else "Short-term progression")
        }
        items(visibleMissions, key = { it.id }) { mission ->
            PremiumGoalCard(
                title = mission.title,
                subtitle = "+${mission.rewardGems} gems",
                progress = mission.fraction,
                stateLabel = when {
                    mission.claimed -> "DONE"
                    mission.completed -> "CLAIM"
                    else -> "${(mission.fraction * 100).toInt()}%"
                },
                enabled = mission.completed && !mission.claimed,
                accent = if (mission.completed && !mission.claimed) EmpireColors.Gold else EmpireColors.Cyan,
                onClick = { vm.claimMission(mission.id) }
            )
        }

        item {
            GoalSectionHeader(
                "ACHIEVEMENTS",
                if (achievementReady > 0) "$achievementReady unlocked reward${if (achievementReady == 1) "" else "s"}" else "Permanent campaign milestones"
            )
        }
        items(visibleAchievements, key = { it.id }) { achievement ->
            PremiumGoalCard(
                title = achievement.title,
                subtitle = achievement.description,
                progress = if (achievement.unlocked) 1f else 0f,
                stateLabel = when {
                    achievement.claimed -> "DONE"
                    achievement.unlocked -> "+${achievement.rewardGems} GEMS"
                    else -> "LOCKED"
                },
                enabled = achievement.unlocked && !achievement.claimed,
                accent = if (achievement.unlocked) EmpireColors.Violet else EmpireColors.TextSecondary,
                onClick = { vm.claimAchievement(achievement.id) }
            )
        }
    }
}

@Composable
private fun GoalStat(label: String, value: String, ready: Int) {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text(value, color = EmpireColors.TextPrimary, fontSize = 15.sp, fontWeight = FontWeight.Black)
        Text(label, color = EmpireColors.TextSecondary, fontSize = 8.sp, fontWeight = FontWeight.Bold)
        if (ready > 0) Text("$ready READY", color = EmpireColors.GoldBright, fontSize = 8.sp, fontWeight = FontWeight.Black)
    }
}

@Composable
private fun GoalSectionHeader(title: String, subtitle: String) {
    Column {
        Text(title, color = EmpireColors.TextPrimary, fontSize = 15.sp, fontWeight = FontWeight.Black, letterSpacing = 1.sp)
        Text(subtitle, color = EmpireColors.TextSecondary, fontSize = 10.sp)
    }
}

@Composable
private fun PremiumGoalCard(
    title: String,
    subtitle: String,
    progress: Float,
    stateLabel: String,
    enabled: Boolean,
    accent: Color,
    onClick: () -> Unit
) {
    Surface(
        color = if (enabled) accent.copy(alpha = .09f) else EmpireColors.Surface.copy(alpha = .91f),
        shape = RoundedCornerShape(20.dp),
        modifier = Modifier.fillMaxWidth().border(
            1.dp,
            if (enabled) accent.copy(alpha = .35f) else Color.White.copy(alpha = .05f),
            RoundedCornerShape(20.dp)
        )
    ) {
        Column(Modifier.padding(14.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text(title, color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black, fontSize = 14.sp, maxLines = 1, overflow = TextOverflow.Ellipsis)
                    Text(subtitle, color = EmpireColors.TextSecondary, fontSize = 10.sp, maxLines = 2, overflow = TextOverflow.Ellipsis)
                }
                TextButton(
                    onClick = onClick,
                    enabled = enabled,
                    modifier = Modifier.heightIn(min = 48.dp)
                ) {
                    Text(stateLabel, color = if (enabled) accent else EmpireColors.TextSecondary, fontWeight = FontWeight.Black, fontSize = 9.sp)
                }
            }
            Spacer(Modifier.height(6.dp))
            LinearProgressIndicator(
                progress = { progress.coerceIn(0f, 1f) },
                modifier = Modifier.fillMaxWidth().height(5.dp),
                color = accent,
                trackColor = EmpireColors.SurfaceHigh
            )
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/PremiumMotion.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun PowerCoreTrailField(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = if (reduced) {
        .18f
    } else {
        val transition = rememberInfiniteTransition(label = "coreTrails")
        val animated by transition.animateFloat(
            0f,
            1f,
            infiniteRepeatable(tween(if (lowPower) 4200 else 2600, easing = LinearEasing)),
            label = "trailPhase"
        )
        animated
    }
    Canvas(modifier) {
        val c = Offset(size.width / 2f, size.height / 2f)
        val r = size.minDimension * .34f
        val trailCount = if (lowPower) 9 else 18
        repeat(trailCount) { i ->
            val p = (phase + i / trailCount.toFloat()) % 1f
            val a = p * (Math.PI * 2.0).toFloat() + i * .31f
            val rr = r * (.55f + .45f * p)
            val pos = Offset(c.x + cos(a) * rr, c.y + sin(a) * rr)
            val alpha = (1f - p) * .8f
            drawCircle(
                color = if (i % 3 == 0) EmpireArtPalette.Cyan.copy(alpha = alpha) else EmpireArtPalette.Gold.copy(alpha = alpha),
                radius = 1.5f + (1f - p) * 4f,
                center = pos
            )
        }
        repeat(3) { ring ->
            drawCircle(
                color = EmpireArtPalette.Gold.copy(alpha = .18f - ring * .035f),
                radius = r * (.72f + ring * .18f),
                center = c,
                style = Stroke(2f + ring)
            )
        }
    }
}

/** Full-screen celebration field used by milestone, reward and prestige overlays. */
@Composable
fun CelebrationVfx(accentName: String, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val phase = if (reduced) {
        .22f
    } else {
        val transition = rememberInfiniteTransition(label = "celebration-$accentName")
        val animated by transition.animateFloat(
            0f,
            1f,
            infiniteRepeatable(tween(if (lowPower) 5200 else 3200, easing = LinearEasing)),
            label = "celebrationPhase"
        )
        animated
    }
    val accent = when (accentName.uppercase()) {
        "PRESTIGE", "ASCENSION" -> EmpireArtPalette.Violet
        "REWARDED", "REWARD" -> EmpireArtPalette.Cyan
        "MILESTONE" -> EmpireArtPalette.GoldHot
        "UNLOCK" -> EmpireArtPalette.Magenta
        else -> EmpireArtPalette.Gold
    }
    Canvas(modifier) {
        val c = Offset(size.width / 2f, size.height / 2f)
        val min = size.minDimension
        drawCircle(Brush.radialGradient(listOf(accent.copy(alpha = .24f), Color.Transparent), c, min * .62f), min * .62f, c)
        repeat(4) { ring ->
            val p = (phase + ring * .18f) % 1f
            drawCircle(accent.copy(alpha = (1f - p) * .34f), min * (.12f + p * .48f), c, style = Stroke(2f + ring))
        }
        val rays = if (lowPower) 12 else 24
        repeat(rays) { i ->
            val a = i * (2f * PI.toFloat() / rays) + phase * .35f
            val inner = min * .16f
            val outer = min * (.34f + (i % 4) * .035f)
            drawLine(
                color = if (i % 3 == 0) Color.White.copy(alpha = .42f) else accent.copy(alpha = .40f),
                start = Offset(c.x + cos(a) * inner, c.y + sin(a) * inner),
                end = Offset(c.x + cos(a) * outer, c.y + sin(a) * outer),
                strokeWidth = if (i % 3 == 0) 2.6f else 1.4f
            )
        }
        val sparks = if (lowPower) 18 else 42
        repeat(sparks) { i ->
            val a = i * 2f * PI.toFloat() / sparks + phase * 2f
            val wave = ((i * 37) % 100) / 100f
            val r = min * (.22f + .35f * wave)
            drawCircle(
                color = if (i % 5 == 0) Color.White.copy(alpha = .85f) else accent.copy(alpha = .72f),
                radius = if (i % 7 == 0) 3.2f else 1.7f,
                center = Offset(c.x + cos(a) * r, c.y + sin(a) * r)
            )
        }
    }
}

@Composable
fun EraTransitionOverlay(eraIndex: Int, visible: Boolean, modifier: Modifier = Modifier) {
    AnimatedVisibility(
        visible = visible,
        enter = fadeIn(tween(180)),
        exit = fadeOut(tween(520)),
        modifier = modifier
    ) {
        val context = LocalContext.current
        val reduced = MotionQuality.reducedMotion(context)
        val lowPower = MotionQuality.lowPowerMode(context)
        val era = EmpireEras.catalog.getOrElse(eraIndex.coerceAtLeast(0)) { EmpireEras.catalog.last() }
        val phase = if (reduced || lowPower) {
            .48f
        } else {
            val transition = rememberInfiniteTransition(label = "eraTransition")
            val animated by transition.animateFloat(
                0f,
                1f,
                infiniteRepeatable(tween(1250, easing = LinearEasing)),
                label = "eraPhase"
            )
            animated
        }
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1, 2 -> EmpireArtPalette.Cyan
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }

        Box(
            Modifier.fillMaxSize().background(EmpireColors.Void),
            contentAlignment = Alignment.Center
        ) {
            EraVistaAAA(era.index, Modifier.fillMaxSize())
            Box(
                Modifier.fillMaxSize().background(
                    Brush.verticalGradient(
                        listOf(
                            EmpireColors.Void.copy(alpha = .34f),
                            EmpireColors.DeepSpace.copy(alpha = .48f),
                            EmpireColors.Void.copy(alpha = .94f)
                        )
                    )
                )
            )
            Canvas(Modifier.fillMaxSize()) {
                val c = Offset(size.width / 2f, size.height * .43f)
                val min = size.minDimension
                repeat(if (lowPower) 2 else 4) { i ->
                    val p = (phase + i * .16f) % 1f
                    drawCircle(
                        accent.copy(alpha = (1f - p) * .42f),
                        min * (.10f + p * .52f),
                        c,
                        style = Stroke(2.5f + i)
                    )
                }
                val particleCount = if (lowPower) 14 else 34
                repeat(particleCount) { i ->
                    val a = i * (Math.PI * 2.0 / particleCount).toFloat() + phase * .7f
                    val spread = min * (.18f + ((i * 17) % 100) / 100f * .34f)
                    drawCircle(
                        color = if (i % 4 == 0) Color.White.copy(alpha = .78f) else accent.copy(alpha = .64f),
                        radius = if (i % 6 == 0) 3.2f else 1.8f,
                        center = Offset(c.x + cos(a) * spread, c.y + sin(a) * spread)
                    )
                }
            }

            Surface(
                color = EmpireColors.DeepSpace.copy(alpha = .84f),
                shape = RoundedCornerShape(28.dp),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 26.dp)
                    .border(1.dp, accent.copy(alpha = .48f), RoundedCornerShape(28.dp))
            ) {
                Column(
                    Modifier.padding(horizontal = 24.dp, vertical = 22.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        "ERA ${era.index + 1} OF ${EmpireEras.catalog.size}",
                        color = accent,
                        fontSize = 10.sp,
                        fontWeight = FontWeight.Black,
                        letterSpacing = 2.1.sp
                    )
                    Spacer(Modifier.height(5.dp))
                    Text(
                        era.icon,
                        color = Color.White,
                        fontSize = 38.sp,
                        fontWeight = FontWeight.Black
                    )
                    Spacer(Modifier.height(4.dp))
                    Text(
                        era.name,
                        color = Color.White,
                        fontSize = 28.sp,
                        fontWeight = FontWeight.Black,
                        textAlign = TextAlign.Center
                    )
                    Spacer(Modifier.height(7.dp))
                    Text(
                        era.subtitle,
                        color = EmpireColors.TextSecondary,
                        fontSize = 13.sp,
                        fontWeight = FontWeight.Bold,
                        textAlign = TextAlign.Center,
                        lineHeight = 18.sp
                    )
                    Spacer(Modifier.height(13.dp))
                    Text(
                        "NEW ECONOMIC HORIZON UNLOCKED",
                        color = accent,
                        fontSize = 9.sp,
                        fontWeight = FontWeight.Black,
                        letterSpacing = 1.4.sp
                    )
                }
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/PremiumSfx.kt
```kotlin
package com.zerotoempire.game

import android.content.Context
import android.media.AudioAttributes
import android.media.SoundPool
import java.io.File
import java.nio.ByteBuffer
import java.nio.ByteOrder
import kotlin.math.PI
import kotlin.math.exp
import kotlin.math.sin
import kotlin.random.Random

enum class PremiumSfxCue { TAP, PURCHASE, REWARD, MILESTONE, PRESTIGE, UI }

/**
 * Original resource-free sound design. Short WAVs are synthesized once into cache and loaded through
 * SoundPool for low-latency playback. No third-party audio files or copyrighted samples are used.
 */
class PremiumSfxEngine(context: Context) {
    private val appContext = context.applicationContext
    private val pool = SoundPool.Builder()
        .setMaxStreams(6)
        .setAudioAttributes(
            AudioAttributes.Builder()
                .setUsage(AudioAttributes.USAGE_GAME)
                .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
                .build()
        ).build()
    private val sounds = mutableMapOf<PremiumSfxCue, Int>()
    private val loaded = mutableSetOf<Int>()

    init {
        pool.setOnLoadCompleteListener { _, sampleId, status -> if (status == 0) synchronized(loaded) { loaded += sampleId } }
        PremiumSfxCue.entries.forEach { cue ->
            val file = ensureWave(cue)
            sounds[cue] = pool.load(file.absolutePath, 1)
        }
    }

    fun play(cue: PremiumSfxCue, volume: Float = 1f) {
        val id = sounds[cue] ?: return
        if (synchronized(loaded) { id !in loaded }) return
        val v = volume.coerceIn(0f, 1f)
        pool.play(id, v, v, 1, 0, 1f)
    }

    fun release() = pool.release()

    private fun ensureWave(cue: PremiumSfxCue): File {
        val dir = File(appContext.cacheDir, "premium_sfx").apply { mkdirs() }
        val file = File(dir, "${cue.name.lowercase()}_v2.wav")
        if (file.exists() && file.length() > 128) return file
        val pcm = synthesize(cue)
        writeWave(file, pcm, 22_050)
        return file
    }

    private fun synthesize(cue: PremiumSfxCue): ShortArray {
        val sampleRate = 22_050
        val duration = when (cue) {
            PremiumSfxCue.TAP -> .075
            PremiumSfxCue.UI -> .055
            PremiumSfxCue.PURCHASE -> .16
            PremiumSfxCue.REWARD -> .32
            PremiumSfxCue.MILESTONE -> .48
            PremiumSfxCue.PRESTIGE -> .72
        }
        val n = (sampleRate * duration).toInt()
        val random = Random(cue.ordinal * 7717 + 41)
        return ShortArray(n) { i ->
            val t = i.toDouble() / sampleRate
            val x = i.toDouble() / n
            val attack = (x / .06).coerceIn(0.0, 1.0)
            val decay = exp(-x * when (cue) {
                PremiumSfxCue.TAP, PremiumSfxCue.UI -> 9.0
                PremiumSfxCue.PURCHASE -> 6.0
                PremiumSfxCue.REWARD -> 4.5
                PremiumSfxCue.MILESTONE -> 3.8
                PremiumSfxCue.PRESTIGE -> 3.1
            })
            val env = attack * decay
            val signal = when (cue) {
                PremiumSfxCue.TAP -> {
                    val f = 820.0 - 260.0 * x
                    sin(2 * PI * f * t) * .78 + (random.nextDouble() * 2 - 1) * .08
                }
                PremiumSfxCue.UI -> sin(2 * PI * (1080.0 + 120.0 * x) * t) * .55
                PremiumSfxCue.PURCHASE -> {
                    sin(2 * PI * (310.0 + 520.0 * x) * t) * .55 +
                        sin(2 * PI * (620.0 + 750.0 * x) * t) * .32
                }
                PremiumSfxCue.REWARD -> chord(t, x, 523.25, 659.25, 783.99) * .62
                PremiumSfxCue.MILESTONE -> chord(t, x, 392.0, 523.25, 783.99) * .70 + sin(2 * PI * (150.0 + 300.0 * x) * t) * .18
                PremiumSfxCue.PRESTIGE -> {
                    val sweep = sin(2 * PI * (120.0 + 900.0 * x * x) * t) * .42
                    val shimmer = chord(t, x, 440.0, 659.25, 987.77) * .45
                    sweep + shimmer + (random.nextDouble() * 2 - 1) * .025
                }
            }
            (signal * env * 25_000.0).coerceIn(-32767.0, 32767.0).toInt().toShort()
        }
    }

    private fun chord(t: Double, x: Double, vararg frequencies: Double): Double =
        frequencies.mapIndexed { index, f -> sin(2 * PI * (f * (1.0 + x * .025 * (index + 1))) * t) }.average()

    private fun writeWave(file: File, pcm: ShortArray, sampleRate: Int) {
        val dataSize = pcm.size * 2
        val buffer = ByteBuffer.allocate(44 + dataSize).order(ByteOrder.LITTLE_ENDIAN)
        buffer.put("RIFF".toByteArray())
        buffer.putInt(36 + dataSize)
        buffer.put("WAVE".toByteArray())
        buffer.put("fmt ".toByteArray())
        buffer.putInt(16)
        buffer.putShort(1)
        buffer.putShort(1)
        buffer.putInt(sampleRate)
        buffer.putInt(sampleRate * 2)
        buffer.putShort(2)
        buffer.putShort(16)
        buffer.put("data".toByteArray())
        buffer.putInt(dataSize)
        pcm.forEach(buffer::putShort)
        file.writeBytes(buffer.array())
    }
}

object GameSfxBus {
    @Volatile private var engine: PremiumSfxEngine? = null

    @Synchronized
    fun attach(engine: PremiumSfxEngine) {
        this.engine?.release()
        this.engine = engine
    }

    fun play(cue: PremiumSfxCue, volume: Float = 1f) = engine?.play(cue, volume) ?: Unit

    @Synchronized
    fun detach(expected: PremiumSfxEngine) {
        if (engine !== expected) return
        engine?.release()
        engine = null
    }

    @Synchronized
    fun detach() {
        engine?.release()
        engine = null
    }
}
```

## File: src/main/java/com/zerotoempire/game/PremiumSprites.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

/**
 * High-detail, resolution-independent business sprites.
 * Every asset is built from several material/emissive/detail layers and evolves by level.
 */
@Composable
fun PremiumBusinessSprite(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val motion = rememberInfiniteTransition(label = "premiumSprite$id")
    val phase by motion.animateFloat(
        0f, 1f,
        infiniteRepeatable(tween(6200 + id * 170, easing = LinearEasing)),
        label = "phase"
    )
    val breathe by motion.animateFloat(
        .82f, 1f,
        infiniteRepeatable(tween(1650 + id * 80), RepeatMode.Reverse),
        label = "breathe"
    )

    val accent = spriteAccent(id)
    val stage = spriteStage(level)

    Box(
        modifier = modifier
            .size(iconSize)
            .background(
                Brush.radialGradient(
                    0f to accent.copy(alpha = .20f + stage * .025f),
                    .42f to EmpireColors.SurfaceHigh,
                    1f to EmpireColors.Void
                ),
                RoundedCornerShape(iconSize * .28f)
            )
    ) {
        Canvas(Modifier.fillMaxSize()) {
            val s = size.minDimension
            val center = Offset(s * .5f, s * .5f)

            // Atmospheric/material layers.
            drawCircle(accent.copy(alpha = (.08f + stage * .025f) * breathe), s * .47f, center)
            drawCircle(accent.copy(alpha = .24f + stage * .04f), s * .405f, center, style = Stroke(s * .018f))
            drawCircle(Color.White.copy(alpha = .055f), s * .365f, center, style = Stroke(s * .008f))
            drawSpriteFloor(accent)

            // Level-based prestige shell.
            if (stage >= 1) drawOrbitRing(accent, phase, .42f, .017f, 3)
            if (stage >= 2) drawOrbitRing(EmpireArtPalette.GoldHot, 1f - phase, .465f, .012f, 5)
            if (stage >= 3) drawPrestigeSpokes(accent, phase)
            if (stage >= 4) drawCrownArc(accent, phase)
            if (stage >= 5) drawAscendantHalo(accent, breathe)

            when (id.coerceIn(0, 9)) {
                0 -> premiumStreetStand(accent, stage)
                1 -> premiumCornerShop(accent, stage)
                2 -> premiumWorkshop(accent, stage, phase)
                3 -> premiumFactory(accent, stage, phase)
                4 -> premiumTechCompany(accent, stage, phase)
                5 -> premiumMegacity(accent, stage, phase)
                6 -> premiumMoonColony(accent, stage, phase)
                7 -> premiumMarsEmpire(accent, stage, phase)
                8 -> premiumDysonNetwork(accent, stage, phase)
                else -> premiumGalacticExchange(accent, stage, phase)
            }

            // Specular highlight unifies all sprites.
            drawArc(
                Color.White.copy(alpha = .20f),
                205f, 58f, false,
                Offset(s * .18f, s * .17f), Size(s * .64f, s * .64f),
                style = Stroke(s * .010f)
            )
        }
    }
}

private fun spriteAccent(id: Int): Color = when (id) {
    0 -> Color(0xFFFFC85A)
    1 -> Color(0xFFFFA95A)
    2 -> Color(0xFF66E7F5)
    3 -> Color(0xFF54C7FF)
    4 -> Color(0xFF9C8CFF)
    5 -> Color(0xFFC077FF)
    6 -> Color(0xFFE6F4FF)
    7 -> Color(0xFFFF6F68)
    8 -> Color(0xFFFFDF72)
    else -> Color(0xFFFF71D8)
}

private fun spriteStage(level: Int): Int = when {
    level >= 1000 -> 5
    level >= 500 -> 4
    level >= 250 -> 3
    level >= 100 -> 2
    level >= 25 -> 1
    else -> 0
}

private fun DrawScope.drawSpriteFloor(accent: Color) {
    val s = size.minDimension
    drawOval(
        Brush.radialGradient(listOf(accent.copy(alpha = .18f), Color.Transparent)),
        Offset(s * .17f, s * .72f), Size(s * .66f, s * .14f)
    )
    drawLine(accent.copy(alpha = .30f), Offset(s * .23f, s * .78f), Offset(s * .77f, s * .78f), s * .010f)
}

private fun DrawScope.drawOrbitRing(color: Color, phase: Float, radius: Float, stroke: Float, nodes: Int) {
    val s = size.minDimension
    val c = Offset(s * .5f, s * .5f)
    drawCircle(color.copy(alpha = .35f), s * radius, c, style = Stroke(s * stroke))
    repeat(nodes) { i ->
        val a = phase * PI.toFloat() * 2f + i * PI.toFloat() * 2f / nodes
        val p = Offset(c.x + cos(a) * s * radius, c.y + sin(a) * s * radius)
        drawCircle(Color.White.copy(alpha = .75f), s * .011f, p)
        drawCircle(color.copy(alpha = .28f), s * .025f, p)
    }
}

private fun DrawScope.drawPrestigeSpokes(color: Color, phase: Float) {
    val s = size.minDimension
    val c = Offset(s * .5f, s * .5f)
    repeat(8) { i ->
        val a = phase * PI.toFloat() * .35f + i * PI.toFloat() / 4f
        drawLine(
            color.copy(alpha = .44f),
            Offset(c.x + cos(a) * s * .39f, c.y + sin(a) * s * .39f),
            Offset(c.x + cos(a) * s * .48f, c.y + sin(a) * s * .48f),
            s * .009f
        )
    }
}

private fun DrawScope.drawCrownArc(color: Color, phase: Float) {
    val s = size.minDimension
    drawArc(
        EmpireArtPalette.GoldHot.copy(alpha = .66f),
        -40f + phase * 18f, 245f, false,
        Offset(s * .075f, s * .075f), Size(s * .85f, s * .85f), style = Stroke(s * .014f)
    )
    drawArc(
        color.copy(alpha = .42f),
        155f - phase * 14f, 165f, false,
        Offset(s * .11f, s * .11f), Size(s * .78f, s * .78f), style = Stroke(s * .010f)
    )
}

private fun DrawScope.drawAscendantHalo(color: Color, breathe: Float) {
    val s = size.minDimension
    drawCircle(
        Brush.radialGradient(listOf(Color.White.copy(alpha = .12f * breathe), color.copy(alpha = .08f), Color.Transparent)),
        s * .51f,
        Offset(s * .5f, s * .5f)
    )
}

private fun DrawScope.premiumStreetStand(c: Color, stage: Int) {
    val s = size.minDimension
    val roof = Path().apply {
        moveTo(s * .22f, s * .38f); lineTo(s * .31f, s * .27f); lineTo(s * .69f, s * .27f); lineTo(s * .78f, s * .38f); close()
    }
    drawPath(roof, Brush.verticalGradient(listOf(EmpireArtPalette.GoldHot, c)))
    drawRoundRect(EmpireArtPalette.Steel, Offset(s * .25f, s * .40f), Size(s * .50f, s * .31f), CornerRadius(s * .035f))
    drawRoundRect(c.copy(alpha = .85f), Offset(s * .28f, s * .44f), Size(s * .44f, s * .08f), CornerRadius(s * .018f))
    drawRect(EmpireArtPalette.Ink, Offset(s * .31f, s * .55f), Size(s * .38f, s * .13f))
    repeat(4) { i -> drawCircle(Color.White.copy(alpha = .8f), s * .010f, Offset(s * (.35f + i * .10f), s * .48f)) }
    if (stage >= 2) {
        drawLine(c, Offset(s * .22f, s * .73f), Offset(s * .78f, s * .73f), s * .018f)
        drawCircle(c, s * .026f, Offset(s * .24f, s * .72f)); drawCircle(c, s * .026f, Offset(s * .76f, s * .72f))
    }
}

private fun DrawScope.premiumCornerShop(c: Color, stage: Int) {
    val s = size.minDimension
    drawRoundRect(EmpireArtPalette.SteelBright, Offset(s * .22f, s * .34f), Size(s * .56f, s * .40f), CornerRadius(s * .04f))
    drawRect(EmpireArtPalette.Ink, Offset(s * .29f, s * .48f), Size(s * .42f, s * .24f))
    repeat(4) { i ->
        val x = s * (.245f + i * .135f)
        drawRoundRect(if (i % 2 == 0) c else EmpireArtPalette.GoldHot, Offset(x, s * .29f), Size(s * .105f, s * .12f), CornerRadius(s * .015f))
    }
    drawLine(c, Offset(s * .34f, s * .57f), Offset(s * .66f, s * .57f), s * .012f)
    if (stage >= 1) drawRoundRect(c.copy(alpha = .30f), Offset(s * .29f, s * .19f), Size(s * .42f, s * .07f), CornerRadius(s * .02f))
}

private fun DrawScope.premiumWorkshop(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    val center = Offset(s * .5f, s * .51f)
    drawCircle(EmpireArtPalette.SteelBright, s * .27f, center)
    drawCircle(c, s * .20f, center, style = Stroke(s * .065f))
    repeat(8) { i ->
        val a = phase * PI.toFloat() * .6f + i * PI.toFloat() / 4f
        drawLine(c, Offset(center.x + cos(a) * s * .21f, center.y + sin(a) * s * .21f), Offset(center.x + cos(a) * s * .31f, center.y + sin(a) * s * .31f), s * .045f)
    }
    drawCircle(EmpireArtPalette.Ink, s * .075f, center)
    drawCircle(Color.White.copy(alpha = .6f), s * .018f, Offset(s * .47f, s * .46f))
    if (stage >= 3) repeat(3) { i -> drawCircle(EmpireArtPalette.GoldHot, s * .014f, Offset(s * (.34f + i * .16f), s * .73f)) }
}

private fun DrawScope.premiumFactory(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    val body = Path().apply {
        moveTo(s*.17f,s*.72f); lineTo(s*.17f,s*.49f); lineTo(s*.34f,s*.37f); lineTo(s*.34f,s*.49f); lineTo(s*.52f,s*.37f); lineTo(s*.52f,s*.49f); lineTo(s*.79f,s*.49f); lineTo(s*.79f,s*.72f); close()
    }
    drawPath(body, Brush.verticalGradient(listOf(EmpireArtPalette.SteelBright, EmpireArtPalette.Steel)))
    drawPath(body, c.copy(alpha=.65f), style = Stroke(s*.018f))
    drawRect(EmpireArtPalette.SteelBright, Offset(s*.66f,s*.20f), Size(s*.085f,s*.30f))
    repeat(3){i-> drawRoundRect(c.copy(alpha=.82f), Offset(s*(.25f+i*.16f),s*.56f), Size(s*.09f,s*.09f), CornerRadius(s*.012f)) }
    val smokeY = s * (.16f - .035f * sin(phase * PI.toFloat()*2f))
    drawCircle(Color.White.copy(alpha=.10f), s*.055f, Offset(s*.70f, smokeY))
    if(stage>=2) drawLine(EmpireArtPalette.GoldHot,Offset(s*.20f,s*.74f),Offset(s*.77f,s*.74f),s*.016f)
}

private fun DrawScope.premiumTechCompany(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    drawRoundRect(EmpireArtPalette.Steel, Offset(s*.21f,s*.26f), Size(s*.58f,s*.48f), CornerRadius(s*.09f))
    drawRoundRect(c.copy(alpha=.25f), Offset(s*.25f,s*.30f), Size(s*.50f,s*.40f), CornerRadius(s*.07f))
    drawCircle(c, s*.115f, Offset(s*.5f,s*.5f), style=Stroke(s*.030f))
    drawCircle(Color.White.copy(alpha=.85f), s*.035f, Offset(s*.5f,s*.5f))
    repeat(8){i->
        val a=i*PI.toFloat()/4f+phase*PI.toFloat()*.25f
        drawLine(c.copy(alpha=.7f),Offset(s*.5f+cos(a)*s*.14f,s*.5f+sin(a)*s*.14f),Offset(s*.5f+cos(a)*s*.25f,s*.5f+sin(a)*s*.25f),s*.015f)
    }
    if(stage>=3) repeat(4){i->drawCircle(EmpireArtPalette.Magenta,s*.015f,Offset(s*(.31f+i*.125f),s*.66f))}
}

private fun DrawScope.premiumMegacity(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    val xs = listOf(.18f,.29f,.40f,.53f,.65f,.74f)
    val hs = listOf(.28f,.44f,.36f,.53f,.40f,.31f)
    xs.forEachIndexed { i,x ->
        val h = s * hs[i]
        val w = s * if(i==3) .12f else .095f
        drawRoundRect(Brush.verticalGradient(listOf(c.copy(alpha=.72f),EmpireArtPalette.Steel)),Offset(s*x,s*.75f-h),Size(w,h),CornerRadius(s*.018f))
        repeat(3){r->
            val glow = if((r+i)%2==0) EmpireArtPalette.Cyan else EmpireArtPalette.GoldHot
            drawCircle(glow.copy(alpha=.65f),s*.008f,Offset(s*(x+.03f),s*.70f-h+r*s*.075f))
        }
    }
    drawLine(c.copy(alpha=.45f),Offset(s*.16f,s*.75f),Offset(s*.84f,s*.75f),s*.012f)
    if(stage>=2){
        val x=s*(.30f+.40f*phase)
        drawLine(EmpireArtPalette.Cyan.copy(alpha=.7f),Offset(x,s*.20f),Offset(x,s*.72f),s*.008f)
    }
}

private fun DrawScope.premiumMoonColony(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    drawCircle(Color(0xFFDCE8F0),s*.265f,Offset(s*.48f,s*.50f))
    drawCircle(Color(0xFF8293A6).copy(alpha=.28f),s*.060f,Offset(s*.39f,s*.42f))
    drawCircle(Color(0xFF8293A6).copy(alpha=.22f),s*.040f,Offset(s*.57f,s*.57f))
    drawArc(c,205f,145f,false,Offset(s*.17f,s*.35f),Size(s*.65f,s*.30f),style=Stroke(s*.028f))
    repeat(3){i->drawCircle(EmpireArtPalette.Cyan,s*.020f,Offset(s*(.35f+i*.13f),s*.64f))}
    val shuttleX=s*(.25f+.50f*phase)
    drawLine(EmpireArtPalette.GoldHot,Offset(shuttleX,s*.26f),Offset(shuttleX+s*.055f,s*.245f),s*.018f)
    if(stage>=4) drawCircle(c.copy(alpha=.20f),s*.35f,Offset(s*.48f,s*.50f),style=Stroke(s*.012f))
}

private fun DrawScope.premiumMarsEmpire(c: Color, stage: Int, phase: Float) {
    val s = size.minDimension
    drawCircle(Color(0xFFD96054),s*.255f,Offset(s*.50f,s*.51f))
    drawCircle(Color(0xFF772E31).copy(alpha=.32f),s*.055f,Offset(s*.41f,s*.45f))
    drawArc(EmpireArtPalette.GoldHot,198f,168f,false,Offset(s*.14f,s*.35f),Size(s*.72f,s*.32f),style=Stroke(s*.030f))
    repeat(4){i->
        val a=phase*PI.toFloat()*2f+i*PI.toFloat()/2f
        drawCircle(c,s*.018f,Offset(s*.5f+cos(a)*s*.34f,s*.5f+sin(a)*s*.15f))
    }
    if(stage>=2){
        drawLine(c,Offset(s*.36f,s*.70f),Offset(s*.36f,s*.55f),s*.014f)
        drawLine(c,Offset(s*.64f,s*.70f),Offset(s*.64f,s*.55f),s*.014f)
    }
}

private fun DrawScope.premiumDysonNetwork(c: Color, stage: Int, phase: Float) {
    val s=size.minDimension
    val center=Offset(s*.5f,s*.5f)
    drawCircle(Brush.radialGradient(listOf(Color.White,EmpireArtPalette.GoldHot,Color(0xFFFF8B3D).copy(alpha=.2f))),s*.15f,center)
    drawCircle(c.copy(alpha=.18f),s*.23f,center)
    repeat(3){ring->
        drawCircle(c.copy(alpha=.65f-ring*.12f),s*(.26f+ring*.06f),center,style=Stroke(s*(.020f-ring*.003f)))
    }
    repeat(12){i->
        val a=phase*PI.toFloat()*2f+i*PI.toFloat()/6f
        val r=s*(.27f+(i%3)*.06f)
        val p=Offset(center.x+cos(a)*r,center.y+sin(a)*r)
        drawRoundRect(if(i%2==0)c else EmpireArtPalette.GoldHot,Offset(p.x-s*.018f,p.y-s*.010f),Size(s*.036f,s*.020f),CornerRadius(s*.006f))
    }
    if(stage>=5) drawCircle(Color.White.copy(alpha=.35f),s*.41f,center,style=Stroke(s*.008f))
}

private fun DrawScope.premiumGalacticExchange(c: Color, stage: Int, phase: Float) {
    val s=size.minDimension
    val center=Offset(s*.5f,s*.51f)
    drawCircle(Color.White,s*.035f,center)
    repeat(4){arm->
        val start=arm*PI.toFloat()/2f+phase*PI.toFloat()*2f
        repeat(13){j->
            val r=s*(.035f+j*.021f)
            val a=start+j*.23f
            val color=when(j%3){0->EmpireArtPalette.Cyan;1->c;else->EmpireArtPalette.Violet}
            drawCircle(color.copy(alpha=.82f-j*.025f),s*(.012f+j*.0006f),Offset(center.x+cos(a)*r,center.y+sin(a)*r*.62f))
        }
    }
    drawCircle(c.copy(alpha=.28f),s*.31f,center,style=Stroke(s*.018f))
    if(stage>=2) drawCircle(EmpireArtPalette.GoldHot.copy(alpha=.45f),s*.38f,center,style=Stroke(s*.010f))
    if(stage>=4) repeat(6){i->
        val a=i*PI.toFloat()/3f-phase*PI.toFloat()
        drawCircle(Color.White.copy(alpha=.9f),s*.012f,Offset(center.x+cos(a)*s*.42f,center.y+sin(a)*s*.22f))
    }
}
```

## File: src/main/java/com/zerotoempire/game/PremiumUiCompat.kt
```kotlin
package com.zerotoempire.game

/** Legacy shared tab type still referenced by reusable art components. */
enum class GameTab { EMPIRE, MANAGERS, UPGRADES, GOALS }

/** Readability alias used by the premium UI. */
val BulkQuote.cost: Double
    get() = totalCost
```

## File: src/main/java/com/zerotoempire/game/PrivacyConsentManager.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity
import com.google.android.ump.ConsentInformation
import com.google.android.ump.ConsentRequestParameters
import com.google.android.ump.UserMessagingPlatform
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

/** Central privacy gate for every ad format. */
class PrivacyConsentManager(private val activity: Activity) {
    private val consentInformation: ConsentInformation = UserMessagingPlatform.getConsentInformation(activity)

    fun gather(onComplete: (canRequestAds: Boolean, error: String?) -> Unit) {
        val params = ConsentRequestParameters.Builder().build()
        consentInformation.requestConsentInfoUpdate(
            activity,
            params,
            {
                UserMessagingPlatform.loadAndShowConsentFormIfRequired(activity) { formError ->
                    publish(consentInformation.canRequestAds())
                    onComplete(consentInformation.canRequestAds(), formError?.message)
                }
            },
            { requestError ->
                publish(consentInformation.canRequestAds())
                onComplete(consentInformation.canRequestAds(), requestError.message)
            }
        )
    }

    fun canRequestAds(): Boolean = consentInformation.canRequestAds()

    fun isPrivacyOptionsRequired(): Boolean =
        consentInformation.privacyOptionsRequirementStatus == ConsentInformation.PrivacyOptionsRequirementStatus.REQUIRED

    fun showPrivacyOptions(onClosed: (String?) -> Unit = {}) {
        UserMessagingPlatform.showPrivacyOptionsForm(activity) { error ->
            publish(consentInformation.canRequestAds())
            onClosed(error?.message)
        }
    }

    private fun publish(value: Boolean) { _adsAllowed.value = value }

    companion object {
        private val _adsAllowed = MutableStateFlow(false)
        val adsAllowed: StateFlow<Boolean> = _adsAllowed.asStateFlow()
    }
}
```

## File: src/main/java/com/zerotoempire/game/PrivacyPolicy.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

internal const val PRIVACY_POLICY_VERSION = "2026-09-18"

internal val PRIVACY_POLICY_SECTIONS: List<Pair<String, String>> = listOf(
    "Overview" to
        "ZERO → EMPIRE stores game progress and preferences on your device. The game does not require a developer account and does not send gameplay telemetry to a developer analytics server.",
    "Advertising and consent" to
        "The game uses Google User Messaging Platform to request and manage advertising consent where required. Google Mobile Ads may process device, advertising, diagnostic and interaction data according to Google's terms and your consent choices. Ad requests are disabled until the consent system reports that ads may be requested. Rewarded ads are optional. Interstitial ads, when enabled, are limited to natural progression breaks and can be disabled by the lifetime remove-ads purchase.",
    "Purchases" to
        "In-app purchases are processed by Google Play Billing. ZERO → EMPIRE receives purchase product identifiers and transaction tokens needed to deliver and restore entitlements. The game does not receive your full payment card details.",
    "Local game data" to
        "Progress, settings, purchase-delivery markers and limited local growth milestones are stored on-device. Android backup or device-transfer services may copy eligible local save data according to your Android and Google account settings.",
    "Diagnostics" to
        "The current build uses local Android logging and local preferences for development and gameplay diagnostics. It does not include a third-party developer analytics SDK.",
    "Your choices" to
        "You can use the in-game privacy options when Google requires an advertising privacy choice. You can also clear the app's local data through Android settings. Removing the app may remove local data, although platform backups can persist according to your Android backup settings.",
    "Third-party services" to
        "Google Play Billing, Google Mobile Ads and Google User Messaging Platform are Google services and may process data under Google's own privacy terms. Their behavior can vary by region, consent state and service configuration.",
    "Contact and updates" to
        "This policy applies to the current ZERO → EMPIRE Android release candidate. Material changes to data handling should be reflected here before a new production release. Privacy questions can be raised through the public ZERO → EMPIRE GitHub repository issue tracker."
)

@Composable
internal fun PrivacyPolicyDialog(onDismiss: () -> Unit) {
    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text("PRIVACY POLICY") },
        text = {
            Column(
                modifier = Modifier
                    .heightIn(max = 520.dp)
                    .verticalScroll(rememberScrollState())
            ) {
                Text("Version: $PRIVACY_POLICY_VERSION")
                PRIVACY_POLICY_SECTIONS.forEach { (heading, body) ->
                    Text("\n$heading\n$body")
                }
            }
        },
        confirmButton = {
            TextButton(onClick = onDismiss) { Text("CLOSE") }
        }
    )
}
```

## File: src/main/java/com/zerotoempire/game/ProgressionSystems.kt
```kotlin
package com.zerotoempire.game

import kotlin.math.floor
import kotlin.math.min
import kotlin.math.pow

data class Mission(
    val id: String,
    val title: String,
    val target: Double,
    val rewardGems: Int,
    val progress: Double = 0.0,
    val claimed: Boolean = false
) {
    val completed: Boolean get() = progress >= target
    val fraction: Float get() = min(1.0, progress / target).toFloat()
}

data class Achievement(
    val id: String,
    val title: String,
    val description: String,
    val unlocked: Boolean = false,
    val claimed: Boolean = false,
    val rewardGems: Int = 10
)

data class PlayerMeta(
    val gems: Int = 0,
    val totalTaps: Long = 0,
    val totalPurchases: Long = 0,
    val prestigeCount: Int = 0,
    val streakDays: Int = 0,
    val lastDailyClaimEpochDay: Long = -1L,
    val boostEndsAtMillis: Long = 0L,
    val claimedMissionIds: Set<String> = emptySet(),
    val claimedAchievementIds: Set<String> = emptySet(),
    val claimedChallengeIds: Set<String> = emptySet(),
    val challengeWeekKey: String = "",
    val challengeWeekTapBase: Long = 0L,
    val challengeWeekPurchaseBase: Long = 0L,
    val challengeWeekPrestigeBase: Int = 0,
    val onboardingCompleted: Boolean = false,
    val highestEraSeen: Int = 0,
    val adsRemoved: Boolean = false,
    val starterPackOwned: Boolean = false
)

object Progression {
    fun prestigeReward(lifetimeCash: Double): Int {
        if (lifetimeCash.isNaN() || lifetimeCash <= 0.0) return 0
        if (lifetimeCash == Double.POSITIVE_INFINITY) return Int.MAX_VALUE
        val reward = floor((lifetimeCash.coerceAtMost(EconomyMath.MAX_VALUE) / 1_000_000.0).pow(0.42))
        if (!reward.isFinite() || reward >= Int.MAX_VALUE.toDouble()) return Int.MAX_VALUE
        return reward.toInt().coerceAtLeast(0)
    }

    /**
     * Produces the next run after an ascension. Run-local cash, lifetime cash,
     * business levels and managers reset. Premium/permanent currency, upgrades,
     * accumulated legacy points and an already-earned timed boost survive.
     * Returns null when the run has not earned any additional legacy point.
     */
    fun prestigeReset(state: GameState): GameState? {
        val totalPoints = prestigeReward(state.lifetimeCash)
        if (totalPoints <= state.prestigePoints) return null
        return GameState(
            prestigePoints = totalPoints,
            gems = state.gems.coerceAtLeast(0),
            upgradeRanks = state.upgradeRanks,
            boostEndsAtMillis = state.boostEndsAtMillis.coerceAtLeast(0L)
        )
    }

    fun dailyReward(day: Int): Int = listOf(5, 7, 10, 15, 20, 30, 50)[day.coerceIn(0, 6)]

    fun missions(state: GameState, meta: PlayerMeta) = listOf(
        Mission("tap_50", "Tap 50 times", 50.0, 5, meta.totalTaps.toDouble(), "tap_50" in meta.claimedMissionIds),
        Mission("buy_25", "Buy 25 business levels", 25.0, 8, meta.totalPurchases.toDouble(), "buy_25" in meta.claimedMissionIds),
        Mission("earn_100k", "Earn 100K lifetime", 100_000.0, 12, state.lifetimeCash, "earn_100k" in meta.claimedMissionIds),
        Mission("prestige_1", "Ascend once", 1.0, 20, meta.prestigeCount.toDouble(), "prestige_1" in meta.claimedMissionIds)
    )

    fun achievements(state: GameState, meta: PlayerMeta): List<Achievement> {
        val ids = meta.claimedAchievementIds
        val totalLevels = state.businesses.sumOf { it.level.toLong() }
        val dynasty = DynastyProgression.status(state, meta).rank.level
        fun a(id: String, title: String, description: String, unlocked: Boolean, reward: Int) =
            Achievement(id, title, description, unlocked, id in ids, reward)

        return listOf(
            // First-session / early campaign
            a("first", "First Step", "Own your first asset", state.businesses.any { it.level > 0 }, 5),
            a("tap_500", "Hands On", "Tap the Power Core 500 times", meta.totalTaps >= 500L, 8),
            a("buy_100", "Builder", "Purchase 100 asset levels across your career", meta.totalPurchases >= 100L, 10),
            a("million", "Millionaire", "Earn 1M lifetime cash in a run", state.lifetimeCash >= 1e6, 10),
            a("century", "Industrial Machine", "Own 100 total asset levels in one run", totalLevels >= 100L, 15),
            a("manager_1", "Delegation", "Hire your first manager", state.hiredManagerIds.isNotEmpty(), 10),
            a("reborn", "Reborn", "Ascend for the first time", meta.prestigeCount > 0, 20),

            // Mid campaign
            a("tap_5000", "Capital Pulse", "Tap the Power Core 5,000 times", meta.totalTaps >= 5_000L, 15),
            a("buy_1000", "Mass Expansion", "Purchase 1,000 asset levels across your career", meta.totalPurchases >= 1_000L, 20),
            a("managers_5", "Executive Board", "Hire 5 managers in one run", state.hiredManagerIds.size >= 5, 20),
            a("levels_1000", "Vertical Integration", "Own 1,000 total asset levels in one run", totalLevels >= 1_000L, 25),
            a("prestige_10", "Iterative Empire", "Complete 10 ascensions", meta.prestigeCount >= 10, 30),
            a("streak_14", "Two Week Operator", "Maintain a 14 day login streak", meta.streakDays >= 14, 20),
            a("era_planetary", "Off-World Balance Sheet", "Reach the Planetary era", meta.highestEraSeen >= 4 || state.empireLevel >= 4, 25),

            // Long campaign
            a("tap_50000", "Human Metronome", "Tap the Power Core 50,000 times", meta.totalTaps >= 50_000L, 35),
            a("buy_10000", "Empire Logistics", "Purchase 10,000 asset levels across your career", meta.totalPurchases >= 10_000L, 40),
            a("prestige_50", "Legacy Engine", "Complete 50 ascensions", meta.prestigeCount >= 50, 50),
            a("streak_30", "Monthly Discipline", "Maintain a 30 day login streak", meta.streakDays >= 30, 40),
            a("era_galactic", "Galactic Balance Sheet", "Reach the Galactic era", meta.highestEraSeen >= 6 || state.empireLevel >= 6, 45),
            a("all_managers", "Board of Fourteen", "Hire every manager in one run", state.hiredManagerIds.size >= Managers.catalog.size, 60),

            // Dynasty ladder: persistent multi-month status targets
            a("dynasty_5", "Dynasty: Established", "Reach Dynasty Rank 5", dynasty >= 5, 15),
            a("dynasty_10", "Dynasty: Influential", "Reach Dynasty Rank 10", dynasty >= 10, 25),
            a("dynasty_20", "Dynasty: Dominant", "Reach Dynasty Rank 20", dynasty >= 20, 50),
            a("dynasty_30", "Dynasty: Sovereign", "Reach Dynasty Rank 30", dynasty >= 30, 75),
            a("dynasty_45", "Dynasty: Eternal", "Reach Dynasty Rank 45", dynasty >= 45, 120),
            a("dynasty_60", "Dynasty: Apex", "Reach the maximum Dynasty Rank 60", dynasty >= 60, 200),

            // Endgame
            a("prestige_250", "Century of Rebirths", "Complete 250 ascensions", meta.prestigeCount >= 250, 125),
            a("streak_90", "Quarter-Year Empire", "Maintain a 90 day login streak", meta.streakDays >= 90, 100),
            a("beyond_everything", "Beyond Everything", "Reach the Transcendent era and the current frontier of Zero → Empire", state.lifetimeCash >= 1e30 || meta.highestEraSeen >= EmpireEras.catalog.lastIndex, 150)
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/PurchaseCreditLedger.kt
```kotlin
package com.zerotoempire.game

/** Pure idempotence ledger for economy credits keyed by store transaction id. */
class PurchaseCreditLedger(initial: Collection<String> = emptyList()) {
    private val credited = initial.filter { it.isNotBlank() }.toMutableSet()

    /** Returns true exactly once for each non-blank transaction id. */
    fun claim(transactionId: String): Boolean =
        transactionId.isNotBlank() && credited.add(transactionId)

    fun snapshot(): Set<String> = credited.toSet()
}
```

## File: src/main/java/com/zerotoempire/game/PurchaseImpactVfx.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

private const val WarmPulseFrameSize = 128
private const val WarmPulseColumns = 4
private const val WarmPulseFrameCount = 8
private const val WarmPulsePeakFrame = 4
private const val ConstructionDustPeakFrame = 3

/**
 * Short-lived feedback for successful asset purchases.
 * FX-06 provides the authored warm energy pulse while Canvas sparks preserve
 * scale-dependent punch without adding idle animation cost.
 */
@Composable
fun AssetPurchaseImpact(
    serial: Int,
    purchaseCount: Int,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_06_final).asImageBitmap()
    }
    val dustSheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_07_final).asImageBitmap()
    }
    val steamSheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_04_final).asImageBitmap()
    }
    val progress = remember { Animatable(1f) }

    LaunchedEffect(serial, reduced, lowPower) {
        if (serial <= 0) return@LaunchedEffect
        progress.snapTo(0f)
        progress.animateTo(
            1f,
            animationSpec = tween(
                durationMillis = when {
                    reduced -> 180
                    lowPower -> 360
                    else -> 520
                }
            )
        )
    }

    if (serial <= 0 || progress.value >= .999f) return
    val p = progress.value
    val intensity = when {
        purchaseCount >= 100 -> 1f
        purchaseCount >= 25 -> .82f
        purchaseCount >= 10 -> .68f
        else -> .52f
    }

    Canvas(modifier) {
        val center = Offset(size.width * .18f, size.height * .50f)
        val min = size.minDimension
        val alpha = (1f - p) * intensity
        val frame = when {
            reduced -> WarmPulsePeakFrame
            lowPower -> ((p * 4f).toInt().coerceIn(0, 3) * 2).coerceAtMost(WarmPulseFrameCount - 1)
            else -> (p * WarmPulseFrameCount).toInt().coerceIn(0, WarmPulseFrameCount - 1)
        }
        val pulseSize = (min * (.34f + intensity * .16f)).toInt().coerceAtLeast(1)
        val pulseOffset = IntOffset(
            x = (center.x - pulseSize / 2f).toInt(),
            y = (center.y - pulseSize / 2f).toInt()
        )

        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (frame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = pulseOffset,
            dstSize = IntSize(pulseSize, pulseSize),
            alpha = if (reduced) intensity * .72f else intensity
        )

        val dustFrame = when {
            reduced -> ConstructionDustPeakFrame
            lowPower -> ((p * 4f).toInt().coerceIn(0, 3) * 2).coerceAtMost(WarmPulseFrameCount - 1)
            else -> (p * WarmPulseFrameCount).toInt().coerceIn(0, WarmPulseFrameCount - 1)
        }
        val dustSize = (min * (.42f + intensity * .14f)).toInt().coerceAtLeast(1)
        drawImage(
            image = dustSheet,
            srcOffset = IntOffset(
                x = (dustFrame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (dustFrame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = IntOffset(
                x = (center.x - dustSize / 2f).toInt(),
                y = (center.y - dustSize * .36f).toInt()
            ),
            dstSize = IntSize(dustSize, dustSize),
            alpha = if (reduced) intensity * .48f else intensity * .76f
        )

        val steamFrame = when {
            reduced -> 3
            lowPower -> ((p * 4f).toInt().coerceIn(0, 3) * 2).coerceAtMost(WarmPulseFrameCount - 1)
            else -> (p * WarmPulseFrameCount).toInt().coerceIn(0, WarmPulseFrameCount - 1)
        }
        val steamSize = (min * (.30f + intensity * .10f)).toInt().coerceAtLeast(1)
        drawImage(
            image = steamSheet,
            srcOffset = IntOffset(
                x = (steamFrame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (steamFrame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = IntOffset(
                x = (center.x + min * .08f - steamSize / 2f).toInt(),
                y = (center.y - steamSize * .72f).toInt()
            ),
            dstSize = IntSize(steamSize, steamSize),
            alpha = if (reduced) intensity * .28f else (1f - p) * intensity * .48f
        )

        if (!reduced) {
            drawCircle(
                color = EmpireArtPalette.GoldHot.copy(alpha = alpha * .24f),
                radius = min * (.08f + p * .32f),
                center = center,
                style = Stroke(width = 2f + intensity * 1.5f)
            )

            val sparks = if (lowPower) 7 else 13
            repeat(sparks) { i ->
                val angle = i * (2f * PI.toFloat() / sparks) + .18f
                val distance = min * (.07f + p * (.22f + (i % 3) * .025f))
                val point = Offset(
                    center.x + cos(angle) * distance,
                    center.y + sin(angle) * distance
                )
                drawCircle(
                    color = if (i % 4 == 0) Color.White.copy(alpha = alpha) else EmpireArtPalette.Gold.copy(alpha = alpha * .86f),
                    radius = if (i % 4 == 0) 2.7f else 1.8f,
                    center = point
                )
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/PurchaseRecovery.kt
```kotlin
package com.zerotoempire.game

/** Pure purchase-recovery rules kept separate so Billing edge cases remain unit-testable. */
object PurchaseRecovery {
    /** Google Play transactions are identified by token; duplicate callbacks must be processed once. */
    fun <T> distinctTransactions(transactions: List<T>, token: (T) -> String): List<T> =
        transactions.distinctBy(token)

    fun extraConsumableGems(products: List<StoreProduct>): Int {
        val extraSmall = (products.count { it == StoreProduct.GEM_PACK_SMALL } - 1).coerceAtLeast(0)
        val extraMedium = (products.count { it == StoreProduct.GEM_PACK_MEDIUM } - 1).coerceAtLeast(0)
        return recoveredConsumableGemValue(extraSmall, extraMedium)
    }

    /** Saturating arithmetic keeps restore compensation representable even for pathological histories. */
    internal fun recoveredConsumableGemValue(extraSmall: Int, extraMedium: Int): Int {
        val recovered = extraSmall.coerceAtLeast(0).toLong() * 120L +
            extraMedium.coerceAtLeast(0).toLong() * 650L
        return recovered.coerceAtMost(Int.MAX_VALUE.toLong()).toInt()
    }

    /** Consumables are transactional: only one restore waiter may receive them after consumption. */
    fun deliveryForWaiter(products: List<StoreProduct>, waiterIndex: Int): List<StoreProduct> =
        if (waiterIndex == 0) products else products.filterNot { it.consumable }

    /**
     * A complete successful Play restore is authoritative for permanent ownership. A failed or
     * partial restore must remain non-destructive because absence may only reflect a transient
     * Billing failure rather than a revoked entitlement.
     */
    fun permanentOwned(
        product: StoreProduct,
        currentOwned: Boolean,
        restoredProducts: Set<StoreProduct>,
        authoritative: Boolean
    ): Boolean = product in restoredProducts || (!authoritative && currentOwned)
}

/**
 * List overload used by Billing restore. The Set member restores permanent entitlements,
 * Starter Pack, and one occurrence of each recovered consumable. We then credit only duplicate
 * consumable transactions that a Set cannot represent.
 */
fun GameViewModel.applyEntitlements(
    products: List<StoreProduct>,
    authoritativePermanentEntitlements: Boolean = false
) {
    applyEntitlements(products.toSet(), authoritativePermanentEntitlements)
    val extraGems = PurchaseRecovery.extraConsumableGems(products)
    if (extraGems > 0) grantGems(extraGems)
}
```

## File: src/main/java/com/zerotoempire/game/Retention.kt
```kotlin
package com.zerotoempire.game

import kotlin.math.min

data class RewardDay(val day: Int, val gems: Int, val multiplierMinutes: Int = 0, val special: String? = null)

object LoginCalendar {
    val sevenDay = listOf(
        RewardDay(1, 5), RewardDay(2, 7), RewardDay(3, 10, 5),
        RewardDay(4, 12), RewardDay(5, 15, 10), RewardDay(6, 20),
        RewardDay(7, 50, 30, "LEGENDARY CHEST")
    )
    fun rewardFor(streak: Int) = sevenDay[(streak.coerceAtLeast(1) - 1) % sevenDay.size]
}

data class ChestReward(val gems: Int, val boostMinutes: Int, val label: String)

object RewardChest {
    fun milestone(level: Int): ChestReward = when {
        level >= 1000 -> ChestReward(100, 60, "COSMIC VAULT")
        level >= 500 -> ChestReward(50, 30, "EMPIRE VAULT")
        level >= 100 -> ChestReward(20, 15, "GOLD VAULT")
        else -> ChestReward(5, 5, "SUPPLY DROP")
    }
}

data class OnboardingState(val step: Int = 0, val completed: Boolean = false) {
    fun advance(): OnboardingState {
        val next = min(step + 1, 5)
        return copy(step = next, completed = next >= 5)
    }
}

object OnboardingCopy {
    val steps = listOf(
        "Tap the core to generate your first capital.",
        "Buy your first asset. Assets generate income every second while you play.",
        "Scale assets to reach powerful milestone multipliers.",
        "Hire managers to boost production and keep their assets earning while you're away.",
        "Ascend when growth slows. Every legacy makes the next empire stronger."
    )
}
```

## File: src/main/java/com/zerotoempire/game/ReviewedCharacterLayer.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import androidx.compose.ui.unit.dp

private data class CharacterPlacement(
    val role: ReviewedCharacterRole,
    val action: ReviewedCharacterAction,
    val x: Dp,
    val y: Dp,
    val size: Dp,
    val phaseFrames: Int,
)

/**
 * Authored ambient population for the Ascendant city.
 *
 * The source assets are 4x4 atlases. This renderer crops one 256x256 cell per
 * actor and advances all actors from one shared 10 fps clock, keeping visual
 * density high without starting one independent infinite animation per sprite.
 */
@Composable
internal fun ReviewedCharacterLayer(
    eraIndex: Int,
    worldFrame: Int,
    reducedMotion: Boolean,
    modifier: Modifier = Modifier,
) {
    val context = LocalContext.current
    val lateEraScale = if (eraIndex >= 4) 1.08f else 1f

    val placements = remember {
        listOf(
            CharacterPlacement(ReviewedCharacterRole.OPERATOR, ReviewedCharacterAction.WORK, 34.dp, 306.dp, 45.dp, 0),
            CharacterPlacement(ReviewedCharacterRole.TECHNICIAN, ReviewedCharacterAction.WALK, 112.dp, 374.dp, 42.dp, 3),
            CharacterPlacement(ReviewedCharacterRole.LOGISTICS, ReviewedCharacterAction.WALK, 203.dp, 455.dp, 43.dp, 5),
            CharacterPlacement(ReviewedCharacterRole.ENGINEER, ReviewedCharacterAction.WORK, 286.dp, 332.dp, 46.dp, 7),
            CharacterPlacement(ReviewedCharacterRole.LOGISTICS, ReviewedCharacterAction.IDLE, 72.dp, 498.dp, 36.dp, 2),
            CharacterPlacement(ReviewedCharacterRole.OPERATOR, ReviewedCharacterAction.WALK, 245.dp, 520.dp, 37.dp, 6),
            CharacterPlacement(ReviewedCharacterRole.TECHNICIAN, ReviewedCharacterAction.WORK, 318.dp, 432.dp, 39.dp, 4),
            CharacterPlacement(ReviewedCharacterRole.ENGINEER, ReviewedCharacterAction.IDLE, 156.dp, 535.dp, 35.dp, 1),
        )
    }

    val atlases = remember {
        placements
            .map { it.role to it.action }
            .distinct()
            .associateWith { (role, action) ->
                ImageBitmap.imageResource(
                    context.resources,
                    reviewedCharacterRasterRes(role, action),
                )
            }
    }

    Box(modifier.fillMaxSize()) {
        placements.forEach { placement ->
            val frameCount = reviewedCharacterFrameCount(placement.action)
            val frame = if (reducedMotion) {
                placement.phaseFrames % frameCount
            } else {
                (worldFrame + placement.phaseFrames) % frameCount
            }
            val atlas = atlases.getValue(placement.role to placement.action)

            CharacterAtlasFrame(
                atlas = atlas,
                frame = frame,
                modifier = Modifier
                    .offset(placement.x, placement.y)
                    .size(placement.size * lateEraScale),
            )
        }
    }
}

@Composable
private fun CharacterAtlasFrame(
    atlas: ImageBitmap,
    frame: Int,
    modifier: Modifier,
) {
    Canvas(modifier) {
        val sourceFrame = frame.coerceIn(0, REVIEWED_CHARACTER_COLUMNS * REVIEWED_CHARACTER_ROWS - 1)
        val srcX = (sourceFrame % REVIEWED_CHARACTER_COLUMNS) * REVIEWED_CHARACTER_CELL_SIDE
        val srcY = (sourceFrame / REVIEWED_CHARACTER_COLUMNS) * REVIEWED_CHARACTER_CELL_SIDE
        val side = minOf(size.width, size.height).toInt().coerceAtLeast(1)
        val dstX = ((size.width - side) / 2f).toInt()
        val dstY = ((size.height - side) / 2f).toInt()

        drawOval(
            color = Color.Black.copy(alpha = .22f),
            topLeft = Offset(size.width * .23f, size.height * .78f),
            size = Size(size.width * .54f, size.height * .11f),
        )
        drawImage(
            image = atlas,
            srcOffset = IntOffset(srcX, srcY),
            srcSize = IntSize(REVIEWED_CHARACTER_CELL_SIDE, REVIEWED_CHARACTER_CELL_SIDE),
            dstOffset = IntOffset(dstX, dstY),
            dstSize = IntSize(side, side),
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/ReviewedMachineLayer.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp

/** Semantically reviewed FLUX machine masters, including run 68 stragglers, visible as era-specific production machinery. */
@Composable
internal fun ReviewedMachineLayer(eraIndex: Int, modifier: Modifier = Modifier) {
    val groups = listOf(
        intArrayOf(R.drawable.zte_machine_00_0_final, R.drawable.zte_machine_00_1_final, R.drawable.zte_machine_01_0_final, R.drawable.zte_machine_01_1_final),
        intArrayOf(R.drawable.zte_machine_02_0_final, R.drawable.zte_machine_02_1_final, R.drawable.zte_machine_03_0_final, R.drawable.zte_machine_03_1_final),
        intArrayOf(R.drawable.zte_machine_04_1_final, R.drawable.zte_machine_05_0_final, R.drawable.zte_machine_05_1_final, R.drawable.zte_machine_06_0_final, R.drawable.zte_machine_06_1_final),
        intArrayOf(R.drawable.zte_machine_07_0_final, R.drawable.zte_machine_07_1_final, R.drawable.zte_machine_08_0_final, R.drawable.zte_machine_08_1_final),
        intArrayOf(R.drawable.zte_machine_09_0_final, R.drawable.zte_machine_09_1_final, R.drawable.zte_machine_10_0_final),
        intArrayOf(R.drawable.zte_machine_10_1_final, R.drawable.zte_machine_11_0_final, R.drawable.zte_machine_11_1_final, R.drawable.zte_machine_12_1_final),
        intArrayOf(R.drawable.zte_machine_12_0_final, R.drawable.zte_machine_13_0_final, R.drawable.zte_machine_13_1_final),
    )
    val ids = groups[eraIndex.coerceIn(0, groups.lastIndex)]
    val x = listOf(18.dp, 94.dp, 188.dp, 270.dp)
    val y = listOf(280.dp, 360.dp, 430.dp, 500.dp)
    Box(modifier.fillMaxSize()) {
        ids.forEachIndexed { index, resId ->
            Image(
                painter = painterResource(resId),
                contentDescription = null,
                contentScale = ContentScale.Fit,
                modifier = Modifier.offset(x[index], y[index]).size(if (eraIndex >= 4) 54.dp else 48.dp),
            )
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/ReviewedTerrainLayer.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp

/** Strictly reviewed modular terrain from FLUX runs 52, 66, 68 and 69, visible in the active city stage. */
@Composable
internal fun ReviewedTerrainLayer(eraIndex: Int, modifier: Modifier = Modifier) {
    val groups = listOf(
        intArrayOf(R.drawable.zte_terrain_00_final, R.drawable.zte_terrain_01_final, R.drawable.zte_terrain_02_final, R.drawable.zte_terrain_03_final),
        intArrayOf(R.drawable.zte_terrain_04_final, R.drawable.zte_terrain_05_final, R.drawable.zte_terrain_06_final, R.drawable.zte_terrain_07_final),
        intArrayOf(R.drawable.zte_terrain_08_final, R.drawable.zte_terrain_09_final, R.drawable.zte_terrain_10_final, R.drawable.zte_terrain_11_final),
        intArrayOf(R.drawable.zte_terrain_12_final, R.drawable.zte_terrain_13_final),
    )
    val group = when { eraIndex <= 1 -> groups[0]; eraIndex <= 3 -> groups[1]; eraIndex <= 5 -> groups[2]; else -> groups[3] }
    Box(modifier.fillMaxSize()) {
        group.forEachIndexed { index, resId ->
            Image(
                painter = painterResource(resId),
                contentDescription = null,
                contentScale = ContentScale.Fit,
                modifier = Modifier.offset((14 + index * 82).dp, (610 + (index % 2) * 44).dp).size(92.dp),
            )
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/RewardedController.kt
```kotlin
package com.zerotoempire.game

import android.app.Activity
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.lifecycle.compose.collectAsStateWithLifecycle

/** Bridges provider-neutral gameplay reward requests to the AdMob gateway. */
@Composable
fun RewardedController(
    activity: Activity,
    adsAllowed: Boolean,
    vm: GameViewModel
) {
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val gateway = remember(activity) { AdMobRewardedGateway(activity.applicationContext) }

    LaunchedEffect(adsAllowed, meta.adsRemoved) {
        val enabled = adsAllowed && !meta.adsRemoved
        gateway.setEnabled(enabled)
        if (enabled) gateway.preload()
    }

    LaunchedEffect(activity, gateway, vm, adsAllowed, meta.adsRemoved) {
        vm.rewardedRequests.collect { placement ->
            if (!adsAllowed || meta.adsRemoved) {
                vm.onRewardedUnavailable(placement)
                return@collect
            }
            if (!gateway.isReady()) {
                gateway.preload()
                vm.onRewardedUnavailable(placement)
                return@collect
            }
            gateway.show(
                activity = activity,
                placement = placement,
                onReward = {
                    when (placement) {
                        RewardPlacement.DOUBLE_OFFLINE_EARNINGS -> vm.rewardDoubleOffline()
                        RewardPlacement.PROFIT_BOOST -> vm.rewardProfitBoost()
                        RewardPlacement.DAILY_BONUS,
                        RewardPlacement.EVENT_BONUS -> Unit
                    }
                },
                onClosed = {
                    // If no reward was earned, release any placement-specific request
                    // guard so the player can retry. Successful double-offline credit
                    // clears its reward before this callback, making this a harmless no-op.
                    vm.onRewardedUnavailable(placement)
                }
            )
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/RewardRequestGate.kt
```kotlin
package com.zerotoempire.game

/** Pure one-shot gate for a rewarded placement. */
class RewardRequestGate {
    private var pending = false

    fun request(): Boolean {
        if (pending) return false
        pending = true
        return true
    }

    fun consume(): Boolean {
        if (!pending) return false
        pending = false
        return true
    }

    fun release() {
        pending = false
    }

    fun isPending(): Boolean = pending
}
```

## File: src/main/java/com/zerotoempire/game/SfxRuntime.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.lifecycle.compose.collectAsStateWithLifecycle

@Composable
fun SfxRuntime(vm: GameViewModel) {
    val state = vm.state.collectAsStateWithLifecycle().value
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val celebration = vm.celebration.collectAsStateWithLifecycle().value

    val tracker = remember { SfxTracker() }

    LaunchedEffect(meta.totalTaps) {
        if (tracker.initialized && meta.totalTaps > tracker.taps) GameSfxBus.play(PremiumSfxCue.TAP, .72f)
        tracker.taps = meta.totalTaps
    }
    LaunchedEffect(meta.totalPurchases) {
        if (tracker.initialized && meta.totalPurchases > tracker.purchases) GameSfxBus.play(PremiumSfxCue.PURCHASE, .82f)
        tracker.purchases = meta.totalPurchases
    }
    LaunchedEffect(state.hiredManagerIds.size) {
        if (tracker.initialized && state.hiredManagerIds.size > tracker.managers) GameSfxBus.play(PremiumSfxCue.PURCHASE, .92f)
        tracker.managers = state.hiredManagerIds.size
    }
    LaunchedEffect(meta.streakDays, meta.claimedMissionIds.size, meta.claimedAchievementIds.size, meta.claimedChallengeIds.size) {
        val rewardScore = meta.streakDays + meta.claimedMissionIds.size + meta.claimedAchievementIds.size + meta.claimedChallengeIds.size
        if (tracker.initialized && rewardScore > tracker.rewardScore) GameSfxBus.play(PremiumSfxCue.REWARD, .90f)
        tracker.rewardScore = rewardScore
    }
    LaunchedEffect(meta.prestigeCount) {
        if (tracker.initialized && meta.prestigeCount > tracker.prestiges) GameSfxBus.play(PremiumSfxCue.PRESTIGE, 1f)
        tracker.prestiges = meta.prestigeCount
    }
    LaunchedEffect(celebration?.title, celebration?.accent) {
        if (celebration != null && celebration.title != tracker.celebrationTitle) {
            when (celebration.accent) {
                "MILESTONE" -> GameSfxBus.play(PremiumSfxCue.MILESTONE, 1f)
                "NEW ERA", "ERA", "PRESTIGE" -> GameSfxBus.play(PremiumSfxCue.PRESTIGE, 1f)
                else -> GameSfxBus.play(PremiumSfxCue.REWARD, .88f)
            }
            tracker.celebrationTitle = celebration.title
        }
    }

    LaunchedEffect(Unit) { tracker.initialized = true }
}

private class SfxTracker {
    var initialized = false
    var taps = 0L
    var purchases = 0L
    var managers = 0
    var rewardScore = 0
    var prestiges = 0
    var celebrationTitle: String? = null
}
```

## File: src/main/java/com/zerotoempire/game/SingularityLensPulse.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val LensFrameSize = 128
private const val LensColumns = 4
private const val LensFrameCount = 8

/** Apex singularity accent. Decorative animation stops under reduced motion/battery saver. */
@Composable
internal fun SingularityLensPulse(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_16_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) {
            while (true) {
                delay(125)
                frame = (frame + 1) % LensFrameCount
            }
        }
    }

    Canvas(modifier) {
        val effectSize = size.minDimension * .82f
        val destination = Offset(
            x = (size.width - effectSize) * .5f,
            y = (size.height - effectSize) * .5f
        )
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % LensColumns) * LensFrameSize,
                y = (frame / LensColumns) * LensFrameSize
            ),
            srcSize = IntSize(LensFrameSize, LensFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .78f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/StellarFlare.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val StellarFlareFrameSize = 128
private const val StellarFlareColumns = 4
private const val StellarFlareFrameCount = 8

/** Reality Engine plasma accent, frozen on its complete first frame under reduced motion. */
@Composable
internal fun StellarFlare(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_15_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(reducedMotion) {
        frame = 0
        if (!reducedMotion) {
            while (true) {
                delay(125)
                frame = (frame + 1) % StellarFlareFrameCount
            }
        }
    }

    Canvas(modifier) {
        val effectSize = size.minDimension * .74f
        val destination = Offset(
            x = (size.width - effectSize) * .5f,
            y = size.height * .12f
        )
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % StellarFlareColumns) * StellarFlareFrameSize,
                y = (frame / StellarFlareColumns) * StellarFlareFrameSize
            ),
            srcSize = IntSize(StellarFlareFrameSize, StellarFlareFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .72f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/UpgradeConstructionFlash.kt
```kotlin
package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val UpgradeFlashFrameSize = 128
private const val UpgradeFlashColumns = 4
private const val UpgradeFlashFrameCount = 8

/** One-shot authored flash replayed whenever a business level changes. */
@Composable
internal fun UpgradeConstructionFlash(trigger: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val sheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_08_final).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(UpgradeFlashFrameCount) }
    LaunchedEffect(trigger, reducedMotion) {
        if (trigger <= 0) return@LaunchedEffect
        if (reducedMotion) {
            frame = 3
            delay(140)
            frame = UpgradeFlashFrameCount
        } else {
            repeat(UpgradeFlashFrameCount) { index ->
                frame = index
                delay(125)
            }
            frame = UpgradeFlashFrameCount
        }
    }
    if (frame >= UpgradeFlashFrameCount) return
    Canvas(modifier) {
        val effectSize = size.minDimension * .62f
        val destination = Offset((size.width - effectSize) * .5f, size.height * .16f)
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                (frame % UpgradeFlashColumns) * UpgradeFlashFrameSize,
                (frame / UpgradeFlashColumns) * UpgradeFlashFrameSize
            ),
            srcSize = IntSize(UpgradeFlashFrameSize, UpgradeFlashFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = .84f
        )
    }
}
```

## File: src/main/java/com/zerotoempire/game/UpgradeProgression.kt
```kotlin
package com.zerotoempire.game

/**
 * Presentation/progression metadata for the permanent upgrade lab.
 * This layer derives entirely from existing upgrade ranks, so old saves remain compatible.
 */
data class UpgradeProgressNode(
    val id: String,
    val tier: Int,
    val rank: Int,
    val maxRank: Int,
    val progress: Float,
    val state: UpgradeNodeState
)

enum class UpgradeNodeState {
    LOCKED,
    AVAILABLE,
    IN_PROGRESS,
    MASTERED
}

object UpgradeProgression {
    const val TIER_COUNT = 4

    /**
     * Upgrade tiers are deliberately derived from catalog order. No new save fields are required.
     * Each tier becomes available after the previous tier has at least one invested rank.
     */
    fun nodes(state: GameState): List<UpgradeProgressNode> {
        val catalog = Upgrades.catalog
        return catalog.mapIndexed { index, upgrade ->
            val rank = (state.upgradeRanks[upgrade.id] ?: 0).coerceIn(0, upgrade.maxRank)
            val previousUnlocked = index == 0 || run {
                val previous = catalog[index - 1]
                (state.upgradeRanks[previous.id] ?: 0) > 0
            }
            val nodeState = when {
                rank >= upgrade.maxRank -> UpgradeNodeState.MASTERED
                rank > 0 -> UpgradeNodeState.IN_PROGRESS
                previousUnlocked -> UpgradeNodeState.AVAILABLE
                else -> UpgradeNodeState.LOCKED
            }
            UpgradeProgressNode(
                id = upgrade.id,
                tier = index + 1,
                rank = rank,
                maxRank = upgrade.maxRank,
                progress = if (upgrade.maxRank <= 0) 1f else rank.toFloat() / upgrade.maxRank.toFloat(),
                state = nodeState
            )
        }
    }

    fun overallProgress(state: GameState): Float {
        val nodes = nodes(state)
        val totalRanks = nodes.sumOf { it.maxRank }
        if (totalRanks <= 0) return 1f
        return (nodes.sumOf { it.rank }.toFloat() / totalRanks.toFloat()).coerceIn(0f, 1f)
    }

    fun masteredCount(state: GameState): Int = nodes(state).count { it.state == UpgradeNodeState.MASTERED }

    fun unlockedTier(state: GameState): Int = nodes(state)
        .filter { it.state != UpgradeNodeState.LOCKED }
        .maxOfOrNull { it.tier }
        ?: 1
}
```

## File: src/main/java/com/zerotoempire/game/UpgradeTreeScreen.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp

@Composable
fun PremiumUpgradeTreeScreen(vm: GameViewModel, state: GameState) {
    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        contentPadding = PaddingValues(16.dp, 18.dp, 16.dp, 30.dp),
        verticalArrangement = Arrangement.spacedBy(14.dp)
    ) {
        item { PremiumUpgradeTree(vm, state, Modifier.fillMaxWidth()) }
        item {
            Button(
                onClick = vm::activateProfitBoost,
                modifier = Modifier.fillMaxWidth().height(50.dp)
            ) {
                Text("⚡ WATCH REWARD  •  ×2 PROFITS", fontWeight = FontWeight.Black)
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/UpgradeTreeUi.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun PremiumUpgradeTree(
    vm: GameViewModel,
    state: GameState,
    modifier: Modifier = Modifier
) {
    val nodes = UpgradeProgression.nodes(state)
    val overall = UpgradeProgression.overallProgress(state)
    val mastered = UpgradeProgression.masteredCount(state)
    val unlockedTier = UpgradeProgression.unlockedTier(state)

    Column(modifier, verticalArrangement = Arrangement.spacedBy(0.dp)) {
        Surface(
            color = EmpireColors.Violet.copy(alpha = .12f),
            shape = RoundedCornerShape(24.dp),
            modifier = Modifier.fillMaxWidth().border(
                1.dp,
                EmpireColors.Violet.copy(alpha = .32f),
                RoundedCornerShape(24.dp)
            )
        ) {
            Column(Modifier.padding(16.dp)) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Column(Modifier.weight(1f)) {
                        Text(
                            "PERMANENT LAB",
                            color = EmpireColors.Violet,
                            fontSize = 10.sp,
                            fontWeight = FontWeight.Black,
                            letterSpacing = 1.7.sp
                        )
                        Text(
                            "EMPIRE TECHNOLOGY TREE",
                            color = EmpireColors.TextPrimary,
                            fontSize = 18.sp,
                            fontWeight = FontWeight.Black
                        )
                    }
                    Text(
                        "${state.gems} GEMS",
                        color = EmpireColors.GoldBright,
                        fontSize = 13.sp,
                        fontWeight = FontWeight.Black
                    )
                }
                Spacer(Modifier.height(11.dp))
                LinearProgressIndicator(
                    progress = { overall },
                    modifier = Modifier.fillMaxWidth().height(6.dp),
                    color = EmpireColors.Violet,
                    trackColor = EmpireColors.SurfaceHigh
                )
                Spacer(Modifier.height(7.dp))
                Row(Modifier.fillMaxWidth()) {
                    Text(
                        "TIER $unlockedTier/${UpgradeProgression.TIER_COUNT}",
                        color = EmpireColors.Cyan,
                        fontSize = 9.sp,
                        fontWeight = FontWeight.Black
                    )
                    Spacer(Modifier.weight(1f))
                    Text(
                        "$mastered/${nodes.size} MASTERED  •  ${(overall * 100).toInt()}%",
                        color = EmpireColors.TextSecondary,
                        fontSize = 9.sp,
                        fontWeight = FontWeight.Bold
                    )
                }
            }
        }

        nodes.forEachIndexed { index, node ->
            if (index > 0) UpgradeConnector(active = node.state != UpgradeNodeState.LOCKED)
            val upgrade = Upgrades.catalog.first { it.id == node.id }
            UpgradeTreeNode(
                upgradeName = upgrade.name,
                description = upgrade.description,
                gemCost = upgrade.gemCost,
                node = node,
                gems = state.gems,
                onUpgrade = { vm.buyUpgrade(node.id) }
            )
        }
    }
}

@Composable
private fun UpgradeConnector(active: Boolean) {
    Box(Modifier.fillMaxWidth().height(28.dp), contentAlignment = Alignment.Center) {
        Canvas(Modifier.size(18.dp, 28.dp)) {
            val color = if (active) EmpireColors.Violet else EmpireColors.TextSecondary.copy(alpha = .20f)
            drawLine(
                color = color.copy(alpha = if (active) .65f else .22f),
                start = Offset(size.width / 2f, 0f),
                end = Offset(size.width / 2f, size.height),
                strokeWidth = if (active) 4f else 2f
            )
            drawCircle(
                color = color,
                radius = if (active) 5f else 3f,
                center = Offset(size.width / 2f, size.height / 2f)
            )
        }
    }
}

@Composable
private fun UpgradeTreeNode(
    upgradeName: String,
    description: String,
    gemCost: Int,
    node: UpgradeProgressNode,
    gems: Int,
    onUpgrade: () -> Unit
) {
    val mastered = node.state == UpgradeNodeState.MASTERED
    val locked = node.state == UpgradeNodeState.LOCKED
    val canBuy = !mastered && !locked && gems >= gemCost
    val shortfall = (gemCost - gems).coerceAtLeast(0)
    val accent = when (node.state) {
        UpgradeNodeState.MASTERED -> EmpireColors.Cyan
        UpgradeNodeState.IN_PROGRESS -> EmpireColors.Violet
        UpgradeNodeState.AVAILABLE -> EmpireColors.Gold
        UpgradeNodeState.LOCKED -> EmpireColors.TextSecondary
    }
    val status = when (node.state) {
        UpgradeNodeState.MASTERED -> "MASTERED"
        UpgradeNodeState.IN_PROGRESS -> "IN DEVELOPMENT"
        UpgradeNodeState.AVAILABLE -> "AVAILABLE"
        UpgradeNodeState.LOCKED -> "LOCKED"
    }

    Surface(
        color = when (node.state) {
            UpgradeNodeState.MASTERED -> EmpireColors.Cyan.copy(alpha = .09f)
            UpgradeNodeState.IN_PROGRESS -> EmpireColors.Violet.copy(alpha = .10f)
            UpgradeNodeState.AVAILABLE -> EmpireColors.Gold.copy(alpha = .08f)
            UpgradeNodeState.LOCKED -> EmpireColors.Surface.copy(alpha = .58f)
        },
        shape = RoundedCornerShape(22.dp),
        modifier = Modifier.fillMaxWidth().border(
            1.dp,
            accent.copy(alpha = if (locked) .12f else .34f),
            RoundedCornerShape(22.dp)
        )
    ) {
        Column(Modifier.padding(15.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Box(
                    Modifier.size(42.dp)
                        .background(accent.copy(alpha = .14f), CircleShape)
                        .border(1.dp, accent.copy(alpha = .45f), CircleShape),
                    contentAlignment = Alignment.Center
                ) {
                    Text(
                        if (mastered) "✓" else "${node.tier}",
                        color = accent,
                        fontSize = 15.sp,
                        fontWeight = FontWeight.Black
                    )
                }
                Spacer(Modifier.size(11.dp))
                Column(Modifier.weight(1f)) {
                    Text(
                        "TIER ${node.tier}  •  $status",
                        color = accent,
                        fontSize = 9.sp,
                        fontWeight = FontWeight.Black,
                        letterSpacing = .8.sp
                    )
                    Text(
                        upgradeName,
                        color = if (locked) EmpireColors.TextSecondary else EmpireColors.TextPrimary,
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Black,
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis
                    )
                    Text(
                        description,
                        color = EmpireColors.TextSecondary,
                        fontSize = 10.sp,
                        maxLines = 2,
                        overflow = TextOverflow.Ellipsis
                    )
                }
            }

            Spacer(Modifier.height(12.dp))
            LinearProgressIndicator(
                progress = { node.progress.coerceIn(0f, 1f) },
                modifier = Modifier.fillMaxWidth().height(5.dp),
                color = accent,
                trackColor = EmpireColors.SurfaceHigh
            )
            Spacer(Modifier.height(6.dp))
            Row(Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                Text(
                    "RANK ${node.rank}/${node.maxRank}",
                    color = EmpireColors.TextSecondary,
                    fontSize = 9.sp,
                    fontWeight = FontWeight.Bold
                )
                Spacer(Modifier.weight(1f))
                Text(
                    when {
                        mastered -> "COMPLETE"
                        locked -> "INVEST IN PREVIOUS TIER"
                        shortfall > 0 -> "NEED $shortfall GEMS"
                        else -> "$gemCost GEMS"
                    },
                    color = if (canBuy) EmpireColors.GoldBright else EmpireColors.TextSecondary,
                    fontSize = 9.sp,
                    fontWeight = FontWeight.Black
                )
            }
            Spacer(Modifier.height(9.dp))
            Button(
                onClick = onUpgrade,
                enabled = canBuy,
                modifier = Modifier.fillMaxWidth().height(48.dp),
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.buttonColors(
                    containerColor = accent,
                    contentColor = EmpireColors.Void,
                    disabledContainerColor = accent.copy(alpha = .10f),
                    disabledContentColor = EmpireColors.TextSecondary
                )
            ) {
                Text(
                    when {
                        mastered -> "MASTERED"
                        locked -> "LOCKED"
                        shortfall > 0 -> "NEED $shortfall GEMS"
                        else -> "INVEST  •  $gemCost GEMS"
                    },
                    fontWeight = FontWeight.Black,
                    fontSize = 10.sp
                )
            }
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/ViralSystems.kt
```kotlin
package com.zerotoempire.game

data class ShareMilestone(
    val id: String,
    val headline: String,
    val body: String,
    val minimumLifetimeCash: Double,
    val rewardGems: Int
)

object ViralMilestones {
    val catalog = listOf(
        ShareMilestone("million", "I BUILT MY FIRST MILLION", "Started with $10. Now the empire begins.", 1e6, 3),
        ShareMilestone("billion", "BILLIONAIRE EMPIRE", "My idle empire just crossed $1B.", 1e9, 5),
        ShareMilestone("trillion", "THE TRILLION CLUB", "This economy is officially out of control.", 1e12, 8),
        ShareMilestone("planet", "PLANETARY TYCOON", "Earth was only the tutorial.", 1e15, 12),
        ShareMilestone("galaxy", "GALACTIC ECONOMY", "I turned nothing into a galactic empire.", 1e18, 20)
    )

    fun latestUnlocked(lifetimeCash: Double): ShareMilestone? =
        catalog.lastOrNull { lifetimeCash >= it.minimumLifetimeCash }
}

data class ReferralState(val invited: Int = 0, val qualified: Int = 0)

object ReferralRewards {
    fun gemsForQualifiedFriends(count: Int): Int = when {
        count >= 20 -> 500
        count >= 10 -> 200
        count >= 5 -> 75
        count >= 3 -> 30
        count >= 1 -> 10
        else -> 0
    }
}
```

## File: src/main/java/com/zerotoempire/game/ViralUi.kt
```kotlin
package com.zerotoempire.game

import android.content.Intent
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun ViralShareChip(state: GameState) {
    val milestone = ViralMilestones.latestUnlocked(state.lifetimeCash) ?: return
    val context = LocalContext.current
    Surface(
        onClick = {
            val text = buildString {
                append(milestone.headline)
                append("\n")
                append(milestone.body)
                append("\n\nZERO → EMPIRE")
            }
            val intent = Intent(Intent.ACTION_SEND).apply {
                type = "text/plain"
                putExtra(Intent.EXTRA_TEXT, text)
            }
            context.startActivity(Intent.createChooser(intent, "Share your empire"))
        },
        modifier = Modifier.heightIn(min = 48.dp),
        shape = RoundedCornerShape(50),
        color = EmpireColors.SurfaceHigh
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 10.dp, vertical = 5.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            MetaSprite(MetaSpriteKind.SHARE, size = 24.dp)
            Spacer(Modifier.width(6.dp))
            Text("SHARE MILESTONE", color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Black)
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/WorldBusinessVisual.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.Dp

/**
 * Sprite-first runtime bridge from authored production assets to the live world.
 *
 * Every authored business family resolves through canonicalBusinessRasterRes so
 * a single tested T0..T6 contract drives visible gameplay. Canvas drawing is kept
 * only for motion, mastery, upgrade and late-tier VFX layered around primary art.
 */
@Composable
internal fun WorldBusinessVisual(
    businessId: Int,
    level: Int,
    size: Dp,
    modifier: Modifier = Modifier
) {
    val tier = WorldSpriteRegistry.tierForLevel(level)
    val drawable = canonicalBusinessRasterRes(businessId, level)

    if (drawable != null) {
        val context = LocalContext.current
        val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
        val reveal = remember(businessId, tier) { Animatable(1f) }

        LaunchedEffect(businessId, tier, reducedMotion) {
            if (reducedMotion) {
                reveal.snapTo(1f)
            } else {
                reveal.snapTo(.88f)
                reveal.animateTo(
                    targetValue = 1f,
                    animationSpec = tween(durationMillis = 380, easing = FastOutSlowInEasing)
                )
            }
        }

        val authoredSize = size * (1f + tier.coerceAtMost(6) * .055f)
        Box(modifier = modifier.size(authoredSize)) {
            BusinessTierVfxBeforePrimary(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )
            Image(
                painter = painterResource(drawable),
                contentDescription = null,
                modifier = Modifier
                    .fillMaxSize()
                    .graphicsLayer {
                        scaleX = reveal.value
                        scaleY = reveal.value
                        alpha = .72f + reveal.value * .28f
                    },
                contentScale = ContentScale.Fit
            )
            BusinessTierVfxAfterPrimary(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )
            IndustrialBusinessFx(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )

            if (businessId in 0..3 && tier >= 1) {
                FoundryWorkerTraffic(
                    businessId = businessId,
                    modifier = Modifier.fillMaxSize()
                )
            }
            if (WorldSpriteRegistry.masteryForLevel(level)) {
                MasteryCrownShimmer(modifier = Modifier.fillMaxSize())
            }
            UpgradeConstructionFlash(trigger = level, modifier = Modifier.fillMaxSize())
        }
    } else {
        Box(modifier = modifier.size(size)) {
            BusinessTierVfxBeforePrimary(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )
            BusinessArtIcon(businessId, level, size)
            BusinessTierVfxAfterPrimary(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )
            IndustrialBusinessFx(
                businessId = businessId,
                tier = tier,
                modifier = Modifier.fillMaxSize()
            )
            UpgradeConstructionFlash(trigger = level, modifier = Modifier.fillMaxSize())
        }
    }
}

/**
 * Existing late-tier effects that visually sit behind their primary business art.
 * Keeping them separate from the raster resolver prevents procedural VFX from
 * becoming a fallback identity for businesses that already have authored sprites.
 */
@Composable
private fun BusinessTierVfxBeforePrimary(
    businessId: Int,
    tier: Int,
    modifier: Modifier = Modifier,
) {
    if (tier < 4) return
    when (businessId) {
        6 -> IncomePickupSparkle(modifier = modifier)
        7 -> ElectricArc(modifier = modifier)
        8 -> HologramScanSweep(modifier = modifier)
        9 -> DroneThruster(modifier = modifier)
        10 -> PhaseDistortion(modifier = modifier)
        11 -> OrbitalIonTrail(modifier = modifier)
        12 -> StellarFlare(modifier = modifier)
    }
}

/** Effects that intentionally sit above the authored primary art. */
@Composable
private fun BusinessTierVfxAfterPrimary(
    businessId: Int,
    tier: Int,
    modifier: Modifier = Modifier,
) {
    if (businessId == 13 && tier >= 4) {
        SingularityLensPulse(modifier = modifier)
    }
}
```

## File: src/main/java/com/zerotoempire/game/WorldMoneyFormat.kt
```kotlin
package com.zerotoempire.game

/** Shared callable formatter for world-scene surfaces that cannot access file-private UI helpers. */
internal val moneyV2: (Double) -> String = { value ->
    if (!value.isFinite()) {
        "∞"
    } else {
        val v = value.coerceAtLeast(0.0)
        when {
            v >= 1e30 -> String.format("%.2fN", v / 1e30)
            v >= 1e27 -> String.format("%.2fO", v / 1e27)
            v >= 1e24 -> String.format("%.2fSp", v / 1e24)
            v >= 1e21 -> String.format("%.2fSx", v / 1e21)
            v >= 1e18 -> String.format("%.2fQi", v / 1e18)
            v >= 1e15 -> String.format("%.2fQa", v / 1e15)
            v >= 1e12 -> String.format("%.2fT", v / 1e12)
            v >= 1e9 -> String.format("%.2fB", v / 1e9)
            v >= 1e6 -> String.format("%.2fM", v / 1e6)
            v >= 1e3 -> String.format("%.2fK", v / 1e3)
            else -> String.format("%.0f", v)
        }
    }
}
```

## File: src/main/java/com/zerotoempire/game/WorldSpriteRegistry.kt
```kotlin
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
            2 to 1 -> "art/source/era01/furnace_stall/t1/zte_business_02_t1_master.svg"
            3 to 0 -> "art/source/era01/assembly_hub/t0/zte_business_03_t0_master.svg"
            3 to 1 -> "art/source/era01/assembly_hub/t1/zte_business_03_t1_master.svg"
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
```

## File: src/main/java/com/zerotoempire/game/WorldTrafficArt.kt
```kotlin
package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlin.math.min

/** Semantically reviewed FLUX assets used as physical scenery in the active city stage. */
private val worldTrafficSprites = intArrayOf(
    R.drawable.zte_vehicle_00_final, R.drawable.zte_vehicle_01_final,
    R.drawable.zte_vehicle_02_final, R.drawable.zte_vehicle_03_final,
    R.drawable.zte_vehicle_04_final, R.drawable.zte_vehicle_05_final,
    R.drawable.zte_vehicle_06_final, R.drawable.zte_vehicle_07_final,
    R.drawable.zte_vehicle_08_final, R.drawable.zte_vehicle_09_final,
    R.drawable.zte_vehicle_10_final,
    R.drawable.zte_vehicle_11_final, R.drawable.zte_vehicle_12_final,
    R.drawable.zte_vehicle_13_final, R.drawable.zte_vehicle_14_final,
    R.drawable.zte_vehicle_15_final, R.drawable.zte_vehicle_16_final,
    R.drawable.zte_vehicle_17_final,
)

private val worldPropSprites = intArrayOf(
    R.drawable.zte_prop_02_b_final, R.drawable.zte_prop_04_a_final,
    R.drawable.zte_prop_05_a_final, R.drawable.zte_prop_05_b_final,
    R.drawable.zte_prop_06_a_final, R.drawable.zte_prop_06_b_final,
    R.drawable.zte_prop_07_a_final, R.drawable.zte_prop_07_b_final,
    R.drawable.zte_prop_08_a_final, R.drawable.zte_prop_08_b_final,
    R.drawable.zte_prop_09_a_final, R.drawable.zte_prop_09_b_final,
    R.drawable.zte_prop_10_a_final, R.drawable.zte_prop_10_b_final,
    R.drawable.zte_prop_11_a_final, R.drawable.zte_prop_11_b_final,
    R.drawable.zte_prop_12_a_final, R.drawable.zte_prop_12_b_final,
    R.drawable.zte_prop_13_a_final, R.drawable.zte_prop_13_b_final,
    R.drawable.zte_prop_00_a_final, R.drawable.zte_prop_00_b_final,
    R.drawable.zte_prop_01_a_final, R.drawable.zte_prop_01_b_final,
    R.drawable.zte_prop_02_a_final, R.drawable.zte_prop_03_a_final,
    R.drawable.zte_prop_03_b_final, R.drawable.zte_prop_04_b_final,
)

private data class TrafficPlacement(
    val x: Float,
    val y: Float,
    val width: Float,
    val travelX: Float,
    val travelY: Float,
    val phaseFrames: Int,
)

private val vehiclePlacements = listOf(
    TrafficPlacement(.45f,.37f,.090f, .06f,.035f, 0),
    TrafficPlacement(.54f,.43f,.105f,-.05f,.040f,17),
    TrafficPlacement(.43f,.50f,.112f, .07f,.050f,31),
    TrafficPlacement(.58f,.58f,.125f,-.08f,.055f,49),
    TrafficPlacement(.39f,.66f,.132f, .09f,.060f,68),
    TrafficPlacement(.63f,.73f,.145f,-.10f,.065f,83),
    TrafficPlacement(.34f,.79f,.090f, .08f,.055f,101),
    TrafficPlacement(.69f,.84f,.150f,-.07f,.050f,119),
    TrafficPlacement(.46f,.89f,.158f, .05f,.035f,137),
    TrafficPlacement(.57f,.94f,.090f,-.04f,.030f,151),
    TrafficPlacement(.51f,.33f,.088f, .03f,.020f,11),
    TrafficPlacement(.61f,.48f,.100f,-.04f,.025f,39),
    TrafficPlacement(.36f,.56f,.108f, .04f,.030f,57),
    TrafficPlacement(.66f,.68f,.118f,-.05f,.035f,76),
    TrafficPlacement(.49f,.81f,.126f, .05f,.035f,94),
    TrafficPlacement(.73f,.55f,.112f,-.03f,.020f,123),
    TrafficPlacement(.28f,.62f,.104f, .03f,.020f,142),
    TrafficPlacement(.78f,.63f,.110f,-.03f,.020f,158),
)

private val propPlacements = listOf(
    Triple(.12f,.38f,.085f), Triple(.83f,.40f,.080f), Triple(.17f,.43f,.088f),
    Triple(.16f,.48f,.095f), Triple(.82f,.51f,.100f), Triple(.13f,.59f,.110f),
    Triple(.86f,.61f,.105f), Triple(.18f,.69f,.120f), Triple(.82f,.71f,.125f),
    Triple(.12f,.78f,.130f), Triple(.88f,.80f,.130f), Triple(.20f,.86f,.140f),
    Triple(.80f,.87f,.145f), Triple(.10f,.91f,.135f), Triple(.90f,.92f,.135f),
    Triple(.25f,.94f,.125f), Triple(.75f,.95f,.125f), Triple(.31f,.84f,.105f),
    Triple(.71f,.76f,.105f), Triple(.91f,.68f,.110f), Triple(.08f,.47f,.078f),
    Triple(.92f,.48f,.078f), Triple(.07f,.56f,.082f), Triple(.93f,.58f,.082f),
    Triple(.09f,.66f,.088f), Triple(.91f,.74f,.090f), Triple(.14f,.73f,.086f),
    Triple(.86f,.45f,.082f),
)

@Composable
internal fun ReviewedWorldTraffic(
    worldFrame: Int,
    reducedMotion: Boolean,
    modifier: Modifier = Modifier,
) {
    val context = LocalContext.current
    val vehicles = remember { worldTrafficSprites.map { ImageBitmap.imageResource(context.resources, it) } }
    val props = remember { worldPropSprites.map { ImageBitmap.imageResource(context.resources, it) } }

    Box(modifier) {
        Canvas(Modifier.fillMaxSize()) {
            vehiclePlacements.forEachIndexed { i, placement ->
                val sample = trafficSample(
                    placement = placement,
                    worldFrame = worldFrame,
                    reducedMotion = reducedMotion,
                )
                drawSprite(
                    image = vehicles[i],
                    xFraction = sample.x,
                    yFraction = sample.y,
                    widthFraction = placement.width,
                    pivot = .72f,
                    shadow = true,
                    alpha = sample.alpha,
                )
            }

            // Props stay still: motion belongs to actors/traffic and remains visually legible.
            propPlacements.forEachIndexed { i, (x,y,w) ->
                drawSprite(props[i], x,y,w,.78f,false,1f)
            }
        }
    }
}

internal data class AmbientTrafficMotion(
    val deltaX: Float,
    val deltaY: Float,
    val alpha: Float,
)

internal fun ambientTrafficMotion(
    worldFrame: Int,
    phaseFrames: Int,
    travelX: Float,
    travelY: Float,
    reducedMotion: Boolean,
): AmbientTrafficMotion {
    if (reducedMotion || (travelX == 0f && travelY == 0f)) {
        return AmbientTrafficMotion(0f, 0f, .92f)
    }

    val cycleFrames = 180
    val normalizedFrame = Math.floorMod(worldFrame + phaseFrames, cycleFrames)
    val cycle = normalizedFrame.toFloat() / cycleFrames
    val centered = cycle - .5f
    val edgeFade = (min(cycle, 1f - cycle) * 10f).coerceIn(.25f, 1f)

    return AmbientTrafficMotion(
        deltaX = travelX * centered,
        deltaY = travelY * centered,
        alpha = .48f + edgeFade * .50f,
    )
}

private data class TrafficSample(
    val x: Float,
    val y: Float,
    val alpha: Float,
)

private fun trafficSample(
    placement: TrafficPlacement,
    worldFrame: Int,
    reducedMotion: Boolean,
): TrafficSample {
    val motion = ambientTrafficMotion(
        worldFrame = worldFrame,
        phaseFrames = placement.phaseFrames,
        travelX = placement.travelX,
        travelY = placement.travelY,
        reducedMotion = reducedMotion,
    )
    return TrafficSample(
        x = placement.x + motion.deltaX,
        y = placement.y + motion.deltaY,
        alpha = motion.alpha,
    )
}

private fun DrawScope.drawSprite(
    image: ImageBitmap,
    xFraction: Float,
    yFraction: Float,
    widthFraction: Float,
    pivot: Float,
    shadow: Boolean,
    alpha: Float,
) {
    val targetWidth=(size.width*widthFraction).toInt().coerceAtLeast(1)
    val targetHeight=(targetWidth*(image.height.toFloat()/image.width.toFloat())).toInt().coerceAtLeast(1)
    val x=(size.width*xFraction-targetWidth/2f).toInt()
    val y=(size.height*yFraction-targetHeight*pivot).toInt()
    if(shadow) {
        drawOval(
            Color.Black.copy(alpha=.28f * alpha),
            Offset(x+targetWidth*.12f,y+targetHeight*.73f),
            Size(targetWidth*.76f,targetHeight*.14f),
        )
    }
    drawImage(
        image=image,
        srcOffset=IntOffset.Zero,
        srcSize=IntSize(image.width,image.height),
        dstOffset=IntOffset(x,y),
        dstSize=IntSize(targetWidth,targetHeight),
        alpha=alpha,
    )
}
```

## File: src/test/java/com/zerotoempire/game/AmbientTrafficMotionTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class AmbientTrafficMotionTest {
    @Test
    fun `reduced motion freezes traffic in place`() {
        val sample = ambientTrafficMotion(
            worldFrame = 123,
            phaseFrames = 47,
            travelX = .12f,
            travelY = .07f,
            reducedMotion = true,
        )
        assertEquals(0f, sample.deltaX, 0f)
        assertEquals(0f, sample.deltaY, 0f)
        assertEquals(.92f, sample.alpha, 0f)
    }

    @Test
    fun `traffic motion repeats every 180 frames`() {
        val a = ambientTrafficMotion(31, 17, .12f, .07f, false)
        val b = ambientTrafficMotion(31 + 180, 17, .12f, .07f, false)
        assertEquals(a.deltaX, b.deltaX, 0f)
        assertEquals(a.deltaY, b.deltaY, 0f)
        assertEquals(a.alpha, b.alpha, 0f)
    }

    @Test
    fun `traffic alpha remains visible and bounded`() {
        repeat(180) { frame ->
            val sample = ambientTrafficMotion(frame, 0, .12f, .07f, false)
            assertTrue(sample.alpha in 0.60f..0.98f)
            assertTrue(sample.deltaX in -0.061f..0.061f)
            assertTrue(sample.deltaY in -0.036f..0.036f)
        }
    }
}
```

## File: src/test/java/com/zerotoempire/game/BillingDiagnosticsTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class BillingDiagnosticsTest {
    @Test
    fun diagnosticLineContainsOnlyTheApprovedFailureShape() {
        val line = BillingDiagnostic(
            BillingOperation.CONSUME,
            responseCode = -1,
            BillingFailureKind.SERVICE_DISCONNECTED
        ).toLogLine()

        assertEquals("operation=CONSUME responseCode=-1 category=SERVICE_DISCONNECTED", line)
        assertFalse(line.contains("token", ignoreCase = true))
        assertFalse(line.contains("order", ignoreCase = true))
        assertFalse(line.contains("product", ignoreCase = true))
    }

    @Test
    fun inMemorySummaryAggregatesWithoutTransactionData() {
        val diagnostics = InMemoryBillingDiagnostics()
        val failure = BillingDiagnostic(BillingOperation.RESTORE, -3, BillingFailureKind.NETWORK_ERROR)
        diagnostics.record(failure)
        diagnostics.record(failure)

        val summary = diagnostics.snapshot()
        val supportText = summary.toSupportText()

        assertEquals(1, summary.counts.size)
        assertEquals(2, summary.counts.single().count)
        assertTrue(supportText.contains("count=2"))
        assertFalse(supportText.contains("token", ignoreCase = true))
        assertFalse(supportText.contains("order", ignoreCase = true))
        assertFalse(supportText.contains("product", ignoreCase = true))
    }
}
```

## File: src/test/java/com/zerotoempire/game/BillingFailurePolicyTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class BillingFailurePolicyTest {
    @Test
    fun transientFailuresRequestReconnectionWithActionableMessages() {
        val disconnected = BillingFailurePolicy.resolve(BillingFailureKind.SERVICE_DISCONNECTED, "internal", "fallback")
        val unavailable = BillingFailurePolicy.resolve(BillingFailureKind.SERVICE_UNAVAILABLE, "internal", "fallback")
        val network = BillingFailurePolicy.resolve(BillingFailureKind.NETWORK_ERROR, "internal", "fallback")

        assertTrue(disconnected.shouldReconnect)
        assertTrue(unavailable.shouldReconnect)
        assertTrue(network.shouldReconnect)
        assertEquals("Google Play disconnected. Reopen the store and try again.", disconnected.message)
        assertEquals("Google Play is temporarily unavailable. Try again shortly.", unavailable.message)
        assertEquals("Network error while contacting Google Play. Check your connection and try again.", network.message)
    }

    @Test
    fun permanentFailureKeepsUsefulDetailWithoutRequestingRetry() {
        val detailed = BillingFailurePolicy.resolve(BillingFailureKind.OTHER, "Product is unavailable", "fallback")
        val fallback = BillingFailurePolicy.resolve(BillingFailureKind.OTHER, "", "Purchase failed")

        assertFalse(detailed.shouldReconnect)
        assertEquals("Product is unavailable", detailed.message)
        assertEquals("Purchase failed", fallback.message)
    }
}
```

## File: src/test/java/com/zerotoempire/game/BulkPurchaseTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.*
import org.junit.Test

class BulkPurchaseTest {
    @Test fun singlePurchaseKeepsExactNextCost() {
        val business = defaultBusinesses().first()

        assertEquals(business.baseCost, business.nextCost, 0.0)
        assertEquals(business.nextCost, BulkPurchase.cost(business, 1), 0.0)
        assertEquals(1, BulkPurchase.quote(business, business.nextCost, BuyMode.X1).count)
    }

    @Test fun bulkCostMatchesSequentialPurchases() {
        val b = defaultBusinesses().first().copy(level = 12)
        var sequential = 0.0
        repeat(25) { i -> sequential += b.baseCost * Math.pow(1.15, (b.level + i).toDouble()) }
        assertEquals(sequential, BulkPurchase.cost(b, 25), sequential * 1e-10)
    }

    @Test fun maxNeverOverspends() {
        val b = defaultBusinesses()[2].copy(level = 31)
        val cash = BulkPurchase.cost(b, 40) * 0.73
        val quote = BulkPurchase.quote(b, cash, BuyMode.MAX)
        assertTrue(quote.totalCost <= cash)
        assertTrue(BulkPurchase.cost(b, quote.count + 1) > cash)
    }

    @Test fun fixedQuoteKeepsRequestedCount() {
        val b = defaultBusinesses().first()
        val cash = BulkPurchase.cost(b, 25)
        val q = BulkPurchase.quote(b, cash, BuyMode.X25)
        assertEquals(25, q.count)
    }

    @Test fun milestonesCrossedAreDetectedInBulk() {
        assertEquals(listOf(10,25,50), BulkPurchase.crossedMilestones(8, 52))
    }
}
```

## File: src/test/java/com/zerotoempire/game/CanonicalBusinessRasterTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class CanonicalBusinessRasterTest {
    private val milestoneLevels = listOf(0, 10, 25, 50, 100, 250, 500, 1000)
    private val canonicalBusinesses = (0..13).toList()

    @Test
    fun `all authored businesses resolve every gameplay milestone`() {
        canonicalBusinesses.forEach { businessId ->
            milestoneLevels.forEach { level ->
                val resource = canonicalBusinessRasterRes(businessId, level)
                assertTrue("business=$businessId level=$level must resolve", resource != null && resource != 0)
            }
        }
    }

    @Test
    fun `final two gameplay milestones intentionally share T6`() {
        canonicalBusinesses.forEach { businessId ->
            assertEquals(
                canonicalBusinessRasterRes(businessId, 500),
                canonicalBusinessRasterRes(businessId, 1000)
            )
        }
    }

    @Test
    fun `ids outside authored business catalog remain unsupported`() {
        assertNull(canonicalBusinessRasterRes(-1, 500))
        assertNull(canonicalBusinessRasterRes(14, 500))
    }

    @Test
    fun `tiers produce seven distinct resources per canonical business`() {
        canonicalBusinesses.forEach { businessId ->
            val resources = listOf(0, 10, 25, 50, 100, 250, 500)
                .map { canonicalBusinessRasterRes(businessId, it) }
            assertEquals("business=$businessId", 7, resources.toSet().size)
        }
    }
}
```

## File: src/test/java/com/zerotoempire/game/CanonicalBusinessTierTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test

class CanonicalBusinessTierTest {
    @Test
    fun `eight gameplay milestones map monotonically to seven canonical tiers`() {
        val milestones = listOf(0, 10, 25, 50, 100, 250, 500, 1000)
        val expected = listOf(0, 1, 2, 3, 4, 5, 6, 6)
        assertEquals(expected, milestones.map(::canonicalBusinessTier))
    }

    @Test
    fun `tier boundaries are stable between milestones`() {
        val cases = mapOf(
            -1 to 0,
            9 to 0,
            10 to 1,
            24 to 1,
            25 to 2,
            49 to 2,
            50 to 3,
            99 to 3,
            100 to 4,
            249 to 4,
            250 to 5,
            499 to 5,
            500 to 6,
            999 to 6,
            1000 to 6,
            Int.MAX_VALUE to 6
        )
        cases.forEach { (level, tier) -> assertEquals("level=$level", tier, canonicalBusinessTier(level)) }
    }
}
```

## File: src/test/java/com/zerotoempire/game/CanonicalCharacterRasterTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Test

class CanonicalCharacterRasterTest {
    @Test
    fun `reviewed idle character roles resolve to packaged authored sprites`() {
        val expected = mapOf(
            ReviewedCharacterRole.OPERATOR to R.drawable.zte_chr_op_idle_final,
            ReviewedCharacterRole.TECHNICIAN to R.drawable.zte_chr_tech_idle_final,
            ReviewedCharacterRole.LOGISTICS to R.drawable.zte_chr_log_idle_final,
            ReviewedCharacterRole.ENGINEER to R.drawable.zte_chr_eng_idle_final,
        )

        expected.forEach { (role, resource) ->
            assertEquals(resource, reviewedCharacterIdleRasterRes(role))
            assertNotEquals(0, resource)
        }
    }

    @Test
    fun `all reviewed character action sheets resolve to distinct packaged assets`() {
        val resources = ReviewedCharacterRole.entries.flatMap { role ->
            ReviewedCharacterAction.entries.map { action ->
                reviewedCharacterRasterRes(role, action)
            }
        }
        assertEquals(
            ReviewedCharacterRole.entries.size * ReviewedCharacterAction.entries.size,
            resources.toSet().size,
        )
        resources.forEach { assertNotEquals(0, it) }
    }

    @Test
    fun `documented authored character actions keep their production frame counts`() {
        val expected = mapOf(
            ReviewedCharacterAction.IDLE to 6,
            ReviewedCharacterAction.WALK to 8,
            ReviewedCharacterAction.WORK to 10,
            ReviewedCharacterAction.CARRY to 8,
            ReviewedCharacterAction.REPAIR to 10,
            ReviewedCharacterAction.CELEBRATE to 8,
        )
        assertEquals(expected, ReviewedCharacterAction.entries.associateWith(::reviewedCharacterFrameCount))
    }

    @Test
    fun `character atlas contract matches production sheets`() {
        assertEquals(1024, REVIEWED_CHARACTER_ATLAS_SIDE)
        assertEquals(256, REVIEWED_CHARACTER_CELL_SIDE)
        assertEquals(4, REVIEWED_CHARACTER_COLUMNS)
        assertEquals(4, REVIEWED_CHARACTER_ROWS)
        assertEquals(
            REVIEWED_CHARACTER_ATLAS_SIDE,
            REVIEWED_CHARACTER_CELL_SIDE * REVIEWED_CHARACTER_COLUMNS,
        )
        assertEquals(
            REVIEWED_CHARACTER_ATLAS_SIDE,
            REVIEWED_CHARACTER_CELL_SIDE * REVIEWED_CHARACTER_ROWS,
        )
    }

    @Test
    fun `ambient population only loops actions documented as continuous`() {
        assertEquals(
            setOf(ReviewedCharacterAction.IDLE, ReviewedCharacterAction.WALK, ReviewedCharacterAction.WORK),
            ReviewedCharacterAction.entries.filter(::reviewedCharacterActionLoopsAmbiently).toSet(),
        )
    }
}
```

## File: src/test/java/com/zerotoempire/game/CanonicalFxRasterTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class CanonicalFxRasterTest {
    @Test
    fun `all manifest authored effects resolve to their production sprite ids`() {
        val expected = mapOf(
            CanonicalFx.WELDING_SPARK_BURST to R.drawable.zte_fx_00_final,
            CanonicalFx.SMALL_FURNACE_FLAME to R.drawable.zte_fx_01_final,
            CanonicalFx.LARGE_PLASMA_FLAME to R.drawable.zte_fx_02_final,
            CanonicalFx.INDUSTRIAL_SMOKE_PUFF to R.drawable.zte_fx_03_final,
            CanonicalFx.STEAM_VENT to R.drawable.zte_fx_04_final,
            CanonicalFx.CYAN_ENERGY_PULSE to R.drawable.zte_fx_05_final,
            CanonicalFx.WARM_ENERGY_PULSE to R.drawable.zte_fx_06_final,
            CanonicalFx.CONSTRUCTION_DUST_BURST to R.drawable.zte_fx_07_final,
            CanonicalFx.UPGRADE_CONSTRUCTION_FLASH to R.drawable.zte_fx_08_final,
            CanonicalFx.INCOME_PICKUP_SPARKLE to R.drawable.zte_fx_09_final,
            CanonicalFx.ELECTRIC_ARC to R.drawable.zte_fx_10_final,
            CanonicalFx.HOLOGRAM_SCAN_SWEEP to R.drawable.zte_fx_11_final,
            CanonicalFx.DRONE_THRUSTER to R.drawable.zte_fx_12_final,
            CanonicalFx.PHASE_DISTORTION to R.drawable.zte_fx_13_final,
            CanonicalFx.ORBITAL_ION_TRAIL to R.drawable.zte_fx_14_final,
            CanonicalFx.STELLAR_FLARE to R.drawable.zte_fx_15_final,
            CanonicalFx.SINGULARITY_LENS_PULSE to R.drawable.zte_fx_16_final,
            CanonicalFx.MASTERY_CROWN_SHIMMER to R.drawable.zte_fx_17_final,
        )

        assertEquals(CanonicalFx.entries.toSet(), expected.keys)
        expected.forEach { (effect, resource) ->
            assertEquals(resource, canonicalFxRasterRes(effect))
            assertNotEquals(0, resource)
        }
    }

    @Test
    fun `verified semantic effects never silently share one sprite`() {
        val resources = CanonicalFx.entries.map(::canonicalFxRasterRes)
        assertEquals(CanonicalFx.entries.size, resources.toSet().size)
        assertTrue(resources.all { it != 0 })
    }

    @Test
    fun `power core only uses authored pulse colors that actually exist`() {
        assertEquals(CanonicalFx.WARM_ENERGY_PULSE, powerCorePulseFx(0))
        assertEquals(CanonicalFx.WARM_ENERGY_PULSE, powerCorePulseFx(2))
        assertEquals(CanonicalFx.CYAN_ENERGY_PULSE, powerCorePulseFx(3))
        assertEquals(CanonicalFx.CYAN_ENERGY_PULSE, powerCorePulseFx(5))
        assertNull(powerCorePulseFx(6))
        assertNull(powerCorePulseFx(8))
        assertEquals(CanonicalFx.WARM_ENERGY_PULSE, powerCorePulseFx(9))
    }

    @Test
    fun `sprite sheet progress selects exactly one of eight frames`() {
        assertEquals(0, canonicalFxFrameIndex(-1f))
        assertEquals(0, canonicalFxFrameIndex(0f))
        assertEquals(0, canonicalFxFrameIndex(.124f))
        assertEquals(1, canonicalFxFrameIndex(.125f))
        assertEquals(3, canonicalFxFrameIndex(.499f))
        assertEquals(4, canonicalFxFrameIndex(.5f))
        assertEquals(7, canonicalFxFrameIndex(.999f))
        assertEquals(7, canonicalFxFrameIndex(1f))
        assertEquals(7, canonicalFxFrameIndex(2f))
    }
}
```

## File: src/test/java/com/zerotoempire/game/ChallengeRotationTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.*
import org.junit.Test
import java.time.LocalDate

class ChallengeRotationTest {
    @Test fun weeklyKeyIsStableInsideSameIsoWeek() {
        val a = ChallengeRotation.weeklyKey(LocalDate.of(2026, 8, 10))
        val b = ChallengeRotation.weeklyKey(LocalDate.of(2026, 8, 14))
        assertEquals(a, b)
    }

    @Test fun weeklyKeyChangesAcrossWeeks() {
        val a = ChallengeRotation.weeklyKey(LocalDate.of(2026, 8, 14))
        val b = ChallengeRotation.weeklyKey(LocalDate.of(2026, 8, 17))
        assertNotEquals(a, b)
    }

    @Test fun completedChallengeCannotLoseCompletion() {
        val date = LocalDate.of(2026, 8, 14)
        val key = ChallengeRotation.weeklyKey(date)
        val meta = PlayerMeta(
            totalTaps = 600,
            challengeWeekKey = key,
            challengeWeekTapBase = 0L
        )
        val challenge = ChallengeRotation.current(GameState(), meta, date).first { it.metric == ChallengeMetric.TAPS }
        assertTrue(challenge.completed)
        assertEquals(1f, challenge.fraction)
    }

    @Test fun claimedChallengeIsScopedToItsWeek() {
        val date = LocalDate.of(2026, 8, 14)
        val key = ChallengeRotation.weeklyKey(date)
        val meta = PlayerMeta(totalTaps = 600, claimedChallengeIds = setOf("$key:tap"))
        val current = ChallengeRotation.current(GameState(), meta, date).first { it.metric == ChallengeMetric.TAPS }
        val nextWeek = ChallengeRotation.current(GameState(), meta, date.plusWeeks(1)).first { it.metric == ChallengeMetric.TAPS }
        assertTrue(current.claimed)
        assertFalse(nextWeek.claimed)
    }

    @Test fun commandCenterPrioritizesClaimableThenActiveThenDone() {
        val active = challenge(id = "active", progress = 5.0)
        val done = challenge(id = "done", progress = 10.0, claimed = true)
        val claimable = challenge(id = "claimable", progress = 10.0)

        val ordered = ChallengeOrdering.forCommandCenter(listOf(done, active, claimable))

        assertEquals(listOf("claimable", "active", "done"), ordered.map { it.id })
    }

    @Test fun commandCenterOrderingIsStableInsideSamePriority() {
        val activeA = challenge(id = "active-a", progress = 1.0)
        val activeB = challenge(id = "active-b", progress = 2.0)
        val claimableA = challenge(id = "claimable-a", progress = 10.0)
        val claimableB = challenge(id = "claimable-b", progress = 12.0)
        val doneA = challenge(id = "done-a", progress = 10.0, claimed = true)
        val doneB = challenge(id = "done-b", progress = 11.0, claimed = true)

        val ordered = ChallengeOrdering.forCommandCenter(
            listOf(activeA, doneA, claimableA, activeB, claimableB, doneB)
        )

        assertEquals(
            listOf("claimable-a", "claimable-b", "active-a", "active-b", "done-a", "done-b"),
            ordered.map { it.id }
        )
    }

    @Test fun commandCenterOrderingDoesNotMutateSourceList() {
        val source = listOf(
            challenge(id = "done", progress = 10.0, claimed = true),
            challenge(id = "claimable", progress = 10.0),
            challenge(id = "active", progress = 1.0)
        )

        ChallengeOrdering.forCommandCenter(source)

        assertEquals(listOf("done", "claimable", "active"), source.map { it.id })
    }

    @Test fun prestigeWindowIncreasesWithEconomyScale() {
        assertTrue(BalanceGuard.recommendedPrestigeWindowSeconds(1e15) > BalanceGuard.recommendedPrestigeWindowSeconds(1e6))
    }

    private fun challenge(id: String, progress: Double, claimed: Boolean = false) = TimedChallenge(
        id = id,
        title = id,
        description = id,
        metric = ChallengeMetric.TAPS,
        target = 10.0,
        rewardGems = 1,
        progress = progress,
        claimed = claimed
    )
}
```

## File: src/test/java/com/zerotoempire/game/CinematicRuntimeTransitionPolicyTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class CinematicRuntimeTransitionPolicyTest {
    @Test fun compactScreensUseShorterImpact() {
        assertEquals(472, cinematicTransitionDurationMillis(compactScreen = true))
        assertEquals(552, cinematicTransitionDurationMillis(compactScreen = false))
    }

    @Test fun reducedMotionNeverRendersImpact() {
        assertFalse(shouldRenderCinematicTransition(reducedMotion = true, phase = 0f))
        assertFalse(shouldRenderCinematicTransition(reducedMotion = true, phase = .5f))
    }

    @Test fun completedImpactLeavesNoIdleCanvas() {
        assertTrue(shouldRenderCinematicTransition(reducedMotion = false, phase = .5f))
        assertFalse(shouldRenderCinematicTransition(reducedMotion = false, phase = .985f))
        assertFalse(shouldRenderCinematicTransition(reducedMotion = false, phase = 1f))
    }
}
```

## File: src/test/java/com/zerotoempire/game/ContentUnlocksTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class ContentUnlocksTest {
    @Test fun firstBusinessIsAlwaysVisible() {
        assertTrue(ContentUnlocks.isBusinessVisible(0, 0.0))
        assertFalse(ContentUnlocks.isBusinessVisible(1, 0.0))
    }

    @Test fun revealThresholdsAreStrictlyIncreasing() {
        val thresholds = defaultBusinesses().map { ContentUnlocks.thresholdForBusiness(it.id) }
        thresholds.zipWithNext().forEach { (a, b) -> assertTrue(b > a) }
    }

    @Test fun everyAssetRevealsBeforeItsBasePurchaseCost() {
        defaultBusinesses().forEach { business ->
            assertTrue(
                "${business.name} reveals too late",
                ContentUnlocks.thresholdForBusiness(business.id) <= business.baseCost
            )
        }
    }

    @Test fun endgameContentStaysHiddenUntilEarned() {
        assertFalse(ContentUnlocks.isBusinessVisible(10, 1e15))
        assertTrue(ContentUnlocks.isBusinessVisible(10, 5e17))
        assertFalse(ContentUnlocks.isBusinessVisible(13, 1e27))
        assertTrue(ContentUnlocks.isBusinessVisible(13, 3e28))
    }

    @Test fun managersFollowTheirBusinessReveal() {
        val early = GameState(lifetimeCash = 10.0)
        assertEquals(listOf(0), ContentUnlocks.visibleManagers(early).map { it.businessId })
    }

    @Test fun affordableUnhiredManagersArePrioritizedForPhoneUsability() {
        val state = GameState(
            cash = 600_000.0,
            lifetimeCash = 600_000.0,
            hiredManagerIds = setOf(0)
        )

        assertEquals(
            listOf(1, 2, 3, 4, 0),
            ContentUnlocks.visibleManagers(state).map { it.businessId }
        )
    }

    @Test fun managerPrioritizationNeverRevealsLockedContent() {
        val state = GameState(cash = Double.MAX_VALUE, lifetimeCash = 10.0)
        assertEquals(listOf(0), ContentUnlocks.visibleManagers(state).map { it.businessId })
    }

    @Test fun fullyProgressedEmpireHasNoHiddenBusiness() {
        val state = GameState(lifetimeCash = 1e31)
        assertNull(ContentUnlocks.nextHiddenBusiness(state))
        assertEquals(1f, ContentUnlocks.progressToNextUnlock(state))
    }
}
```

## File: src/test/java/com/zerotoempire/game/DynastyProgressionTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class DynastyProgressionTest {
    @Test
    fun ranks_are_monotonic_and_start_at_zero_requirement() {
        val ranks = DynastyProgression.ranks
        assertEquals(DynastyProgression.MAX_RANK, ranks.size)
        assertEquals(0.0, ranks.first().renownRequired, 0.0)
        assertEquals((1..DynastyProgression.MAX_RANK).toList(), ranks.map { it.level })
        ranks.zipWithNext().forEach { (a, b) ->
            assertTrue("rank thresholds must increase", b.renownRequired > a.renownRequired)
        }
    }

    @Test
    fun fresh_save_starts_at_rank_one() {
        val status = DynastyProgression.status(GameState(), PlayerMeta())
        assertEquals(1, status.rank.level)
        assertTrue(status.progress in 0f..1f)
    }

    @Test
    fun persistent_career_stats_raise_dynasty_rank() {
        val fresh = DynastyProgression.status(GameState(), PlayerMeta()).rank.level
        val veteranState = GameState(prestigePoints = 50_000)
        val veteranMeta = PlayerMeta(
            totalTaps = 100_000,
            totalPurchases = 50_000,
            prestigeCount = 150,
            streakDays = 90,
            highestEraSeen = 10
        )
        val veteran = DynastyProgression.status(veteranState, veteranMeta)
        assertTrue(veteran.rank.level > fresh)
        assertTrue(veteran.renown > 0.0)
    }

    @Test
    fun dynasty_status_never_exceeds_rank_cap() {
        val extremeState = GameState(prestigePoints = Int.MAX_VALUE)
        val extremeMeta = PlayerMeta(
            totalTaps = Long.MAX_VALUE,
            totalPurchases = Long.MAX_VALUE,
            prestigeCount = Int.MAX_VALUE,
            streakDays = Int.MAX_VALUE,
            highestEraSeen = Int.MAX_VALUE
        )
        val status = DynastyProgression.status(extremeState, extremeMeta)
        assertEquals(DynastyProgression.MAX_RANK, status.rank.level)
        assertEquals(1f, status.progress, 0f)
    }
}
```

## File: src/test/java/com/zerotoempire/game/EconomyInvariantTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class EconomyInvariantTest {
    @Test
    fun bulkPurchaseNeverSpendsMoreThanAvailableCash() {
        val business = defaultBusinesses().first().copy(level = 12)
        val budgets = listOf(0.0, business.nextCost * .99, business.nextCost, 1e6, 1e12)

        budgets.forEach { cash ->
            BuyMode.entries.forEach { mode ->
                val quote = BulkPurchase.quote(business, cash, mode)
                assertTrue("negative count for $mode", quote.count >= 0)
                assertTrue("negative cost for $mode", quote.totalCost >= 0.0)
                assertTrue("non-finite cost for $mode", quote.totalCost.isFinite())
                if (quote.valid) {
                    assertTrue("quote exceeds budget for $mode", quote.totalCost <= cash)
                }
            }
        }
    }

    @Test
    fun bulkCostIsMonotonicWithQuantity() {
        val business = defaultBusinesses().first().copy(level = 25)
        var previous = 0.0
        for (count in 1..100) {
            val cost = BulkPurchase.cost(business, count)
            assertTrue(cost.isFinite())
            assertTrue(cost >= previous)
            previous = cost
        }
    }

    @Test
    fun offlineProgressRejectsClockRollback() {
        val state = automatedState()
        val reward = OfflineProgress.calculate(
            state = state,
            lastSeenMillis = 2_000_000L,
            nowMillis = 1_000_000L
        )

        assertEquals(0L, reward.elapsedSeconds)
        assertEquals(0L, reward.paidSeconds)
        assertEquals(0.0, reward.cash, 0.0)
        assertFalse(reward.eligible)
    }

    @Test
    fun offlineProgressPaysOnlyAutomatedBusinesses() {
        val businesses = defaultBusinesses().mapIndexed { index, business ->
            if (index == 0) business.copy(level = 20) else business
        }
        val manual = GameState(businesses = businesses)
        val automated = manual.copy(hiredManagerIds = setOf(businesses.first().id))
        val now = 10_000_000L
        val since = now - 3600_000L

        val manualReward = OfflineProgress.calculate(manual, since, now)
        val automatedReward = OfflineProgress.calculate(automated, since, now)

        assertEquals(0.0, manualReward.cash, 0.0)
        assertTrue(automatedReward.cash > 0.0)
    }

    @Test
    fun offlineRewardCannotExceedConfiguredCap() {
        val state = automatedState().copy(upgradeRanks = mapOf("offline" to 8))
        val now = 10_000_000_000L
        val reward = OfflineProgress.calculate(
            state,
            lastSeenMillis = now - 30L * 24L * 3600L * 1000L,
            nowMillis = now
        )

        assertEquals(16L * 3600L, reward.paidSeconds)
        assertTrue(reward.elapsedSeconds > reward.paidSeconds)
    }

    private fun automatedState(): GameState {
        val businesses = defaultBusinesses().mapIndexed { index, business ->
            if (index == 0) business.copy(level = 20) else business
        }
        return GameState(
            businesses = businesses,
            hiredManagerIds = setOf(businesses.first().id)
        )
    }
}
```

## File: src/test/java/com/zerotoempire/game/EconomyMathBoundaryTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class EconomyMathBoundaryTest {
    @Test
    fun finiteNormalizesInvalidAndExtremeValues() {
        assertEquals(0.0, EconomyMath.finite(Double.NaN), 0.0)
        assertEquals(0.0, EconomyMath.finite(Double.NEGATIVE_INFINITY), 0.0)
        assertEquals(0.0, EconomyMath.finite(-1.0), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.finite(Double.POSITIVE_INFINITY), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.finite(Double.MAX_VALUE), 0.0)
    }

    @Test
    fun safeAddSaturatesInsteadOfOverflowing() {
        assertEquals(
            EconomyMath.MAX_VALUE,
            EconomyMath.safeAdd(EconomyMath.MAX_VALUE, EconomyMath.MAX_VALUE),
            0.0
        )
        assertEquals(
            EconomyMath.MAX_VALUE,
            EconomyMath.safeAdd(EconomyMath.MAX_VALUE * .9, EconomyMath.MAX_VALUE * .2),
            0.0
        )
    }

    @Test
    fun growthCostStaysFiniteAtExtremeLevels() {
        val cost = EconomyMath.growthCost(10.0, Int.MAX_VALUE)
        assertTrue(cost.isFinite())
        assertEquals(EconomyMath.MAX_VALUE, cost, 0.0)
    }

    @Test
    fun geometricCostStaysFiniteForHugePurchases() {
        val cost = EconomyMath.geometricCost(10.0, 0, Int.MAX_VALUE)
        assertTrue(cost.isFinite())
        assertEquals(EconomyMath.MAX_VALUE, cost, 0.0)
    }

    @Test
    fun bulkQuoteWithExtremeCashRemainsBoundedAndAffordable() {
        val business = defaultBusinesses().first()
        val quote = BulkPurchase.quote(business, EconomyMath.MAX_VALUE, BuyMode.MAX)

        assertTrue(quote.count in 1..1_000_000)
        assertTrue(quote.totalCost.isFinite())
        assertTrue(quote.totalCost <= EconomyMath.MAX_VALUE)
    }

    @Test
    fun milestoneDistanceDoesNotOverflowNearIntMax() {
        val business = defaultBusinesses().first().copy(level = Int.MAX_VALUE - 1)
        val distance = BulkPurchase.levelsToNextMilestone(business)

        assertEquals(1, distance)
    }
}
```

## File: src/test/java/com/zerotoempire/game/EconomySafetyTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class EconomySafetyTest {
    @Test
    fun finiteClampsNanInfinityAndOverflow() {
        assertEquals(0.0, EconomyMath.finite(Double.NaN), 0.0)
        assertEquals(0.0, EconomyMath.finite(-1.0), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.finite(Double.POSITIVE_INFINITY), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.finite(Double.MAX_VALUE), 0.0)
    }

    @Test
    fun safeAddSaturatesInsteadOfOverflowing() {
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.safeAdd(EconomyMath.MAX_VALUE, 1.0), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.safeAdd(EconomyMath.MAX_VALUE * .9, EconomyMath.MAX_VALUE * .2), 0.0)
        assertTrue(EconomyMath.safeAdd(10.0, 20.0).isFinite())
    }

    @Test
    fun growthCostRemainsFiniteAtExtremeLevel() {
        val cost = EconomyMath.growthCost(10.0, Int.MAX_VALUE)
        assertTrue(cost.isFinite())
        assertEquals(EconomyMath.MAX_VALUE, cost, 0.0)
    }

    @Test
    fun extremeGameStateNeverProducesNaNOrInfinity() {
        val maxedBusinesses = defaultBusinesses().map { it.copy(level = Int.MAX_VALUE) }
        val state = GameState(
            cash = EconomyMath.MAX_VALUE,
            lifetimeCash = EconomyMath.MAX_VALUE,
            prestigePoints = Int.MAX_VALUE,
            businesses = maxedBusinesses,
            hiredManagerIds = maxedBusinesses.map { it.id }.toSet(),
            upgradeRanks = mapOf("income" to Int.MAX_VALUE, "tap" to Int.MAX_VALUE, "prestige" to Int.MAX_VALUE)
        )

        assertTrue(state.incomePerSecond.isFinite())
        assertTrue(state.automatedIncomePerSecond.isFinite())
        assertTrue(state.tapValue.isFinite())
        assertTrue(state.incomePerSecond <= EconomyMath.MAX_VALUE)
        assertTrue(state.tapValue <= EconomyMath.MAX_VALUE)
    }

    @Test
    fun prestigeResetPreservesPermanentResourcesAndBoost() {
        val boostEnd = 9_999_999_999L
        val state = GameState(
            cash = 123_456.0,
            lifetimeCash = 1e18,
            prestigePoints = 0,
            businesses = defaultBusinesses().mapIndexed { index, b -> if (index == 0) b.copy(level = 100) else b },
            hiredManagerIds = setOf(0),
            upgradeRanks = mapOf("income" to 4, "prestige" to 2),
            gems = 777,
            boostEndsAtMillis = boostEnd
        )

        val reset = Progression.prestigeReset(state)
        assertNotNull(reset)
        reset!!
        assertEquals(10.0, reset.cash, 0.0)
        assertEquals(10.0, reset.lifetimeCash, 0.0)
        assertTrue(reset.businesses.all { it.level == 0 })
        assertTrue(reset.hiredManagerIds.isEmpty())
        assertEquals(777, reset.gems)
        assertEquals(state.upgradeRanks, reset.upgradeRanks)
        assertEquals(boostEnd, reset.boostEndsAtMillis)
        assertTrue(reset.prestigePoints > 0)
    }

    @Test
    fun prestigeCannotRepeatWithoutNewRunProgress() {
        val first = Progression.prestigeReset(GameState(lifetimeCash = 1e12, prestigePoints = 0))
        assertNotNull(first)
        assertNull(Progression.prestigeReset(first!!))
    }

    @Test
    fun prestigeRewardHandlesNonFiniteInputs() {
        assertEquals(0, Progression.prestigeReward(Double.NaN))
        assertEquals(0, Progression.prestigeReward(Double.NEGATIVE_INFINITY))
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(Double.POSITIVE_INFINITY))
        assertTrue(Progression.prestigeReward(EconomyMath.MAX_VALUE) >= 0)
    }
}
```

## File: src/test/java/com/zerotoempire/game/EconomyTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.*
import org.junit.Test

class EconomyTest {
    @Test fun costsAlwaysIncrease(){ defaultBusinesses().forEach{b->assertTrue(b.copy(level=100).nextCost>b.copy(level=10).nextCost)} }
    @Test fun milestonesNeverReduceIncome(){ val b=defaultBusinesses().first(); assertTrue(b.copy(level=25).rawIncomePerSecond>=b.copy(level=24).rawIncomePerSecond) }
    @Test fun prestigeRewardIsMonotonic(){ var previous=0; listOf(1e6,1e7,1e8,1e9,1e12,1e15).forEach{cash->val reward=Progression.prestigeReward(cash);assertTrue(reward>=previous);previous=reward} }
    @Test fun managerRaisesBusinessIncome(){ val base=GameState(businesses=defaultBusinesses().map{if(it.id==0)it.copy(level=10) else it}); val managed=base.copy(hiredManagerIds=setOf(0)); assertTrue(managed.businessIncome(managed.businesses[0])>base.businessIncome(base.businesses[0])) }
    @Test fun upgradeRaisesGlobalIncome(){ val b=defaultBusinesses().map{if(it.id==0)it.copy(level=10)else it}; val base=GameState(businesses=b); val upgraded=base.copy(upgradeRanks=mapOf("income" to 1)); assertTrue(upgraded.incomePerSecond>base.incomePerSecond) }
    @Test fun offlineRewardIsCapped(){ val s=GameState(businesses=defaultBusinesses().map{if(it.id==0)it.copy(level=10)else it}); val now=1_000_000_000L; val r=OfflineProgress.calculate(s,now-100L*3600*1000,now); assertEquals(8L*3600,r.paidSeconds) }
    @Test fun offlineUpgradeExtendsCap(){ val s=GameState(businesses=defaultBusinesses().map{if(it.id==0)it.copy(level=10)else it},upgradeRanks=mapOf("offline" to 3)); val now=1_000_000_000L; val r=OfflineProgress.calculate(s,now-100L*3600*1000,now); assertEquals(11L*3600,r.paidSeconds) }
}
```

## File: src/test/java/com/zerotoempire/game/EmpireNumberFormatTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test

class EmpireNumberFormatTest {
    @Test fun formatsEarlyEconomy() {
        assertEquals("$10.0", EmpireNumberFormat.money(10.0))
        assertEquals("$1.50K", EmpireNumberFormat.money(1_500.0))
    }

    @Test fun formatsLateEconomyWithoutHugeQiStrings() {
        assertEquals("$2.00Sx", EmpireNumberFormat.money(2.0e21))
        assertEquals("$3.00Oc", EmpireNumberFormat.money(3.0e27))
        assertEquals("$1.20No", EmpireNumberFormat.money(1.2e30))
    }

    @Test fun handlesInfinityDeterministically() {
        assertEquals("$∞", EmpireNumberFormat.money(Double.POSITIVE_INFINITY))
    }
}
```

## File: src/test/java/com/zerotoempire/game/EndgameContentTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class EndgameContentTest {
    @Test fun businessCatalogContainsPostGalacticTier() {
        val businesses = defaultBusinesses()
        assertEquals(14, businesses.size)
        assertEquals("Intergalactic Gateway", businesses[10].name)
        assertEquals("Cosmic Foundry", businesses[11].name)
        assertEquals("Reality Engine", businesses[12].name)
        assertEquals("Transcendent Nexus", businesses[13].name)
    }

    @Test fun endgameBusinessesScaleStrictly() {
        val endgame = defaultBusinesses().filter { it.id >= 10 }
        endgame.zipWithNext().forEach { (a, b) ->
            assertTrue(b.baseCost > a.baseCost)
            assertTrue(b.baseIncome > a.baseIncome)
        }
    }

    @Test fun everyBusinessHasManager() {
        val managedIds = Managers.catalog.map { it.businessId }.toSet()
        defaultBusinesses().forEach { assertTrue(it.id in managedIds) }
    }

    @Test fun managerMultipliersIncreaseIntoEndgame() {
        val endgame = Managers.catalog.filter { it.businessId >= 9 }
        endgame.zipWithNext().forEach { (a, b) -> assertTrue(b.incomeMultiplier > a.incomeMultiplier) }
    }
}
```

## File: src/test/java/com/zerotoempire/game/EndgameProgressionTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class EndgameProgressionTest {
    @Test fun multiplier_is_one_before_endgame() {
        assertEquals(1.0, EndgameProgression.transcendenceMultiplier(1e15), 0.000001)
    }

    @Test fun transcendence_multiplier_is_monotonic_and_bounded() {
        val values = listOf(1e18, 1e21, 1e24, 1e27, 1e30).map(EndgameProgression::transcendenceMultiplier)
        values.zipWithNext().forEach { (a, b) -> assertTrue(b > a) }
        assertTrue(values.last().isFinite())
        assertTrue(values.last() < 5.0)
    }

    @Test fun eras_extend_beyond_galactic() {
        assertEquals("GALACTIC", EmpireEras.current(1e18).name)
        assertEquals("INTERGALACTIC", EmpireEras.current(1e21).name)
        assertEquals("COSMIC", EmpireEras.current(1e24).name)
        assertEquals("REALITY ENGINE", EmpireEras.current(1e27).name)
        assertEquals("TRANSCENDENT", EmpireEras.current(1e30).name)
    }

    @Test fun empire_level_tracks_era_catalog() {
        assertEquals(10, GameState(lifetimeCash = 1e30).empireLevel)
    }
}
```

## File: src/test/java/com/zerotoempire/game/IdentitySystemsTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class IdentitySystemsTest {
    @Test
    fun eraProgressionIsStrictlyIncreasing() {
        val thresholds = EmpireEras.catalog.map { it.requiredLifetimeCash }
        assertEquals(thresholds.sorted(), thresholds)
        assertEquals(thresholds.distinct().size, thresholds.size)
    }

    @Test
    fun currentEraMatchesThresholds() {
        assertEquals("SCRAPPY START", EmpireEras.current(0.0).name)
        assertEquals("LOCAL HUSTLE", EmpireEras.current(1_000.0).name)
        assertEquals("INDUSTRIAL AGE", EmpireEras.current(1_000_000.0).name)
        assertEquals("GALACTIC", EmpireEras.current(1e18).name)
    }

    @Test
    fun viralMilestonesUnlockInOrder() {
        assertNull(ViralMilestones.latestUnlocked(999_999.0))
        assertEquals("million", ViralMilestones.latestUnlocked(1e6)?.id)
        assertEquals("billion", ViralMilestones.latestUnlocked(1e9)?.id)
        assertEquals("galaxy", ViralMilestones.latestUnlocked(1e18)?.id)
        assertTrue(ViralMilestones.catalog.zipWithNext().all { (a, b) -> a.minimumLifetimeCash < b.minimumLifetimeCash })
    }
}
```

## File: src/test/java/com/zerotoempire/game/InterstitialPolicyTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class InterstitialPolicyTest {
    private val day = 20_000L
    private val sessionStart = 1_000_000L

    @Test fun blocksDuringEarlySession() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 5 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun allowsExactlyAtSessionWarmupBoundary() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertTrue(InterstitialPolicy.canShow(s, sessionStart + InterstitialPolicy.MIN_SESSION_AGE_MS, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun allowsAtNaturalBreakAfterWarmup() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertTrue(InterstitialPolicy.canShow(s, sessionStart + 13 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun removeAdsAlwaysWins() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 30 * 60_000L, day, NaturalBreakPoint.ERA_UNLOCK, true, true))
    }

    @Test fun onboardingMustBeComplete() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 30 * 60_000L, day, NaturalBreakPoint.PRESTIGE, false, false))
    }

    @Test fun enforcesMinimumGap() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, lastShownAtMillis = now - 2 * 60_000L, dayEpoch = day, dayShows = 1)
        assertFalse(InterstitialPolicy.canShow(s, now, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun blocksOneMillisecondBeforeMinimumGap() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            lastShownAtMillis = now - InterstitialPolicy.MIN_GAP_MS + 1,
            dayEpoch = day,
            dayShows = 1
        )
        assertFalse(InterstitialPolicy.canShow(s, now, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun allowsExactlyAtMinimumGap() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            lastShownAtMillis = now - InterstitialPolicy.MIN_GAP_MS,
            dayEpoch = day,
            dayShows = 1
        )
        assertTrue(InterstitialPolicy.canShow(s, now, day, NaturalBreakPoint.ERA_UNLOCK, true, false))
    }

    @Test fun enforcesSessionCap() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, sessionShows = InterstitialPolicy.MAX_PER_SESSION, dayEpoch = day, dayShows = 2)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 60 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun enforcesDailyCap() {
        val s = InterstitialPolicyState(sessionStartedAtMillis = sessionStart, dayEpoch = day, dayShows = InterstitialPolicy.MAX_PER_DAY)
        assertFalse(InterstitialPolicy.canShow(s, sessionStart + 60 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun staleDailyCapDoesNotCarryIntoNewDay() {
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            dayEpoch = day - 1,
            dayShows = InterstitialPolicy.MAX_PER_DAY
        )
        assertTrue(InterstitialPolicy.canShow(s, sessionStart + 60 * 60_000L, day, NaturalBreakPoint.PRESTIGE, true, false))
    }

    @Test fun recordShowIncrementsSessionAndSameDayCounters() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            sessionShows = 1,
            lastShownAtMillis = 42L,
            dayEpoch = day,
            dayShows = 2
        )

        val updated = InterstitialPolicy.recordShow(s, now, day)

        assertEquals(2, updated.sessionShows)
        assertEquals(now, updated.lastShownAtMillis)
        assertEquals(day, updated.dayEpoch)
        assertEquals(3, updated.dayShows)
    }

    @Test fun recordShowResetsDailyCounterOnNewDay() {
        val now = sessionStart + 30 * 60_000L
        val s = InterstitialPolicyState(
            sessionStartedAtMillis = sessionStart,
            sessionShows = 1,
            dayEpoch = day - 1,
            dayShows = InterstitialPolicy.MAX_PER_DAY
        )

        val updated = InterstitialPolicy.recordShow(s, now, day)

        assertEquals(2, updated.sessionShows)
        assertEquals(day, updated.dayEpoch)
        assertEquals(1, updated.dayShows)
    }
}
```

## File: src/test/java/com/zerotoempire/game/LateGameTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class LateGameTest {
    @Test fun legacyMasteryIsMonotonic() {
        assertEquals(1.0, LateGame.legacyMasteryMultiplier(0), 1e-9)
        assertTrue(LateGame.legacyMasteryMultiplier(100) > LateGame.legacyMasteryMultiplier(10))
    }

    @Test fun portfolioDepthRewardsDeepBusinesses() {
        val base = defaultBusinesses()
        val deep = base.mapIndexed { i, b -> if (i < 3) b.copy(level = 500) else b }
        assertTrue(LateGame.portfolioDepthMultiplier(deep) > LateGame.portfolioDepthMultiplier(base))
    }

    @Test fun prestigeRecommendationRequiresMeaningfulGain() {
        assertFalse(LateGame.recommendedPrestige(100, 1_000_000.0))
        assertTrue(LateGame.recommendedPrestige(0, 1_000_000.0))
    }

    @Test fun milestoneModeTargetsExactNextMilestone() {
        val b = defaultBusinesses().first().copy(level = 7)
        assertEquals(3, BulkPurchase.levelsToNextMilestone(b))
        val cost = BulkPurchase.cost(b, 3)
        val quote = BulkPurchase.quote(b, cost, BuyMode.MILESTONE)
        assertEquals(3, quote.count)
        assertEquals(cost, quote.totalCost, 1e-6)
    }

    @Test fun milestoneModeDoesNotPartiallyBuyWhenUnaffordable() {
        val b = defaultBusinesses().first().copy(level = 7)
        val full = BulkPurchase.cost(b, 3)
        val quote = BulkPurchase.quote(b, full * .9, BuyMode.MILESTONE)
        assertEquals(0, quote.count)
        assertEquals(full, quote.totalCost, 1e-6)
    }
}
```

## File: src/test/java/com/zerotoempire/game/LongCampaignInvariantTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class LongCampaignInvariantTest {
    @Test
    fun repeatedPrestigeCyclesRemainFiniteAndProgressiveUntilSaturation() {
        var points = 0
        val progressiveRuns = listOf(1e12, 1e15, 1e18, 1e21, 1e24, 1e27, 1e28)

        progressiveRuns.forEach { lifetime ->
            val state = GameState(
                lifetimeCash = lifetime,
                prestigePoints = points,
                gems = 500,
                upgradeRanks = mapOf("income" to 10, "prestige" to 10),
                boostEndsAtMillis = 9_999_999_999L
            )
            val reset = Progression.prestigeReset(state)
            assertNotNull("run at $lifetime should earn additional legacy", reset)
            reset!!
            val previousPoints = points
            points = reset.prestigePoints

            assertTrue(points > previousPoints)
            assertTrue(reset.prestigeMultiplier.isFinite())
            assertTrue(reset.legacyMasteryMultiplier.isFinite())
            assertTrue(reset.incomePerSecond.isFinite())
            assertEquals(500, reset.gems)
            assertEquals(state.upgradeRanks, reset.upgradeRanks)
            assertEquals(state.boostEndsAtMillis, reset.boostEndsAtMillis)
            assertTrue(reset.businesses.all { it.level == 0 })
            assertTrue(reset.hiredManagerIds.isEmpty())
        }

        val saturated = Progression.prestigeReset(GameState(lifetimeCash = 1e30, prestigePoints = points))
        assertNotNull(saturated)
        assertEquals(Int.MAX_VALUE, saturated!!.prestigePoints)
        assertNull(Progression.prestigeReset(GameState(lifetimeCash = EconomyMath.MAX_VALUE, prestigePoints = Int.MAX_VALUE)))
    }

    @Test
    fun matureManagedEmpireCanGoOfflineAndReturnWithoutOverflow() {
        val businesses = defaultBusinesses().map { business ->
            business.copy(level = if (business.id >= 10) 1_000 else 5_000)
        }
        val state = GameState(
            cash = 1e150,
            lifetimeCash = 1e150,
            prestigePoints = 1_000_000,
            businesses = businesses,
            hiredManagerIds = businesses.map { it.id }.toSet(),
            upgradeRanks = mapOf("income" to 20, "offline" to 8, "prestige" to 15),
            boostEndsAtMillis = 0L
        )

        val start = 1_800_000_000_000L
        val reward = OfflineProgress.calculate(state, start, start + 7L * 24L * 60L * 60L * 1_000L)

        assertTrue(reward.eligible)
        assertEquals(16L * 60L * 60L, reward.paidSeconds)
        assertTrue(reward.cash.isFinite())
        assertTrue(reward.cash > 0.0)
        assertTrue(reward.cash <= EconomyMath.MAX_VALUE)

        val returned = state.copy(
            cash = EconomyMath.safeAdd(state.cash, reward.cash),
            lifetimeCash = EconomyMath.safeAdd(state.lifetimeCash, reward.cash)
        )
        assertTrue(returned.cash.isFinite())
        assertTrue(returned.lifetimeCash.isFinite())
        assertTrue(returned.incomePerSecond.isFinite())
        assertTrue(returned.tapValue.isFinite())
    }

    @Test
    fun transcendenceFrontierStillSupportsPurchasesAndPrestigeMath() {
        val nexus = defaultBusinesses().last().copy(level = 1_000)
        val state = GameState(
            cash = EconomyMath.MAX_VALUE,
            lifetimeCash = EconomyMath.MAX_VALUE,
            prestigePoints = 10_000_000,
            businesses = defaultBusinesses().map { if (it.id == nexus.id) nexus else it },
            hiredManagerIds = setOf(nexus.id),
            upgradeRanks = mapOf("income" to 20, "prestige" to 15)
        )

        val quote = BulkPurchase.quote(nexus, state.cash, BuyMode.MAX)
        assertTrue(quote.count >= 0)
        assertTrue(quote.totalCost.isFinite())
        assertTrue(state.incomePerSecond.isFinite())
        assertTrue(state.automatedIncomePerSecond.isFinite())
        assertTrue(Progression.prestigeReward(state.lifetimeCash) >= state.prestigePoints)
    }
}
```

## File: src/test/java/com/zerotoempire/game/NumericStabilityTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class NumericStabilityTest {
    @Test
    fun extremeBusinessCostsRemainFinite() {
        val business = defaultBusinesses().last().copy(level = 100_000)
        assertTrue(business.nextCost.isFinite())
        assertEquals(EconomyMath.MAX_VALUE, business.nextCost, 0.0)
        assertTrue(BulkPurchase.cost(business, 25).isFinite())
    }

    @Test
    fun extremeStateIncomeAndTapRemainFinite() {
        val businesses = defaultBusinesses().map { it.copy(level = 1_000_000) }
        val state = GameState(
            cash = EconomyMath.MAX_VALUE,
            lifetimeCash = EconomyMath.MAX_VALUE,
            prestigePoints = Int.MAX_VALUE,
            businesses = businesses,
            hiredManagerIds = businesses.map { it.id }.toSet(),
            upgradeRanks = mapOf("tap" to 10, "income" to 20, "offline" to 8, "prestige" to 15)
        )

        assertTrue(state.incomePerSecond.isFinite())
        assertTrue(state.automatedIncomePerSecond.isFinite())
        assertTrue(state.tapValue.isFinite())
        assertTrue(state.incomePerSecond <= EconomyMath.MAX_VALUE)
    }

    @Test
    fun safeAddSaturatesInsteadOfOverflowing() {
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.safeAdd(EconomyMath.MAX_VALUE, 1e299), 0.0)
        assertEquals(EconomyMath.MAX_VALUE, EconomyMath.safeAdd(Double.POSITIVE_INFINITY, 1.0), 0.0)
    }

    @Test
    fun maxBulkQuoteNeverReturnsInfinity() {
        val business = defaultBusinesses().first().copy(level = 4_500)
        val quote = BulkPurchase.quote(business, EconomyMath.MAX_VALUE, BuyMode.MAX)
        assertTrue(quote.count >= 0)
        assertTrue(quote.totalCost.isFinite())
        assertTrue(quote.totalCost <= EconomyMath.MAX_VALUE)
    }
}
```

## File: src/test/java/com/zerotoempire/game/OfflineAutomationTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class OfflineAutomationTest {
    @Test
    fun ownedBusinessWithoutManagerProducesNoOfflineCash() {
        val business = defaultBusinesses().first().copy(level = 100)
        val state = GameState(
            businesses = defaultBusinesses().map { if (it.id == business.id) business else it }
        )

        assertTrue(state.incomePerSecond > 0.0)
        assertEquals(0.0, state.automatedIncomePerSecond, 0.0)

        val reward = OfflineProgress.calculate(state, 1_000_000L, 1_000_000L + 3_600_000L)
        assertEquals(0.0, reward.cash, 0.0)
    }

    @Test
    fun hiredManagerEnablesOfflineProductionForItsBusiness() {
        val business = defaultBusinesses().first().copy(level = 100)
        val state = GameState(
            businesses = defaultBusinesses().map { if (it.id == business.id) business else it },
            hiredManagerIds = setOf(business.id)
        )

        assertTrue(state.automatedIncomePerSecond > 0.0)
        val reward = OfflineProgress.calculate(state, 1_000_000L, 1_000_000L + 3_600_000L)
        assertTrue(reward.eligible)
        assertTrue(reward.cash > 0.0)
    }

    @Test
    fun onlyManagedBusinessesContributeOffline() {
        val first = defaultBusinesses()[0].copy(level = 100)
        val second = defaultBusinesses()[1].copy(level = 100)
        val state = GameState(
            businesses = defaultBusinesses().map {
                when (it.id) {
                    first.id -> first
                    second.id -> second
                    else -> it
                }
            },
            hiredManagerIds = setOf(first.id)
        )

        assertTrue(state.incomePerSecond > state.automatedIncomePerSecond)
        assertEquals(state.businessIncome(first) *
            state.prestigeMultiplier *
            state.legacyMasteryMultiplier *
            state.portfolioDepthMultiplier *
            state.transcendenceMultiplier *
            state.globalUpgradeMultiplier *
            state.boostMultiplier *
            state.eventMultiplier,
            state.automatedIncomePerSecond,
            0.0001
        )
    }
}
```

## File: src/test/java/com/zerotoempire/game/OfflineProgressBoundaryTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import java.time.ZoneId

class OfflineProgressBoundaryTest {
    private val utc = ZoneId.of("UTC")

    @Test
    fun exactlyThirtySecondsIsEligibleWhenAutomated() {
        val state = automatedState()
        val start = 1_700_000_000_000L
        val reward = OfflineProgress.calculate(state, start, start + 30_000L, utc)

        assertEquals(30L, reward.elapsedSeconds)
        assertEquals(30L, reward.paidSeconds)
        assertTrue(reward.cash > 0.0)
        assertTrue(reward.eligible)
    }

    @Test
    fun lessThanThirtySecondsIsNotEligible() {
        val state = automatedState()
        val start = 1_700_000_000_000L
        val reward = OfflineProgress.calculate(state, start, start + 29_999L, utc)

        assertEquals(29L, reward.elapsedSeconds)
        assertEquals(29L, reward.paidSeconds)
        assertTrue(reward.cash > 0.0)
        assertFalse(reward.eligible)
    }

    @Test
    fun boostExpirySplitsOfflineIncomeExactlyAtBoundary() {
        val base = automatedState()
        val start = 1_700_000_000_000L
        val state = base.copy(boostEndsAtMillis = start + 60_000L)
        val reward = OfflineProgress.calculate(state, start, start + 120_000L, utc)

        val expected = base.automatedBaseIncomePerSecond * .75 * (60.0 * 2.0 + 60.0)
        assertEquals(expected, reward.cash, expected * 1e-9 + 1e-9)
    }

    @Test
    fun rewardAtOfflineCapDoesNotGrowWithLongerAbsence() {
        val state = automatedState()
        val start = 1_700_000_000_000L
        val capEnd = start + 8L * 3600L * 1000L
        val capped = OfflineProgress.calculate(state, start, capEnd, utc)
        val muchLater = OfflineProgress.calculate(state, start, start + 30L * 24L * 3600L * 1000L, utc)

        assertEquals(8L * 3600L, capped.paidSeconds)
        assertEquals(capped.paidSeconds, muchLater.paidSeconds)
        assertEquals(capped.cash, muchLater.cash, capped.cash * 1e-9 + 1e-9)
    }

    private fun automatedState(): GameState {
        val businesses = defaultBusinesses().mapIndexed { index, business ->
            if (index == 0) business.copy(level = 20) else business
        }
        return GameState(
            businesses = businesses,
            hiredManagerIds = setOf(businesses.first().id)
        )
    }
}
```

## File: src/test/java/com/zerotoempire/game/OfflineProgressLifecycleTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import java.time.ZoneOffset

class OfflineProgressLifecycleTest {
    private val automatedState = GameState(
        businesses = GameState().businesses.mapIndexed { index, business ->
            if (index == 0) business.copy(level = 10) else business
        },
        hiredManagerIds = setOf(0)
    )

    @Test
    fun shortLifecycleInterruptionsNeverSurfaceOfflineReward() {
        val start = 1_700_000_000_000L

        val reward = OfflineProgress.calculate(
            state = automatedState,
            lastSeenMillis = start,
            nowMillis = start + 29_999L,
            zoneId = ZoneOffset.UTC
        )

        assertFalse(reward.eligible)
        assertEquals(29L, reward.paidSeconds)
    }

    @Test
    fun thirtySecondBackgroundBoundaryIsEligibleWhenIncomeIsAutomated() {
        val start = 1_700_000_000_000L

        val reward = OfflineProgress.calculate(
            state = automatedState,
            lastSeenMillis = start,
            nowMillis = start + 30_000L,
            zoneId = ZoneOffset.UTC
        )

        assertTrue(reward.cash > 0.0)
        assertEquals(30L, reward.paidSeconds)
        assertTrue(reward.eligible)
    }

    @Test
    fun invalidOrReversedLifecycleTimestampsCannotGrantOfflineCash() {
        val timestamp = 1_700_000_000_000L

        val equal = OfflineProgress.calculate(
            state = automatedState,
            lastSeenMillis = timestamp,
            nowMillis = timestamp,
            zoneId = ZoneOffset.UTC
        )
        val reversed = OfflineProgress.calculate(
            state = automatedState,
            lastSeenMillis = timestamp,
            nowMillis = timestamp - 60_000L,
            zoneId = ZoneOffset.UTC
        )

        assertEquals(0.0, equal.cash, 0.0)
        assertEquals(0.0, reversed.cash, 0.0)
        assertFalse(equal.eligible)
        assertFalse(reversed.eligible)
    }
}
```

## File: src/test/java/com/zerotoempire/game/OfflineTemporalTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test
import java.time.ZoneId
import java.time.ZonedDateTime

class OfflineTemporalTest {
    private val zone = ZoneId.of("Europe/Paris")

    private fun managedState(boostEndsAtMillis: Long = 0L): GameState {
        val first = defaultBusinesses().first().copy(level = 100)
        return GameState(
            businesses = defaultBusinesses().map { if (it.id == first.id) first else it },
            hiredManagerIds = setOf(first.id),
            boostEndsAtMillis = boostEndsAtMillis
        )
    }

    @Test
    fun boostOnlyAppliesUntilItsActualExpiry() {
        val start = ZonedDateTime.of(2026, 8, 17, 10, 0, 0, 0, zone).toInstant().toEpochMilli() // Monday
        val end = start + 3_600_000L
        val boostEnd = start + 1_800_000L
        val state = managedState(boostEnd)

        val reward = OfflineProgress.calculate(state, start, end, zone)
        val expected = state.automatedBaseIncomePerSecond * ((1_800.0 * 2.0) + 1_800.0) * .75

        assertEquals(expected, reward.cash, expected * 1e-9)
    }

    @Test
    fun liveEventMultiplierChangesAtLocalMidnight() {
        val start = ZonedDateTime.of(2026, 8, 21, 23, 30, 0, 0, zone).toInstant().toEpochMilli() // Friday
        val end = start + 3_600_000L // Saturday 00:30
        val state = managedState()

        val reward = OfflineProgress.calculate(state, start, end, zone)
        val expected = state.automatedBaseIncomePerSecond * ((1_800.0 * 2.0) + (1_800.0 * 1.5)) * .75

        assertEquals(expected, reward.cash, expected * 1e-9)
    }
}
```

## File: src/test/java/com/zerotoempire/game/PlayableFlowTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Test

class PlayableFlowTest {

    @Test
    fun freshPlayerCanBuyFirstAssetAndStartPassiveIncome() {
        val initial = GameState()
        val first = initial.businesses.first()
        val quote = BulkPurchase.quote(first, initial.cash, BuyMode.X1)

        assertEquals(1, quote.count)
        assertTrue(quote.totalCost <= initial.cash)

        val purchased = first.copy(level = first.level + quote.count)
        val next = initial.copy(
            cash = initial.cash - quote.totalCost,
            businesses = initial.businesses.map { if (it.id == purchased.id) purchased else it }
        )

        assertEquals(1, next.businesses.first().level)
        assertTrue(next.incomePerSecond > 0.0)
        assertTrue(next.tapValue > 0.0)
    }

    @Test
    fun managerHireActuallyImprovesAssociatedProduction() {
        val business = defaultBusinesses().first().copy(level = 100)
        val withoutManager = GameState(
            cash = 10_000.0,
            lifetimeCash = 10_000.0,
            businesses = defaultBusinesses().map { if (it.id == business.id) business else it }
        )
        val withManager = withoutManager.copy(hiredManagerIds = setOf(business.id))

        assertTrue(withManager.businessIncome(business) > withoutManager.businessIncome(business))
        assertTrue(withManager.incomePerSecond > withoutManager.incomePerSecond)
    }

    @Test
    fun offlineProgressPaysPositiveCappedIncomeForAutomatedEmpire() {
        val business = defaultBusinesses().first().copy(level = 100)
        val state = GameState(
            businesses = defaultBusinesses().map { if (it.id == business.id) business else it },
            hiredManagerIds = setOf(business.id)
        )
        val lastSeen = 1_000_000L
        val nineHoursLater = lastSeen + 9L * 60L * 60L * 1000L
        val reward = OfflineProgress.calculate(state, lastSeen, nineHoursLater)

        assertTrue(reward.eligible)
        assertEquals(8L * 60L * 60L, reward.paidSeconds)
        assertTrue(reward.cash > 0.0)
    }

    @Test
    fun prestigeBecomesAvailableAndCreatesPermanentPower() {
        val before = GameState(lifetimeCash = 1.0e12)
        val after = Progression.prestigeReset(before)
        assertNotNull(after)
        assertTrue(after!!.prestigePoints > 0)
        assertTrue(after.prestigeMultiplier > before.prestigeMultiplier)
        assertEquals(10.0, after.cash, 0.0)
    }

    @Test
    fun playerCanCompleteMultiplePrestigeCycles() {
        val firstRun = GameState(lifetimeCash = 1.0e12, gems = 40, upgradeRanks = mapOf("income" to 2))
        val firstReset = Progression.prestigeReset(firstRun)
        assertNotNull(firstReset)

        val secondRun = firstReset!!.copy(
            cash = 1.0e18,
            lifetimeCash = 1.0e18,
            businesses = defaultBusinesses().mapIndexed { index, b -> if (index <= 8) b.copy(level = 100) else b },
            hiredManagerIds = Managers.catalog.filter { it.businessId <= 8 }.map { it.businessId }.toSet()
        )
        val secondReset = Progression.prestigeReset(secondRun)
        assertNotNull(secondReset)
        secondReset!!

        assertTrue(secondReset.prestigePoints > firstReset.prestigePoints)
        assertEquals(firstReset.gems, secondReset.gems)
        assertEquals(firstReset.upgradeRanks, secondReset.upgradeRanks)
        assertTrue(secondReset.businesses.all { it.level == 0 })
        assertTrue(secondReset.hiredManagerIds.isEmpty())
    }

    @Test
    fun bulkMilestonePurchaseTargetsNextPowerSpike() {
        val business = defaultBusinesses().first().copy(level = 24)
        val required = BulkPurchase.cost(business, 1)
        val quote = BulkPurchase.quote(business, required, BuyMode.MILESTONE)

        assertEquals(1, quote.count)
        assertEquals(25, business.level + quote.count)
        assertTrue(25 in BulkPurchase.crossedMilestones(business.level, business.level + quote.count))
    }

    @Test
    fun endgameContentRemainsEconomicallyFiniteAtUnlockScale() {
        val businesses = defaultBusinesses().map { business -> business.copy(level = 25) }
        val state = GameState(
            cash = 1.0e32,
            lifetimeCash = 1.0e32,
            businesses = businesses,
            hiredManagerIds = Managers.catalog.map { it.businessId }.toSet(),
            prestigePoints = 250
        )

        assertEquals(14, state.businesses.size)
        assertTrue(state.incomePerSecond.isFinite())
        assertTrue(state.incomePerSecond > 0.0)
        assertTrue(state.transcendenceMultiplier >= 1.0)
    }
}
```

## File: src/test/java/com/zerotoempire/game/PlayBillingGatewayInvariantTest.kt
```kotlin
package com.zerotoempire.game

import java.nio.file.Files
import java.nio.file.Paths
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * Regression guards for the asynchronous BillingClient callback lifecycle.
 *
 * These invariants deliberately inspect the production source because PlayBillingGateway owns a
 * concrete BillingClient that cannot be driven deterministically from local JVM tests. They keep
 * the critical pending -> new purchase -> late confirmation routing rules under CI without adding
 * a fake billing implementation to production code.
 */
class PlayBillingGatewayInvariantTest {
    private val source: String by lazy { gatewaySource() }

    @Test
    fun pendingPurchaseReleasesActiveSlotOnlyAfterCallbackIsDeferred() {
        assertOrdered(
            "deferredPurchases[purchase.purchaseToken] = DeferredPurchase(product, callback)",
            "clearPending()",
            "callback(PurchaseResult.Pending)"
        )
    }

    @Test
    fun latePurchaseUpdateCannotHijackNewActivePurchase() {
        assertTrue(
            source.contains(
                "purchases.firstOrNull { target.productId in it.products && it.purchaseToken !in deferredPurchases }"
            )
        )
        assertOrdered(
            "processPurchase(activePurchase, target)",
            "purchases.filter { it.purchaseToken != activeToken }.forEach { processPurchase(it) }"
        )
    }

    @Test
    fun deferredCompletionIsDeliveredAtMostOnce() {
        val function = source.substringAfter("private fun completeDeferred(")
            .substringBefore("private fun acknowledge(")
        val lookup = function.indexOf("val deferred = deferredPurchases[token] ?: return")
        val identityGuard = function.indexOf("if (deferred.callback !== callback) return")
        val removal = function.indexOf("deferredPurchases.remove(token)")
        val delivery = function.indexOf("callback(result)")

        assertTrue(lookup >= 0)
        assertTrue(identityGuard > lookup)
        assertTrue(removal > identityGuard)
        assertTrue(delivery > removal)
    }

    @Test
    fun disconnectDropsAllUiCallbacksAndAlwaysClosesBillingClient() {
        val function = source.substringAfter("override fun disconnect()")
            .substringBefore("override fun purchase(")
        assertTrue(function.contains("clearPending()"))
        assertTrue(function.contains("deferredPurchases.clear()"))
        assertTrue(function.contains("billingClient.endConnection()"))
        assertTrue(!function.contains("if (billingClient.isReady) billingClient.endConnection()"))
    }

    private fun assertOrdered(vararg snippets: String) {
        var previous = -1
        snippets.forEach { snippet ->
            val index = source.indexOf(snippet, startIndex = previous + 1)
            assertTrue("Missing or out-of-order billing invariant: $snippet", index > previous)
            previous = index
        }
    }

    private fun gatewaySource(): String {
        val relative = "src/main/java/com/zerotoempire/game/PlayBillingGateway.kt"
        val candidates = listOf(Paths.get(relative), Paths.get("app", relative))
        val path = candidates.firstOrNull(Files::isRegularFile)
            ?: error("PlayBillingGateway.kt not found from ${Paths.get("").toAbsolutePath()}")
        return String(Files.readAllBytes(path), Charsets.UTF_8)
    }
}
```

## File: src/test/java/com/zerotoempire/game/PreDeviceSmokeInvariantTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PreDeviceSmokeInvariantTest {
    @Test
    fun catalogsAreCompleteAndInternallyConsistent() {
        val businesses = defaultBusinesses()
        val managers = Managers.catalog

        assertEquals(14, businesses.size)
        assertEquals(14, managers.size)
        assertEquals((0..13).toList(), businesses.map { it.id })
        assertEquals((0..13).toList(), managers.map { it.businessId })
        assertEquals(businesses.map { it.id }.toSet().size, businesses.size)
        assertEquals(managers.map { it.businessId }.toSet().size, managers.size)
        assertTrue(businesses.all { it.baseCost > 0.0 && it.baseCost.isFinite() })
        assertTrue(businesses.all { it.baseIncome > 0.0 && it.baseIncome.isFinite() })
        assertTrue(managers.all { it.cost > 0.0 && it.cost.isFinite() })
        assertTrue(managers.all { it.incomeMultiplier >= 1.0 && it.incomeMultiplier.isFinite() })
    }

    @Test
    fun upgradesHaveUniqueIdsAndPlayableBounds() {
        val upgrades = Upgrades.catalog
        assertEquals(upgrades.size, upgrades.map { it.id }.toSet().size)
        assertTrue(upgrades.all { it.gemCost > 0 })
        assertTrue(upgrades.all { it.maxRank > 0 })
        assertTrue(upgrades.all { it.rank in 0..it.maxRank })
    }

    @Test
    fun everyManagerMatchesARealBusinessAndRevealPath() {
        val businesses = defaultBusinesses().associateBy { it.id }
        Managers.catalog.forEach { manager ->
            val business = businesses[manager.businessId]
            assertTrue("manager ${manager.name} has no business", business != null)
            assertTrue(ContentUnlocks.thresholdForBusiness(manager.businessId).isFinite())
        }
    }

    @Test
    fun freshInstallHasImmediatePlayableAction() {
        val state = GameState()
        val first = state.businesses.first()
        assertTrue(ContentUnlocks.isBusinessVisible(first.id, state.lifetimeCash))
        val quote = BulkPurchase.quote(first, state.cash, BuyMode.X1)
        assertEquals(1, quote.count)
        assertTrue(quote.totalCost <= state.cash)
    }

    @Test
    fun finalBusinessAndManagerRemainReachableBeforeNumericCeiling() {
        val finalBusiness = defaultBusinesses().last()
        val finalManager = Managers.catalog.last()
        assertTrue(ContentUnlocks.thresholdForBusiness(finalBusiness.id) < EconomyMath.MAX_VALUE)
        assertTrue(finalBusiness.baseCost < EconomyMath.MAX_VALUE)
        assertTrue(finalManager.cost < EconomyMath.MAX_VALUE)
        assertTrue(ContentUnlocks.isBusinessVisible(finalBusiness.id, 1e30))
    }
}
```

## File: src/test/java/com/zerotoempire/game/PrestigeCycleTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class PrestigeCycleTest {
    @Test
    fun prestigeRewardGrowsAcrossRunsAndStaysFinite() {
        val first = Progression.prestigeReward(1e9)
        val second = Progression.prestigeReward(1e15)
        val endgame = Progression.prestigeReward(1e30)
        assertTrue(first > 0)
        assertTrue(second > first)
        assertTrue(endgame > second)
        assertTrue(endgame > 0)
    }

    @Test
    fun productionResetRetainsPermanentPowerButResetsRunEconomy() {
        val boostEnd = 9_999_999_999L
        val before = GameState(
            cash = 1e15,
            lifetimeCash = 1e15,
            prestigePoints = 3,
            gems = 90,
            upgradeRanks = mapOf("income" to 5, "prestige" to 4),
            boostEndsAtMillis = boostEnd,
            businesses = defaultBusinesses().mapIndexed { index, b -> if (index < 4) b.copy(level = 100) else b },
            hiredManagerIds = setOf(0, 1, 2)
        )
        val reset = Progression.prestigeReset(before)
        assertNotNull(reset)
        reset!!

        assertEquals(10.0, reset.cash, 0.0)
        assertEquals(10.0, reset.lifetimeCash, 0.0)
        assertEquals(0L, reset.businesses.sumOf { it.level.toLong() })
        assertTrue(reset.hiredManagerIds.isEmpty())
        assertEquals(before.gems, reset.gems)
        assertEquals(before.upgradeRanks, reset.upgradeRanks)
        assertEquals(boostEnd, reset.boostEndsAtMillis)
        assertTrue(reset.prestigePoints > before.prestigePoints)
        assertEquals(0.0, reset.incomePerSecond, 0.0)
        assertEquals(0.0, reset.automatedIncomePerSecond, 0.0)
        assertTrue(reset.tapValue.isFinite())
        assertTrue(reset.tapValue > 1.0)
    }

    @Test
    fun sameRunCannotPrestigeTwiceWithoutNewProgress() {
        val first = Progression.prestigeReset(GameState(lifetimeCash = 1e12))
        assertNotNull(first)
        assertNull(Progression.prestigeReset(first!!))
    }

    @Test
    fun laterRunEarnsMoreLegacyButNeverCarriesAutomation() {
        val first = Progression.prestigeReset(GameState(lifetimeCash = 1e12))!!
        val laterRun = first.copy(
            cash = 1e18,
            lifetimeCash = 1e18,
            businesses = defaultBusinesses().map { it.copy(level = 250) },
            hiredManagerIds = defaultBusinesses().map { it.id }.toSet()
        )
        val second = Progression.prestigeReset(laterRun)
        assertNotNull(second)
        second!!

        assertTrue(second.prestigePoints > first.prestigePoints)
        assertTrue(second.hiredManagerIds.isEmpty())
        assertFalse(second.businesses.any { it.level > 0 })
        assertEquals(10.0, second.lifetimeCash, 0.0)
    }

    @Test
    fun maxLegacySaveCannotOverflowOrPrestigeAgain() {
        val maxed = GameState(
            cash = EconomyMath.MAX_VALUE,
            lifetimeCash = EconomyMath.MAX_VALUE,
            prestigePoints = Int.MAX_VALUE
        )
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(maxed.lifetimeCash))
        assertNull(Progression.prestigeReset(maxed))
        assertTrue(maxed.prestigeMultiplier.isFinite())
        assertTrue(maxed.tapValue.isFinite())
    }

    @Test
    fun pathologicalPrestigeInputsAreBounded() {
        assertEquals(0, Progression.prestigeReward(Double.NaN))
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(Double.POSITIVE_INFINITY))
        assertEquals(Int.MAX_VALUE, Progression.prestigeReward(EconomyMath.MAX_VALUE))
        assertEquals(0, Progression.prestigeReward(-1.0))
    }
}
```

## File: src/test/java/com/zerotoempire/game/PrestigeResetTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class PrestigeResetTest {
    @Test
    fun prestigeResetKeepsOnlyPermanentProgress() {
        val state = GameState(
            cash = 9.0e12,
            lifetimeCash = 1.0e15,
            prestigePoints = 3,
            businesses = defaultBusinesses().mapIndexed { index, b -> b.copy(level = index + 20) },
            hiredManagerIds = setOf(0, 1, 2, 3),
            upgradeRanks = mapOf("income" to 4, "tap" to 2, "offline" to 3, "prestige" to 5),
            gems = 777,
            boostEndsAtMillis = 9_000_000L
        )

        val reset = Progression.prestigeReset(state)
        assertNotNull(reset)
        reset!!
        assertEquals(10.0, reset.cash, 0.0)
        assertEquals(10.0, reset.lifetimeCash, 0.0)
        assertTrue(reset.prestigePoints > state.prestigePoints)
        assertEquals(Progression.prestigeReward(state.lifetimeCash), reset.prestigePoints)
        assertTrue(reset.businesses.all { it.level == 0 })
        assertTrue(reset.hiredManagerIds.isEmpty())
        assertEquals(state.upgradeRanks, reset.upgradeRanks)
        assertEquals(777, reset.gems)
        assertEquals(9_000_000L, reset.boostEndsAtMillis)
    }

    @Test
    fun prestigeResetRejectsRunWithoutNewLegacyPoints() {
        assertNull(Progression.prestigeReset(GameState(lifetimeCash = 10.0, prestigePoints = 0)))
    }

    @Test
    fun prestigeResetAtNumericCeilingCannotWrapPoints() {
        val reset = Progression.prestigeReset(
            GameState(lifetimeCash = EconomyMath.MAX_VALUE, prestigePoints = Int.MAX_VALUE - 1)
        )
        assertNotNull(reset)
        assertEquals(Int.MAX_VALUE, reset!!.prestigePoints)
        assertNull(Progression.prestigeReset(reset.copy(lifetimeCash = EconomyMath.MAX_VALUE)))
    }

    @Test
    fun prestigeReadinessAtIntegerCeilingNeverWrapsNegative() {
        assertEquals(0.0, LateGame.prestigeReadiness(Int.MAX_VALUE, EconomyMath.MAX_VALUE), 0.0)
        assertFalse(LateGame.recommendedPrestige(Int.MAX_VALUE, EconomyMath.MAX_VALUE))
        val nearCeiling = LateGame.prestigeReadiness(Int.MAX_VALUE - 1, EconomyMath.MAX_VALUE)
        assertTrue(nearCeiling >= 0.0)
        assertTrue(nearCeiling.isFinite())
    }
}
```

## File: src/test/java/com/zerotoempire/game/ProgressionCycleTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Test

class ProgressionCycleTest {
    @Test
    fun repeatedPrestigeOfflineCyclePreservesOnlyPermanentProgress() {
        val activeBoost = System.currentTimeMillis() + 3_600_000L
        val runOne = GameState(
            cash = 5e12,
            lifetimeCash = 5e12,
            businesses = defaultBusinesses().mapIndexed { index, b ->
                when (index) {
                    0 -> b.copy(level = 250)
                    1 -> b.copy(level = 100)
                    else -> b
                }
            },
            hiredManagerIds = setOf(0, 1),
            upgradeRanks = mapOf("income" to 3, "offline" to 2, "prestige" to 1),
            gems = 321,
            boostEndsAtMillis = activeBoost
        )

        val afterFirstPrestige = Progression.prestigeReset(runOne)
        assertNotNull(afterFirstPrestige)
        afterFirstPrestige!!
        assertEquals(321, afterFirstPrestige.gems)
        assertEquals(runOne.upgradeRanks, afterFirstPrestige.upgradeRanks)
        assertEquals(activeBoost, afterFirstPrestige.boostEndsAtMillis)
        assertTrue(afterFirstPrestige.businesses.all { it.level == 0 })
        assertTrue(afterFirstPrestige.hiredManagerIds.isEmpty())

        val rebuiltBusiness = afterFirstPrestige.businesses.first().copy(level = 100)
        val runTwo = afterFirstPrestige.copy(
            cash = 1e16,
            lifetimeCash = 1e16,
            businesses = afterFirstPrestige.businesses.map { if (it.id == rebuiltBusiness.id) rebuiltBusiness else it },
            hiredManagerIds = setOf(rebuiltBusiness.id)
        )

        val start = 1_700_000_000_000L
        val reward = OfflineProgress.calculate(runTwo.copy(boostEndsAtMillis = 0L), start, start + 3_600_000L)
        assertTrue(reward.eligible)
        assertTrue(reward.cash > 0.0)
        assertTrue(reward.cash.isFinite())

        val creditedRun = runTwo.copy(
            cash = EconomyMath.safeAdd(runTwo.cash, reward.cash),
            lifetimeCash = EconomyMath.safeAdd(runTwo.lifetimeCash, reward.cash)
        )
        val afterSecondPrestige = Progression.prestigeReset(creditedRun)
        assertNotNull(afterSecondPrestige)
        afterSecondPrestige!!

        assertTrue(afterSecondPrestige.prestigePoints > afterFirstPrestige.prestigePoints)
        assertEquals(321, afterSecondPrestige.gems)
        assertEquals(runOne.upgradeRanks, afterSecondPrestige.upgradeRanks)
        assertEquals(activeBoost, afterSecondPrestige.boostEndsAtMillis)
        assertTrue(afterSecondPrestige.businesses.all { it.level == 0 })
        assertTrue(afterSecondPrestige.hiredManagerIds.isEmpty())
        assertEquals(10.0, afterSecondPrestige.cash, 0.0)
        assertEquals(10.0, afterSecondPrestige.lifetimeCash, 0.0)
    }
}
```

## File: src/test/java/com/zerotoempire/game/PurchaseCreditLedgerTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class PurchaseCreditLedgerTest {
    @Test fun blankTransactionIsRejected() {
        val ledger = PurchaseCreditLedger()
        assertFalse(ledger.claim(""))
        assertFalse(ledger.claim("   "))
        assertTrue(ledger.snapshot().isEmpty())
    }

    @Test fun sameTransactionCanOnlyBeClaimedOnce() {
        val ledger = PurchaseCreditLedger()
        assertTrue(ledger.claim("token-a"))
        assertFalse(ledger.claim("token-a"))
        assertEquals(setOf("token-a"), ledger.snapshot())
    }

    @Test fun differentTransactionsForSameSkuRemainIndependent() {
        val ledger = PurchaseCreditLedger()
        assertTrue(ledger.claim("token-a"))
        assertTrue(ledger.claim("token-b"))
        assertEquals(setOf("token-a", "token-b"), ledger.snapshot())
    }

    @Test fun restoredLedgerRejectsPreviouslyCreditedTransaction() {
        val restored = PurchaseCreditLedger(setOf("token-old"))
        assertFalse(restored.claim("token-old"))
        assertTrue(restored.claim("token-new"))
        assertEquals(setOf("token-old", "token-new"), restored.snapshot())
    }
}
```

## File: src/test/java/com/zerotoempire/game/PurchaseRecoveryTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test

class PurchaseRecoveryTest {
    @Test
    fun duplicatePurchaseTokensAreRecoveredExactlyOnce() {
        data class Transaction(val token: String, val product: StoreProduct)
        val transactions = listOf(
            Transaction("token-a", StoreProduct.GEM_PACK_SMALL),
            Transaction("token-a", StoreProduct.GEM_PACK_SMALL),
            Transaction("token-b", StoreProduct.GEM_PACK_SMALL)
        )

        assertEquals(
            listOf(transactions[0], transactions[2]),
            PurchaseRecovery.distinctTransactions(transactions, Transaction::token)
        )
    }

    @Test
    fun noDuplicateConsumablesNeedNoExtraCredit() {
        val products = listOf(
            StoreProduct.REMOVE_ADS,
            StoreProduct.STARTER_PACK,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_MEDIUM
        )

        assertEquals(0, PurchaseRecovery.extraConsumableGems(products))
    }

    @Test
    fun duplicateSmallPacksPreserveEveryRecoveredTransaction() {
        val products = listOf(
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_SMALL
        )

        assertEquals(240, PurchaseRecovery.extraConsumableGems(products))
    }

    @Test
    fun mixedDuplicatePacksPreserveExactGemValue() {
        val products = listOf(
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_MEDIUM,
            StoreProduct.GEM_PACK_MEDIUM,
            StoreProduct.GEM_PACK_MEDIUM
        )

        assertEquals(120 + 650 + 650, PurchaseRecovery.extraConsumableGems(products))
    }

    @Test
    fun pathologicalRecoveryValueSaturatesInsteadOfOverflowing() {
        assertEquals(
            Int.MAX_VALUE,
            PurchaseRecovery.recoveredConsumableGemValue(Int.MAX_VALUE, Int.MAX_VALUE)
        )
    }

    @Test
    fun recoveryValueRejectsNegativeCounts() {
        assertEquals(0, PurchaseRecovery.recoveredConsumableGemValue(-1, -1))
    }

    @Test
    fun concurrentRestoreWaitersCannotDoubleCreditConsumables() {
        val products = listOf(
            StoreProduct.REMOVE_ADS,
            StoreProduct.STARTER_PACK,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_MEDIUM
        )

        assertEquals(products, PurchaseRecovery.deliveryForWaiter(products, 0))
        assertEquals(
            listOf(StoreProduct.REMOVE_ADS, StoreProduct.STARTER_PACK),
            PurchaseRecovery.deliveryForWaiter(products, 1)
        )
        assertEquals(
            listOf(StoreProduct.REMOVE_ADS, StoreProduct.STARTER_PACK),
            PurchaseRecovery.deliveryForWaiter(products, 2)
        )
    }

    @Test
    fun successfulRestoreRevokesPermanentEntitlementMissingFromPlay() {
        assertEquals(
            false,
            PurchaseRecovery.permanentOwned(
                product = StoreProduct.REMOVE_ADS,
                currentOwned = true,
                restoredProducts = emptySet(),
                authoritative = true
            )
        )
    }

    @Test
    fun failedRestoreNeverRevokesSavedPermanentEntitlement() {
        assertEquals(
            true,
            PurchaseRecovery.permanentOwned(
                product = StoreProduct.REMOVE_ADS,
                currentOwned = true,
                restoredProducts = emptySet(),
                authoritative = false
            )
        )
    }

    @Test
    fun successfulRestoreKeepsPermanentEntitlementConfirmedByPlay() {
        assertEquals(
            true,
            PurchaseRecovery.permanentOwned(
                product = StoreProduct.STARTER_PACK,
                currentOwned = false,
                restoredProducts = setOf(StoreProduct.STARTER_PACK),
                authoritative = true
            )
        )
    }
}
```

## File: src/test/java/com/zerotoempire/game/ReviewedTerrainLayerTest.kt
```kotlin
package com.zerotoempire.game

import java.io.File
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class ReviewedTerrainLayerTest {
    @Test
    fun `reviewed terrain layer references every final terrain sprite`() {
        val relativePath = "src/main/java/com/zerotoempire/game/ReviewedTerrainLayer.kt"
        val source = listOf(File(relativePath), File("app/$relativePath"))
            .firstOrNull(File::exists)
            ?.readText()
            ?: error("Unable to locate ReviewedTerrainLayer.kt from ${System.getProperty("user.dir")}")

        val referencedIds = Regex("zte_terrain_(\\d{2})_final")
            .findAll(source)
            .map { it.groupValues[1].toInt() }
            .toSet()

        assertEquals((0..13).toSet(), referencedIds)
        assertTrue("TER-07 must be visible in the reviewed runtime layer", 7 in referencedIds)
    }
}
```

## File: src/test/java/com/zerotoempire/game/RewardRequestGateTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class RewardRequestGateTest {
    @Test fun requestIsOneShotUntilReleased() {
        val gate = RewardRequestGate()
        assertTrue(gate.request())
        assertFalse(gate.request())
        gate.release()
        assertTrue(gate.request())
    }

    @Test fun consumeRequiresPendingRequestAndIsOneShot() {
        val gate = RewardRequestGate()
        assertFalse(gate.consume())
        assertTrue(gate.request())
        assertTrue(gate.consume())
        assertFalse(gate.consume())
        assertFalse(gate.isPending())
    }

    @Test fun releaseIsIdempotent() {
        val gate = RewardRequestGate()
        gate.release()
        gate.release()
        assertFalse(gate.isPending())
        assertTrue(gate.request())
        gate.release()
        gate.release()
        assertFalse(gate.isPending())
    }
}
```

## File: src/test/java/com/zerotoempire/game/RuntimePerformanceInvariantTest.kt
```kotlin
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
```

## File: src/test/java/com/zerotoempire/game/StoreProductResolverTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test

class StoreProductResolverTest {
    @Test
    fun exactKnownProductResolves() {
        assertEquals(StoreProduct.GEM_PACK_SMALL, StoreProductResolver.resolve(listOf("gems_small")))
    }

    @Test
    fun unknownOrAmbiguousProductsNeverResolve() {
        assertNull(StoreProductResolver.resolve(emptyList()))
        assertNull(StoreProductResolver.resolve(listOf("unknown")))
        assertNull(StoreProductResolver.resolve(listOf("gems_small", "gems_medium")))
        assertNull(StoreProductResolver.resolve(listOf("gems_small", "unknown")))
    }
}
```

## File: src/test/java/com/zerotoempire/game/UpgradeProgressionTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class UpgradeProgressionTest {
    @Test
    fun firstTierIsAvailableOnFreshSave() {
        val nodes = UpgradeProgression.nodes(GameState())
        assertTrue(nodes.isNotEmpty())
        assertEquals(UpgradeNodeState.AVAILABLE, nodes.first().state)
        if (nodes.size > 1) assertEquals(UpgradeNodeState.LOCKED, nodes[1].state)
    }

    @Test
    fun investingUnlocksNextTierWithoutNewSaveFields() {
        val first = Upgrades.catalog.first()
        val state = GameState(upgradeRanks = mapOf(first.id to 1))
        val nodes = UpgradeProgression.nodes(state)
        assertEquals(UpgradeNodeState.IN_PROGRESS, nodes[0].state)
        if (nodes.size > 1) assertEquals(UpgradeNodeState.AVAILABLE, nodes[1].state)
    }

    @Test
    fun masteredUpgradeReportsFullProgress() {
        val first = Upgrades.catalog.first()
        val state = GameState(upgradeRanks = mapOf(first.id to first.maxRank))
        val node = UpgradeProgression.nodes(state).first()
        assertEquals(UpgradeNodeState.MASTERED, node.state)
        assertEquals(1f, node.progress)
    }

    @Test
    fun overallProgressIsBounded() {
        val progress = UpgradeProgression.overallProgress(GameState())
        assertTrue(progress in 0f..1f)
    }
}
```

## File: src/test/java/com/zerotoempire/game/WeeklyChallengeTest.kt
```kotlin
package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import java.time.LocalDate

class WeeklyChallengeTest {
    private val date = LocalDate.of(2026, 8, 18)

    @Test
    fun weeklyCountersUseBaselinesInsteadOfLifetimeTotals() {
        val key = ChallengeRotation.weeklyKey(date)
        val meta = PlayerMeta(
            totalTaps = 10_450,
            totalPurchases = 4_120,
            prestigeCount = 27,
            challengeWeekKey = key,
            challengeWeekTapBase = 10_000,
            challengeWeekPurchaseBase = 4_000,
            challengeWeekPrestigeBase = 26
        )
        val challenges = ChallengeRotation.current(GameState(), meta, date)

        assertEquals(450.0, challenges.first { it.metric == ChallengeMetric.TAPS }.progress, 0.0)
        assertEquals(120.0, challenges.first { it.metric == ChallengeMetric.PURCHASES }.progress, 0.0)
        assertEquals(1.0, challenges.first { it.metric == ChallengeMetric.PRESTIGES }.progress, 0.0)
        assertFalse(challenges.first { it.metric == ChallengeMetric.TAPS }.completed)
    }

    @Test
    fun claimsRemainScopedToIsoWeek() {
        val key = ChallengeRotation.weeklyKey(date)
        val meta = PlayerMeta(
            totalTaps = 600,
            challengeWeekKey = key,
            claimedChallengeIds = setOf("$key:tap")
        )
        val challenge = ChallengeRotation.current(GameState(), meta, date).first { it.metric == ChallengeMetric.TAPS }

        assertTrue(challenge.completed)
        assertTrue(challenge.claimed)
    }
}
```

## File: build.gradle.kts
```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

val sampleAdMobAppId = "ca-app-pub-3940256099942544~3347511713"
val sampleRewardedId = "ca-app-pub-3940256099942544/5224354917"
val sampleInterstitialId = "ca-app-pub-3940256099942544/1033173712"
val adMobAppIdPattern = Regex("^ca-app-pub-[0-9]{16}~[0-9]{10}$")
val adMobAdUnitIdPattern = Regex("^ca-app-pub-[0-9]{16}/[0-9]{10}$")
val productionAdMobAppId = providers.gradleProperty("ADMOB_APP_ID").orElse(sampleAdMobAppId)
val productionRewardedId = providers.gradleProperty("REWARDED_AD_UNIT_ID").orElse("")
val productionInterstitialId = providers.gradleProperty("INTERSTITIAL_AD_UNIT_ID").orElse("")

val versionCodeProperty = providers.gradleProperty("VERSION_CODE").orNull?.trim()
val versionNameProperty = providers.gradleProperty("VERSION_NAME").orNull?.trim()
val releaseVersionCode = when {
    versionCodeProperty == null -> 1
    versionCodeProperty.toIntOrNull() == null || versionCodeProperty.toInt() <= 0 ->
        throw GradleException("VERSION_CODE must be a positive integer.")
    else -> versionCodeProperty.toInt()
}
val releaseVersionName = when {
    versionNameProperty == null -> "0.1.0"
    versionNameProperty.isBlank() -> throw GradleException("VERSION_NAME must not be blank.")
    else -> versionNameProperty
}

val releaseStorePath = providers.environmentVariable("ZERO_EMPIRE_KEYSTORE_PATH").orNull
val releaseStorePassword = providers.environmentVariable("ZERO_EMPIRE_KEYSTORE_PASSWORD").orNull
val releaseKeyAlias = providers.environmentVariable("ZERO_EMPIRE_KEY_ALIAS").orNull
val releaseKeyPassword = providers.environmentVariable("ZERO_EMPIRE_KEY_PASSWORD").orNull
val releaseSigningValues = listOf(
    releaseStorePath,
    releaseStorePassword,
    releaseKeyAlias,
    releaseKeyPassword
)
val hasAnyReleaseSigning = releaseSigningValues.any { !it.isNullOrBlank() }
val hasReleaseSigning = releaseSigningValues.all { !it.isNullOrBlank() }

if (hasAnyReleaseSigning && !hasReleaseSigning) {
    throw GradleException(
        "Incomplete release signing configuration. Set all of " +
            "ZERO_EMPIRE_KEYSTORE_PATH, ZERO_EMPIRE_KEYSTORE_PASSWORD, " +
            "ZERO_EMPIRE_KEY_ALIAS and ZERO_EMPIRE_KEY_PASSWORD, or set none of them."
    )
}

if (hasReleaseSigning && !file(releaseStorePath!!).isFile) {
    throw GradleException("Release keystore file does not exist at ZERO_EMPIRE_KEYSTORE_PATH.")
}

if (hasReleaseSigning) {
    if (versionCodeProperty == null || versionNameProperty == null) {
        throw GradleException(
            "Signed release requires explicit VERSION_CODE and VERSION_NAME Gradle properties."
        )
    }

    val appId = productionAdMobAppId.get().trim()
    val rewardedId = productionRewardedId.get().trim()
    val interstitialId = productionInterstitialId.get().trim()

    if (appId.isBlank() || appId == sampleAdMobAppId || appId.startsWith("ca-app-pub-3940256099942544")) {
        throw GradleException(
            "Signed release requires a production ADMOB_APP_ID. Google's sample/test App ID is not allowed."
        )
    }
    if (!adMobAppIdPattern.matches(appId)) {
        throw GradleException(
            "ADMOB_APP_ID must match ca-app-pub-################~########## for a signed release."
        )
    }
    if (rewardedId.isBlank() || rewardedId == sampleRewardedId || rewardedId.startsWith("ca-app-pub-3940256099942544")) {
        throw GradleException(
            "Signed release requires a production REWARDED_AD_UNIT_ID. Google's sample/test ad unit is not allowed."
        )
    }
    if (!adMobAdUnitIdPattern.matches(rewardedId)) {
        throw GradleException(
            "REWARDED_AD_UNIT_ID must match ca-app-pub-################/########## for a signed release."
        )
    }
    if (interstitialId.isBlank() || interstitialId == sampleInterstitialId || interstitialId.startsWith("ca-app-pub-3940256099942544")) {
        throw GradleException(
            "Signed release requires a production INTERSTITIAL_AD_UNIT_ID. Google's sample/test ad unit is not allowed."
        )
    }
    if (!adMobAdUnitIdPattern.matches(interstitialId)) {
        throw GradleException(
            "INTERSTITIAL_AD_UNIT_ID must match ca-app-pub-################/########## for a signed release."
        )
    }
    if (rewardedId == interstitialId) {
        throw GradleException(
            "REWARDED_AD_UNIT_ID and INTERSTITIAL_AD_UNIT_ID must be different production ad units."
        )
    }
}

android {
    namespace = "com.zerotoempire.game"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.zerotoempire.game"
        minSdk = 26
        targetSdk = 36
        versionCode = releaseVersionCode
        versionName = releaseVersionName

        // Debug/CI can run safely with Google's sample app id. Production can inject the real id
        // through ~/.gradle/gradle.properties or CI secrets without committing credentials.
        manifestPlaceholders["ADMOB_APP_ID"] = productionAdMobAppId.get()
    }

    buildFeatures {
        compose = true
        buildConfig = true
    }

    signingConfigs {
        if (hasReleaseSigning) {
            create("releaseUpload") {
                storeFile = file(releaseStorePath!!)
                storePassword = releaseStorePassword
                keyAlias = releaseKeyAlias
                keyPassword = releaseKeyPassword
            }
        }
    }

    buildTypes {
        debug {
            buildConfigField("String", "REWARDED_AD_UNIT_ID", "\"$sampleRewardedId\"")
            buildConfigField("String", "INTERSTITIAL_AD_UNIT_ID", "\"$sampleInterstitialId\"")
        }
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            if (hasReleaseSigning) {
                signingConfig = signingConfigs.getByName("releaseUpload")
            }
            buildConfigField("String", "REWARDED_AD_UNIT_ID", "\"${productionRewardedId.get()}\"")
            buildConfigField("String", "INTERSTITIAL_AD_UNIT_ID", "\"${productionInterstitialId.get()}\"")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
}

val validateProductionRelease by tasks.registering {
    group = "verification"
    description = "Fails unless all metadata, signing and AdMob values required for a production release are configured."

    doLast {
        if (versionCodeProperty == null || versionNameProperty == null) {
            throw GradleException(
                "Production release requires explicit -PVERSION_CODE and -PVERSION_NAME."
            )
        }
        if (!hasReleaseSigning) {
            throw GradleException(
                "Production release requires ZERO_EMPIRE_KEYSTORE_PATH, ZERO_EMPIRE_KEYSTORE_PASSWORD, " +
                    "ZERO_EMPIRE_KEY_ALIAS and ZERO_EMPIRE_KEY_PASSWORD."
            )
        }
        if (!file(releaseStorePath!!).isFile) {
            throw GradleException("Production release keystore does not exist at ZERO_EMPIRE_KEYSTORE_PATH.")
        }

        val appId = productionAdMobAppId.get().trim()
        val rewardedId = productionRewardedId.get().trim()
        val interstitialId = productionInterstitialId.get().trim()

        if (!adMobAppIdPattern.matches(appId) || appId.startsWith("ca-app-pub-3940256099942544")) {
            throw GradleException("Production release requires a valid non-test ADMOB_APP_ID.")
        }
        if (!adMobAdUnitIdPattern.matches(rewardedId) || rewardedId.startsWith("ca-app-pub-3940256099942544")) {
            throw GradleException("Production release requires a valid non-test REWARDED_AD_UNIT_ID.")
        }
        if (!adMobAdUnitIdPattern.matches(interstitialId) || interstitialId.startsWith("ca-app-pub-3940256099942544")) {
            throw GradleException("Production release requires a valid non-test INTERSTITIAL_AD_UNIT_ID.")
        }
        if (rewardedId == interstitialId) {
            throw GradleException("Production rewarded and interstitial ad unit IDs must be different.")
        }
    }
}

// Deliberately separate from ordinary bundleRelease so CI can keep producing an unsigned
// release artifact while a real store build has one explicit, fail-closed entry point.
val bundleProductionRelease by tasks.registering {
    group = "build"
    description = "Validates production configuration, then builds the signed Play Store release bundle."
    dependsOn(validateProductionRelease)
    dependsOn("bundleRelease")
}

// Android creates variant tasks late in configuration. Configure lazily so ordinary CI
// can still discover bundleRelease while the production gate keeps deterministic ordering.
tasks.configureEach {
    if (name == "bundleRelease") {
        mustRunAfter(validateProductionRelease)
    }
}

dependencies {
    implementation(platform("androidx.compose:compose-bom:2025.08.00"))
    implementation("androidx.activity:activity-compose:1.10.1")
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.9.2")
    implementation("androidx.lifecycle:lifecycle-runtime-compose:2.9.2")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.datastore:datastore-preferences:1.1.7")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")

    implementation("com.android.billingclient:billing:9.1.0")
    implementation("com.google.android.gms:play-services-ads:25.4.0")
    implementation("com.google.android.ump:user-messaging-platform:3.2.0")

    testImplementation("junit:junit:4.13.2")
    debugImplementation("androidx.compose.ui:ui-tooling")
}
```
