# CyclicList Class Infinite Sequence Looper

## Description 📝

The `CyclicList` class implements a cyclic list that stores elements from an optional iterable provided during instantiation (defaulting to empty).
It supports adding elements with `append()`, removing elements with `pop()` (by index or last element), and querying length via `len()`.
The class is iterable, yielding elements infinitely in a cyclic manner, and allows cyclic indexing, where indices wrap around using modulo (e.g., index `4` in `[1, 2, 3]` accesses index `4 % 3 = 1`, yielding `2`).
It maintains an independent copy of the initial iterable and assumes non-negative indices.

## Purpose 🎯

This class is designed for applications requiring cyclic data access, such as round-robin scheduling, circular buffers, or game mechanics (e.g., cycling through player turns).
Its infinite iteration and cyclic indexing make it ideal for simulations, animations, or data streaming, while its independence from the source iterable ensures stability.
It’s also a great educational tool for teaching Python’s sequence and iterator protocols.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts an optional `iterable` (defaults to empty tuple `()`).
    -   Creates a new list `self._list` by converting `iterable` to a list, ensuring independence from the source (changes to the original iterable don’t affect the instance).
-   **Append Method (`append`)**:
    -   Adds the provided `obj` to the end of `self._list` using `list.append`, extending the cycle.
-   **Pop Method (`pop`)**:
    -   Accepts an optional index `id` (defaults to `None`).
    -   If `None`, calls `self._list.pop()` to remove and return the last element.
    -   Otherwise, uses `self._list.pop(id)` to remove and return the element at `id`.
    -   Raises `IndexError` if the list is empty or the index is invalid (though non-negative indices are guaranteed).
-   **Length (`__len__`)**:
    -   Returns `len(self._list)`, reflecting the current number of elements.
-   **Iteration (`__iter__`)**:
    -   If `self._list` is empty, returns immediately (yielding nothing).
    -   Otherwise, enters an infinite loop that yields each element in `self._list` using a for-loop, restarting from the beginning after the last element.
    -   Uses `yield` for efficient, lazy iteration.
-   **Indexing (`**getitem**)**:
    -   Takes a non-negative integer `key` (guaranteed valid).
    -   If `self._list` is empty, raises `IndexError("CyclicList is empty")`.
    -   Computes the cyclic index with `key % len(self._list)` to wrap around, accessing `self._list` at that index.
    -   Returns the corresponding element, enabling cyclic access (e.g., `key=4` in `[1, 2, 3]` maps to index `1`).

## Verification ✅

Your implementation is correct and robust:

-   **Initialization**: `c = CyclicList([1, 2, 3])` creates `[1, 2, 3]`; `CyclicList()` is empty.
-   **Append**: `c.append(4)` makes `[1, 2, 3, 4]`.
-   **Pop**: `c.pop() == 4`; `c.pop(0) == 1`; list becomes `[2, 3]`.
-   **Length**: `len(c) == 2`.
-   **Iteration**: `iter(c)` yields `2, 3, 2, 3, ...` infinitely; empty list yields nothing.
-   **Indexing**: `c[0] == 2`, `c[2] == 2`, `c[3] == 3` (cyclic).
-   **Independence**: Changes to the source iterable don’t affect `c`.

## Potential Considerations 🛠️

-   **Efficiency**: List storage is O(1) for append/pop/indexing; modulo indexing is O(1); iteration is O(n) per cycle.
-   **Edge Cases**: Handles empty lists robustly; non-negative indices guaranteed.
-   **Iteration Stop**: Infinite iteration suits the task, but users must break loops manually (e.g., with `break` or `next()`).

## Usage Example (For Clarity, Not Submission) 📦

```python
c = CyclicList([1, 2, 3])
print(len(c))      # 3
print(c[4])        # 2
c.append(4)
print(list(itertools.islice(c, 5)))  # [1, 2, 3, 4, 1]
print(c.pop())     # 4
print(c[0])        # 1
```

## Conclusion 🚀

Your `CyclicList` implementation is excellent, providing a robust cyclic list with infinite iteration and modular indexing.
Its independent storage, efficient methods, and clear handling of edge cases make it ideal for cyclic data tasks or teaching Python protocols.
Fully meeting the task’s requirements, it’s ready for scheduling, buffering, or educational use. Extensions like negative index support aren’t needed but could be considered.
