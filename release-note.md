## Alne's fork of SM 6.11.0

Monochrome, local-only fork of SteaMidra with a portable Windows build and a polished desktop UI.

### Downloads

- **[Windows] Setup.exe** — recommended Windows installer. Installs per-user, creates shortcuts, and includes the .NET/VC++ runtime checks.
- **[Windows] ZIP** — portable Windows build. Extract and run `Alnes_fork_of_SM.exe`; no installation.
- **[Linux] AppImage** — single-file Linux build. Make it executable and run it.
- **[Linux] ZIP** — AppImage plus `steamidra_install.sh` and the app icon for desktop-menu installation.
- **Source code (zip)** / **Source code (tar.gz)** — GitHub-generated source archives for this tag.

### Highlights

- **Monochrome UI polish** — Pure Dark theme, consistent control sizing, readable accent surfaces, and grayscale branding across the app, splash, tray, and icon.
- **Contribution is opt-in** — provider key contribution and Steam-appinfo enrichment now default to off for new and upgraded settings.
- **Quieter tray** — removed the startup and close-to-tray balloon notifications; the tray menu uses the fork name.
- **Fork identity** — `Alne's fork of SM` across the About dialog, sidebar, and tray; Explorer context menu uses the `AlnesForkOfSM` registry key and removes legacy keys on uninstall.
- **Windows portable build** — no installer required; settings and downloaded data stay alongside the executable.
- **Linux build fixes** — the AppImage now packages and launches the rebuilt `Alnes_fork_of_SM` binary.

### Notes

- The Windows Setup and portable ZIP contain the same application. Choose Setup for shortcuts and uninstall support, or the ZIP to keep everything portable.
- Settings, logs, and local data are not included in the release archives.
