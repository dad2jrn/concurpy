import multiprocessing

class MultiprocessingHandler:
    def __init__(self, workers=4):
        self.pool = multiprocessing.Pool(workers)

    def handle_task(self, func, *args, **kwargs):
        result = self.pool.apply(func, args=args, kwds=kwargs)
        return result
