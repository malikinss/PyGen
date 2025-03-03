# Returns String Decorator

## Description 📝

This Python program implements a `returns_string` decorator that ensures the return value of the decorated function is of type `str`.
If the return value is not a string, the decorator raises a `TypeError` exception.
The decorator also preserves the original function's name and docstring.

## Purpose 🎯

The `returns_string` decorator is used to enforce that a function always returns a string.
This helps in ensuring type consistency and can be particularly useful when working with functions where the return type is critical for further processing.

## How It Works 🔍

1. **Input**:

    - The `returns_string` decorator is applied to a function. The function can accept any number of positional and keyword arguments.

2. **Processing**:

    - The decorator wraps the original function using the `wraps` function to preserve the function's name and docstring.
    - After the original function executes, the decorator checks if the return value is of type `str`. If not, it raises a `TypeError`.

3. **Output**:
    - If the function returns a string, the return value is passed as-is.
    - If the function does not return a string, a `TypeError` is raised.

## Example 📜

```python
# Example function that returns a string
@returns_string
def greet(name: str) -> str:
    """Greets a person by name."""
    return f"Hello, {name}!"

# Call the decorated function
print(greet("Alice"))  # Output: "Hello, Alice!"

# Example of a function that does not return a string
@returns_string
def add_numbers(a: int, b: int) -> str:
    """Adds two numbers and returns the result as a string."""
    return a + b  # This will raise a TypeError
```

### Output:

```
Hello, Alice!
TypeError: Expected return type 'str', got 'int'.
```

## Usage 📦

1. Define the `returns_string` decorator in your script.
2. Apply it to any function by using the `@returns_string` syntax before the function definition.
3. Call the decorated function, and if the return value is not a string, a `TypeError` will be raised.

## Conclusion 🚀

The `returns_string` decorator ensures that the return value of the decorated function is always of type `str`.
This helps in maintaining type consistency across functions and can be useful in scenarios where string outputs are required.
The decorator also preserves the function's metadata using `functools.wraps`, keeping the function name and docstring intact.
