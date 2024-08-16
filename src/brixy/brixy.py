import functools
from loguru import logger


def log_step(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        def custom_format(record):
            # Change the function name to something custom
            record["function"] = func.__qualname__.replace("<", "\\<")
            return (
                f"{record['time']:YYYY-MM-DD HH:mm:ss.SSS} | "
                f"{record['level'].name: <8} | "
                f"{record['extra']['state']:1} | "
                f"JobStep:{record['function']} - "
                f"{record['message']}\n"
            )

        # Configure the logger with the custom format
        logger.remove()  # Remove default logger
        logger.add(lambda msg: print(msg, end=""), format=custom_format)

        logger.info(f"Running {func.__name__}", state='🏃‍♀️')
        try:
            value = func(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Failed running {func.__name__} - {e}", state='❌')
            raise e
        logger.info(f"Completed running {func.__name__}", state='✅')
        return value

    return wrapper
