# Vector Class Plane Operator

## Description 📝

The `Vector` class represents a 2D vector with `x` and `y` coordinates, set during instantiation.
It provides a formal string representation via `__repr__` as `Vector(<x>, <y>)` and an informal one via `__str__` as `(<x>, <y>)`.
It supports unary operators `+` (same coordinates) and `-` (negated coordinates) and returns its modulus via `abs()` using the formula `sqrt(x^2 + y^2)`.

## Purpose 🎯

This class is designed for vector representation and basic operations, suitable for geometric computations, educational examples of operator overloading, or applications needing vector magnitude.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets `x` and `y` attributes.
-   ****repr**() Method**: Returns `Vector(<x>, <y>)` for formal output.
-   ****str**() Method**: Returns `(<x>, <y>)` for informal output.
-   ****pos**() Method**: Implements unary `+`, returning a new `Vector` with unchanged coordinates.
-   ****neg**() Method**: Implements unary `-`, returning a new `Vector` with negated coordinates.
-   ****abs**() Method**: Calculates and returns the vector’s modulus using `sqrt(x^2 + y^2)`.

## Usage 📦

1. Save the class in a Python file, e.g., `vector.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from vector import Vector
v = Vector(3, 4)
print(v)
print(repr(v))
print(+v)
print(-v)
print(abs(v))
```

## Conclusion 🚀

The `Vector` class provides a robust and intuitive way to handle 2D vectors in Python, with clear string representations, unary operator support, and modulus calculation.
Its design is versatile, making it a solid foundation for adding binary operations like addition or dot product for more advanced vector functionality.
