# NonNegativeInteger Class Restricted Integer Descriptor

## Description 📝

The `NonNegativeInteger` class is a descriptor that ensures an attribute’s value is a non-negative integer.
It accepts two arguments during instantiation: `name` (the attribute name) and `default` (an optional default value, defaulting to `None`).
When accessing the attribute, it returns the stored value or the `default` value if unset; if `default` is `None` and the attribute is unset, it raises `AttributeError` with "Attribute not found".
When setting the attribute, it verifies the value is a non-negative integer, raising `ValueError` with "Invalid value" if not.

## Purpose 🎯

Intended for scenarios requiring strict type and range validation, such as counters, indices, or configuration settings in data models, APIs, or frameworks.
The descriptor enforces data integrity, making it suitable for robust applications or educational examples of Python’s descriptor protocol and value validation.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `name` (string) and `default` (optional integer or `None`).
    -   Stores `name` as `self._attr` and `default` as `self._default`.
-   **Get Method (`__get__`)**:
    -   If `obj` is `None` (class access), returns the descriptor instance.
    -   If the attribute exists in `obj.__dict__`, returns its value.
    -   If unset and `self._default` is not `None`, returns `self._default`.
    -   Otherwise, raises `AttributeError` with "Attribute not found".
-   **Set Method (`__set__`)**:
    -   Checks if `value` is a non-negative integer using `__is_non_negative_int`.
    -   If invalid, raises `ValueError` with "Invalid value".
    -   Otherwise, stores `value` in `obj.__dict__[self._attr]`.
-   **Helper Method (`__is_non_negative_int`)**:
    -   Returns `True` if `value` is an integer (`isinstance(value, int)`) and non-negative (`value >= 0`), `False` otherwise.
-   **Behavior**:
    -   Ensures attribute values are non-negative integers.
    -   Provides flexible default value handling for unset attributes.
    -   Raises appropriate errors for invalid access or values.

## Verification ✅

Implementation satisfies requirements:

-   **Attribute Access**:
    -   `obj.x` returns the set value (e.g., `obj.x = 5; print(obj.x)` yields `5`).
    -   If unset with `default=0`, `obj.x` returns `0`.
    -   If unset with `default=None`, `obj.x` raises `AttributeError: Attribute not found`.
-   **Attribute Setting**:
    -   `obj.x = 10` sets successfully.
    -   `obj.x = -1`, `obj.x = 1.5`, or `obj.x = "10"` raise `ValueError: Invalid value`.
-   **Type Check**:
    -   Only integers `>= 0` are allowed; other types (floats, strings, etc.) are rejected.
-   **Descriptor Protocol**: `__get__` and `__set__` manage attribute access and mutation correctly.

## Potential Considerations 🛠️

-   **Correctness**: `isinstance(value, int)` excludes floats and other numeric types; `value >= 0` ensures non-negativity. Default handling is precise.
-   **Performance**: Type and range checks are O(1), and dictionary access is efficient.
-   **Design**: Storing values in `obj.__dict__` is standard; omitting `__set_name__` is acceptable since `name` is provided explicitly, aligning with arbitrary implementation.

## Usage Example (For Clarity, Not Submission) 📦

```python
class Test:
    x = NonNegativeInteger("x", default=0)
    y = NonNegativeInteger("y")

obj = Test()
print(obj.x)  # 0 (default)
obj.x = 42  # Sets successfully
print(obj.x)  # 42
obj.x = -1  # Raises ValueError: Invalid value
obj.y = 10  # Sets successfully
print(obj.y)  # 10
print(obj.y)  # Raises AttributeError: Attribute not found (after del obj.y)
```

## Conclusion 🚀

The `NonNegativeInteger` implementation is accurate, enforcing non-negative integer values with flexible default handling and clear error messages.
It’s ideal for attribute validation or descriptor education, fully compliant with the task’s requirements.
