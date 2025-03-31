# Scales Class Simulator

## Description 📝

The `Scales` class models a two-pan balance scale, allowing weights to be added to either the left or right pan.
It tracks the total weight on each pan and provides a method to determine the balance state, returning whether the scale is balanced, or which pan is heavier.
The class requires no arguments upon instantiation.

## Purpose 🎯

This class is designed to simulate a physical balance scale, useful for teaching object-oriented programming concepts, modeling physical systems, or as part of a larger simulation involving weight comparisons.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets both `left_pan` and `right_pan` attributes to 0, representing empty pans.
-   **add_right() Method**: Adds a specified weight to the `right_pan`.
-   **add_left() Method**: Adds a specified weight to the `left_pan`.
-   **get_result() Method**: Compares the weights and returns a string: "The scale is balanced" if equal, "The left pan is heavier" if the left is greater, or "The right pan is heavier" if the right is greater.

## Output 📜

Example usage:

```python
scales = Scales()
print(scales.get_result())  # Output: The scale is balanced
scales.add_left(2.5)
scales.add_right(1.5)
print(scales.get_result())  # Output: The left pan is heavier
scales.add_right(1.0)
print(scales.get_result())  # Output: The scale is balanced
```

## Usage 📦

1. Save the class in a Python file, e.g., `scales.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from scales import Scales
my_scales = Scales()
my_scales.add_left(3)
my_scales.add_right(2)
print(my_scales.get_result())  # Output: The left pan is heavier
my_scales.add_right(1)
print(my_scales.get_result())  # Output: The scale is balanced
```

## Conclusion 🚀

The `Scales` class provides an intuitive and functional way to simulate a two-pan balance scale in Python.
Its ability to track and compare weights makes it a practical tool for simple balance simulations, and it can be extended with features like weight removal or precision adjustments for more complex scenarios.
