# QuadraticPolynomial Class Polynomial Builder

## Description 📝

The `QuadraticPolynomial` class represents a square trinomial `ax^2 + bx + c`, initialized with coefficients `a`, `b`, and `c`.
It includes two class methods:

-   `from_iterable()` to create an instance from an iterable of coefficients
-   `from_str()` to create one from a space-separated string of coefficients converted to floats.

## Purpose 🎯

This class is designed for flexible instantiation of quadratic polynomials, suitable for mathematical modeling, educational examples of class methods, or applications needing polynomial representations.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `a`, `b`, and `c` attributes from provided values.
-   **from_iterable() Method**: A `@classmethod` that unpacks an iterable of three elements into `a`, `b`, and `c` to create a new instance.
-   **from_str() Method**: A `@classmethod` that splits a string into three parts, converts them to floats, and creates a new instance.

## Usage 📦

1. Save the class in a Python file, e.g., `quadratic_polynomial.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from quadratic_polynomial import QuadraticPolynomial
poly1 = QuadraticPolynomial(1, -5, 6)
poly2 = QuadraticPolynomial.from_iterable([1, 2, 3])
poly3 = QuadraticPolynomial.from_str("1 -2 4")
print(f"Poly1: {poly1.a}, {poly1.b}, {poly1.c}")
print(f"Poly2: {poly2.a}, {poly2.b}, {poly2.c}")
print(f"Poly3: {poly3.a}, {poly3.b}, {poly3.c}")
```

## Conclusion 🚀

The `QuadraticPolynomial` class provides a versatile way to instantiate square trinomials in Python, with its class methods enabling creation from various data sources.
It’s a practical tool that can be extended with properties like roots or string representation for enhanced functionality.
