Lesson 6.2: Sequence Protocol

Magic Method **len**()
Magic Methods **getitem**(), **setitem**() and **delitem**()
Magic Method **contains**()
Abstract: The lesson is about sequence protocol.

https://stepik.org/lesson/805785/step/1?unit=816644

This lesson has good theory explonation, has 9 programing practical tasks and 8 theoretical questions presented on the website.

1. 6_2_1_ReversedSequence

```
# ReversedSequence Class Backward Sequence Accessor
The `ReversedSequence` class provides a view into a sequence that accesses its elements in reverse order.
It accepts a single `sequence` argument during instantiation, supports length queries via `len()`, iterates over elements in reverse, and allows indexing where index `0` maps to the last element, `1` to the penultimate, and so on.
The class maintains a live dependency on the original sequence, reflecting any changes to it, and assumes non-negative indices as guaranteed.
This class is designed for applications needing reversed access to sequences without copying, such as parsing data backward, displaying lists in reverse, or processing time-series data in reverse chronological order.
Its live link to the original sequence makes it ideal for dynamic datasets in GUI applications, data analysis, or algorithms like reverse traversals, while also serving as an educational tool for teaching Python’s sequence protocol and dynamic referencing.
```

2. 6_2_2_SparseArray

```
# SparseArray Class Efficient Element Storage
The `SparseArray` class implements a sparse array that stores only non-default elements, using a dictionary to track defined indices and their values.
It accepts a single `default` argument during instantiation, which is returned for undefined indices.
The class supports getting and setting values via indexing (`arr[i]`), with non-negative indices guaranteed.
Setting a value equal to the default removes it from storage, optimizing memory usage, while accessing undefined indices returns the default value.
This class is designed for scenarios where most array elements are a default value, such as in numerical computations (e.g., sparse matrices in scientific computing), game development (e.g., maps with mostly empty tiles), or data processing with large datasets having few significant entries.
Its memory-efficient storage makes it ideal for big data applications, while also serving as an educational example for Python’s indexing protocol and dictionary-based data structures.
```

3. 6_2_3_CyclicList

```
# CyclicList Class Infinite Sequence Looper
The `CyclicList` class implements a cyclic list that stores elements from an optional iterable provided during instantiation (defaulting to empty).
It supports adding elements with `append()`, removing elements with `pop()` (by index or last element), and querying length via `len()`.
The class is iterable, yielding elements infinitely in a cyclic manner, and allows cyclic indexing, where indices wrap around using modulo (e.g., index `4` in `[1, 2, 3]` accesses index `4 % 3 = 1`, yielding `2`).
It maintains an independent copy of the initial iterable and assumes non-negative indices.
This class is designed for applications requiring cyclic data access, such as round-robin scheduling, circular buffers, or game mechanics (e.g., cycling through player turns).
Its infinite iteration and cyclic indexing make it ideal for simulations, animations, or data streaming, while its independence from the source iterable ensures stability.
It’s also a great educational tool for teaching Python’s sequence and iterator protocols.
```

4. 6_2_4_SequenceZip

```
# SequenceZip Class Tuple Combiner
The `SequenceZip` class creates a sequence of tuples by combining elements from multiple input sequences, akin to Python’s `zip()` function.
It accepts arbitrary positional arguments (sequences) during instantiation, stores independent copies, and supports length queries via `len()`, iteration over zipped tuples, and indexing to access tuples by position.
The class ensures independence from the original sequences, uses only non-negative indices as guaranteed, and provides a memory-efficient way to access combined elements.
This class is designed for tasks requiring synchronized access to multiple sequences, such as merging datasets, processing parallel lists (e.g., names and scores), or generating paired outputs in data processing, machine learning, or reporting.
Its independence and sequence-like interface make it ideal for static snapshots of zipped data, while also serving as an educational tool for teaching Python’s sequence protocol and zipping mechanics.
```

5. 6_2_5_OrderedSet

```
# OrderedSet Class Unique Element Sequencer
The `OrderedSet` class represents an ordered set that maintains the insertion order of unique elements.
It accepts an optional `iterable` during instantiation (defaulting to empty), ensures independence from the source, and provides methods `add()` (appends unique elements) and `discard()` (removes elements if present).
It supports length queries via `len()`, iteration, membership testing with `in`, and equality comparisons (`==`, `!=`) with both `OrderedSet` and `set` instances.
Comparisons with `OrderedSet` check for identical ordered elements, while with `set`, they verify equal elements regardless of order, returning `NotImplemented` for invalid comparisons.
This class is suited for applications needing a set-like structure with predictable order, such as tracking unique events in logs, maintaining ordered task lists, or deduplicating data while preserving sequence.
Its comparison flexibility makes it ideal for testing equivalence with unordered sets or ordered collections, and it’s a strong educational tool for teaching Python’s container protocols, comparison methods, and ordered data structures.
```

6.

```

```

7.

```

```

8.

```

```

9.

```

```
