# type_check Decorator Class Implementation

## Description 📝

The provided code implements the `type_check` decorator as a class that ensures the types of positional arguments passed to a decorated function match the types specified in a provided list.
It checks that the type of each positional argument corresponds to the respective type in the `types` list, raising a `TypeError` if any mismatch occurs.
The decorator handles cases where the number of arguments is less than or greater than the number of types, uses `functools.wraps` to preserve metadata, supports arbitrary positional and keyword arguments, and passes the function’s return value unchanged.

## Purpose 🎯

Intended for scenarios requiring strict type checking of positional arguments, such as API validation, type-safe programming, or educational examples of Python decorators, callable classes, type checking, and metadata preservation.

## How It Works 🔍

-   **Class Definition**:
    -   `type_check` is a class that acts as a decorator by implementing `__init__` and `__call__`.
-   **Initialization (`__init__`)**:
    -   Takes `types` (a list of data types, e.g., `[int, str]`).
    -   Stores `types` as a tuple in `self.types` for immutability and efficiency.
-   **Call Method (`__call__`)**:
    -   Takes `func` (the function to decorate).
    -   Returns a wrapped function using `@wraps(func)` to preserve metadata (e.g., `__name__`, `__doc__`).
    -   The wrapper function:
        -   Uses `zip(args, self.types)` to pair each positional argument with its expected type.
        -   Checks each pair using `isinstance(arg, expected_type)`.
        -   Raises `TypeError` if any argument’s type does not match (no specific message required).
        -   Calls `func` with the original `*args` and `**kwargs`, returning its result.
-   **Behavior**:
    -   Checks types of positional arguments against `self.types` in order.
    -   Ignores excess arguments (if `len(args) > len(types)`).
    -   Ignores excess types (if `len(args) < len(types)`).
    -   Preserves function metadata and supports arbitrary arguments.
    -   Keyword arguments are not checked, as only positional arguments are specified.
    -   No additional validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Decorator Class**:
    -   `type_check` is a class that takes a list of types as an argument.
-   **Type Checking**:
    -   Ensures the type of the `i`-th positional argument matches the `i`-th type in `types`.
    -   Raises `TypeError` for any mismatch.
    -   Ignores excess arguments or types as specified.
-   **Arbitrary Arguments**:
    -   Handles functions with any number of positional arguments: `f()`, `f(1, "a")`, etc.
    -   Handles keyword arguments without checking: `f(x=1)`, `f(1, y=2)`.
-   **Return Value**:
    -   Returns the decorated function’s result when types match.
-   **Metadata Preservation**:
    -   `@wraps` ensures `__name__`, `__doc__`, etc., are copied from the original function.
-   **Correctness**:
    -   Uses `zip` to correctly pair arguments and types.
    -   `isinstance` ensures accurate type checking.
    -   Handles partial matches (fewer args or types) correctly.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `zip(args, self.types)` automatically handles cases where `args` or `types` have different lengths.
    -   `isinstance(arg, expected_type)` accurately checks types.
    -   `TypeError` is raised without a custom message, as none is specified.
    -   `@wraps` preserves function metadata, ensuring transparency.
-   **Performance**:
    -   Initialization: O(n) for converting `types` to a tuple (n is length of `types`).
    -   `__call__`: O(1) for wrapping.
    -   Wrapper execution: O(min(m, n)) for checking types (m is number of args, n is number of types), plus the cost of the decorated function.
    -   Efficient for typical argument counts.
-   **Design**:
    -   Class-based decorator is explicit and aligns with requirements.
    -   `@wraps` ensures proper introspection (e.g., `func.__name__`).
    -   Type hints (`List[Type[Any]]`, `Callable[..., Any]`, `Any`) clarify inputs and outputs.
    -   Storing `types` as a tuple ensures immutability.
-   **Alternatives**:
    -   Function-based decorator: Possible but less aligned with class-based requirement.
    -   Manual metadata copying: Unnecessary, as `@wraps` handles it.
    -   Explicit loop with indices: Less concise than `zip`.
-   **Extensibility**:
    -   Easily extended to check keyword arguments or allow multiple types per position.
    -   Could add custom error messages or logging if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
@type_check([int, str])
def format_pair(number, text):
    return f"{number}: {text}"

# Test valid types
print(format_pair(42, "hello"))  # 42: hello

# Test invalid types
try:
    format_pair("42", "hello")
except TypeError:
    print("TypeError raised")  # TypeError raised

# Test fewer arguments
@type_check([int, str, float])
def add(a, b):
    return a + len(b)

print(add(1, "abc"))  # 4 (float type ignored)

# Test more arguments
@type_check([int])
def sum_args(a, b):
    return a + b

print(sum_args(1, 2))  # 3 (second arg not checked)

# Test with keyword arguments
@type_check([int, str])
def process(a, b, c=0):
    return a + len(b) + c

print(process(1, "abc", c=5))  # 9 (keyword arg not checked)

# Test metadata preservation
print(format_pair.__name__)  # format_pair
```

## Conclusion 🚀

The `type_check` decorator class implementation is precise, correctly enforcing that positional argument types match the specified list and raising `TypeError` for mismatches.
It handles cases with fewer or more arguments, supports arbitrary arguments, preserves metadata with `@wraps`, and passes return values unchanged.
The design is simple, efficient, and extensible, making it ideal for type-checking tasks or teaching decorator concepts, fully compliant with the task’s requirements.
