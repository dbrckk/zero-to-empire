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
        .enablePendingPurchases(
            PendingPurchasesParams.newBuilder().enableOneTimeProducts().build()
        )
        .enableAutoServiceReconnection()
        .build()

    override fun connect() {
        if (billingClient.isReady) return
        billingClient.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(result: BillingResult) {
                if (result.responseCode == BillingClient.BillingResponseCode.OK) restore { }
            }
            override fun onBillingServiceDisconnected() = Unit
        })
    }

    override fun disconnect() {
        if (billingClient.isReady) billingClient.endConnection()
    }

    override fun purchase(
        activity: Activity,
        product: StoreProduct,
        onResult: (PurchaseResult) -> Unit
    ) {
        if (!billingClient.isReady) {
            onResult(PurchaseResult.Failed("Google Play Billing is not ready"))
            connect()
            return
        }

        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(
                listOf(
                    QueryProductDetailsParams.Product.newBuilder()
                        .setProductId(product.productId)
                        .setProductType(BillingClient.ProductType.INAPP)
                        .build()
                )
            )
            .build()

        billingClient.queryProductDetailsAsync(params) { result, detailsResult ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) {
                onResult(PurchaseResult.Failed(result.debugMessage))
                return@queryProductDetailsAsync
            }
            val details = detailsResult.productDetailsList.firstOrNull()
            if (details == null) {
                onResult(PurchaseResult.Failed("Product is unavailable in Google Play"))
                return@queryProductDetailsAsync
            }
            launch(activity, product, details, onResult)
        }
    }

    private fun launch(
        activity: Activity,
        product: StoreProduct,
        details: ProductDetails,
        onResult: (PurchaseResult) -> Unit
    ) {
        pendingResult = onResult
        val productParams = BillingFlowParams.ProductDetailsParams.newBuilder()
            .setProductDetails(details)
            .build()
        val flowParams = BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(listOf(productParams))
            .build()
        val result = billingClient.launchBillingFlow(activity, flowParams)
        if (result.responseCode != BillingClient.BillingResponseCode.OK) {
            pendingResult = null
            onResult(PurchaseResult.Failed(result.debugMessage))
        }
    }

    override fun restore(onResult: (Set<StoreProduct>) -> Unit) {
        if (!billingClient.isReady) {
            onResult(emptySet())
            return
        }
        val params = QueryPurchasesParams.newBuilder()
            .setProductType(BillingClient.ProductType.INAPP)
            .build()
        billingClient.queryPurchasesAsync(params) { result, purchases ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) {
                onResult(emptySet())
                return@queryPurchasesAsync
            }
            val owned = purchases
                .filter { it.purchaseState == Purchase.PurchaseState.PURCHASED }
                .flatMap { it.products }
                .mapNotNull { id -> StoreProduct.entries.firstOrNull { it.productId == id && !it.consumable } }
                .toSet()
            purchases.forEach { purchase ->
                if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED && !purchase.isAcknowledged) acknowledge(purchase)
            }
            onResult(owned)
        }
    }

    private fun processPurchase(purchase: Purchase) {
        val product = purchase.products
            .asSequence()
            .mapNotNull { id -> StoreProduct.entries.firstOrNull { it.productId == id } }
            .firstOrNull() ?: return

        when (purchase.purchaseState) {
            Purchase.PurchaseState.PENDING -> {
                pendingResult?.invoke(PurchaseResult.Pending)
                pendingResult = null
            }
            Purchase.PurchaseState.PURCHASED -> {
                if (product.consumable) consume(purchase, product) else {
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
        val params = AcknowledgePurchaseParams.newBuilder()
            .setPurchaseToken(purchase.purchaseToken)
            .build()
        billingClient.acknowledgePurchase(params) { }
    }

    private fun consume(purchase: Purchase, product: StoreProduct) {
        val params = ConsumeParams.newBuilder()
            .setPurchaseToken(purchase.purchaseToken)
            .build()
        billingClient.consumeAsync(params) { result, _ ->
            if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                pendingResult?.invoke(PurchaseResult.Success(product))
            } else {
                pendingResult?.invoke(PurchaseResult.Failed(result.debugMessage))
            }
            pendingResult = null
        }
    }
}
