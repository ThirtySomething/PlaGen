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
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../vendor/MDO/MDO/"))

from MDO import MDO

from plagen.plagendefines import PlagenDefines


class PlagenConfig(MDO):

    ############################################################################
    def setup(self: object) -> bool:
        # --- Logging settings ---
        self.add(PlagenDefines.section_logging, PlagenDefines.logging_logfile, f"{PlagenDefines.app_name}.log")
        self.add(PlagenDefines.section_logging, PlagenDefines.logging_loglevel, "info")
        self.add(PlagenDefines.section_logging, PlagenDefines.logging_logstring, "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s:%(funcName)s | %(message)s")

        # --- Program settings ---
        self.add(PlagenDefines.section_program, PlagenDefines.program_playlist_extension, "m3u")
        self.add(PlagenDefines.section_program, PlagenDefines.program_playlist_path, "")
