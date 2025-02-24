# Line Counter 📝

## Description 📝

This program counts the number of lines in a given text file and prints the result.

## Purpose 🎯

To correct a previously faulty program that failed to properly read and count the lines in the file.

## How It Works 🔍

1. The function `count_lines(filename)`:
    - Takes the file name as an argument.
    - Opens the file using the `open()` function with UTF-8 encoding.
    - Uses a generator expression inside `sum()` to iterate over each line of the file and count them.
2. The program prints the result, which is the total number of lines in the specified file.

## Output 📜

**Example Input:**
The file `data.txt` contains 5 lines.
**Example Output:**

```python
5
```

## Usage 📦

1. Make sure the file `data.txt` is in the correct directory or provide the correct file path.
2. Run the script, and it will output the number of lines in the file.

## Conclusion 🚀

The fixed implementation counts lines efficiently using a generator expression, making the program concise and easy to understand.
