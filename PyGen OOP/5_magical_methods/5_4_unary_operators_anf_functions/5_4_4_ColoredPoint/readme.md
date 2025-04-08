# ColoredPoint Class Plane Marker

## Description 📝

The `ColoredPoint` class represents a point on a plane with `x` and `y` coordinates and an RGB color, defaulting to black `(0, 0, 0)`.
It provides a formal string representation via `__repr__` including coordinates and color, and an informal one via `__str__` showing only coordinates.
It supports unary operators: `+` (copy), `-` (negate coordinates), and `~` (swap coordinates and invert color).

## Purpose 🎯

This class is designed for representing colored points, suitable for graphics programming, educational examples of operator overloading, or applications needing positional and color data.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets `x`, `y`, and `color` attributes, with `color` defaulting to `(0, 0, 0)`.
-   ****repr**() Method**: Returns `ColoredPoint(<x>, <y>, <color>)` for formal output.
-   ****str**() Method**: Returns `(<x>, <y>)` for informal output.
-   ****pos**() Method**: Implements unary `+`, returning a new instance with unchanged values.
-   ****neg**() Method**: Implements unary `-`, negating coordinates while keeping the color.
-   ****invert**() Method**: Implements unary `~`, swapping `x` and `y` and inverting each color component (255 - value).

## Usage 📦

1. Save the class in a Python file, e.g., `colored_point.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from colored_point import ColoredPoint
p = ColoredPoint(1, 2, (255, 0, 0))
print(p)
print(repr(p))
print(+p)
print(-p)
print(~p)
```

## Conclusion 🚀

The `ColoredPoint` class offers a versatile way to manage colored points in Python, with clear string representations and intuitive unary operator support.
Its design is robust and can be extended with methods like distance calculation or color manipulation for more advanced graphical applications.
