# Penultimate Line Reader 📜

## Description 📝

This program reads a file name from user input and displays the **penultimate (second-to-last) line** of the file.

## Purpose 🎯

Useful for quickly retrieving the penultimate line of a text file without manually opening it.

## How It Works 🔍

1. **File Reading**:
    - The program opens the file in read mode (`'r'`).
    - It reads all lines into a list using `.readlines()`.
2. **Accessing the Penultimate Line**:
    - Since the file is **guaranteed to have at least two lines**, it directly returns `lines[-2]`, stripping any trailing newline.

## Example Usage:

**File (`example.txt`):**

```
First line
Second line
Third line
Fourth line
```

**Program Output:**

```python
>>> Enter the file name: example.txt
Third line
```

## Conclusion 🚀

The `get_penultimate_line()` function efficiently retrieves the penultimate line of a file, ensuring a quick and simple solution for this task. 🚀
