# Rectangle Class Geometry Tool

## Description 📝

The `Rectangle` class represents a rectangle defined by its length and width.
It provides direct access to these attributes and includes read-only properties for calculating the perimeter and area, which update dynamically when the length or width changes.

## Purpose 🎯

This class is designed for geometric computations involving rectangles, making it suitable for educational purposes, design applications, or simulations requiring area and perimeter calculations.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `length` and `width` attributes.
-   **get_perimeter() Method**: Calculates the perimeter as `2 * (length + width)`.
-   **get_area() Method**: Calculates the area as `length * width`.
-   **Properties**: `perimeter` and `area` are defined as read-only properties using the `property` decorator, linked to their respective getter methods.

## Usage 📦

1. Save the class in a Python file, e.g., `rectangle.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from rectangle import Rectangle
rect = Rectangle(4, 3)
print(f"Perimeter: {rect.perimeter}")
print(f"Area: {rect.area}")
rect.length = 5
print(f"New Perimeter: {rect.perimeter}")
print(f"New Area: {rect.area}")
```

## Conclusion 🚀

The `Rectangle` class offers a straightforward and dynamic way to work with rectangle properties in Python.
Its read-only properties ensure consistent perimeter and area calculations, providing a solid base that can be extended with setters or additional geometric features for more advanced use cases.
