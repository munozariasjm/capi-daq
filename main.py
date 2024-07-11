import sys
import os
import time
import pandas as pd
import numpy as np
this_path = os.path.abspath(__file__)
father_path = "C:\\Users\\EMALAB\\Desktop\\TW_DAQ"
sys.path.append(father_path)
from fast_tagger_gui.gui.launching_gui import SimpleGUI
import subprocess
from PyQt5.QtWidgets import QApplication
from threading import Thread
import sys
import os
import json
from PyQt5.QtWidgets import QApplication
from fast_tagger_gui.gui.launching_gui import SimpleGUI
import sys
import os
import json
from PyQt5.QtWidgets import QApplication
from fast_tagger_gui.gui.launching_gui import SimpleGUI

def write_settings(saving_path):
    settings_path = "C:\\Users\\EMALAB\\Desktop\\TW_DAQ\\fast_tagger_gui\\settings.json"
    settings = {"save_path": saving_path}
    with open(settings_path, 'w') as f:
        json.dump(settings, f)

def build_script_command(script_path, save_path, refresh_rate=0.5, is_scanning=False):
    command = f"\"{script_path}\" --save_path \"{save_path}\" --refresh_rate {refresh_rate} --is_scanning {is_scanning}"
    return command

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    SETTINGS_PATH = "C:\\Users\\EMALAB\\Desktop\\TW_DAQ\\fast_tagger_gui\\settings.json"
    PATH_TAGGER_SCRIPT = "C:\\Users\\EMALAB\\Desktop\\TW_DAQ\\fast_tagger_gui\\scripts\\run_tagger.py"
    PATH_TAGGER_PLOTTER = "C:\\Users\\EMALAB\\Desktop\\TW_DAQ\\fast_tagger_gui\\gui\\no_scan_plotter.py"
    PATH_SCAN_SCRIPT = "C:\\Users\\EMALAB\\Desktop\\TW_DAQ\\fast_tagger_gui\\scripts\\run_scan.py"
    PATH_SCANNING_PLOTTER = "C:\\Users\\EMALAB\\Desktop\\TW_DAQ\\fast_tagger_gui\\gui\\scan_plotter.py"

    default_save_path = "C:\\Users\\EMALAB\\Music\\TDC.csv"
    
    plotting_script = PATH_TAGGER_PLOTTER
    tagger_script = build_script_command(PATH_TAGGER_SCRIPT, default_save_path)
    scan_script = build_script_command(PATH_SCAN_SCRIPT, default_save_path, is_scanning=True)
    scanning_plotter = PATH_SCANNING_PLOTTER

    gui = SimpleGUI(plotting_script, tagger_script, scan_script, scanning_plotter)
    gui.show()

    if gui.save_path:
        save_path = gui.save_path
        write_settings(save_path)
    else:
        write_settings(default_save_path)

    sys.exit(app.exec_())