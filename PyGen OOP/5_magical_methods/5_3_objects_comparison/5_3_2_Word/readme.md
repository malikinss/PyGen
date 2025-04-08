# Word Class Length Comparator

## Description 📝

The `Word` class represents a sequence of Latin letters, initialized with a string argument.
It provides a formal string representation via `__repr__` as `Word('<word>')` and an informal one via `__str__` with the first letter uppercase and the rest lowercase.
Using `@total_ordering`, it supports all comparison operations (`==`, `!=`, `>`, `<`, `>=`, `<=`) based on word length, returning `NotImplemented` for invalid comparisons.

## Purpose 🎯

This class is designed for word representation and length-based comparison, suitable for text processing, educational examples of comparison operators, or applications needing ordered word lists.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `word` attribute.
-   ****repr**() Method**: Returns `Word('<word>')` for formal output.
-   ****str**() Method**: Returns the word capitalized (e.g., "Hello" for "hello").
-   ****eq**() Method**: Checks equality by comparing lengths of two `Word` instances.
-   ****lt**() Method**: Defines less-than by comparing lengths.
-   **@total_ordering**: Automatically generates `!=`, `>`, `>=`, and `<=` from `__eq__` and `__lt__`.
-   **Comparison Handling**: Returns `NotImplemented` for non-`Word` objects.

## Usage 📦

1. Save the class in a Python file, e.g., `word.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from word import Word
w1 = Word("cat")
w2 = Word("dog")
w3 = Word("bird")
print(w1)
print(repr(w2))
print(w1 == w2)
print(w1 < w3)
print(w2 >= w3)
```

## Conclusion 🚀

The `Word` class provides a clean and efficient way to represent and compare words by length in Python, leveraging `@total_ordering` for full comparison support.
Its design is flexible and can be extended with additional attributes or comparison criteria for more complex text analysis tasks.
