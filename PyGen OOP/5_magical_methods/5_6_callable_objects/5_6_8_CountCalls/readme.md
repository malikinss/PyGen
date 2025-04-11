# CountCalls Decorator Call Counter

## Description 📝

The `CountCalls` class is a Python decorator that wraps a function to count how many times it is invoked.
The call count is stored in an accessible `calls` attribute on the decorator instance.
It is designed to be non-intrusive, preserving the original function’s return value and supporting any number of positional and keyword arguments, making it versatile for a wide range of use cases.

## Purpose 🎯

This decorator serves as a utility for tracking function call frequency, making it ideal for debugging, performance monitoring, logging function usage in applications, or teaching the concept of decorators in Python.
Its simplicity and flexibility make it a valuable tool in both development and educational contexts.

## How It Works 🔍

-   **Class Structure**: Implemented as a class to maintain state (the call count) across invocations.
-   **Initialization**: The `__init__` method takes the function to decorate, storing it in `self.func` and setting `self.calls` to 0 to track invocations.
-   **Call Execution**: The `__call__` method makes the instance callable, incrementing `self.calls` each time the function is invoked, then passing all arguments (`*args` and `**kwargs`) to the original function and returning its result unchanged.
-   **Argument Handling**: Uses `*args` and `**kwargs` to ensure compatibility with any function signature, from no arguments to complex combinations of positional and named parameters.

## Usage 📦

1. **Save the Code**: Place the `CountCalls` class in a Python file, e.g., `count_calls.py`.
2. **Apply the Decorator**: Use the `@CountCalls` syntax above any function definition to enable call counting.
3. **Access the Count**: After calling the function, access the `.calls` attribute on the function object to retrieve the number of invocations.
4. **Example**:

    ```python
    @CountCalls
    def multiply(x, y):
        return x * y

    result = multiply(2, 3)  # First call
    multiply(4, 5)          # Second call
    print(multiply.calls)   # Outputs: 2
    print(result)           # Outputs: 6
    ```

## Conclusion 🚀

The `CountCalls` decorator offers a straightforward, efficient, and reusable solution for monitoring function calls in Python.
Its class-based approach ensures state persistence, while its flexible argument handling guarantees compatibility with diverse function signatures.
This makes it an excellent choice for developers looking to add lightweight instrumentation to their code or for educators demonstrating decorator mechanics.
Potential extensions could include resetting the counter or logging call details, but its current form meets the core need with elegance and simplicity.
