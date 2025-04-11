# QuadraticPolynomial Class Function Evaluator

## Description 📝

The `QuadraticPolynomial` class represents a quadratic trinomial `ax^2 + bx + c`, initialized with coefficients `a`, `b`, and `c`.
It’s a callable object that takes a number `x` and returns the polynomial’s value at that point, computed as `ax^2 + bx + c`.

## Purpose 🎯

This class is designed for evaluating quadratic expressions, suitable for mathematical modeling, educational examples of callable objects, or applications needing polynomial calculations.

## How It Works 🔍

-   **Initialization**: Stores coefficients `a`, `b`, and `c` as instance attributes.
-   ****call**()**: Makes instances callable, computing and returning `a * x^2 + b * x + c` for the given `x`.

## Usage 📦

1. Save the class in a Python file, e.g., `quadratic_polynomial.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from quadratic_polynomial import QuadraticPolynomial
poly = QuadraticPolynomial(1, -5, 6)  # x^2 - 5x + 6
print(poly(2))  # 4 - 10 + 6 = 0
print(poly(3))  # 9 - 15 + 6 = 0
print(poly(0))  # 0 - 0 + 6 = 6
```

## Conclusion 🚀

The `QuadraticPolynomial` class provides a simple and efficient way to evaluate quadratic polynomials in Python, using the callable pattern for intuitive usage.
Its design is straightforward and can be extended with methods like finding roots or derivatives for more advanced mathematical applications.
