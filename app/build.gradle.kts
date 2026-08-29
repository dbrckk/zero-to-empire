plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

val sampleAdMobAppId = "ca-app-pub-3940256099942544~3347511713"
val sampleRewardedId = "ca-app-pub-3940256099942544/5224354917"
val sampleInterstitialId = "ca-app-pub-3940256099942544/1033173712"
val productionAdMobAppId = providers.gradleProperty("ADMOB_APP_ID").orElse(sampleAdMobAppId)
val productionRewardedId = providers.gradleProperty("REWARDED_AD_UNIT_ID").orElse("")
val productionInterstitialId = providers.gradleProperty("INTERSTITIAL_AD_UNIT_ID").orElse("")

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

android {
    namespace = "com.zerotoempire.game"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.zerotoempire.game"
        minSdk = 26
        targetSdk = 36
        versionCode = 1
        versionName = "0.1.0"

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
