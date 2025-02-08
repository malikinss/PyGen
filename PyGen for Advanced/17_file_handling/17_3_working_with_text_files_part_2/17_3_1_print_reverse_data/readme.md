# Reverse Line from File 🌀📄

## Description 📝

This program reads a single line of text from a file named **"text.txt"** and displays the line in reverse order.
The text is read, then reversed, and finally printed to the screen.

## Purpose 🎯

To **reverse** the contents of a file's single line and display the result.

## How It Works 🔍

1. **File Reading (`get_data_from_file`)**:

    - Opens the **"text.txt"** file in read mode (`rt`) with UTF-8 encoding.
    - Reads the entire content and **removes** any trailing whitespace or newline characters.

2. **Reversing the String (`reverse`)**:
    - The string is **reversed** using Python's slicing method `[::-1]`, which reads the string from end to start.

## Example Usage:

**File (`text.txt`):**

```
Hello, World!
```

**Program Output:**

```python
>>> !dlroW ,olleH
```

## Conclusion 🚀

This program is a simple yet efficient way to **reverse a string** from a file. It demonstrates basic **file handling** and string manipulation techniques in Python! ✨
