# Retrieve N-th Element Using iter() and next() 📝

## Description 📝

This program demonstrates how to retrieve the N-th element from a list using the `iter()` and `next()` functions.
Instead of directly indexing the list, an iterator is used to traverse it step by step.

## Purpose 🎯

The purpose of this implementation is to:

-   Show how to work with iterators in Python.
-   Retrieve the fourth element from a list without using direct indexing (`numbers[3]`).
-   Provide a function that can retrieve any N-th element using iteration.

## How It Works 🔍

1. The function `get_nth_element()` takes two arguments:
    - `numbers`: A list of integers.
    - `n`: The position of the element to retrieve (1-based index).
2. **Validation Check**:

    - The function checks if `n` is within the valid range (`1 ≤ n ≤ len(numbers)`) and raises an `IndexError` if it is out of range.

3. **Creating an Iterator**:

    - `iter(numbers)` creates an iterator for the list.

4. **Fetching the N-th Element**:
    - A loop is used to call `next()` on the iterator `n` times.
    - The result of the last `next()` call is returned.

## Output 📜

Given the predefined list, calling:

```python
print(get_nth_element(numbers, 4))
```

will produce:

```
45
```

since the fourth element (1-based index) in the list is `45`.

## Usage 📦

1. Call `get_nth_element()` with a list and the desired element index.
2. Make sure `n` is within the valid range (from 1 to the length of the list).
3. The function returns the required element or raises an `IndexError` if `n` is out of bounds.

## Conclusion 🚀

This implementation showcases an alternative way to access list elements using `iter()` and `next()`, reinforcing the understanding of Python iterators.
It can be useful in scenarios where list iteration is required without direct indexing.
