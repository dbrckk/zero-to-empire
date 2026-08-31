package com.zerotoempire.game

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent

class MainActivity : ComponentActivity() {
    private lateinit var sfxEngine: PremiumSfxEngine
    private lateinit var musicEngine: AdaptiveMusicEngine

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
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

    override fun onStop() {
        GameMusicBus.pause()
        super.onStop()
    }

    override fun onDestroy() {
        GameMusicBus.detach(musicEngine)
        GameSfxBus.detach(sfxEngine)
        super.onDestroy()
    }
}
