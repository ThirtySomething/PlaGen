import logging

from plagen.plagendefines import PlagenDefines
from plagen.plagenconfig import PlagenConfig

PLAGEN_CONFIG = PlagenConfig(f"{PlagenDefines.app_name}.json")
PLAGEN_CONFIG.save()


LOGGER_SETUP = logging.getLogger(PlagenDefines.app_name)
loglevel: str = PLAGEN_CONFIG.value_get(PlagenDefines.section_logging, PlagenDefines.logging_loglevel).upper()
LOGGER_SETUP.setLevel(loglevel)
LOGGER_HANDLER = logging.FileHandler(PLAGEN_CONFIG.value_get(PlagenDefines.section_logging, PlagenDefines.logging_logfile), "w", "utf-8")
LOGGER_HANDLER.setFormatter(logging.Formatter(PLAGEN_CONFIG.value_get(PlagenDefines.section_logging, PlagenDefines.logging_logstring)))
LOGGER_SETUP.addHandler(LOGGER_HANDLER)
