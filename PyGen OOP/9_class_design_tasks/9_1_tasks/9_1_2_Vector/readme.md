# Vector Class Implementation

## Description 📝

The provided code implements the `Vector` class, which represents a vector of arbitrary dimension in a coordinate space.
It supports initialization with any number of coordinates, informal string representation, vector operations (addition, subtraction, dot product, normalization), and equality comparisons.
The class raises a `ValueError` with the message "Vectors must have equal length" when operations are attempted on vectors of different dimensions.
The implementation uses Python’s operator overloading and functional programming techniques for concise operation handling.

## Purpose 🎯

Intended for applications involving vector mathematics, such as physics simulations, computer graphics, or educational examples of Python classes, operator overloading, and mathematical operations.

## How It Works 🔍

-   **Class Definition**:
    -   `Vector` is a class with a class constant `ERR_MSG = 'Vectors must have equal length'` for error messages.
    -   Uses type hints (`Union`, `Callable`) for clarity.
-   **Initialization (`__init__`)**:
    -   Accepts a variable number of `coords` (floats) via `*coords`.
    -   Stores coordinates as a list in `self.coords`.
-   **String Representation (`__str__`)**:
    -   Returns a string in the format `(x, y, z, ...)`, with coordinates joined by commas.
    -   Example: `Vector(1, 2, 3)` → `(1, 2, 3)`.
-   **Helper Methods**:
    -   `_same_length(other)`:
        -   Checks if two vectors have equal lengths.
        -   Raises `ValueError` with `ERR_MSG` if lengths differ.
        -   Returns `True` if lengths are equal.
    -   `_do_action(other, action)`:
        -   Generic method to perform element-wise operations (`add`, `sub`, `mul`).
        -   Validates that `other` is a `Vector` and checks length equality.
        -   Applies the `action` (e.g., `operator.add`) to corresponding coordinates using `map`.
        -   For `mul`, returns the sum of products (dot product).
        -   For `add` or `sub`, returns a new `Vector` with resulting coordinates.
        -   Returns `NotImplemented` for non-`Vector` operands.
-   **Vector Operations**:
    -   `__add__(other)`: Returns a new `Vector` with element-wise sum of coordinates.
        -   Example: `Vector(1, 2, 3) + Vector(3, 4, 5)` → `Vector(4, 6, 8)`.
    -   `__sub__(other)`: Returns a new `Vector` with element-wise difference.
        -   Example: `Vector(1, 2, 3) - Vector(3, 4, 5)` → `Vector(-2, -2, -2)`.
    -   `__mul__(other)`: Returns the dot product (sum of element-wise products).
        -   Example: `Vector(1, 2, 3) * Vector(3, 4, 5)` → `1*3 + 2*4 + 3*5 = 26`.
-   **Normalization (`norm`)**:
    -   Computes the Euclidean norm (square root of the dot product with itself).
    -   Example: `Vector(5, 6, 7, 8).norm()` → `sqrt(5^2 + 6^2 + 7^2 + 8^2) = sqrt(174) ≈ 13.19090595827292`.
-   **Equality Comparison (`__eq__`)**:
    -   Checks if two vectors have equal coordinates.
    -   Returns `True` if lengths and coordinates match, `False` otherwise.
    -   Returns `NotImplemented` for non-`Vector` operands.
    -   Example: `Vector(1, 2, 3) == Vector(1, 2, 3)` → `True`.
-   **Behavior**:
    -   Supports vectors of any dimension.
    -   Raises `ValueError` for operations on vectors of different lengths.
    -   Handles addition, subtraction, dot product, normalization, and equality.
    -   Informal string representation matches `(x, y, z, ...)` format.
    -   No validation beyond length checks, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Accepts arbitrary number of coordinates.
    -   Example: `Vector(1, 2, 3)`, `Vector(5, 6, 7, 8)` work as expected.
-   **String Representation**:
    -   Informal: `(x, y, z, ...)`.
    -   Example: `str(Vector(1, 2, 3))` → `(1, 2, 3)`.
-   **Vector Operations**:
    -   Addition: `Vector(1, 2, 3) + Vector(3, 4, 5)` → `(4, 6, 8)`.
    -   Subtraction: `Vector(1, 2, 3) - Vector(3, 4, 5)` → `(-2, -2, -2)`.
    -   Dot Product: `Vector(1, 2, 3) * Vector(3, 4, 5)` → `26`.
    -   Normalization: `Vector(5, 6, 7, 8).norm()` → `≈13.19090595827292`.
