# Decimal Number Validator 🔢

## Description 📝

The `is_decimal()` function checks if a given string represents a valid decimal number (including integers).
It ensures that the input follows the correct structure for real numbers, allowing an optional negative sign (`-`) and a decimal point (`.`) at any valid position.

## Purpose 🎯

This function helps validate whether a string represents a valid numerical value, either an integer or a real number.
It prevents incorrect formats such as misplaced decimal points or non-numeric characters.

## How It Works 🔍

1. The function first ensures that the input is not empty.
2. It uses a regular expression to match different valid formats:
    - Integers: `"123"`, `"-456"`
    - Decimal numbers: `"12.34"`, `"-0.56"`, `"10."`, `".99"`
    - The decimal point cannot precede the optional `-` sign.
3. The regex pattern ensures that only valid number formats are matched.
4. The function returns `True` if the string represents a valid decimal number, otherwise `False`.

### Example Inputs & Outputs:

| Input     | Output  |
| --------- | ------- |
| `"123"`   | `True`  |
| `"-456"`  | `True`  |
| `"12.34"` | `True`  |
| `"-0.56"` | `True`  |
| `"."`     | `False` |
| `"1..2"`  | `False` |
| `"abc"`   | `False` |

## Output 📜

Returns `True` if the input string is a valid integer or real number, and `False` otherwise.

## Usage 📦

1. Call `is_decimal()` with a string argument.
2. The function will return `True` for valid numbers and `False` otherwise.

### Example:

```python
is_decimal("-123.45")  # Returns: True
is_decimal("0.99")  # Returns: True
is_decimal(".99")  # Returns: True
is_decimal("..12")  # Returns: False
is_decimal("abc")  # Returns: False
```

## Conclusion 🚀

The `is_decimal()` function ensures that a string follows valid integer and real number formats, making it useful for input validation in various applications.
