# `around()`: Generator for Tracking Previous, Current, and Next Elements

## Description 📝

The `around()` function is a generator that iterates over an iterable and yields tuples containing each element along with its previous and next elements.
If an element has no previous or next value, `None` is used in its place.

## Purpose 🎯

This function is useful when processing sequential data where relationships between consecutive elements are important, such as analyzing trends, detecting changes, or smoothing data.

## How It Works 🔍

1. **Input Parameter**:

    - `iterable`: Any iterable (list, string, tuple, etc.).

2. **Logic**:
    - The function initializes three variables: `prev`, `cur`, and `next_`.
    - Iterates through the iterable while updating these values.
    - Yields a tuple `(previous_element, current_element, next_element)`.
    - The first element has `None` as its previous value, and the last element has `None` as its next value.

## Output 📜

A generator yielding tuples where:

-   The first value is the previous element (`None` for the first item).
-   The second value is the current element.
-   The third value is the next element (`None` for the last item).

### Example:

```python
>>> list(around([10, 20, 30, 40]))
[(None, 10, 20), (10, 20, 30), (20, 30, 40), (30, 40, None)]
```

### Example with Strings:

```python
>>> list(around("abc"))
[(None, 'a', 'b'), ('a', 'b', 'c'), ('b', 'c', None)]
```

## Usage 📦

1. Save the function in a Python file (e.g., `around.py`).
2. Use it with any iterable:
    ```python
    numbers = [5, 15, 25, 35]
    for prev, current, next_item in around(numbers):
        print(f"Prev: {prev}, Current: {current}, Next: {next_item}")
    ```
3. Works with lists, tuples, strings, and more.

## Conclusion 🚀

The `around()` function is an efficient way to iterate through an iterable while keeping track of surrounding values.
It is useful for comparing adjacent elements, detecting patterns, and simplifying algorithms that require knowledge of previous and next items. 🌟
