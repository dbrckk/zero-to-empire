plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

val sampleAdMobAppId = "ca-app-pub-3940256099942544~3347511713"
val sampleRewardedId = "ca-app-pub-3940256099942544/5224354917"
val sampleInterstitialId = "ca-app-pub-3940256099942544/1033173712"
val adMobAppIdPattern = Regex("^ca-app-pub-[0-9]{16}~[0-9]{10}$")
val adMobAdUnitIdPattern = Regex("^ca-app-pub-[0-9]{16}/[0-9]{10}$")
val productionAdMobAppId = providers.gradleProperty("ADMOB_APP_ID").orElse(sampleAdMobAppId)
val productionRewardedId = providers.gradleProperty("REWARDED_AD_UNIT_ID").orElse("")
val productionInterstitialId = providers.gradleProperty("INTERSTITIAL_AD_UNIT_ID").orElse("")

val versionCodeProperty = providers.gradleProperty("VERSION_CODE").orNull?.trim()
val versionNameProperty = providers.gradleProperty("VERSION_NAME").orNull?.trim()
val releaseVersionCode = when {
    versionCodeProperty == null -> 1
    versionCodeProperty.toIntOrNull() == null || versionCodeProperty.toInt() <= 0 ->
        throw GradleException("VERSION_CODE must be a positive integer.")
    else -> versionCodeProperty.toInt()
}
val releaseVersionName = when {
    versionNameProperty == null -> "0.1.0"
    versionNameProperty.isBlank() -> throw GradleException("VERSION_NAME must not be blank.")
    else -> versionNameProperty
}

val releaseStorePath = providers.environmentVariable("ZERO_EMPIRE_KEYSTORE_PATH").orNull
val releaseStorePassword = providers.environmentVariable("ZERO_EMPIRE_KEYSTORE_PASSWORD").orNull
val releaseKeyAlias = providers.environmentVariable("ZERO_EMPIRE_KEY_ALIAS").orNull
val releaseKeyPassword = providers.environmentVariable("ZERO_EMPIRE_KEY_PASSWORD").orNull
val releaseSigningValues = listOf(
    releaseStorePath,
    releaseStorePassword,
    releaseKeyAlias,
    releaseKeyPassword
)
val hasAnyReleaseSigning = releaseSigningValues.any { !it.isNullOrBlank() }
val hasReleaseSigning = releaseSigningValues.all { !it.isNullOrBlank() }

if (hasAnyReleaseSigning && !hasReleaseSigning) {
    throw GradleException(
        "Incomplete release signing configuration. Set all of " +
            "ZERO_EMPIRE_KEYSTORE_PATH, ZERO_EMPIRE_KEYSTORE_PASSWORD, " +
            "ZERO_EMPIRE_KEY_ALIAS and ZERO_EMPIRE_KEY_PASSWORD, or set none of them."
    )
}

if (hasReleaseSigning && !file(releaseStorePath!!).isFile) {
    throw GradleException("Release keystore file does not exist at ZERO_EMPIRE_KEYSTORE_PATH.")
}

if (hasReleaseSigning) {
    if (versionCodeProperty == null || versionNameProperty == null) {
        throw GradleException(
            "Signed release requires explicit VERSION_CODE and VERSION_NAME Gradle properties."
        )
    }

    val appId = productionAdMobAppId.get().trim()
    val rewardedId = productionRewardedId.get().trim()
    val interstitialId = productionInterstitialId.get().trim()

    if (appId.isBlank() || appId == sampleAdMobAppId || appId.startsWith("ca-app-pub-3940256099942544")) {
        throw GradleException(
            "Signed release requires a production ADMOB_APP_ID. Google's sample/test App ID is not allowed."
        )
    }
    if (!adMobAppIdPattern.matches(appId)) {
        throw GradleException(
            "ADMOB_APP_ID must match ca-app-pub-################~########## for a signed release."
        )
    }
    if (rewardedId.isBlank() || rewardedId == sampleRewardedId || rewardedId.startsWith("ca-app-pub-3940256099942544")) {
        throw GradleException(
            "Signed release requires a production REWARDED_AD_UNIT_ID. Google's sample/test ad unit is not allowed."
        )
    }
    if (!adMobAdUnitIdPattern.matches(rewardedId)) {
        throw GradleException(
            "REWARDED_AD_UNIT_ID must match ca-app-pub-################/########## for a signed release."
        )
    }
    if (interstitialId.isBlank() || interstitialId == sampleInterstitialId || interstitialId.startsWith("ca-app-pub-3940256099942544")) {
        throw GradleException(
            "Signed release requires a production INTERSTITIAL_AD_UNIT_ID. Google's sample/test ad unit is not allowed."
        )
    }
    if (!adMobAdUnitIdPattern.matches(interstitialId)) {
        throw GradleException(
            "INTERSTITIAL_AD_UNIT_ID must match ca-app-pub-################/########## for a signed release."
        )
    }
    if (rewardedId == interstitialId) {
        throw GradleException(
            "REWARDED_AD_UNIT_ID and INTERSTITIAL_AD_UNIT_ID must be different production ad units."
        )
    }
}

