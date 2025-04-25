# DefaultList Class Implementation

## Description 📝

The provided code implements the `DefaultList` class, a subclass of `collections.UserList`.
It represents a list that returns a specified default value when attempting to access an element at a non-existent index.
The class is initialized with two arguments: `iterable` (defining the initial elements, defaulting to an empty tuple) and `default` (the value returned for out-of-bounds indices, defaulting to `None`).
The list is independent of the input iterable, ensuring that changes to the original iterable do not affect the `DefaultList` instance.

## Purpose 🎯

Intended for scenarios where safe index access is needed, such as data processing, user input handling, or dynamic list manipulation, avoiding `IndexError` exceptions.
It’s also suitable for educational examples of list subclassing and custom indexing behavior in Python.

## How It Works 🔍

-   **Class Definition**:
    -   `DefaultList` inherits from `UserList`, which provides a list-like interface with a `self.data` attribute (a standard `list`).
-   **Initialization (`__init__`)**:
    -   Accepts `iterable` (any iterable, default `()`) and `default` (any type, default `None`).
    -   Stores `default` as `self._default`.
    -   Calls `super().__init__(iterable)` to initialize `self.data` with a copy of the iterable’s elements, ensuring independence.
-   **Method**:
    -   `__getitem__(index)`:
        -   Attempts to access `self.data[index]`.
        -   Returns the element if the index exists.
        -   Catches `IndexError` and returns `self._default` for non-existent indices.
-   **Behavior**:
    -   Behaves like a standard list for valid indices and operations (e.g., append, slicing).
    -   Returns `self._default` for out-of-bounds indices (e.g., `lst[100]` or `lst[-100]`).
    -   Independent of the input iterable due to `UserList`’s copying behavior.
    -   Supports all `UserList` methods (e.g., `append`, `extend`, `pop`).

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Accepts `iterable` and `default`: `DefaultList([1, 2], 0)`, `DefaultList(range(3))`, `DefaultList(default="N/A")`.
    -   E.g., `DefaultList([1, 2, 3], 0)` creates a list `[1, 2, 3]` with default `0`.
-   **Default Value**:
    -   Out-of-bounds access returns `default`: `lst = DefaultList([1], 0); lst[5]` → `0`.
    -   Negative indices: `lst[-10]` → `0`.
    -   Default `None`: `DefaultList([1]).[10]` → `None`.
-   **Independence**:
    -   Changes to the input iterable do not affect the list.
    -   E.g., `lst = [1, 2]; d = DefaultList(lst, 0); lst[0] = 3; print(d)` → `[1, 2]`.
-   **List Behavior**:
    -   Inherits `UserList` methods: `append`, `extend`, indexing, etc.
    -   E.g., `d = DefaultList([1], 0); d.append(2); d[1]` → `2`, `d[2]` → `0`.
-   **Inheritance**:
    -   `issubclass(DefaultList, UserList)` → `True`.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**: `__getitem__` handles out-of-bounds indices by returning `self._default`. `UserList` initialization ensures independence via internal list copying. No validation needed per requirements.
-   **Performance**: Index access is O(1) for valid indices; `IndexError` handling is constant-time. Initialization is O(n) for copying the iterable, standard for lists.
-   **Design**: Using `UserList` simplifies list-like behavior. `__getitem__` override is minimal and focused, preserving all other list functionality. Storing `default` as `_default` avoids conflicts with list operations.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
d1 = DefaultList([1, 2, 3], 0)
d2 = DefaultList(range(2), default="N/A")
d3 = DefaultList()
lst = [1, 2]
d4 = DefaultList(lst, -1)

# Test indexing
print(d1[0])    # 1
print(d1[5])    # 0
print(d2[10])   # N/A
print(d3[0])    # None
print(d1[-10])  # 0

# Test independence
lst[0] = 3
print(d4)  # [1, 2]

# Test list operations
d1.append(4)
print(d1)  # [1, 2, 3, 4]
print(d1[4])  # 0
print(isinstance(d1, UserList))  # True
```

## Conclusion 🚀

The `DefaultList` implementation is precise, providing a list that safely handles out-of-bounds index access with a default value while maintaining independence from the input iterable.
It’s ideal for robust list handling or list subclassing education, fully compliant with the task’s requirements.
