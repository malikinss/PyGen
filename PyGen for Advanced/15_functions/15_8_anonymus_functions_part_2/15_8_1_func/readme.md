# Divisibility Check Using Anonymous Function

## Description

This program defines an anonymous function (`lambda`) that checks whether a given integer is divisible by 19 or 13.
If the number is divisible by either, the function returns `True`; otherwise, it returns `False`.

## Purpose

The main goal of this program is to demonstrate the use of anonymous functions (`lambda`) for simple logical operations.
It provides a concise way to define a function without using the `def` keyword.

## How It Works

1. **Anonymous Function (`lambda`)**:
    - The function takes an integer `x` as an argument.
    - It checks whether `x` is divisible by either 19 or 13 using the modulo operator (`%`).
    - If `x % 19 == 0` or `x % 13 == 0`, it returns `True`; otherwise, it returns `False`.

## Output

For example, given the following inputs:

```python
print(func(19))  # True (divisible by 19)
print(func(26))  # True (divisible by 13)
print(func(38))  # True (divisible by 19)
print(func(20))  # False (not divisible by 19 or 13)
```

## Usage

1. Assign the anonymous function to `func`.
2. Call `func(n)`, where `n` is an integer.
3. The function will return `True` if `n` is divisible by 19 or 13, and `False` otherwise.

## Conclusion

This program is a simple yet effective demonstration of using `lambda` functions for mathematical condition checking, making the code more compact and readable.
