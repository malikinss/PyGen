# Filter Class Iterable Sifter

## Description 📝

The `Filter` class creates callable instances that filter elements from an iterable based on a predicate function, defaulting to `bool()` if no predicate is provided.
When called with an iterable, it returns a list of elements where the predicate evaluates to `True`.

## Purpose 🎯

This class is designed for data filtering, suitable for list processing, educational examples of callable objects, or applications needing custom iterable refinement.

## How It Works 🔍

-   **Initialization**: Stores the `predicate`, using `bool` if `None` is passed.
-   **`__call__`()**: Makes instances callable, using a list comprehension to return elements from the `iterable` where `self.predicate(element)` is `True`.

## Usage 📦

1. Save the class in a Python file, e.g., `filter.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from filter import Filter
is_positive = Filter(lambda x: x > 0)
truthy = Filter(None)
print(is_positive([-2, 0, 1, 3]))      # [1, 3]
print(truthy([0, 1, "", "hello"]))     # [1, "hello"]
print(is_positive(range(-1, 5)))       # [0, 1, 2, 3, 4]
```

## Conclusion 🚀

The `Filter` class provides a flexible and concise way to filter iterables in Python, leveraging callable objects for reusability.
Its design is efficient and can be extended with features like iterator output or multiple predicates for more complex filtering tasks.
