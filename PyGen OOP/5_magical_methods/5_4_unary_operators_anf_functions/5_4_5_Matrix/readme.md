# Matrix Class Grid Operator

## Description 📝

The `Matrix` class represents a 2D matrix with specified rows and columns, initialized with a default value of 0.
It includes methods to get and set values, provides formal (`__repr__`) and informal (`__str__`) string representations, and supports unary operators `+` (copy), `-` (negate), `~` (transpose), as well as rounding via `round()` with an optional precision argument.

## Purpose 🎯

This class is designed for matrix manipulation, suitable for mathematical computations, educational examples of operator overloading, or applications needing grid-based data structures.

## How It Works 🔍

-   **Initialization**: Sets `rows` and `cols`, creating a 2D list `matrix` filled with the initial `value`.
-   ****repr**()**: Returns `Matrix(<rows>, <cols>)`.
-   ****str**()**: Returns elements as rows separated by newlines, with spaces between columns.
-   **get_value()**: Retrieves the value at `(row, col)`.
-   **set_value()**: Sets the value at `(row, col)`.
-   ****pos**()**: Creates a new `Matrix` with copied values.
-   ****neg**()**: Creates a new `Matrix` with negated values.
-   ****invert**()**: Creates a transposed `Matrix` (swaps rows and cols).
-   ****round**()**: Creates a new `Matrix` with elements rounded to `n` decimal places (default 0).

## Usage 📦

1. Save the class in a Python file, e.g., `matrix.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from matrix import Matrix
m = Matrix(2, 3, 1.5)
m.set_value(0, 1, 2.75)
print(m)
print(repr(m))
print(+m)
print(-m)
print(~m)
print(round(m, 1))
```

## Conclusion 🚀

The `Matrix` class offers a comprehensive way to manage 2D matrices in Python, with intuitive string outputs, element access, and operator support.
Its flexible design makes it a strong foundation for adding binary operations like matrix multiplication or advanced features like determinant calculation.
