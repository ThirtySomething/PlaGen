import logging
import wx
from plagen.ui.generated.frmmain import frmmain
from plagen.plagenconfig import PlagenConfig
from plagen.plagendefines import PlagenDefines
from plagen.ui.dlgplaylistnew import DlgPlaylistNew


class FrmMain(frmmain):
    def __init__(self, *args, **kwargs):
        super(FrmMain, self).__init__(*args, **kwargs)
        self.config: PlagenConfig = None
        self.SetTitle(PlagenDefines.app_name)

    def app_close(self) -> None:
        dlg = wx.MessageDialog(self, "Do you really want to close this application?", "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            # self.savedata()
            self.Destroy()

    def init_special(self, plagenconfig: PlagenConfig) -> None:
        self.config = plagenconfig
        logging.info(f"Config [{self.config}]")

    def on_app_close(self, event: wx.CommandEvent) -> None:
        self.app_close()

    def on_menu_file_new(self, event: wx.CommandEvent) -> None:
        dlg: DlgPlaylistNew = DlgPlaylistNew(self)
        dlg.init_special(self.config)
        dlg.ShowModal()
        playlistname: str = dlg.playlistname_get()
        if 0 < len(playlistname):
            logging.info(f"New playlist [{playlistname}]")
        dlg.Destroy()

    def on_menu_file_exit(self, event: wx.CommandEvent) -> None:
        self.app_close()
