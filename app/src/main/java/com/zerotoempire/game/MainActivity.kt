package com.zerotoempire.game

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        GameSfxBus.attach(PremiumSfxEngine(applicationContext))
        GameMusicBus.attach(AdaptiveMusicEngine(applicationContext))
        setContent { GrowthRuntimeRoot() }
    }

    override fun onDestroy() {
        GameMusicBus.detach()
        GameSfxBus.detach()
        super.onDestroy()
    }
}
