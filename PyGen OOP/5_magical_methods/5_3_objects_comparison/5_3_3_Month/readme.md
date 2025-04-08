# Month Class Date Comparator

## Description 📝

The `Month` class represents a month with a year and ordinal number, set during instantiation.
It provides a formal string representation via `__repr__` as `Month(<year>, <month>)` and an informal one via `__str__` as `<year>-<month>`.
Using `@total_ordering`, it supports all comparison operations (`==`, `!=`, `>`, `<`, `>=`, `<=`) based on year and month, handling both `Month` objects and 2-element tuples, returning `NotImplemented` for invalid comparisons.

## Purpose 🎯

This class is designed for month representation and chronological ordering, suitable for date management, educational examples of comparison logic, or applications needing sorted timelines.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets `year` and `month` attributes.
-   ****repr**() Method**: Returns `Month(<year>, <month>)` for formal output.
-   ****str**() Method**: Returns `<year>-<month>` for informal output.
-   ****eq**() Method**: Checks equality by matching both `year` and `month` with another `Month` or a 2-tuple.
-   ****gt**() Method**: Defines greater-than by comparing `year` first, then `month` if years are equal.
-   **@total_ordering**: Generates `!=`, `<`, `>=`, and `<=` from `__eq__` and `__gt__`.
-   **Comparison Handling**: Returns `NotImplemented` for non-`Month` or invalid tuple comparisons.

## Usage 📦

1. Save the class in a Python file, e.g., `month.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from month import Month
m1 = Month(2023, 5)
m2 = Month(2023, 6)
m3 = Month(2024, 1)
print(m1)
print(repr(m2))
print(m1 == Month(2023, 5))
print(m1 < m2)
print(m3 > (2023, 12))
```

## Conclusion 🚀

The `Month` class offers a robust way to represent and compare months in Python, with clear string outputs and comprehensive ordering based on year and month.
Its use of `@total_ordering` simplifies implementation, making it a flexible tool that can be extended with date validation or additional properties like month names.
