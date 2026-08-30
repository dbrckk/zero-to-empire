package com.zerotoempire.game

import android.util.Log

enum class BillingOperation { CONNECT, PURCHASE_UPDATE, PRODUCT_LOOKUP, LAUNCH, RESTORE, ACKNOWLEDGE, CONSUME, RECOVER_CONSUMABLE }

data class BillingDiagnostic(
    val operation: BillingOperation,
    val responseCode: Int,
    val failureKind: BillingFailureKind
) {
    fun toLogLine(): String = "operation=$operation responseCode=$responseCode category=$failureKind"
}

fun interface BillingDiagnostics {
    fun record(diagnostic: BillingDiagnostic)
}

object LocalBillingDiagnostics : BillingDiagnostics {
    override fun record(diagnostic: BillingDiagnostic) {
        // Deliberately excludes purchase tokens, order IDs, product IDs and debug messages.
        Log.w("ZeroEmpireBilling", diagnostic.toLogLine())
    }
}
