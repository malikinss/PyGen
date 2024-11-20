# Unicode Code Points of a String 🌐

## Description 📝

This program takes a string as input and translates each character into its corresponding Unicode code point, displaying the results in a single line separated by spaces.

## Purpose 🎯

To demonstrate the mapping of characters in a string to their Unicode code points and showcase Python's ability to handle Unicode conversions efficiently.

## How It Works 🔍

1. The program accepts a string from the user.
2. It iterates through each character in the string:
    - For each character, it uses Python's `ord()` function to find its Unicode code point.
3. The Unicode code points are printed in a single line, separated by spaces.

## Output 📜

### Example:

```bash
Input: Hello!
Output: 72 101 108 108 111 33
```

### Explanation:

-   `H` corresponds to Unicode code point `72`.
-   `e` corresponds to `101`, `l` corresponds to `108`, and so on.
-   `!` corresponds to `33`.

## Usage 📦

1. Run the program in a Python environment.
2. Input a string when prompted.
3. View the Unicode code points of the string's characters.

### Notes:

-   The program supports all Unicode characters, including special symbols and non-Latin scripts.
-   If the string is empty, no output will be produced.

## Conclusion 🚀

This program highlights the link between text and its underlying numerical representation, making it useful for encoding tasks and exploring Unicode's versatility.
