from setuptools import setup, find_packages

setup(
    name='ConcurPy',
    version='0.1.0',
    author='dad2jrn',
    author_email='dad2jrn@gmail.com',
    description='ConcurPy is a powerful Python library designed to streamline the management of concurrency and parallelism across your applications. It offers an intuitive set of tools for integrating asynchronous programming, multi-threading, and multi-processing with ease. Using simple decorators, developers can execute code in parallel, manage task priorities, and orchestrate complex asynchronous workflows, all while minimizing boilerplate. Ideal for creating efficient, high-performance web applications and scalable data processing tasks, ConcurPy enables precise control over CPU and I/O operations and adapts to various programming needs with its flexible configuration options.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dad2jrn/concurpy',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # e.g., 'requests', 'aiohttp'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
)
