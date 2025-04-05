# Processor Class Type Handler

## Description 📝

The `Processor` class provides a static method `process()` for converting objects based on their type, reimplemented using the `@singledispatchmethod` decorator.
It handles specific types (int/float, str, list, tuple) with tailored processing and raises a `TypeError` for unsupported types, requiring no instantiation arguments.

## Purpose 🎯

This class is designed for type-specific object processing, ideal for educational examples of single dispatch, data transformation utilities, or applications needing polymorphic behavior without subclassing.

## How It Works 🔍

-   **process() Method**: A `@singledispatchmethod` base that raises a `TypeError` for unsupported types.
-   **\_process_number() Method**: Registers with `@process.register` to double integers or floats.
-   **\_process_string() Method**: Registers to convert strings to uppercase.
-   **\_process_list() Method**: Registers to sort lists.
-   **\_process_tuple() Method**: Registers to sort tuples and return a new tuple.
-   All methods are `@staticmethod` for class-level access.

## Usage 📦

1. Save the class in a Python file, e.g., `processor.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from processor import Processor
print(Processor.process(5))
print(Processor.process("hello"))
print(Processor.process([3, 1, 2]))
print(Processor.process((2, 1, 3)))
```

## Conclusion 🚀

The `Processor` class leverages `@singledispatchmethod` to elegantly handle type-specific processing in Python, offering a clean alternative to traditional type checking.
Its static design and extensible dispatch system make it a versatile tool, easily adaptable for additional types or processing rules.
