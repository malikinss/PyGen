# Code Review Task 🪲

## Description 📝

This task demonstrates how to enhance a Python script to output the first 12 characters of a string using slicing. The program processes the string `"In 2010, someone paid 10k Bitcoin for two pizzas."` and retrieves the substring `"In 2010, som"`.

## Purpose 🎯

The purpose of this program is to:

1. Use slicing to extract a specific range of characters from a string.
2. Correctly implement the slicing operator `[:n]` to avoid errors.
3. Showcase Python's ability to handle substrings efficiently.

## How It Works 🔍

-   The program initializes the string `s`.
-   It uses slicing `[:12]` to extract the first 12 characters.
-   The output displays the substring formed by the specified range.

## Output 📜

-   The program outputs: `In 2010, som`

## Identified Errors in the Original Code 🕵🏾:

1. **Empty Print Statement**:

    - Original: `print()`
    - Issue: The `print()` function lacks an argument, producing no output.
    - Fix: Add slicing `s[:12]` as the argument to retrieve the first 12 characters.

2. **Lack of Explanation**:
    - The original code lacks comments to explain the slicing operation.

## Fixed Code 🛠:

```python
# Original string
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

# Output the first 12 characters using slicing
print(s[:12])  # Outputs 'In 2010, som'
```

## Explanation of Changes 🧾:

1. **Implemented slicing**: Used `[:12]` to extract the first 12 characters from the string.
2. **Added comments**: Included comments to clarify the purpose and logic of the slicing operation.

## Conclusion 🚀

This task demonstrates the correct use of slicing to retrieve a substring from the start of a string.
By fixing the error, the program now outputs the first 12 characters as intended, showcasing Python’s powerful string manipulation capabilities.
