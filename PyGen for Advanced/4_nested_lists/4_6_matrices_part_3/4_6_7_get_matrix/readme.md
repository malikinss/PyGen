# Matrix Pattern Program 🧮

## Description 📝

This program generates an `n x m` matrix filled with numbers from 1 to `m` following a specific pattern. The first row starts from `1` to `m`, and each subsequent row is a shifted version of the previous one.

### Example:

For the input:

```
n = 5
m = 4
```

The resulting matrix will be:

```
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
```

## Purpose 🎯

The purpose of this program is to generate a matrix based on a specific pattern where the rows follow a cyclic shift of numbers from `1` to `m`.

## How It Works 🔍

1. The program takes the input values `n` and `m`, which define the number of rows and columns, respectively.
2. The first row is initialized with numbers from `1` to `m`.
3. Each subsequent row is created by shifting the numbers from the previous row, ensuring the pattern.
4. The matrix is printed, row by row, with the values separated by spaces.

## Output 📜

The program prints the generated matrix where each row is a shifted version of the first row.

### Example:

For input `n = 5` and `m = 4`, the output will be:

```
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
```

## Usage 📦

1. Run the program.
2. Input the values of `n` (number of rows) and `m` (number of columns).
3. View the resulting matrix printed on the screen.

## Conclusion 🚀

This program demonstrates how to generate a matrix where each row is a cyclically shifted version of the previous one, providing a unique pattern generation technique for matrix manipulation.
