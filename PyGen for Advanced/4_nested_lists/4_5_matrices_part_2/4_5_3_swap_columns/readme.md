# Swap Columns in a Matrix Program 📝

## Description 📝

This program swaps two specified columns in a given matrix.
The matrix is input by the user, and the program exchanges the values in the specified columns, then prints the modified matrix.

## Purpose 🎯

The purpose of this program is to demonstrate how to swap columns in a matrix, which can be useful for matrix manipulation tasks, data reordering, and algorithmic challenges.

## How It Works 🔍

1. **Input**:

    - The program reads the number of rows `n` of the matrix.
    - It then reads the `n` rows of the matrix, each containing space-separated integers.
    - The program also reads a list of two column indices to swap.

2. **Swapping Logic**:

    - The columns at the specified indices are swapped by iterating over each row and swapping the elements at the given column positions.

3. **Output**:
    - After the columns are swapped, the program prints the modified matrix.

### Example:

**Input:**

```plaintext
3
1 2 3
4 5 6
7 8 9
0 2
```

**Output:**

```plaintext
3 2 1
6 5 4
9 8 7
```

**Explanation:**

-   The matrix has 3 rows and 3 columns. The user specifies columns `0` and `2` for swapping. The first and third columns are exchanged, resulting in the modified matrix.

## Usage 📦

1. Copy the code into a Python file (e.g., `swap_columns.py`).
2. Run the script:
    ```bash
    python swap_columns.py
    ```
3. Enter the number of rows (`n`), the matrix elements (one row at a time), and the two column indices to swap.

## Conclusion 🚀

This program provides an easy-to-understand method for swapping columns in a matrix, making it useful for matrix manipulation tasks in various programming applications.
