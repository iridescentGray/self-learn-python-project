import os

from loguru import logger

log_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "logs/my_log.log"
)

logger.add(log_path, rotation="12:00")