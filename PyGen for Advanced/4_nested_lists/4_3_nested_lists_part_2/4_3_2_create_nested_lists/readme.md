# Create Nested List Program 📝

## Description 📝

This program creates a nested list, where each sublist contains a sequence of integers starting from 1 up to the index of that sublist.
The number of sublists is determined by the input `n`.

## Purpose 🎯

The purpose of this program is to generate a nested list of integers where each sublist contains increasing sequences starting from 1.

## How It Works 🔍

1. **Input**: The program takes an integer `n` as input, which determines the number of sublists.
2. **List Creation**: The program uses a `for` loop to create `n` sublists. Each sublist is created using `list(range(1, i+1))`, which generates a list of integers from 1 to `i`.

3. **Output**: After generating the nested list, the program prints each sublist on a new line.

### Example:

For `n = 4`, the input and output will look like this:
**Input**:

```plaintext
4
```

**Output**:

```plaintext
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
```

This means that the program has created 4 sublists, each containing integers from 1 to the index of that sublist.

## Usage 📦

1. Copy the code into a Python file, e.g., `create_nested_lists.py`.
2. Run the script in the terminal:
    ```bash
    python create_nested_lists.py
    ```
3. Enter a number `n` when prompted.
4. The program will output `n` sublists, where each sublist contains a sequence of integers from 1 up to the index of the sublist.

## Conclusion 🚀

This program demonstrates how to generate a nested list in Python, where each sublist contains increasing numbers.
It's a simple example that can be useful in various scenarios where nested structures are needed.
