from .utilities import setup_logging, timing, catch_exceptions
from .async_handler import AsyncHandler
from .threading_handler import ThreadingHandler
from .multiprocessing_handler import MultiprocessingHandler


class ConcurPy:
    def __init__(self, mode="async", workers=4, log_level="INFO"):
        setup_logging(log_level)
        self.mode = mode
        self.workers = workers

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
        def wrapper(*args, **kwargs):
            return self.handler.handle_task(func, *args, **kwargs)

        return wrapper


##TODO: Docstrings and documentation
