# Triangle and EquilateralTriangle Class Hierarchy

## Description 📝

The provided code implements two classes: `Triangle` and `EquilateralTriangle`.
The `Triangle` class represents a general triangle, initialized with three side lengths (`a`, `b`, `c`) and featuring a `perimeter` method that returns the sum of the sides.
The `EquilateralTriangle` class, a subclass of `Triangle`, represents an equilateral triangle, initialized with a single `side` length, which is used for all three sides.

## Purpose 🎯

Intended to model triangles in geometric applications, such as graphics, physics simulations, or mathematical tools.
The hierarchy supports general and specialized triangle types, making it suitable for extensible geometric modeling or educational examples of inheritance and method reuse in Python.

## How It Works 🔍

-   **Triangle Class**:
    -   **Initialization (`__init__`)**:
        -   Accepts three arguments: `a`, `b`, `c` (floats), representing side lengths.
        -   Stores them as instance attributes: `self.a`, `self.b`, `self.c`.
    -   **Method (`perimeter`)**:
        -   Returns the sum of the sides: `self.a + self.b + self.c`.
-   **EquilateralTriangle Class**:
    -   Inherits from `Triangle`.
    -   **Initialization (`__init__`)**:
        -   Accepts one argument: `side` (float), representing the length of each side.
        -   Calls `super().__init__(side, side, side)` to initialize the parent `Triangle` with equal sides.
    -   **Method**:
        -   Inherits `perimeter` from `Triangle`, which works correctly as all sides are equal.
-   **Behavior**:
    -   `Triangle` handles any valid triangle with arbitrary side lengths.
    -   `EquilateralTriangle` simplifies initialization for equilateral cases, reusing `Triangle`’s perimeter logic.
    -   Inheritance ensures `EquilateralTriangle` is a specialized `Triangle`.

## Verification ✅

Implementation satisfies requirements:

-   **Triangle**:
    -   Initialization: `Triangle(3, 4, 5)` sets `a=3`, `b=4`, `c=5`.
    -   `perimeter`: `t.perimeter()` returns `3 + 4 + 5 = 12`.
    -   E.g., `t = Triangle(2.5, 3.5, 4); print(t.perimeter())` → `10.0`.
-   **EquilateralTriangle**:
    -   Initialization: `EquilateralTriangle(5)` sets `a=5`, `b=5`, `c=5` via parent `__init__`.
    -   `perimeter`: `et.perimeter()` returns `5 + 5 + 5 = 15`.
    -   E.g., `et = EquilateralTriangle(3); print(et.perimeter())` → `9.0`.
-   **Inheritance**:
    -   `issubclass(EquilateralTriangle, Triangle)` → `True`.
    -   `EquilateralTriangle` reuses `Triangle.perimeter` without modification.
-   **Documentation**: Clear docstrings for classes and methods.

## Potential Considerations 🛠️

-   **Correctness**: `super().__init__(side, side, side)` correctly sets equal sides; `perimeter` works for both classes. No validation needed per requirements.
-   **Performance**: Perimeter calculation is O(1), efficient for all cases.
-   **Design**: Inheritance with `super()` minimizes code duplication; single `side` argument for `EquilateralTriangle` simplifies usage. Docstrings and type hints enhance clarity.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
t = Triangle(3, 4, 5)
et = EquilateralTriangle(6)

# Test methods
print(t.perimeter())  # 12
print(et.perimeter())  # 18
print(isinstance(et, Triangle))  # True
print(et.a, et.b, et.c)  # 6 6 6
```

## Conclusion 🚀

The `Triangle` and `EquilateralTriangle` implementation is precise, providing a general triangle class and a specialized equilateral subclass with efficient perimeter calculation.
It’s ideal for geometric applications or inheritance education, fully compliant with the task’s requirements.
