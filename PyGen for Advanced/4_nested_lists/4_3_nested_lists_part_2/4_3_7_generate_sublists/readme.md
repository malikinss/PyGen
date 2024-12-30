# Generating Contiguous Sublists from a List 📝

## Description 📝

This program takes a string of characters as input, converts it into a list of characters, and then generates all possible contiguous sublists of the list, including the empty list.
The order of sublists is maintained in the order in which they appear in the main list.

## Purpose 🎯

The purpose of this program is to generate all possible sublists of a given list, considering contiguous sequences of elements.
This can be useful in various scenarios such as substring search, pattern matching, or extracting all possible subsequences from a list.

## How It Works 🔍

1. **Input**:
    - The program receives a string of characters, and it splits this string into a list of individual characters.
2. **Logic**:
    - The program uses two loops:
        - The outer loop selects the starting index of the sublist.
        - The inner loop creates sublists starting from the current index to every possible end index, generating all contiguous sublists.
    - It begins with an empty list, as the empty list is always a sublist of any list.
3. **Output**:
    - The program outputs a list of all sublists, including the empty list, in the order of their appearance in the original list.

### Example:

For the input:

```plaintext
a b c
```

The output will be:

```plaintext
[[], ['a'], ['a', 'b'], ['a', 'b', 'c'], ['b'], ['b', 'c'], ['c']]
```

This shows all possible contiguous sublists, including the empty list, from the original list.

## Usage 📦

1. Copy the code into a Python file, e.g., `generate_sublists.py`.
2. Run the script in the terminal:
    ```bash
    python generate_sublists.py
    ```
3. Enter the characters as space-separated values on the first line.
4. The program will output the list of all possible contiguous sublists.

## Conclusion 🚀

This program effectively generates and outputs all contiguous sublists, providing a comprehensive set of subsequences from the input list, including the empty list.
