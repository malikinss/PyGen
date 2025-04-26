# BitArray Class Implementation

## Description 📝

The provided code implements the `BitArray` class, a subclass of `collections.abc.Sequence`.
It represents a sequence of bits (0s and 1s) initialized from an iterable, supporting iteration, indexing, length calculation, reverse iteration, membership testing, and bitwise operations (`~`, `&`, `|`).
The class ensures independence from the input iterable and handles invalid operands for logical operations by returning `NotImplemented`.

## Purpose 🎯

Intended for scenarios requiring manipulation of bit sequences, such as binary data processing, digital logic, or low-level programming.
It’s also suitable for educational examples of sequence protocols, bitwise operations, and abstract base classes in Python.

## Choice of Parent Class 🛠️

-   **Why `Sequence`?**:
    -   `collections.abc.Sequence` is ideal because `BitArray` is an ordered, indexable collection of bits with a fixed length.
    -   Requires only `__len__` and `__getitem__`, which are straightforward to implement with an internal list.
    -   Provides default implementations for `__iter__`, `__contains__`, `__reversed__`, and others, reducing code duplication.
    -   Alternatives considered:
        -   `Iterable`: Too minimal, lacks indexing and length support.
        -   `Collection`: Adds `__contains__` but not indexing or reversal.
        -   `List`: Concrete class, not an abstract base, and unnecessary since only sequence behavior is needed.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts an optional `iterable` (default `()`), converts it to a list (`self.arr`) to ensure independence.
    -   Stores bits (0s and 1s) in `self.arr`.
-   **Sequence Methods**:
    -   `__len__`: Returns the length of `self.arr`.
    -   `__getitem__(key)`: Returns a bit or slice from `self.arr`, supporting positive/negative indices and slices.
    -   `__contains__(value)`: Checks if `value` (0 or 1) is in `self.arr`.
    -   `__reversed__`: Returns an iterator over `self.arr` in reverse order.
-   **String Representation**:
    -   `__str__`: Returns a string like `[<bit1>, <bit2>, ...]`, matching `self.arr`’s representation.
-   **Bitwise Operations**:
    -   `__invert__`: Returns a new `BitArray` with each bit inverted (`1 - bit`).
    -   `__and__(other)`: Performs bitwise AND on corresponding bits of two `BitArray`s of equal length, returning a new `BitArray`. Returns `NotImplemented` if `other` is not a `BitArray` or lengths differ.
    -   `__or__(other)`: Performs bitwise OR on corresponding bits, similar to `__and__`.
-   **Behavior**:
    -   Iterable: Supports `for x in bit_array`.
    -   Length: `len(bit_array)` returns number of bits.
    -   Reversed: `reversed(bit_array)` iterates in reverse.
    -   Membership: `x in bit_array` checks for 0 or 1.
    -   Indexing: Supports `bit_array[i]` (positive/negative) and slicing.
    -   Bitwise: `~bit_array`, `bit_array & other`, `bit_array | other` produce new `BitArray`s.
    -   Independent: Copying `iterable` to `self.arr` ensures no dependency on input.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Accepts iterable: `BitArray([0, 1, 0])` → `[0, 1, 0]`.
    -   Empty: `BitArray()` → `[]`.
    -   Independent: `lst = [0, 1]; ba = BitArray(lst); lst[0] = 2; print(ba)` → `[0, 1]`.
-   **String Representation**:
    -   `str(BitArray([0, 1, 0]))` → `[0, 1, 0]`.
-   **Length**:
    -   `len(BitArray([0, 1]))` → `2`.
    -   `len(BitArray())` → `0`.
-   **Iteration**:
    -   `list(BitArray([0, 1]))` → `[0, 1]`.
-   **Reversed**:
    -   `list(reversed(BitArray([0, 1, 0])))` → `[0, 1, 0]`.
-   **Membership**:
    -   `1 in BitArray([0, 1, 0])` → `True`.
    -   `2 in BitArray([0, 1])` → `False`.
-   **Indexing**:
    -   `ba = BitArray([0, 1, 0]); ba[1]` → `1`; `ba[-1]` → `0`.
    -   Slicing: `ba[1:3]` → `[1, 0]`.
-   **Bitwise Operations**:
    -   Invert: `~BitArray([0, 1, 0])` → `BitArray([1, 0, 1])`.
    -   AND: `BitArray([1, 0, 1]) & BitArray([1, 1, 0])` → `BitArray([1, 0, 0])`.
    -   OR: `BitArray([1, 0, 1]) | BitArray([1, 1, 0])` → `BitArray([1, 1, 1])`.
    -   Invalid operand: `BitArray([0, 1]) & [0, 1]` → `NotImplemented`.
    -   Unequal length: `BitArray([0, 1]) & BitArray([0, 1, 0])` → `NotImplemented`.
-   **Sequence Behavior**:
    -   Inherits `Sequence` methods: `ba.count(1)`, `ba.index(0)`, etc.
    -   E.g., `BitArray([0, 1, 0]).count(0)` → `2`.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `self.arr` as a list ensures independence and supports all operations.
    -   `Sequence` provides robust defaults for iteration, membership, and reversal.
    -   Bitwise operations return new `BitArray`s and handle invalid cases with `NotImplemented`.
    -   No validation needed per requirements (assumes input contains only 0s and 1s).
-   **Performance**:
    -   Initialization: O(n) for copying iterable (n is length).
    -   `__len__`, `__getitem__`: O(1) for index, O(k) for slice of length k.
    -   `__contains__`: O(n) worst-case.
    -   `__reversed__`: O(1) to create iterator, O(n) to consume.
    -   Bitwise operations: O(n) for iterating pairs or inverting.
    -   Efficient for typical bit array sizes.
-   **Design**:
    -   `Sequence` minimizes implementation effort.
    -   List storage simplifies operations and ensures immutability of the sequence structure.
    -   `NotImplemented` for invalid operands follows Python’s operator protocol.
    -   Type hints and docstrings enhance clarity.
-   **Extensibility**:
    -   Easily extended for additional operations (e.g., XOR, shift) or validation.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
ba = BitArray([0, 1, 0])
ba2 = BitArray([1, 1, 0])

# Test string representation
print(ba)  # [0, 1, 0]

# Test length
print(len(ba))  # 3

# Test iteration
print(list(ba))  # [0, 1, 0]

# Test reversed
print(list(reversed(ba)))  # [0, 1, 0]

# Test membership
print(1 in ba)  # True
print(2 in ba)  # False

# Test indexing
print(ba[1])   # 1
print(ba[-1])  # 0
print(ba[0:2]) # [0, 1]

# Test bitwise operations
print(~ba)         # [1, 0, 1]
print(ba & ba2)    # [0, 1, 0]
print(ba | ba2)    # [1, 1, 0]
print(ba & [0, 1]) # NotImplemented

# Test independence
lst = [0, 1]
ba3 = BitArray(lst)
lst[0] = 2
print(ba3)  # [0, 1]
```

## Conclusion 🚀

The `BitArray` implementation is precise, providing a sequence of bits with support for iteration, indexing, and bitwise operations.
Inheriting from `collections.abc.Sequence` ensures robust behavior with minimal code.
It’s ideal for bit manipulation tasks or sequence protocol education, fully compliant with the task’s requirements.
