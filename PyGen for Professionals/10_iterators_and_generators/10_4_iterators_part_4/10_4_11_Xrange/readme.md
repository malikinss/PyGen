# Xrange Class

## Description 📝

The `Xrange` class is an iterator that generates a sequence of numbers in an arithmetic progression, starting from a given `start` value and ending just before the `end` value. The progression increments or decrements by a specified `step` value.
The `step` value defaults to `1`.
Once the sequence reaches the `end` value, the iterator raises a `StopIteration` exception.

## Purpose 🎯

The `Xrange` iterator is useful when you need to generate a sequence of numbers with a specific interval (either positive or negative) that excludes the `end` value.
This is similar to Python's built-in `range`, but it also supports floating-point values and can generate sequences with both positive and negative steps.

## How It Works 🔍

1. **Initialization (`__init__`)**:
    - Takes three arguments: `start`, `end`, and an optional `step` (default is `1`).
    - If no `step` is provided, it defaults to `1`.
2. **Iterator Protocol**:
    - `__iter__()`: Returns the iterator instance itself (`self`).
    - `__next__()`:
        - Returns the next value in the arithmetic progression, calculated by adding the `step` to the `current` value.
        - If the `current` value is outside the range defined by `start` and `end`, it raises a `StopIteration` exception.

## Usage 📦

1. Save the class in a file, e.g., `xrange.py`.
2. Create an instance and iterate through the range:

    ```python
    # Example with integers
    xrange_int = Xrange(0, 10)
    for num in xrange_int:
        print(num)

    # Example with floating-point values
    xrange_float = Xrange(0.1, 1, 0.2)
    for num in xrange_float:
        print(num)
    ```

## Conclusion 🚀

The `Xrange` class is a flexible iterator that allows generating sequences of numbers with custom intervals.
It supports both integers and floating-point numbers, making it more versatile than Python's built-in `range` function.
It is ideal for generating arithmetic progressions with various step sizes and ranges, including negative steps.
