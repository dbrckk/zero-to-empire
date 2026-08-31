package com.zerotoempire.game

import android.app.Activity

/** Conservative lifecycle gate shared by full-screen ad surfaces.
 * A finishing/destroyed Activity must never be handed to an ad SDK because
 * configuration changes and background transitions can invalidate it between
 * preload and show.
 */
internal fun Activity.canHostFullScreenAd(): Boolean = !isFinishing && !isDestroyed
