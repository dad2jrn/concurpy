# ConcurPy Library Documentation

ConcurPy is a Python library designed to simplify the management of concurrency and parallelism through easy-to-use decorators. It supports asynchronous programming, threading, and multiprocessing to enhance the performance of Python applications.

## Table of Contents

1. Introduction
2. Getting Started
   - Installation
   - Basic Usage
3. Core Concepts
   - Concurrency Models
   - Decorator Design Pattern
4. API Reference
   - ConcurPy Class
   - Handlers
   - Utility Functions
5. Advanced Usage
   - Configuring Logging
   - Handling Exceptions
   - Measuring Performance
6. Examples
   - Simple Examples
   - Advanced Scenarios
7. FAQ
8. Troubleshooting
9. Contributing
10. License

## Introduction

ConcurPy aims to provide a straightforward interface for Python developers to implement concurrency and parallelism in their applications. By abstracting the complexities of Python's `asyncio`, `threading`, and `multiprocessing`, ConcurPy allows developers to focus on their application logic without worrying about the underlying concurrency model.

## Getting Started

### Installation

To install ConcurPy, run the following command:

`pip install concurpy`

### Basic Usage

To get started with ConcurPy, you can apply the ConcurPy decorator to any function that you want to run concurrently. Specify the concurrency mode (`async`, `threading`, or `multiprocessing`) as follows:

```python
from concurpy import ConcurPy

@ConcurPy(mode='threading', workers=4)
def fetch_data():
    # Function logic here
    pass
```

## Core Concepts

### Concurrency Models
ConcurPy supports three main types of concurrency models:

- **Async:** Utilizes Python's asyncio library for asynchronous I/O operations.
- **Threading:** Implements multithreading for I/O-bound and some CPU-bound operations.
- **Multiprocessing:** Uses multiple processes to handle CPU-intensive tasks by leveraging multiple CPU cores.

### Decorator Design Pattern
ConcurPy uses the decorator design pattern to wrap functions with additional functionality. This approach allows developers to easily toggle between different concurrency models without altering the function logic.

## API Reference

### ConcurPy Class

```python
class ConcurPy:
    def __init__(self, mode='async', workers=4, log_level='INFO'):
        """
        Initialize the ConcurPy decorator.

        Parameters:
        - mode (str): Concurrency mode ('async', 'threading', 'multiprocessing').
        - workers (int): Number of workers to use.
        - log_level (str): Logging level.
        """
```
## Handlers
ConcurPy uses different handlers to manage tasks based on the selected concurrency model:

- AsyncHandler
- ThreadingHandler
- MultiprocessingHandler

Each handler is optimized for its respective concurrency model, ensuring efficient task execution.

### Utility Functions
ConcurPy includes utility functions such as setup_logging, timing, and catch_exceptions to enhance debugging and performance measurement.

## Advanced Usage

### Configuring Logging
ConcurPy allows developers to configure logging to monitor and debug the execution of concurrent operations. The logging level can be set via the ConcurPy constructor.

### Handling Exceptions
Exception handling is critical in concurrent operations. ConcurPy provides mechanisms to catch and log exceptions without halting the application.

### Measuring Performance
The timing utility function can be used to measure and log the execution time of functions, helping in performance optimization.

## Examples

### Simple Examples
Here's a simple example demonstrating how to use ConcurPy with threading:
```python
@ConcurPy(mode='threading', workers=2)
def compute_sum(data):
    return sum(data)
```

## Advanced Scenarios
Advanced usage might involve combining multiple concurrency models in a single application or handling complex data processing tasks.

## FAQ

**Q:** How does ConcurPy handle task scheduling?

**A:** ConcurPy delegates task scheduling to the underlying Python concurrency libraries, using simple abstractions to manage these tasks efficiently.

## Troubleshooting

If you encounter issues with ConcurPy, ensure that your environment is set up correctly and that all dependencies are installed. Check the Python version and compatibility.

## Contributing

Contributions to ConcurPy are welcome! Please refer to the repository's CONTRIBUTING.md file for guidelines on how to submit pull requests, report bugs, or suggest new features.

## License

ConcurPy is released under the MIT License. This license allows free use, modification, and distribution of the library in both commercial and non-commercial settings.