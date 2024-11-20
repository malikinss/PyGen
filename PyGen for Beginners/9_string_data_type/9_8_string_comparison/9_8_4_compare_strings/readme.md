# String Comparison Program 📝

## Description 📝

This program compares two input strings by ignoring case and all non-alphabetic characters. It extracts only the alphabetic characters from both strings, converts them to lowercase, and compares them. If the resulting strings are equal, it outputs "YES", otherwise, it outputs "NO".

## Purpose 🎯

The program aims to provide a simple way to compare two strings by focusing only on their alphabetic characters, ignoring case sensitivity and any non-alphabetic symbols.

## How It Works 🔍

1. The program reads two strings as input.
2. It extracts the alphabetic characters from both strings and converts them to lowercase.
3. It compares the processed strings:
    - If they are identical, the program outputs "YES".
    - Otherwise, it outputs "NO".

### Example

```bash
Input:
Hello, World!
hello world

Output:
YES
```

**Explanation:**

-   Both strings have the same alphabetic characters after ignoring case and non-alphabetic characters, so the output is "YES".

```bash
Input:
Python@123
pyton

Output:
NO
```

**Explanation:**

-   The strings differ after ignoring case and non-alphabetic characters, so the output is "NO".

## Usage 📦

1. Copy the program code into a Python script file (e.g., `compare_strings.py`).
2. Run the script in your terminal or IDE.
3. Enter the first string.
4. Enter the second string.
5. The program will output whether the processed strings are equal ("YES") or not ("NO").

## Conclusion 🚀

This program simplifies string comparison by stripping away unnecessary characters and ignoring case differences, making it easier to compare two strings based only on their alphabetic content.
