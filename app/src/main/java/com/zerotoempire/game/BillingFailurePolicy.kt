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
