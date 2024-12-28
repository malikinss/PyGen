# Longest Word Length Program

## Description 📝

This Python program determines the length of the longest word in a given string of text.
The program uses a list expression to calculate the length of each word and then finds the maximum length.

## Purpose 🎯

-   To find the length of the longest word in an input string.
-   To demonstrate the use of string manipulation, list expressions, and the `max()` function in Python.

## How It Works 🔍

1. **Function `longest_word_length`**:

    - The function takes an input string `text` and splits it into a list of words using the `split()` method.
    - It checks if the list of words is empty, returning 0 if true.
    - The function uses a list expression to calculate the length of each word and returns the maximum value using the `max()` function.

2. **Processing**:

    - The input string is split into words.
    - For each word, its length is calculated.
    - The maximum length among all words is found and returned.

3. **Output**:
    - The program prints the length of the longest word.

## Output 📜

The program prints the length of the longest word in the given string.

**Example 1**:

```
Input:
The quick brown fox jumps over the lazy dog

Output:
5
```

**Example 2**:

```
Input:
Python programming is fun

Output:
11
```

## Usage 📦

1. Copy the code into a Python file, e.g., `longest_word_length.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python longest_word_length.py
    ```
5. Enter a string of text when prompted.
6. View the output: the program will print the length of the longest word.

## Conclusion 🚀

This program is a simple yet effective way to analyze strings and extract information about their structure.
It showcases Python's ability to manipulate strings and perform operations on them concisely. 🎉
