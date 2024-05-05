import asyncio
import threading
import multiprocessing
import functools
import logging

class ConcurPy:
    def __init__(self, mode='async', workers=4, log_level='INFO'):
        self.mode = mode
        self.workers = workers
        self.logger = logging.getLogger('ConcurPy')
        self.logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    def __call__(self, func):
        if self.mode == 'async':
            return self.async_wrapper(func)
        elif self.mode == 'threading':
            return self.threading_wrapper(func)
        elif self.mode == 'multiprocessing':
            return self.multiprocessing_wrapper(func)
        else:
            raise ValueError("Unsupported mode. Choose 'async', 'threading', or 'multiprocessing'.")

    def async_wrapper(self, func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                return await asyncio.to_thread(func, *args, **kwargs)
            return wrapped

    def threading_wrapper(self, func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = None
            def target():
                nonlocal result
                result = func(*args, **kwargs)
            thread = threading.Thread(target=target)
            thread.start()
            thread.join()
            return result
        return wrapped

    def multiprocessing_wrapper(self, func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            with multiprocessing.Pool(processes=self.workers) as pool:
                result = pool.apply(func, args=args, kwds=kwargs)
            return result
        return wrapped

    ##TODO  possible extending this class for additional functionality