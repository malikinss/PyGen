# Matrix Transposition Program 📝

## Description 📝

This program reads a matrix of size `n x m` from user input, displays it, and then prints its transposed version.
Transposing a matrix means swapping its rows and columns.

## Purpose 🎯

The goal of this program is to practice matrix manipulation by transposing it.
This is useful in various computational tasks such as image processing, linear algebra, and data analysis.

## How It Works 🔍

1. **Input**:
    - The program receives two integers, `n` (rows) and `m` (columns), representing the matrix dimensions.
    - Matrix elements are entered line by line in row-major order.
2. **Matrix Construction**:
    - A nested list comprehension is used to read and store matrix elements.
    - Each row is created by reading `m` elements and appended to the matrix.
3. **Matrix Transposition**:

    - The transposed matrix is created by swapping rows and columns using list comprehensions.

4. **Output**:
    - The matrix is printed row by row.
    - An empty line is printed to separate the original and transposed matrices.
    - The transposed matrix is then printed.

### Example:

**Input:**

```plaintext
2
3
a
b
c
d
e
f
```

**Output:**

```plaintext
a b c
d e f

a d
b e
c f
```

## Usage 📦

1. Copy the code into a Python file (e.g., `matrix_transpose.py`).
2. Run the script:
    ```bash
    python matrix_transpose.py
    ```
3. Enter the matrix dimensions and elements as prompted.
4. The program will display the matrix and its transposed version.

## Conclusion 🚀

This program efficiently handles matrix input, printing, and transposition, showcasing Python's list comprehensions and nested loops for clean and concise matrix operations.
