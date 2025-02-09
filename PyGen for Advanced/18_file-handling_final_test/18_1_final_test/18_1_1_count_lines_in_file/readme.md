# Line Counting Program

## Description 📝

This Python program reads a text file and counts the number of lines in it.
The program takes the file name as input, processes the file, and outputs the total number of lines.

## Purpose 🎯

The purpose of this program is to quickly determine the number of lines in a given text file.
This can be useful for analyzing file length, verifying data completeness, or preprocessing files for further operations.

## How It Works 🔍

1. **User Input**:
    - The program takes a single input, which is the name of the file.
2. **Counting Lines**:
    - The `count_lines_in_file()` function opens the file and iterates through each line, counting the total number of lines using `sum(1 for line in given_file)`.
3. **Displaying Output**:
    - The total count is printed to the console.

## Output 📜

The program prints the number of lines in the specified file.

For example, if `sample.txt` contains:

```
Hello, World!
This is a test file.
It has three lines.
```

Running the program with input `sample.txt` will output:

```
3
```

## Usage 📦

1. Save the code in a file, e.g., `count_lines.py`.
2. Ensure that the target text file is in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the script's directory.
5. Run the script using:
    ```
    python count_lines.py
    ```
6. Enter the name of the text file when prompted.
7. The program will output the total number of lines.

## Conclusion 🚀

This program provides a simple and efficient way to count the number of lines in a file using Python's built-in file handling features. It is useful for text processing and file analysis tasks.
