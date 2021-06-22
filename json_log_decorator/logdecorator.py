import functools
import logging
import sys, os, time
from pythonjsonlogger import jsonlogger
import __main__


def get_logger():
    LOG_FORMAT = f"%(name)s - %(levelname)s - %(asctime)s  - %(message)s"
    logger = logging.getLogger(os.path.basename(__main__.__file__))
    # logger = logging.getLogger("trigger-handle-candidates")
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = jsonlogger.JsonFormatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def LogDecorator(logger=get_logger()):
    # logger is the logging object
    # exception is the decorator objects
    # that logs every exception into log file
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ts = time.time()
            logger.info(f"Function Called:[{func.__name__}]")
            try:
                val = func(*args, **kwargs)
                te = time.time()
                logger.info(
                    f"Function Ended:[{func.__name__}] timetaken:[{te-ts}] Seconds"
                )
                return val
            except:
                issue = "exception in " + func.__name__
                logger.exception(issue)
                raise

        return wrapper

    return decorator