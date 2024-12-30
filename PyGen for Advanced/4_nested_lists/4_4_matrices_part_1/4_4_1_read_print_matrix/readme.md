# Matrix Input and Output 📝

## Description 📝

This program reads a matrix from user input, where the matrix dimensions (rows and columns) and elements are provided line by line.
The program then outputs the matrix in a readable format.

## Purpose 🎯

The purpose of this program is to handle matrix input and output operations.
It demonstrates how to read matrix elements dynamically and print them in the same structure as input, making it useful for matrix manipulations, data processing, and visualization tasks.

## How It Works 🔍

1. **Input**:
    - The program first accepts two integers, `n` and `m`, representing the number of rows and columns of the matrix.
    - Matrix elements are then entered line by line in row-major order.
2. **Logic**:
    - The program uses nested loops:
        - The outer loop iterates over the number of rows.
        - The inner loop collects `m` elements for each row.
    - Each element is read individually, and rows are appended to construct the matrix.
3. **Output**:
    - The matrix is printed row by row with elements separated by spaces.

### Example:

For the input:

```plaintext
3
3
a
b
c
d
e
f
g
h
i
```

The output will be:

```plaintext
a b c
d e f
g h i
```

## Usage 📦

1. Copy the code into a Python file, e.g., `matrix_io.py`.
2. Run the script:
    ```bash
    python matrix_io.py
    ```
3. Enter the matrix dimensions (rows and columns).
4. Provide matrix elements one by one.
5. The program will print the matrix in the same format as it was entered.

## Conclusion 🚀

This program simplifies matrix input and output handling in Python.
It provides an efficient way to collect and display matrix data, ensuring correct formatting and readability.
