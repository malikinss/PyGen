# Magic Square Checker 🧙‍♂️

## Description 📝

This program checks whether a given square matrix is a magic square.
A magic square is a square matrix of size `n x n` filled with numbers from `1` to `n^2` in such a way that the sum of each row, column, and diagonal is the same.

## Purpose 🎯

The program determines if a matrix meets the criteria of a magic square:

-   Every row, column, and diagonal must sum to the same value.
-   All integers from `1` to `n^2` must be present in the matrix exactly once.

## How It Works 🔍

1. The program accepts an integer `n` representing the size of the matrix.
2. It then reads `n` rows of integers to construct the matrix.
3. The sum of the main diagonal is calculated and used as the control sum.
4. The program checks each row, column, and both diagonals to ensure they match the control sum.
5. Additionally, it verifies that all numbers from `1` to `n^2` are present.
6. The program outputs `YES` if the matrix is a magic square and `NO` otherwise.

## Output 📜

-   `YES` – The matrix is a magic square.
-   `NO` – The matrix is not a magic square.

## Usage 📦

1. Run the program.
2. Enter the matrix size `n`.
3. Input the matrix row by row.
4. View the result indicating if the matrix is a magic square.

### Example:

```
Input:
3
8 1 6
3 5 7
4 9 2

Output:
YES
```

### Explanation:

-   Row sums: 15, 15, 15
-   Column sums: 15, 15, 15
-   Diagonal sums: 15, 15
-   All numbers from 1 to 9 are present.

## Conclusion 🚀

This program provides a simple and efficient way to verify if a matrix is a magic square.
It's a useful exercise for practicing matrix manipulation and mathematical logic in programming.
