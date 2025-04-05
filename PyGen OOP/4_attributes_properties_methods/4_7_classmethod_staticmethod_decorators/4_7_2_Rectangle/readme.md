# Rectangle Class Shape Creator

## Description 📝

The `Rectangle` class represents a rectangle with a specified length and width, set during instantiation.
It includes a class method `square()` that creates a `Rectangle` instance where both length and width equal a given side, effectively forming a square.

## Purpose 🎯

This class is designed for geometric modeling of rectangles and squares, ideal for educational demonstrations of class methods or applications requiring shape instantiation.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `length` and `width` attributes from the provided values.
-   **square() Method**: A `@classmethod` that takes a `side` value and returns a new `Rectangle` instance with both `length` and `width` set to `side`.

## Usage 📦

1. Save the class in a Python file, e.g., `rectangle.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from rectangle import Rectangle
rect = Rectangle(4, 3)
square = Rectangle.square(5)
print(f"Rectangle: {rect.length} x {rect.width}")
print(f"Square: {square.length} x {square.width}")
```

## Conclusion 🚀

The `Rectangle` class offers a straightforward way to create rectangles and squares in Python, with its `square()` class method providing a convenient shortcut for square instantiation.
It’s a versatile tool that can be enhanced with properties like area or additional shape-related methods.
