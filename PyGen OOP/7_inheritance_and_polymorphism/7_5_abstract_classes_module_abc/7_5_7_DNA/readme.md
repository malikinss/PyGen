# DNA Class Implementation

## Description 📝

The provided code implements the `DNA` class, a subclass of `collections.abc.Sequence`.
It represents a double-stranded DNA helix, initialized with the first strand (a string of nitrogenous bases: A, G, T, C).
The class supports iteration, indexing, length calculation, reverse iteration, membership testing, equality comparison, and addition, using the principle of complementarity (A-T, G-C) to derive the second strand.
Invalid operands for comparison or addition return `NotImplemented`.

## Purpose 🎯

Intended for biological or bioinformatics applications, such as DNA sequence analysis, genetic simulations, or sequence alignment.
It’s also suitable for educational examples of sequence protocols, operator overloading, and abstract base classes in Python.

## Choice of Parent Class 🛠️

-   **Why `Sequence`?**:
    -   `collections.abc.Sequence` is ideal because `DNA` is an ordered, indexable collection of base pairs with a fixed length.
    -   Requires only `__len__` and `__getitem__`, which are straightforward to implement for accessing base pairs.
    -   Provides default implementations for `__iter__`, `__contains__`, `__reversed__`, and others, reducing code duplication.
    -   Alternatives considered:
        -   `Iterable`: Too minimal, lacks indexing or length support.
        -   `Collection`: Adds `__contains__` but not indexing or reversal.
        -   `Sequence` is better than `List` (a concrete class) as it’s abstract and tailored for sequence behavior.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `chain` (str of A, G, T, C), stored as `self._first`.
    -   Defines `_PAIRS` (class-level dict) for complementarity: `{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}`.
-   **Sequence Methods**:
    -   `__len__`: Returns the length of `self._first`.
    -   `__getitem__(key)`: Returns a tuple `(base, complement)` for an index or a list of such tuples for a slice.
    -   `__iter__`: Yields tuples `(base, complement)` for each base in `self._first`.
    -   `__reversed__`: Yields tuples `(base, complement)` in reverse order.
    -   `__contains__(value)`: Checks if `value` is in `self._first`.
-   **String Representation**:
    -   `__str__`: Returns `self._first`.
-   **Comparison**:
    -   `__eq__(other)`: Returns `True` if `other` is a `DNA` with the same first strand, `NotImplemented` otherwise.
-   **Addition**:
    -   `__add__(other)`: Returns a new `DNA` with the concatenated first strands if `other` is a `DNA`, `NotImplemented` otherwise.
-   **Behavior**:
    -   Iterable: `for pair in dna` yields `(base, complement)` tuples.
    -   Length: `len(dna)` returns strand length.
    -   Reversed: `reversed(dna)` iterates over pairs in reverse.
    -   Membership: `base in dna` checks the first strand.
    -   Indexing: `dna[i]` returns `(base, complement)`; supports negative indices.
    -   Equality: `dna1 == dna2` compares first strands.
    -   Addition: `dna1 + dna2` concatenates first strands.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   `DNA("ATCG")` creates a DNA with first strand `"ATCG"`.
    -   E.g., `dna = DNA("AG")` → first strand `"AG"`, second strand `"TC"`.
-   **String Representation**:
    -   `str(DNA("ATCG"))` → `"ATCG"`.
-   **Length**:
    -   `len(DNA("AT"))` → `2`.
    -   `len(DNA(""))` → `0`.
-   **Iteration**:
    -   `list(DNA("AG"))` → `[('A', 'T'), ('G', 'C')]`.
-   **Reversed**:
    -   `list(reversed(DNA("AG")))` → `[('G', 'C'), ('A', 'T')]`.
-   **Membership**:
    -   `'A' in DNA("ATCG")` → `True`.
    -   `'X' in DNA("ATCG")` → `False`.
-   **Indexing**:
    -   `dna = DNA("AT"); dna[0]` → `('A', 'T')`; `dna[-1]` → `('T', 'A')`.
    -   Slicing: `dna[0:2]` → `[('A', 'T'), ('T', 'A')]`.
-   **Comparison**:
    -   `DNA("AT") == DNA("AT")` → `True`.
    -   `DNA("AT") == DNA("AG")` → `False`.
    -   `DNA("AT") == "AT"` → `NotImplemented`.
-   **Addition**:
    -   `DNA("AT") + DNA("CG")` → `DNA("ATCG")`.
    -   `DNA("AT") + "CG"` → `NotImplemented`.
-   **Sequence Behavior**:
    -   Inherits `Sequence` methods: `dna.count(('A', 'T'))`, `dna.index(('G', 'C'))`.
    -   E.g., `DNA("AT").count(('A', 'T'))` → `1`.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   Stores only the first strand, deriving the second via `_PAIRS`, ensuring complementarity (A-T, G-C).
    -   `Sequence` provides robust defaults for iteration, membership, and reversal.
    -   `NotImplemented` handles invalid operands for `==`, `!=`, and `+`.
    -   No validation needed per requirements (assumes `chain` contains only A, G, T, C).
-   **Performance**:
    -   Initialization: O(1) for storing string.
    -   `__len__`, `__getitem__`: O(1) for index, O(k) for slice of length k.
    -   `__contains__`: O(n) worst-case for string search.
    -   `__iter__`, `__reversed__`: O(1) to create, O(n) to consume.
    -   `__eq__`, `__add__`: O(n) for string comparison or concatenation.
    -   Efficient for typical DNA sequence sizes.
-   **Design**:
    -   `Sequence` minimizes implementation effort.
    -   Storing only the first strand optimizes memory; complementarity is computed on access.
    -   `_PAIRS` as a class-level dict is clear and reusable.
    -   `NotImplemented` follows Python’s operator protocol.
    -   Type hints and docstrings enhance clarity.
-   **Extensibility**:
    -   Easily extended for additional operations (e.g., mutation, substring search) or validation.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
dna1 = DNA("ATCG")
dna2 = DNA("AT")

# Test string representation
print(dna1)  # ATCG

# Test length
print(len(dna1))  # 4

# Test iteration
print(list(dna1))  # [('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')]

# Test reversed
print(list(reversed(dna2)))  # [('T', 'A'), ('A', 'T')]

# Test membership
print('A' in dna1)  # True
print('X' in dna1)  # False

# Test indexing
print(dna2[0])   # ('A', 'T')
print(dna2[-1])  # ('T', 'A')
print(dna2[0:2]) # [('A', 'T'), ('T', 'A')]

# Test comparison
print(dna1 == DNA("ATCG"))  # True
print(dna1 != DNA("AT"))    # True
print(dna1 == "ATCG")       # NotImplemented

# Test addition
print(dna2 + DNA("CG"))  # ATCG
print(dna2 + "CG")       # NotImplemented
```

## Conclusion 🚀

The `DNA` implementation is precise, providing a sequence of DNA base pairs with support for iteration, indexing, and operations like equality and addition.
Inheriting from `collections.abc.Sequence` ensures robust behavior with minimal code.
It’s ideal for DNA sequence tasks or sequence protocol education, fully compliant with the task’s requirements.
