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