-   **Comparisons**:
    -   Equality: `Vector(1, 2, 3) == Vector(1, 2, 3)` → `True`; `Vector(1, 2, 3) == Vector(4, 5, 6)` → `False`.
    -   Inequality: Implicitly supported via `__eq__`.
-   **Error Handling**:
    -   Raises `ValueError` with "Vectors must have equal length" for operations on vectors of different dimensions.
    -   Example: `Vector(1, 2) + Vector(1, 2, 3)` raises `ValueError`.
-   **Correctness**:
    -   `_do_action` centralizes operation logic, reducing code duplication.
    -   `map` with `operator` functions (`add`, `sub`, `mul`) ensures efficient element-wise operations.
    -   `sqrt` from `math` computes norm accurately.
    -   No additional validation needed, as inputs are guaranteed correct.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `self.coords = list(coords)` stores coordinates as a list for flexibility.
    -   `_same_length` enforces equal length for operations, raising `ValueError` as required.
    -   `_do_action` handles all vector operations consistently, using `map` for efficiency.
    -   `__eq__` compares coordinates directly, leveraging list equality.
    -   `norm` reuses `_do_action` for dot product, ensuring consistency.
-   **Performance**:
    -   Initialization: O(n) for storing n coordinates.
    -   `__str__`: O(n) for string formatting.
    -   Operations (`__add__`, `__sub__`, `__mul__`): O(n) for mapping n coordinates.
    -   `norm`: O(n) for dot product plus O(1) for `sqrt`.
    -   `__eq__`: O(n) for comparing n coordinates.
    -   Efficient for typical vector sizes.
-   **Design**:
    -   Class-based design with operator overloading is intuitive for vector operations.
    -   Type hints (`Union['Vector', float]`, `Callable`) clarify return and argument types.
    -   `_do_action` reduces code duplication and improves maintainability.
    -   `NotImplemented` for non-`Vector` operands ensures proper operator delegation.
-   **Alternatives**:
    -   Manual loops instead of `map`: More verbose, less functional.
    -   List comprehension for operations: Similar performance but less elegant.
    -   Using `numpy`: Overkill for this simple task.
    -   Storing coordinates as tuple: Less flexible for potential extensions.
-   **Extensibility**:
    -   Easily extended to support additional operations (e.g., cross product for 3D vectors).
    -   Could add validation (e.g., numeric coordinates) if needed.
-   **Edge Cases**:
    -   Empty vector (`Vector()`): Valid, operations with it raise `ValueError` if lengths differ.
    -   Single-dimensional vector: Handled correctly (e.g., `Vector(1) + Vector(2)` → `Vector(3)`).
    -   Non-`Vector` operands: Returns `NotImplemented`, allowing Python to handle errors.
    -   Different lengths: Correctly raises `ValueError`.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create vectors
a = Vector(1, 2, 3)
b = Vector(3, 4, 5)
c = Vector(5, 6, 7, 8)

# Test string representation
print(a)  # (1, 2, 3)
print(b)  # (3, 4, 5)
print(c)  # (5, 6, 7, 8)

# Test vector operations
print(a + b)  # (4, 6, 8)
print(a - b)  # (-2, -2, -2)
print(a * b)  # 26
print(c.norm())  # 13.19090595827292

# Test equality
print(a == Vector(1, 2, 3))  # True
print(a == Vector(4, 5, 6))  # False
print(a != Vector(1, 2, 3))  # False (implicit via __eq__)

# Test different lengths
try:
    a + c  # Raises ValueError: Vectors must have equal length
except ValueError as e:
    print(e)  # Vectors must have equal length

# Test with single dimension
d = Vector(1)
e = Vector(2)
print(d + e)  # (3)
print(d * e)  # 2
```

## Conclusion 🚀

The `Vector` class implementation is precise, supporting arbitrary-dimensional vectors with correct initialization, string representation, operations (addition, subtraction, dot product, normalization), and equality comparisons.
It robustly handles errors for unequal lengths, is efficient, and is extensible.
The design is ideal for mathematical applications or teaching vector concepts, fully compliant with the task’s requirements.
