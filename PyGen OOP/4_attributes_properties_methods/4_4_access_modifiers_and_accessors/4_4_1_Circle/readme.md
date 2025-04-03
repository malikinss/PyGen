# Circle Class Geometry Tool

## Description 📝

The `Circle` class represents a circle defined by its radius, with calculated diameter and area stored as private attributes.
It takes a radius upon instantiation and provides methods to retrieve the radius, diameter, and area, using the mathematical constant π from the `math` module for area computation.

## Purpose 🎯

This class is designed for geometric calculations involving circles, suitable for educational purposes, mathematical modeling, or applications requiring basic circle properties.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets `_radius` to the provided value, calculates `_diameter` as `2 * radius`, and computes `_area` as `π * radius^2`.
-   **get_radius() Method**: Returns the stored `_radius`.
-   **get_diameter() Method**: Returns the stored `_diameter`.
-   **get_area() Method**: Returns the stored `_area`.

## Usage 📦

1. Save the class in a Python file, e.g., `circle.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from circle import Circle
my_circle = Circle(3)
print(f"Radius: {my_circle.get_radius()}")      # Output: Radius: 3
print(f"Diameter: {my_circle.get_diameter()}")  # Output: Diameter: 6
print(f"Area: {my_circle.get_area()}")          # Output: Area: 28.274333882308138
```

## Conclusion 🚀

The `Circle` class provides a simple and efficient way to encapsulate and access a circle’s geometric properties in Python.
Its use of private attributes and getter methods ensures data integrity, making it a solid foundation that can be extended with setters or additional properties like circumference for more advanced geometric applications.
