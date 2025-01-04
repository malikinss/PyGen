# Square Matrix Transposition 🧮

## Description 📝

This Python program transposes a square matrix in place. Transposition involves swapping the rows and columns of the matrix without using an auxiliary list.

## Purpose 🎯

-   Demonstrate matrix manipulation by transposing rows and columns directly.
-   Efficiently perform the operation in place, saving memory.
-   Develop a deeper understanding of matrix algorithms and nested loops.

## How It Works 🔍

1. **Function `get_square_matrix()`**:

    - Accepts the matrix size `n` and reads `n` rows of space-separated integers.
    - Constructs a square matrix (list of lists).

2. **Function `transpose_matrix_in_place()`**:

    - Swaps elements `matrix[i][j]` and `matrix[j][i]` for all `i < j`.
    - Modifies the matrix directly, transposing it without creating a new matrix.

3. **Function `print_matrix()`**:

    - Prints the matrix row by row.

4. **Function `main()`**:
    - Handles user input for matrix size and data.
    - Calls functions to transpose the matrix and print the result.

## Usage 📦

1. Run the script `matrix_transpose.py`.
2. Enter the size of the square matrix (n).
3. Input the matrix row by row, space-separated.
4. The program will transpose the matrix and print the result.

### Example:

```
Enter the size of the square matrix: 3
1 2 3
4 5 6
7 8 9
```

**Output**:

```
1 4 7
2 5 8
3 6 9
```

### Explanation:

-   The original matrix:

```
1 2 3
4 5 6
7 8 9
```

-   After transposition:

```
1 4 7
2 5 8
3 6 9
```

## Output 📜

-   A square matrix that represents the transposed version of the input matrix.

## Conclusion 🚀

This program efficiently transposes square matrices by modifying them in place, demonstrating in-depth matrix manipulation skills. It's a practical algorithm for working with matrices in various computational tasks.
