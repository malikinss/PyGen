# Matrix Function 🧮

## Description 📝

This function, `matrix()`, dynamically creates and returns a matrix of a specified size, filled with a given value. It provides flexibility in defining dimensions and default values.

## Purpose 🎯

The function is designed to generate matrices based on the number of rows and columns specified by the user. If no dimensions are provided, it defaults to a `1×1` matrix filled with `0`.

## How It Works 🔍

-   `matrix()` → Returns a `1×1` matrix filled with `0`.
-   `matrix(n)` → Returns an `n×n` matrix filled with `0`.
-   `matrix(n, m)` → Returns an `n×m` matrix filled with `0`.
-   `matrix(n, m, value)` → Returns an `n×m` matrix where each element is set to `value`.

The function uses default parameters and a list comprehension to efficiently generate the matrix.

## Output 📜

Example calls and their expected outputs:

```python
print(matrix())
# [[0]]

print(matrix(3))
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(matrix(2, 5))
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

print(matrix(3, 4, 9))
# [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]
```

## Usage 📦

1. Call `matrix()` with no arguments to get a `1×1` matrix of zeros.
2. Call `matrix(n)` to get an `n×n` matrix of zeros.
3. Call `matrix(n, m)` to get an `n×m` matrix of zeros.
4. Call `matrix(n, m, value)` to get an `n×m` matrix with the specified value.

## Conclusion 🚀

This function simplifies matrix creation by leveraging default arguments and list comprehensions, making it easy to generate matrices of any size and fill them with any value. It is efficient and flexible for various use cases.
