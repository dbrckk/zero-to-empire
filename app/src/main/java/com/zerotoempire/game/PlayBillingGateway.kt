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

class PlayBillingGateway(
    private val context: Context,
    private val diagnostics: BillingDiagnostics = LocalBillingDiagnostics
) : PurchaseGateway {
    private var pendingResult: ((PurchaseResult) -> Unit)? = null
    private var pendingProduct: StoreProduct? = null
    private var pendingNotifiedToken: String? = null
    private val restoreCallbacks = mutableListOf<(RestoreResult) -> Unit>()
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
                finishPending(billingFailure(result, BillingOperation.PURCHASE_UPDATE, "Google Play purchase failed"))
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
                processPurchase(matchingPurchase, target)
            } else {
                // Purchase updates can also arrive after process/activity recreation. Those have no
                // live UI callback, but still need acknowledgement/recovery handling.
                purchases.forEach { processPurchase(it) }
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
                    failAllRestores(restoreFailure(result, BillingOperation.CONNECT, "Google Play Billing could not connect"))
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
        pendingNotifiedToken = null
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
        pendingNotifiedToken = null
        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(listOf(QueryProductDetailsParams.Product.newBuilder().setProductId(product.productId).setProductType(BillingClient.ProductType.INAPP).build()))
            .build()
        billingClient.queryProductDetailsAsync(params) { result, detailsResult ->
            // Ignore a stale lookup that completed after disconnect or another terminal result.
            if (pendingResult !== onResult || pendingProduct != product) return@queryProductDetailsAsync
            if (result.responseCode != BillingClient.BillingResponseCode.OK) {
                completePending(onResult, billingFailure(result, BillingOperation.PRODUCT_LOOKUP, "Google Play product lookup failed"))
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
            completePending(onResult, billingFailure(result, BillingOperation.LAUNCH, "Google Play could not start the purchase"))
        }
    }

    override fun restore(onResult: (RestoreResult) -> Unit) {
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
                reconnectIfTransient(result)
                finishRestore(runId, RestoreResult.Failed(restoreFailure(result, BillingOperation.RESTORE, "Google Play could not restore purchases")))
                return@queryPurchasesAsync
            }
            val transactions = PurchaseRecovery.distinctTransactions(
                purchases,
                { it.purchaseToken }
            )
            val pendingProducts = transactions
                .filter { it.purchaseState == Purchase.PurchaseState.PENDING }
                .mapNotNull { StoreProductResolver.resolve(it.products) }
                .toSet()
            val purchased = transactions.filter { it.purchaseState == Purchase.PurchaseState.PURCHASED }
            val resolvedPurchases = purchased.mapNotNull { purchase ->
                StoreProductResolver.resolve(purchase.products)?.let { purchase to it }
            }
            val ambiguousPurchases = purchased.size - resolvedPurchases.size
            val permanentOwned = resolvedPurchases.map { it.second }
                .filterNot { it.consumable }
                .distinct()
            resolvedPurchases.filterNot { it.second.consumable }.forEach { (purchase, _) ->
                acknowledge(purchase) { }
            }
            val recoverable = resolvedPurchases.filter { it.second.consumable }
            if (recoverable.isEmpty()) {
                val restoreResult = if (ambiguousPurchases == 0) {
                    RestoreResult.Success(permanentOwned, pendingProducts)
                } else {
                    RestoreResult.Failed(
                        "An ambiguous Google Play transaction was not restored. Contact support if it remains unresolved.",
                        permanentOwned,
                        pendingProducts
                    )
                }
                finishRestore(runId, restoreResult)
                return@queryPurchasesAsync
            }

            val recovered = mutableListOf<StoreProduct>()
            var failedConsumables = 0
            var remaining = recoverable.size
            recoverable.forEach { (purchase, product) ->
                consumeRecovered(purchase) { success ->
                    if (runId != restoreRunId) return@consumeRecovered
                    if (success) recovered += product
                    else failedConsumables++
                    remaining--
                    if (remaining == 0) {
                        val products = permanentOwned + recovered
                        val restoreResult = if (failedConsumables == 0 && ambiguousPurchases == 0) {
                            RestoreResult.Success(products, pendingProducts)
                        } else {
                            val reason = if (ambiguousPurchases > 0) {
                                "An ambiguous Google Play transaction was not restored. Contact support if it remains unresolved."
                            } else {
                                "Some purchases could not be restored. Check your connection and try again."
                            }
                            RestoreResult.Failed(
                                reason,
                                products,
                                pendingProducts
                            )
                        }
                        finishRestore(runId, restoreResult)
                    }
                }
            }
        }
    }

    private fun finishRestore(runId: Long, result: RestoreResult) {
        if (runId != restoreRunId) return
        val callbacks = restoreCallbacks.toList()
        restoreCallbacks.clear()
        restoreInFlight = false
        callbacks.forEachIndexed { index, callback ->
            val products = PurchaseRecovery.deliveryForWaiter(result.products, index)
            callback(when (result) {
                is RestoreResult.Success -> result.copy(products = products)
                is RestoreResult.Failed -> result.copy(products = products)
            })
        }
    }

    private fun failAllRestores(reason: String) {
        restoreRunId++
        val callbacks = restoreCallbacks.toList()
        restoreCallbacks.clear()
        restoreInFlight = false
        callbacks.forEach { it(RestoreResult.Failed(reason)) }
    }

    private fun processPurchase(purchase: Purchase, expectedProduct: StoreProduct? = null) {
        val product = StoreProductResolver.resolve(purchase.products)
        if (product == null || expectedProduct != null && product != expectedProduct) {
            if (pendingResult != null) finishPending(PurchaseResult.Failed("Google Play returned an ambiguous or unexpected product"))
            return
        }

        when (purchase.purchaseState) {
            Purchase.PurchaseState.PENDING -> {
                // Pending is informational, not terminal. Google Play may emit the same token more
                // than once while payment is unresolved, so notify the UI once per transaction while
                // retaining the callback for the later PURCHASED transition.
                if (pendingNotifiedToken != purchase.purchaseToken) {
                    pendingNotifiedToken = purchase.purchaseToken
                    pendingResult?.invoke(PurchaseResult.Pending)
                }
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
                                billingFailure(result, BillingOperation.ACKNOWLEDGE, "Google Play could not confirm the purchase", record = false)
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
        pendingNotifiedToken = null
        callback(result)
    }

    private fun completePending(callback: (PurchaseResult) -> Unit, result: PurchaseResult) {
        if (pendingResult !== callback) return
        pendingResult = null
        pendingProduct = null
        pendingNotifiedToken = null
        callback(result)
    }

    private fun acknowledge(purchase: Purchase, onResult: (BillingResult) -> Unit) {
        if (purchase.isAcknowledged) {
            onResult(BillingResult.newBuilder().setResponseCode(BillingClient.BillingResponseCode.OK).build())
            return
        }
        val params = AcknowledgePurchaseParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.acknowledgePurchase(params) { result ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) recordFailure(result, BillingOperation.ACKNOWLEDGE)
            onResult(result)
        }
    }

    private fun consume(purchase: Purchase, product: StoreProduct, callback: (PurchaseResult) -> Unit) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ ->
            val purchaseResult = if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                PurchaseResult.Success(product)
            } else {
                billingFailure(result, BillingOperation.CONSUME, "Google Play could not consume the purchase")
            }
            completePending(callback, purchaseResult)
        }
    }

    private fun consumeRecovered(purchase: Purchase, done: (Boolean) -> Unit) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) recordFailure(result, BillingOperation.RECOVER_CONSUMABLE)
            reconnectIfTransient(result)
            done(result.responseCode == BillingClient.BillingResponseCode.OK)
        }
    }

    private fun billingFailure(
        result: BillingResult,
        operation: BillingOperation,
        fallback: String,
        record: Boolean = true
    ): PurchaseResult.Failed {
        if (record) recordFailure(result, operation)
        val failure = BillingFailurePolicy.resolve(result.failureKind(), result.debugMessage, fallback)
        if (failure.shouldReconnect) connect()
        return PurchaseResult.Failed(failure.message)
    }

    private fun reconnectIfTransient(result: BillingResult) {
        if (BillingFailurePolicy.resolve(result.failureKind(), result.debugMessage, "").shouldReconnect) connect()
    }

    private fun restoreFailure(result: BillingResult, operation: BillingOperation, fallback: String): String {
        recordFailure(result, operation)
        return BillingFailurePolicy.resolve(result.failureKind(), result.debugMessage, fallback).message
    }

    private fun recordFailure(result: BillingResult, operation: BillingOperation) {
        diagnostics.record(BillingDiagnostic(operation, result.responseCode, result.failureKind()))
    }

    private fun BillingResult.failureKind(): BillingFailureKind = when (responseCode) {
        BillingClient.BillingResponseCode.SERVICE_DISCONNECTED -> BillingFailureKind.SERVICE_DISCONNECTED
        BillingClient.BillingResponseCode.SERVICE_UNAVAILABLE -> BillingFailureKind.SERVICE_UNAVAILABLE
        BillingClient.BillingResponseCode.NETWORK_ERROR -> BillingFailureKind.NETWORK_ERROR
        else -> BillingFailureKind.OTHER
    }
}
