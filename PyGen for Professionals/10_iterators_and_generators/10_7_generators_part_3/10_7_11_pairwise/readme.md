# `pairwise()`: Generator for Pairing Consecutive Elements

## Description 📝

The `pairwise()` function is a generator that iterates over an iterable and yields tuples containing each element along with its next element.
The last element is paired with `None` since there is no next element.

## Purpose 🎯

This function is useful when working with sequences where relationships between consecutive elements are important, such as detecting changes, comparing adjacent values, or processing ordered data efficiently.

## How It Works 🔍

1. **Input Parameter**:

    - `iterable`: Any iterable (list, string, tuple, etc.).

2. **Logic**:
    - The function initializes `prev` as the first element of the iterable.
    - Iterates through the iterable and yields a tuple `(current_element, next_element)`.
    - The last element is paired with `None`.

## Output 📜

A generator yielding tuples where:

-   The first value is the current element.
-   The second value is the next element (`None` for the last item).

### Example:

```python
>>> list(pairwise([10, 20, 30, 40]))
[(10, 20), (20, 30), (30, 40), (40, None)]
```

### Example with Strings:

```python
>>> list(pairwise("abc"))
[('a', 'b'), ('b', 'c'), ('c', None)]
```

## Usage 📦

1. Save the function in a Python file (e.g., `pairwise.py`).
2. Use it with any iterable:
    ```python
    numbers = [5, 15, 25]
    for current, next_item in pairwise(numbers):
        print(f"Current: {current}, Next: {next_item}")
    ```
3. Works with lists, tuples, strings, and more.

## Conclusion 🚀

The `pairwise()` function is an efficient way to iterate through an iterable while tracking the next value.
It is useful for comparing adjacent elements, detecting patterns, and simplifying algorithms that rely on sequential pairs. 🌟
