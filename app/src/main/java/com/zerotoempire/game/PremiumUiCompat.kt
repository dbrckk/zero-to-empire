package com.zerotoempire.game

/** Legacy shared tab type still referenced by reusable art components. */
enum class GameTab { EMPIRE, MANAGERS, UPGRADES, GOALS }

/** Readability alias used by the premium UI. */
val BulkQuote.cost: Double
    get() = totalCost
