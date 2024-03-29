import sys

from loguru import logger

logging_level = "INFO"

# Delete existing log handlers，because we can't change default logger‘s logger_leve
logger.remove()
logger.add(sink=sys.stderr, level=logging_level)
logger.add("logs/simple.log", level=logging_level, rotation="12:00")
logger.add("logs/error.log", backtrace=False, diagnose=True, level="ERROR")
