# Power Function

## Description 📝

This Python script defines a function `power(degree)` that returns a new function.
The new function, when called with an integer, raises that integer to the power of the provided degree.

## Purpose 🎯

The goal is to:

-   Create a higher-order function that generates another function based on a given exponent.
-   Demonstrate closures where an inner function can access the outer function's variables (in this case, `degree`).

## How It Works 🔍

1. **Outer Function (`power`)**:
    - Takes a single argument `degree`, which specifies the exponent.
    - Ensures `degree` is an integer.
2. **Inner Function (`raise_to_power`)**:
    - Takes an argument `x` and returns `x` raised to the power of `degree`.
3. **Return**:
    - The outer function returns the inner function, which is now "configured" to raise any number to the specified power.
4. **Example Usage**:
    - The function `power(2)` creates a function that squares numbers. This returned function can then be used for any base number `x` to compute `x**2`.

## Output 📜

Example usage and outputs:

```python
square = power(2)
print(square(5))  # Output: 25

cube = power(3)
print(cube(4))  # Output: 64
```

## Usage 📦

1. Save the code to a file named `power_function.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using Python:

    ```python
    from power_function import power

    square = power(2)
    print(square(5))  # 25

    cube = power(3)
    print(cube(4))  # 64
    ```

## Conclusion 🚀

This program illustrates the concept of higher-order functions and closures in Python.
The `power()` function dynamically creates functions that perform exponentiation, making it versatile for various power-related calculations.
