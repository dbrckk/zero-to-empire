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
    private val restoreCallbacks = mutableListOf<(List<StoreProduct>) -> Unit>()
    private var connecting = false
    private var restoreInFlight = false

    private val billingClient = BillingClient.newBuilder(context)
        .setListener { result, purchases ->
            if (result.responseCode == BillingClient.BillingResponseCode.USER_CANCELED) {
                pendingResult?.invoke(PurchaseResult.Cancelled)
                pendingResult = null
                return@setListener
            }
            if (result.responseCode != BillingClient.BillingResponseCode.OK || purchases == null) {
                pendingResult?.invoke(PurchaseResult.Failed(result.debugMessage))
                pendingResult = null
                return@setListener
            }
            purchases.forEach(::processPurchase)
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
                    finishRestore(emptyList())
                }
            }

            override fun onBillingServiceDisconnected() {
                connecting = false
                restoreInFlight = false
            }
        })
    }

    override fun disconnect() {
        restoreCallbacks.clear()
        restoreInFlight = false
        connecting = false
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
        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(listOf(QueryProductDetailsParams.Product.newBuilder().setProductId(product.productId).setProductType(BillingClient.ProductType.INAPP).build()))
            .build()
        billingClient.queryProductDetailsAsync(params) { result, detailsResult ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) {
                onResult(PurchaseResult.Failed(result.debugMessage)); return@queryProductDetailsAsync
            }
            val details = detailsResult.productDetailsList.firstOrNull()
            if (details == null) { onResult(PurchaseResult.Failed("Product is unavailable in Google Play")); return@queryProductDetailsAsync }
            launch(activity, product, details, onResult)
        }
    }

    private fun launch(activity: Activity, product: StoreProduct, details: ProductDetails, onResult: (PurchaseResult) -> Unit) {
        pendingResult = onResult
        val productParams = BillingFlowParams.ProductDetailsParams.newBuilder().setProductDetails(details).build()
        val flowParams = BillingFlowParams.newBuilder().setProductDetailsParamsList(listOf(productParams)).build()
        val result = billingClient.launchBillingFlow(activity, flowParams)
        if (result.responseCode != BillingClient.BillingResponseCode.OK) {
            pendingResult = null
            onResult(PurchaseResult.Failed(result.debugMessage))
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
        val params = QueryPurchasesParams.newBuilder().setProductType(BillingClient.ProductType.INAPP).build()
        billingClient.queryPurchasesAsync(params) { result, purchases ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) {
                finishRestore(emptyList())
                return@queryPurchasesAsync
            }
            val purchased = purchases.filter { it.purchaseState == Purchase.PurchaseState.PURCHASED }
            val permanentOwned = purchased.flatMap { it.products }
                .mapNotNull { id -> StoreProduct.entries.firstOrNull { it.productId == id && !it.consumable } }
                .distinct()
            purchased.filter { purchase -> purchase.products.any { id -> StoreProduct.entries.any { it.productId == id && !it.consumable } } }.forEach(::acknowledge)
            val recoverable = purchased.mapNotNull { purchase ->
                val product = purchase.products.asSequence().mapNotNull { id -> StoreProduct.entries.firstOrNull { it.productId == id && it.consumable } }.firstOrNull()
                if (product == null) null else purchase to product
            }
            if (recoverable.isEmpty()) {
                finishRestore(permanentOwned)
                return@queryPurchasesAsync
            }

            val recovered = mutableListOf<StoreProduct>()
            var remaining = recoverable.size
            recoverable.forEach { (purchase, product) ->
                consumeRecovered(purchase) { success ->
                    if (success) recovered += product
                    remaining--
                    if (remaining == 0) finishRestore(permanentOwned + recovered)
                }
            }
        }
    }

    private fun finishRestore(products: List<StoreProduct>) {
        val callbacks = restoreCallbacks.toList()
        restoreCallbacks.clear()
        restoreInFlight = false
        callbacks.forEachIndexed { index, callback ->
            callback(PurchaseRecovery.deliveryForWaiter(products, index))
        }
    }

    private fun processPurchase(purchase: Purchase) {
        val product = purchase.products.asSequence().mapNotNull { id -> StoreProduct.entries.firstOrNull { it.productId == id } }.firstOrNull() ?: return
        when (purchase.purchaseState) {
            Purchase.PurchaseState.PENDING -> pendingResult?.invoke(PurchaseResult.Pending)
            Purchase.PurchaseState.PURCHASED -> {
                if (product.consumable) {
                    // If this confirmation arrived after process recreation, no UI callback exists.
                    // Keep the purchase unconsumed so Restore Purchases / next launch can recover it.
                    if (pendingResult != null) consume(purchase, product)
                } else {
                    acknowledge(purchase)
                    pendingResult?.invoke(PurchaseResult.Success(product))
                    pendingResult = null
                }
            }
            else -> Unit
        }
    }

    private fun acknowledge(purchase: Purchase) {
        if (purchase.isAcknowledged) return
        val params = AcknowledgePurchaseParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.acknowledgePurchase(params) { }
    }

    private fun consume(purchase: Purchase, product: StoreProduct) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ ->
            if (result.responseCode == BillingClient.BillingResponseCode.OK) pendingResult?.invoke(PurchaseResult.Success(product))
            else pendingResult?.invoke(PurchaseResult.Failed(result.debugMessage))
            pendingResult = null
        }
    }

    private fun consumeRecovered(purchase: Purchase, done: (Boolean) -> Unit) {
        val params = ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        billingClient.consumeAsync(params) { result, _ -> done(result.responseCode == BillingClient.BillingResponseCode.OK) }
    }
}
