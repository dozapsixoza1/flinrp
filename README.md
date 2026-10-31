# FLIN RP Mobile Launcher

This repository is the working area for the FLIN RP Android launcher based on the supplied Flinity APK.

## Server target

- Address: `195.18.27.226`
- Port: `3146`
- Display name: `FLIN RP`

## Current source status

The supplied archive `Flinity_flinityRelease29.12.2025.zip` is an APK package, not an Android Studio source project. It contains three DEX files, Android resources, `assets/libsamp.so`, and ARMv7 native libraries including `libGTASA.so` and `libsamp.so`.

The package already contains FLIN-branded resources and server labels such as `FLIN MOBILE #1` and `FLIN MOBILE #2`. The configured target address was not found in the initial static string scan.

## Build status

No APK build is claimed yet. To produce a modified, installable APK safely, the original APK must be decoded, the launcher connection configuration identified and changed, then rebuilt and signed. A GitHub Actions workflow cannot create a valid modified APK from this repository alone until the APK binary is available to the workflow and the correct connection setting has been located.

## Next technical step

Inspect the decompiled launcher code around its server-selection / connection setup and identify how it calls the native client setters `setClientIp` and `setClientPort`. Then apply the FLIN RP host and port and verify the resulting APK on an Android device.
