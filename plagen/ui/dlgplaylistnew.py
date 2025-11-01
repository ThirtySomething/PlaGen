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

import os

from wx import DD_DEFAULT_STYLE, DD_DIR_MUST_EXIST, ID_OK, CommandEvent, DirDialog

from plagen.plagenconfig import PlagenConfig
from plagen.plagendefines import PlagenDefines
from plagen.ui.generated.dlgplaylistnew import dlgplaylistnew


class DlgPlaylistNew(dlgplaylistnew):

    ############################################################################
    def __init__(self, *args, **kwargs):
        super(DlgPlaylistNew, self).__init__(*args, **kwargs)
        self.config: PlagenConfig = None
        self.playlistname: str = ""

    ############################################################################
    def init_special(self, plagenconfig: PlagenConfig) -> None:
        self.config = plagenconfig
        playlist_path: str = self.config.value_get(PlagenDefines.section_program, PlagenDefines.program_playlist_path)
        self.m_textctrl_location.SetValue(playlist_path)

    ############################################################################
    def on_btn_abort(self, event: CommandEvent) -> None:
        self.Hide()

    ############################################################################
    def on_btn_location(self, event: CommandEvent) -> None:
        dlg = DirDialog(None, "Select playlist location", "", DD_DEFAULT_STYLE | DD_DIR_MUST_EXIST)
        dlg.SetPath(self.m_textctrl_location.GetValue())
        if ID_OK == dlg.ShowModal():
            self.m_textctrl_location.SetValue(dlg.GetPath())
        dlg.Destroy()

    ############################################################################
    def on_btn_save(self, event: CommandEvent) -> None:
        playlist_path: str = self.m_textctrl_location.GetValue()
        playlist_name: str = self.m_textctrl_name.GetValue()
        playlist_extension: str = self.config.value_get(PlagenDefines.section_program, PlagenDefines.program_playlist_extension)
        filename: str = f"{playlist_name}.{playlist_extension}"
        self.playlistname = os.path.join(playlist_path, filename)
        self.config.value_set(PlagenDefines.section_program, PlagenDefines.program_playlist_path, playlist_path)
        self.config.save()
        self.Hide()

    ############################################################################
    def playlistname_get(self) -> str:
        return self.playlistname
