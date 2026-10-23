# Alne's fork of SM

> A monochrome, local-only fork of [SteaMidra (SFF)](https://github.com/drappula/SFF).  
> Pure Dark UI, tray control, offline Store — nothing phones home.

A Windows-first fork of SteaMidra that runs as a plain folder. No background service, no telemetry — settings, logs, and caches live next to the executable so the whole thing can be moved anywhere.

---

## Releases

Latest builds from [GitHub Releases](https://github.com/AlneXDev/Alnes-fork-of-SM/releases):

| Asset | What it is |
|---|---|
| **Windows Setup.exe** | Recommended. Installs per-user with Start Menu and desktop shortcuts. |
| **Windows ZIP** | Portable. Extract anywhere and run `Alnes_fork_of_SM.exe`. Keep `_internal` next to it. |
| **Linux AppImage** | Single-file build; make it executable and run it. |
| **Linux ZIP** | AppImage plus the desktop installer script. |

Windows 10 / 11 (x64) required for Windows builds.

---

## What changed

- **Monochrome UI** — grayscale logo/icon, Pure Dark theme, consistent dark/light palette with readable contrast on every built-in theme.
- **Polished controls** — shared tokens for heights, radii, spacing, motion, and elevation.
- **Blank native title bar** — app name lives in the sidebar, tray menu, and About dialog instead.
- **Offline Store & Library** — bundled game catalog loads without network.
- **Opt-in provider keys** — key contribution is off by default; only submits after you enable it.
- **Fork identity** — `AlnesForkOfSM` registry key; uninstaller also removes legacy `SteaMidra`/`SFF` keys.
- **Quieter tray** — no startup balloon, no blue Information badge, no old branding.
- **Close button behavior** — Settings → "Close button behavior" lets you pick hide-to-tray or full exit.

Everything else — manifests, Lua generation, LumaCore setup, DLC unlockers, cloud saves, downloads — is inherited from SteaMidra.

---

## Build from source

Python 3.14 + Windows recommended.

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install steam==1.4.4 --no-deps
python -m PyInstaller build_sff_gui.spec
```

Output lands in `dist\Alnes_fork_of_SM\`.

---

## Credits

Built on [SteaMidra (SFF)](https://github.com/drappula/SFF) by Midrag and contributors. Bundled third-party tools carry their own licenses alongside `third_party_licenses/`.

---

## License & disclaimer

GPL-3.0 — see [LICENSE](LICENSE).

Educational use only; use at your own risk. Not affiliated with Steam and does not replace or crack Steam itself.
