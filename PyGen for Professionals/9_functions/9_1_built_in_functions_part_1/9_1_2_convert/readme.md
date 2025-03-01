# Convert Integer to Binary, Octal, and Hexadecimal 🔢

## Description 📝

The program defines a function `convert()` that takes an integer as an argument and returns a tuple containing its binary, octal, and hexadecimal representations.

-   The binary representation is returned as a string without the `0b` prefix.
-   The octal representation is returned as a string without the `0o` prefix.
-   The hexadecimal representation is returned as an uppercase string without the `0x` prefix.

## Purpose 🎯

The purpose of the `convert()` function is to demonstrate how to convert an integer to its binary, octal, and hexadecimal forms using Python’s built-in functions `bin()`, `oct()`, and `hex()`.

## How It Works 🔍

The function follows these steps:

1. **Binary Conversion**: The `bin()` function is used to convert the integer to a binary string. The `0b` prefix is removed by slicing the string starting from the third character.
2. **Octal Conversion**: The `oct()` function is used to convert the integer to an octal string. The `0o` prefix is removed in the same manner as the binary representation.
3. **Hexadecimal Conversion**: The `hex()` function converts the integer to a hexadecimal string, and the `0x` prefix is removed. The resulting string is then converted to uppercase for consistency.

## Usage 📦

1. **Call the function `convert(number)`**:
    - **Argument**: The function takes a single argument, `number`, which is the integer to be converted.
    - **Return**: The function returns a tuple of three strings: the binary, octal, and hexadecimal representations of the integer.
2. Example usage:

    ```python
    print(convert(24))
    ```

    This will print:

    ```
    ('11000', '30', '18')
    ```

3. The `convert()` function can handle both positive and negative integers.

## Conclusion 🚀

The `convert()` function efficiently demonstrates how to convert an integer into its binary, octal, and hexadecimal representations.
It showcases Python’s built-in `bin()`, `oct()`, and `hex()` functions while also providing a clean and readable output without the prefixes.
