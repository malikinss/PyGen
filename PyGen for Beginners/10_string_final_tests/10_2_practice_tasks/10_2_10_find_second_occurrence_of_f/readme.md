# Find Second Occurrence of 'f' 📝

## Description 📝

This Python program finds the index of the second occurrence of the letter `'f'` in a given string. If the letter `'f'` occurs only once, it returns `-1`. If the letter `'f'` is not found at all, it returns `-2`.

## Purpose 🎯

The program demonstrates string searching and conditional logic to handle different cases of letter occurrence in a string.

## How It Works 🔍

1. The function `find_second_occurrence_of_f()` first checks for the first occurrence of the letter `'f'` using `find()`.
2. If `'f'` is not found, the function returns `-2`.
3. If the first occurrence is found, the function searches for the second occurrence starting from the index right after the first occurrence.
4. If the second occurrence is found, its index is returned.
5. If the second occurrence is not found, it returns `-1`.

## Output 📜

```bash
Example Input: coffee
Example Output: 3

Example Input: french
Example Output: -1

Example Input: hello
Example Output: -2
```

## Usage 📦

1. Save the script as `find_second_occurrence.py`.
2. Run the script in a Python environment.
3. Provide a string input when prompted.
4. View the result printed to the console.

### Steps:

1. Open a terminal or Python IDE.
2. Execute the script using `python find_second_occurrence.py`.
3. Enter a string that contains the letter `'f'` when prompted.
4. The program will output the index of the second occurrence, or `-1` or `-2` based on the occurrence count.

## Conclusion 🚀

This program is an efficient way to search for specific character occurrences in a string, and it handles edge cases such as no occurrences or only one occurrence of the letter `'f'`.
