# ZERO → EMPIRE release hardening.
# Google Mobile Ads, Billing, UMP, AndroidX and Compose ship consumer rules.
# Keep only app-side classes that may be referenced indirectly by Android tooling/runtime.
-keep class com.zerotoempire.game.MainActivity { *; }

# Preserve meaningful source/line metadata for production crash diagnostics.
-keepattributes SourceFile,LineNumberTable
-renamesourcefileattribute SourceFile

# Kotlin metadata is useful for tooling and does not require broad class retention.
-keepattributes *Annotation*,InnerClasses,EnclosingMethod
