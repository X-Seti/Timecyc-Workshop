# Timecyc Workshop — Changelog

---

## Build 3 — May 2026

### New Features
- SA support: 23 weathers × 8 time slots, all weather names from file headers
- `timecycp.dat` support (SA PSP/Mobile variant, 52 fields)
- Rotated 90° column headers — weather names compact, cells 48px wide
- Convert dialog — remap fields between GTA III ↔ VC ↔ SA and save new file
- Export / Import buttons (stubs, ready for implementation)
- Action button bar in grid header (Convert/Load/Save/Import/Export) — visible when docked, hidden in standalone
- Buttons collapse to abbreviations when left panel < 380px
- Sky preview now game-aware (correct field indices per game)
- `_get_game_layout()` — single source of truth for weather/time counts per game

### Fixes
- `_form_layout` AttributeError on SA file load
- `_rebuild_field_widgets` used wrong layout clear method (QFormLayout vs QVBoxLayout)
- Weather/time row assignment was inverted (time-major vs weather-major)
- `int(float(p))` in parser — handles float values like `1.0` in timecyc
- Toolbar Load/Save/Convert buttons rewired to correct class methods (Qt `checked=bool` signal arg fix)
- `QStyleOptionHeader`, `QSize`, `QDialog`, `QDialogButtonBox` import fixes
- Save sort order corrected to weather-major
- Save button now enables on first field edit

---

## Build 2 — May 2026

### New Features
- VC field indices corrected from GTAMods wiki (SkyTop=[15-17], Dir=[12-14] etc.)
- Grid cell colours use sky top colour (game-aware: SA=[9-11], VC=[15-17])
- GUIWorkshop toolbar hidden when docked; inner chrome removed
- Left panel hidden; grid is the main view
- 2-panel layout: grid left, colour fields + sky preview right

### Fixes
- Parser row ordering fixed to weather-major (all 24h for Sunny first, then Cloudy etc.)
- `TimecycEditor` class renamed to `TimecycWorkshop`
- Launcher fixed: was calling module, not class

---

## Build 1 — May 2026 (initial)

- GTA III / VC parsing, weather/time grid, field editor, sky preview
- Extracted from IMG Factory 1.6 Timecyc_Editor component
- Standalone `launch_timecycle_workshop.py`
