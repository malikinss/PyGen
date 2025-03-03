# Custom Print Function

## Description 📝

This Python script overrides the built-in `print()` function to ensure that all string arguments, as well as the `sep` and `end` values, are converted to uppercase before being printed.

## Purpose 🎯

The goal of this program is to demonstrate function overriding in Python, specifically modifying the behavior of the built-in `print()` function.
This exercise helps in understanding function wrapping, argument handling, and modifying default behavior dynamically.

## How It Works 🔍

1. **Backup Original Print**: The original `print()` function is stored as `original_print` to allow calling it inside the new function.
2. **Argument Transformation**:
    - All string arguments (`*args`) are converted to uppercase.
    - The `sep` and `end` values in `**kwargs` are also transformed to uppercase.
3. **Default Values Handling**: If `sep` or `end` are not provided, they default to `' '` (space) and `'\n'` (newline), respectively.
4. **Calling the Original Print**: The transformed arguments are passed to `original_print()` for actual output.

## Output 📜

Example usage and outputs:

```python
print("hello", "world")
# Output: HELLO WORLD

print("Python", "is", "fun", sep="-")
# Output: PYTHON-IS-FUN

print("custom", "print", end="!!!")
# Output: CUSTOM PRINT!!!
```

## Usage 📦

1. Save the code to a file named `custom_print.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute a Python script that imports and uses the custom `print()` function.

    ```python
    from custom_print import print

    print("hello", "world")
    print("this", "is", "a", "test", sep=" - ", end="!!!\n")
    ```

## Conclusion 🚀

This program provides an example of function overriding and modification in Python.
It showcases how built-in functions can be wrapped and customized for specific use cases.
