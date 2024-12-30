# Create List of Lists Program 📝

## Description 📝

This program generates a list of `n` sublists, where each sublist contains integers from 1 to `n`.
The number `n` is taken as input from the user, and the program outputs each sublist line by line.

## Purpose 🎯

The purpose of this program is to demonstrate how to create a list of lists in Python, where each sublist contains a sequence of integers from 1 to `n`.
This is a simple example of list manipulation.

## How It Works 🔍

1. **Input**: The program takes an integer `n` as input, which represents the number of sublists and the maximum integer in each sublist.
2. **List Creation**: The program uses a `for` loop to create `n` sublists. Each sublist is created using `list(range(1, n+1))`, which generates a list of integers from 1 to `n`.
3. **Output**: After the list of lists is created, the program prints each sublist on a new line.

### Example:

For `n = 3`, the input and output will look like this:
**Input**:

```plaintext
3
```

**Output**:

```plaintext
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
```

This means that the program has created 3 sublists, each containing the numbers from 1 to 3.

## Usage 📦

1. Copy the code into a Python file, e.g., `create_lists.py`.
2. Run the script in the terminal:
    ```bash
    python create_lists.py
    ```
3. Enter a number `n` when prompted.
4. The program will output `n` sublists, each containing integers from 1 to `n`.

## Conclusion 🚀

This program demonstrates a simple approach to creating and manipulating lists in Python.
It's useful for scenarios where I need a collection of lists, each containing a sequence of numbers.
