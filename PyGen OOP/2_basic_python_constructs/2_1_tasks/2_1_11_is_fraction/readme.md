# Fraction Validator 🔢

## Description 📝

The `is_fraction()` function checks whether a given string represents a valid common fraction.
The fraction is composed of a numerator, followed by a forward slash (`/`), and a denominator.
The function also handles optional negative signs and ensures the denominator is not zero.

## Purpose 🎯

This function helps to validate if a string accurately represents a valid common fraction, allowing for negative fractions and ensuring the denominator is non-zero.
It is useful for parsing or validating user inputs where fractions are required.

## How It Works 🔍

1. The function checks if the string contains a forward slash (`/`), which is necessary for a fraction.
2. It then uses a regular expression to match the following valid formats:
    - The numerator can be any non-negative integer.
    - The denominator must be a positive integer with at least one non-zero digit.
    - An optional negative sign (`-`) may appear at the start.
3. The regex pattern is used to validate the structure of the string, ensuring it follows the common fraction format.
4. The function returns `True` if the string represents a valid fraction, and `False` otherwise.

### Example Inputs & Outputs:

| Input           | Output  |
| --------------- | ------- |
| `"1000/00001"`  | `True`  |
| `"-1000/00001"` | `True`  |
| `"5/0"`         | `False` |
| `"0/2"`         | `True`  |
| `"100/000"`     | `True`  |
| `"1/01"`        | `True`  |
| `"-/3"`         | `False` |

## Output 📜

Returns `True` if the input string is a valid common fraction, and `False` otherwise.

## Usage 📦

1. Call `is_fraction()` with a string argument.
2. The function will return `True` for valid fractions and `False` otherwise.

## Conclusion 🚀

The `is_fraction()` function ensures that a string is a valid common fraction, making it useful for validating fractional inputs in various applications.
