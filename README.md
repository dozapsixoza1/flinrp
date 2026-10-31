# FLIN RP Mobile Launcher

Working repository for the FLIN RP Android launcher based on the supplied Flinity package.

## Server target

- Address: `195.18.27.226`
- Port: `3146`
- Display name: `FLIN RP`

## Native library inspection

The repository's `libsamp.so` was inspected by GitHub Actions.

- File size: 1,136,956 bytes
- Format: ELF32, ARM (32-bit ARM / EABI5)
- Build: Android 14, NDK r17c
- Required shared libraries: `liblog.so`, `libc.so`, `libm.so`, `libdl.so`
- SHA-256: `893e4afc3fcded597073a54cddc81fdfae3e12ac21faa1f6fbf9fe2e3703fcf8`

The supplied Flinity package contains two different files named `libsamp.so`:

- `assets/libsamp.so` — 1,169,668 bytes, also ELF32 ARM.
- `lib/armeabi-v7a/libsamp.so` — 4,081,636 bytes; exports the Java native methods `setClientIp` and `setClientPort`.

The FLIN RP library is close in size and ABI to the Flinity **assets** library, but it is not the same binary and its exported-symbol set differs. It does not expose the Java `setClientIp` / `setClientPort` symbols present in Flinity's 4 MB runtime library. Therefore it must **not** be copied over `lib/armeabi-v7a/libsamp.so`. Replacing the assets copy also needs confirmation of the exact asset-loading path before changing the APK.

## Build status

The native inspection workflow is active and completed successfully:
https://github.com/dozapsixoza1/flinrp/actions/runs/41239829158

No modified APK has been built or signed yet. The launcher package still needs its asset-loading path and Java/native connection setup verified before replacing any binary or producing an installable APK.
