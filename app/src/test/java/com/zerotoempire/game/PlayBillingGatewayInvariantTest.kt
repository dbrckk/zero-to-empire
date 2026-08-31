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
