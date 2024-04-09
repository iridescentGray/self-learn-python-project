import functools

from loguru import logger


def logger_wraps(*, entry=True, exit=True, level="DEBUG"):
    """Logging entry and exit of functions


    Args:
        entry (bool, optional): _description_. Defaults to True.
        exit (bool, optional): _description_. Defaults to True.
        level (str, optional): _description_. Defaults to "DEBUG".
    """

    def wrapper(func):
        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)
            if entry:
                logger_.log(
                    level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs
                )
            result = func(*args, **kwargs)
            if exit:
                logger_.log(level, "Exiting '{}' (result={})", name, result)
            return result

        return wrapped

    return wrapper
