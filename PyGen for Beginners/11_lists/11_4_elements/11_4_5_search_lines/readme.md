# Search Lines 📝

## Description 📝

This Python program takes a set of input lines and a search term, then prints all the lines that contain the search term. The search is case-insensitive, meaning it doesn't matter whether the search term or the input lines are in upper or lower case.

## Purpose 🎯

The program is useful for filtering a list of strings based on a search term. It can be applied in contexts like log file analysis, text search, and other scenarios where you need to find occurrences of a term in a given set of strings.

## How It Works 🔍

1. The program first reads an integer `n` which specifies the number of input lines.
2. Then, it reads `n` lines of text.
3. Afterward, the program reads a search term.
4. It then compares each line to the search term (case-insensitive).
5. Finally, the program prints all lines that contain the search term.

## Output 📜

```bash
Example Input:
5
apple pie
banana bread
apple sauce
orange juice
apple tart
apple

Example Output:
apple pie
apple sauce
apple tart
```

## Usage 📦

1. Save the script as `search_lines.py`.
2. Run the script in a Python environment.
3. Input the number `n` (number of lines to be entered).
4. Input the `n` lines, one per line.
5. Input the search term.
6. The program will output all lines that contain the search term.

## Conclusion 🚀

This program allows you to easily filter lines based on a search term, making it useful for data analysis, log searching, and text processing tasks.
