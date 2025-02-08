# Writing Numbered List to a File

## Description 📝

This Python program reads the contents of a file `input.txt`, adds a line number to each line, and writes the result to a new file called `output.txt`. Each line in the new file is preceded by its line number in the format `N) line_text`.

## Purpose 🎯

The purpose of this program is to demonstrate how to read from and write to text files, as well as how to enumerate the lines of a file and format them in a specific way.

## How It Works 🔍

1. **Reading Data**:
    - The `read_data_from_file()` function reads the contents of `input.txt` and returns the lines as a list of strings.
2. **Enumerating Lines**:
    - The `enumerate_data_rows()` function adds line numbers to each line of text in the format `N) line_text`.
3. **Writing Data**:
    - The `write_data_to_file()` function writes the numbered lines to `output.txt`.

## Output 📜

The program creates (or overwrites) the `output.txt` file, with each line from `input.txt` preceded by its line number in the following format:

```
1) This is the first line.
2) This is the second line.
...
```

## Usage 📦

1. Save the code in a file, e.g., `add_line_numbers.py`.
2. Make sure the `input.txt` file is in the same directory as the script and contains some text.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command:
   `python add_line_numbers.py`
6. The program will create or overwrite the `output.txt` file with the numbered lines.

## Conclusion 🚀

This program demonstrates how to manipulate text files in Python, specifically for reading, numbering the lines, and writing the output to a new file. It showcases file handling, list manipulation, and formatting text for output.
