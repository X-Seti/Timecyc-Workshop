#!/usr/bin/env python3
"""
X-Seti - May 2026 - Timecyc Workshop - Root Launcher
#this belongs in root /launch_timecycle_workshop.py - Version: 3
"""
import sys
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

if __name__ == "__main__":
    try:
        print("Timecyc Workshop starting...")
        from PyQt6.QtWidgets import QApplication
        from apps.components.Timecyc_Editor.timecyc_workshop import TimecycWorkshop

        app = QApplication(sys.argv)
        w = TimecycWorkshop()
        w.setWindowTitle("Timecyc Workshop — Standalone")
        w.resize(1280, 860)
        w.show()
        sys.exit(app.exec())

    except ImportError as e:
        print(f"ERROR: Failed to import: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
