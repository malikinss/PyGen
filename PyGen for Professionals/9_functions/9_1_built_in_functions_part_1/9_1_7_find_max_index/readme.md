# Find Maximum Index

## Description 📝

This program defines the `find_max_index()` function, which finds the index of the maximum element in a given list of integers.

## Purpose 🎯

The purpose of this function is to identify the position of the highest number in a list.
This can be useful for ranking, optimization, and data analysis tasks.

## How It Works 🔍

1. The function accepts a list of integers as an argument.
2. If the list is empty, it prints an error message and returns `-1`.
3. It uses the `enumerate()` function to pair each element with its index.
4. The `max()` function is used with a lambda function to determine the index of the largest value.
5. The function returns the index of the maximum element.

## Usage 📦

1. Provide a list of integers to the `find_max_index()` function.
2. The function will return the index of the maximum value.

### Example:

```python
numbers = [10, 20, 5, 30, 25]
print(find_max_index(numbers))
```

## Conclusion 🚀

The `find_max_index()` function efficiently finds the index of the largest number in a list using `enumerate()` and `max()`, making it a simple and powerful tool for handling numerical lists.
