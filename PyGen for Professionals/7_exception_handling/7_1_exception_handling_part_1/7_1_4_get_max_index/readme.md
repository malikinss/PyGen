# Find the Maximum Index 📝

## Description 📝

The program implements a function `get_max_index()` that returns the index of the largest integer in a list of distinct integers.

## Purpose 🎯

To identify and correct the mistakes in the original code, ensuring that the function correctly returns the index of the largest number in the list.

## How It Works 🔍

1. The original code contains errors such as:
    - Incorrect variable names (`get_max_inex` instead of `get_max_index`).
    - The wrong starting index for `enumerate()`.
    - The wrong comparison for finding the maximum value.
2. The corrected function simply uses Python's built-in `max()` to find the maximum value and `index()` to return its position in the list.

## Output 📜

**Example Input:**

```python
numbers = [3, 1, 4, 1, 5, 9]
```

**Example Output:**

```python
4
```

## Usage 📦

1. Call the function `get_max_index()` with a list of integers as an argument.
2. It will return the index of the largest number.

## Conclusion 🚀

The function is now fixed and works as expected, finding the index of the maximum value in the list.
