# Print Digits Recursively 📝

## Description 🎯

The `print_digits()` function recursively prints the digits of a natural number, starting with the most significant digit to the least significant one. Each digit is printed on a separate line.

## Purpose 🎯

This function is useful when you need to display or process the digits of a number starting from the most significant (leftmost) digit.
The recursive method allows the number to be broken down and printed one digit at a time.

## How It Works 🔍

1. The function accepts a natural number as input.
2. It checks if the number is greater than or equal to 10.
3. If true, the function calls itself recursively with the number divided by 10 (removes the least significant digit).
4. Once the number is a single digit (i.e., less than 10), the recursion stops.
5. The most significant digit is printed on each return step of the recursion.

## Output 📜

For an input number `12345`, the output will be:

```
1
2
3
4
5
```

The digits are printed starting from the most significant digit (leftmost), each on a new line.

## Usage 📦

1. Call the function `print_digits()` with a natural number as an argument.
2. Example:
    ```python
    print_digits(12345)
    ```
3. The function will print each digit of the number starting from the most significant digit.

## Conclusion 🚀

The `print_digits()` function provides a recursive solution for printing the digits of a natural number in the order from most significant to least significant.
This showcases recursion and modular arithmetic for number manipulation.
