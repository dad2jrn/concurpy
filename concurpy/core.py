import logging
from .utilities import setup_logging, timing, catch_exceptions
from .async_handler import AsyncHandler
from .threading_handler import ThreadingHandler
from .multiprocessing_handler import MultiprocessingHandler


class ConcurPy:
    """
    A class to manage concurrency and parallelism using decorators to simplify function execution across different concurrency models.

    Attributes:
        mode (str): The concurrency model to use ('async', 'threading', 'multiprocessing').
        workers (int): The number of worker threads or processes to use.
        logger (logging.Logger): Configured logger for this class.

    Methods:
        __call__(self, func): A decorator to apply the concurrency model to a function.
    """

    def __init__(self, mode="async", workers=4, log_level="INFO"):
        """
        Initializes the ConcurPy decorator with specified concurrency mode, number of workers, and log level.

        Parameters:
            mode (str): The concurrency mode ('async', 'threading', 'multiprocessing').
            workers (int): The number of workers to use for threading or multiprocessing.
            log_level (str): The logging level name.
        """
        setup_logging(log_level)
        self.mode = mode
        self.workers = workers
        self.logger = logging.getLogger("ConcurPy")

        if mode == "async":
            self.handler = AsyncHandler(workers)
        elif mode == "threading":
            self.handler = ThreadingHandler(workers)
        elif mode == "multiprocessing":
            self.handler = MultiprocessingHandler(workers)
        else:
            raise ValueError(
                "Unsupported mode. Choose 'async', 'threading', or 'multiprocessing'."
            )

    @catch_exceptions
    @timing
    def __call__(self, func):
        """
        Decorator to apply the concurrency model to a function, enabling its execution according to the specified mode.

        Parameters:
            func (Callable): The function to decorate.

        Returns:
            Callable: A wrapped function that when called will execute in the specified concurrency model.
        """

        def wrapper(*args, **kwargs):
            return self.handler.handle_task(func, *args, **kwargs)

        return wrapper
