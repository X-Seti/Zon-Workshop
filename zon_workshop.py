#!/usr/bin/env python3
#this belongs in zon_workshop.py - Version: 1
# X-Seti - May12 2026 - Zon Workshop
"""
Zon Workshop — GTA SA zone/occluder file editor.
Base: RadarWorkshop (radar map display + tile viewer).
Adds: .zon file parsing, occluder zone overlay on radar map.

Supported files:
  zon/   — zone definition files (SA)
  occlu/ — occluder files (SA)
"""

import sys, os
from pathlib import Path

_depends = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'depends')
if _depends not in sys.path:
    sys.path.insert(0, _depends)

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

# Import radar base
from radar_workshop import RadarWorkshop, RADSettings

App_name   = "Zon Workshop"
App_build  = "Build 1"
App_auth   = "X-Seti"
config_key = "zon_workshop"


class ZonWorkshop(RadarWorkshop):
    """Zon/Occluder editor — extends RadarWorkshop with zone overlay."""

    App_name   = App_name
    App_build  = App_build
    config_key = config_key

    def __init__(self, parent=None, main_window=None):
        super().__init__(parent, main_window)
        self._zon_zones   = []   # list of zone rects
        self._occluders   = []   # list of occluder quads

    # TODO: _parse_zon_file(path)    — parse SA .zon format
    # TODO: _parse_occlu_file(path)  — parse SA occluder format
    # TODO: _draw_zone_overlay()     — draw zones on radar grid (QPainter)
    # TODO: _draw_occluder_overlay() — draw occluder boxes on radar grid


def open_zon_workshop(main_window=None):
    app = QApplication.instance() or QApplication(sys.argv)
    w = ZonWorkshop(main_window=main_window)
    w.resize(1200, 800)
    w.show()
    return w


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ZonWorkshop()
    w.resize(1200, 800)
    w.show()
    sys.exit(app.exec())
