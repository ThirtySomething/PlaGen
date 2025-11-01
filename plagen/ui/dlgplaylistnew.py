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
        playlist_path: str = self.config.value_get(PlagenDefines.section_program, PlagenDefines.program_playlist_path)
        self.m_textctrl_location.SetValue(playlist_path)

    def playlistname_get(self) -> str:
        return self.playlistname

    def on_btn_abort(self, event: wx.CommandEvent) -> None:
        self.Hide()

    def on_btn_location(self, event: wx.CommandEvent) -> None:
        dlg = wx.DirDialog(None, "Select playlist location", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        dlg.SetPath(self.m_textctrl_location.GetValue())
        if wx.ID_OK == dlg.ShowModal():
            self.m_textctrl_location.SetValue(dlg.GetPath())
        dlg.Destroy()

    def on_btn_save(self, event: wx.CommandEvent) -> None:
        playlist_path: str = self.m_textctrl_location.GetValue()
        playlist_name: str = self.m_textctrl_name.GetValue()
        playlist_extension: str = self.config.value_get(PlagenDefines.section_program, PlagenDefines.program_playlist_extension)
        filename: str = f"{playlist_name}.{playlist_extension}"
        self.playlistname = os.path.join(playlist_path, filename)
        self.config.value_set(PlagenDefines.section_program, PlagenDefines.program_playlist_path, playlist_path)
        self.config.save()
        self.Hide()
