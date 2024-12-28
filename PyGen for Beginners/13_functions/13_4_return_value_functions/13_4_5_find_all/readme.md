# Find All Symbol Locations Program 🔍

## Description 📝

This Python program takes a string and a symbol (character) as inputs and returns a list containing all the indices of the specified symbol in the string.
It efficiently identifies all occurrences of the symbol and returns their positions.

## Purpose 🎯

-   To find all occurrences of a character within a string.
-   Useful in searching, text processing, and analyzing character frequencies.

## How It Works 🔍

1. **Function `find_all(target, symbol)`**:
    - The function iterates through each character in the `target` string and checks if it matches the specified `symbol`.
    - If the symbol matches, the index of the symbol is added to the list.
2. **Example**:
   For the input `target = "banana"` and `symbol = "a"`, the function will return the list `[1, 3, 5]` since the letter "a" appears at these indices.

## Usage 📦

1. Copy the code into a Python file, e.g., `find_all_symbol.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python find_all_symbol.py
    ```
5. Input the target string and symbol (character) when prompted. The program will then return a list of indices where the symbol appears.

## Conclusion 🚀

This function helps you efficiently find all occurrences of a character in a string, making it suitable for various text processing tasks, such as searching or text analysis.
