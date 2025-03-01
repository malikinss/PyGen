# Nested List Sum Comparison

## Description 📝

This program defines the `is_greater()` function, which checks whether the sum of any nested list within a list of nested lists is greater than a given integer.
The function returns `True` if at least one nested list satisfies the condition, otherwise it returns `False`.

## Purpose 🎯

The purpose of this function is to compare the sum of the elements in each nested list to a specified number.
It efficiently checks if any nested list has a sum greater than the given number using Python's built-in `any()` function.

## How It Works 🔍

1. The function accepts two arguments:
    - `nested_lists`: A list of lists of integers.
    - `number`: An integer to compare the sum of nested lists against.
2. The function computes the sum of each nested list.
3. The `any()` function checks if any of the sums is greater than the given number and returns `True` if found, otherwise `False`.

## Output 📜

-   If the sum of at least one nested list is greater than the given number, the function returns `True`.
-   If no nested list has a sum greater than the given number, the function returns `False`.

## Usage 📦

1. Provide a list of nested lists and a number to the `is_greater()` function.
2. The function will compare the sum of each nested list against the given number and return `True` or `False` based on the comparison.

### Example:

```python
is_greater([[1, 2, 3], [4, 5, 6]], 10)  # Returns: True
is_greater([[0, 0, 0], [1, 1, 1]], 5)  # Returns: False
```

## Conclusion 🚀

The `is_greater()` function allows you to efficiently check if any nested list's sum in a list of lists exceeds a given number, using Python's built-in functionality for optimized evaluation.
