import unittest
from concurpy.threading_handler import ThreadingHandler

class TestThreadingHandler(unittest.TestCase):
    def test_handle_task(self):
        threading_handler = ThreadingHandler()

        def task(x):
            return x * 2

        # Running the task through the handler
        result = threading_handler.handle_task(task, 5)
        self.assertEqual(result, 10, "Threading task did not compute correctly")

if __name__ == '__main__':
    unittest.main()
