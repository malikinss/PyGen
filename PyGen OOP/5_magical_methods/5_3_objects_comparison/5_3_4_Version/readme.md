# Version Class Software Tracker

## Description 📝

The `Version` class represents a software version as a string of three integers separated by periods (e.g., '2.8.1'), padding omitted numbers with zeros.
It provides formal (`__repr__`) and informal (`__str__`) string representations and supports all comparison operations (`==`, `!=`, `>`, `<`, `>=`, `<=`) using `@total_ordering`, comparing versions hierarchically by their numbers, with `NotImplemented` for invalid comparisons.

## Purpose 🎯

This class is designed for version management, suitable for software development, educational examples of comparison logic, or applications needing version ordering.

## How It Works 🔍

-   **Initialization**: The `__init__` method parses the version string, splits it by periods, pads to three numbers with zeros, converts to a tuple of integers (`numbers`), and stores the normalized string (`version_str`).
-   ****repr**() Method**: Returns `Version('<x.y.z>')` for formal output.
-   ****str**() Method**: Returns `<x.y.z>` for informal output.
-   ****eq**() Method**: Checks equality by comparing the `numbers` tuples of two `Version` instances.
-   ****gt**() Method**: Defines greater-than by comparing `numbers` tuples lexicographically (first, second, third).
-   **@total_ordering**: Generates `!=`, `<`, `>=`, and `<=` from `__eq__` and `__gt__`.
-   **Comparison Handling**: Returns `NotImplemented` for non-`Version` objects.

## Usage 📦

1. Save the class in a Python file, e.g., `version.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from version import Version
v1 = Version("2.8.1")
v2 = Version("2.8")
v3 = Version("3.0.0")
print(v1)
print(repr(v2))
print(v1 == Version("2.8.1"))
print(v2 < v3)
print(v1 >= v2)
```

## Conclusion 🚀

The `Version` class provides a robust and intuitive way to manage software versions in Python, with normalized string handling and comprehensive comparison support.
Its use of `@total_ordering` simplifies implementation, making it a versatile tool that can be extended with validation or additional version components for more complex scenarios.
