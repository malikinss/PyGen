# Matrix with Diagonals Filled with Increasing Numbers 🔢

## Description 📝

This program creates a square matrix of size `n x n` and fills it based on the following rules:

-   The main diagonal contains the number 0.
-   The diagonals adjacent to the main diagonal contain the number 1.
-   The next two diagonals contain the number 2, and so on.

## Purpose 🎯

-   Demonstrate matrix creation and manipulation based on diagonal positions.
-   Illustrate the use of absolute differences to fill the matrix with the appropriate numbers.

## How It Works 🔍

1. **Function `create_matrix(n: int)`**:
    - Creates an `n x n` matrix where each element is filled based on its distance from the main diagonal.
    - The main diagonal is filled with 0, the diagonals adjacent to it with 1, the next diagonals with 2, and so on.
2. **Function `print_matrix(matrix: List[List[int]])`**:

    - Prints the generated matrix row by row.

3. **Function `main()`**:
    - Reads the matrix size `n` from input, calls the function to create the matrix, and prints the result.

## Usage 📦

1. Run the script `matrix_diagonals.py`.
2. Input a natural number `n` to define the size of the matrix (e.g., `3`, `4`, `5`).
3. The program will generate and print the matrix with the specified diagonal rules.

### Example:

```
Input: 5
Output:
0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0
```

## Output 📜

-   The matrix with the main diagonal containing 0.
-   Adjacent diagonals containing increasing numbers starting from 1.
-   Each row is printed in a readable format with space-separated values.

## Conclusion 🚀

This program efficiently fills and displays a matrix according to the given diagonal pattern, showcasing basic matrix manipulation and the use of absolute differences to calculate values.
