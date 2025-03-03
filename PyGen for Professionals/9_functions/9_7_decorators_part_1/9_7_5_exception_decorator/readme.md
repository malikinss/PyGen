# Exception Decorator

## Description 📝

This Python program implements an `exception_decorator`, which wraps a function to handle exceptions.
If the function completes successfully, it returns a tuple containing the return value of the function and a success message.
If an error occurs during the execution of the function, it returns a tuple containing `None` and an error message with the exception details.

## Purpose 🎯

The `exception_decorator` is useful for handling exceptions in a clean and standardized way without having to manually handle them within each function.
This decorator ensures that the calling code receives a status message and can easily differentiate between success and failure.

## How It Works 🔍

1. **Input**:

    - The `exception_decorator` is applied to a function. This function can take any number of positional and keyword arguments.

2. **Processing**:

    - The decorator defines a `wrapper` function that calls the decorated function with the provided arguments.
    - If the function completes without errors, the wrapper returns a tuple with the result and a success message.
    - If an exception occurs during the execution of the function, the wrapper catches the exception and returns a tuple with `None` and an error message.

3. **Output**:
    - The decorated function is wrapped with exception handling, and the calling code receives either the function's result or an error message.

## Example 📜

### Example Usage:

```python
# Decorate the function with `exception_decorator`
@exception_decorator
def divide(a: int, b: int) -> float:
    return a / b

# Call the decorated function with valid arguments
result = divide(10, 2)
print(result)  # Output: (5.0, 'The function completed without errors')

# Call the decorated function with invalid arguments (division by zero)
result = divide(10, 0)
print(result)  # Output: (None, 'An error occurred while calling the function: division by zero')
```

### Output:

```
(5.0, 'The function completed without errors')
(None, 'An error occurred while calling the function: division by zero')
```

In the example, the `divide` function is decorated with `exception_decorator`. When called with valid arguments, it returns a tuple containing the result and a success message. When called with invalid arguments (division by zero), it returns a tuple containing `None` and the error message.

## Usage 📦

1. Define the `exception_decorator` in your script.
2. Apply it to any function by using the `@exception_decorator` syntax before the function definition.
3. Call the decorated function, and the result will be returned as a tuple containing either the return value and success message or `None` and an error message.

## Conclusion 🚀

The `exception_decorator` simplifies exception handling by encapsulating it in a decorator.
It ensures that the function's return value and status message are always returned in a tuple, making error handling more consistent and readable.
