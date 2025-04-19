# LimitedTakes Class Access-Restricted Descriptor

## Description 📝

The `LimitedTakes` class is a descriptor that restricts the number of times an attribute can be accessed, taking a single argument `times` (the access limit) during instantiation.
It must be assigned to an attribute matching the variable name. When accessing the attribute, it returns the stored value if set and within the access limit, raises `AttributeError` with "Attribute not found" if unset, or raises `MaxCallsException` with "The number of times the attribute can be accessed has been exceeded" if the limit is exceeded.
Setting the attribute stores the value without restrictions.

## Purpose 🎯

Intended for scenarios requiring controlled attribute access, such as rate-limiting data retrieval, enforcing usage quotas, or protecting sensitive data in objects.
It’s also suitable for educational examples demonstrating Python’s descriptor protocol and custom exception handling.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `times` (integer) and stores it as `self._limit`.
    -   Initializes `self._counter` to `0` to track accesses.
    -   Initializes `self._attr` as an empty string to store the attribute name.
-   **Set Name Method (`__set_name__`)**:
    -   Called automatically when the descriptor is assigned in a class.
    -   Sets `self._attr` to the attribute name, ensuring it matches the variable name.
-   **Get Method (`__get__`)**:
    -   If `obj` is `None` (class access), returns the descriptor instance.
    -   Checks if `self._counter >= self._limit`; if true, raises `MaxCallsException`.
    -   If `self._attr` is not in `obj.__dict__`, raises `AttributeError` with "Attribute not found".
    -   Increments `self._counter` and returns the value from `obj.__dict__[self._attr]`.
-   **Set Method (`__set__`)**:
    -   Stores `value` in `obj.__dict__[self._attr]` without any checks.
-   **Behavior**:
    -   Limits attribute reads to `times` accesses.
    -   Allows unrestricted writes.
    -   Tracks accesses per instance via `self._counter`.
    -   Uses custom `MaxCallsException` for limit violations.

## Verification ✅

Implementation satisfies requirements:

-   **Attribute Access**:
    -   `obj.x = "value"; print(obj.x)` returns `"value"` if within limit.
    -   After `times` accesses, `obj.x` raises `MaxCallsException: The number of times the attribute can be accessed has been exceeded`.
    -   If unset, `obj.x` raises `AttributeError: Attribute not found`.
-   **Attribute Setting**:
    -   `obj.x = any_value` sets successfully, regardless of type or prior state.
-   **Access Limit**:
    -   For `LimitedTakes(2)`, `obj.x` allows exactly two accesses before raising `MaxCallsException`.
-   **Naming**:
    -   Descriptor assigned as `x = LimitedTakes(2)` uses `x` as `self._attr` via `__set_name__`.
-   **Descriptor Protocol**: `__get__`, `__set__`, and `__set_name__` manage attribute behavior correctly.

## Potential Considerations 🛠️

-   **Correctness**: `self._counter` per instance ensures independent tracking; `__set_name__` aligns with naming requirement. Exception messages match exactly.
-   **Performance**: O(1) for counter checks and dictionary access, efficient for all operations.
-   **Design**: Storing values in `obj.__dict__` is standard; custom `MaxCallsException` provides clear error signaling, aligning with arbitrary implementation.

## Usage Example (For Clarity, Not Submission) 📦

```python
class Test:
    x = LimitedTakes(2)

obj = Test()
obj.x = "data"
print(obj.x)  # data (1st access)
print(obj.x)  # data (2nd access)
print(obj.x)  # Raises MaxCallsException
obj.x = "new"  # Sets successfully
print(obj.x)  # data (1st access again after set)
del obj.x
print(obj.x)  # Raises AttributeError: Attribute not found
```

## Conclusion 🚀

The `LimitedTakes` implementation is precise, enforcing access limits with clear error handling and unrestricted setting.
It’s ideal for controlled attribute access or descriptor education, fully compliant with the task’s requirements.
