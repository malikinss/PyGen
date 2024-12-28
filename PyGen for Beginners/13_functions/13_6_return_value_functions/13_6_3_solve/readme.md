# Quadratic Equation Solver 🎯

## Description 📝

This program solves a quadratic equation of the form `ax² + bx + c = 0`, where `a`, `b`, and `c` are the coefficients provided by the user.
The solution involves calculating the roots of the equation using the discriminant formula.

## Purpose 🎯

The function `solve()` calculates the roots of the quadratic equation and returns them in ascending order.
If the equation has no real solutions, it provides a message indicating that there are no real roots.

## How It Works 🔍

1. **Function `solve(a, b, c)`**:
    - The discriminant (`D`) is calculated as:
      \[
      D = b^2 - 4ac
      \]
    - Based on the value of `D`, the function determines the roots:
        - If `D > 0`, the equation has two real and distinct roots:
          \[
          x_1 = \frac{-b - \sqrt{D}}{2a}, \quad x_2 = \frac{-b + \sqrt{D}}{2a}
          \]
        - The function returns the roots in ascending order.
    - If `D < 0`, the equation has no real roots, and the function returns a message indicating so.

## Usage 📦

1. Copy the code into a Python file, e.g., `quadratic_solver.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python quadratic_solver.py
    ```
5. Enter the values for `a`, `b`, and `c`:
    - Example:
        ```
        1
        -3
        2
        ```
6. The program will output the roots of the quadratic equation:
    ```
    1.0 2.0
    ```

## Conclusion 🚀

This program provides an efficient and easy way to solve a quadratic equation and determine its roots, displaying them in ascending order.
It demonstrates the use of basic algebraic formulas and Python's `math` module to solve real-world problems.
