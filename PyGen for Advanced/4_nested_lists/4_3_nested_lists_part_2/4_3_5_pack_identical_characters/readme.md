# Identical Character Packing 📝

## Description 📝

This program takes a string as input and packs sequences of identical characters into sublists.
Consecutive identical characters are grouped together into one sublist, and different characters start new sublists.

## Purpose 🎯

The purpose of this program is to take a string and group consecutive identical characters into sublists.
It helps in identifying and grouping repeating patterns in strings.

## How It Works 🔍

1. **Input**: The program accepts a string `s` containing characters as input.
2. **Logic**:
    - The program initializes an empty list `lst` to store the sublists.
    - It starts by adding the first character as a sublist.
    - As the program iterates through the string, it checks if each character is identical to the previous one.
      If so, it adds the character to the current sublist; otherwise, it starts a new sublist.
3. **Output**: The program outputs a list of lists, each containing consecutive identical characters.

### Example:

For the input string `"aaabbccaaa"`, the input and output will look like this:

**Input**:

```plaintext
aaabbccaaa
```

**Output**:

```plaintext
[['a', 'a', 'a'], ['b', 'b'], ['c', 'c'], ['a', 'a', 'a']]
```

This means the program successfully grouped the identical characters together into sublists.

## Usage 📦

1. Copy the code into a Python file, e.g., `pack_identical_characters.py`.
2. Run the script in the terminal:
    ```bash
    python pack_identical_characters.py
    ```
3. Enter a string when prompted.
4. The program will output the packed sequences of identical characters.

## Conclusion 🚀

This program is a simple yet powerful tool to process and group characters in a string based on their identity, helping to identify patterns or simplify data representation.
