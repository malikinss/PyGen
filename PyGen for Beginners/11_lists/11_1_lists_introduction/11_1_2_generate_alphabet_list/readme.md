# Generate List of First n Lowercase Alphabet Letters 📝

## Description 📝

This Python program generates a list consisting of the first `n` lowercase letters of the English alphabet.

## Purpose 🎯

The program demonstrates how to use Python's built-in `string` module to generate a list of alphabet letters, utilizing string slicing to get the first `n` letters.

## How It Works 🔍

1. The function `generate_alphabet_list()` takes an integer `n` as input.
2. It uses `string.ascii_lowercase` to access the entire lowercase English alphabet.
3. It slices the alphabet string to include only the first `n` letters.
4. The sliced string is then converted into a list and returned.

## Output 📜

```bash
 Example Input: 5
 Example Output: ['a', 'b', 'c', 'd', 'e']


 Example Input: 8
 Example Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```

## Usage 📦

1. Save the script as `generate_alphabet_list.py`.
2. Run the script in a Python environment.
3. Provide an integer `n` when prompted.
4. View the generated list of letters in the console.

### Steps:

1. Open a terminal or Python IDE.
2. Execute the script using `python generate_alphabet_list.py`.
3. Enter a positive integer value for `n` (number of letters).
4. The program will output a list of the first `n` letters of the alphabet.

## Conclusion 🚀

This program is an example of how to generate and manipulate a sequence of alphabetic characters, and it demonstrates the utility of Python's `string` module for easy access to common string constants like the alphabet.
