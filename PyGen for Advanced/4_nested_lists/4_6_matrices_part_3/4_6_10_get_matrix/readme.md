# Diagonal Pattern Matrix Program 🔺

## Description 📝

This program generates an `n x m` matrix filled with numbers in a diagonal pattern. The numbers fill the matrix such that they start from the first row or first column and move diagonally downwards, creating a visually appealing diagonal arrangement.

### Example:

For the input:

```
n = 3
m = 5
```

The resulting matrix will be:

```
1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
```

## Purpose 🎯

The purpose of this program is to create a matrix filled in a diagonal pattern, which can be useful for tasks that require diagonal traversals or pattern generation based on diagonals.

## How It Works 🔍

1. The program first reads the values of `n` (number of rows) and `m` (number of columns).
2. It then creates an empty matrix of size `n x m`, filled with zeros.
3. The matrix is then filled with numbers starting from 1, following a diagonal pattern:
    - Starting from the first row, moving down to the bottom-right corner diagonally.
    - After completing a diagonal from top to bottom, the next diagonal starts from the first column.
4. Finally, the filled matrix is printed row by row.

## Output 📜

The program prints the generated matrix filled with numbers arranged in a diagonal pattern.

### Example:

For input `n = 3` and `m = 5`, the output will be:

```
1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
```

## Usage 📦

1. Run the program.
2. Input the values for `n` (number of rows) and `m` (number of columns).
3. View the resulting diagonal-patterned matrix printed on the screen.

## Conclusion 🚀

This program demonstrates how to fill a matrix with numbers in a diagonal pattern, useful for tasks requiring traversal along diagonals or generating diagonal-based patterns.
