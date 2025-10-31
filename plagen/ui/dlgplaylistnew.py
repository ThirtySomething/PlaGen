import logging
import wx
import os
from plagen.ui.generated.dlgplaylistnew import dlgplaylistnew
from plagen.plagenconfig import PlagenConfig
from plagen.plagendefines import PlagenDefines


class DlgPlaylistNew(dlgplaylistnew):
    def __init__(self, *args, **kwargs):
        super(DlgPlaylistNew, self).__init__(*args, **kwargs)
        self.config: PlagenConfig = None
        self.playlistname: str = ""
        self.m_textctrl_location.SetEditable(False)

    def init_special(self, plagenconfig: PlagenConfig) -> None:
        self.config = plagenconfig

    def on_btn_abort(self, event: wx.CommandEvent) -> None:
        self.Hide()

    def on_btn_location(self, event: wx.CommandEvent) -> None:
        dlg = wx.DirDialog(None, "Select playlist location", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if wx.ID_OK == dlg.ShowModal():
            self.m_textctrl_location.SetValue(dlg.GetPath())
        dlg.Destroy()

    def on_btn_save(self, event: wx.CommandEvent) -> None:
        filename: str = f"{self.m_textctrl_name.GetValue()}.{self.config.value_get(PlagenDefines.section_program, PlagenDefines.program_playlist_extension)}"
        self.playlistname = os.path.join(self.m_textctrl_location.GetValue(), filename)
        self.Hide()
