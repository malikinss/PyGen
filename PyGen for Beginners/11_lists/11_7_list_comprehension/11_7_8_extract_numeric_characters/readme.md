# Extract Numeric Characters

## Description 📝

This Python program takes an input string containing text and numeric characters. It extracts all the numeric characters from the string and prints them, concatenated without spaces.

## Purpose 🎯

-   To practice extracting specific characters from a string.
-   To demonstrate string manipulation using list expressions and the `isdigit()` method in Python.
-   To handle user input and display output without spaces.

## How It Works 🔍

1. **Function `extract_numeric_characters`**:

    - Accepts a string `text` as input.
    - Uses a list expression to iterate over each character in the string and checks if the character is numeric using the `isdigit()` method.
    - Joins the numeric characters into a new string using the `join()` method and returns it.

2. **Function `main`**:
    - Prompts the user to input a string using `input()`.
    - Calls the `extract_numeric_characters` function to extract the numeric characters.
    - Prints the extracted numeric characters without spaces.

## Output 📜

The numeric characters from the input string are printed as a continuous string.

**Example**:

```

Enter a string of text: The year is 2024, and the month is 12.
202412

```

## Usage 📦

1. Copy the code into a Python file, e.g., `extract_numeric_characters.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:

    ```bash
    python extract_numeric_characters.py
    ```

5. Enter a string when prompted.
6. View the numeric characters printed as a continuous string.

## Conclusion 🚀

This program demonstrates how to extract numeric characters from a given string and print them as a single, concatenated string.
It’s a useful example for string handling, working with user input, and filtering characters in Python. 🧑‍💻🎉
