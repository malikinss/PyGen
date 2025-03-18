# Number Generator in Custom Base

## Description 📝

The `generate_numbers()` function generates all possible numbers of length `m` in a custom number system with base `n`, where `2 ≤ n ≤ 16`.
It uses the `product()` function from the `itertools` module to create combinations of digits in the specified base and length, then outputs them in ascending order.

## Purpose 🎯

This function is useful for generating all numbers in a number system with a custom base (between 2 and 16) and a specified length.
It can be applied in scenarios such as simulations, encoding/decoding tasks, or generating test data.

## How It Works 🔍

-   **Using `product()`**: The `product()` function from `itertools` generates all possible combinations of the given digits (up to base `n`) for numbers of length `m`.
    -   The `digits` string contains all valid digits for number systems with base 2 through 16 (i.e., '0123456789ABCDEF').
    -   The `repeat=m` argument ensures that the combinations are of length `m`.
-   **Generating Numbers**: The function iterates over the resulting combinations and prints each number, joining the digits into a string.

## Output 📜

Example usage:

```python
generate_numbers(3, 2)
# Output: 00 01 02 10 11 12 20 21 22
```

## Usage 📦

1. Save the function in a Python file, e.g., `generate_numbers.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the function:
    ```python
    from generate_numbers import generate_numbers
    generate_numbers(3, 2)  # Output: 00 01 02 10 11 12 20 21 22
    ```

## Conclusion 🚀

The `generate_numbers()` function is an efficient and straightforward way to generate numbers of length `m` in a custom base `n`.
By using `product()`, the code remains simple, readable, and adaptable to different number systems.
