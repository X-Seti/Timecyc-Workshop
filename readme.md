# Timecyc Workshop

**X-Seti — May 2026**  
A standalone and dockable GTA timecyc editor for IMG Factory 1.6.

---

## Overview

Timecyc Workshop reads, displays and edits GTA time-of-day colour cycle files (`timecyc.dat`, `timecycp.dat`). It shows a weather/time colour grid, live sky preview, and per-cell RGB/scalar field editors.

Supports:
- **GTA III / LC** — 40 fields, 8 weathers × 12 time slots
- **GTA Vice City** — 52 fields, 7 weathers × 24 hours
- **GTA San Andreas** — 51 fields (PC) / 52 fields (PSP `timecycp.dat`), 23 weathers × 8 time slots

---

## Standalone Usage

```bash
./launch_timecycle_workshop.py
```

Requires Python 3.10+ and PyQt6.

---

## Features

- **Weather/Time Grid** — colour cells show sky top colour per cell; click any cell to select it
- **Field Editor** — RGB spinboxes + atmosphere scalars update live; Save enabled on first edit
- **Sky Preview** — gradient sky + sun reflecting selected cell's sky top/bottom/sun colours
- **Rotated column headers** — weather names at 90° for compact display; collapses to abbreviations when panel is narrow
- **Convert** — remaps fields between GTA III ↔ VC ↔ SA layouts and saves a new file
- **Export / Import** — for future cross-format operations
- **Dockable** — loads as a tab inside IMG Factory 1.6 with auto-cached file loading from DAT Browser

---

## File Format Notes

| File | Game | Fields | Weathers | Times |
|------|------|--------|----------|-------|
| `timecyc.dat` | GTA III / LC | 40 | 8 | 12 (2-hr steps) |
| `timecyc.dat` | Vice City | 52 | 7 | 24 |
| `timecyc.dat` | San Andreas PC | 51 | 23 | 8 |
| `timecycp.dat` | SA PSP/Mobile | 52 | 23 | 8 |

VC weather order: Sunny, Cloudy, Rainy, Foggy, ExtraSunny, Rainy2, ExtraColours  
SA time slots: Midnight, 5AM, 6AM, 7AM, Noon, 7PM, 8PM, 10PM

---

## Repo Structure

```
apps/
  components/Timecyc_Editor/
    timecyc_workshop.py      ← main workshop class (TimecycWorkshop)
    gui_workshop.py          ← GUIWorkshop base (toolbar, settings, layout)
  methods/
    imgfactory_svg_icons.py  ← SVG icon library
launch_timecycle_workshop.py ← standalone entry point
```

---

## Part of IMG Factory 1.6

Also bundled in [IMG Factory 1.6](https://github.com/X-Seti/Img-Factory-1.6) — accessible via the Weather button in Editing Options or the Welcome screen.
