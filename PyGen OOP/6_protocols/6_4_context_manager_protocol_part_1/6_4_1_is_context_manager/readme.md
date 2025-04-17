# is_context_manager Function Context Protocol Checker

## Description 📝

The `is_context_manager` function accepts an arbitrary object `obj` and returns `True` if it qualifies as a context manager, otherwise `False`.
A context manager is identified by the presence of both `__enter__` and `__exit__` methods, as required by Python’s context management protocol.

## Purpose 🎯

Designed for introspection tasks, such as validating objects before use in `with` statements, debugging, or framework development where context manager compatibility must be confirmed.
It’s useful in testing, dynamic type checking, or educational contexts exploring Python’s protocols.

## How It Works 🔍

-   **Input**: `obj`, any Python object.
-   **Operation**:
    -   Uses `hasattr(obj, '__enter__')` to check for the `__enter__` method.
    -   Uses `hasattr(obj, '__exit__')` to check for the `__exit__` method.
    -   Combines checks with `and`, returning `True` only if both methods exist.
-   **Output**: Boolean indicating whether `obj` is a context manager.
-   **Behavior**: Simple attribute lookup ensures fast, reliable detection.

## Verification ✅

Implementation meets requirements:

-   **Valid Context Managers**: Returns `True` for objects like file objects (`open('file.txt')`), `tempfile.TemporaryDirectory()`, or custom classes with `__enter__` and `__exit__`.
-   **Non-Context Managers**: Returns `False` for strings, integers, lists, or objects missing either method.
-   **Edge Cases**: Correctly handles `None`, built-in types, or partial implementations (e.g., only `__enter__`).

## Potential Considerations 🛠️

-   **Accuracy**: Checking `__enter__` and `__exit__` is sufficient, as Python’s `with` statement requires both. No need to verify method callability, per task simplicity.
-   **Performance**: `hasattr` is O(1), making the function highly efficient.
-   **Design**: Minimal and precise, avoiding overcomplication for arbitrary objects.

## Usage Example (For Clarity, Not Submission) 📦

```python
with open('test.txt', 'w') as f:
    print(is_context_manager(f))  # True
print(is_context_manager("text"))  # False
class Test:
    def __enter__(self): pass
    def __exit__(self, *args): pass
print(is_context_manager(Test()))  # True
```

## Conclusion 🚀

The `is_context_manager` function is correct and efficient, accurately identifying context managers via `__enter__` and `__exit__` checks.
It’s ready for introspection or validation tasks, fully compliant with the specification.
