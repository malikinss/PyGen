# RandomNumbers Class

## Description 📝

The `RandomNumbers` class is an iterator that generates a sequence of `n` random numbers within a given range [left, right] inclusive.
The sequence is finite, and once `n` numbers have been generated, it raises a `StopIteration` exception.

## Purpose 🎯

This iterator can be useful when there is a need to generate a specific number of random values within a defined range, such as for simulations, random sampling, or games.

## How It Works 🔍

1. **Initialization (`__init__`)**:
    - Takes three arguments: `left` (lower bound), `right` (upper bound), and `n` (number of random values).
    - Checks for invalid values (e.g., if `left > right` or `n <= 0`).
2. **Iterator Protocol**:
    - `__iter__()`: Returns the iterator instance itself (`self`).
    - `__next__()`:
        - Returns the next random number in the sequence.
        - When `n` numbers have been generated, raises `StopIteration`.

## Output 📜

Example usage:

```python
random_gen = RandomNumbers(1, 10, 5)
for num in random_gen:
    print(num, end=' ')
```

**Expected Output:**

```
3 7 1 9 5  # Example, actual numbers will vary
```

## Usage 📦

1. Save the class in a file, e.g., `random_numbers.py`.
2. Create an instance and iterate to generate random numbers:
    ```python
    random_gen = RandomNumbers(1, 100, 10)
    for num in random_gen:
        print(num)
    ```

## Conclusion 🚀

The `RandomNumbers` iterator provides a controlled way to generate a sequence of random numbers within a given range, which can be used in various applications that require random sampling.
