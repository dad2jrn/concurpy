from concurpy.core import ConcurPy

# Example function that calculates the sum of a list
def calculate_sum(data):
    return sum(data)

# Using the ConcurPy decorator to apply threading
@ConcurPy(mode='threading', workers=2)
def threaded_sum(data):
    return calculate_sum(data)

# Using the ConcurPy decorator for multiprocessing
@ConcurPy(mode='multiprocessing', workers=3)
def multiprocessing_sum(data):
    return calculate_sum(data)

# Applying the ConcurPy decorator for asynchronous operations
@ConcurPy(mode='async', workers=4)
async def async_sum(data):
    return calculate_sum(data)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    # Output results from threading
    print("Threaded sum:", threaded_sum(data))

    # Output results from multiprocessing
    print("Multiprocessing sum:", multiprocessing_sum(data))

    # Run async example and output results
    import asyncio
    asyncio.run(async_sum(data))
