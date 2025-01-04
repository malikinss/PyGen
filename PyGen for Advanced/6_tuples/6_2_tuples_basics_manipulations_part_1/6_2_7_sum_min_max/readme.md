# Sum of Minimum and Maximum Elements 🔢

## Description 📝

This program calculates the sum of the minimum and maximum values in a tuple of numbers.
It utilizes the built-in `min()` and `max()` functions to find these values, and then returns their sum.

## Purpose 🎯

-   To find the sum of the minimum and maximum elements in a given tuple of numbers.
-   Demonstrates the usage of `min()` and `max()` to find the smallest and largest values in a tuple.

## How It Works 🔍

1. **Function `sum_min_max(numbers: Tuple[float, ...])`**:

    - Takes a tuple `numbers` as input, which contains numerical values.
    - Finds the minimum value using `min()` and the maximum value using `max()`.
    - Returns the sum of these two values.

2. **Tuple `numbers`**:

    - Contains a sequence of floating-point numbers.

3. **The result**:
    - The sum of the minimum and maximum values from the tuple is calculated and printed.

### Example:

```
Input: (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
Output: 13.624 (Sum of 1.1618 and 12.5)
```

## Output 📜

The output will be:

```
13.624
```

## Conclusion 🚀

This code successfully calculates the sum of the minimum and maximum values in a tuple, demonstrating the use of Python's built-in functions `min()` and `max()` for handling numerical data.
