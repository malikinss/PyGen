# Formatter Class Type Printer

## Description 📝

The `Formatter` class provides a static method `format()` to display information about objects of type `int`, `float`, `list`, `tuple`, or `dict`, requiring no instantiation arguments.
It uses the `@singledispatchmethod` decorator to handle type-specific formatting, enclosing string elements in apostrophes, and raises a `TypeError` for unsupported types.

## Purpose 🎯

This class is designed for formatted output of common data types, suitable for debugging, educational examples of type dispatching, or applications needing consistent object representation.

## How It Works 🔍

-   **format() Method**: A `@singledispatchmethod` base that raises a `TypeError` for unsupported types.
-   **\_format_int() Method**: Prints integers as `"Integer: <value>"`.
-   **\_format_float() Method**: Prints floats as `"Float: <value>"`.
-   **\_format_list() Method**: Prints lists as `"List: <elements>"`, with elements formatted by `_format_list_or_tuple()`.
-   **\_format_tuple() Method**: Prints tuples as `"Tuple: <elements>"`, using `_format_list_or_tuple()`.
-   **\_format_dict() Method**: Prints dictionaries as `"Dict: (key, value), ..."`, formatting keys and values.
-   **Helper Methods**: `_format_value()` adds apostrophes to strings; `_format_list_or_tuple()` formats list/tuple elements.
-   All methods are `@staticmethod` for class-level use.

## Usage 📦

1. Save the class in a Python file, e.g., `formatter.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from formatter import Formatter
Formatter.format(42)
Formatter.format(3.14)
Formatter.format(["a", 1, 2.5])
Formatter.format(("b", 2))
Formatter.format({"x": 1, "y": "z"})
```

## Conclusion 🚀

The `Formatter` class offers a clean and type-specific way to print object details in Python, using single dispatch for extensibility.
Its static design and helper methods ensure consistent formatting, making it a handy tool that can be expanded to support additional types or custom output styles.
