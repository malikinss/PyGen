# Matrix Shuffling Program 🔀

## Description 📝

This program randomly shuffles the contents of a two-dimensional list (matrix).
The matrix is shuffled both row-wise (shuffling each row individually) and overall (shuffling the rows themselves).

## Purpose 🎯

The purpose of this program is to demonstrate how to randomly shuffle a matrix, which can be useful for simulations, randomization tasks, or game development.

## How It Works 🔍

1. **Input**:

    - A two-dimensional list (matrix) is provided as the input. This matrix consists of rows, where each row is a list of integers.

2. **Processing**:

    - The program first shuffles the elements within each row of the matrix using `random.shuffle()`.
    - Afterward, the rows themselves are shuffled, effectively randomizing the order of the rows in the matrix.

3. **Output**:
    - The matrix is shuffled in-place, meaning that the contents of the matrix are modified without returning a new matrix.

## Output 📜

The contents of the matrix are shuffled, but the program does not print the matrix. The matrix is modified in place.

### Example:

If the initial matrix is:

```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

After shuffling, it could become:

```
[[3, 2, 1],
 [5, 6, 4],
 [9, 7, 8]]
```

## Usage 📦

1. Copy the code into a Python file (e.g., `shuffle_matrix.py`).
2. Define a matrix (two-dimensional list) and pass it to the `shuffle_matrix()` function.
3. The matrix will be shuffled in place.

### Example Run:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

shuffle_matrix(matrix)

# The matrix has been shuffled in place
print(matrix)  # Example output: [[3, 2, 1], [5, 6, 4], [9, 7, 8]]
```

## Conclusion 🚀

This program effectively demonstrates how to shuffle a two-dimensional list (matrix) in Python, both by shuffling the rows and the elements within each row.
