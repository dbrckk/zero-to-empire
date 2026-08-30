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

class PlayBillingGateway(private val context: Context) : PurchaseGateway {
    private var pendingResult: ((PurchaseResult) -> Unit)? = null
    private var pendingProduct: StoreProduct? = null
    private val restoreCallbacks = mutableListOf<(List<StoreProduct>) -> Unit>()
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
                finishPending(PurchaseResult.Failed(result.debugMessage.ifBlank { "Google Play purchase failed" }))
                return@setListener
            }
            if (purchases.isEmpty()) {
                finishPending(PurchaseResult.Failed("Google Play returned no purchase to process"))
                return@setListener
            }

            // A launch callback must only be completed by the product that was actually launched.
            // Billing may occasionally include other owned purchases in an update; processing one of
            // those as the active purchase could grant the wrong entitlement and leave the real flow stuck.
            val target = pendingProduct
            if (pendingResult != null && target != null) {
                val matchingPurchase = purchases.firstOrNull { target.productId in it.products }
                if (matchingPurchase == null) {
                    finishPending(PurchaseResult.Failed("Google Play returned an unexpected product"))
                    return@setListener
                }
                processPurchase(matchingPurchase)
            } else {
                // Purchase updates can also arrive after process/activity recreation. Those have no
                // live UI callback, but still need acknowledgement/recovery handling.
                purchases.forEach(::processPurchase)
            }
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
                    failAllRestores()
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
        // Never retain an Activity/UI callback beyond the gateway lifecycle.
        pendingResult = null
        pendingProduct = null
        if (billingClient.isReady) billingClient.endConnection()
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
                completePending(onResult, PurchaseResult.Failed(result.debugMessage.ifBlank { "Google Play product lookup failed" }))
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
            completePending(onResult, PurchaseResult.Failed(result.debugMessage.ifBlank { "Google Play could not start the purchase" }))
        }
    }

    override fun restore(onResult: (List<StoreProduct>) -> Unit) {
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
                finishRestore(runId, emptyList())
                return@queryPurchasesAsync
            }
            val purchased = PurchaseRecovery.distinctTransactions(
                purchases.filter { it.purchaseState == Purchase.PurchaseState.PURCHASED },
                { it.purchaseToken }
            )
            val permanentOwned = purchased.flatMap { it.products }
                .mapNotNull { id -> StoreProduct.entries.firstOrNull { it.productId == id && !it.consumable } }
                .distinct()
            purchased.filter { purchase -> purchase.products.any { id -> StoreProduct.entries.any { it.productId == id && !it.consumable } } }.forEach { purchase ->
                acknowledge(purchase) { }
            }
            val recoverable = purchased.mapNotNull { purchase ->
                val product = purchase.products.asSequence().mapNotNull { id -> StoreProduct.entries.firstOrNull { it.productId == id && it.consumable } }.firstOrNull()
                if (product == null) null else purchase to product
            }
            if (recoverable.isEmpty()) {
                finishRestore(runId, permanentOwned)
                return@queryPurchasesAsync
            }

            val recovered = mutableListOf<StoreProduct>()
            var remaining = recoverable.size
            recoverable.forEach { (purchase, product) ->
                consumeRecovered(purchase) { success ->
                    if (runId != restoreRunId) return@consumeRecovered
                    if (success) recovered += product
                    remaining--
                    if (remaining == 0) finishRestore(runId, permanentOwned + recovered)
                }
            }
        }
    }

    private fun finishRestore(runId: Long, products: List<StoreProduct>) {
        if (runId != restoreRunId) return
        val callbacks = restoreCallbacks.toList()
        restoreCallbacks.clear()
        restoreInFlight = false
        callbacks.forEachIndexed { index, callback ->
            callback(PurchaseRecovery.deliveryForWaiter(products, index))
        }
    }

    private fun failAllRestores() {
        restoreRunId++
        val callbacks = restoreCallbacks.toList()
        restoreCallbacks.clear()
        restoreInFlight = false
        callbacks.forEach { it(emptyList()) }
    }

    private fun processPurchase(purchase: Purchase) {
        val product = purchase.products.asSequence().mapNotNull { id -> StoreProduct.entries.firstOrNull { it.productId == id } }.firstOrNull()
        if (product == null) {
            if (pendingResult != null) finishPending(PurchaseResult.Failed("Google Play returned an unknown product"))
            return
        }

        when (purchase.purchaseState) {
            Purchase.PurchaseState.PENDING -> {
                // Pending is informational, not terminal. Keep the callback associated with this
                // product so a later PURCHASED update can complete the exact same transaction.
                pendingResult?.invoke(PurchaseResult.Pending)
            }
            Purchase.PurchaseState.PURCHASED -> {
                if (product.consumable) {
                    // If this confirmation arrived after process recreation, no UI callback exists.
                    // Keep the purchase unconsumed so Restore Purchases / next launch can recover it.
                    val callback = pendingResult
                    if (callback != null) consume(purchase, product, callback)
                } else {
                    val callback = pendingResult
                    if (callback == null) {
                        // The purchase may have completed after process recreation. Restore Purchases
                        // remains the source of entitlement recovery; still acknowledge promptly.
                        acknowledge(purchase) { }
                    } else {
                        acknowledge(purchase) { result ->
                            val purchaseResult = if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                                PurchaseResult.Success(product)
                            } else {
                                PurchaseResult.Failed("Google Play could not confirm the purchase: ${result.debugMessage}")
                            }
                            completePending(callback, purchaseResult)
                        }
                    }
                }
            }
            else -> {
                if (pendingResult != null) {
                    finishPending(PurchaseResult.Failed("Google Play returned an unsupported purchase state: ${purchase.purchaseState}"))
                }
            }
        }
    }

    private fun finishPending(result: PurchaseResult) {
        val callback = pendingResult ?: return
        pendingResult = null
        pendingProduct = null
        callback(result)
    }

    private fun completePending(callback: (PurchaseResult) -> Unit, result: PurchaseResult) {
        if (pendingResult !== callback) return
        pendingResult = null
        pendingProduct = null
        callback(result)
    }

    private fun acknowledge(purchase: Purchase, onResult: (BillingResult) -> Unit) {
        if (purchase.isAcknowledged) {
            onResult(BillingResult.newBuilder().setResponseCode(BillingClient.BillingResponseCode.OK).build())
            return
        }
        val params = AcknowledgePurchaseParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.acknowledgePurchase(params, onResult)
    }

    private fun consume(purchase: Purchase, product: StoreProduct, callback: (PurchaseResult) -> Unit) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ ->
            val purchaseResult = if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                PurchaseResult.Success(product)
            } else {
                PurchaseResult.Failed(result.debugMessage.ifBlank { "Google Play could not consume the purchase" })
            }
            completePending(callback, purchaseResult)
        }
    }

    private fun consumeRecovered(purchase: Purchase, done: (Boolean) -> Unit) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ -> done(result.responseCode == BillingClient.BillingResponseCode.OK) }
    }
}
