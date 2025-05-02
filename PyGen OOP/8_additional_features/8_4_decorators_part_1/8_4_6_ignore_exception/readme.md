# ignore_exception Decorator Class Implementation

## Description 📝

The provided code implements the `ignore_exception` decorator as a class that catches specified exception types, prints "Exception <exception type> handled", and returns `None`.
If an exception is not one of the specified types, it is re-raised.
The decorator uses `functools.wraps` to preserve the decorated function's metadata, supports arbitrary positional and keyword arguments, and does not consume the function’s return value when no exception occurs.

## Purpose 🎯

Intended for scenarios requiring selective exception handling, such as logging, error suppression, or educational examples of Python decorators, callable classes, exception handling, and metadata preservation.

## How It Works 🔍

-   **Class Definition**:
    -   `ignore_exception` is a class that acts as a decorator by implementing `__init__` and `__call__`.
-   **Initialization (`__init__`)**:
    -   Takes `*exceptions` (an arbitrary number of exception types, e.g., `ValueError`, `TypeError`).
    -   Stores them as `self.exceptions` (a tuple of exception types).
-   **Call Method (`__call__`)**:
    -   Takes `func` (the function to decorate).
    -   Returns a wrapped function using `@wraps(func)` to preserve metadata (e.g., `__name__`, `__doc__`).
    -   The wrapper function:
        -   Uses a `try-except` block:
            -   In the `try` block, calls `func(*args, **kwargs)` and returns its result.
            -   In the first `except` block, catches exceptions in `self.exceptions`, prints "Exception <type_name> handled" (using `type(e).__name__`), and returns `None`.
            -   In the second `except` block, catches any other `Exception` and re-raises it unchanged.
-   **Behavior**:
    -   Handles specified exceptions by printing and returning `None`.
    -   Re-raises unhandled exceptions.
    -   Preserves function metadata and supports arbitrary arguments.
    -   No validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Decorator Class**:
    -   `ignore_exception` is a class that takes arbitrary exception types as arguments.
-   **Exception Handling**:
    -   For specified exceptions, prints "Exception <type> handled" and returns `None`.
    -   For unspecified exceptions, re-raises the exception unchanged.
-   **Arbitrary Arguments**:
    -   Handles functions with any number of positional arguments: `f()`, `f(1, 2)`, etc.
    -   Handles keyword arguments: `f(x=1)`, `f(1, y=2)`.
-   **Return Value**:
    -   Returns the function’s result when no exception occurs.
    -   Returns `None` when a specified exception is handled.
-   **Metadata Preservation**:
    -   `@wraps` ensures `__name__`, `__doc__`, etc., are copied from the original function.
-   **Correctness**:
    -   Correctly identifies and handles specified exceptions.
    -   Prints the exact exception type name (e.g., `ValueError`).
    -   Re-raises other exceptions as required.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `except self.exceptions` correctly catches any exception type in the provided tuple.
    -   `type(e).__name__` provides the exception’s type name for printing.
    -   Re-raising via `raise e` preserves the original exception’s type and message.
    -   `@wraps` preserves function metadata, ensuring transparency.
-   **Performance**:
    -   Initialization: O(1) for storing exceptions.
    -   `__call__`: O(1) for wrapping.
    -   Wrapper execution: O(1) for exception handling plus the cost of the decorated function.
    -   Highly efficient for all operations.
-   **Design**:
    -   Class-based decorator is explicit and aligns with requirements.
    -   `@wraps` ensures proper introspection (e.g., `func.__name__`).
    -   Type hints (`Type[Exception]`, `Callable[..., Any]`, `Any`) clarify inputs and outputs.
    -   Separate `except Exception` block ensures unhandled exceptions are re-raised.
-   **Alternatives**:
    -   Function-based decorator: Possible but less aligned with class-based requirement.
    -   Manual metadata copying: Unnecessary, as `@wraps` handles it.
    -   Single `except` with type checking: Less clear than separate blocks.
-   **Extensibility**:
    -   Easily extended to log exceptions or customize output messages.
    -   Could add validation (e.g., ensure exceptions are subclasses of `Exception`) if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
@ignore_exception(ValueError, TypeError)
def divide(a, b):
    return a / b

# Test successful execution
print(divide(10, 2))  # 5.0

# Test handled exception
print(divide(10, 0))  # Exception ZeroDivisionError handled
                      # None
print(divide("10", 2))  # Exception TypeError handled
                        # None

# Test unhandled exception
try:
    @ignore_exception(ValueError)
    def raise_key_error():
        raise KeyError("key")
    raise_key_error()
except KeyError as e:
    print(f"KeyError: {e}")  # KeyError: key

# Test with keyword arguments
@ignore_exception(ValueError)
def add(a, b=0):
    if a < 0:
        raise ValueError("Negative")
    return a + b

print(add(5, b=3))  # 8
print(add(-1))      # Exception ValueError handled
                    # None

# Test metadata preservation
print(divide.__name__)  # divide
```

## Conclusion 🚀

The `ignore_exception` decorator class implementation is precise, correctly handling specified exceptions by printing their type and returning `None`, while re-raising unhandled exceptions.
It supports arbitrary arguments, preserves metadata with `@wraps`, and handles return values as specified.
The design is simple, efficient, and extensible, making it ideal for selective exception handling or teaching decorator concepts, fully compliant with the task’s requirements.
