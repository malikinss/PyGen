# Queue Class FIFO Handler

## Description 📝

The `Queue` class implements a first-in-first-out (FIFO) data structure, accepting arbitrary elements during instantiation.
It offers methods to add (`add()`) and remove (`pop()`), an informal string representation, equality comparisons (`==`, `!=`), addition (`+` and `+=`), and right shift (`>>`) to drop initial elements, returning `NotImplemented` for invalid operations.

## Purpose 🎯

This class is designed for queue-based operations, suitable for task scheduling, educational examples of data structures, or applications needing ordered element processing.

## How It Works 🔍

-   **Initialization**: Stores elements in a list from `*args`.
-   **`__str__`()**: Joins elements with `->` for display.
-   **add()**: Appends elements to the end via `extend`.
-   **pop()**: Removes and returns the first element, or `None` if empty.
-   **`__eq__`()**: Compares element lists for equality.
-   **`__add__`()**: Creates a new `Queue` with concatenated elements.
-   **`__iadd__`()**: Extends `self.elements` in-place.
-   **`__rshift__`()**: Returns a new `Queue` sans the first `n` elements, empty if `n >= len`.
-   **Error Handling**: Returns `NotImplemented` for non-`Queue` or non-integer operands.

## Usage 📦

1. Save the class in a Python file, e.g., `queue.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from queue import Queue
q1 = Queue(1, 2, 3)
q2 = Queue(4, 5)
print(q1)          # 1 -> 2 -> 3
q1.add(6, 7)
print(q1.pop())    # 1
print(q1 + q2)     # 2 -> 3 -> 6 -> 7 -> 4 -> 5
q1 += q2
print(q1)          # 2 -> 3 -> 6 -> 7 -> 4 -> 5
print(q1 >> 2)     # 6 -> 7 -> 4 -> 5
print(q1 == Queue(2, 3, 6, 7, 4, 5))  # True
```

## Conclusion 🚀

The `Queue` class provides a robust FIFO implementation in Python, with intuitive operations for element management, comparison, and concatenation.
Its design is flexible, making it a strong base for adding features like size limits or iteration support for more advanced queueing systems.
