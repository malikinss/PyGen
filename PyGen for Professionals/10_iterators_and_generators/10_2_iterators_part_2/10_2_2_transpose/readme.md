# Matrix Transposition with `transpose()` 📝

## Description 📝

The `transpose()` function takes a matrix (a list of lists) and returns its transposed version, where rows are turned into columns and vice versa. The transposition is performed using the `zip()` function.

## Purpose 🎯

-   **Matrix Transposition**: Switches rows with columns in a matrix.
-   **Flexibility**: Works with matrices of any dimension (rectangular or square).
-   **Efficiency**: The function returns a new matrix without modifying the original.

## How It Works 🔍

1. **Function Definition**:
    - `transpose(matrix)` takes a matrix represented as a list of lists.
2. **Using `zip()`**:

    - The `zip(*matrix)` function combines corresponding elements from each row into a new tuple, which effectively forms the columns of the original matrix.
    - `list(row)` is used to convert each tuple into a list, forming the transposed rows.

3. **Returning the Result**:
    - The list comprehension `[list(row) for row in zip(*matrix)]` generates the transposed matrix.

## Output 📜

1. Given an original matrix:

```python
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

The transposed matrix will be:

```python
transposed_matrix = transpose(original_matrix)
print(transposed_matrix)
```

Output:

```
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

## Usage 📦

1. Call the `transpose()` function with any matrix (list of lists) as an argument.
2. The function will return the transposed matrix with rows converted into columns.

## Conclusion 🚀

The `transpose()` function effectively handles matrix transposition, making it easy to swap rows and columns using Python's powerful `zip()` function, and ensures that the original matrix remains unchanged.
