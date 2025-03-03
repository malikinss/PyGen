# Polynomial Function

## Description 📝

This Python script defines a function `polynom(x)`, which calculates the value of the polynomial expression \( x^2 + 1 \).
Additionally, the function maintains a `values` attribute, which stores all previously computed results in a set.

## Purpose 🎯

The purpose of this program is to demonstrate:

-   Function attributes in Python (`polynom.values`).
-   Dynamic storage of computed values for tracking function outputs.
-   Basic mathematical operations involving polynomials.

## How It Works 🔍

1. **Function Definition**: The function `polynom(x)` is defined to compute the polynomial expression \( x^2 + 1 \).
2. **Attribute Initialization**: The `values` attribute is initialized as a set if it doesn’t already exist. This is done using `setdefault()`.
3. **Computation**: The function calculates the polynomial value.
4. **Storage**: The computed value is added to `polynom.values`.
5. **Return Value**: The computed result is returned.

## Output 📜

Example usage and outputs:

```python
print(polynom(2))
# Output: 5

print(polynom(3))
# Output: 10

print(polynom.values)
# Output: {5, 10}
```

## Usage 📦

1. Save the code to a file named `polynom_function.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using Python:

    ```python
    from polynom_function import polynom

    print(polynom(4))
    print(polynom(5))
    print(polynom.values)
    ```

## Conclusion 🚀

This program provides an example of function attributes and dynamic value storage in Python.
It demonstrates an elegant way to keep track of computed values without using global variables.
