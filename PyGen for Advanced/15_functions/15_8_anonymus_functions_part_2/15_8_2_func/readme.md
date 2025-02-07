# Checking If a String Starts and Ends with 'A'

## Description

This program defines an anonymous function (`lambda`) that checks whether a given string starts and ends with the letter 'a' (case-insensitive).
If the condition is met, the function returns `True`; otherwise, it returns `False`.

## Purpose

The goal of this program is to demonstrate the use of `lambda` functions in combination with helper functions for efficient string validation.

## How It Works

1. **Helper Functions**:

    - `starts_with(word, letter)`: Checks if `word` starts with `letter` (case-insensitive).
    - `ends_with(word, letter)`: Checks if `word` ends with `letter` (case-insensitive).

2. **Anonymous Function (`lambda`)**:
    - Calls `starts_with(x, 'a')` and `ends_with(x, 'a')`.
    - If both return `True`, the function returns `True`; otherwise, it returns `False`.

## Output

For example, given the following inputs:

```python
print(func("Anna"))     # True (starts and ends with 'A')
print(func("America"))  # True (starts and ends with 'A')
print(func("apple"))    # False (does not end with 'A')
print(func("Alaska"))   # True (starts and ends with 'A')
print(func("banana"))   # False (does not start with 'A')
```

## Usage

1. Assign the anonymous function to `func`.
2. Call `func(string)`, where `string` is the input to check.
3. The function will return `True` if `string` starts and ends with 'A' (case-insensitive), and `False` otherwise.

## Conclusion

This program efficiently validates whether a given string meets the specified conditions using a compact `lambda` function combined with helper functions for clarity.
