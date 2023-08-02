import sys
from loguru import logger

logger.add(
    sys.stdout,
    format="{time} {level} {message}",
    filter="my_module",
    level="INFO",
)

logger.add(
    sys.stderr,
    format="{time} {level} {message}",
    filter="my_module",
    level="INFO",
)

logger.add("tool/loguru/hello_world_loguru/project.log", rotation="12:00")


logger.debug("That's it, beautiful and simple logging!")


def error_handle():
    try:
        1 / 0
    except Exception as e:
        logger.exception("error happend", e)


error_handle()


@logger.catch
def error_with_des(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


error_with_des(0, 0, 0)


logger.info("not catch the exp?")
