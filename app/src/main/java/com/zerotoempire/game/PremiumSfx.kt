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
    fun attach(engine: PremiumSfxEngine) { this.engine?.release(); this.engine = engine }
    fun play(cue: PremiumSfxCue, volume: Float = 1f) = engine?.play(cue, volume) ?: Unit
    fun detach() { engine?.release(); engine = null }
}
