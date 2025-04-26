# SortedList Class Implementation

## Description 📝

The provided code implements the `SortedList` class, a subclass of `collections.abc.Sequence`.
It represents a list that maintains its elements in sorted order upon creation and modification.
The class supports adding, removing, and updating elements while ensuring sort order, and provides iteration, indexing, membership testing, and arithmetic operations (`+`, `+=`, `*`, `*=`).
Certain list methods (`append`, `insert`, `extend`, `reverse`, `__setitem__`, `__reversed__`) raise `NotImplementedError` to enforce the sorted nature of the list.

## Purpose 🎯

Intended for scenarios requiring a dynamically maintained sorted list, such as priority queues, ranked data storage, or sorted collections in algorithms.
It’s also suitable for educational examples of sequence protocols, operator overloading, and efficient insertion in Python.

## Choice of Parent Class 🛠️

-   **Why `Sequence`?**:
    -   `collections.abc.Sequence` is ideal because `SortedList` is an ordered, indexable collection with a fixed length.
    -   Requires only `__len__` and `__getitem__`, which are straightforward to implement with an internal sorted list.
    -   Provides default implementations for `__iter__`, `__contains__`, and others, reducing code duplication.
    -   Alternatives considered:
        -   `Iterable`: Too minimal, lacks indexing or length support.
        -   `Collection`: Adds `__contains__` but not indexing.
        -   `List`: Concrete class, not abstract, and inappropriate for enforcing sorted behavior.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts an optional `iterable` (default `()`), converts it to a sorted list (`self._data`).
    -   Ensures independence by copying the iterable.
-   **Core Methods**:
    -   `add(obj)`: Inserts `obj` using `bisect.insort` to maintain sort order.
    -   `discard(obj)`: Removes all occurrences of `obj` by rebuilding the list.
    -   `update(iterable)`: Adds elements from `iterable` one-by-one using `bisect.insort`.
-   **Restricted Methods**:
    -   `append()`, `insert()`, `extend()`, `reverse()`: Raise `NotImplementedError`.
-   **Sequence Methods**:
    -   `__len__`: Returns length of `self._data`.
    -   `__getitem__(key)`: Returns element or slice from `self._data`.
    -   `__iter__`: Iterates over `self._data`.
    -   `__contains__(value)`: Checks if `value` is in `self._data`.
    -   `__delitem__(key)`: Deletes element or slice from `self._data`.
    -   `__setitem__(key, value)`: Raises `NotImplementedError` to prevent unsorted modifications.
    -   `__reversed__`: Raises `NotImplementedError` to enforce sorted order.
-   **String Representation**:
    -   `__repr__`: Returns `SortedList([...])` with the sorted elements.
-   **Arithmetic Operations**:
    -   `__add__(other)`: Concatenates with another `SortedList`, sorts, returns new `SortedList`. Returns `NotImplemented` for non-`SortedList`.
    -   `__iadd__(other)`: Updates `self` with elements from another `SortedList` via `update`, returns `self`. Returns `NotImplemented` for non-`SortedList`.
    -   `__mul__(n)`: Repeats `self._data` `n` times, sorts, returns new `SortedList`. Returns `NotImplemented` for non-`int`.
    -   `__imul__(n)`: Repeats `self._data` in-place, sorts, returns `self`. Returns `NotImplemented` for non-`int`.
-   **Behavior**:
    -   Maintains sorted order at all times.
    -   Iterable: Supports `for x in sorted_list`.
    -   Length: `len(sorted_list)` returns element count.
    -   Membership: `x in sorted_list` checks presence.
    -   Indexing: Supports `sorted_list[i]` (positive/negative) and slicing.
    -   Deletion: Supports `del sorted_list[i]` or `del sorted_list[i:j]`.
    -   Independent: Copies input iterable to `self._data`.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   `SortedList([3, 1, 2])` → `[1, 2, 3]`.
    -   `SortedList()` → `[]`.
    -   Independent: `lst = [1, 2]; sl = SortedList(lst); lst[0] = 3; print(sl)` → `[1, 2]`.
-   **Core Methods**:
    -   `add`: `sl = SortedList([1, 3]); sl.add(2)` → `[1, 2, 3]`.
    -   `discard`: `sl = SortedList([1, 2, 2, 3]); sl.discard(2)` → `[1, 3]`.
    -   `update`: `sl = SortedList([1, 3]); sl.update([2, 4])` → `[1, 2, 3, 4]`.
-   **Restricted Methods**:
    -   `sl.append(1)`, `sl.insert(0, 1)`, `sl.extend([1])`, `sl.reverse()` raise `NotImplementedError`.
-   **String Representation**:
    -   `repr(SortedList([1, 2, 3]))` → `SortedList([1, 2, 3])`.
-   **Length**:
    -   `len(SortedList([1, 2]))` → `2`.
    -   `len(SortedList())` → `0`.
-   **Iteration**:
    -   `list(SortedList([1, 2, 3]))` → `[1, 2, 3]`.
-   **Reversed**:
    -   `reversed(SortedList([1, 2]))` raises `NotImplementedError`.
