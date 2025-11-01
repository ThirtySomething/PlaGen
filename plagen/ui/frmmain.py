import logging

from wx import (
    CANCEL,
    DEFAULT_FRAME_STYLE,
    ICON_QUESTION,
    ID_OK,
    MAXIMIZE_BOX,
    OK,
    RESIZE_BORDER,
    CommandEvent,
    MessageDialog,
)

from plagen.plagen import PlaGen
from plagen.plagenconfig import PlagenConfig
from plagen.plagendefines import PlagenDefines
from plagen.ui.dlgplaylistnew import DlgPlaylistNew
from plagen.ui.generated.frmmain import frmmain


class FrmMain(frmmain):

    ############################################################################
    def __init__(self, *args, **kwargs):
        super(FrmMain, self).__init__(*args, **kwargs)
        self.config: PlagenConfig = None
        self.SetTitle(PlagenDefines.app_name)
        self.plagen: PlaGen = None
        self.WindowStyle = DEFAULT_FRAME_STYLE ^ RESIZE_BORDER ^ MAXIMIZE_BOX

    ############################################################################
    def app_close(self) -> None:
        dlg = MessageDialog(self, "Do you really want to close this application?", "Confirm Exit", OK | CANCEL | ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if ID_OK == result:
            self.Destroy()

    ############################################################################
    def app_playlist_new(self) -> None:
        dlg: DlgPlaylistNew = DlgPlaylistNew(self)
        dlg.init_special(self.config)
        dlg.ShowModal()
        playlistname: str = dlg.playlistname_get()
        if 0 < len(playlistname):
            self.plagen.playlist_clear()
            self.plagen.playlist_new(playlistname, self.config.value_get(PlagenDefines.section_program, PlagenDefines.program_playlist_path))
            self.m_textctrl_playlist.SetValue(playlistname)
        dlg.Destroy()

    ############################################################################
    def init_special(self, plagenconfig: PlagenConfig) -> None:
        self.config = plagenconfig
        self.plagen = PlaGen(self.config)
        logging.info(f"Config [{self.config}]")

    ############################################################################
    def on_app_close(self, event: CommandEvent) -> None:
        self.app_close()

    ############################################################################
    def on_btn_playlist_new(self, event: CommandEvent) -> None:
        self.app_playlist_new()

    ############################################################################
    def on_btn_playlist_save(self, event: CommandEvent) -> None:
        logging.info("Not implemented yet")
        event.Skip()

    ############################################################################
    def on_btn_playlist_edit(self, event: CommandEvent) -> None:
        logging.info("Not implemented yet")
        event.Skip()

    ############################################################################
    def on_btn_playlist_revert(self, event: CommandEvent) -> None:
        logging.info("Not implemented yet")
        event.Skip()

    ############################################################################
    def on_menu_file_edit(self, event: CommandEvent) -> None:
        logging.info("Not implemented yet")
        event.Skip()

    ############################################################################
    def on_menu_file_exit(self, event: CommandEvent) -> None:
        self.app_close()

    ############################################################################
    def on_menu_file_new(self, event: CommandEvent) -> None:
        self.app_playlist_new()

    ############################################################################
    def on_menu_file_revert(self, event: CommandEvent) -> None:
        logging.info("Not implemented yet")
        event.Skip()

    ############################################################################
    def on_menu_file_save(self, event: CommandEvent) -> None:
        logging.info("Not implemented yet")
        event.Skip()

    ############################################################################
    def on_menu_file_settings(self, event: CommandEvent) -> None:
        logging.info("Not implemented yet")
        event.Skip()
