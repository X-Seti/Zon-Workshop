#!/usr/bin/env python3
#this belongs in apps/components/Zon_Workshop/zon_workshop.py - Version: 1
# X-Seti - May12 2026 - Zon Workshop
"""
Zon Workshop — GTA SA zone/occluder file editor.
Base: RadarWorkshop. Adds .zon / occluder overlay on radar map.
"""

import sys, os
_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if _root not in sys.path: sys.path.insert(0, _root)

from apps.components.Zon_Workshop.radar_workshop import RadarWorkshop

App_name   = "Zon Workshop"
App_build  = "Build 1"
config_key = "zon_workshop"


class ZonWorkshop(RadarWorkshop):
    App_name   = App_name
    App_build  = App_build
    config_key = config_key

    def __init__(self, parent=None, main_window=None):
        super().__init__(parent, main_window)
        self._zon_zones  = []
        self._occluders  = []
    # TODO: _parse_zon_file, _parse_occlu_file, _draw_zone_overlay


def open_zon_workshop(main_window=None):
    from PyQt6.QtWidgets import QApplication
    app = QApplication.instance() or QApplication(sys.argv)
    w = ZonWorkshop(main_window=main_window)
    w.resize(1200, 800); w.show()
    return w