-   **Membership**:
    -   `2 in SortedList([1, 2, 3])` → `True`.
    -   `4 in SortedList([1, 2, 3])` → `False`.
-   **Indexing**:
    -   `sl = SortedList([1, 2, 3]); sl[0]` → `1`; `sl[-1]` → `3`.
    -   Slicing: `sl[1:3]` → `[2, 3]`.
-   **Deletion**:
    -   `sl = SortedList([1, 2, 3]); del sl[1]; print(sl)` → `[1, 3]`.
    -   `del sl[0:2]; print(sl)` → `[]`.
-   **Setitem**:
    -   `sl[0] = 4` raises `NotImplementedError`.
-   **Arithmetic Operations**:
    -   `SortedList([1, 3]) + SortedList([2, 4])` → `SortedList([1, 2, 3, 4])`.
    -   `sl = SortedList([1, 2]); sl += SortedList([3, 4])` → `[1, 2, 3, 4]`.
    -   `SortedList([1, 2]) * 2` → `SortedList([1, 1, 2, 2])`.
    -   `sl = SortedList([1, 2]); sl *= 2` → `[1, 1, 2, 2]`.
    -   Invalid: `SortedList([1]) + [2]`, `SortedList([1]) * "2"` return `NotImplemented`.
-   **Sequence Behavior**:
    -   Inherits `Sequence` methods: `sl.count(1)`, `sl.index(2)`.
    -   E.g., `SortedList([1, 1, 2]).count(1)` → `2`.
-   **Documentation**: Clear docstrings with type hints.

## Performance Optimization 🛠️

-   **Efficient Insertion**:
    -   Uses `bisect.insort` for `add` and `update`, which performs binary insertion in O(log n) for finding the position and O(n) for shifting elements, totaling O(n) per insertion.
    -   This is faster than sorting after each addition (O(n log n)).
    -   Alternative (e.g., heap or balanced tree) could improve insertion to O(log n), but `bisect` is simpler and sufficient for typical use cases.
-   **Other Operations**:
    -   `__len__`, `__getitem__`: O(1) for index, O(k) for slice of length k.
    -   `__contains__`: O(n) worst-case (linear search; could be O(log n) with binary search but not implemented for simplicity).
    -   `discard`: O(n) for filtering.
    -   Arithmetic operations: O(n log n) due to sorting concatenated or multiplied lists.
    -   Deletion: O(n) for shifting elements after deletion.
-   **Trade-offs**:
    -   List-based storage is simple and leverages `bisect` for efficient insertion.
    -   More complex structures (e.g., BST) could optimize insertion but increase code complexity and overhead for small lists.

## Potential Considerations 🛠️

-   **Correctness**:
    -   Maintains sorted order via `bisect.insort` and sorting in `__init__`, `__mul__`, `__imul__`.
    -   `Sequence` provides robust defaults for iteration and membership.
    -   `NotImplementedError` enforces sorted constraints.
    -   `NotImplemented` handles invalid operands for arithmetic operations.
    -   No validation needed per requirements (assumes comparable elements).
-   **Design**:
    -   `Sequence` minimizes implementation effort.
    -   List storage with `bisect` balances simplicity and insertion efficiency.
    -   `NotImplemented` follows Python’s operator protocol.
    -   Type hints and docstrings enhance clarity.
-   **Extensibility**:
    -   Easily extended for additional operations (e.g., custom comparators) or validation.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
sl = SortedList([3, 1, 2])
sl2 = SortedList([4, 5])

# Test representation
print(sl)  # SortedList([1, 2, 3])

# Test core methods
sl.add(4)
print(sl)  # SortedList([1, 2, 3, 4])
sl.discard(2)
print(sl)  # SortedList([1, 3, 4])
sl.update([2, 5])
print(sl)  # SortedList([1, 2, 3, 4, 5])

# Test restricted methods
try:
    sl.append(1)
except NotImplementedError:
    print("append not implemented")

# Test length
print(len(sl))  # 5

# Test iteration
print(list(sl))  # [1, 2, 3, 4, 5]

# Test membership
print(3 in sl)  # True

# Test indexing
print(sl[0])   # 1
print(sl[-1])  # 5
print(sl[1:3]) # [2, 3]

# Test deletion
del sl[1]
print(sl)  # SortedList([1, 3, 4, 5])

# Test setitem
try:
    sl[0] = 2
except NotImplementedError:
    print("setitem not implemented")

# Test arithmetic
print(sl + sl2)  # SortedList([1, 3, 4, 4, 5, 5])
sl += sl2
print(sl)  # SortedList([1, 3, 4, 4, 5, 5])
print(sl * 2)  # SortedList([1, 1, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])
sl *= 2
print(sl)  # SortedList([1, 1, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])

# Test invalid operations
print(sl + [1])  # NotImplemented
```

## Conclusion 🚀

The `SortedList` implementation is precise, maintaining a sorted list with efficient insertion via `bisect` and supporting all required operations.
Inheriting from `collections.abc.Sequence` ensures robust sequence behavior with minimal code.
It’s ideal for sorted collection tasks or sequence protocol education, fully compliant with the task’s requirements.
