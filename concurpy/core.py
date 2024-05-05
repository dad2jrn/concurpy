import logging
from .async_handler import AsyncHandler
from .threading_handler import ThreadingHandler
from .multiprocessing_handler import MultiprocessingHandler

class ConcurPy:
    def __init__(self, mode='async', workers=4, log_level='INFO'):
        self.mode = mode
        self.workers = workers
        self.logger = logging.getLogger('ConcurPy')
        self.logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

        if mode == 'async':
            self.handler = AsyncHandler(workers)
        elif mode == 'threading':
            self.handler = ThreadingHandler(workers)
        elif mode == 'multiprocessing':
            self.handler = MultiprocessingHandler(workers)
        else:
            raise ValueError("Unsupported mode. Choose 'async', 'threading', or 'multiprocessing'.")

    def __call__(self, func):
        if hasattr(self.handler, 'handle_task'):
            def wrapper(*args, **kwargs):
                return self.handler.handle_task(func, *args, **kwargs)
            return wrapper
        else:
            self.logger.error(f"No handler available for {self.mode}")
            raise NotImplementedError(f"Handler for {self.mode} is not implemented")

# The ConcurPy class can now use any of the specified handlers to manage concurrency,
# with each handler designed for a specific model (async, threading, multiprocessing).
