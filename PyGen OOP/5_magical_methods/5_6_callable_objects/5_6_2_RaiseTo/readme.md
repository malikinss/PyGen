# RaiseTo Class Power Function

## Description 📝

The `RaiseTo` class creates callable instances that raise a number to a fixed exponent specified during instantiation.
It takes one argument (`degree`) at creation and one argument (`x`) when called, returning `x` raised to `degree`.

## Purpose 🎯

This class is designed for exponentiation tasks, suitable for mathematical utilities, educational examples of callable objects, or applications needing repeated power operations.

## How It Works 🔍

-   **Initialization**: Stores the `degree` as an instance attribute.
-   ****call**()**: Makes instances callable, taking a number `x` and returning `x ** self.degree` using Python’s exponentiation operator.

## Usage 📦

1. Save the class in a Python file, e.g., `raise_to.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from raise_to import RaiseTo
square = RaiseTo(2)
cube = RaiseTo(3)
print(square(5))  # 25
print(cube(2))    # 8
print(square(3))  # 9
```

## Conclusion 🚀

The `RaiseTo` class offers a simple and elegant way to encapsulate exponentiation in Python, leveraging the callable object pattern for reusability.
Its minimal design is easily extensible, such as adding support for negative exponents or complex numbers if needed.
