# Output Longest Strings from File 📜🔝

## Description 📝

This program reads a file named **"lines.txt"** and outputs all the **longest strings** in the file while maintaining their original order.

## Purpose 🎯

To identify and print the longest strings from a file without changing the order in which they appear.

## How It Works 🔍

1. **Reading File (`get_data_from_file`)**:

    - The file **"lines.txt"** is opened and read line by line.
    - Each line is stripped of trailing newline characters to ensure clean input.

2. **Finding Longest Lines (`get_longest_lines`)**:

    - The program calculates the **maximum length** of all lines using `max(data, key=len)`.
    - It then filters out all lines whose length matches the **maximum length** and returns them in the same order.

3. **Printing Longest Lines**:
    - The longest lines are printed one by one using the `print(*data, sep='\n')` method to ensure each line appears on a new line.

## Example Usage:

**File (`lines.txt`):**

```
Short line.
Longer line than before.
The longest line in the entire file.
Short one.
The longest line in the entire file.
```

**Program Output:**

```python
>>> The longest line in the entire file.
>>> The longest line in the entire file.
```

## Conclusion 🚀

This program provides a straightforward solution to find and output the longest strings from a text file, keeping their order intact. It leverages Python's string manipulation and filtering capabilities to deliver a clean and efficient result.
