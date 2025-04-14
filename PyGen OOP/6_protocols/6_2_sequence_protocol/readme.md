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

3.

```

```

4.

```

```

5.

```

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
