# Arithmetic Mean Calculation Program 📊

## Description 📝

This program calculates the arithmetic mean (average) of the elements in a given set of integers.
It leverages Python's set data structure to automatically remove duplicates before performing the calculation.

## Purpose 🎯

-   To compute the average of unique integers in a set.
-   To demonstrate how to use Python’s `sum()` and `len()` functions for quick calculations.

## How It Works 🔍

1. **Function `calculate_arithmetic_mean`**:

    - Accepts a set of integers.
    - Computes the sum of all elements using `sum()`.
    - Divides the sum by the total number of elements (`len()`) to get the arithmetic mean.

2. **Set Initialization**:

    - A set of integers is initialized, including duplicates.
    - The set automatically removes duplicates, ensuring unique values are used for the calculation.

3. **Result Calculation**:
    - The arithmetic mean is calculated and printed to the console.

### Example:

```python
numbers = {
    20, 6, 8, 18,
    18, 2, 4, 6,
    8, 10, 12, 14,
    16, 18, 20, 12,
    8, 8, 10, 4,
    2, 2, 2, 16, 20
}
print(calculate_arithmetic_mean(numbers))
```

**Output**:

```
11.0
```

## Output 📜

-   The program calculates the arithmetic mean by dividing the sum of the unique integers by their count.
-   In this example, the unique integers are:
    ```
    {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    ```
    -   Sum = `2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 = 110`
    -   Count = `10`
    -   Arithmetic Mean = `110 / 10 = 11.0`

## Conclusion 🚀

This simple program efficiently calculates the arithmetic mean while demonstrating the power of Python's set operations.
It showcases how to handle duplicate values and perform basic mathematical computations using core Python functions.
