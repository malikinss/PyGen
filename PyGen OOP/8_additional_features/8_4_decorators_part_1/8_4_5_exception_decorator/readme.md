# exception_decorator Class Implementation

## Description 📝

The provided code implements the `exception_decorator` as a class that wraps a function to capture its execution outcome.
It returns a tuple: `(value, None)` if the function executes without raising an exception, where `value` is the function’s return value, or `(None, errortype)` if an exception occurs, where `errortype` is the type of the raised exception.
The decorator uses `functools.update_wrapper` to preserve the decorated function's metadata and supports arbitrary positional and keyword arguments.

## Purpose 🎯

Intended for scenarios requiring exception handling and result reporting, such as logging, debugging, or educational examples of Python decorators, callable classes, exception handling, and metadata preservation.

## How It Works 🔍

-   **Class Definition**:
    -   `exception_decorator` is a class that acts as a decorator by implementing `__init__` and `__call__`.
-   **Initialization (`__init__`)**:
    -   Takes `func` (the function to decorate).
    -   Uses `update_wrapper(self, func)` to copy metadata (e.g., `__name__`, `__doc__`) from `func` to the decorator instance.
    -   Stores `func` as `self.func`.
-   **Call Method (`__call__`)**:
    -   Takes `*args` (positional arguments) and `**kwargs` (keyword arguments).
    -   Uses a `try-except` block:
        -   In the `try` block, calls `self.func(*args, **kwargs)` and returns `(result, None)`.
        -   In the `except` block, catches any `Exception` as `e` and returns `(None, type(e))`.
-   **Behavior**:
    -   Captures the function’s return value or exception type in a tuple.
    -   Preserves function metadata and supports arbitrary arguments.
    -   Handles any exception type derived from `Exception`.
    -   No validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Decorator Class**:
    -   `exception_decorator` is a class that acts as a decorator.
-   **Return Format**:
    -   Returns `(value, None)` for successful execution, where `value` is the function’s return value.
    -   Returns `(None, errortype)` for exceptions, where `errortype` is the exception’s type (e.g., `ValueError`).
-   **Arbitrary Arguments**:
    -   Handles functions with any number of positional arguments: `f()`, `f(1, 2)`, etc.
    -   Handles keyword arguments: `f(x=1)`, `f(1, y=2)`.
-   **Return Value**:
    -   Preserves the function’s return value in the success tuple.
-   **Metadata Preservation**:
    -   `update_wrapper` ensures `__name__`, `__doc__`, etc., are copied from the original function.
-   **Correctness**:
    -   Correctly handles successful executions and exceptions.
    -   Returns the exact type of the raised exception.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `try-except` captures any `Exception` subclass, covering all standard exceptions (e.g., `ValueError`, `TypeError`).
    -   `type(e)` returns the exception’s class, as required.
    -   `update_wrapper` preserves function metadata, ensuring transparency.
-   **Performance**:
    -   Initialization: O(1) for storing `func`.
    -   `__call__`: O(1) for try-except overhead plus the cost of the decorated function.
    -   Highly efficient for all operations.
-   **Design**:
    -   Class-based decorator is explicit and aligns with requirements.
    -   `update_wrapper` ensures proper introspection (e.g., `func.__name__`).
    -   Type hints (`Callable[..., Any]`, `Tuple[Any, Union[Type[Exception], None]]`) clarify inputs and outputs.
    -   Simple implementation avoids complexity.
-   **Alternatives**:
    -   Function-based decorator: Possible but less aligned with class-based requirement.
    -   Manual metadata copying: Unnecessary, as `update_wrapper` handles it.
    -   Catching specific exceptions: Overly restrictive, as any `Exception` should be caught.
-   **Extensibility**:
    -   Easily extended to log exceptions or capture additional exception details (e.g., message).
    -   Could add validation or specific exception filtering if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
@exception_decorator
def divide(a, b):
    return a / b

@exception_decorator
def greet(name):
    return f"Hello, {name}"

# Test successful execution
print(divide(10, 2))  # (5.0, None)
print(greet("Alice")) # ('Hello, Alice', None)

# Test exception
print(divide(10, 0))  # (None, <class 'ZeroDivisionError'>)

# Test with keyword arguments
@exception_decorator
def add(a, b=0):
    if a < 0:
        raise ValueError("Negative number")
    return a + b

print(add(5, b=3))  # (8, None)
print(add(-1))      # (None, <class 'ValueError'>)

# Test metadata preservation
print(divide.__name__)  # divide
```

## Conclusion 🚀

The `exception_decorator` class implementation is precise, correctly returning `(value, None)` for successful executions and `(None, errortype)` for exceptions.
It supports arbitrary arguments, preserves metadata with `update_wrapper`, and handles return values and exceptions as specified.
The design is simple, efficient, and extensible, making it ideal for exception handling tasks or teaching decorator concepts, fully compliant with the task’s requirements.
