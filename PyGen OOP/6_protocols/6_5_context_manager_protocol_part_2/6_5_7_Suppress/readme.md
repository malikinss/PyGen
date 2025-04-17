# Suppress Class Selective Exception Silencer

## Description 📝

The `Suppress` class is a context manager that accepts an arbitrary number of exception types as positional arguments during instantiation.
It suppresses exceptions of the specified types raised within a `with` block, storing the suppressed exception in its `exception` attribute (set to `None` if no exception is suppressed or no exception occurs).
The class implements the context manager protocol with `__enter__` and `__exit__` methods.

## Purpose 🎯

Designed for scenarios requiring targeted exception handling, such as ignoring specific errors in data processing, testing, or user input validation, while preserving others.
The `exception` attribute enables post-block inspection of suppressed errors, making it useful for logging or debugging.
It also serves as an educational tool for Python’s context manager protocol and exception handling.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `*args`, a variable number of exception types (subclasses of `BaseException`).
    -   Stores the types in `self._exceptions` as a tuple.
    -   Initializes `self.exception` as `None` to track any suppressed exception.
-   **Enter Method (`__enter__`)**:
    -   Returns `self`, allowing access to the `exception` attribute within the `with` block.
-   **Exit Method (`__exit__`)**:
    -   Accepts `exc_type` (exception type), `exc_value` (exception instance), and `traceback` (traceback object), all possibly `None`.
    -   If `exc_type` is not `None` (an exception occurred):
    -   Checks if `exc_type` is a subclass of any type in `self._exceptions` using `issubclass`.
    -   If a match is found, sets `self.exception = exc_value` and returns `True` to suppress the exception.
    -   Returns `False` if no exception occurred or the exception type doesn’t match, allowing propagation.
-   **Behavior**:
    -   Suppresses only specified exception types, storing the instance in `exception`.
    -   Non-matching exceptions propagate normally.
    -   `exception` remains `None` if no exception is raised or suppressed.

## Verification ✅

Implementation meets requirements:

-   **Suppression**: `with Suppress(ValueError): raise ValueError("error")` suppresses the exception, sets `s.exception` to the `ValueError` instance.
-   **Non-Suppressed**: `with Suppress(ValueError): raise TypeError` propagates `TypeError`, `s.exception` remains `None`.
-   **No Exception**: `with Suppress(ValueError): pass` leaves `s.exception` as `None`.
-   **Multiple Types**: `Suppress(ValueError, TypeError)` suppresses both types.
-   **Protocol**: `__enter__` and `__exit__` enable `with` statement usage.

## Potential Considerations 🛠️

-   **Correctness**: `issubclass` ensures proper type checking, including subclasses (e.g., `ZeroDivisionError` for `ArithmeticError`).
-   **Performance**: O(n) for checking `n` exception types, negligible for typical use.
-   **Design**: Storing `exc_value` in `exception` allows inspection, and `None` default handles all non-suppressed cases cleanly.

## Usage Example (For Clarity, Not Submission) 📦

```python
with Suppress(ValueError) as s:
    raise ValueError("test")  # Suppressed
print(s.exception)  # ValueError: test

with Suppress(TypeError) as s:
    print("No error")  # No error
print(s.exception)  # None
```

## Conclusion 🚀

The `Suppress` implementation is accurate and efficient, suppressing specified exceptions while tracking them in the `exception` attribute.
It’s suitable for selective error handling or protocol education, fully compliant with the task’s requirements.
