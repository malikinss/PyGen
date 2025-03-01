# Sum of Digits Recursively 📝

## Description 🎯

The `get_digits_sum()` function calculates the sum of the digits of a given number using recursion.

## Purpose 🎯

This function is useful for computing the sum of digits in a number without converting it to a string.
It demonstrates recursion as an elegant way to break down a problem into smaller subproblems.

## How It Works 🔍

1. If the number is a single digit (0-9), return it (base case).
2. Otherwise, extract the last digit using `number % 10`.
3. Recursively call `get_digits_sum()` on `number // 10` (removing the last digit).
4. Add the extracted digit to the recursive sum.
5. The recursion continues until the number is reduced to a single digit.

## Output 📜

For an input `111211`, the output will be:

```
7
```

(1 + 1 + 1 + 2 + 1 + 1 = 7)

## Usage 📦

1. Call the function `get_digits_sum()` with a number as an argument.
2. Example:
    ```python
    print(get_digits_sum(98765))
    ```
3. The function will return the sum of the digits of the given number.

## Conclusion 🚀

The `get_digits_sum()` function effectively computes the sum of a number's digits using recursion, demonstrating a mathematical approach to problem-solving without loops or string manipulations.
