# `matrix_by_elem` Generator Refactor Using `yield from`

## Description 📝

The `matrix_by_elem` function generates a sequence of elements from a matrix (a list of lists), yielding each element one by one, following the order of rows.
The function has been refactored using the `yield from` construct to simplify the code and improve readability.

## Purpose 🎯

This generator is designed to produce a flat sequence of elements from a matrix, which could have arbitrary dimensions (i.e., any number of rows and columns).
It ensures that elements are yielded in the same order as they appear row by row in the matrix.

## How It Works 🔍

-   The function uses `yield from` to iterate over each row in the matrix, yielding the elements in sequence.
-   `yield from` automatically handles the iteration over each row, making the code concise and readable.

## Output 📜

Example usage:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

gen = matrix_by_elem(matrix)

# Print all elements of the matrix
for elem in gen:
    print(elem)
```

**Output:**

```
1
2
3
4
5
6
7
8
9
```

## Usage 📦

1. **Create a matrix and extract elements**:
    ```python
    matrix = [
        [1.1, 2.2, 3.3],
        [4.4, 5.5],
        [6.6]
    ]
    gen = matrix_by_elem(matrix)
    for elem in gen:
        print(elem)
    ```

## Conclusion 🚀

The `matrix_by_elem` function has been successfully refactored using the `yield from` construct.
This makes the generator more concise while maintaining its functionality of yielding all elements from a matrix in row-major order.
