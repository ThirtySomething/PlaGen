import os


class Playlist:

    ############################################################################
    def __init__(self) -> None:
        self.playlist_elements: list[str] = []
        self.playlist_location: str = ""
        self.playlist_name: str = ""
        self.dirty: bool = False

    ############################################################################
    def __str__(self) -> str:
        return self.playlist_fqn_get()

    ############################################################################
    def __repr__(self) -> str:
        return self.__str__()

    ############################################################################
    def is_dirty(self) -> bool:
        return self.dirty

    ############################################################################
    def playlist_clear(self) -> None:
        self.playlist_elements = []
        self.playlist_location = ""
        self.playlist_name = ""
        self.dirty = False

    ############################################################################
    def playlist_elements_append(self, playlist_elements: list[str]) -> None:
        self.playlist_elements.append(playlist_elements)
        self.dirty = True

    ############################################################################
    def playlist_elements_get(self) -> list[str]:
        return self.playlist_elements

    ############################################################################
    def playlist_fqn_get(self) -> str:
        return os.path.join(self.playlist_location, self.playlist_name)

    ############################################################################
    def playlist_location_get(self) -> str:
        return self.playlist_location

    ############################################################################
    def playlist_location_set(self, playlist_location: str) -> None:
        self.playlist_location = playlist_location
        self.dirty = True

    ############################################################################
    def playlist_name_get(self) -> str:
        return self.playlist_name

    ############################################################################
    def playlist_name_set(self, playlist_name: str) -> None:
        self.playlist_name = playlist_name
        self.dirty = True

    ############################################################################
    def playlist_new(self, playlist_name: str, playlist_location: str) -> None:
        self.playlist_clear()
        self.playlist_name_set(playlist_name)
        self.playlist_location_set(playlist_location)
        self.playlist_read()
        self.dirty = False

    ############################################################################
    def playlist_read(self) -> None:
        fqn: str = self.playlist_fqn_get()
        if os.path.exists(fqn):
            with open(fqn, "r", encoding="utf-8") as playlistfile:
                self.playlist_elements = playlistfile.read().splitlines()
