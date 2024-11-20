# Lexicographic Min/Max Line Finder 📝

## Description 📝

This program reads a sequence of lines and finds the lexicographically minimum and maximum lines.
The sequence ends with the word `"END"` (which is not part of the sequence).
The program outputs the minimum and maximum lines in lexicographic order, using the format:
`Minimum line ⬇️: <minimum line>`
`Maximum line ⬆️: <maximum line>`

This is useful for finding the "smallest" and "largest" strings in a list based on their lexicographic comparison.

## Purpose 🎯

The purpose of this program is to read a sequence of lines, identify the lexicographically smallest and largest lines, and print them.
It works by comparing strings in the order they are inputted and ensures that the result is not affected by the `"END"` keyword used to stop the sequence.

## How It Works 🔍

1. The program continuously reads input lines until the word "END" is encountered.
2. It compares each line against the current minimum and maximum values.
3. Once all lines are processed, it outputs the minimum and maximum lines.

### Example

```bash
Input:
apple
banana
grape
END

Output:
Minimum line ⬇️: apple
Maximum line ⬆️: grape
```

## Usage 📦

1. Copy the program code into a Python script file (e.g., `find_min_max_lines.py`).
2. Run the script in your terminal or an IDE.
3. Enter lines of text, each on a new line. The sequence ends when the word "END" is typed.
4. The program will print the minimum and maximum lines based on lexicographic order.

## Conclusion 🚀

This program provides a simple and efficient way to find the lexicographically smallest and largest lines from a sequence.
It stops reading input at the keyword `"END"` and outputs the results in a clear, readable format.
