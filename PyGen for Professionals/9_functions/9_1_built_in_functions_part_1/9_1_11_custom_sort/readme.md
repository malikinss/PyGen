# Custom Sorting of a String

## Description 📝

This script implements a custom sorting function that arranges characters in a string based on specific sorting rules:

1. Lowercase letters (sorted alphabetically) come first.
2. Uppercase letters (sorted alphabetically) come next.
3. Numbers are sorted such that odd numbers come before even numbers.

## Purpose 🎯

The goal is to practice custom sorting with Python's `sorted()` function and sorting keys.
This implementation ensures structured ordering of mixed characters while following predefined constraints.

## How It Works 🔍

1. **TODO Comment**: Describes the sorting rules applied to the input string.
2. **`custom_sort()` Function**:
    - Uses a helper function `character_sort_key()` to define sorting priorities.
    - Applies the sorting order:
        - Lowercase letters (`a-z`) have the highest priority.
        - Uppercase letters (`A-Z`) come after lowercase letters.
        - Odd digits (`1, 3, 5, 7, 9`) come before even digits (`0, 2, 4, 6, 8`).
    - Uses `sorted()` with the custom key function to order the characters.
    - Joins the sorted characters into a final string.
3. **`character_sort_key()` Function**:
    - Returns a sorting key as a tuple based on character type and position.
    - The tuple structure ensures correct ordering of characters.
4. **Example Execution**:
    - Reads user input.
    - Calls `custom_sort()` to sort the string.
    - Prints the sorted result.

## Output 📜

For an input like:

```plaintext
aC3bA2d1
```

The output will be:

```plaintext
abdAC31
```

Explanation:

-   `abd` (sorted lowercase letters)
-   `AC` (sorted uppercase letters)
-   `31` (sorted odd numbers)
-   `2` (sorted even number)

## Usage 📦

1. Save the code to a file (e.g., `custom_sort.py`).
2. Open a terminal and navigate to the script's directory.
3. Run the script with:
    ```
    python custom_sort.py
    ```
4. Enter a string containing Latin letters and numbers.
5. Observe the sorted output based on the given rules.

## Conclusion 🚀

This script demonstrates how to perform advanced character sorting using custom keys in Python's `sorted()` function.
It is a great example of leveraging tuple-based sorting to control ordering in a structured manner.
