# Counter Class Hierarchy

## Description 📝

The provided code implements three classes: `Counter`, `NonDecCounter`, and `LimitedCounter`.
The `Counter` class represents a non-negative counter with a `value` attribute and methods to increment (`inc`) and decrement (`dec`) it.
`NonDecCounter`, a subclass of `Counter`, allows only incrementing, with an empty `dec` method. `LimitedCounter`, another subclass of `Counter`, restricts incrementing to a specified `limit`.
All classes adhere to their respective initialization and behavior requirements.

## Purpose 🎯

Intended to model counters with varying constraints, suitable for applications like score tracking, resource limits, or inventory management.
The hierarchy demonstrates inheritance and method overriding, making it ideal for robust systems or educational examples of object-oriented programming in Python.

## How It Works 🔍

-   **Counter Class**:
    -   **Initialization (`__init__`)**:
        -   Accepts `start` (integer, default `0`) and sets `self.value = start`.
    -   **Methods**:
        -   `inc(num=None)`: Increments `self.value` by `num` (default `1` if `None`).
        -   `dec(num=None)`: Decrements `self.value` by `num` (default `1` if `None`), ensuring `self.value` stays non-negative by setting it to `0` if negative.
    -   **Attribute**:
        -   `value`: Current counter value.
-   **NonDecCounter Class**:
    -   Inherits from `Counter`, reusing its `__init__` (same initialization: `start`, default `0`).
    -   **Methods**:
        -   Inherits `inc` from `Counter`.
        -   `dec(num=None)`: Empty method (`pass`), disabling decrementing while matching `Counter.dec`’s signature.
    -   **Attribute**:
        -   `value`: Current counter value (inherited behavior).
-   **LimitedCounter Class**:
    -   Inherits from `Counter`.
    -   **Initialization (`__init__`)**:
        -   Accepts `start` (integer, default `0`) and `limit` (integer, default `10`).
        -   Sets `self.value = start` and `self.limit = limit`.
    -   **Methods**:
        -   `inc(num=None)`: Increments `self.value` by `num` (default `1` if `None`), capping at `self.limit` (sets `self.value` to `min(new_value, limit)`).
        -   Inherits `dec` from `Counter`.
    -   **Attribute**:
        -   `value`: Current counter value.

## Verification ✅

Implementation satisfies requirements:

-   **Counter**:
    -   Initialization: `Counter(5)` sets `value=5`; `Counter()` sets `value=0`.
    -   `inc`: `c.inc(2)` adds `2`; `c.inc()` adds `1`.
    -   `dec`: `c.dec(3)` subtracts `3`; `c.dec()` subtracts `1`; `c.value` stays `>= 0`.
    -   E.g., `c = Counter(2); c.dec(5); print(c.value)` → `0`.
-   **NonDecCounter**:
    -   Initialization: Same as `Counter` (e.g., `NonDecCounter(3)` sets `value=3`).
    -   `inc`: Works as in `Counter`.
    -   `dec`: `ndc.dec(2)` or `ndc.dec()` does nothing.
    -   E.g., `ndc = NonDecCounter(5); ndc.dec(3); print(ndc.value)` → `5`.
-   **LimitedCounter**:
    -   Initialization: `LimitedCounter(5, 10)` sets `value=5`, `limit=10`; `LimitedCounter()` sets `value=0`, `limit=10`.
    -   `inc`: `lc.inc(3)` adds `3` if `value <= limit`; `lc.inc()` adds `1`; caps at `limit`.
    -   `dec`: Inherited, works as in `Counter`.
    -   E.g., `lc = LimitedCounter(8, 10); lc.inc(5); print(lc.value)` → `10`.
-   **Inheritance**:
    -   `issubclass(NonDecCounter, Counter)` → `True`.
    -   `issubclass(LimitedCounter, Counter)` → `True`.
-   **Documentation**: Clear docstrings for classes and methods.

## Potential Considerations 🛠️

-   **Correctness**: Non-negative constraint in `Counter.dec`, empty `NonDecCounter.dec`, and limit capping in `LimitedCounter.inc` match requirements. Method signatures are consistent.
-   **Performance**: All operations (increment, decrement, comparison) are O(1), efficient for typical use.
-   **Design**: Inheritance minimizes code duplication; optional `num` parameter is handled cleanly. Docstrings and typing enhance clarity.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Counter
c = Counter(3)
c.inc()  # value = 4
c.dec(2)  # value = 2
c.dec(5)  # value = 0
print(c.value)  # 0

# NonDecCounter
ndc = NonDecCounter(5)
ndc.inc(2)  # value = 7
ndc.dec(3)  # value = 7 (no change)
print(ndc.value)  # 7

# LimitedCounter
lc = LimitedCounter(8, 10)
lc.inc(5)  # value = 10 (capped)
lc.dec(3)  # value = 7
print(lc.value)  # 7
```

## Conclusion 🚀

The `Counter`, `NonDecCounter`, and `LimitedCounter` implementation is accurate, providing flexible counter functionality with specific constraints.
It’s ideal for counter-based applications or inheritance education, fully compliant with the task’s requirements.
