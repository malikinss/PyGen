# Code Review Task 2 🪲

## Description 📝

This task demonstrates how to enhance a Python script to output a specific character from a string using indexing.
The program processes the string `"In 2010, someone paid 10k Bitcoin for two pizzas."` and retrieves the character at index `7`, which is a comma `,`.

## Purpose 🎯

The purpose of this program is to:

1. Use string indexing to extract a specific character.
2. Correctly implement the use of the indexing operator `[]` to avoid runtime errors.
3. Provide clear and functional code for character extraction.

## How It Works 🔍

-   The program defines the string `s`.
-   It uses the indexing operator `[]` with a valid integer to access the character at position `7`.
-   The output displays the character found at the specified index.

## Output 📜

-   The program outputs: `,`

## Identified Errors in the Original Code 🕵🏾:

1. **Empty Indexer**:

    - Original: `print(s[])`
    - Issue: The `[]` operator requires a valid integer index.
    - Fix: Specify the index `7` to retrieve the comma.

2. **Lack of Clarity**:
    - Original code lacks comments to explain the purpose or logic.

## Fixed Code 🛠:

```python
# Original string
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

# Output the comma character using indexing
print(s[7])  # Outputs the comma at index 7
```

## Explanation of Changes 🧾:

1. **Provided a valid index**: Added `7` to the indexing operator to retrieve the comma character.
2. **Added comments**: Included comments to clarify the purpose of the code.

## Conclusion 🚀

This task highlights the proper use of string indexing in Python.
By identifying and fixing the error, the program now retrieves and outputs the comma character `,` as intended.
The improved implementation underscores the value of precision and clarity in code.
