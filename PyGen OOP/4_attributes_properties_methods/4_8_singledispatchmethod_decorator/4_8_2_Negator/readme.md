# Negator Class Value Inverter

## Description 📝

The `Negator` class provides a static method `neg()` to invert the value of an object based on its type, requiring no instantiation arguments.
It negates numbers by changing their sign, flips boolean values, and raises a `TypeError` for unsupported types, implemented using the `@singledispatchmethod` decorator.

## Purpose 🎯

This class is designed for simple value negation, suitable for educational examples of type dispatching, logical operations, or utilities needing basic inversion functionality.

## How It Works 🔍

-   **neg() Method**: A `@singledispatchmethod` base that raises a `TypeError` for unsupported types.
-   **\_neg_number() Method**: Registers with `@neg.register` to negate integers or floats by multiplying by -1.
-   **\_neg_boolean() Method**: Registers to invert boolean values using the `not` operator.
-   All methods are `@staticmethod` for direct class access.

## Usage 📦

1. Save the class in a Python file, e.g., `negator.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from negator import Negator
print(Negator.neg(5))
print(Negator.neg(-3.14))
print(Negator.neg(True))
```

## Conclusion 🚀

The `Negator` class offers a concise and type-safe way to invert values in Python, leveraging single dispatch for clarity and extensibility.
Its static design makes it a lightweight utility, easily expandable to handle additional types or custom negation rules.
