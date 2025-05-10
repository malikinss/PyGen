# predicate Decorator Implementation

## Description 📝

The provided code implements the `predicate` decorator class, which wraps functions returning boolean values (predicates) to enable logical combinations using `&` (AND), `|` (OR), and `~` (NOT) operators.
The decorator preserves the original function’s behavior for direct calls and supports predicates with any number of positional or keyword arguments.
Combined predicates apply the same arguments to both functions and compute the logical result.
The implementation uses a class-based decorator with operator overloading for clean syntax.

## Purpose 🎯

Intended for applications requiring flexible predicate logic, such as filtering, validation, or educational examples of Python decorators, operator overloading, and functional programming.

## How It Works 🔍

-   **Class Definition**:
    -   `predicate` is a decorator class that wraps a boolean-returning function.
    -   Uses `functools.wraps` and `update_wrapper` to preserve the wrapped function’s metadata.
    -   Imports `typing.Callable` for type hints.
-   **Initialization (`__init__`)**:
    -   Takes a function (`func`) that returns a boolean.
    -   Stores `func` as `self.func`.
    -   Calls `update_wrapper` to copy metadata (e.g., `__name__`, `__doc__`) from `func`.
-   ****call** Method**:
    -   Makes the decorator callable, allowing the wrapped function to be invoked directly.
    -   Passes all positional (`*args`) and keyword (`**kwargs`) arguments to `self.func`.
    -   Returns the boolean result of `self.func`.
-   ****and** Method**:
    -   Implements the `&` operator for logical AND.
    -   Takes another `predicate` instance (`other`).
    -   Creates a new predicate that applies both `self.func` and `other.func` to the same arguments and returns their logical AND.
    -   Uses `@predicate` and `@wraps` to decorate the combined function.
-   ****or** Method**:
    -   Implements the `|` operator for logical OR.
    -   Similar to `__and__`, but returns the logical OR of `self.func` and `other.func`.
-   ****invert** Method**:
    -   Implements the `~` operator for logical NOT.
    -   Creates a new predicate that negates the result of `self.func`.
    -   Uses `@predicate` and `@wraps` to decorate the negated function.
-   **Behavior**:
    -   Decorated predicates can be called directly, behaving like the original function.
    -   Combined predicates (`&`, `|`, `~`) create new predicates that apply logical operations.
    -   Supports any number of arguments (positional or keyword), as long as combined predicates have compatible signatures.
    -   Preserves function metadata for introspection.
    -   No validation needed, as signatures are guaranteed compatible.

## Verification ✅

Implementation satisfies requirements:

-   **Decorator Application**:
    -   Applies to predicates (functions returning `True` or `False`).
    -   Example: `@predicate def is_even(num): return num % 2 == 0` works correctly.
-   **Logical Operations**:
    -   AND (`&`): `(is_even & is_positive)(4)` → `True`, `(is_even & is_positive)(3)` → `False`.
    -   OR (`|`): `(is_even | is_positive)(3)` → `True`.
    -   NOT (`~`): `(~is_even & is_positive)(3)` → `True`.
    -   Example: `(to_be | ~to_be)()` → `True`.
-   **Argument Support**:
    -   Handles any number of arguments.
    -   Example: `@predicate def is_equal(a, b): return a == b` works for `(is_less_than | is_equal)(1, 2)` → `True`.
    -   Supports positional and keyword arguments.
    -   Example: `(is_less_than | is_equal)(2, b=2)` → `True`, `(is_less_than | is_equal)(a=3, b=2)` → `False`.
-   **Direct Access**:
    -   Decorated functions work independently.
    -   Example: `is_less_than(1, 2)` → `True`, `is_less_than(3, 2)` → `False`.
-   **Correctness**:
    -   Logical operations (`and`, `or`, `not`) are applied correctly to predicate results.
    -   Same arguments are passed to both predicates in combinations.
    -   Metadata is preserved via `wraps` and `update_wrapper`.
    -   No validation needed, as signatures are guaranteed compatible.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `__call__` passes all arguments to the wrapped function, preserving its behavior.
    -   `__and__` and `__or__` apply the same `*args` and `**kwargs` to both predicates, ensuring consistent evaluation.
    -   `__invert__` negates the result of `self.func` correctly.
    -   `update_wrapper` and `wraps` ensure combined predicates retain metadata.
    -   Class-based decorator allows operator overloading for `&`, `|`, `~`.
-   **Performance**:
    -   Initialization: O(1) for storing the function.
    -   `__call__`: O(1) plus the wrapped function’s complexity.
    -   `__and__`, `__or__`: O(1) for creating combined predicate, O(f + g) for evaluation (f, g are predicate complexities).
    -   `__invert__`: O(1) for creating negated predicate, O(f) for evaluation.
    -   Efficient for typical predicate use cases.
-   **Design**:
    -   Class-based decorator is ideal for operator overloading.
    -   Type hints (`Callable[..., bool]`, `'predicate'`) clarify signatures.
    -   `functools.wraps` ensures combined predicates are introspectable.
    -   Single class handles all logical operations cleanly.
-   **Alternatives**:
    -   Function-based decorator: Cannot easily support operator overloading.
    -   External combination functions: Less intuitive than `&`, `|`, `~`.
    -   No metadata preservation: Would break introspection but not required.
-   **Extensibility**:
    -   Easily extended to support additional operators (e.g., XOR).
    -   Could add validation for return type (bool) if needed.
-   **Edge Cases**:
    -   No arguments: Handled correctly (e.g., `to_be()`).
    -   Multiple arguments: Supported via `*args` and `**kwargs`.
    -   Keyword arguments: Passed correctly to predicates.
    -   Empty combination: Not applicable, as operations require predicates.
    -   Non-boolean predicates: Not an issue, as guaranteed to return bool.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Define predicates
@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_positive(num):
    return num > 0

# Test logical combinations
print((is_even & is_positive)(4))  # True (4 is even and positive)
print((is_even & is_positive)(3))  # False (3 is not even)
print((is_even | is_positive)(3))  # True (3 is positive)
print((~is_even & is_positive)(3))  # True (3 is not even and positive)

# Test no-argument predicate
@predicate
def to_be():
    return True

print((to_be | ~to_be)())  # True (True or False)

# Test multi-argument predicates
@predicate
def is_equal(a, b):
    return a == b

@predicate
def is_less_than(a, b):
    return a < b

print((is_less_than | is_equal)(1, 2))  # True (1 < 2)
print((is_less_than | is_equal)(2, 2))  # True (2 == 2)
print((is_less_than | is_equal)(3, 2))  # False (neither 3 < 2 nor 3 == 2)

# Test keyword arguments
print((is_less_than | is_equal)(2, b=2))  # True (2 == 2)
print((is_less_than | is_equal)(a=3, b=2))  # False (neither 3 < 2 nor 3 == 2)

# Test direct access
print(is_less_than(1, 2))  # True
print(is_less_than(2, 2))  # False
print(is_less_than(3, 2))  # False
```

## Conclusion 🚀

The `predicate` decorator implementation is precise, enabling logical combinations of predicates using `&`, `|`, and `~` operators while preserving direct function behavior.
It supports arbitrary argument counts, positional and keyword arguments, and maintains metadata for introspection.
The class-based design with operator overloading is elegant and efficient, making it ideal for predicate logic tasks or teaching advanced decorator techniques, fully compliant with the task’s requirements.
