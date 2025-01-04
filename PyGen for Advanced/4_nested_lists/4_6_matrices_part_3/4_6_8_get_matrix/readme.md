# Snake Pattern Matrix Program 🐍

## Description 📝

This program generates an `n x m` matrix filled with numbers in a "snake" pattern. The numbers in the matrix fill each row either from left to right (increasing order) or from right to left (decreasing order), creating a snake-like flow.

### Example:

For the input:

```
n = 3
m = 5
```

The resulting matrix will be:

```
1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
```

## Purpose 🎯

The purpose of this program is to create a matrix filled in a zigzag or "snake" pattern, alternating the direction of the numbers in each row. This can be useful for tasks involving matrix traversal or pattern generation.

## How It Works 🔍

1. The program takes input values for `n` (number of rows) and `m` (number of columns).
2. It generates each row based on the current row number:
    - Odd-numbered rows (1st, 3rd, etc.) are filled with numbers in increasing order.
    - Even-numbered rows (2nd, 4th, etc.) are filled with numbers in decreasing order.
3. After constructing each row, it is appended to the matrix.
4. The matrix is then printed row by row.

## Output 📜

The program prints the generated matrix with the "snake" pattern, where each row alternates in direction.

### Example:

For input `n = 3` and `m = 5`, the output will be:

```
1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
```

## Usage 📦

1. Run the program.
2. Input the values for `n` (number of rows) and `m` (number of columns).
3. View the resulting snake-patterned matrix printed on the screen.

## Conclusion 🚀

This program demonstrates how to fill a matrix in a snake-like pattern, alternating the direction of the numbers in each row. It’s a useful technique for various matrix manipulation tasks and pattern generation exercises.
