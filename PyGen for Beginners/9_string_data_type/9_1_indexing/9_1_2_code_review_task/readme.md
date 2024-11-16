# Code Review Task 3 🪲

## Description 📝

This task demonstrates how to enhance a Python script to output a specific character from a string using negative indexing. The program processes the string `"In 2010, someone paid 10k Bitcoin for two pizzas."` and retrieves the character at index `-10`, which is the letter `w`.

## Purpose 🎯

The purpose of this program is to:

1. Use string indexing with negative indices to extract a specific character.
2. Correctly implement the indexing operator `[]` to avoid errors.
3. Showcase Python’s flexibility in string manipulation using negative indexing.

## How It Works 🔍

-   The program initializes the string `s`.
-   It uses the indexing operator `[]` with the negative index `-10` to access the 10th character from the end of the string.
-   The output displays the character found at the specified position.

## Output 📜

-   The program outputs: `w`

## Identified Errors in the Original Code 🕵🏾:

1. **Empty Indexer**:

    - Original: `print(s[])`
    - Issue: The `[]` operator requires a valid integer index.
    - Fix: Specify the index `-10` to retrieve the character `w`.

2. **Lack of Explanation**:
    - The original code lacks comments explaining the purpose or logic of the indexing.

## Fixed Code 🛠:

```python
# Original string
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

# Output the 'w' character using negative indexing
print(s[-10])  # Outputs the letter 'w' at index -10
```

## Explanation of Changes 🧾:

1. **Added a valid index**: Used the negative index `-10` to access the letter `w`.
2. **Provided comments**: Included comments to clarify the purpose of the code.

## Conclusion 🚀

This task demonstrates the correct use of negative indexing to access characters from the end of a string.
The program now outputs the letter `w` as intended, emphasizing the versatility of Python's string operations.
