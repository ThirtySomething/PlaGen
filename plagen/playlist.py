import os


class Playlist:

    ############################################################################
    def __init__(self) -> None:
        self.playlist_clear()

    ############################################################################
    def __str__(self) -> str:
        fqn: str = os.path.join(self.playlist_location, self.playlist_name)
        measstr: str = f"{fqn}"
        return measstr

    ############################################################################
    def __repr__(self) -> str:
        return self.__str__()

    ############################################################################
    def playlist_clear(self) -> None:
        self.playlist_elements: list[str] = []
        self.playlist_location: str = ""
        self.playlist_name: str = ""

    ############################################################################
    def playlist_elements_append(self, playlist_elements: list[str]) -> None:
        self.playlist_elements.append(playlist_elements)

    ############################################################################
    def playlist_elements_get(self) -> list[str]:
        return self.playlist_elements

    ############################################################################
    def playlist_location_get(self) -> str:
        return self.playlist_location

    ############################################################################
    def playlist_location_set(self, playlist_location: str) -> None:
        self.playlist_location = playlist_location

    ############################################################################
    def playlist_name_get(self) -> str:
        return self.playlist_name

    ############################################################################
    def playlist_name_set(self, playlistname: str) -> None:
        self.playlist_name = playlistname
