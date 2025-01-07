# Sum of Minimum and Maximum Elements Program 🔢

## Description 📝

This program calculates the sum of the minimum and maximum values in a given set of floating-point numbers.
The solution demonstrates how to efficiently work with sets in Python and perform basic operations like finding the minimum and maximum values.

## Purpose 🎯

-   To compute the sum of the smallest and largest elements in a set of numbers.
-   To demonstrate the use of Python’s `min()` and `max()` functions.

## How It Works 🔍

1. **Function `find_sum_of_min_max`**:

    - Takes a set of floating-point numbers as input.
    - Calculates the minimum and maximum values using `min()` and `max()`.
    - Returns the sum of these two values.

2. **Set Initialization**:

    - A set of floating-point numbers is initialized to avoid duplicates.

3. **Result Calculation**:
    - The function is called with the provided set of numbers, and the result is printed.

### Example:

```python
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
result = find_sum_of_min_max(numbers)
print(result)
```

**Output**:

```
13.6618
```

## Output 📜

-   The program outputs the sum of the smallest and largest values from the set.
-   In this example, the smallest value is `1.1618` and the largest is `12.5`, so the result is:
    ```
    1.1618 + 12.5 = 13.6618
    ```

## Conclusion 🚀

This program provides a simple yet effective way to perform basic mathematical operations on sets.
It highlights the usefulness of Python's set data structure in eliminating duplicates and the ease of using built-in functions for quick computations.
