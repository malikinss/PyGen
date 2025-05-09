# Selfie Class Implementation

## Description 📝

The provided code implements the `Selfie` class, which allows instances to save their state (attributes and values), restore previous states by index, and track the number of saved states.
The class uses a list to store state snapshots, excluding the history itself to avoid recursive issues.
The `save_state` method captures the current state, `recover_state` returns a new instance with the state at a given index (or the current instance if the index is invalid), and `n_states` returns the count of saved states.
Deep copying ensures state integrity.

## Purpose 🎯

Intended for applications requiring state management, such as undo/redo functionality, object versioning, or educational examples of Python classes, state persistence, and deep copying.

## How It Works 🔍

-   **Class Definition**:
    -   `Selfie` manages a history of states as a list of dictionaries.
    -   Uses type hints (`Dict`, `Any`, `Self`, `List`) for clarity.
-   **Initialization (`__init__`)**:
    -   Initializes `self.history` as an empty list to store state snapshots.
-   **save_state Method**:
    -   Creates a dictionary of current attributes (`self.__dict__`), excluding `history` to prevent recursive copying.
    -   Uses `deepcopy` to ensure a complete copy of attribute values.
    -   Appends the state to `self.history`.
-   **recover_state Method**:
    -   Takes an `index` (0-based) to restore a saved state.
    -   If `index` is valid (`0 <= index < len(self.history)`):
        -   Creates a new `Selfie` instance.
        -   Updates its `__dict__` with a deep copy of the state at `index`.
        -   Sets the new instance’s `history` to a deep copy of the state at `index` (as a single-entry list).
        -   Returns the new instance.
    -   If `index` is invalid, returns `self` (current instance).
-   **n_states Method**:
    -   Returns the length of `self.history`, indicating the number of saved states.
-   **Behavior**:
    -   Saves states as dictionaries of attributes (excluding `history`).
    -   Indexes states starting at 0 (first state), 1, 2, etc.
    -   Restores states by creating new instances with the saved attributes.
    -   Returns the current instance for invalid state indices.
    -   Tracks the number of states accurately.
    -   Uses deep copying to handle complex attribute values (e.g., lists).

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Creates a `Selfie` instance with no initial attributes or history.
    -   Example: `Selfie()` has `history = []`.
-   **save_state**:
    -   Captures current attributes (excluding `history`) and adds to `history`.
    -   Example: `obj.x = 1; obj.y = 2; obj.save_state()` stores `{'x': 1, 'y': 2}`.
-   **recover_state**:
    -   Returns a new `Selfie` instance with the state at the given index.
    -   Example: After `save_state()` with `x=1, y=2`, `recover_state(0)` returns a new instance with `x=1, y=2`.
    -   Invalid index: Returns `self`.
    -   Example: `recover_state(7)` returns the current instance if no state at index 7.
-   **n_states**:
    -   Returns the number of saved states.
    -   Example: After three `save_state()` calls, `n_states()` → `3`.
    -   Initially: `n_states()` → `0`.
-   **Correctness**:
    -   States are indexed correctly (0, 1, 2, ...).
    -   `deepcopy` ensures independent state copies, handling nested objects.
    -   Excluding `history` from saved states prevents recursive issues.
    -   New instances from `recover_state` have their own `history` with the restored state.
    -   No validation needed, as inputs are guaranteed correct.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   Excluding `history` from saved states avoids infinite recursion and keeps states clean.
    -   `deepcopy` ensures that mutable attributes (e.g., lists) are not shared between states.
    -   `recover_state` creates a new instance, preserving the original instance’s state.
    -   Invalid indices return `self`, matching the requirement.
    -   `history` in restored instances is set to a single state to maintain consistency.
-   **Performance**:
    -   Initialization: O(1) for creating empty list.
    -   `save_state`: O(n) for copying n attributes, including deep copy overhead.
    -   `recover_state`: O(n) for copying state attributes and history.
    -   `n_states`: O(1) for returning list length.
    -   Efficient for typical use cases with small attribute sets.
-   **Design**:
    -   List-based `history` is simple and supports indexing naturally.
    -   Type hints (`Self`, `Dict[str, Any]`) clarify return and attribute types.
    -   Deep copying ensures state isolation, critical for mutable attributes.
    -   Single `history` list per instance tracks all states efficiently.
-   **Alternatives**:
    -   Shallow copy: Insufficient for mutable attributes (e.g., lists would be shared).
    -   Custom state storage (e.g., named tuples): More complex, no clear benefit.
    -   Full history in restored instances: Possible but deviates from requirement (restored instance needs only the current state).
-   **Extensibility**:
    -   Easily extended to limit history size or add state metadata (e.g., timestamps).
    -   Could add state comparison or merging if needed.
-   **Edge Cases**:
    -   Empty state: `save_state()` saves `{}` if no attributes.
    -   No states: `recover_state(n)` returns `self`, `n_states()` returns `0`.
    -   Mutable attributes: Handled correctly by `deepcopy`.
    -   Negative index: Returns `self` (invalid index).
    -   Multiple `save_state` calls: States are stored and indexed correctly.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instance and modify state
obj = Selfie()
print(obj.n_states())  # 0
obj.x = 1
obj.y = 2
obj.save_state()  # State 0: x=1, y=2

# Change state
obj.x = 0
obj.y = 0
print(obj.x, obj.y)  # 0 0

# Restore state
obj = obj.recover_state(0)
print(obj.x, obj.y)  # 1 2
print(obj.n_states())  # 1 (restored instance has state 0)

# Invalid index
obj = obj.recover_state(7)
print(obj.x, obj.y)  # 1 2 (returns self)

# Multiple states
obj = Selfie()
obj.x = 0
obj.save_state()  # State 0: x=0
obj.x = 1
obj.save_state()  # State 1: x=1
obj.x = 2
obj.save_state()  # State 2: x=2
print(obj.n_states())  # 3
obj = obj.recover_state(1)
print(obj.x)  # 1
print(obj.n_states())  # 1

# Test with mutable attributes
obj = Selfie()
obj.list = [1, 2]
obj.save_state()
obj.list.append(3)
obj = obj.recover_state(0)
print(obj.list)  # [1, 2] (deep copy preserved original)
```

## Conclusion 🚀

The `Selfie` class implementation is precise, correctly managing state saving, restoration, and counting.
It uses `deepcopy` to handle complex attributes, returns new instances for state restoration, and handles invalid indices by returning the current instance.
The implementation is efficient, extensible, and ideal for state management tasks or teaching state persistence, fully compliant with the task’s requirements.
