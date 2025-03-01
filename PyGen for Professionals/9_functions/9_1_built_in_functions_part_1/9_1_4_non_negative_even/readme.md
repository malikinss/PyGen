# Non-Negative Even Numbers Check

## Description 📝

This program defines the `non_negative_even()` function, which checks whether all numbers in a given list are both even and non-negative.
The function returns `True` if all numbers meet the criteria, or `False` otherwise.

## Purpose 🎯

The purpose of this function is to validate a list of numbers by ensuring that they are all even and non-negative.
This function makes use of Python's `all()` function for efficient checking of multiple conditions in one pass.

## How It Works 🔍

1. The function accepts a list of integers called `numbers`.
2. It checks every number in the list to ensure it is both non-negative and even using a generator expression.
3. The `all()` function returns `True` if all the numbers satisfy the conditions, otherwise `False`.

## Output 📜

-   If all numbers in the list are non-negative and even, the function returns `True`.
-   If any number fails to meet these conditions, the function returns `False`.

## Usage 📦

1. Provide a list of numbers to the `non_negative_even()` function.
2. The function will check if all numbers are even and non-negative.

### Example:

```python
non_negative_even([2, 4, 6, 8])  # Returns: True
non_negative_even([1, 2, 3, 4])  # Returns: False
```

## Conclusion 🚀

The `non_negative_even()` function efficiently checks whether a list of numbers contains only even, non-negative values, using Python's built-in functionality for concise and effective evaluation.
