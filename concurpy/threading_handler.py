import threading

class ThreadingHandler:
    def __init__(self, workers=4):
        self.workers = workers

    def handle_task(self, func, *args, **kwargs):
        result = [None]  # To capture the function result from the thread
        def target():
            result[0] = func(*args, **kwargs)
        thread = threading.Thread(target=target)
        thread.start()
        thread.join()
        return result[0]
