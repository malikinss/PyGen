# Peekable Class Enhanced Look-Ahead Iterator

## Description 📝

The `Peekable` class implements an iterator that yields elements from a provided iterable in their original order, raising `StopIteration` when exhausted.
It accepts a single `iterable` argument during instantiation and adheres to the iterator protocol with `__iter__` and `__next__`.
The class includes a `peek()` method that previews the next element without advancing the iterator, returning a `default` value if specified when empty, or raising `StopIteration` otherwise.
This version uses a sentinel to distinguish between explicit `None` defaults and no default, offering a nuanced approach to handling exhaustion.

## Purpose 🎯

This class is perfect for applications needing to inspect upcoming elements without consuming them, such as in parsers (e.g., lexical analysis), event queues, or data stream processing.
Its lookahead capability enhances control in algorithms like predictive modeling or UI event handling, and it serves as an excellent educational example for Python’s iterator protocol, state management, and sentinel-based default handling in custom iterators.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Converts the input `iterable` to an iterator (`iter(iterable)`) and stores it in `self._iterator`.
    -   Initializes `self._next_item` to hold the next element and `self._has_item` as a boolean flag indicating availability.
    -   Attempts to prefetch the first element with `next(self._iterator)`, setting `self._next_item` and `self._has_item = True` on success, or `self._has_item = False` if `StopIteration` indicates an empty iterable.
-   **Iterator Protocol (`__iter__`)**:
    -   Returns `self`, enabling the instance to act as its own iterator for use in loops or iterator functions.
-   **Next Element (`__next__`)**:
    -   Checks `self._has_item`. If `False`, raises `StopIteration`.
    -   Stores `self._next_item` as the result to return.
    -   Attempts to fetch the next element into `self._next_item`, updating `self._has_item = False` and clearing `self._next_item` if `StopIteration` is raised.
    -   Returns the result, advancing the iterator’s state.
-   **Peek Method (`peek`)**:
    -   Accepts an optional `default` parameter, defaulting to a unique `_SENTINEL` object defined at the class level to distinguish between explicit `None` and no default.
    -   If `self._has_item` is `True`, returns `self._next_item` without altering the iterator.
    -   If exhausted (`self._has_item = False`):
    -   Returns `default` if it’s not the sentinel (i.e., a user-provided value, including `None`).
    -   Raises `StopIteration` if `default` is the sentinel (no default provided).
-   **Sentinel Usage**: The `_SENTINEL` ensures that `peek(default=None)` returns `None` explicitly, while `peek()` without arguments raises `StopIteration`, providing precise control over exhaustion behavior.

## Verification ✅

Your implementation is robust and correct:

-   Yields elements in order: `Peekable([1, 2, 3])` gives `1, 2, 3`.
-   Supports peeking: `p = Peekable([1]); p.peek() == 1; next(p) == 1`.
-   Handles defaults: `p = Peekable([]); p.peek(default=0) == 0; p.peek(default=None) == None`.
-   Raises `StopIteration` correctly: `p = Peekable([]); p.peek()` raises it.
-   Manages empty iterables and maintains iterator protocol seamlessly.

## Comparison with Previous Submission 🔄

This version differs from your earlier `Peekable` submission by:

-   Using a `_SENTINEL` object for default handling instead of `None`, allowing explicit `None` as a valid default value without ambiguity.
-   Simplifying `peek()` logic by checking `self._has_item` first, reducing conditional nesting.
-   Renaming `_has_next` to `_has_item` for clarity, aligning with the stored item’s context.
    Both are correct, but this version offers a slight edge in handling `default=None` explicitly and has a more streamlined `peek()` implementation.

## Potential Considerations 🛠️

-   **Efficiency**: Prefetching one element minimizes overhead, and the sentinel approach avoids complex default checks.
-   **Edge Cases**: Handles empty iterables, `None` defaults, and exhaustion robustly, as guaranteed by valid data.
-   **Clarity**: The sentinel pattern is a Pythonic way to differentiate defaults, though it adds minimal complexity compared to the previous version’s direct `None` check.

## Usage Example (For Clarity, Not Submission) 📦

```python
p = Peekable([1, 2])
print(p.peek())       # 1
print(next(p))        # 1
print(p.peek(0))      # 2
print(list(p))        # [2]
p = Peekable([])
print(p.peek(default=-1))  # -1
```

## Conclusion 🚀

Your `Peekable` implementation is excellent, offering a clean, efficient iterator with robust lookahead via `peek()`.
The sentinel-based default handling adds precision, distinguishing explicit `None` defaults, while the prefetching logic ensures minimal overhead.
It’s ideal for parsing, streaming, or teaching iterator design, fully meeting the task’s requirements with a slight refinement over the previous version.
Ready to enhance any project needing peekable iteration!
If you have more tasks or want further refinements, I’m here!
