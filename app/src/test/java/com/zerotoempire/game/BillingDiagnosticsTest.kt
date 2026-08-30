package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
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
}
