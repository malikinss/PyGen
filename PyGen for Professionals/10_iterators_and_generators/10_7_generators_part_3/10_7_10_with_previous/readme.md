# `with_previous()`: Generator for Tracking Previous Elements

## Description 📝

The `with_previous()` function is a generator that iterates over an iterable and yields tuples containing each element along with its predecessor.
The first element is paired with `None` since there is no previous element.

## Purpose 🎯

This function is useful when processing data where the relationship between consecutive elements matters.
It allows tracking the previous element in a simple and memory-efficient way using a generator.

## How It Works 🔍

1. **Input Parameter**:
    - `iterable`: Any iterable (list, string, tuple, etc.).
2. **Logic**:
    - The function initializes `prev` as `None`.
    - Iterates through the iterable and yields a tuple `(current_element, previous_element)`.
    - Updates `prev` with the current element before the next iteration.

## Output 📜

A generator yielding tuples where:

-   The first value is the current element.
-   The second value is the previous element (`None` for the first item).

### Example:

```python
>>> list(with_previous([10, 20, 30, 40]))
[(10, None), (20, 10), (30, 20), (40, 30)]
```

### Example with Strings:

```python
>>> list(with_previous("abc"))
[('a', None), ('b', 'a'), ('c', 'b')]
```

## Usage 📦

1. Save the function in a Python file (e.g., `with_previous.py`).
2. Use it with any iterable:
    ```python
    numbers = [5, 15, 25]
    for current, previous in with_previous(numbers):
        print(f"Current: {current}, Previous: {previous}")
    ```
3. Works with lists, tuples, strings, and more.

## Conclusion 🚀

The `with_previous()` function is an efficient way to iterate through an iterable while tracking previous values.
It’s useful in situations where you need to compare elements or maintain a running context of past values. 🌟
