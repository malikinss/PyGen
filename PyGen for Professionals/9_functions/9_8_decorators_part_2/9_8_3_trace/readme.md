# Trace Decorator

## Description 📝

This Python program implements a `trace` decorator that prints debugging information during the execution of the decorated function.
Specifically, it prints the function's name, the arguments passed to it (both positional and named), and the return value.
The decorator preserves the name and docstring of the decorated function.

## Purpose 🎯

The `trace` decorator is useful for debugging purposes.
It allows you to see when a function is called, what arguments were passed, and what value is returned, helping you track the flow of execution and identify issues.

## How It Works 🔍

1. **Input**:

    - The `trace` decorator is applied to a function. The decorated function can accept any number of positional and keyword arguments.

2. **Processing**:

    - When the decorated function is called, the decorator prints the following debugging information:
        - The function's name
        - The tuple of positional arguments
        - The dictionary of keyword arguments
    - After the function executes, the return value is printed in a similar format.

3. **Output**:
    - The function’s return value is returned as usual.
    - Debugging information is printed to the console.

## Example 📜

```python
# Define a simple function
@trace
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

# Call the decorated function
add(5, 3)
```

### Output:

```
TRACE: call add() with arguments: (5, 3), {}
TRACE: return value add(): 8
```

## Usage 📦

1. Define the `trace` decorator in your script.
2. Apply it to any function by using the `@trace` syntax before the function definition.
3. Call the decorated function. It will print the trace information to the console.

## Conclusion 🚀

The `trace` decorator is a powerful tool for debugging Python functions.
It prints detailed information about function calls, including the function name, arguments, and return values, helping to understand and troubleshoot the program flow.
The decorator preserves the function's metadata using `functools.wraps`, keeping the function name and docstring intact.
