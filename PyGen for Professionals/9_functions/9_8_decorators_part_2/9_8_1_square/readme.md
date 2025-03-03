# Square Decorator

## Description 📝

This Python program implements a `square` decorator that raises the return value of the decorated function to the power of two.
The decorator preserves the name and docstring of the original function using `functools.wraps`.

## Purpose 🎯

The `square` decorator is used to modify the return value of a function by squaring it.
This is useful when you want to ensure that the result of a function is always squared without modifying the function's code directly.

## How It Works 🔍

1. **Input**:

    - The `square` decorator is applied to a function. This function can take any number of positional and keyword arguments.

2. **Processing**:

    - The decorator wraps the original function using the `wraps` function to preserve the original function's name and docstring.
    - The decorated function is called, and its return value is squared before returning the result.

3. **Output**:
    - The return value of the original function is squared and returned.

## Example 📜

```python
# Example function that returns a number
@square
def add_two_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

# Call the decorated function
print(add_two_numbers(3, 4))  # Output: 49 (7 squared)
```

### Output:

```
49
add_two_numbers
Adds two numbers.
```

## Usage 📦

1. Define the `square` decorator in your script.
2. Apply it to any function by using the `@square` syntax before the function definition.
3. Call the decorated function, and the result will be the square of the original return value.

## Conclusion 🚀

The `square` decorator is a simple and effective way to modify the return value of a function by squaring it.
By using `functools.wraps`, the decorator ensures that the original function’s name and docstring are preserved, making it more transparent and maintainable.
