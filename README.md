

<h1 align="center">Concurpy</h1>

<div align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/dad2jrn/concurpy?color=56BEB8"> <img alt="Github language count" src="https://img.shields.io/github/languages/count/dad2jrn/concurpy?color=56BEB8"> <img alt="Repository size" src="https://img.shields.io/github/repo-size/dad2jrn/concurpy?color=56BEB8"> <img alt="License" src="https://img.shields.io/github/license/dad2jrn/concurpy?color=56BEB8"> <img alt="Github issues" src="https://img.shields.io/github/issues/dad2jrn/concurpy?color=56BEB8"> <img alt="Github Release" src="https://img.shields.io/github/v/release/dad2jrn/concurpy?color=56BEB8"> <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/dad2jrn/concurpy?color=56BEB8"> <img alt="Github stars" src="https://img.shields.io/github/stars/dad2jrn/concurpy?color=56BEB8"> -->
</div>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Concurpy 🚀 Under construction...  🚧
</h4>

<hr> -->

<!-- <p align="center">
  <a href="#about">About</a> &#xa0; | &#xa0;
  <a href="#features">Features</a> &#xa0; | &#xa0;
  <a href="#installation">Installation</a> &#xa0; | &#xa0;
  <a href="#quick_start_guide">Quick Start Guide</a> &#xa0; | &#xa0;
  <a href="#usage">Usage</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/dad2jrn" target="_blank">Author</a>
</p> -->

<br>

## About ##

ConcurPy is a meticulously designed Python library crafted to streamline and simplify the management of concurrency and parallelism in Python applications. As developers grapple with the increasing complexity of modern software development, the need for efficient concurrency management becomes paramount. ConcurPy addresses this challenge by providing a seamless, decorator-based interface that allows developers to effortlessly apply asynchronous programming, multithreading, or multiprocessing to any function or method. This intuitive approach democratizes access to powerful concurrency models, making them accessible even to developers who are not experts in parallel programming.

The core intent behind ConcurPy is to enhance the performance and responsiveness of applications without burdening developers with the intricacies of concurrency mechanisms. By abstracting the complexity behind simple, readable decorators, ConcurPy enables code that is not only faster and more efficient but also cleaner and easier to maintain. Whether handling I/O-bound operations with asyncio, improving responsiveness with threading, or maximizing CPU utilization through multiprocessing, ConcurPy equips developers with the tools to build robust applications that scale gracefully. This project empowers developers to focus more on delivering business value and less on the underlying execution model, fostering innovation and efficiency in Python projects across diverse domains.

## Features ##

ConcurPy is designed with a range of powerful features that cater to the diverse needs of Python developers looking to implement concurrency and parallelism in their applications. Here are some of the main features that highlight its capabilities and advantages:

<div align="left">

1. **Decorator-Based Concurrency**:

    - ConcurPy utilizes a decorator approach to apply concurrency models, making it straightforward to add asynchronous, threading, or multiprocessing capabilities to any function without altering the core logic.

2. **Multiple Concurrency Models**:

- Supports three primary concurrency models:
     - **Async**: Utilizes Python's `asyncio` library for managing asynchronous I/O operations efficiently.
     - **Threading**: Implements multithreading to handle I/O-bound and some CPU-bound operations better.
     - **Multiprocessing**: Leverages multiple processes, making use of additional CPU cores for CPU-intensive tasks, effectively bypassing the Global Interpreter Lock (GIL).

3. **Simple Integration**:
     - The library is designed for easy integration into existing projects. Developers can enable concurrency with minimal configuration and a few lines of code.

4. **Performance Monitoring**:
     - Includes built-in utilities to measure and log the performance of concurrent operations, helping developers optimize their applications and identify bottlenecks.

5. **Advanced Error Handling**:
     - Provides robust error handling capabilities across different concurrency models, ensuring that exceptions are managed gracefully without crashing the application.

6. **Flexible Worker Configuration**:
     - Offers the ability to specify the number of worker threads or processes, giving developers control over resource allocation based on their application's specific needs.

7. **Compatibility with Modern Python**:
    - Fully compatible with modern Python versions, ensuring that developers can leverage the latest features and improvements in the Python ecosystem.

8. **Scalability**:
     - Designed to scale seamlessly from small applications to large, complex systems, making it suitable for both development and production environments.
</div>

These features make ConcurPy a versatile and powerful tool for Python developers aiming to enhance the performance and scalability of their applications through effective concurrency management.

## Installation ##

To install ConcurPy, use pip:

```bash
pip install concurpy
```

## Quick Start Guide ##

Here's how to quickly get started with ConcurPy:

```python
from concurpy import ConcurPy

@ConcurPy(mode='threading', workers=4)
def fetch_data():
    # your function logic here
    pass
```

## Usage ##

ConcurPy simplifies applying concurrency to your functions:

```python
@ConcurPy(mode='multiprocessing', workers=8)
def process_data(data):
    return sum(data)
```

## Contributing ##

Contributions are welcome! Please read our Contributing Guidelines on how to propose bug fixes, improvements, or new features.

## License ##

ConcurPy is made available under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

## Support ##

For support, questions, or more detailed documentation, please visit our official [documentation](docs/documentation.md)

&#xa0;

<a href="#top">Back to top</a>
