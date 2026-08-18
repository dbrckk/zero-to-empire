package com.zerotoempire.game

import android.content.Context
import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioTrack
import java.util.concurrent.atomic.AtomicBoolean
import kotlin.concurrent.thread
import kotlin.math.PI
import kotlin.math.sin

/** Resource-free adaptive soundtrack synthesized at runtime. */
class AdaptiveMusicEngine(context: Context) {
    private val running = AtomicBoolean(false)
    private val foreground = AtomicBoolean(true)
    @Volatile private var intensity = 0
    @Volatile private var volume = .18f
    private var worker: Thread? = null

    private val sampleRate = 22_050
    private val bufferSize = AudioTrack.getMinBufferSize(
        sampleRate,
        AudioFormat.CHANNEL_OUT_STEREO,
        AudioFormat.ENCODING_PCM_16BIT
    ).coerceAtLeast(4096)

    private val track = AudioTrack.Builder()
        .setAudioAttributes(
            AudioAttributes.Builder()
                .setUsage(AudioAttributes.USAGE_GAME)
                .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                .build()
        )
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
        track.play()
        worker = thread(name = "EmpireAdaptiveMusic", isDaemon = true) { renderLoop() }
    }

    fun resumePlayback() {
        if (!running.get() || foreground.getAndSet(true)) return
        runCatching { track.play() }
    }

    fun pausePlayback() {
        if (!running.get() || !foreground.getAndSet(false)) return
        runCatching { track.pause() }
        runCatching { track.flush() }
    }

    fun setEmpireLevel(level: Int) { intensity = level.coerceIn(0, 10) }
    fun setVolume(value: Float) { volume = value.coerceIn(0f, .35f) }

    fun release() {
        foreground.set(false)
        running.set(false)
        worker?.join(250)
        worker = null
        runCatching { track.pause() }
        runCatching { track.flush() }
        track.release()
    }

    private fun renderLoop() {
        val frames = (bufferSize / 4).coerceAtLeast(512)
        val pcm = ShortArray(frames * 2)
        var sampleCursor = 0L
        while (running.get()) {
            if (!foreground.get()) {
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
                val amp = volume.toDouble() * (pad + shimmer + drive)
                val left = (amp * 26_000.0).coerceIn(-32767.0, 32767.0).toInt().toShort()
                val rightPhase = sin(2 * PI * root * 1.0025 * t) * .03 * volume
                val right = ((amp + rightPhase) * 26_000.0).coerceIn(-32767.0, 32767.0).toInt().toShort()
                pcm[frame * 2] = left
                pcm[frame * 2 + 1] = right
                sampleCursor++
            }
            if (foreground.get()) track.write(pcm, 0, pcm.size, AudioTrack.WRITE_BLOCKING)
        }
    }
}

object GameMusicBus {
    @Volatile private var engine: AdaptiveMusicEngine? = null
    fun attach(engine: AdaptiveMusicEngine) { this.engine?.release(); this.engine = engine; engine.start() }
    fun resume() = engine?.resumePlayback() ?: Unit
    fun pause() = engine?.pausePlayback() ?: Unit
    fun setEmpireLevel(level: Int) = engine?.setEmpireLevel(level) ?: Unit
    fun setVolume(volume: Float) = engine?.setVolume(volume) ?: Unit
    fun detach() { engine?.release(); engine = null }
}