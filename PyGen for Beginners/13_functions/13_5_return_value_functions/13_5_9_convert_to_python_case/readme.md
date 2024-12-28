# Camel Case to Snake Case Converter 🎯

## Description 📝

This program converts a string written in camel case notation to snake case.
In camel case, each new word in the string starts with a capital letter, while in snake case, words are separated by underscores, and all letters are lowercase.

## Purpose 🎯

The function `convert_to_python_case()` is designed to take a camel case string as input and return its snake case equivalent.
This is useful for adapting variable or function names to the Python naming convention.

## How It Works 🔍

1. **Function `convert_to_python_case(text)`**:
    - Initializes an empty string `new_text` to build the result.
    - Iterates over each character of the input string `text`:
        - When an uppercase letter is encountered, it is converted to lowercase, and an underscore is added before it (unless it's the first character).
        - Otherwise, the character is directly appended to `new_text`.
    - The final `new_text` string represents the input in snake case.

## Usage 📦

1. Copy the code into a Python file, e.g., `camel_to_snake_converter.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python camel_to_snake_converter.py
    ```
5. Enter a camel case string to convert it to snake case.

    - Example 1: `camelCaseString` will return `camel_case_string`.
    - Example 2: `convertToPythonCase` will return `convert_to_python_case`.

## Conclusion 🚀

This program makes it easy to convert camel case strings to snake case, which is a standard naming convention in Python.
