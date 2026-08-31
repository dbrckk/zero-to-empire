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
