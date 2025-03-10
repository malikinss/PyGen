# Count Elements in an Iterable

## Description 📝

This script defines the `count_iterable()` function, which efficiently counts the number of elements in an iterable using a generator expression.

## Purpose 🎯

The function provides a concise way to determine the length of any iterable without directly converting it into a list, making it memory-efficient for large iterables.

## How It Works 🔍

1. **Generator Expression**: Iterates over the elements of the iterable and yields `1` for each item.
2. **`sum()` Function**: Adds up the yielded values, effectively counting the elements.

## Output 📜

Example usage:

```python
print(count_iterable([1, 2, 3, 4]))  # Output: 4
print(count_iterable("hello"))       # Output: 5
print(count_iterable(range(10)))     # Output: 10
```

## Usage 📦

1. Save the function in a Python file, e.g., `count_iterable.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the function:
    ```python
    from count_iterable import count_iterable
    print(count_iterable([10, 20, 30]))  # Output: 3
    ```
4. The function can be used in loops, list comprehensions, or other data-processing tasks.

## Conclusion 🚀

This function provides a simple yet powerful way to count elements in any iterable while maintaining efficiency and readability. 🚀
