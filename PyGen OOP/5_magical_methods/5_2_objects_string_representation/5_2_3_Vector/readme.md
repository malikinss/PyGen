# Vector Class Plane Descriptor

## Description 📝

The `Vector` class represents a vector on a 2D plane, defined by its x and y coordinates, set during instantiation.
It provides a formal string representation via `__repr__` as `Vector(<x>, <y>)` and an informal one via `__str__` as `A vector on the plane with coordinates (<x>, <y>)`.

## Purpose 🎯

This class is designed for representing 2D vectors, suitable for geometric calculations, educational examples of string representation, or applications needing vector descriptions.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `x` and `y` attributes from the provided coordinates.
-   ****repr**() Method**: Returns the formal string `Vector(<x>, <y>)`, useful for debugging or object recreation.
-   ****str**() Method**: Returns the informal string `A vector on the plane with coordinates (<x>, <y>)` for readable output.

## Usage 📦

1. Save the class in a Python file, e.g., `vector.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from vector import Vector
vec = Vector(3, 4)
print(vec)
print(repr(vec))
```

## Conclusion 🚀

The `Vector` class offers a clear and distinct way to represent vectors in Python, with tailored formal and informal string outputs.
Its simple design makes it a solid foundation, easily extensible with vector operations like addition or magnitude calculation for more advanced use cases.
