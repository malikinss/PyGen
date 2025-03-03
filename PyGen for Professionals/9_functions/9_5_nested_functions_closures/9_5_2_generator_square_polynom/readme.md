# Square Trinomial Function Generator

## Description 📝

This Python function defines a generator `generator_square_polynom(a, b, c)` that takes three real numbers (coefficients `a`, `b`, and `c`) and returns a function corresponding to the square trinomial \( f(x) = ax^2 + bx + c \).
The returned function can then be used to compute the value of this quadratic equation for any given input \( x \).

## Purpose 🎯

The purpose is to create a higher-order function (`generator_square_polynom`) that allows generating different quadratic functions (square trinomials) based on the coefficients provided.
This can be useful for mathematical modeling or solving specific quadratic equations.

## How It Works 🔍

1. **Function Definition (`generator_square_polynom`)**:
    - Takes three arguments: `a`, `b`, and `c`, which are the coefficients of the quadratic equation.
    - Ensures that all coefficients are either integers or floats, though this validation is optional for this case.
2. **Lambda Function**:

    - The function returns a lambda function that computes the value of \( ax^2 + bx + c \) for any input \( x \).

3. **Example Usage**:
    - Calling `generator_square_polynom(1, 2, 1)` will generate the quadratic function \( f(x) = x^2 + 2x + 1 \).
    - This function can then be called with any value of \( x \) to compute the result.

## Output 📜

Example usage and outputs:

```python
# Create a function corresponding to x^2 + 2x + 1
f = generator_square_polynom(1, 2, 1)
print(f(5))  # Output: 36 (5^2 + 5*2 + 1 = 36)

# Create a function corresponding to 2x^2 + 3x + 5
g = generator_square_polynom(2, 3, 5)
print(g(4))  # Output: 51 (2*4^2 + 3*4 + 5 = 51)
```

## Usage 📦

1. Save the code to a file named `square_trinomial.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using Python:

    ```python
    from square_trinomial import generator_square_polynom

    f = generator_square_polynom(1, 2, 1)
    print(f(5))  # 36

    g = generator_square_polynom(2, 3, 5)
    print(g(4))  # 51
    ```

## Conclusion 🚀

This function generator provides a flexible way to create any square trinomial function.
You can easily customize the coefficients \( a \), \( b \), and \( c \) to define different quadratic equations and use them dynamically in your programs.
