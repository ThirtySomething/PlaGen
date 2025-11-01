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
