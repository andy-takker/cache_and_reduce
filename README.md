# Cache and Reduce

## TL;DR

This is a Python project demonstrating the implementation of
caching and data reduction strategies in asynchronous Python
applications to enhance performance.

## Overview

The project showcases how to effectively apply caching
mechanisms and request reduction techniques within asynchronous
Python applications. It illustrates methods to cache results
of computationally expensive operations and aggregate data,
thereby reducing system load and improving response times.

## Key Features

- **Asynchronous Caching**: Utilizes [`aiocache`](https://github.com/aio-libs/aiocache) to store results of asynchronous operations, preventing the need to recompute resource-intensive tasks.
- **Data Reduction**: Implements data aggregation and processing techniques to minimize data volume, enchancing efficiency in subsequent operations

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/andy-takker/cache_and_reduce.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cache_and_reduce
   ```

3. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

## Usage

1. Activate the virtual environment:

   ```bash
   poetry shell
   ```

2. Run the main script:

   ```bash
   python -m cache_and_reduce
   ```

## Requirements

- Python 3.7 or higher
- Poetry for dependency management

## Project Structure

```
cache_and_reduce/
├── clients
│   ├── bar
│   │   ├── cached.py
│   │   ├── client.py
│   │   ├── countered.py
│   │   ├── __init__.py
│   │   └── reduced.py
│   ├── foo.py
│   └── __init__.py
├── __init__.py
├── interfaces
│   ├── bar_client.py
│   ├── foo_client.py
│   └── __init__.py
├── __main__.py
├── servers
│   ├── bar.py
│   ├── foo.py
│   └── __init__.py
└── utils
    ├── cache.py
    ├── counter.py
    ├── __init__.py
    └── reduce.py
```

- `./clients/`: bar clients - real, countered, cached, reduced
- `./interfaces/`: abstract interfaces for project
- `./servers/`: `foo` and `bar` example servers for testing
- `./utils/`: decorators for caching, countering and reducing
