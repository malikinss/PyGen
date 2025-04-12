# ColoredPoint Class Plane Position Marker

## Description 📝

The `ColoredPoint` class represents a point on a 2D plane with `x` and `y` coordinates and a `color` attribute, all set during instantiation.
It provides read-only access to these attributes via properties (`x`, `y`, `color`), ensuring immutability after creation.
The class supports a formal string representation as `ColoredPoint(x, y, 'color')`, equality comparisons (`==`, `!=`) based on matching coordinates and color, and hashing via `hash()` using a tuple of `(x, y, color)`. Invalid comparison operands return `NotImplemented`.

## Purpose 🎯

This class is designed for geometric applications, visualization tools, or data structures where points with associated colors need to be uniquely identified, compared, or stored (e.g., in sets or dictionaries).
It’s ideal for graphics programming, game development, or educational exercises demonstrating Python’s property decorators, comparison methods, and hashable objects, offering a clear and robust way to model colored points with consistent behavior.

## How It Works 🔍

-   **Initialization (`__init__`)**: Accepts three arguments (`x`, `y`, `color`) of any type, storing them as private attributes (`_x`, `_y`, `_color`) to prevent direct modification and support read-only properties.
-   **Properties**:
    -   `x` (read-only): Returns `_x`, exposing the x-coordinate.
    -   `y` (read-only): Returns `_y`, exposing the y-coordinate.
    -   `color` (read-only): Returns `_color`, exposing the color value.
    -   Implemented using `@property` decorators to ensure attributes are accessible but not modifiable, maintaining encapsulation.
-   **Formal Representation (`__repr__`)**: Returns a string in the format `ColoredPoint(x, y, 'color')`, with `color` enclosed in single quotes for clarity, providing a precise and reproducible depiction of the point.
-   **Equality Comparison (`__eq__`)**:
    -   Checks if `other` is a `ColoredPoint` instance using `isinstance`.
    -   Returns `True` if `x`, `y`, and `color` match exactly; `False` otherwise.
    -   Returns `NotImplemented` for non-`ColoredPoint` operands, allowing Python to handle invalid comparisons gracefully (e.g., enabling `__ne__` via fallback).
-   **Hashing (`__hash__`)**: Computes the hash of a tuple `(self._x, self._y, self._color)` using the built-in `hash()` function, ensuring consistent hash values for equal points, making instances suitable for use in hash-based collections like sets or dictionaries.
-   **Immutability**: By using private attributes and read-only properties, ensures the point’s state (coordinates and color) remains fixed after creation, aligning with hashability requirements.

## Usage 📦

1. **Save the Code**: Store the `ColoredPoint` class in a Python file, e.g., `colored_point.py`, for use in projects or submission to a testing system.
2. **Create and Test Instances**: Instantiate points and explore their properties, comparisons, and hashing:
    ```python
    from colored_point import ColoredPoint
    p1 = ColoredPoint(1, 2, "red")
    p2 = ColoredPoint(1, 2, "red")
    p3 = ColoredPoint(3, 4, "blue")
    print(p1)           # ColoredPoint(1, 2, 'red')
    print(p1.x, p1.y, p1.color)  # 1 2 red
    print(p1 == p2)     # True
    print(p1 == p3)     # False
    print(hash(p1) == hash(p2))  # True
    print({p1, p3})    # {ColoredPoint(1, 2, 'red'), ColoredPoint(3, 4, 'blue')}
    ```
3. **Apply in Context**: Use in graphics applications to represent colored pixels, in games for sprite positions, or in data analysis to track labeled coordinates, leveraging equality for deduplication and hashing for efficient storage.
4. **Test Behaviors**: Experiment with different coordinate types (integers, floats) and color values (strings, numbers) to confirm robust comparison and hashing, or try invalid comparisons (e.g., `p1 == 42`) to verify `NotImplemented` handling.

## Conclusion 🚀

The `ColoredPoint` class offers a clean and reliable implementation for modeling colored points on a plane in Python, balancing simplicity with powerful functionality.
Its read-only properties ensure immutability, making it safe for hashing and comparisons, while the formal string representation provides clear debugging output.
The equality checks and hash computation enable seamless integration into collections, supporting use cases from visualization to data processing.
This class excels in both practical applications—where precise point representation is needed—and educational settings, illustrating key Python concepts like properties, dunder methods, and hashability.
While already complete, it could be extended with features like distance calculations or coordinate transformations, but its current form fully meets the task’s requirements with elegance and precision, ready to enhance any project needing structured, comparable, and hashable colored points.
