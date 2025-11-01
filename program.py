"""
******************************************************************************
Copyright 2025 ThirtySomething
******************************************************************************
This file is part of PlaGen.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
******************************************************************************
"""

import logging
import platform

import wx

from plagen.plagenconfig import PlagenConfig
from plagen.plagendefines import PlagenDefines
from plagen.ui.frmmain import FrmMain

PLAGEN_CONFIG = PlagenConfig(f"{PlagenDefines.app_name}.json")
PLAGEN_CONFIG.save()

LOGGER_SETUP = logging.getLogger()
loglevel: str = PLAGEN_CONFIG.value_get(PlagenDefines.section_logging, PlagenDefines.logging_loglevel).upper()
LOGGER_SETUP.setLevel(loglevel)
LOGGER_HANDLER = logging.FileHandler(PLAGEN_CONFIG.value_get(PlagenDefines.section_logging, PlagenDefines.logging_logfile), "w", "utf-8")
LOGGER_HANDLER.setFormatter(logging.Formatter(PLAGEN_CONFIG.value_get(PlagenDefines.section_logging, PlagenDefines.logging_logstring)))
LOGGER_SETUP.addHandler(LOGGER_HANDLER)

if __name__ == "__main__":
    logging.info(f"Starting [{PlagenDefines.app_name}]")
    logging.info(f"Platform [{platform.system()}|{platform.platform()}]")
    logging.info(f"wxPython [{wx.__version__}]")

    try:
        app = wx.App()
        frm = FrmMain(None)
        frm.init_special(PLAGEN_CONFIG)
        frm.Show()
        app.MainLoop()
    except Exception as e:
        logging.exception(f"An error occurred [{e}]")
