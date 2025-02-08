# Reverse Lines from File 🔄📄

## Description 📝

This program reads all the lines from a text file named **"data.txt"** and prints them in **reverse order**.
The last line is printed first, followed by the penultimate one, and so on.

## Purpose 🎯

To **reverse the order** of lines in a file and output them, starting with the last line.

## How It Works 🔍

1. **Reading File (`get_data_from_file`)**:

    - Opens the file **"data.txt"** in read mode (`rt`) with UTF-8 encoding.
    - Reads all lines from the file and strips any trailing newline or whitespace characters.

2. **Reversing Lines (`reverse_lines`)**:

    - The order of the lines is **reversed** using Python's slicing method `[::-1]`, which reverses the list.

3. **Printing Reversed Lines**:
    - The reversed list is printed line by line using the `print(*data, sep='\n')` method to ensure each line appears on a new line.

## Example Usage:

**File (`data.txt`):**

```
First line.
Second line.
Third line.
```

**Program Output:**

```python
>>> Third line.
>>> Second line.
>>> First line.
```

## Conclusion 🚀

This program demonstrates how to easily **reverse the order of lines** in a text file and display them efficiently.
It highlights basic **file handling** and **list manipulation** in Python.
