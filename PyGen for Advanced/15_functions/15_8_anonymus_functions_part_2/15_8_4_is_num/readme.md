# Checking If a String Represents a Valid Number

## Description

This program defines an anonymous function (`lambda`) that determines whether a given string represents a valid number (integer or float).
If the input meets the criteria, the function returns `True`; otherwise, it returns `False`.

## Purpose

The goal is to provide a concise way to check if a string is a valid numerical representation, including both integers and floating-point numbers.

## How It Works

1. **Validates the Input String**:

    - Ensures that the string consists of digits and at most one decimal point (`.`).
    - Allows a leading minus sign (`-`) but ensures it does not appear elsewhere in the string.

2. **Anonymous Function (`lambda`)**:
    - Uses a helper function (`is_valid_number`) to handle digit validation.
    - Ensures that a negative sign appears only at the beginning.

## Output

For example, given the following inputs:

```python
print(is_num("123"))       # True (valid integer)
print(is_num("45.67"))     # True (valid float)
print(is_num("-78"))       # True (negative integer)
print(is_num("0.5"))       # True (valid float)
print(is_num("4.5.6"))     # False (multiple dots)
print(is_num(".5"))        # False (invalid format)
print(is_num("--12"))      # False (multiple negatives)
print(is_num("abc"))       # False (not a number)
```

## Usage

1. Assign the anonymous function to `is_num`.
2. Call `is_num(string)`, where `string` is the input to check.
3. The function will return `True` if the input is a valid integer or float, and `False` otherwise.

## Conclusion

This implementation provides an efficient way to determine if a string represents a valid number using an anonymous function.
