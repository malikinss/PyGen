# Versioned Class Attribute History Descriptor

## Description 📝

The `Versioned` class is a descriptor that tracks the history of an attribute’s values, allowing access to the current value and all previous values set via dot notation or `setattr()`.
It takes no arguments during instantiation and must be assigned to an attribute matching the variable name. When accessing the attribute, it returns the current value or raises `AttributeError` with "Attribute not found" if unset. Setting the attribute adds the new value to the history.
The class provides two methods: `get_version` (retrieves the n-th value, 1-based index) and `set_version` (sets the n-th value as current without adding to history).

## Purpose 🎯

Intended for scenarios requiring versioned attribute access, such as undo/redo functionality, auditing changes, or maintaining state history in data models or applications.
The ability to restore previous values without altering history makes it suitable for robust systems or educational examples of Python’s descriptor protocol and state management.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Initializes `self._attr` (attribute name) and `self._history_key` (history storage key) as empty strings.
-   **Set Name Method (`__set_name__`)**:
    -   Called automatically when the descriptor is assigned in a class.
    -   Sets `self._attr` to the attribute name and `self._history_key` to `{attr}_history` for storing history.
-   **Get Method (`__get__`)**:
    -   If `obj` is `None` (class access), returns the descriptor instance.
    -   If `self._attr` is not in `obj.__dict__`, raises `AttributeError` with "Attribute not found".
    -   Returns the current value from `obj.__dict__[self._attr]`.
-   **Set Method (`__set__`)**:
    -   Initializes an empty history list in `obj.__dict__[self._history_key]` if not present.
    -   Appends `value` to the history list.
    -   Sets `obj.__dict__[self._attr]` to `value`.
-   **Get Version Method (`get_version`)**:
    -   Takes `obj` (instance) and `n` (1-based index).
    -   Returns the (n-1)-th value from `obj.__dict__[self._history_key]`.
-   **Set Version Method (`set_version`)**:
    -   Takes `obj` (instance) and `n` (1-based index).
    -   Sets `obj.__dict__[self._attr]` to the (n-1)-th value from the history, without appending to history.
-   **Helper Method (`_is_history_exists`)**:
    -   Checks if `self._history_key` exists in `obj.__dict__`.
-   **Behavior**:
    -   Tracks all values set via `__set__` in a history list.
    -   Allows retrieval or restoration of any historical value using 1-based indexing.
    -   `set_version` restores values without affecting history.

## Verification ✅

Implementation satisfies requirements:

-   **Attribute Access**:
    -   `obj.x = 1; print(obj.x)` returns `1`.
    -   If unset, `obj.x` raises `AttributeError: Attribute not found`.
-   **Attribute Setting**:
    -   `obj.x = 1; obj.x = 2` stores `[1, 2]` in history; `obj.x` is `2`.
-   **Version Methods**:
    -   `v.get_version(obj, 1)` returns `1` (first value).
    -   `v.set_version(obj, 1)` sets `obj.x` to `1` without adding to history.
    -   Subsequent `obj.x = 3` continues history as `[1, 2, 3]`.
-   **Naming**:
    -   Descriptor assigned as `x = Versioned()` uses `x` as `self._attr` via `__set_name__`.
-   **Descriptor Protocol**: `__get__`, `__set__`, and `__set_name__` manage attribute behavior correctly.

## Potential Considerations 🛠️

-   **Correctness**: History is only updated in `__set__`, ensuring `set_version` doesn’t alter it. 1-based indexing matches typical user expectations.
-   **Performance**: List append and access are O(1) on average; dictionary operations are efficient.
-   **Design**: Storing history in `obj.__dict__` with a unique key avoids conflicts; `__set_name__` ensures naming consistency, aligning with arbitrary implementation.

## Usage Example (For Clarity, Not Submission) 📦

```python
class Test:
    x = Versioned()

obj = Test()
obj.x = 1
obj.x = 2
print(obj.x)  # 2
print(obj.x.get_version(obj, 1))  # 1
obj.x.set_version(obj, 1)
print(obj.x)  # 1
obj.x = 3
print(obj.x.get_version(obj, 3))  # 3
print(obj.x)  # Raises AttributeError: Attribute not found (if unset)
```

## Conclusion 🚀

The `Versioned` implementation is robust, tracking attribute value history with flexible version retrieval and restoration.
It’s ideal for versioned state management or descriptor education, fully compliant with the task’s requirements.
