# Timecyc Workshop — TODO

---

## High Priority

- [ ] **Save verification** — reload saved file and compare row count/values to confirm round-trip integrity
- [ ] **Undo/redo** — track field edits with undo stack (currently no undo on colour changes)
- [ ] **Cell colour picker** — click swatch to open QColorDialog for direct RGB picking
- [ ] **Fog overlay in sky preview** — show fog start distance as a white overlay at the horizon

---

## Conversion & Import/Export

- [ ] **Export button** — save current game's timecyc to a different format (wire to convert dialog with pre-selected target)
- [ ] **Import button** — open a timecyc from any game and auto-convert to current game's layout
- [ ] **Batch convert** — drag-and-drop multiple files, convert all to a target game
- [ ] **GTA IV timecyc** — XML format parser (completely different structure from III/VC/SA)
- [ ] **GTA V timecyc** — XML/meta format

---

## UI Improvements

- [ ] **Weather column colour coding** — tint column header background with the noon sky colour for that weather
- [ ] **Time row labels** — show actual clock times more clearly (SA: Midnight/5AM/6AM/7AM/Noon/7PM/8PM/10PM)
- [ ] **Heatmap mode** — option to colour cells by a single scalar field (fog, shadow strength etc.) instead of sky top
- [ ] **Copy weather** — right-click column → copy all 24 time slots to another weather column
- [ ] **Interpolate** — fill missing time slots by interpolating between two selected rows
- [ ] **Compare mode** — side-by-side diff of two timecyc files (e.g. timecyc vs timecycp)

---

## Sky Preview

- [ ] **Sun position** — move sun across sky based on time slot (left=morning, centre=noon, right=evening)
- [ ] **Cloud colour** — draw a cloud shape tinted with lower clouds RGB
- [ ] **Water strip** — show water colour at the bottom of the preview
- [ ] **Ambient overlay** — tint the preview with ambient light colour

---

## Future / Speculative

- [ ] **GTA IV XML timecyc** — separate parser, mapped to same UI
- [ ] **Live in-game preview** — CLEO/script bridge to apply timecyc values to a running SA instance
- [ ] **Weather preset library** — save/load named weather presets, share as JSON
- [ ] **Timecyc randomiser** — generate stylised timecyc (noir, sunset, desert etc.) from palette
