# Vector Class Calculator

## Description 📝

The `Vector` class represents a 2D vector on a plane, defined by its x and y coordinates.
It allows instantiation with optional coordinates (defaulting to 0, 0) and provides a method to calculate the vector's absolute value (magnitude) using the Euclidean distance formula.
The class uses the `sqrt` function from the `math` module for this computation.

## Purpose 🎯

This class is designed for geometric calculations involving 2D vectors, making it useful in educational settings, physics simulations, or graphics programming where vector magnitudes are needed.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `x` and `y` attributes, defaulting to 0 if no values are provided.
-   **abs() Method**: Calculates the vector's magnitude using the formula `sqrt(x^2 + y^2)`, where `x` and `y` are the coordinates, and returns the result as a float.

## Output 📜

Example usage:

```python
vector = Vector(3, 4)
print(vector.abs())  # Output: 5.0
vector2 = Vector()
print(vector2.abs())  # Output: 0.0
vector3 = Vector(1, 1)
print(vector3.abs())  # Output: 1.4142135623730951
```

## Usage 📦

1. Save the class in a Python file, e.g., `vector.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from vector import Vector
my_vector = Vector(5, 12)
print(f"Vector magnitude: {my_vector.abs()}")  # Output: Vector magnitude: 13.0
```

## Conclusion 🚀

The `Vector` class offers a concise and accurate way to represent and compute the magnitude of a 2D vector in Python.
Its simplicity makes it an excellent tool for basic vector operations, and it can be extended with additional methods like vector addition or normalization for more advanced geometric applications.
