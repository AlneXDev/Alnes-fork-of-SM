<p align="center">
  <a href="https://github.com/AlneXDev/Alnes-fork-of-SM/releases/latest">
    <img src="https://img.shields.io/github/v/release/AlneXDev/Alnes-fork-of-SM?color=9333ea&label=Latest&style=for-the-badge" alt="Latest release"/>
  </a>
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux-9333ea?style=for-the-badge" alt="Platform"/>
  <img src="https://img.shields.io/badge/Python-3.14-9333ea?style=for-the-badge" alt="Python 3.14"/>
</p>

<h1 align="center">Alne's fork of SM</h1>

<p align="center">
  A monochrome, local-only fork of <b>SteaMidra (SFF)</b> with Pure Dark UI, tray control, and an offline Store.<br>
  <b>No background service. No telemetry.</b> Settings and caches live next to the executable — move the folder anywhere.
</p>

---

## 📦 Releases

Download the latest build from [GitHub Releases](https://github.com/AlneXDev/Alnes-fork-of-SM/releases):

| Asset | What it does |
|-------|--------------|
| **Windows Setup.exe** | Recommended. Per-user installer with Start Menu and desktop shortcuts. |
| **Windows ZIP** | Portable. Extract anywhere and run `Alnes_fork_of_SM.exe`. Keep `_internal` next to it. |
| **Linux AppImage** | Single-file build. Make it executable and run it. |
| **Linux ZIP** | AppImage plus the desktop installer script. |

Windows 10 / 11 (x64) required for Windows builds.

---

## ✨ What changed

- **Monochrome UI** — grayscale logo/icon, Pure Dark theme, consistent dark/light palette with readable contrast everywhere.
- **Polished controls** — shared tokens for heights, radii, spacing, motion, and elevation.
- **Blank native title bar** — app name stays in the sidebar, tray menu, and About dialog.
- **Offline Store & Library** — bundled game catalog loads without network.
- **Opt-in provider keys** — key contribution is off by default; submits only after you enable it.
- **Quieter tray** — no startup balloon, no blue badge, no old branding.
- **Close button behavior** — Settings → "Close button behavior": hide to tray or full exit.
- **Fork identity** — `AlnesForkOfSM` registry key; uninstaller removes legacy `SteaMidra`/`SFF` keys.

Everything else — manifests, Lua generation, LumaCore setup, DLC unlockers, cloud saves, downloads — is inherited from SteaMidra.

---

## 🛠️ Build from source

Python 3.14 + Windows recommended.

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install steam==1.4.4 --no-deps
python -m PyInstaller build_sff_gui.spec
```

Output: `dist\Alnes_fork_of_SM\`

---

## 📄 Credits & license

Built on [SteaMidra (SFF)](https://github.com/drappula/SFF) by Midrag and contributors.  
Bundled third-party tools carry their own licenses alongside `third_party_licenses/`.

GPL-3.0 — see [LICENSE](LICENSE).

Educational use only; use at your own risk. Not affiliated with Steam and does not replace or crack Steam itself.
