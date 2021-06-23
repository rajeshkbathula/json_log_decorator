import functools, time
import logging
import sys, os
import __main__
from pythonjsonlogger import jsonlogger
import logging_loki

def get_logger(name=None,loki_host=None):
    LOG_FORMAT = f"%(name)s - %(levelname)s - %(asctime)s  - %(message)s"
    if name:
        logger = logging.getLogger(name)
    else:
        name = os.path.basename(__main__.__file__).split('.')[0]
        logger = logging.getLogger(name)
    formatter = jsonlogger.JsonFormatter(LOG_FORMAT)
    if loki_host:
        handler = logging_loki.LokiHandler(
            url=f"{loki_host}/loki/api/v1/push",
            tags={"job": f"{name}"},
            version="1",
        )
    else:
        handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def LogDecorator(logger=get_logger()):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_passed_in_function = [repr(a) for a in args]
            kwargs_passed_in_function = [f"{k}={v!r}" for k, v in kwargs.items()]
            formatted_arguments = ", ".join(args_passed_in_function + kwargs_passed_in_function)
            ts = time.time()
            logger.debug(f"Function :[{func.__name__}] Called with Arguments: [{formatted_arguments}]")
            logger.info(f"Function Called:[{func.__name__}]")
            try:
                val = func(*args, **kwargs)
                te = time.time()
                logger.info(
                    f"Function Ended:[{func.__name__}] timetaken:[{int(te-ts)}] Seconds"
                )
                logger.debug(f"Function Ended:[{func.__name__}] with return value : [{val}]")
                return val
            except:
                issue = "Exception in " + func.__name__
                logger.exception(issue)
                raise
        return wrapper
    return decorator
