# Side Diagonal Matrix Generator 🔢

## Description 📝

This program generates an `n x n` matrix based on the following rules:

-   The numbers on the side diagonal (from top-right to bottom-left) are set to `1`.
-   The numbers above the side diagonal are set to `0`.
-   The numbers below the side diagonal are set to `2`.

The program then displays the resulting matrix with each number separated by a space.

## Purpose 🎯

The program allows the user to input a natural number `n`, representing the size of the square matrix, and creates a matrix filled with a pattern based on the side diagonal.
It then displays the matrix.

## How It Works 🔍

1. The user inputs a number `n`, specifying the size of the square matrix.
2. The matrix is generated by placing `1` along the side diagonal (from top-right to bottom-left), `0` above this diagonal, and `2` below this diagonal.
3. The matrix is printed row by row with elements separated by spaces.

## Output 📜

The program prints the generated matrix based on the side diagonal rule.

### Example:

```
Input:
4

Output:
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0
```

## Usage 📦

1. Run the program.
2. Enter the size of the matrix `n`.
3. View the resulting matrix printed on the screen.

## Conclusion 🚀

This program generates a matrix with a unique pattern based on the side diagonal, providing an interesting way to practice matrix creation and manipulation in programming.