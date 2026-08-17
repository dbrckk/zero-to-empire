package com.zerotoempire.game

data class Manager(
    val businessId: Int,
    val name: String,
    val title: String,
    val cost: Double,
    val incomeMultiplier: Double = 1.0,
    val hired: Boolean = false
)

object Managers {
    val catalog = listOf(
        Manager(0, "Maya", "Street Hustler", 2_500.0, 1.15),
        Manager(1, "Noah", "Retail Operator", 35_000.0, 1.20),
        Manager(2, "Ava", "Production Chief", 500_000.0, 1.25),
        Manager(3, "Leo", "Factory Director", 8_000_000.0, 1.30),
        Manager(4, "Nova", "Tech Visionary", 180_000_000.0, 1.40),
        Manager(5, "Atlas", "City Architect", 5_000_000_000.0, 1.50),
        Manager(6, "Luna", "Lunar Governor", 300_000_000_000.0, 1.65),
        Manager(7, "Ares", "Martian Chancellor", 25_000_000_000_000.0, 1.80),
        Manager(8, "Sol", "Stellar Engineer", 3.0e15, 2.0),
        Manager(9, "Orion", "Galactic Broker", 4.0e17, 2.25),
        Manager(10, "Vega", "Intergalactic Navigator", 1.2e20, 2.55),
        Manager(11, "Lyra", "Cosmic Fabricator", 5.0e23, 2.90),
        Manager(12, "Axiom", "Reality Systems Architect", 2.0e27, 3.35),
        Manager(13, "Zenith", "Transcendence Director", 8.0e30, 4.00)
    )
}

data class Upgrade(
    val id: String,
    val name: String,
    val description: String,
    val gemCost: Int,
    val maxRank: Int,
    val rank: Int = 0
)

object Upgrades {
    val catalog = listOf(
        Upgrade("tap", "Golden Touch", "+25% tap value per rank", 15, 10),
        Upgrade("income", "Compound Engine", "+10% global income per rank", 25, 20),
        Upgrade("offline", "Deep Automation", "+1 hour offline cap per rank", 20, 8),
        Upgrade("prestige", "Legacy Network", "+8% prestige power per rank", 35, 15)
    )
}
