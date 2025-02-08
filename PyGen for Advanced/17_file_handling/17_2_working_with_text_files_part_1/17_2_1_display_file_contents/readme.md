# File Content Display 📄

## Description 📝

This program reads a file name from user input and displays its contents on the screen.
If the file does not exist or cannot be read, an error message is shown.

## Purpose 🎯

This function is useful for quickly viewing the contents of a text file without needing to open it in an editor.
It also includes error handling to ensure smooth execution.

## How It Works 🔍

1. **Reading the File**:

    - The program opens the file in read mode (`'r'`).
    - It reads the file line by line using a loop to avoid loading the entire file into memory.

2. **Error Handling**:
    - If the file is **not found**, a `FileNotFoundError` is caught, and an error message is displayed.
    - If there is an **I/O error** (e.g., permission issues), a generic `IOError` is caught, and an error message is displayed.

## Example Usage:

```python
>>> Enter the file name: example.txt
Hello, world!
This is a test file.
```

If the file does not exist:

```python
>>> Enter the file name: missing.txt
Error: The file 'missing.txt' does not exist.
```

## Conclusion 🚀

The `display_file_contents()` function provides a simple and efficient way to read and display a file’s contents.
It ensures that potential errors, like missing or unreadable files, are handled gracefully.
