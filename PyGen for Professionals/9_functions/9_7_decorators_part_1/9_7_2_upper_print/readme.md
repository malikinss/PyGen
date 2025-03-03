# Uppercase Print Decorator

## Description 📝

This Python program defines a `upper_print` decorator that overrides the built-in `print()` function.
It ensures that all text printed is in uppercase, including the `sep` and `end` parameters, if provided.
The decorator allows the `print()` function to behave as normal while converting all text to uppercase.

## Purpose 🎯

The goal of this program is to decorate the `print()` function so that all output, including any separators and endings, is printed in uppercase.
The decorator works with any number of positional and keyword arguments passed to the `print()` function.

## How It Works 🔍

1. **Input**:

    - The `upper_print` decorator is applied to the `print()` function.
    - The `print()` function accepts any number of arguments, including text and special parameters like `sep` and `end`.

2. **Processing**:

    - The `upper_print` decorator intercepts the call to `print()`.
    - It converts all string arguments and special parameters (`sep` and `end`) to uppercase using a helper function.
    - The modified arguments are passed to the original `print()` function.

3. **Output**:
    - The output text is printed in uppercase, and the separator and ending text (if any) are also converted to uppercase.

## Example 📜

### Example Usage:

```python
# Print a sentence with normal behavior
print("Hello, world!")

# Print with a custom separator and end text
print("Hello", "world", sep=", ", end=".\n")
```

### Output:

```
HELLO, WORLD!
HELLO, WORLD.
```

In both cases, the text is printed in uppercase, and the `sep` and `end` values are also converted to uppercase.

## Usage 📦

1. Define the `upper_print` decorator in your script.
2. Decorate the built-in `print()` function by assigning `print = upper_print(print)`.
3. Call `print()` with any number of arguments as usual, and the output will be converted to uppercase.

## Conclusion 🚀

The `upper_print` decorator provides a simple and effective way to modify the behavior of the `print()` function, ensuring that all printed text is in uppercase.
It is a flexible solution that can be used in various scenarios where you want to control the output formatting.
