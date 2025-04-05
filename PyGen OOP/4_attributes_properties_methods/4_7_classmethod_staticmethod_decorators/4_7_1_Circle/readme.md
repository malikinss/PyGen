# Circle Class Geometry Builder

## Description 📝

The `Circle` class represents a circle defined by its radius, set during instantiation.
It includes a class method `from_diameter()` that creates a `Circle` instance based on a provided diameter, calculating the radius as half the diameter.

## Purpose 🎯

This class is designed for creating circle objects in geometric contexts, suitable for educational examples of class methods, or applications needing flexible circle instantiation.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `radius` attribute from the provided value.
-   **from_diameter() Method**: A `@classmethod` that takes a `diameter`, computes the radius as `diameter / 2`, and returns a new `Circle` instance.

## Usage 📦

1. Save the class in a Python file, e.g., `circle.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from circle import Circle
circle1 = Circle(5)
circle2 = Circle.from_diameter(10)
print(f"Circle1 radius: {circle1.radius}")
print(f"Circle2 radius: {circle2.radius}")
```

## Conclusion 🚀

The `Circle` class provides a simple and versatile way to create circle objects in Python, enhanced by its `from_diameter()` class method for alternative instantiation.
It’s a foundational tool that can be extended with properties like area or methods for geometric operations.
