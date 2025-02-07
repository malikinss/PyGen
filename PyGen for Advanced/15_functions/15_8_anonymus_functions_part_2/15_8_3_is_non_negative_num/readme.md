# Checking If a String Represents a Non-Negative Number

## Description

This program defines an anonymous function (`lambda`) that checks whether a given string represents a non-negative number (either an integer or a float).
If the condition is met, the function returns `True`; otherwise, it returns `False`.

## Purpose

The goal is to efficiently determine if a string is a valid non-negative numerical representation using a compact `lambda` function.

## How It Works

1. **Validates the Input String**:

    - Ensures the string contains at most one decimal point (`.`).
    - Removes the decimal point (if any) and checks if the remaining characters are digits.
    - Ensures the string does not start with a minus sign (`-`), which would indicate a negative number.

2. **Anonymous Function (`lambda`)**:
    - Combines all checks into a single `lambda` function using logical operators.

## Output

For example, given the following inputs:

```python
print(is_non_negative_num("123"))       # True (valid integer)
print(is_non_negative_num("0"))         # True (valid integer)
print(is_non_negative_num("45.67"))     # True (valid float)
print(is_non_negative_num(".5"))        # False (invalid format)
print(is_non_negative_num("4.5.6"))     # False (multiple dots)
print(is_non_negative_num("-78"))       # False (negative integer)
print(is_non_negative_num("abc"))       # False (not a number)
```

## Usage

1. Assign the anonymous function to `is_non_negative_num`.
2. Call `is_non_negative_num(string)`, where `string` is the input to check.
3. The function will return `True` if the input is a valid non-negative integer or float, and `False` otherwise.

## Conclusion

This program provides an efficient and concise way to validate numerical strings using a `lambda` function.
