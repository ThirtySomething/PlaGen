import logging

from plagen.plagenconfig import PlagenConfig
from plagen.plagendefines import PlagenDefines
from plagen.playlist import Playlist


class PlaGen:

    ############################################################################
    def __init__(self, plagenconfig: PlagenConfig) -> None:
        self.config: PlagenConfig = plagenconfig
        self.playlist: Playlist = Playlist()

    ############################################################################
    def playlist_clear(self) -> None:
        self.playlist.playlist_clear()

    ############################################################################
    def playlist_new(self, playlist_name: str, playlist_location: str) -> None:
        self.playlist.playlist_new(playlist_name, playlist_location)
        logging.info(f"New playlist [{self.playlist}]")
