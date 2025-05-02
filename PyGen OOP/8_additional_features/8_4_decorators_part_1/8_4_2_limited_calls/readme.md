# limited_calls Decorator Class Implementation

## Description 📝

The provided code implements the `limited_calls` decorator as a class that restricts a decorated function to a maximum of `n` calls.
It uses `functools.wraps` to preserve the decorated function's metadata and raises a `MaxCallsException` with the specified message if the call limit is exceeded.
The decorator supports functions with any number of positional and keyword arguments and passes the function’s return value unchanged.

## Purpose 🎯

Intended for scenarios requiring call restrictions, such as rate limiting, resource management, or educational examples of Python decorators, callable classes, exception handling, and metadata preservation.

## How It Works 🔍

-   **MaxCallsException**:
    -   A custom exception class inheriting from `Exception`.
    -   Used to signal when the call limit is exceeded with the message: "The allowed number of calls has been exceeded".
-   **limited_calls Class**:
    -   **Initialization (`__init__`)**:
        -   Takes `n` (an integer) as the maximum number of allowed calls.
        -   Stores `n` as `self.limit` and initializes `self.count` to 0 to track calls.
    -   **Call Method (`__call__`)**:
        -   Takes `func` (the function to decorate).
        -   Returns a wrapped function using `@wraps(func)` to preserve metadata (e.g., `__name__`, `__doc__`).
        -   The wrapper function:
            -   Checks if `self.count >= self.limit`.
            -   If true, raises `MaxCallsException` with the specified message.
            -   Increments `self.count`.
            -   Calls `func` with `*args` and `**kwargs`, returning its result.
-   **Behavior**:
    -   Limits the decorated function to `n` calls.
    -   Tracks calls with an instance-specific counter (`self.count`).
    -   Preserves function metadata and supports arbitrary arguments.
    -   No validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Decorator Class**:
    -   `limited_calls` is a class that takes an integer `n` and acts as a decorator.
-   **Call Limitation**:
    -   Allows exactly `n` calls to the decorated function.
    -   Raises `MaxCallsException` with "The allowed number of calls has been exceeded" on the (n+1)th call.
-   **Arbitrary Arguments**:
    -   Handles functions with any number of positional arguments: `f()`, `f(1, 2)`, etc.
    -   Handles keyword arguments: `f(x=1)`, `f(1, y=2)`.
-   **Return Value**:
    -   Returns the decorated function’s result without modification.
-   **Metadata Preservation**:
    -   `@wraps` ensures `__name__`, `__doc__`, etc., are copied from the original function.
-   **Correctness**:
    -   Tracks calls correctly with `self.count`.
    -   Raises exception at the correct threshold.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `self.count` accurately tracks calls per decorator instance.
    -   `MaxCallsException` is raised with the exact message required.
    -   `@wraps` preserves function metadata, ensuring transparency.
-   **Performance**:
    -   Initialization: O(1) for storing `n`.
    -   `__call__`: O(1) for wrapping and counter increment.
    -   Wrapper execution: O(1) plus the cost of the decorated function.
    -   Highly efficient for all operations.
-   **Design**:
    -   Class-based decorator allows state (`self.count`) to persist across calls.
    -   `@wraps` ensures proper introspection (e.g., `func.__name__`).
    -   Type hints (`int`, `Callable[..., Any]`, `Any`) clarify inputs and outputs.
    -   Custom `MaxCallsException` provides clear error signaling.
-   **Alternatives**:
    -   Function-based decorator: Possible but less intuitive for state management.
    -   Manual metadata copying: Unnecessary, as `@wraps` handles it.
    -   Global counter: Incorrect, as it wouldn’t be instance-specific.
-   **Extensibility**:
    -   Easily extended to reset the counter, adjust limits, or log calls.
    -   Could add validation (e.g., `n >= 0`) if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Test with a simple function
@limited_calls(2)
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Test successful calls
print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", greeting="Hi"))  # Hi, Bob!

# Test exceeding limit
try:
    greet("Charlie")
except MaxCallsException as e:
    print(e)  # The allowed number of calls has been exceeded

# Test metadata preservation
print(greet.__name__)  # greet

# Test with different argument counts
@limited_calls(1)
def add(*args):
    return sum(args)

print(add(1, 2, 3))  # 6
try:
    add(4)
except MaxCallsException as e:
    print(e)  # The allowed number of calls has been exceeded
```

## Conclusion 🚀

The `limited_calls` decorator class implementation is precise, correctly limiting function calls to `n` and raising `MaxCallsException` when exceeded.
It supports arbitrary arguments, preserves metadata with `@wraps`, and passes return values unchanged.
The design is simple, efficient, and extensible, making it ideal for call restriction tasks or teaching decorator concepts, fully compliant with the task’s requirements.
