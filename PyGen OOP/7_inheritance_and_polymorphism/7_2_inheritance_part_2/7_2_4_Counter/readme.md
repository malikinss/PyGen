# DoubledCounter Class Implementation

## Description 📝

The provided code implements the `DoubledCounter` class, a subclass of the given `Counter` class.
The `Counter` class represents a non-negative counter with a `value` attribute and methods `inc` and `dec` to increment or decrement the counter, ensuring non-negativity.
The `DoubledCounter` class extends `Counter` to double the effect of incrementing and decrementing operations, while maintaining the same initialization process and non-negative constraint.

## Purpose 🎯

Intended to model a counter with amplified increment and decrement operations, suitable for applications requiring scaled counting, such as tracking events with weighted impacts or simulations.
It’s also ideal for educational examples of inheritance and method overriding in Python.

## How It Works 🔍

-   **Counter Class** (Given):
    -   **Initialization (`__init__`)**:
        -   Accepts `start` (integer, default `0`) and sets `self.value = start`.
    -   **Methods**:
        -   `inc(num=1)`: Increments `self.value` by `num` (default `1`).
        -   `dec(num=1)`: Decrements `self.value` by `num` (default `1`), ensuring `self.value >= 0` using `max`.
    -   **Attribute**:
        -   `value`: Current counter value.
-   **DoubledCounter Class**:
    -   Inherits from `Counter`, reusing its `__init__` (accepts `start`, default `0`).
    -   **Methods**:
        -   `inc(num=2)`: Calls `super().inc(num)` to increment `self.value` by `num` (default `2`), effectively doubling the default increment (2 instead of 1).
        -   `dec(num=2)`: Calls `super().dec(num)` to decrement `self.value` by `num` (default `2`), ensuring non-negativity via `Counter.dec`, doubling the default decrement (2 instead of 1).
    -   **Attribute**:
        -   `value`: Current counter value (inherited behavior).
-   **Behavior**:
    -   `DoubledCounter` doubles the increment/decrement amount compared to `Counter`.
    -   Non-negativity is enforced by `Counter.dec`.
    -   Initialization matches `Counter` exactly.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   `DoubledCounter(5)` sets `value=5`; `DoubledCounter()` sets `value=0`.
    -   Matches `Counter`’s initialization process.
-   **Attributes**:
    -   `dc.value` reflects the current counter value, inherited from `Counter`.
-   **Methods**:
    -   `inc`:
        -   `dc.inc(3)` increments by `3` (calls `super().inc(3)`).
        -   `dc.inc()` increments by `2` (default, vs. `Counter`’s `1`).
        -   E.g., `dc = DoubledCounter(10); dc.inc(5); print(dc.value)` → `15`.
    -   `dec`:
        -   `dc.dec(3)` decrements by `3` (calls `super().dec(3)`).
        -   `dc.dec()` decrements by `2` (default, vs. `Counter`’s `1`).
        -   Non-negativity enforced: `dc = DoubledCounter(3); dc.dec(5); print(dc.value)` → `0`.
-   **Inheritance**:
    -   `issubclass(DoubledCounter, Counter)` → `True`.
    -   Reuses `Counter`’s logic, adjusting only the default `num` values.
-   **Documentation**: Clear docstrings for classes and methods.

## Potential Considerations 🛠️

-   **Correctness**: Using `super().inc(num)` and `super().dec(num)` with adjusted defaults (`num=2`) correctly doubles the effect. Non-negativity is handled by `Counter.dec`.
-   **Performance**: Operations remain O(1), as `super()` calls are direct and `max` is constant-time.
-   **Design**: Leveraging `Counter`’s existing logic via `super()` minimizes code duplication. Default `num=2` in method signatures ensures doubling for default cases. Docstrings and type hints enhance clarity.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
c = Counter(5)
dc = DoubledCounter(5)

# Test methods
c.inc()  # value = 6
dc.inc()  # value = 7 (increments by 2)
print(c.value, dc.value)  # 6 7

c.dec(3)  # value = 3
dc.dec(3)  # value = 4 (decrements by 3)
print(c.value, dc.value)  # 3 4

dc.dec(10)  # value = 0 (non-negative)
print(dc.value)  # 0
```

## Conclusion 🚀

The `DoubledCounter` implementation is precise, effectively doubling the increment and decrement operations of the `Counter` class while maintaining non-negativity and initialization consistency.
It’s ideal for scaled counter applications or inheritance education, fully compliant with the task’s requirements.
