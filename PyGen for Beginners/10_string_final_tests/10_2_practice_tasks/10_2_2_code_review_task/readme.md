# Code Review Task 🪲

## Description 📝

This task updates a Python script to output the fourth character of a given string:  
`"Python rocks!"`.

## Purpose 🎯

The purpose of this program is to:

1. Demonstrate how to access individual characters in a string using indexing.
2. Output the fourth character from the given string.
3. Provide an example of precise string manipulation in Python.

## How It Works 🔍

-   The program defines a string `s` with the value `"Python rocks!"`.
-   By using indexing (`s[3]`), the fourth character of the string is accessed.
-   The program then prints the result to the console.

## Output 📜

-   The program outputs the fourth character of the string:  
    `"h"`

## Identified Errors in the Original Code 🕵🏾:

1. **Missing indexing operation**:
    - Original: `print()`
    - Issue: No indexing is applied to extract the fourth character.
    - Fix: Use `s[3]` to access the fourth character of the string.

## Fixed Code 🛠:

```python
# Define the string
s = 'Python rocks!'

# Access and print the fourth character
print(s[3])
# Outputs: h
```

## Explanation of Changes 🧾:

1. **Indexing applied**: Used `s[3]` to access the fourth character of the string (Python uses 0-based indexing).
2. **Output clarity:** Printed the extracted character directly to the console.

## Conclusion 🚀

This task highlights how to use string indexing to retrieve specific characters.
By completing the missing code, the script now correctly outputs the fourth character of the given string.
