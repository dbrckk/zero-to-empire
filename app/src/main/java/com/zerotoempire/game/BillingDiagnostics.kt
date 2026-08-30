package com.zerotoempire.game

import android.util.Log
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.atomic.AtomicInteger

enum class BillingOperation { CONNECT, PURCHASE_UPDATE, PRODUCT_LOOKUP, LAUNCH, RESTORE, ACKNOWLEDGE, CONSUME, RECOVER_CONSUMABLE }

data class BillingDiagnostic(
    val operation: BillingOperation,
    val responseCode: Int,
    val failureKind: BillingFailureKind
) {
    fun toLogLine(): String = "operation=$operation responseCode=$responseCode category=$failureKind"
}

data class BillingDiagnosticCount(val diagnostic: BillingDiagnostic, val count: Int)

data class BillingDiagnosticSummary(val counts: List<BillingDiagnosticCount>) {
    fun toSupportText(): String = if (counts.isEmpty()) {
        "No Google Play Billing errors recorded during this app session."
    } else {
        buildString {
            appendLine("Google Play Billing errors for this app session:")
            counts.forEach { entry -> appendLine("${entry.diagnostic.toLogLine()} count=${entry.count}") }
        }.trimEnd()
    }
}

fun interface BillingDiagnostics {
    fun record(diagnostic: BillingDiagnostic)
    fun snapshot(): BillingDiagnosticSummary = BillingDiagnosticSummary(emptyList())
}

class InMemoryBillingDiagnostics : BillingDiagnostics {
    private val counts = ConcurrentHashMap<BillingDiagnostic, AtomicInteger>()

    override fun record(diagnostic: BillingDiagnostic) {
        counts.computeIfAbsent(diagnostic) { AtomicInteger() }.incrementAndGet()
    }

    override fun snapshot(): BillingDiagnosticSummary = BillingDiagnosticSummary(
        counts.entries
            .map { BillingDiagnosticCount(it.key, it.value.get()) }
            .sortedWith(compareBy({ it.diagnostic.operation.name }, { it.diagnostic.failureKind.name }, { it.diagnostic.responseCode }))
    )
}

object LocalBillingDiagnostics : BillingDiagnostics {
    private val counter = InMemoryBillingDiagnostics()

    override fun record(diagnostic: BillingDiagnostic) {
        counter.record(diagnostic)
        // Deliberately excludes purchase tokens, order IDs, product IDs and debug messages.
        Log.w("ZeroEmpireBilling", diagnostic.toLogLine())
    }

    override fun snapshot(): BillingDiagnosticSummary = counter.snapshot()
}
