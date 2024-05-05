import unittest
import logging
# from io import StringIO
from concurpy.utilities import setup_logging, timing, catch_exceptions

class TestUtilities(unittest.TestCase):
    def test_setup_logging(self):
        """Test that the logging setup configures the logging level correctly."""
        with self.assertLogs(level='INFO') as log:
            setup_logging('INFO')
            logging.info("Test logging info level")
        self.assertIn("Test logging info level", log.output[0])

    def test_timing_decorator(self):
        """Test that the timing decorator logs execution time."""
        @timing
        def sample_function(delay):
            import time
            time.sleep(delay)
            return delay

        with self.assertLogs(level='INFO') as log:
            sample_function(0.1)

        self.assertTrue(any("sample_function executed in" in message for message in log.output))

    def test_catch_exceptions(self):
        """Test that exceptions are caught and logged."""
        @catch_exceptions
        def function_that_raises():
            raise ValueError("This is a test exception.")

        with self.assertLogs(level='ERROR') as log:
            self.assertRaises(ValueError, function_that_raises)

        self.assertTrue(any("Exception in function_that_raises:" in message for message in log.output))

if __name__ == '__main__':
    unittest.main()