android {
    namespace = "com.zerotoempire.game"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.zerotoempire.game"
        minSdk = 26
        targetSdk = 36
        versionCode = releaseVersionCode
        versionName = releaseVersionName

        // Debug/CI can run safely with Google's sample app id. Production can inject the real id
        // through ~/.gradle/gradle.properties or CI secrets without committing credentials.
        manifestPlaceholders["ADMOB_APP_ID"] = productionAdMobAppId.get()
    }

    buildFeatures {
        compose = true
        buildConfig = true
    }

    signingConfigs {
        if (hasReleaseSigning) {
            create("releaseUpload") {
                storeFile = file(releaseStorePath!!)
                storePassword = releaseStorePassword
                keyAlias = releaseKeyAlias
                keyPassword = releaseKeyPassword
            }
        }
    }

    buildTypes {
        debug {
            buildConfigField("String", "REWARDED_AD_UNIT_ID", "\"$sampleRewardedId\"")
            buildConfigField("String", "INTERSTITIAL_AD_UNIT_ID", "\"$sampleInterstitialId\"")
        }
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            if (hasReleaseSigning) {
                signingConfig = signingConfigs.getByName("releaseUpload")
            }
            buildConfigField("String", "REWARDED_AD_UNIT_ID", "\"${productionRewardedId.get()}\"")
            buildConfigField("String", "INTERSTITIAL_AD_UNIT_ID", "\"${productionInterstitialId.get()}\"")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
}

val validateProductionRelease by tasks.registering {
    group = "verification"
    description = "Fails unless all metadata, signing and AdMob values required for a production release are configured."

    doLast {
        if (versionCodeProperty == null || versionNameProperty == null) {
            throw GradleException(
                "Production release requires explicit -PVERSION_CODE and -PVERSION_NAME."
            )
        }
        if (!hasReleaseSigning) {
            throw GradleException(
                "Production release requires ZERO_EMPIRE_KEYSTORE_PATH, ZERO_EMPIRE_KEYSTORE_PASSWORD, " +
                    "ZERO_EMPIRE_KEY_ALIAS and ZERO_EMPIRE_KEY_PASSWORD."
            )
        }
        if (!file(releaseStorePath!!).isFile) {
            throw GradleException("Production release keystore does not exist at ZERO_EMPIRE_KEYSTORE_PATH.")
        }

        val appId = productionAdMobAppId.get().trim()
        val rewardedId = productionRewardedId.get().trim()
        val interstitialId = productionInterstitialId.get().trim()

        if (!adMobAppIdPattern.matches(appId) || appId.startsWith("ca-app-pub-3940256099942544")) {
            throw GradleException("Production release requires a valid non-test ADMOB_APP_ID.")
        }
        if (!adMobAdUnitIdPattern.matches(rewardedId) || rewardedId.startsWith("ca-app-pub-3940256099942544")) {
            throw GradleException("Production release requires a valid non-test REWARDED_AD_UNIT_ID.")
        }
        if (!adMobAdUnitIdPattern.matches(interstitialId) || interstitialId.startsWith("ca-app-pub-3940256099942544")) {
            throw GradleException("Production release requires a valid non-test INTERSTITIAL_AD_UNIT_ID.")
        }
        if (rewardedId == interstitialId) {
            throw GradleException("Production rewarded and interstitial ad unit IDs must be different.")
        }
    }
}

// Deliberately separate from ordinary bundleRelease so CI can keep producing an unsigned
// release artifact while a real store build has one explicit, fail-closed entry point.
val bundleProductionRelease by tasks.registering {
    group = "build"
    description = "Validates production configuration, then builds the signed Play Store release bundle."
    dependsOn(validateProductionRelease)
    dependsOn("bundleRelease")
}

// Android creates variant tasks late in configuration. Configure lazily so ordinary CI
// can still discover bundleRelease while the production gate keeps deterministic ordering.
tasks.configureEach {
    if (name == "bundleRelease") {
        mustRunAfter(validateProductionRelease)
    }
}

dependencies {
    implementation(platform("androidx.compose:compose-bom:2025.08.00"))
    implementation("androidx.activity:activity-compose:1.10.1")
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.9.2")
    implementation("androidx.lifecycle:lifecycle-runtime-compose:2.9.2")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.datastore:datastore-preferences:1.1.7")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")

    implementation("com.android.billingclient:billing:9.1.0")
    implementation("com.google.android.gms:play-services-ads:25.4.0")
    implementation("com.google.android.ump:user-messaging-platform:3.2.0")

    testImplementation("junit:junit:4.13.2")
    debugImplementation("androidx.compose.ui:ui-tooling")
}
