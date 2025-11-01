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
