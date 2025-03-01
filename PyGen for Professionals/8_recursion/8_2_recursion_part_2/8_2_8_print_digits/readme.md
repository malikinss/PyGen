# Print Digits Recursively 📝

## Description 🎯

The `print_digits()` function recursively prints the digits of a natural number, starting from the least significant digit to the most significant one. Each digit is printed on a separate line.

## Purpose 🎯

This function is useful for scenarios where you need to process or display the digits of a number in reverse order.
The recursive approach helps break down the number and print each digit individually.

## How It Works 🔍

1. The function takes a natural number as input.
2. It checks if the number is greater than 0.
3. The least significant digit (rightmost digit) is printed.
4. The function then recursively calls itself with the remaining number (excluding the least significant digit).
5. This process continues until all digits are printed.

## Output 📜

For an input number `12345`, the output will be:

```
5
4
3
2
1
```

The digits are printed starting from the least significant digit (rightmost), each on a new line.

## Usage 📦

1. Call the function `print_digits()` with a natural number as an argument.
2. Example:
    ```python
    print_digits(12345)
    ```
3. The function will print each digit of the number starting from the least significant digit.

## Conclusion 🚀

The `print_digits()` function provides a simple recursive solution for printing the digits of a natural number in reverse order, demonstrating the use of recursion and modular arithmetic.
