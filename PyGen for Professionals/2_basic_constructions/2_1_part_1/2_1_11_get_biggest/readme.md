# Get Biggest Number Function

## Description 📝

The `get_biggest()` function constructs the largest possible number by rearranging a given list of non-negative integers.

## Purpose 🎯

This function is useful for:

-   Optimizing number formation in combinatorial problems.
-   Creating the largest possible numerical value from given digits.
-   Applications in sorting and greedy algorithms.

## How It Works 🔍

1. Converts all numbers to strings for easy concatenation.
2. Sorts the numbers using a custom comparison rule:
    - For two numbers `a` and `b`, it checks if `a + b > b + a` to determine their relative order.
3. Joins the sorted numbers into a single string and converts it back to an integer.

## Output 📜

Example usage and expected outputs:

```python
get_biggest([1, 2, 3])
# 321

get_biggest([10, 2])
# 210

get_biggest([3, 30, 34, 5, 9])
# 9534330

get_biggest([0, 0, 0])
# 0

get_biggest([])
# -1
```

## Usage 📦

1. Clone this repository.
2. Import the function into your Python script.
3. Use `get_biggest()` with a list of numbers.

Example:

```python
from number_combiner import get_biggest

print(get_biggest([54, 546, 548, 60]))  # Output: 6054854654
```

## Conclusion 🚀

The `get_biggest()` function is an efficient way to maximize a number by rearranging its components.
It is particularly useful in coding challenges and algorithmic optimizations.
