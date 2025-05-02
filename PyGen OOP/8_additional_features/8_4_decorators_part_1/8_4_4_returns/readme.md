# returns Decorator Class Implementation

## Description 📝

The provided code implements the `returns` decorator as a class that ensures the return value of a decorated function matches a specified `datatype`.
If the return value is not an instance of `datatype`, it raises a `TypeError`.
The decorator uses `functools.wraps` to preserve the decorated function's metadata, supports arbitrary positional and keyword arguments, and passes the return value unchanged when valid.

## Purpose 🎯

Intended for scenarios requiring return type validation, such as API development, type-safe programming, or educational examples of Python decorators, callable classes, type checking, and metadata preservation.

## How It Works 🔍

-   **Class Definition**:
    -   `returns` is a class that acts as a decorator by implementing `__init__` and `__call__`.
-   **Initialization (`__init__`)**:
    -   Takes `datatype` (a type, e.g., `int`, `str`).
    -   Stores `datatype` as `self.datatype`.
-   **Call Method (`__call__`)**:
    -   Takes `func` (the function to decorate).
    -   Returns a wrapped function using `@wraps(func)` to preserve metadata (e.g., `__name__`, `__doc__`).
    -   The wrapper function:
        -   Calls `func` with `*args` and `**kwargs`, storing the result.
        -   Checks if `result` is an instance of `self.datatype` using `isinstance`.
        -   Raises `TypeError` if the check fails (with no specific message, as none is specified).
        -   Returns `result` if valid.
-   **Behavior**:
    -   Enforces that the function’s return value matches `datatype`.
    -   Preserves function metadata and supports arbitrary arguments.
    -   No additional validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Decorator Class**:
    -   `returns` is a class that takes a `datatype` argument and acts as a decorator.
-   **Return Type Checking**:
    -   Ensures the return value is an instance of `datatype`.
    -   Raises `TypeError` for non-matching return types.
-   **Arbitrary Arguments**:
    -   Handles functions with any number of positional arguments: `f()`, `f(1, 2)`, etc.
    -   Handles keyword arguments: `f(x=1)`, `f(1, y=2)`.
-   **Return Value**:
    -   Returns the decorated function’s result when the type is valid.
-   **Metadata Preservation**:
    -   `@wraps` ensures `__name__`, `__doc__`, etc., are copied from the original function.
-   **Correctness**:
    -   Uses `isinstance` to check return type.
    -   Raises `TypeError` for invalid return types.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `isinstance(result, self.datatype)` accurately checks the return type.
    -   `TypeError` is raised without a custom message, as none is specified in the requirements.
    -   `@wraps` preserves function metadata, ensuring transparency.
-   **Performance**:
    -   Initialization: O(1) for storing `datatype`.
    -   `__call__`: O(1) for wrapping.
    -   Wrapper execution: O(1) for `isinstance` plus the cost of the decorated function.
    -   Highly efficient for all operations.
-   **Design**:
    -   Class-based decorator is explicit and aligns with requirements.
    -   `@wraps` ensures proper introspection (e.g., `func.__name__`).
    -   Type hints (`Type[Any]`, `Callable[..., Any]`, `Any`) clarify inputs and outputs.
    -   Simple implementation avoids complexity.
-   **Alternatives**:
    -   Function-based decorator: Possible but less aligned with class-based requirement.
    -   Manual metadata copying: Unnecessary, as `@wraps` handles it.
    -   Custom error message: Not required, as the task specifies only `TypeError`.
-   **Extensibility**:
    -   Easily extended to support multiple allowed types (e.g., tuple of types).
    -   Could add custom error messages or logging if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
@returns(int)
def add(a, b):
    return a + b

@returns(str)
def greet(name):
    return f"Hello, {name}"

# Test valid return types
print(add(1, 2))  # 3
print(greet("Alice"))  # Hello, Alice

# Test invalid return types
@returns(int)
def invalid():
    return "not an int"

try:
    invalid()
except TypeError:
    print("TypeError raised")  # TypeError raised

# Test with keyword arguments
@returns(float)
def divide(a, b=1):
    return a / b

print(divide(5, b=2))  # 2.5
try:
    @returns(int)
    def return_float():
        return 1.5
    return_float()
except TypeError:
    print("TypeError raised")  # TypeError raised

# Test metadata preservation
print(add.__name__)  # add
```

## Conclusion 🚀

The `returns` decorator class implementation is precise, correctly enforcing that the decorated function’s return value matches the specified `datatype` and raising `TypeError` for mismatches.
It supports arbitrary arguments, preserves metadata with `@wraps`, and passes valid return values unchanged.
The design is simple, efficient, and extensible, making it ideal for type-checking tasks or teaching decorator concepts, fully compliant with the task’s requirements.
