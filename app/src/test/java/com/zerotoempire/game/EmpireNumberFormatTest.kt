package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test

class EmpireNumberFormatTest {
    @Test fun formatsEarlyEconomy() {
        assertEquals("$10.0", EmpireNumberFormat.money(10.0))
        assertEquals("$1.50K", EmpireNumberFormat.money(1_500.0))
    }

    @Test fun formatsLateEconomyWithoutHugeQiStrings() {
        assertEquals("$2.00Sx", EmpireNumberFormat.money(2.0e21))
        assertEquals("$3.00Oc", EmpireNumberFormat.money(3.0e27))
        assertEquals("$1.20No", EmpireNumberFormat.money(1.2e30))
    }

    @Test fun handlesInfinityDeterministically() {
        assertEquals("$∞", EmpireNumberFormat.money(Double.POSITIVE_INFINITY))
    }
}
