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
