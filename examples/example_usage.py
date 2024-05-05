from concurpy.core import ConcurPy

# Example function that calculates the sum of a list
def calculate_sum(data):
    return sum(data)

# Decorate the function with ConcurPy for threading
@ConcurPy(mode='threading', workers=2)
def threaded_sum(data):
    return calculate_sum(data)

# Decorate the function with ConcurPy for multiprocessing
@ConcurPy(mode='multiprocessing', workers=2)
def multiprocessing_sum(data):
    return calculate_sum(data)

# Decorate the function with ConcurPy for asynchronous execution
@ConcurPy(mode='async', workers=2)
async def async_sum(data):
    return calculate_sum(data)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    # Run threading example
    print("Threaded sum:", threaded_sum(data))

    # Run multiprocessing example
    print("Multiprocessing sum:", multiprocessing_sum(data))

    # Run async example
    import asyncio
    result = asyncio.run(async_sum(data))
    print("Async sum:", result)
