# RandomNumber Class Random Integer Descriptor

## Description 📝

The `RandomNumber` class is a descriptor that generates a random integer within a specified range `[start, end]` (inclusive) when an attribute is accessed.
It accepts three arguments during instantiation: `start` (integer), `end` (integer), and `cache` (boolean, defaulting to `False`).
The descriptor must be assigned to an attribute matching the variable name.
If `cache` is `True`, it returns the first generated number on subsequent accesses; otherwise, it generates a new random number each time.
Setting the attribute raises `AttributeError` with "Change is not possible".

## Purpose 🎯

Intended for scenarios requiring controlled random value generation, such as simulations, testing, or game mechanics, where consistent or fresh random numbers are needed.
The read-only nature and caching option make it suitable for applications requiring stable or dynamic randomness, as well as educational examples of Python’s descriptor protocol.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `start`, `end` (integers), and `cache` (boolean).
    -   Stores them as `self._start`, `self._end`, and `self._cache`.
    -   Initializes `self._generated` as `None` to track the cached number.
    -   Initializes `self._attr` as an empty string for the attribute name.
-   **Set Name Method (`__set_name__`)**:
    -   Called automatically when the descriptor is assigned in a class.
    -   Sets `self._attr` to the attribute name, ensuring it matches the variable name.
-   **Get Method (`__get__`)**:
    -   If `obj` is `None` (class access), returns the descriptor instance.
    -   If `self._cache` is `True` and `self._generated` is not `None`, returns the cached `self._generated`.
    -   Otherwise, generates a new random integer using `random.randint(self._start, self._end)`, stores it in `self._generated`, and returns it.
-   **Set Method (`__set__`)**:
    -   Raises `AttributeError` with "Change is not possible" for any attempt to set or modify the attribute.
-   **Behavior**:
    -   Provides random integers in the specified range on access.
    -   Caches the first generated number if `cache=True`.
    -   Prevents attribute modification with a clear error.

## Verification ✅

Implementation satisfies requirements:

-   **Random Generation**:
    -   `obj.x` returns a random integer in `[start, end]` (e.g., `RandomNumber(1, 10)` yields `1` to `10`).
-   **Caching**:
    -   `RandomNumber(1, 10, cache=True)`: `obj.x` returns the same number across accesses.
    -   `RandomNumber(1, 10, cache=False)`: `obj.x` may return different numbers.
-   **Read-Only**:
    -   `obj.x = 5` raises `AttributeError: Change is not possible`.
-   **Naming**:
    -   Descriptor assigned as `x = RandomNumber(1, 10)` uses `x` as `self._attr` via `__set_name__`.
-   **Descriptor Protocol**: `__get__`, `__set__`, and `__set_name__` manage attribute behavior correctly.

## Potential Considerations 🛠️

-   **Correctness**: `random.randint` ensures inclusive range; caching logic correctly persists the first number when `cache=True`. Error message matches requirement.
-   **Performance**: Random number generation and attribute access are O(1), efficient for all operations.
-   **Design**: Storing state (`_generated`, `_attr`) per descriptor instance is clean; `__set_name__` ensures naming consistency, aligning with arbitrary implementation.

## Usage Example (For Clarity, Not Submission) 📦

```python
class Test:
    x = RandomNumber(1, 3)

obj = Test()
print(obj.x)  # Random: 1, 2, or 3
print(obj.x)  # Different random number (if cache=False)
obj.x = 5  # Raises AttributeError: Change is not possible

class CachedTest:
    x = RandomNumber(1, 3, cache=True)

obj2 = CachedTest()
print(obj2.x)  # Random: 1, 2, or 3
print(obj2.x)  # Same number as first access
```

## Conclusion 🚀

The `RandomNumber` implementation is precise, providing controlled random integer generation with optional caching and read-only access.
It’s ideal for randomized attribute access or descriptor education, fully compliant with the task’s requirements.
