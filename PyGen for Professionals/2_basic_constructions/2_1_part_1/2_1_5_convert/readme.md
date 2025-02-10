# Convert String Based on Letter Frequency

## Description 📝

This program implements the `convert()` function, which converts an input string to either all lowercase or all uppercase based on the frequency of lowercase and uppercase letters in the string.
Non-letter characters are ignored in the process.

## Purpose 🎯

The purpose of this function is to modify the case of the entire string based on the number of lowercase and uppercase letters.
This can be useful for formatting text according to letter frequency or ensuring uniformity in case formatting.

## How It Works 🔍

1. The function counts the number of lowercase and uppercase letters in the given string.
2. It ignores non-letter characters in the string.
3. If the number of lowercase letters is greater than or equal to the number of uppercase letters, the string is converted to lowercase.
4. If the number of uppercase letters is greater than lowercase, the string is converted to uppercase.

## Output 📜

The function returns a string:

-   In lowercase if the number of lowercase letters is greater than or equal to uppercase letters.
-   In uppercase if the number of uppercase letters is greater than lowercase letters.
-   If the counts of lowercase and uppercase letters are the same, the string is converted to lowercase.

## Usage 📦

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Call the `convert()` function with a string to convert it based on letter frequency.

Example:

```python
convert("Hello World!")
# Output:
# hello world!

convert("HELLO world!")
# Output:
# HELLO WORLD!
```

## Conclusion 🚀

The `convert()` function offers a simple way to convert a string to either uppercase or lowercase based on the number of each type of letter.
This is useful for consistent text formatting or for analyzing letter case in a string.
