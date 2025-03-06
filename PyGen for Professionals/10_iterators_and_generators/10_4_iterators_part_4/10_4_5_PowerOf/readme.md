# PowerOf Iterator Class

## Description 📝

The `PowerOf` class defines an iterator that generates an infinite sequence of nonnegative integer powers of a given nonzero number.
The sequence starts with the 0th power and continues with increasing powers in ascending order (e.g., `num^0, num^1, num^2, ...`).

## Purpose 🎯

This iterator allows for generating powers of a given number on-demand, starting from the 0th power and continuing indefinitely.
It’s useful for scenarios where a continuous sequence of powers is needed without precomputing or storing them.

## How It Works 🔍

1. **Initialization (`__init__`)**:

    - Takes a nonzero number and raises a `ValueError` if the number is zero (since powers of zero are undefined).
    - Initializes `exp` to 0, so the first power returned is `num^0 = 1`.

2. **Iterator Protocol**:
    - `__iter__()`: Returns the instance itself (necessary for the iterator protocol).
    - `__next__()`:
        - Computes the next power of the given number using `num ** exp`.
        - Increments the exponent (`exp`) for the next call to generate the next power.

## Output 📜

Example usage:

```python
powers_of_2 = PowerOf(2)
for _ in range(5):
    print(next(powers_of_2))  # Output: 1, 2, 4, 8, 16
```

## Usage 📦

1. Save the class in a file, e.g., `power_of_iterator.py`.
2. Run the following code:
    ```python
    powers_of_3 = PowerOf(3)
    for _ in range(6):
        print(next(powers_of_3))
    ```
    **Expected Output:**
    ```
    1
    3
    9
    27
    81
    243
    ```

## Conclusion 🚀

The `PowerOf` class provides an efficient and memory-friendly way to generate an infinite sequence of powers for any nonzero number.
It follows the Python iterator protocol and is ideal for generating powers without precomputing or storing them. ⚡
