# FieldTracker Class Implementation

## Description 📝

The `FieldTracker` class is a base class designed to enable its subclasses to track changes in specified attributes.
It assumes subclasses define a `fields` tuple containing the names of attributes to track and call `FieldTracker.__init__` after setting initial attribute values.
It provides four methods: `base` (returns an attribute's initial value), `has_changed` (checks if an attribute has changed), `changed` (returns a dictionary of changed attributes and their initial values), and `save` (resets tracking to consider current values as initial).

## Purpose 🎯

Intended for scenarios requiring attribute state tracking, such as auditing changes in data models, implementing undo functionality, or monitoring configuration objects.
It’s suitable for extensible frameworks or educational examples of state management and inheritance in Python.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Creates a `_history` dictionary storing the initial values of tracked attributes (from `self.fields`) by accessing their current values via `getattr(self, attr)`.
    -   Assumes `self.fields` exists and attributes are set before calling.
-   **Methods**:
    -   `base(attr)`:
        -   Returns the initial value of `attr` from `self._history`.
    -   `has_changed(attr)`:
        -   Returns `True` if the current value of `attr` (`getattr(self, attr)`) differs from its initial value (`self.base(attr)`), `False` otherwise.
    -   `changed()`:
        -   Returns a dictionary of attributes from `self.fields` that have changed, mapping each to its initial value.
        -   Uses `has_changed` to filter changed attributes.
    -   `save()`:
        -   Updates `self._history` with the current values of all tracked attributes, resetting tracking.
-   **Behavior**:
    -   Tracks changes only when attribute values differ (per requirement).
    -   Stores initial values at initialization and updates them only via `save`.
    -   Relies on `self.fields` tuple for attribute names and assumes proper subclass initialization.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   `FieldTracker.__init__` captures initial values of `fields` attributes.
    -   Works with subclasses that set `fields` and call `super().__init__`.
-   **Methods**:
    -   `base(attr)`: Returns initial value, e.g., `tracker.base("x")` → initial `x` value.
    -   `has_changed(attr)`: Returns `True` if `attr` changed, e.g., `tracker.x = new_value; tracker.has_changed("x")` → `True` if `new_value != initial`.
    -   `changed()`: Returns `{attr: initial_value}` for changed attributes, e.g., if `x` changed, returns `{"x": initial_x}`.
    -   `save()`: Resets tracking, so `has_changed(attr)` returns `False` until further changes.
-   **Behavior**:
    -   Tracks only attributes in `self.fields`.
    -   Considers changes only when values differ.
    -   Resets tracking correctly with `save`.
-   **Assumptions**:
    -   Subclasses provide `fields` tuple and call `FieldTracker.__init__` after setting attributes.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**: `_history` captures initial values at initialization; `has_changed` uses value comparison; `save` updates `_history` correctly. Matches requirement for change detection.
-   **Performance**: Dictionary operations and `getattr` are O(1); `changed` iterates `fields` (O(n), where n is number of fields, typically small).
-   **Design**: `_history` dictionary is simple and effective; relying on `self.fields` and subclass initialization aligns with requirements. Arbitrary implementation allows flexibility.

## Usage Example (For Clarity, Not Submission) 📦

```python
class Point(FieldTracker):
    fields = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

p = Point(1, 2)
print(p.base("x"))  # 1
p.x = 3
print(p.has_changed("x"))  # True
print(p.has_changed("y"))  # False
print(p.changed())  # {"x": 1}
p.save()
print(p.has_changed("x"))  # False
print(p.base("x"))  # 3
```

## Conclusion 🚀

The `FieldTracker` implementation is precise, providing robust attribute state tracking with minimal overhead.
It’s ideal for change monitoring in data models or inheritance education, fully compliant with the task’s requirements.
