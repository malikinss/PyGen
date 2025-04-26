# CustomRange Class Implementation

## Description 📝

The provided code implements the `CustomRange` class, a subclass of `collections.abc.Sequence`.
It represents a sequence of integers derived from single numbers and ranges (e.g., `"1-4"` for 1, 2, 3, 4).
The class supports iteration, length calculation, reverse iteration, membership testing, and indexing (positive and negative).
It accepts an arbitrary number of positional arguments (integers or range strings) during initialization.

## Purpose 🎯

Intended for scenarios requiring a flexible sequence of integers from mixed inputs (single numbers and ranges), such as data processing, range-based iteration, or custom sequence handling.
It’s also suitable for educational examples of sequence protocols and abstract base classes in Python.

## How It Works 🔍

-   **Class Definition**:
    -   Inherits from `collections.abc.Sequence`, which provides default implementations for `__iter__`, `__contains__`, `__reversed__`, and others, requiring only `__len__` and `__getitem__`.
-   **Initialization (`__init__`)**:
    -   Accepts `*args` (integers or range strings like `"a-b"`).
    -   Processes each argument:
        -   For strings: Splits on `'-'`, converts to integers, and adds all numbers from `start` to `end` (inclusive) using `range(start, end + 1)`.
        -   For integers: Adds directly to the internal list.
    -   Stores all numbers in `self.data` (a list).
-   **Methods**:
    -   `__len__`: Returns the length of `self.data`.
    -   `__getitem__(key)`: Returns the element or slice from `self.data`, supporting positive/negative indices and slices.
-   **Inherited Behavior (from `Sequence`)**:
    -   `__iter__`: Iterates over `self.data`.
    -   `__reversed__`: Returns an iterator over `self.data` in reverse order.
    -   `__contains__`: Checks if a value is in `self.data` (for `in` operator).
-   **Behavior**:
    -   Iterable: Supports `for x in custom_range`.
    -   Length: `len(custom_range)` returns total numbers.
    -   Reversed: `reversed(custom_range)` iterates in reverse.
    -   Membership: `x in custom_range` checks presence.
    -   Indexing: Supports `custom_range[i]` (positive/negative) and slicing.

## Choice of Parent Class 🛠️

-   **Why `Sequence`?**:
    -   `collections.abc.Sequence` is ideal because `CustomRange` represents an ordered, indexable collection of integers with a fixed length.
    -   `Sequence` requires `__len__` and `__getitem__`, which are straightforward to implement given the internal list storage.
    -   It provides default implementations for `__iter__`, `__contains__`, `__reversed__`, and others, reducing code duplication.
    -   Alternatives like `Iterable` or `Collection` were less suitable:
        -   `Iterable` only requires `__iter__`, insufficient for indexing or length.
        -   `Collection` adds `__contains__` but lacks indexing/reversal support.
        -   `List` is a concrete class, not an abstract base class, and unnecessary since we only need sequence behavior.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Accepts integers and range strings: `CustomRange(1, "2-4", 5)` → `[1, 2, 3, 4, 5]`.
    -   Empty: `CustomRange()` → `[]`.
    -   E.g., `CustomRange("1-3", 4, "5-6")` → `[1, 2, 3, 4, 5, 6]`.
-   **Length**:
    -   `len(CustomRange("1-3"))` → `3` (for `[1, 2, 3]`).
    -   `len(CustomRange())` → `0`.
-   **Iteration**:
    -   `list(CustomRange(1, "2-3"))` → `[1, 2, 3]`.
-   **Reversed**:
    -   `list(reversed(CustomRange(1, "2-3")))` → `[3, 2, 1]`.
-   **Membership**:
    -   `2 in CustomRange("1-3")` → `True`.
    -   `4 in CustomRange("1-3")` → `False`.
-   **Indexing**:
    -   `cr = CustomRange("1-3"); cr[0]` → `1`; `cr[-1]` → `3`.
    -   Slicing: `cr[1:3]` → `[2, 3]`.
-   **Sequence Behavior**:
    -   Inherits `Sequence` methods: `cr.count(2)`, `cr.index(3)`, etc.
    -   E.g., `CustomRange("1-3").index(2)` → `1`.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**: Stores all numbers in a flat list, ensuring consistent iteration, indexing, and membership testing. `Sequence` provides robust defaults. No validation needed per requirements.
-   **Performance**:
    -   Initialization: O(n) for processing args (n is total numbers in ranges).
    -   `__len__`: O(1).
    -   `__getitem__`: O(1) for single index, O(k) for slice of length k.
    -   `__contains__`: O(n) worst-case for membership.
    -   `__reversed__`: O(1) to create iterator, O(n) to consume.
    -   Efficient for typical use cases.
-   **Design**:
    -   `Sequence` minimizes implementation effort by providing defaults.
    -   Flat list storage simplifies all operations.
    -   Type hints and docstrings enhance clarity.
    -   No additional attributes needed, keeping the design minimal.
-   **Extensibility**: Easily extended to support additional input types (e.g., tuples) or validation if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
cr = CustomRange(1, "2-4", 5)
cr2 = CustomRange("1-3")

# Test length
print(len(cr))  # 5
print(len(CustomRange()))  # 0

# Test iteration
print(list(cr))  # [1, 2, 3, 4, 5]

# Test reversed
print(list(reversed(cr2)))  # [3, 2, 1]

# Test membership
print(3 in cr)  # True
print(6 in cr)  # False

# Test indexing
print(cr[0])   # 1
print(cr[-1])  # 5
print(cr[1:4]) # [2, 3, 4]

# Test Sequence methods
print(cr.index(3))  # 2
print(cr.count(2))  # 1
```

## Conclusion 🚀

The `CustomRange` implementation is precise, providing a flexible sequence of integers from single numbers and ranges with full support for iteration, indexing, and Sequence protocol features.
Inheriting from `collections.abc.Sequence` ensures robust behavior with minimal code.
It’s ideal for range-based sequence tasks or sequence protocol education, fully compliant with the task’s requirements.
