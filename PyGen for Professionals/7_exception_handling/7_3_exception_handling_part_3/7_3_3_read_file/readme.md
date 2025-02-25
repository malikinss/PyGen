# File Reader Program

## Description 📝

This program defines the `read_file()` function that attempts to read the contents of a specified text file.
If the file exists in the program's directory, its contents are displayed.
If the file cannot be found, an error message is printed.

## Purpose 🎯

The purpose of this program is to handle file reading operations safely by using a try-except block.
It provides clear feedback when a file is not found and allows for easy retrieval of file contents when available.

## How It Works 🔍

1. The function accepts the filename as input, which should include the file's extension.
2. The program tries to open the file using the `open()` function with UTF-8 encoding.
3. If the file is found, its contents are read and printed.
4. If the file is not found, a `FileNotFoundError` is caught, and the message "File not found" is printed instead.

## Output 📜

-   If the file is found, its contents will be displayed.
-   If the file is not found, the program will output:
    ```text
    File not found
    ```

## Usage 📦

1. The program prompts the user to enter the name of a text file.
2. It attempts to open and print the file contents or displays an error message if the file is missing.

Example:

```python
read_file('example.txt')
```

Output (if file exists):

```text
Contents of the file.
```

Output (if file does not exist):

```text
File not found
```

## Conclusion 🚀

The `read_file()` function is a simple but effective way to safely read files in Python, handling potential errors like missing files and ensuring that users receive appropriate feedback.
