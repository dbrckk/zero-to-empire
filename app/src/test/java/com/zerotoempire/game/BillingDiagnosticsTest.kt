package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class BillingDiagnosticsTest {
    @Test
    fun diagnosticLineContainsOnlyTheApprovedFailureShape() {
        val line = BillingDiagnostic(
            BillingOperation.CONSUME,
            responseCode = -1,
            BillingFailureKind.SERVICE_DISCONNECTED
        ).toLogLine()

        assertEquals("operation=CONSUME responseCode=-1 category=SERVICE_DISCONNECTED", line)
        assertFalse(line.contains("token", ignoreCase = true))
        assertFalse(line.contains("order", ignoreCase = true))
        assertFalse(line.contains("product", ignoreCase = true))
    }

    @Test
    fun inMemorySummaryAggregatesWithoutTransactionData() {
        val diagnostics = InMemoryBillingDiagnostics()
        val failure = BillingDiagnostic(BillingOperation.RESTORE, -3, BillingFailureKind.NETWORK_ERROR)
        diagnostics.record(failure)
        diagnostics.record(failure)

        val summary = diagnostics.snapshot()
        val supportText = summary.toSupportText()

        assertEquals(1, summary.counts.size)
        assertEquals(2, summary.counts.single().count)
        assertTrue(supportText.contains("count=2"))
        assertFalse(supportText.contains("token", ignoreCase = true))
        assertFalse(supportText.contains("order", ignoreCase = true))
        assertFalse(supportText.contains("product", ignoreCase = true))
    }
}
