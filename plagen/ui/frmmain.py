import logging

from plagen.ui.generated.frmmain import frmmain
from plagen.plagenconfig import PlagenConfig
from plagen.plagendefines import PlagenDefines


class FrmMain(frmmain):
    def __init__(self, *args, **kwargs):
        super(FrmMain, self).__init__(*args, **kwargs)
        self.config: PlagenConfig = None

    def init_special(self, plagenconfig: PlagenConfig) -> None:
        self.config = plagenconfig
        logging.info(f"Config [{self.config}]")
