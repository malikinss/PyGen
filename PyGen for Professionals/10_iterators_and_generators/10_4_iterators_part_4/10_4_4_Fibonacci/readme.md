# Fibonacci Iterator Class

## Description 📝

The `Fibonacci` class defines an iterator that generates an infinite sequence of Fibonacci numbers, starting from 1.
Each number is the sum of the two preceding ones, following the pattern: 1, 1, 2, 3, 5, 8, 13, ...

## Purpose 🎯

This class is used to generate Fibonacci numbers on-demand using the iterator protocol.
It is ideal for applications that require generating or processing Fibonacci numbers efficiently without needing to store the entire sequence in memory.

## How It Works 🔍

1. **Initialization (`__init__`)**:

    - Starts the sequence with `prev = 0` and `cur = 1`, representing the first two Fibonacci numbers.

2. **Iterator Protocol**:
    - `__iter__()`: Returns the instance itself (needed for the iterator protocol).
    - `__next__()`:
        - Returns the current Fibonacci number (`cur`).
        - Updates `prev` and `cur` to the next two Fibonacci numbers in the sequence, ensuring the sequence continues indefinitely.

## Output 📜

Example usage:

```python
fib = Fibonacci()
for _ in range(5):
    print(next(fib))  # Output: 1, 1, 2, 3, 5
```

## Usage 📦

1. Save the class in a file, e.g., `fibonacci_iterator.py`.
2. Run the following code:
    ```python
    fib = Fibonacci()
    for _ in range(10):
        print(next(fib))
    ```
    **Expected Output:**
    ```
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    ```

## Conclusion 🚀

The `Fibonacci` class provides a simple and memory-efficient way to generate an infinite sequence of Fibonacci numbers.
It adheres to the Python iterator protocol and is perfect for scenarios where Fibonacci numbers are needed in a streaming or lazy evaluation manner. 🧠💡
