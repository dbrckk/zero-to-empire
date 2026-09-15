package com.zerotoempire.game

/** Pure idempotence ledger for economy credits keyed by store transaction id. */
class PurchaseCreditLedger(initial: Collection<String> = emptyList()) {
    private val credited = initial.filter { it.isNotBlank() }.toMutableSet()

    /** Returns true exactly once for each non-blank transaction id. */
    fun claim(transactionId: String): Boolean =
        transactionId.isNotBlank() && credited.add(transactionId)

    fun snapshot(): Set<String> = credited.toSet()
}
