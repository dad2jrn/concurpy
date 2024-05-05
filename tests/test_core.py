import unittest
import asyncio
from concurpy.core import ConcurPy

def compute_sum(data):
    return sum(data)

class TestConcurPy(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.expected_sum = sum(self.data)

    def test_threading_sum(self):
        decorated_func = ConcurPy(mode='threading', workers=2)(compute_sum)
        result = decorated_func(self.data)
        self.assertEqual(result, self.expected_sum, "Threading mode failed to compute the correct sum.")

    def test_multiprocessing_sum(self):
        decorated_func = ConcurPy(mode='multiprocessing', workers=2)(compute_sum)
        result = decorated_func(self.data)
        self.assertEqual(result, self.expected_sum, "Multiprocessing mode failed to compute the correct sum.")

class AsyncTestConcurPy(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.expected_sum = sum(self.data)

    async def test_async_sum(self):
        decorated_func = ConcurPy(mode='async', workers=2)(compute_sum)
        result = await decorated_func(self.data)
        self.assertEqual(result, self.expected_sum, "Async mode failed to compute the correct sum.")

if __name__ == '__main__':
    unittest.main()
