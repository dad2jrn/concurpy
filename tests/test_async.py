import unittest
import asyncio
from concurpy.async_handler import AsyncHandler

class TestAsyncHandler(unittest.TestCase):
    async def test_handle_task(self):
        async_handler = AsyncHandler()

        async def async_task(x):
            return x * 2

        # Running the async task through the handler
        result = await async_handler.handle_task(async_task, 5)
        self.assertEqual(result, 10, "Async task did not compute correctly")

if __name__ == '__main__':
    unittest.main()
