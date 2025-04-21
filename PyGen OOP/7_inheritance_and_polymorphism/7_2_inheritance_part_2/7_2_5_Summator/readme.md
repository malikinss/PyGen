# Summator Class Hierarchy

## Description 📝

The provided code implements four classes: `Summator`, `SquareSummator`, `QubeSummator`, and `CustomSummator`.
The `Summator` class calculates the sum of natural numbers from 1 to `n` (1 + 2 + ... + n) using a `total` method.
Its subclasses—`SquareSummator` (sum of squares: 1² + 2² + ... + n²), `QubeSummator` (sum of cubes: 1³ + 2³ + ... + n³), and `CustomSummator` (sum of m-th powers: 1^m + 2^m + ... + n^m)—extend this functionality by overriding the power used in the calculation.
The `total` method is defined only in `Summator`, reused by all subclasses via a `power` attribute.

## Purpose 🎯

Intended to model mathematical summation operations for natural numbers raised to specific or custom powers, suitable for mathematical computations, data analysis, or algorithm development.
The hierarchy demonstrates inheritance and method reuse, making it ideal for extensible calculation frameworks or educational examples of object-oriented programming in Python.

## How It Works 🔍

-   **Summator Class**:
    -   **Initialization (`__init__`)**:
        -   Takes no arguments.
        -   Sets `self.power = 1` (default for sum of numbers).
    -   **Method (`total`)**:
        -   Accepts `n` (integer).
        -   Returns the sum of `k ** self.power` for `k` from 1 to `n` (inclusive) using a generator expression: `sum(k ** self.power for k in range(1, n + 1))`.
-   **SquareSummator Class**:
    -   Inherits from `Summator`.
    -   **Initialization (`__init__`)**:
        -   Takes no arguments, calls `super().__init__()`.
        -   Sets `self.power = 2` (for squares).
    -   Uses `Summator.total` for calculation.
-   **QubeSummator Class**:
    -   Inherits from `Summator`.
    -   **Initialization (`__init__`)**:
        -   Takes no arguments, calls `super().__init__()`.
        -   Sets `self.power = 3` (for cubes).
    -   Uses `Summator.total` for calculation.
-   **CustomSummator Class**:
    -   Inherits from `Summator`.
    -   **Initialization (`__init__`)**:
        -   Accepts `m` (integer, the power).
        -   Calls `super().__init__()`.
        -   Sets `self.power = m` (custom power).
    -   Uses `Summator.total` for calculation.
-   **Behavior**:
    -   `Summator.total` is the single point of calculation, parameterized by `self.power`.
    -   Subclasses set `power` to specialize the summation (1 for numbers, 2 for squares, 3 for cubes, `m` for custom).
    -   All classes except `CustomSummator` instantiate without arguments; `CustomSummator` takes `m`.

## Verification ✅

Implementation satisfies requirements:

-   **Summator**:
    -   No arguments: `Summator()` creates an instance.
    -   `total`: `s.total(3)` → `1 + 2 + 3 = 6`.
-   **SquareSummator**:
    -   No arguments: `SquareSummator()` creates an instance.
    -   `total`: `ss.total(3)` → `1² + 2² + 3² = 1 + 4 + 9 = 14`.
-   **QubeSummator**:
    -   No arguments: `QubeSummator()` creates an instance.
    -   `total`: `qs.total(3)` → `1³ + 2³ + 3³ = 1 + 8 + 27 = 36`.
-   **CustomSummator**:
    -   Initialization: `CustomSummator(4)` sets `power=4`.
    -   `total`: `cs.total(3)` → `1⁴ + 2⁴ + 3⁴ = 1 + 16 + 81 = 98`.
-   **Single `total` Method**:
    -   Defined only in `Summator`, reused via `self.power` in subclasses.
-   **Inheritance**:
    -   `issubclass(SquareSummator, Summator)` → `True`.
    -   `issubclass(QubeSummator, Summator)` → `True`.
    -   `issubclass(CustomSummator, Summator)` → `True`.
-   **Documentation**: Clear docstrings for classes and methods.

## Potential Considerations 🛠️

-   **Correctness**: Single `total` method with `self.power` ensures consistency and avoids duplication. `range(1, n + 1)` includes `n` in the sum.
-   **Performance**: `sum` with generator expression is efficient, O(n) for `n` terms. Could use mathematical formulas (e.g., `n(n+1)/2` for `power=1`) for O(1), but not required.
-   **Design**: `power` attribute centralizes logic; `super().__init__()` ensures proper initialization. Docstrings and type hints enhance clarity.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
s = Summator()
ss = SquareSummator()
qs = QubeSummator()
cs = CustomSummator(4)

# Test methods
print(s.total(3))   # 6 (1 + 2 + 3)
print(ss.total(3))  # 14 (1² + 2² + 3²)
print(qs.total(3))  # 36 (1³ + 2³ + 3³)
print(cs.total(3))  # 98 (1⁴ + 2⁴ + 3⁴)
```

## Conclusion 🚀

The `Summator`, `SquareSummator`, `QubeSummator`, and `CustomSummator` implementation is precise, efficiently calculating sums of powers using a single `total` method.
It’s ideal for mathematical applications or inheritance education, fully compliant with the task’s requirements.
