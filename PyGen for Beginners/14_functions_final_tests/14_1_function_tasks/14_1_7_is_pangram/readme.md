# Pangram Checker 🅰️

## Description 📝

This Python script checks if a given text is a **pangram**. A pangram is a phrase that contains all the letters of the English alphabet at least once.
The function `is_pangram` takes a string of text as input and returns `True` if the text is a pangram, or `False` otherwise.

## Purpose 🎯

The script provides an easy way to verify if a given string contains all 26 letters of the English alphabet, which is commonly useful in applications like font testing or keyboard layouts.

## How It Works 🔍

1. **Input Format**:
    - The user inputs a string containing only English letters and spaces.
2. **Function Logic**:

    - The `is_pangram` function first converts the input string to lowercase to ensure case-insensitive comparison.
    - It then checks if each letter from 'a' to 'z' is present in the string.
    - If any letter is missing, it returns `False`. If all letters are found, it returns `True`.

3. **Example**:

    ```
    Enter the text: The quick brown fox jumps over the lazy dog
    Output: True
    ```

4. **Edge Cases**:
    - The string may contain uppercase and lowercase letters, which will be handled uniformly by converting the text to lowercase.
    - It only considers English letters and spaces, and spaces are ignored in the check.

## Usage 📦

1. Copy the code into a Python file, e.g., `pangram_check.py`.
2. Run the script in the terminal:
    ```bash
    python pangram_check.py
    ```
3. Enter a text string when prompted.
4. The script will print `True` if the text is a pangram, or `False` otherwise.

## Conclusion 🚀

This script helps identify whether a given text contains all the letters of the English alphabet, a useful tool for font presentation and testing applications where full alphabet coverage is needed.
