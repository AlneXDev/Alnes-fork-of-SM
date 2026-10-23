# Alne's fork of SM

A Windows-first, local-only fork of [SteaMidra (SFF)](https://github.com/drappula/SFF) with a monochrome interface, a portable build, and a few opinionated defaults.

This fork does not run a background service or upload your data. Settings, logs, and caches live next to the executable, so the folder can be moved anywhere.

## Download

Get the latest portable Windows build from [Releases](https://github.com/AlneXDev/Alnes-fork-of-SM/releases). Extract the archive and run `Alnes_fork_of_SM.exe`. Keep the `_internal` folder next to the executable.

Requires Windows 10 or 11 (x64).

## What changed in this fork

- Monochrome interface: grayscale logo and application icon, Pure Dark theme, and a simplified dark/light palette system.
- Polished controls: shared tokens for control heights, radii, spacing, motion, and elevation, with readable contrast on every built-in theme.
- Blank native title bar; the application name stays in the sidebar, tray menu, and About dialog.
- Provider key contribution is **off by default** and only runs after you enable it in Settings -> Provider.
- Explorer context-menu entry uses its own `AlnesForkOfSM` registry key; the uninstaller also removes legacy `SteaMidra` and `SFF` keys.
- Tray notifications no longer show the startup balloon, the blue Information badge, or the old branding.
- Store and Library lists work offline from the bundled game catalog.

Everything else - manifests, Lua generation, LumaCore setup, DLC unlockers, cloud saves, and downloads - is inherited from SteaMidra.

## Build from source

Python 3.14 and Windows are recommended.

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install steam==1.4.4 --no-deps
python -m PyInstaller build_sff_gui.spec
```

The portable build is written to `dist\Alnes_fork_of_SM\`.

## Credits

Based on [SteaMidra (SFF)](https://github.com/drappula/SFF) by Midrag and contributors. Third-party licenses are listed in `third_party_licenses/` and next to the bundled tools.

## License and disclaimer

GPL-3.0. See [LICENSE](LICENSE).

This project is provided for educational use only. Use at your own risk. It does not replace or crack Steam itself.
