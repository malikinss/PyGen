# ArithmeticProgression and GeometricProgression Class Implementation

## Description 📝

The provided code implements two classes, `ArithmeticProgression` and `GeometricProgression`, for generating terms of infinite arithmetic and geometric progressions, respectively.
Both classes inherit from an abstract base class `Progression`, which defines common iteration logic. `ArithmeticProgression` generates terms by adding a fixed difference, while `GeometricProgression` generates terms by multiplying by a fixed ratio.
Both classes are iterable, infinite, and initialized with a starting term and a step (difference or ratio).

## Purpose 🎯

Intended for applications requiring sequences of numbers, such as mathematical modeling, algorithm testing, or educational examples of Python iterators, abstract base classes, and progression generation.

## How It Works 🔍

-   **Progression (Abstract Base Class)**:
    -   Defined with `ABC` to serve as a base for progression classes.
    -   `__init__(start, step)`:
        -   Stores `start` (first term) and `step` (difference or ratio) as `self.start` and `self.step`.
        -   Initializes `self.cur` to `start` for tracking the current term.
    -   `__iter__`: Returns `self` to make the class iterable.
    -   `__next__`: Abstract method, to be implemented by subclasses.
-   **ArithmeticProgression**:
    -   Inherits from `Progression`.
    -   `__next__`:
        -   Returns the current term (`self.cur`).
        -   Increments `self.cur` by `self.step` (difference).
        -   Example: `ArithmeticProgression(0, 1)` generates `0, 1, 2, 3, ...`.
-   **GeometricProgression**:
    -   Inherits from `Progression`.
    -   `__next__`:
        -   Returns the current term (`self.cur`).
        -   Multiplies `self.cur` by `self.step` (ratio).
        -   Example: `GeometricProgression(1, 2)` generates `1, 2, 4, 8, ...`.
-   **Behavior**:
    -   Both classes are infinite iterators, generating terms on demand.
    -   Support iteration via `for` loops or `next()`.
    -   Initialized with a starting term and a step (difference for arithmetic, ratio for geometric).
    -   No validation is needed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **ArithmeticProgression**:
    -   Initialization: Accepts `start` (first term) and `step` (difference).
        -   Example: `ArithmeticProgression(0, 1)` starts at 0, increments by 1.
    -   Iterable: Supports `for` loop iteration.
    -   Infinite: Continues generating terms indefinitely.
    -   Example Output: `0 1 2 3 4 5 6 7 8 9 10` for loop with `elem > 10` break.
-   **GeometricProgression**:
    -   Initialization: Accepts `start` (first term) and `step` (ratio).
        -   Example: `GeometricProgression(1, 2)` starts at 1, multiplies by 2.
    -   Iterable: Supports `for` loop iteration.
    -   Infinite: Continues generating terms indefinitely.
    -   Example Output: `1 2 4 8` for loop with `elem > 10` break.
-   **Correctness**:
    -   `Progression` abstracts common logic, reducing code duplication.
    -   `__iter__` and `__next__` implement the iterator protocol correctly.
    -   Arithmetic: Adds `step` to generate next term.
    -   Geometric: Multiplies by `step` to generate next term.
    -   No validation needed, as inputs are guaranteed correct.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `self.cur` tracks the current term, updated correctly in `__next__`.
    -   Arithmetic: `self.cur += self.step` produces the next term (e.g., `0 + 1 = 1`).
    -   Geometric: `self.cur *= self.step` produces the next term (e.g., `1 * 2 = 2`).
    -   Returning `self.cur` before updating ensures the correct term is yielded.
    -   Infinite iteration is achieved by not raising `StopIteration`.
-   **Performance**:
    -   Initialization: O(1) for storing `start` and `step`.
    -   `__next__`: O(1) for arithmetic (addition) or geometric (multiplication).
    -   Iteration: O(n) for generating n terms.
    -   Highly efficient for typical use cases.
-   **Design**:
    -   Abstract base class `Progression` promotes code reuse and clarity.
    -   Type hints (`float`, `Self`) clarify method signatures.
    -   Separate classes for arithmetic and geometric progressions align with requirements.
    -   Iterator protocol (`__iter__`, `__next__`) is standard and intuitive.
-   **Alternatives**:
    -   Manual iterator class: More verbose, less elegant.
    -   Generator function: Possible but doesn’t fit class-based requirement.
    -   Single class with mode: Less clear than separate classes.
-   **Extensibility**:
    -   Easily extended to support finite progressions (e.g., add `stop` condition).
    -   Could add validation (e.g., non-zero step for geometric) if needed.
-   **Edge Cases**:
    -   Zero step (arithmetic): Valid, generates constant sequence (e.g., `0, 0, 0, ...`).
    -   Zero step (geometric): Valid, generates zeros after first term.
    -   Negative step: Valid, generates decreasing sequences.
    -   Non-integer inputs: Supported via `float` type, as no restrictions specified.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Test ArithmeticProgression
progression = ArithmeticProgression(0, 1)
for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')  # 0 1 2 3 4 5 6 7 8 9 10
print()

# Test GeometricProgression
progression = GeometricProgression(1, 2)
for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')  # 1 2 4 8
print()

# Test with different parameters
arith = ArithmeticProgression(5, 2)
for i, elem in enumerate(arith):
    if i >= 5:
        break
    print(elem, end=' ')  # 5 7 9 11 13
print()

geom = GeometricProgression(2, 3)
for i, elem in enumerate(geom):
    if i >= 4:
        break
    print(elem, end=' ')  # 2 6 18 54
print()

# Test iterator directly
arith_iter = iter(ArithmeticProgression(0, 0.5))
print(next(arith_iter))  # 0.0
print(next(arith_iter))  # 0.5
print(next(arith_iter))  # 1.0
```

## Conclusion 🚀

The `ArithmeticProgression` and `GeometricProgression` class implementations are precise, providing infinite, iterable sequences using the iterator protocol.
The abstract `Progression` base class ensures code reuse, while separate classes clearly distinguish arithmetic (addition) and geometric (multiplication) logic.
The implementation is efficient, extensible, and ideal for sequence generation tasks or teaching iterator concepts, fully compliant with the task’s requirements.
