# Retrieve Last Element Using iter() and next() 📝

## Description 📝

This program retrieves and prints the last element of a list using `iter()` and `next()`.
Instead of using direct indexing (`numbers[-1]`), it leverages Python's iterator functions.

## Purpose 🎯

The purpose of this implementation is to:

-   Demonstrate an alternative approach to accessing the last element of a list.
-   Utilize `iter()` and `next()` for iteration-based element retrieval.
-   Ensure safety by handling edge cases such as an empty list.

## How It Works 🔍

1. **Function Definition**:
    - `print_last_element(any_list: List[int])` takes a list as input.
2. **Validation Check**:

    - If the list is empty, a `ValueError` is raised.

3. **Using iter() and next()**:
    - `reversed(any_list)` creates a reverse iterator for the list.
    - `iter(reversed(any_list))` converts it into an explicit iterator.
    - `next(...)` fetches the first element from this reversed iterator, which is the last element of the original list.

## Output 📜

For the given list, calling:

```python
print_last_element(numbers)
```

will produce:

```
-22
```

since `-22` is the last element in the list.

## Usage 📦

1. Call `print_last_element()` with a list of integers.
2. Ensure the list is not empty to avoid errors.
3. The function prints the last element efficiently.

## Conclusion 🚀

This approach highlights the power of Python iterators, showcasing how `iter()`, `next()`, and `reversed()` can be used to retrieve elements dynamically without relying on direct indexing.
