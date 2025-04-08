# Vector Class Plane Calculator

## Description 📝

The `Vector` class represents a 2D vector with `x` and `y` coordinates, providing a formal string representation via `__repr__` as `Vector(<x>, <y>)`.
It supports addition (`+`) and subtraction (`-`) between vectors, as well as multiplication (`*`) and division (`/`) by scalars (int or float), with multiplication working in both orders.
Invalid operands return `NotImplemented`.

## Purpose 🎯

This class is designed for vector arithmetic, suitable for geometric operations, educational examples of operator overloading, or applications needing vector manipulation.

## How It Works 🔍

-   **Initialization**: Sets `x` and `y` attributes.
-   **`__repr__`()**: Returns `Vector(<x>, <y>)`.
-   **`__add__`()**: Adds coordinates of two `Vector` instances.
-   **`__sub__`()**: Subtracts coordinates of another `Vector` from this one.
-   **`__mul__`()**: Scales coordinates by a scalar.
-   **`__rmul__`()**: Handles right multiplication (e.g., `2 * vector`) by reusing `__mul__`.
-   **`__truediv__`()**: Divides coordinates by a scalar.
-   **Error Handling**: Returns `NotImplemented` for unsupported operand types.

## Usage 📦

1. Save the class in a Python file, e.g., `vector.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from vector import Vector
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(2 * v1)
print(v1 / 2)
```

## Conclusion 🚀

The `Vector` class offers a clean and robust way to perform vector operations in Python, with comprehensive arithmetic support and proper error handling.
Its design is extensible, making it a strong base for adding features like vector magnitude or dot product for more advanced geometric computations.
