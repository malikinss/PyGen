# Count Digits Recursively 📝

## Description 🎯

The `print_digit_count()` function takes a number as input and outputs the number of digits in that number using recursion.

## Purpose 🎯

This function is useful for determining the number of digits in a given number without using built-in string conversion methods.
It demonstrates the power of recursion in mathematical operations.

## How It Works 🔍

1. The function `print_digit_count()` calls an internal recursive function `count_digits()`.
2. `count_digits()` checks if the number is a single-digit number (0–9). If so, it returns `1`.
3. Otherwise, the function recursively calls itself with `number // 10` (removing the last digit) and adds `1` to the count.
4. The final count is printed.

## Output 📜

For an input number `11111`, the output will be:

```
5
```

## Usage 📦

1. Call the function `print_digit_count()` with a number as an argument.
2. Example:
    ```python
    print_digit_count(987654321)
    ```
3. The function will output the number of digits in the given number.

## Conclusion 🚀

The `print_digit_count()` function efficiently calculates the number of digits in a number using recursion.
It avoids string conversions and showcases a mathematical approach to digit counting.
