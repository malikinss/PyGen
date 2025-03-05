# Square Iterator Class

## Description 📝

The `Square` class defines an iterator that generates the squares of the first `n` natural numbers, starting from `1²`.
After producing `n` squares, it raises a `StopIteration` exception.

## Purpose 🎯

This class is useful for generating a sequence of squared values efficiently while following the iterator protocol.
It ensures controlled iteration, making it useful for mathematical operations, data processing, and algorithm development.

## How It Works 🔍

1. **Initialization (`__init__`)**:

    - Takes `n` (number of squares to generate).
    - Initializes `num` to `0`, which keeps track of the current iteration.

2. **Iterator Protocol**:
    - `__iter__()`: Returns the instance itself.
    - `__next__()`:
        - Increments `num` to move to the next natural number.
        - Returns the square of `num`.
        - Raises `StopIteration` after `n` iterations.

## Output 📜

Example usage:

```python
squares = Square(5)
print(list(squares))  # Output: [1, 4, 9, 16, 25]
```

## Usage 📦

1. Save the class in a file, e.g., `square_iterator.py`.
2. Run the following code:
    ```python
    squares = Square(7)
    for square in squares:
        print(square)
    ```
    **Expected Output:**
    ```
    1
    4
    9
    16
    25
    36
    49
    ```

## Conclusion 🚀

The `Square` class provides a simple yet powerful way to generate square numbers using an iterator.
It follows the Python iterator protocol, ensuring memory efficiency and controlled iteration.
Perfect for mathematical computations! 🧮🔥
