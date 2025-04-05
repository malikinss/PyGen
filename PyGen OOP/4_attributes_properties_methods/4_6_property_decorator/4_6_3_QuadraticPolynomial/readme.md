# QuadraticPolynomial Class Math Tool

## Description 📝

The `QuadraticPolynomial` class models a square trinomial `ax^2 + bx + c`, initialized with coefficients `a`, `b`, and `c`.
It provides read-only properties for the roots (`x1`, `x2`) and a string representation (`view`), plus a read-write property for the coefficients, ensuring all properties update dynamically with coefficient changes.

## Purpose 🎯

This class is designed for mathematical analysis of quadratic equations, suitable for educational purposes, root-finding applications, or simulations involving polynomials.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `a`, `b`, and `c` attributes.
-   **x1 Property**: Returns the first root using `(-b - sqrt(b^2 - 4ac)) / 2a`, or `None` if no real roots exist.
-   **x2 Property**: Returns the second root using `(-b + sqrt(b^2 - 4ac)) / 2a`, or `None` if no real roots exist.
-   **view Property**: Returns the trinomial as a string, e.g., `1x^2 + 2x - 3`.
-   **coefficients Property**: Provides get/set access to `(a, b, c)` tuple, updating attributes when set.
-   **Helper Method**: `_calculate_discriminant()` computes `b^2 - 4ac` for root calculations.

## Usage 📦

1. Save the class in a Python file, e.g., `quadratic_polynomial.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from quadratic_polynomial import QuadraticPolynomial
poly = QuadraticPolynomial(1, -5, 6)
print(f"Roots: {poly.x1}, {poly.x2}")
print(f"Polynomial: {poly.view}")
poly.coefficients = (1, 0, 1)
print(f"New roots: {poly.x1}, {poly.x2}")
print(f"New polynomial: {poly.view}")
```

## Conclusion 🚀

The `QuadraticPolynomial` class offers a robust way to work with square trinomials in Python, dynamically tracking roots and representation as coefficients change.
Its property-based design makes it intuitive and extensible, potentially supporting additional features like root multiplicity or graphing capabilities.
