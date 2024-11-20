# Russian Alphabet Letter Finder 🇷🇺

## Description 📝

This program takes an uppercase Russian letter as input and determines the next letter in the Russian alphabet.
If the entered letter is the last in the alphabet (`Я`), it informs the user that there are no subsequent letters.

## Purpose 🎯

To help identify the next letter in the Russian alphabet or indicate when the last letter has been reached.
This can be useful for educational purposes or simple string manipulations.

## How It Works 🔍

1. The program calculates the Unicode value of the input letter using Python's `ord()` function.
2. It checks whether the input letter is the last (`Я`) in the Russian alphabet:
    - If it is, the program outputs:  
      `"There are no further letters"`.
3. Otherwise, it calculates the Unicode value of the next letter and converts it back to a character using `chr()`.
4. The next letter is displayed.

## Output 📜

### Examples:

```bash
Input 1: Б
Output 1: В

Input 2: Я
Output 2: There are no further letters
```

## Usage 📦

1. Run the program in a Python environment.
2. Enter an uppercase Russian letter when prompted.
3. View the next letter or the notification that the entered letter is the last.

### Edge Cases:

-   If the input is not a valid uppercase Russian letter, the program will not handle such input gracefully (additional validation can be added as needed).

## Conclusion 🚀

This simple program illustrates the use of Unicode operations for handling alphabetic sequences in a non-English alphabet.
It highlights the versatility of Python's character manipulation capabilities.
