# Letter Frequency Counter in Zen of Python

## Description 📝

This Python program reads the "Zen of Python" text from a file, counts the occurrences of each letter (ignoring case and non-alphabetic characters), and displays the results in lexicographic order.
The program treats uppercase and lowercase letters as the same and ignores any non-alphabetic characters.

## Purpose 🎯

The purpose of this program is to analyze the frequency of letters in the "Zen of Python" text.
It outputs the number of times each letter appears in the text, sorted alphabetically.

## How It Works 🔍

1. The program reads the text from a file, `pythonzen.txt`.
2. It processes the text, counting the occurrences of each letter while ignoring case and non-alphabetic characters.
3. The counts of the letters are sorted in lexicographic order.
4. The program then outputs the result in the format `<letter>: <count>`.

## Output 📜

The program outputs the count of each letter in the following format:

```
a: 53
b: 21
...
```

### Example:

Input (from the file):

```
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
...
```

Output:

```
a: 53
b: 21
...
```

## Usage 📦

1. Ensure you have the `pythonzen.txt` file available in the specified path.
2. Copy the code into a Python file.
3. Run the program, and it will print the letter frequency counts.

### Example:

```python
# Input (contents of the file):
The Zen of Python, by Tim Peters

# Output:
a: 53
b: 21
...
```

## Conclusion 🚀

This program provides a simple and effective way to count the frequency of each letter in a given text, sorting the results alphabetically.
It is case-insensitive and ignores any non-alphabetic characters.
