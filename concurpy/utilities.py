import logging
import time
from functools import wraps

def setup_logging(level=logging.INFO):
    """
    Set up standard logging for the library.

    Parameters:
        level (int): The logging level.
    """
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def timing(func):
    """
    Decorator to measure the execution time of a function.

    Parameters:
        func (Callable): The function to time.

    Returns:
        Callable: The wrapped function with timing.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__} executed in {end - start:.4f} seconds.")
        return result
    return wrapper

def catch_exceptions(func):
    """
    Decorator to catch and log any exceptions occurring in a function.

    Parameters:
        func (Callable): The function to apply exception handling.

    Returns:
        Callable: The wrapped function with exception handling.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception in {func.__name__}: {e}", exc_info=True)
            raise  # Re-raise the exception after logging
    return wrapper
