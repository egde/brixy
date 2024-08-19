import functools
import logging
import threading

# Thread-local storage for storing the indentation level per thread
thread_local = threading.local()

# Configure the standard logger
logger = logging.getLogger("JobStepLogger")
logger.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()

# Define the custom log format (will be dynamically updated later)
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

def log_step():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Initialize the indentation level if not already set
            if not hasattr(thread_local, "indent_level"):
                thread_local.indent_level = 0


            # Generate the custom format string based on the current indentation level
            indent = " " * 4 * thread_local.indent_level  # 4 spaces per indent level
            format_string = (
                "%(asctime)s | %(levelname)-8s | %(state)-9s | %(func_name)-50.50s | %(message)s"
            )
            formatter = logging.Formatter(format_string)
            console_handler.setFormatter(formatter)

            # Increment the indentation level before running the function
            thread_local.indent_level += 1

            logger.info(f"{indent}🏃‍♀️ Running {func.__name__}", extra={'state':'RUNNING', 'func_name': func.__qualname__})
            try:
                value = func(*args, **kwargs)
            except Exception as e:
                logger.exception(f"{indent}❌ Failed running {func.__name__} - {e}", extra={'state':'FAIL', 'func_name': func.__qualname__})
                raise e
            logger.info(f"{indent}✅ Completed running {func.__name__}", extra={'state':'COMPLETED', 'func_name': func.__qualname__})

            # Decrement the indentation level after the function has run
            thread_local.indent_level -= 1

            return value

        return wrapper
    
    return decorator
