# Circle Class Calculator

## Description 📝

The `Circle` class represents a circle with geometric properties. It takes a radius as input during instantiation and automatically calculates the diameter and area based on this value, using the mathematical constant π (pi) from the `math` module.

## Purpose 🎯

This class provides a simple way to model a circle and access its key properties—radius, diameter, and area—making it useful for educational purposes, geometric calculations, or as part of a larger graphics or physics simulation.

## How It Works 🔍

-   **Initialization**: The `__init__` method accepts a `radius` parameter and sets it as an instance attribute.
-   **Diameter Calculation**: The `diameter` attribute is computed as `radius * 2`.
-   **Area Calculation**: The `area` attribute is calculated using the formula `π * radius^2`, where `pi` is imported from the `math` module.

## Output 📜

Example usage:

```python
circle = Circle(5)
print(f"Radius: {circle.radius}")    # Output: Radius: 5
print(f"Diameter: {circle.diameter}") # Output: Diameter: 10
print(f"Area: {circle.area}")        # Output: Area: 78.53981633974483
```

## Usage 📦

1. Save the class in a Python file, e.g., `circle.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from circle import Circle
my_circle = Circle(3)
print(f"Circle with radius {my_circle.radius} has diameter {my_circle.diameter} and area {my_circle.area}")
# Output: Circle with radius 3 has diameter 6 and area 28.274333882308138
```

## Conclusion 🚀

The `Circle` class offers an efficient and accurate way to represent a circle’s properties in Python.
By automatically calculating the diameter and area from a given radius, it simplifies geometric computations and serves as a reusable component that can be extended with methods like circumference calculation or radius updates for more advanced use cases.
