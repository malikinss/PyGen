# Rectangle Class Shape Descriptor

## Description 📝

The `Rectangle` class represents a rectangle with a specified length and width, set during instantiation.
It implements both formal (`__repr__`) and informal (`__str__`) string representations as `Rectangle(<length>, <width>)`, aligning them to meet the specified requirement.

## Purpose 🎯

This class is designed for representing rectangles with consistent string output, suitable for geometric applications, educational examples of string representation, or systems needing clear object descriptions.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `length` and `width` attributes.
-   ****repr**() Method**: Returns the formal string `Rectangle(<length>, <width>)`, ideal for debugging or object recreation.
-   ****str**() Method**: Returns the same string as `__repr__()`, fulfilling the requirement for identical formal and informal representations.

## Usage 📦

1. Save the class in a Python file, e.g., `rectangle.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from rectangle import Rectangle
rect = Rectangle(5, 3)
print(rect)
print(repr(rect))
```

## Conclusion 🚀

The `Rectangle` class provides a simple and unified string representation for rectangles in Python, meeting the specified format for both formal and informal outputs.
Its design is minimal yet effective, easily extensible with additional properties or methods for more complex geometric functionality.
