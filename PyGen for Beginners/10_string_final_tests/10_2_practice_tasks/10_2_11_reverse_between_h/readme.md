# Reverse Substring Between First and Last 'h' 📝

## Description 📝

This Python program takes a string as input and reverses the sequence of characters between the first and last occurrences of the letter `'h'`. The rest of the string remains unchanged.

## Purpose 🎯

The program demonstrates string manipulation, including finding specific characters, slicing, and reversing substrings in Python.

## How It Works 🔍

1. The function `reverse_between_h()` finds the index of the first and last occurrences of the letter `'h'`.
2. It extracts the substring between these two indices and reverses it.
3. The original string is reconstructed by concatenating the part before the first `'h'`, the reversed substring, and the part after the last `'h'`.
4. The modified string is returned.

## Output 📜

```bash
Example Input: ahibchdefgh
Example Output: ahigcdhf

Example Input: hello world
Example Output: hello world
```

## Usage 📦

1. Save the script as `reverse_between_h.py`.
2. Run the script in a Python environment.
3. Provide a string containing at least two occurrences of the letter `'h'` when prompted.
4. View the modified string in the console.

### Steps:

1. Open a terminal or Python IDE.
2. Execute the script using `python reverse_between_h.py`.
3. Enter a string that contains at least two occurrences of `'h'`.
4. The program will output the string with the characters between the first and last `'h'` reversed.

## Conclusion 🚀

This program is a practical example of string slicing and reversing, and it highlights how to manipulate substrings based on specific character positions.
