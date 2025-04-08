# Vector Class Plane Comparator

## Description 📝

The `Vector` class represents a 2D vector with `x` and `y` coordinates, set during instantiation.
It provides a formal string representation via `__repr__` as `Vector(<x>, <y>)` and supports equality (`==`) and inequality (`!=`) comparisons with other `Vector` instances or tuples of two numbers, returning `NotImplemented` for invalid comparisons.

## Purpose 🎯

This class is designed for vector representation and comparison, suitable for geometric applications, educational examples of comparison operators, or systems needing vector equality checks.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `x` and `y` attributes from the provided coordinates.
-   ****repr**() Method**: Returns the formal string `Vector(<x>, <y>)`.
-   ****eq**() Method**: Implements equality comparison:
    -   With another `Vector`, checks if `x` and `y` match.
    -   With a 2-element tuple, compares `x` with the first element and `y` with the second.
    -   Returns `NotImplemented` for other types, enabling Python to handle `__ne__` automatically via inversion.

## Usage 📦

1. Save the class in a Python file, e.g., `vector.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from vector import Vector
v1 = Vector(1, 2)
v2 = Vector(1, 2)
v3 = Vector(3, 4)
print(v1 == v2)
print(v1 != v3)
print(v1 == (1, 2))
print(v1 != (3, 4))
```

## Conclusion 🚀

The `Vector` class provides a straightforward way to represent and compare vectors in Python, with robust equality handling for both vectors and tuples.
Its design is extensible, allowing for additional comparison operators or vector operations like addition to enhance functionality.
