import multiprocessing

class MultiprocessingHandler:
    """
    Handler for managing tasks executed in separate processes, ideal for CPU-intensive operations.

    Attributes:
        pool (multiprocessing.Pool): A pool of worker processes.
    """

    def __init__(self, workers=4):
        """
        Initialize the multiprocessing handler with a specific number of worker processes.

        Parameters:
            workers (int): The number of worker processes in the pool.
        """
        self.pool = multiprocessing.Pool(workers)

    def handle_task(self, func, *args, **kwargs):
        """
        Handle and execute a task in a separate process.

        Parameters:
            func (Callable): The function to execute in a process.
            *args: Argument list for the function.
            **kwargs: Keyword arguments for the function.

        Returns:
            Any: The result of the function execution.
        """
        return self.pool.apply(func, args=args, kwds=kwargs)
