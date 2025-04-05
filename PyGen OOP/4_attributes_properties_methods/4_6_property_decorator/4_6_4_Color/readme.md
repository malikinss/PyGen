# Color Class Hex Manager

## Description 📝

The `Color` class represents a color using hexadecimal notation, initialized with a hex code (e.g., '#RRGGBB' or 'RRGGBB').
It stores the red (`r`), green (`g`), and blue (`b`) components as decimal values (0-255) and provides a read-write `hexcode` property to access or update the color, ensuring synchronization with the component attributes.

## Purpose 🎯

This class is designed for color manipulation in applications like graphic design tools, educational examples of property usage, or systems requiring RGB color handling in hexadecimal format.

## How It Works 🔍

-   **Initialization**: The `__init__` method parses the hex code, converting it to decimal `r`, `g`, and `b` values.
-   **hexcode Property (Getter)**: Constructs and returns the hex code from `r`, `g`, and `b` using `_get_hex()`.
-   **hexcode Property (Setter)**: Updates `r`, `g`, and `b` by parsing a new hex code with `_get_dec()`.
-   **Helper Methods**: `_get_hex()` converts decimals to two-digit hex strings; `_get_dec()` converts hex strings to decimals.

## Usage 📦

1. Save the class in a Python file, e.g., `color.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from color import Color
color = Color('#FF0000')
print(f"Red: {color.r}, Green: {color.g}, Blue: {color.b}")
print(f"Hex: {color.hexcode}")
color.hexcode = '00FF00'
print(f"New Red: {color.r}, New Green: {color.g}, New Blue: {color.b}")
print(f"New Hex: {color.hexcode}")
```

## Conclusion 🚀

The `Color` class offers a seamless way to manage colors in hexadecimal format in Python, dynamically linking the hex code with RGB components.
Its property-based approach makes it intuitive and extensible, potentially supporting additional features like color blending or validation for more advanced use cases.
