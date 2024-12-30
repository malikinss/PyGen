# Find Maximum Element's Indices Program 📝

## Description 📝

This program reads a matrix of integers and finds the indices of the first occurrence of the maximum element in the matrix.
The indices are returned as a tuple of row and column numbers, where the numbering starts from zero.

## Purpose 🎯

The purpose of this program is to locate the position of the largest number in a matrix and return its position in the form of row and column indices.
This is useful for applications such as matrix analysis or optimization problems.

## How It Works 🔍

1. **Input**:
    - The program reads two integers, `n` (the number of rows) and `m` (the number of columns), followed by `n` rows of `m` integers.
2. **Matrix Processing**:
    - The program traverses the matrix to find the first occurrence of the maximum element. The traversal starts from the top-left corner of the matrix and checks each element.
3. **Output**:
    - The program prints the row and column indices of the first occurrence of the maximum element in the matrix.

### Example:

**Input:**

```plaintext
3
3
1 2 3
4 5 6
7 8 9
```

**Output:**

```plaintext
2 2
```

**Explanation:**

-   The matrix has 3 rows and 3 columns. The maximum element is `9`, and its position is at row `2`, column `2` (using zero-based indexing).

## Usage 📦

1. Copy the code into a Python file (e.g., `max_element_indices.py`).
2. Run the script:
    ```bash
    python max_element_indices.py
    ```
3. Enter the number of rows (`n`), columns (`m`), followed by the matrix elements (one row at a time).

## Conclusion 🚀

This program efficiently identifies the position of the first occurrence of the maximum element in a matrix.
It is a simple solution for matrix-related queries and can be modified to suit more complex matrix manipulations.
