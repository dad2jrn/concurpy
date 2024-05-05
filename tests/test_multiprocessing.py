import unittest
from concurpy.multiprocessing_handler import MultiprocessingHandler

# Define the function at the top level
def test_task(x):
    return x * 2

class TestMultiprocessingHandler(unittest.TestCase):
    def test_handle_task(self):
        multiprocessing_handler = MultiprocessingHandler()

        # Use the top-level function in the handler
        result = multiprocessing_handler.handle_task(test_task, 5)
        self.assertEqual(result, 10, "Multiprocessing task did not compute correctly")

if __name__ == '__main__':
    unittest.main()
