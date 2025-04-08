# Money Class Ruble Manager

## Description 📝

The `Money` class represents a monetary amount in rubles, initialized with a given value.
It provides an informal string representation via `__str__` as `<amount> rubles` and supports unary operators: `+` (via `__pos__`) for a non-negative amount and `-` (via `__neg__`) for a negative amount, each returning a new instance.

## Purpose 🎯

This class is designed for simple monetary representation and manipulation, suitable for financial examples, educational demonstrations of unary operators, or applications needing basic money handling.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `amount` attribute from the provided value.
-   ****str**() Method**: Returns the amount followed by " rubles" as the informal representation.
-   ****pos**() Method**: Implements unary `+`, returning a new `Money` instance with the absolute value of `amount`.
-   ****neg**() Method**: Implements unary `-`, returning a new `Money` instance with the negated absolute value of `amount`.

## Usage 📦

1. Save the class in a Python file, e.g., `money.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from money import Money
m = Money(-50.75)
print(m)
positive_m = +m
negative_m = -m
print(positive_m)
print(negative_m)
```

## Conclusion 🚀

The `Money` class provides a clean and intuitive way to represent and manipulate monetary amounts in rubles in Python, with unary operators for sign control.
Its straightforward design makes it a flexible tool, easily extensible with arithmetic operations or currency formatting for more complex financial applications.
