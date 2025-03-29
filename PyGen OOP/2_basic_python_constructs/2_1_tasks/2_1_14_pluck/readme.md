# Pluck Function for Extracting Values from Nested Dictionaries 🔍

## Description 📝

The `pluck()` function allows you to extract values from a deeply nested dictionary based on a given key path.
The key path is specified as a string where keys are separated by dots (`.`).
If any key is missing along the path, the function will return a default value.

## Purpose 🎯

This function is useful for working with complex data structures where you need to retrieve a value from a dictionary, even if it's deeply nested.
It handles missing keys gracefully by returning a default value if the key doesn't exist.

## How It Works 🔍

1. **Input Arguments**:

    - `data`: A dictionary (can be arbitrarily nested) from which the value will be extracted.
    - `path`: A string representing the key path, with keys separated by dots.
    - `default`: The value to return if any key in the path is missing. Defaults to `None`.

2. **Key Path**:
    - The function splits the `path` string into individual keys.
    - It iterates through the dictionary, accessing each key in sequence.
    - If a key is missing at any point, the function returns the `default` value.
3. **Return Value**:
    - The function returns the value found at the final key in the path, or `default` if any key is missing.

### Example Inputs & Outputs:

| Input                                                | Output |
| ---------------------------------------------------- | ------ |
| `data = {'a': {'b': 10}}, path = 'a.b'`              | `10`   |
| `data = {'a': {'b': 10}}, path = 'a.c'`              | `None` |
| `data = {'a': {'b': 10}}, path = 'a.c', default = 0` | `0`    |

## Output 📜

The function returns the value found at the specified path, or the default value if the key path is invalid.

## Usage 📦

1. Call `pluck()` with a dictionary, a path (string), and an optional default value.
2. The function will return the corresponding value or the default if the path is invalid.

## Conclusion 🚀

The `pluck()` function is a handy tool for extracting values from nested dictionaries using a clear path.
It ensures safe access to dictionary data and can handle missing keys gracefully with a customizable default return value.
