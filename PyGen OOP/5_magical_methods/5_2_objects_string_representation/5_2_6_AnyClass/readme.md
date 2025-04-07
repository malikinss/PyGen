# AnyClass Class Flexible Descriptor

## Description 📝

The `AnyClass` class dynamically accepts any number of named arguments during instantiation, setting them as instance attributes.
It provides a formal string representation via `__repr__` as `AnyClass(<key>=<value>, ...)` and an informal one via `__str__` as `AnyClass: <key>=<value>, ...`, with string values enclosed in single quotes.

## Purpose 🎯

This class is designed for creating objects with arbitrary attributes, suitable for prototyping, educational examples of dynamic attribute handling, or applications needing flexible data structures.

## How It Works 🔍

-   **Initialization**: The `__init__` method uses `**kwargs` to accept named arguments and updates the instance’s `__dict__` with them.
-   **\_format_attrs() Method**: Helper that formats attributes into a comma-separated string, quoting string values.
-   ****repr**() Method**: Returns the formal string using the formatted attributes inside `AnyClass(...)`.
-   ****str**() Method**: Returns the informal string prefixed with `AnyClass: ` followed by the formatted attributes.

## Usage 📦

1. Save the class in a Python file, e.g., `any_class.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from any_class import AnyClass
obj = AnyClass(name="Alice", age=25, active=True)
print(obj)
print(repr(obj))
```

## Conclusion 🚀

The `AnyClass` class offers a versatile and dynamic way to create objects with custom attributes in Python, with clear and consistent string representations.
Its design is highly adaptable, making it a useful tool that can be extended with attribute validation or additional formatting options for more specific needs.
